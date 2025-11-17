#!/usr/bin/env python3
"""
Generate Builder pattern classes for all TIDAS Pydantic models.

This script automatically generates builder classes that enable incremental construction
of complex nested TIDAS entities. Builders support:
- Property assignment (builder.field.nested_field = value)
- Multi-language helper methods (set_name(text, lang))
- Optional validation configuration
- Auto-initialization of nested builders
- Array field handling with add_*() methods
"""

import ast
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from loguru import logger


class BuilderGenerator:
    """Generate builder classes from Pydantic models."""

    # Multi-language field type names
    MULTI_LANG_TYPES = {"StringMultiLang", "STMultiLang", "FTMultiLang"}

    # Fields to skip in builders (non-data attributes)
    SKIP_FIELDS = {"model_config"}

    def __init__(self, types_dir: Path, schema_dir: Path):
        """Initialize builder generator.

        Args:
            types_dir: Directory containing generated Pydantic types
            schema_dir: Directory containing JSON schemas
        """
        self.types_dir = types_dir
        self.schema_dir = schema_dir
        self.schemas: Dict[str, Dict[str, Any]] = {}
        self.type_definitions: Dict[str, Dict[str, Any]] = {}

    def load_schema(self, schema_name: str) -> Dict[str, Any]:
        """Load a JSON schema file.

        Args:
            schema_name: Name of schema file (e.g., 'tidas_contacts')

        Returns:
            Parsed schema dictionary
        """
        schema_file = self.schema_dir / f"{schema_name}.json"
        if not schema_file.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_file}")

        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)

        self.schemas[schema_name] = schema
        return schema

    def parse_type_file(self, type_file: Path) -> Tuple[Dict[str, Dict[str, Any]], List[str]]:
        """Parse a generated Pydantic types file to extract class definitions and imports.

        Args:
            type_file: Path to types file

        Returns:
            Tuple of (class_definitions, import_lines)
        """
        with open(type_file, "r", encoding="utf-8") as f:
            content = f.read()
            tree = ast.parse(content)

        classes = {}
        import_statements = []

        # Extract import statements from AST
        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                if node.module:
                    import_statements.append({
                        'type': 'from',
                        'module': node.module,
                        'names': [alias.name for alias in node.names],
                    })
            elif isinstance(node, ast.Import):
                import_statements.append({
                    'type': 'import',
                    'names': [alias.name for alias in node.names],
                })

        # Extract classes
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Skip RootModel classes (they're type aliases)
                is_root_model = any(
                    isinstance(base, ast.Name) and base.id == "RootModel"
                    for base in node.bases
                )
                if is_root_model:
                    continue

                fields = self._extract_fields_from_class(node)
                if fields:  # Only include classes with fields
                    classes[node.name] = {
                        "fields": fields,
                        "docstring": ast.get_docstring(node),
                    }

        return classes, import_statements

    def _extract_fields_from_class(
        self, class_node: ast.ClassDef
    ) -> Dict[str, Dict[str, Any]]:
        """Extract field definitions from a class AST node.

        Args:
            class_node: AST node for the class

        Returns:
            Dictionary mapping field names to their type information
        """
        fields = {}

        for node in class_node.body:
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                field_name = node.target.id

                # Skip model_config and other special fields
                if field_name in self.SKIP_FIELDS:
                    continue

                # Extract type annotation
                type_str = self._annotation_to_string(node.annotation)

                # Check if this is a Field() call to get alias
                alias = None
                is_required = True
                if isinstance(node.value, ast.Call):
                    if isinstance(node.value.func, ast.Name) and node.value.func.id == "Field":
                        # Extract alias from Field call
                        for keyword in node.value.keywords:
                            if keyword.arg == "alias":
                                if isinstance(keyword.value, ast.Constant):
                                    alias = keyword.value.value
                        # Check if field is required (first positional arg is ...)
                        if node.value.args and isinstance(
                            node.value.args[0], ast.Constant
                        ):
                            if node.value.args[0].value == ...:
                                is_required = True
                            else:
                                is_required = False
                        elif not node.value.args:
                            is_required = False

                # Check if type is optional
                is_optional = " | None" in type_str or "None" in type_str

                # Determine if this is a nested object, array, or simple type
                field_info = {
                    "type": type_str,
                    "alias": alias,
                    "is_required": is_required,
                    "is_optional": is_optional,
                    "is_multi_lang": any(
                        ml_type in type_str for ml_type in self.MULTI_LANG_TYPES
                    ),
                    "is_list": type_str.startswith("list[") or type_str.startswith("List["),
                }

                fields[field_name] = field_info

        return fields

    def _annotation_to_string(self, annotation: ast.expr) -> str:
        """Convert AST annotation to type string.

        Args:
            annotation: AST annotation node

        Returns:
            Type as string
        """
        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Subscript):
            value = self._annotation_to_string(annotation.value)
            slice_str = self._annotation_to_string(annotation.slice)
            return f"{value}[{slice_str}]"
        elif isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
            left = self._annotation_to_string(annotation.left)
            right = self._annotation_to_string(annotation.right)
            return f"{left} | {right}"
        elif isinstance(annotation, ast.Constant):
            return repr(annotation.value)
        elif isinstance(annotation, ast.Tuple):
            elts = [self._annotation_to_string(elt) for elt in annotation.elts]
            return ", ".join(elts)
        else:
            return "Any"

    def _to_python_name(self, name: str) -> str:
        """Convert a field name to Python-safe property name.

        Args:
            name: Original field name (e.g., 'common_UUID', '@xmlns')

        Returns:
            Python-safe name
        """
        # Already converted by Pydantic generator (e.g., common_UUID)
        return name

    def _get_original_name(self, field_name: str, field_info: Dict[str, Any]) -> str:
        """Get the original field name (from alias or field name).

        Args:
            field_name: Python field name
            field_info: Field information dictionary

        Returns:
            Original field name for use in Pydantic model
        """
        return field_info.get("alias") or field_name

    def _is_nested_object(self, type_str: str, known_classes: Set[str]) -> bool:
        """Check if a type represents a nested object.

        Args:
            type_str: Type string
            known_classes: Set of known class names

        Returns:
            True if this is a nested object type
        """
        # Remove optional suffix
        base_type = type_str.replace(" | None", "").replace("None", "").strip(" |")

        # Check if it's a list
        if base_type.startswith("list[") or base_type.startswith("List["):
            # Extract inner type
            inner = base_type[base_type.index("[") + 1 : base_type.rindex("]")]
            base_type = inner

        # Check if it's a union of multiple types (excluding None)
        if " | " in base_type:
            # Could be a union of nested objects, check first one
            base_type = base_type.split(" | ")[0].strip()

        # Check if it's a known class (not a primitive or imported type)
        return base_type in known_classes

    def generate_builder_class(
        self,
        class_name: str,
        class_info: Dict[str, Any],
        known_classes: Set[str],
        indent: str = "",
    ) -> str:
        """Generate a builder class for a Pydantic model.

        Args:
            class_name: Name of the Pydantic class
            class_info: Class field information
            known_classes: Set of all known class names
            indent: Indentation string

        Returns:
            Generated builder class code
        """
        builder_name = f"{class_name}Builder"
        fields = class_info["fields"]
        docstring = class_info.get("docstring")

        lines = []

        # Class definition
        lines.append(f"{indent}class {builder_name}(BaseModel):")

        # Docstring with usage notes
        if docstring:
            lines.append(f'{indent}    """{docstring} (Builder)')
        else:
            lines.append(f'{indent}    """Builder for {class_name}.')

        # Add common usage notes for all builders
        lines.append(f'{indent}    ')
        lines.append(f'{indent}    Important:')
        lines.append(f'{indent}        - During construction, nested data is stored in private fields')
        lines.append(f'{indent}        - Calling model_dump() or model_dump_json() will NOT show nested builder state')
        lines.append(f'{indent}        - Always call build() to create the final model before serialization')
        lines.append(f'{indent}        - Use build_dump() for debugging to see full builder state during construction')
        lines.append(f'{indent}    ')
        lines.append(f'{indent}    Example:')
        lines.append(f'{indent}        builder = {builder_name}()')
        lines.append(f'{indent}        # Set fields...')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        # WRONG - returns empty or incomplete:')
        lines.append(f'{indent}        # json_str = builder.model_dump_json()')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        # CORRECT - build first, then serialize:')
        lines.append(f'{indent}        model = builder.build()')
        lines.append(f'{indent}        json_str = model.model_dump_json()')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        # For debugging during construction:')
        lines.append(f'{indent}        debug_json = builder.build_dump()')
        lines.append(f'{indent}    """')
        lines.append("")

        # Regular fields (non-nested, non-array)
        regular_fields = []
        nested_fields = []
        array_fields = []

        for field_name, field_info in fields.items():
            type_str = field_info["type"]
            is_list = field_info["is_list"]

            # Determine field category
            if is_list:
                inner_type = type_str[type_str.index("[") + 1 : type_str.rindex("]")]
                # Remove optional markers
                inner_type = inner_type.replace(" | None", "").strip()
                if self._is_nested_object(inner_type, known_classes):
                    array_fields.append((field_name, field_info, inner_type))
                else:
                    regular_fields.append((field_name, field_info))
            elif self._is_nested_object(type_str, known_classes):
                nested_fields.append((field_name, field_info))
            else:
                regular_fields.append((field_name, field_info))

        # Generate regular fields as Optional
        for field_name, field_info in regular_fields:
            type_str = field_info["type"]
            # Make all fields optional
            if " | None" not in type_str and "None" not in type_str:
                type_str = f"Optional[{type_str}]"
            elif not type_str.startswith("Optional["):
                # Already has | None, convert to Optional
                type_str = type_str.replace(" | None", "").replace("None", "").strip(" |")
                type_str = f"Optional[{type_str}]"

            # Include field alias if present
            alias = field_info.get("alias")
            if alias:
                lines.append(f"{indent}    {field_name}: {type_str} = Field(None, alias='{alias}')")
            else:
                lines.append(f"{indent}    {field_name}: {type_str} = None")

        # Private fields for nested objects
        for field_name, field_info in nested_fields:
            builder_type = self._get_builder_type(field_info["type"], known_classes)
            lines.append(f"{indent}    _{field_name}: Optional[{builder_type}] = None")

        # Private fields for arrays
        for field_name, field_info, inner_type in array_fields:
            builder_type = f"{inner_type}Builder"
            lines.append(f"{indent}    _{field_name}: List[{builder_type}] = []")

        lines.append("")

        # Model config
        lines.append(f"{indent}    model_config = ConfigDict(")
        lines.append(f"{indent}        extra='allow',")
        lines.append(f"{indent}        validate_assignment=True,  # Enable validators on assignment")
        lines.append(f"{indent}    )")
        lines.append("")

        # Property accessors for nested objects
        for field_name, field_info in nested_fields:
            builder_type = self._get_builder_type(field_info["type"], known_classes)
            lines.append(f"{indent}    @property")
            lines.append(f"{indent}    def {field_name}(self) -> {builder_type}:")
            lines.append(f'{indent}        """Access {field_name} builder (auto-initialized)."""')
            lines.append(f"{indent}        if self._{field_name} is None:")
            lines.append(f"{indent}            self._{field_name} = {builder_type}()")
            lines.append(f"{indent}        return self._{field_name}")
            lines.append("")

        # Property accessors for arrays (with getter and setter)
        for field_name, field_info, inner_type in array_fields:
            builder_type = f"{inner_type}Builder"
            lines.append(f"{indent}    @property")
            lines.append(f"{indent}    def {field_name}(self) -> List[{builder_type}]:")
            lines.append(f'{indent}        """Access {field_name} builder list."""')
            lines.append(f"{indent}        return self._{field_name}")
            lines.append("")

            # Add setter for list fields
            lines.append(f"{indent}    @{field_name}.setter")
            lines.append(f"{indent}    def {field_name}(self, value: List[{builder_type}]) -> None:")
            lines.append(f'{indent}        """Set {field_name} builder list."""')
            lines.append(f"{indent}        self._{field_name} = value")
            lines.append("")

        # Add methods for arrays
        for field_name, field_info, inner_type in array_fields:
            # Check if inner_type is a union (contains " | ")
            if " | " in inner_type:
                # For union types, use the first type for instantiation
                first_type = inner_type.split(" | ")[0].strip()
                instantiate_type = f"{first_type}Builder"
                builder_type = f"{inner_type}Builder"  # Keep full union for return type
            else:
                instantiate_type = f"{inner_type}Builder"
                builder_type = instantiate_type

            method_name = f"add_{field_name.rstrip('s')}"  # Simple pluralization
            lines.append(f"{indent}    def {method_name}(self) -> {builder_type}:")
            lines.append(f'{indent}        """Add and return a new {inner_type} builder."""')
            lines.append(f"{indent}        builder = {instantiate_type}()")
            lines.append(f"{indent}        self._{field_name}.append(builder)")
            lines.append(f"{indent}        return builder")
            lines.append("")

        # Multi-language field validators (for automatic type conversion)
        ml_fields = [
            (name, info) for name, info in regular_fields if info["is_multi_lang"]
        ]

        if ml_fields:
            # Group fields by multi-lang type
            string_ml_fields = []
            st_ml_fields = []
            ft_ml_fields = []

            for field_name, field_info in ml_fields:
                field_type = field_info["type"]
                if "StringMultiLang" in field_type:
                    string_ml_fields.append(field_name)
                elif "STMultiLang" in field_type:
                    st_ml_fields.append(field_name)
                elif "FTMultiLang" in field_type:
                    ft_ml_fields.append(field_name)

            # Generate validator for StringMultiLang fields
            if string_ml_fields:
                field_list = ", ".join([f"'{f}'" for f in string_ml_fields])
                lines.append(f"{indent}    @field_validator({field_list}, mode='before')")
                lines.append(f"{indent}    @classmethod")
                lines.append(f"{indent}    def _convert_string_multilang(cls, v):")
                lines.append(f'{indent}        """Auto-convert dict or list[dict] to StringMultiLang."""')
                lines.append(f"{indent}        if v is None or isinstance(v, StringMultiLang):")
                lines.append(f"{indent}            return v")
                lines.append(f"{indent}        ")
                lines.append(f"{indent}        ml = StringMultiLang()")
                lines.append(f"{indent}        if isinstance(v, dict):")
                lines.append(f"{indent}            ml.items.append(MultiLangItemString(**v))")
                lines.append(f"{indent}        elif isinstance(v, list):")
                lines.append(f"{indent}            for item in v:")
                lines.append(f"{indent}                if isinstance(item, dict):")
                lines.append(f"{indent}                    ml.items.append(MultiLangItemString(**item))")
                lines.append(f"{indent}        return ml")
                lines.append("")

            # Generate validator for STMultiLang fields
            if st_ml_fields:
                field_list = ", ".join([f"'{f}'" for f in st_ml_fields])
                lines.append(f"{indent}    @field_validator({field_list}, mode='before')")
                lines.append(f"{indent}    @classmethod")
                lines.append(f"{indent}    def _convert_st_multilang(cls, v):")
                lines.append(f'{indent}        """Auto-convert dict or list[dict] to STMultiLang."""')
                lines.append(f"{indent}        if v is None or isinstance(v, STMultiLang):")
                lines.append(f"{indent}            return v")
                lines.append(f"{indent}        ")
                lines.append(f"{indent}        ml = STMultiLang()")
                lines.append(f"{indent}        if isinstance(v, dict):")
                lines.append(f"{indent}            ml.items.append(MultiLangItemST(**v))")
                lines.append(f"{indent}        elif isinstance(v, list):")
                lines.append(f"{indent}            for item in v:")
                lines.append(f"{indent}                if isinstance(item, dict):")
                lines.append(f"{indent}                    ml.items.append(MultiLangItemST(**item))")
                lines.append(f"{indent}        return ml")
                lines.append("")

            # Generate validator for FTMultiLang fields
            if ft_ml_fields:
                field_list = ", ".join([f"'{f}'" for f in ft_ml_fields])
                lines.append(f"{indent}    @field_validator({field_list}, mode='before')")
                lines.append(f"{indent}    @classmethod")
                lines.append(f"{indent}    def _convert_ft_multilang(cls, v):")
                lines.append(f'{indent}        """Auto-convert dict or list[dict] to FTMultiLang."""')
                lines.append(f"{indent}        if v is None or isinstance(v, FTMultiLang):")
                lines.append(f"{indent}            return v")
                lines.append(f"{indent}        ")
                lines.append(f"{indent}        ml = FTMultiLang()")
                lines.append(f"{indent}        if isinstance(v, dict):")
                lines.append(f"{indent}            ml.items.append(MultiLangItem(**v))")
                lines.append(f"{indent}        elif isinstance(v, list):")
                lines.append(f"{indent}            for item in v:")
                lines.append(f"{indent}                if isinstance(item, dict):")
                lines.append(f"{indent}                    ml.items.append(MultiLangItem(**item))")
                lines.append(f"{indent}        return ml")
                lines.append("")

        # Multi-language helper methods
        for field_name, field_info in ml_fields:
            # Determine the multi-lang type from the field type
            field_type = field_info["type"]
            if "StringMultiLang" in field_type:
                ml_class = "StringMultiLang"
                item_class = "MultiLangItemString"
            elif "STMultiLang" in field_type:
                ml_class = "STMultiLang"
                item_class = "MultiLangItemST"
            elif "FTMultiLang" in field_type:
                ml_class = "FTMultiLang"
                item_class = "MultiLangItem"  # FTMultiLang uses MultiLangItem, not MultiLangItemFT
            else:
                continue  # Skip if not a recognized multi-lang type

            # set_<field> method
            base_name = field_name.replace("common_", "").replace("_", "")
            lines.append(
                f"{indent}    def set_{base_name}(self, text: str, lang: str = 'en') -> '{builder_name}':"
            )
            lines.append(
                f'{indent}        """Set {field_name} text for a specific language."""'
            )
            lines.append(f"{indent}        if self.{field_name} is None:")
            lines.append(f"{indent}            self.{field_name} = {ml_class}()")
            lines.append("")
            lines.append(f"{indent}        # Update existing or add new")
            lines.append(f"{indent}        for item in self.{field_name}.items:")
            lines.append(f"{indent}            if item.lang == lang:")
            lines.append(f"{indent}                item.text = text")
            lines.append(f"{indent}                return self")
            lines.append("")
            lines.append(
                f"{indent}        self.{field_name}.items.append({item_class}(**{{'@xml:lang': lang, '#text': text}}))"
            )
            lines.append(f"{indent}        return self")
            lines.append("")

            # get_<field> method
            lines.append(
                f"{indent}    def get_{base_name}(self, lang: str = 'en') -> Optional[str]:"
            )
            lines.append(
                f'{indent}        """Get {field_name} text for a specific language."""'
            )
            lines.append(f"{indent}        if not self.{field_name}:")
            lines.append(f"{indent}            return None")
            lines.append(f"{indent}        for item in self.{field_name}.items:")
            lines.append(f"{indent}            if item.lang == lang:")
            lines.append(f"{indent}                return item.text")
            lines.append(f"{indent}        return None")
            lines.append("")

        # Build method
        lines.append(f"{indent}    def build(self) -> {class_name}:")
        lines.append(f'{indent}        """Build the final {class_name} instance."""')
        lines.append(
            f"{indent}        data = self.model_dump(exclude_none=True, by_alias=True)"
        )
        lines.append("")

        # Remove private fields from data
        if nested_fields or array_fields:
            lines.append(f"{indent}        # Remove private builder fields")
            for field_name, _ in nested_fields:
                lines.append(f"{indent}        data.pop('_{field_name}', None)")
            for field_name, _, _ in array_fields:
                lines.append(f"{indent}        data.pop('_{field_name}', None)")
            lines.append("")

        # Build nested objects
        if nested_fields:
            lines.append(f"{indent}        # Build nested objects")
            for field_name, field_info in nested_fields:
                orig_name = self._get_original_name(field_name, field_info)
                lines.append(f"{indent}        if self._{field_name} is not None:")
                lines.append(
                    f"{indent}            data['{orig_name}'] = self._{field_name}.build()"
                )
            lines.append("")

        # Build arrays
        if array_fields:
            lines.append(f"{indent}        # Build array fields")
            for field_name, field_info, _ in array_fields:
                orig_name = self._get_original_name(field_name, field_info)
                lines.append(f"{indent}        if self._{field_name}:")
                lines.append(
                    f"{indent}            data['{orig_name}'] = [item.build() for item in self._{field_name}]"
                )
            lines.append("")

        lines.append(f"{indent}        return {class_name}.model_validate(data)")
        lines.append("")

        # Build dump method for debugging
        lines.append(f"{indent}    def build_dump(self, indent: int = 2) -> str:")
        lines.append(f'{indent}        """Dump builder state including nested builders for debugging.')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        Warning: This is for debugging only. The output structure differs')
        lines.append(f'{indent}        from the final model. Use build() to create the actual model.')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        Returns:')
        lines.append(f'{indent}            JSON string with full builder state including nested builders')
        lines.append(f'{indent}        """')
        lines.append(f'{indent}        import json')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        def _dump_builder(obj, depth=0, seen=None):')
        lines.append(f'{indent}            """Recursively dump builder objects."""')
        lines.append(f'{indent}            if seen is None:')
        lines.append(f'{indent}                seen = set()')
        lines.append(f'{indent}            ')
        lines.append(f'{indent}            # Prevent infinite recursion')
        lines.append(f'{indent}            obj_id = id(obj)')
        lines.append(f'{indent}            if obj_id in seen or depth > 20:')
        lines.append(f'{indent}                return "<circular>"')
        lines.append(f'{indent}            ')
        lines.append(f'{indent}            if isinstance(obj, BaseModel):')
        lines.append(f'{indent}                seen.add(obj_id)')
        lines.append(f'{indent}                result = {{}}')
        lines.append(f'{indent}                ')
        lines.append(f'{indent}                # Dump regular fields from __dict__')
        lines.append(f'{indent}                for field_name, field_value in obj.__dict__.items():')
        lines.append(f'{indent}                    if field_value is None:')
        lines.append(f'{indent}                        continue')
        lines.append(f'{indent}                    if field_name.startswith("_"):')
        lines.append(f'{indent}                        # Private field - include without underscore')
        lines.append(f'{indent}                        clean_name = field_name[1:]')
        lines.append(f'{indent}                        result[clean_name] = _dump_builder(field_value, depth+1, seen)')
        lines.append(f'{indent}                    else:')
        lines.append(f'{indent}                        result[field_name] = _dump_builder(field_value, depth+1, seen)')
        lines.append(f'{indent}                ')
        lines.append(f'{indent}                seen.remove(obj_id)')
        lines.append(f'{indent}                return result')
        lines.append(f'{indent}            elif isinstance(obj, list):')
        lines.append(f'{indent}                return [_dump_builder(item, depth+1, seen) for item in obj]')
        lines.append(f'{indent}            elif isinstance(obj, dict):')
        lines.append(f'{indent}                return {{k: _dump_builder(v, depth+1, seen) for k, v in obj.items()}}')
        lines.append(f'{indent}            else:')
        lines.append(f'{indent}                return obj')
        lines.append(f'{indent}        ')
        lines.append(f'{indent}        return json.dumps(_dump_builder(self), indent=indent, default=str)')
        lines.append("")

        return "\n".join(lines)

    def _get_builder_type(self, type_str: str, known_classes: Set[str]) -> str:
        """Get the builder type name for a given type string.

        Args:
            type_str: Original type string
            known_classes: Set of known class names

        Returns:
            Builder type name
        """
        # Remove optional markers
        base_type = type_str.replace(" | None", "").replace("None", "").strip(" |")

        # Handle unions - take first type
        if " | " in base_type:
            base_type = base_type.split(" | ")[0].strip()

        return f"{base_type}Builder"

    def generate_builders_file(self, entity_name: str) -> str:
        """Generate complete builders file for an entity.

        Args:
            entity_name: Entity name (e.g., 'tidas_contacts')

        Returns:
            Complete Python file content
        """
        logger.info(f"Generating builders for {entity_name}")

        # Load type file
        type_file = self.types_dir / f"{entity_name}.py"
        if not type_file.exists():
            raise FileNotFoundError(f"Type file not found: {type_file}")

        # Parse classes and imports
        classes, original_imports = self.parse_type_file(type_file)
        known_classes = set(classes.keys())

        logger.info(f"Found {len(classes)} classes in {entity_name}")

        # Generate file header
        lines = [
            "# Auto-generated builder classes for TIDAS entities",
            "# DO NOT EDIT - Regenerate using scripts/generate_builders.py",
            "",
            "from __future__ import annotations",
            "",
        ]

        # Collect needed imports from original file
        typing_imports = set()
        pydantic_imports = set()
        other_imports = []

        for import_stmt in original_imports:
            if import_stmt['type'] == 'from':
                module = import_stmt['module']
                names = import_stmt['names']

                # Skip imports from the same module
                if module == f"tidas_sdk.types.{entity_name}":
                    continue
                # Skip __future__ imports (already added)
                elif module == '__future__':
                    continue
                # Collect typing imports
                elif module == 'typing':
                    typing_imports.update(names)
                # Collect pydantic imports
                elif module in ('pydantic', 'pydantic.types'):
                    pydantic_imports.update(names)
                # Keep other imports
                else:
                    other_imports.append(import_stmt)

        # Add typing imports
        typing_imports.update(['Optional', 'List'])
        if typing_imports:
            lines.append(f"from typing import {', '.join(sorted(typing_imports))}")

        # Add pydantic imports
        pydantic_imports.update(['BaseModel', 'ConfigDict', 'field_validator'])
        if pydantic_imports:
            lines.append(f"from pydantic import {', '.join(sorted(pydantic_imports))}")

        # Add other imports (category, data_types, etc.)
        for import_stmt in other_imports:
            module = import_stmt['module']
            names = import_stmt['names']
            lines.append(f"from {module} import (")
            for name in names:
                lines.append(f"    {name},")
            lines.append(")")

        # Add wildcard import for all classes from current entity
        # This includes Enums, type aliases, and other types used in field annotations
        lines.extend([
            "",
            f"from tidas_sdk.types.{entity_name} import *",
            "",
            ""
        ])

        # Generate builder classes in order (simple -> complex)
        # This ensures nested builders are defined before parent builders
        sorted_classes = self._topological_sort(classes, known_classes)

        for class_name in sorted_classes:
            class_info = classes[class_name]
            builder_code = self.generate_builder_class(
                class_name, class_info, known_classes
            )
            lines.append(builder_code)

        # Add model_rebuild() calls to resolve forward references
        lines.append("# Rebuild models to resolve forward references")
        for class_name in sorted_classes:
            builder_name = f"{class_name}Builder"
            lines.append(f"{builder_name}.model_rebuild()")
        lines.append("")

        return "\n".join(lines)

    def _topological_sort(
        self, classes: Dict[str, Dict[str, Any]], known_classes: Set[str]
    ) -> List[str]:
        """Sort classes topologically (nested objects first).

        Args:
            classes: Dictionary of class definitions
            known_classes: Set of known class names

        Returns:
            Sorted list of class names
        """
        # Build dependency graph
        dependencies = {}
        for class_name, class_info in classes.items():
            deps = set()
            for field_info in class_info["fields"].values():
                type_str = field_info["type"]
                # Extract base types from the type string
                for known_class in known_classes:
                    if known_class in type_str and known_class != class_name:
                        deps.add(known_class)
            dependencies[class_name] = deps

        # Topological sort
        sorted_classes = []
        visited = set()

        def visit(name: str):
            if name in visited:
                return
            visited.add(name)
            for dep in dependencies.get(name, []):
                if dep in classes:  # Only visit if it's in our classes dict
                    visit(dep)
            sorted_classes.append(name)

        for class_name in classes:
            visit(class_name)

        return sorted_classes

    def generate_all_builders(self, output_dir: Path):
        """Generate builders for all TIDAS entities.

        Args:
            output_dir: Output directory for builder files
        """
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Find all entity type files
        entity_files = sorted(self.types_dir.glob("tidas_*.py"))

        # Skip category and data_types files
        entity_files = [
            f
            for f in entity_files
            if not f.name.endswith("_category.py") and f.name != "tidas_data_types.py"
        ]

        logger.info(f"Found {len(entity_files)} entity files")

        generated_files = []
        for type_file in entity_files:
            entity_name = type_file.stem

            try:
                # Generate builders
                builders_code = self.generate_builders_file(entity_name)

                # Write output file
                output_file = output_dir / f"{entity_name}_builders.py"
                output_file.write_text(builders_code, encoding="utf-8")

                logger.info(f"✅ Generated {output_file.name}")
                generated_files.append(output_file.name)

            except Exception as e:
                logger.error(f"❌ Failed to generate builders for {entity_name}: {e}")
                if "--verbose" in sys.argv or "-v" in sys.argv:
                    import traceback

                    traceback.print_exc()

        # Generate __init__.py
        self._generate_init_file(output_dir, generated_files)

        logger.info(f"✅ Successfully generated {len(generated_files)} builder files")

    def _generate_init_file(self, output_dir: Path, generated_files: List[str]):
        """Generate __init__.py for builders module.

        Args:
            output_dir: Output directory
            generated_files: List of generated file names
        """
        init_file = output_dir / "__init__.py"

        lines = [
            '"""Auto-generated builder classes for TIDAS entities."""',
            "",
            "# Builders enable incremental construction of complex TIDAS entities",
            "# Usage:",
            "#   from tidas_sdk.builders import ContactBuilder",
            "#   builder = ContactBuilder()",
            "#   builder.contact_data_set.contact_information.data_set_information.email = 'test@example.com'",
            "#   contact = builder.build()",
            "",
        ]

        # Import all builders
        imports = []
        exports = []

        for file_name in sorted(generated_files):
            # Entity name without _builders.py suffix
            entity_name = file_name.replace("_builders.py", "")

            # Main builder name (e.g., ContactBuilder, ProcessesBuilder)
            # Convert tidas_contacts -> Contact, tidas_processes -> Processes
            entity_simple = entity_name.replace("tidas_", "")
            builder_name = (
                "".join(word.capitalize() for word in entity_simple.split("_"))
                + "Builder"
            )

            # Find the actual root builder class name by reading the file
            # For now, we'll use a heuristic: the Model class becomes ModelBuilder
            # But we know from the type files that the root is usually "Model"
            # So we import Model as <Entity>Builder - but we need the actual name

            # Let's just import the whole module for now
            module_name = file_name.replace(".py", "")
            imports.append(f"from .{module_name} import *")

        lines.extend(imports)
        lines.append("")
        lines.append("__all__ = [")
        lines.append('    "# All builder classes are exported"')
        lines.append("]")
        lines.append("")

        init_file.write_text("\n".join(lines), encoding="utf-8")
        logger.info(f"✅ Generated {init_file.name}")


