"""
Type mapper for JSON Schema to Python type conversion.
"""

from typing import Any, Dict, List, Optional, Set

from loguru import logger


class TypeMapper:
    """Maps JSON Schema types to Python type annotations."""

    def __init__(self) -> None:
        """Initialize type mapper with import tracking."""
        self.imports: Set[str] = set()
        self.field_imports: Set[str] = set()

    def map_type(self, schema: Dict[str, Any], field_name: str) -> str:
        """Map JSON Schema type to Python type annotation.

        Args:
            schema: JSON Schema field definition
            field_name: Name of the field (for context)

        Returns:
            Python type annotation as string
        """
        json_type = schema.get("type")
        format_type = schema.get("format")

        # Handle type arrays (e.g., ["string", "null"])
        if isinstance(json_type, list):
            # Filter out "null" and make it Optional
            types = [t for t in json_type if t != "null"]
            has_null = "null" in json_type

            if len(types) == 1:
                base_type = self._map_single_type(types[0], format_type, schema)
                if has_null:
                    self.imports.add("from typing import Optional")
                    return f"Optional[{base_type}]"
                return base_type
            else:
                # Multiple non-null types -> Union
                self.imports.add("from typing import Union")
                mapped_types = [self._map_single_type(t, None, schema) for t in types]
                union_type = f"Union[{', '.join(mapped_types)}]"
                if has_null:
                    self.imports.add("from typing import Optional")
                    return f"Optional[{union_type}]"
                return union_type

        # Handle enum
        if "enum" in schema:
            return self.handle_enum(schema["enum"])

        # Handle oneOf/anyOf
        if "oneOf" in schema:
            return self.handle_union(schema["oneOf"])
        if "anyOf" in schema:
            return self.handle_union(schema["anyOf"])

        return self._map_single_type(json_type, format_type, schema)

    def _map_single_type(
        self,
        json_type: Optional[str],
        format_type: Optional[str],
        schema: Dict[str, Any],
    ) -> str:
        """Map a single JSON Schema type to Python type.

        Args:
            json_type: JSON Schema type
            format_type: JSON Schema format
            schema: Full schema for context

        Returns:
            Python type as string
        """
        if json_type == "string":
            if format_type == "uuid":
                self.imports.add("from uuid import UUID")
                return "UUID"
            elif format_type == "date-time":
                self.imports.add("from datetime import datetime")
                return "datetime"
            else:
                return "str"

        elif json_type == "integer":
            return "int"

        elif json_type == "number":
            return "float"

        elif json_type == "boolean":
            return "bool"

        elif json_type == "array":
            items_schema = schema.get("items", {})
            item_type = self.map_type(items_schema, "item")
            self.imports.add("from typing import List")
            return f"List[{item_type}]"

        elif json_type == "object":
            # Check if it has properties (nested object)
            if "properties" in schema:
                # Will be replaced with actual model name in code generator
                self.imports.add("from typing import Dict, Any")
                return "Dict[str, Any]"  # Placeholder for nested objects
            else:
                self.imports.add("from typing import Dict, Any")
                return "Dict[str, Any]"

        elif json_type == "null":
            return "None"

        else:
            # Fallback to Any
            self.imports.add("from typing import Any")
            return "Any"

    def extract_field_constraints(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Extract Pydantic Field() constraints from JSON Schema.

        Args:
            schema: JSON Schema field definition

        Returns:
            Dictionary of Field() kwargs
        """
        constraints: Dict[str, Any] = {}

        if "maxLength" in schema:
            constraints["max_length"] = schema["maxLength"]
            self.field_imports.add("from pydantic import Field")

        if "minLength" in schema:
            constraints["min_length"] = schema["minLength"]
            self.field_imports.add("from pydantic import Field")

        if "pattern" in schema:
            constraints["pattern"] = schema["pattern"]
            self.field_imports.add("from pydantic import Field")

        if "minimum" in schema:
            constraints["ge"] = schema["minimum"]
            self.field_imports.add("from pydantic import Field")

        if "maximum" in schema:
            constraints["le"] = schema["maximum"]
            self.field_imports.add("from pydantic import Field")

        if "description" in schema:
            constraints["description"] = schema["description"]
            self.field_imports.add("from pydantic import Field")

        # Handle default values
        if "default" in schema:
            constraints["default"] = schema["default"]

        return constraints

    def is_required(self, field_name: str, required_fields: List[str]) -> bool:
        """Check if field is required.

        Args:
            field_name: Name of field to check
            required_fields: List of required field names from schema

        Returns:
            True if field is required
        """
        return field_name in required_fields

    def handle_enum(self, enum_values: List[Any]) -> str:
        """Convert enum to Literal type.

        Args:
            enum_values: List of allowed enum values

        Returns:
            Literal type annotation string
        """
        self.imports.add("from typing import Literal")

        # Quote string values
        quoted_values = []
        for value in enum_values:
            if isinstance(value, str):
                # Escape quotes in strings
                escaped = value.replace('"', '\\"')
                quoted_values.append(f'"{escaped}"')
            elif isinstance(value, bool):
                quoted_values.append(str(value))
            elif value is None:
                quoted_values.append("None")
            else:
                quoted_values.append(str(value))

        return f"Literal[{', '.join(quoted_values)}]"

    def handle_union(self, schemas: List[Dict[str, Any]]) -> str:
        """Convert oneOf/anyOf to Union type.

        Args:
            schemas: List of schema options

        Returns:
            Union type annotation string
        """
        self.imports.add("from typing import Union")

        types = []
        for schema in schemas:
            mapped_type = self.map_type(schema, "union_member")
            types.append(mapped_type)

        # Remove duplicates while preserving order
        seen = set()
        unique_types = []
        for t in types:
            if t not in seen:
                seen.add(t)
                unique_types.append(t)

        if len(unique_types) == 1:
            return unique_types[0]

        return f"Union[{', '.join(unique_types)}]"

    def get_imports(self) -> List[str]:
        """Get list of import statements needed for generated types.

        Returns:
            List of import statement strings, sorted and deduplicated
        """
        all_imports = self.imports.union(self.field_imports)
        return sorted(list(all_imports))

    def reset_imports(self) -> None:
        """Reset import tracking for new file generation."""
        self.imports.clear()
        self.field_imports.clear()
