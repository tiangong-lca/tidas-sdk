"""
AST-based code generator for Pydantic models.

Generates syntactically correct Python code from JSON schemas using
Python's ast module for proper structure and black for formatting.
"""

import ast
from typing import Any, Dict, List, Optional, Tuple

import black
from loguru import logger

from type_mapper import TypeMapper


class CodeGenerator:
    """Generates Pydantic model code using Python AST."""

    def __init__(self) -> None:
        """Initialize code generator with type mapper."""
        self.type_mapper = TypeMapper()

    def generate_model(
        self,
        model_name: str,
        properties: Dict[str, Any],
        required: List[str],
        description: str = "",
    ) -> str:
        """Generate a Pydantic model class from schema properties.

        Args:
            model_name: Name of the Pydantic model class
            properties: Schema properties dictionary
            required: List of required field names
            description: Model description (becomes docstring)

        Returns:
            Formatted Python code as string
        """
        # Reset type mapper for clean imports
        self.type_mapper.reset_imports()

        # Create module AST node
        module = ast.Module(body=[], type_ignores=[])

        # Add imports
        import_stmts = self._create_imports()
        module.body.extend(import_stmts)

        # Create class
        class_node = self._create_class(model_name, properties, required, description)
        module.body.append(class_node)

        # Fix missing locations (required for AST)
        ast.fix_missing_locations(module)

        # Convert to code
        code = ast.unparse(module)

        # Format with black
        try:
            formatted_code = black.format_str(code, mode=black.FileMode(line_length=100))
        except Exception as e:
            logger.warning(f"Black formatting failed: {e}, using unformatted code")
            formatted_code = code

        return formatted_code

    def _create_imports(self) -> List[ast.stmt]:
        """Create import statements for the module.

        Returns:
            List of AST import nodes
        """
        imports = []

        # Always include basic typing imports
        typing_names = ["Optional", "List", "Dict", "Any"]
        imports.append(
            ast.ImportFrom(
                module="typing",
                names=[ast.alias(name=name, asname=None) for name in typing_names],
                level=0,
            )
        )

        # Always include pydantic imports
        pydantic_names = ["BaseModel", "Field"]
        imports.append(
            ast.ImportFrom(
                module="pydantic",
                names=[ast.alias(name=name, asname=None) for name in pydantic_names],
                level=0,
            )
        )

        # UUID import
        imports.append(
            ast.ImportFrom(
                module="uuid",
                names=[ast.alias(name="UUID", asname=None)],
                level=0,
            )
        )

        # Datetime import
        imports.append(
            ast.ImportFrom(
                module="datetime",
                names=[ast.alias(name="datetime", asname=None)],
                level=0,
            )
        )

        return imports

    def _create_class(
        self,
        model_name: str,
        properties: Dict[str, Any],
        required: List[str],
        description: str,
    ) -> ast.ClassDef:
        """Create a Pydantic model class AST node.

        Args:
            model_name: Class name
            properties: Field definitions
            required: Required field names
            description: Class docstring

        Returns:
            ClassDef AST node
        """
        class_body = []

        # Add docstring if provided
        if description:
            docstring = ast.Expr(value=ast.Constant(value=description))
            class_body.append(docstring)

        # Add field definitions
        for field_name, field_schema in properties.items():
            field_node = self._create_field(field_name, field_schema, required)
            if field_node:
                class_body.append(field_node)

        # If no fields, add 'pass'
        if not class_body or (len(class_body) == 1 and isinstance(class_body[0], ast.Expr)):
            class_body.append(ast.Pass())

        # Create class
        class_node = ast.ClassDef(
            name=model_name,
            bases=[ast.Name(id="BaseModel", ctx=ast.Load())],
            keywords=[],
            body=class_body,
            decorator_list=[],
        )

        return class_node

    def _create_field(
        self, field_name: str, field_schema: Dict[str, Any], required: List[str]
    ) -> Optional[ast.AnnAssign]:
        """Create a field definition with type annotation.

        Args:
            field_name: Name of the field
            field_schema: JSON Schema for this field
            required: List of required field names

        Returns:
            AnnAssign AST node (annotated assignment) or None if skipped
        """
        # Get Python type
        python_type = self.type_mapper.map_type(field_schema, field_name)

        # Check if required
        is_required = self.type_mapper.is_required(field_name, required)

        # If not required and not already Optional, wrap in Optional
        if not is_required and not python_type.startswith("Optional["):
            python_type = f"Optional[{python_type}]"

        # Create type annotation (parse as expression)
        try:
            type_annotation = ast.parse(python_type, mode="eval").body
        except SyntaxError as e:
            logger.error(f"Invalid type annotation '{python_type}' for field '{field_name}': {e}")
            # Fallback to Any
            type_annotation = ast.Name(id="Any", ctx=ast.Load())

        # Get field constraints
        constraints = self.type_mapper.extract_field_constraints(field_schema)

        # Create field value
        field_value = None

        if constraints or field_name != field_name.replace(":", "_"):
            # Need Field() for constraints or aliases
            field_kwargs = []

            # Handle field name aliases (e.g., "common:UUID" -> alias="common:UUID")
            if ":" in field_name or "-" in field_name:
                # Field name needs sanitization
                constraints["alias"] = field_name

            for key, value in constraints.items():
                # Create keyword argument
                if isinstance(value, str):
                    value_node = ast.Constant(value=value)
                elif isinstance(value, (int, float, bool)):
                    value_node = ast.Constant(value=value)
                elif value is None:
                    value_node = ast.Constant(value=None)
                else:
                    value_node = ast.Constant(value=str(value))

                field_kwargs.append(ast.keyword(arg=key, value=value_node))

            # Add default=None for optional fields if no default specified
            if not is_required and "default" not in constraints:
                field_kwargs.append(
                    ast.keyword(arg="default", value=ast.Constant(value=None))
                )

            field_value = ast.Call(
                func=ast.Name(id="Field", ctx=ast.Load()),
                args=[],
                keywords=field_kwargs,
            )
        elif not is_required:
            # Optional field without constraints: field_name: Optional[Type] = None
            field_value = ast.Constant(value=None)

        # Sanitize field name for Python (replace : and - with _)
        python_field_name = field_name.replace(":", "_").replace("-", "_")

        # Create annotated assignment
        ann_assign = ast.AnnAssign(
            target=ast.Name(id=python_field_name, ctx=ast.Store()),
            annotation=type_annotation,
            value=field_value,
            simple=1,
        )

        return ann_assign

    def generate_file_header(self, schema_name: str) -> str:
        """Generate file header comment.

        Args:
            schema_name: Name of the schema

        Returns:
            Header comment string
        """
        return f'''"""
Generated Pydantic models from {schema_name}.json

DO NOT EDIT: This file is auto-generated.
Run scripts/generate_types.py to regenerate.
"""

'''

    def generate_module(
        self, schema_name: str, models: List[Dict[str, Any]]
    ) -> str:
        """Generate complete module with multiple models.

        Args:
            schema_name: Name of the schema
            models: List of model definitions, each with 'name', 'properties',
                   'required', and optionally 'description'

        Returns:
            Complete Python module code
        """
        code_parts = [self.generate_file_header(schema_name)]

        for model in models:
            model_code = self.generate_model(
                model["name"],
                model["properties"],
                model["required"],
                model.get("description", ""),
            )
            code_parts.append(model_code)
            code_parts.append("\n\n")

        return "".join(code_parts)

    def extract_nested_models(
        self, properties: Dict[str, Any], parent_name: str = ""
    ) -> List[Dict[str, Any]]:
        """Extract nested objects that should be separate models.

        Args:
            properties: Schema properties
            parent_name: Parent model name for naming nested models

        Returns:
            List of nested model definitions
        """
        nested_models = []

        for field_name, field_schema in properties.items():
            if self._is_nested_object(field_schema):
                # Create model name from field name
                if parent_name:
                    model_name = (
                        parent_name
                        + "".join(word.capitalize() for word in field_name.split("_"))
                    )
                else:
                    model_name = "".join(
                        word.capitalize() for word in field_name.split("_")
                    )

                nested_model = {
                    "name": model_name,
                    "properties": field_schema.get("properties", {}),
                    "required": field_schema.get("required", []),
                    "description": field_schema.get("description", ""),
                }

                nested_models.append(nested_model)

                # Recursively extract nested models
                sub_nested = self.extract_nested_models(
                    field_schema.get("properties", {}), model_name
                )
                nested_models.extend(sub_nested)

        return nested_models

    def _is_nested_object(self, field_schema: Dict[str, Any]) -> bool:
        """Check if field is a nested object requiring separate model.

        Args:
            field_schema: Field schema definition

        Returns:
            True if field should be a nested model
        """
        # Check if it's an object with properties
        if field_schema.get("type") != "object":
            return False

        properties = field_schema.get("properties", {})

        # Only create separate model if it has more than 3 properties
        # (threshold to avoid too many tiny models)
        return len(properties) > 3