def find_types_dir() -> Path:
    """Find the types directory.

    Returns:
        Path to types directory
    """
    # Try relative to script location
    script_dir = Path(__file__).parent
    types_dir = script_dir.parent / "src" / "tidas_sdk" / "types"

    if types_dir.exists():
        return types_dir

    raise FileNotFoundError(
        f"Could not find types directory at {types_dir}. "
        "Please run this script from the sdks/python directory."
    )


def find_schema_dir() -> Path:
    """Find the schema directory.

    Returns:
        Path to schema directory
    """
    # Check environment variable first
    tidas_tools_path = os.environ.get("TIDAS_TOOLS_PATH")
    if tidas_tools_path:
        schema_dir = Path(tidas_tools_path) / "src" / "tidas_tools" / "tidas" / "schemas"
        if schema_dir.exists():
            return schema_dir

    # Try to find tidas-tools
    current = Path.cwd()
    for _ in range(5):
        tidas_tools = (
            current / "tidas-tools" / "src" / "tidas_tools" / "tidas" / "schemas"
        )
        if tidas_tools.exists():
            return tidas_tools
        current = current.parent

    raise FileNotFoundError(
        "Could not find TIDAS schemas directory. "
        "Please set TIDAS_TOOLS_PATH environment variable or ensure tidas-tools is in parent directories."
    )


def main() -> int:
    """Main entry point."""
    # Setup logging
    logger.remove()
    logger.add(sys.stderr, level="INFO")

    print("=" * 60)
    print("TIDAS SDK Builder Generator")
    print("=" * 60)

    try:
        # Find directories
        types_dir = find_types_dir()
        schema_dir = find_schema_dir()

        logger.info(f"Types directory: {types_dir}")
        logger.info(f"Schema directory: {schema_dir}")

        # Create generator
        generator = BuilderGenerator(types_dir, schema_dir)

        # Output directory
        output_dir = types_dir.parent / "builders"

        # Generate all builders
        generator.generate_all_builders(output_dir)

        print("=" * 60)
        print("✅ Builder generation completed successfully!")
        print(f"📁 Output: {output_dir}")
        print("=" * 60)

        return 0

    except Exception as e:
        logger.error(f"❌ Builder generation failed: {e}")
        if "--verbose" in sys.argv or "-v" in sys.argv:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
