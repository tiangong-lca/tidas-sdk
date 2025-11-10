#!/usr/bin/env python3
"""
Auto-generate typed wrapper classes from TIDAS JSON schemas.

This script generates wrapper classes that provide IDE autocomplete and type hints
for entity fields. The wrappers are automatically synchronized with schema changes.
"""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from loguru import logger


class WrapperGenerator:
    """Generate typed wrapper classes from JSON schemas."""

    MULTI_LANG_TYPES = {
        "StringMultiLang",
        "STMultiLang",
        "FTMultiLang",
    }

    def __init__(self, schema_dir: Optional[str] = None):
        """Initialize wrapper generator.

        Args:
            schema_dir: Path to directory containing JSON schemas
        """
        if schema_dir is None:
            tidas_tools_path = os.environ.get("TIDAS_TOOLS_PATH")
            if tidas_tools_path:
                schema_dir = os.path.join(
                    tidas_tools_path, "src/tidas_tools/tidas/schemas"
                )
            else:
                repo_root = Path(__file__).parent.parent.parent.parent
                schema_dir = str(
                    repo_root
                    / "tidas-tools"
                    / "src"
                    / "tidas_tools"
                    / "tidas"
                    / "schemas"
                )

        self.schema_dir = Path(schema_dir)
        if not self.schema_dir.exists():
            raise FileNotFoundError(f"Schema directory not found: {self.schema_dir}")

        logger.info(f"Using schema directory: {self.schema_dir}")
        self.schemas: Dict[str, Dict[str, Any]] = {}
        self.generated_classes: Set[str] = set()

    def load_schema(self, schema_name: str) -> Dict[str, Any]:
        """Load a JSON schema file.

        Args:
            schema_name: Name of schema (e.g., 'tidas_contacts')

        Returns:
            Parsed schema dictionary
        """
        schema_file = self.schema_dir / f"{schema_name}.json"
        with open(schema_file, "r", encoding="utf-8") as f:
            schema = json.load(f)
        self.schemas[schema_name] = schema
        return schema

    def resolve_ref(self, ref: str) -> Optional[str]:
        """Resolve a $ref to determine field type.

        Args:
            ref: $ref string (e.g., 'tidas_data_types.json#/$defs/StringMultiLang')

        Returns:
            Type name or None
        """
        if "#/$defs/" in ref:
            return ref.split("#/$defs/")[1]
        return None

    def is_multi_lang_field(self, field_schema: Dict[str, Any]) -> bool:
        """Check if a field is a multi-language field.

        Args:
            field_schema: Field schema dictionary

        Returns:
            True if field is multi-language
        """
        if "$ref" in field_schema:
            ref_type = self.resolve_ref(field_schema["$ref"])
            return ref_type in self.MULTI_LANG_TYPES
        return False

    def is_nested_object(self, field_schema: Dict[str, Any]) -> bool:
        """Check if a field is a nested object.

        Args:
            field_schema: Field schema dictionary

        Returns:
            True if field is nested object
        """
        return field_schema.get("type") == "object"

    def is_optional_field(self, field_name: str, required: List[str]) -> bool:
        """Check if a field is optional.

        Args:
            field_name: Name of field
            required: List of required field names

        Returns:
            True if field is optional
        """
        return field_name not in required

    # Python keywords that need to be escaped
    PYTHON_KEYWORDS = {
        "class",
        "def",
        "return",
        "if",
        "else",
        "elif",
        "while",
        "for",
        "try",
        "except",
        "finally",
        "with",
        "as",
        "import",
        "from",
        "global",
        "nonlocal",
        "lambda",
        "yield",
        "break",
        "continue",
        "pass",
        "raise",
        "assert",
        "del",
        "in",
        "is",
        "not",
        "and",
        "or",
        "None",
        "True",
        "False",
    }

    def python_field_name(self, field_name: str) -> str:
        """Convert schema field name to Python attribute name.

        Args:
            field_name: Schema field name (e.g., 'dataSetInformation', 'common:UUID', 'WWWAddress')

        Returns:
            Python attribute name (e.g., 'data_set_information', 'uuid', 'www_address')
        """
        # Remove namespace prefixes
        if ":" in field_name:
            field_name = field_name.split(":")[-1]

        # Remove @ and # prefixes
        field_name = field_name.lstrip("@#")

        # Convert camelCase to snake_case
        # Handle consecutive uppercase letters (e.g., WWWAddress -> www_address)
        result = []
        for i, char in enumerate(field_name):
            if char.isupper():
                # Add underscore before uppercase if:
                # 1. Previous char is lowercase (camelCase boundary)
                # 2. Next char is lowercase and current is part of acronym (e.g., WWWAddress -> www_address)
                if i > 0:
                    prev_lower = field_name[i - 1].islower()
                    next_lower = i + 1 < len(field_name) and field_name[i + 1].islower()
                    if prev_lower or next_lower:
                        result.append("_")
            result.append(char.lower())

        python_name = "".join(result)

        # Escape Python keywords by appending underscore
        if python_name in self.PYTHON_KEYWORDS:
            python_name = python_name + "_"

        return python_name

    def generate_simple_property(
        self,
        field_name: str,
        python_name: str,
        field_schema: Dict[str, Any],
        is_optional: bool,
    ) -> List[str]:
        """Generate a simple property (string, int, bool, etc.).

        Args:
            field_name: Original field name in schema
            python_name: Python attribute name
            field_schema: Field schema
            is_optional: Whether field is optional

        Returns:
            List of code lines
        """
        # Determine Python type
        field_type = field_schema.get("type", "str")
        py_type = {
            "string": "str",
            "integer": "int",
            "number": "float",
            "boolean": "bool",
        }.get(field_type, "str")

        if is_optional:
            py_type = f"Optional[{py_type}]"

        description = field_schema.get("description", f"Access {field_name} field")

        lines = [
            f"    @property",
            f"    def {python_name}(self) -> {py_type}:",
            f'        """ {description} """',
            f'        return self._data.get("{field_name}")',
            f"",
            f"    @{python_name}.setter",
            f"    def {python_name}(self, value: {py_type}) -> None:",
            f'        """Set {field_name}."""',
        ]

        if is_optional:
            lines.extend(
                [
                    f"        if value is None:",
                    f'            self._data.pop("{field_name}", None)',
                    f"        else:",
                    f'            self._data["{field_name}"] = value',
                ]
            )
        else:
            lines.append(f'        self._data["{field_name}"] = value')

        lines.append("")
        return lines

    def generate_multilang_property(
        self, field_name: str, python_name: str, field_schema: Dict[str, Any]
    ) -> List[str]:
        """Generate a multi-language text property.

        Args:
            field_name: Original field name in schema
            python_name: Python attribute name
            field_schema: Field schema

        Returns:
            List of code lines
        """
        description = field_schema.get(
            "description", f"Access {field_name} multi-language field"
        )

        return [
            f"    @property",
            f"    def {python_name}(self) -> MultiLangText:",
            f'        """ {description} """',
            f'        return self._get_multi_lang("{field_name}")',
            f"",
        ]

    def generate_nested_property(
        self,
        field_name: str,
        python_name: str,
        field_schema: Dict[str, Any],
        wrapper_class_name: str,
    ) -> List[str]:
        """Generate a nested object property.

        Args:
            field_name: Original field name in schema
            python_name: Python attribute name
            field_schema: Field schema
            wrapper_class_name: Name of wrapper class for nested object

        Returns:
            List of code lines
        """
        description = field_schema.get(
            "description", f"Access {field_name} nested object"
        )

        return [
            f"    @property",
            f"    def {python_name}(self) -> {wrapper_class_name}:",
            f'        """ {description} """',
            f'        self._ensure_field("{field_name}")',
            f'        return {wrapper_class_name}(self._entity, self._data["{field_name}"])',
            f"",
        ]

    def generate_wrapper_class(
        self,
        class_name: str,
        field_schema: Dict[str, Any],
        depth: int = 0,
    ) -> List[str]:
        """Generate a wrapper class for a nested object.

        Args:
            class_name: Name of wrapper class
            field_schema: Schema for the object
            depth: Nesting depth (for recursion limit)

        Returns:
            List of code lines
        """
        if depth > 10 or class_name in self.generated_classes:
            return []

        self.generated_classes.add(class_name)
        properties = field_schema.get("properties", {})
        required = field_schema.get("required", [])

        lines = [
            f"",
            f"class {class_name}(BaseWrapper):",
            f'    """Auto-generated wrapper for {class_name}."""',
            f"",
            f"    __slots__ = ()",
            f"",
        ]

        # Generate properties for each field
        for field_name, nested_schema in properties.items():
            # Skip namespace declarations
            if field_name.startswith("@xmlns"):
                continue

            python_name = self.python_field_name(field_name)
            is_optional = self.is_optional_field(field_name, required)

            # Multi-language field
            if self.is_multi_lang_field(nested_schema):
                lines.extend(
                    self.generate_multilang_property(
                        field_name, python_name, nested_schema
                    )
                )

            # Nested object
            elif self.is_nested_object(nested_schema):
                # Generate nested wrapper class first
                nested_class_name = f"{self.python_field_name(field_name).title().replace('_', '')}Wrapper"
                nested_lines = self.generate_wrapper_class(
                    nested_class_name, nested_schema, depth + 1
                )
                if nested_lines:
                    lines = nested_lines + lines  # Add nested class before parent

                # Generate property
                lines.extend(
                    self.generate_nested_property(
                        field_name, python_name, nested_schema, nested_class_name
                    )
                )

            # Simple field
            else:
                lines.extend(
                    self.generate_simple_property(
                        field_name, python_name, nested_schema, is_optional
                    )
                )

        return lines

    def generate_entity_wrappers(self, entity_name: str) -> str:
        """Generate wrapper file for an entity.

        Args:
            entity_name: Entity name (e.g., 'contacts', 'flows')

        Returns:
            Generated Python code
        """
        schema = self.load_schema(f"tidas_{entity_name}")
        self.generated_classes.clear()

        # Header
        lines = [
            '"""',
            f"Auto-generated typed wrappers for {entity_name} entity.",
            "",
            "DO NOT EDIT THIS FILE MANUALLY - it is auto-generated from JSON schemas.",
            "To regenerate, run: uv run python scripts/generate_wrappers.py",
            '"""',
            "",
            "from typing import Optional",
            "",
            "from tidas_sdk.core.typed_access import BaseWrapper, MultiLangText",
            "",
            "",
        ]

        # Find root object (e.g., 'contactDataSet')
        properties = schema.get("properties", {})
        if not properties:
            logger.warning(f"No properties found in schema for {entity_name}")
            return "\n".join(lines)

        # Assume first property is root (e.g., 'contactDataSet')
        root_field_name = list(properties.keys())[0]
        root_schema = properties[root_field_name]

        # Generate root wrapper class
        root_class_name = f"{entity_name.title()}DataSetWrapper"
        wrapper_lines = self.generate_wrapper_class(root_class_name, root_schema)

        lines.extend(wrapper_lines)
        return "\n".join(lines)

    def generate_all_wrappers(self, output_dir: Path) -> None:
        """Generate wrapper files for all entity types.

        Args:
            output_dir: Directory to write wrapper files
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        entities = [
            "contacts",
            "flows",
            "processes",
            "sources",
            "flowproperties",
            "unitgroups",
            "lciamethods",
            "lifecyclemodels",
        ]

        for entity in entities:
            logger.info(f"Generating wrappers for {entity}...")
            try:
                code = self.generate_entity_wrappers(entity)
                output_file = output_dir / f"{entity}_wrappers.py"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(code)
                logger.info(f"  ✓ Generated {output_file}")
            except Exception as e:
                logger.error(f"  ✗ Failed to generate {entity}: {e}")

        # Generate __init__.py
        init_file = output_dir / "__init__.py"
        with open(init_file, "w", encoding="utf-8") as f:
            f.write('"""Auto-generated typed wrappers for all entities."""\n')
        logger.info(f"  ✓ Generated {init_file}")


def main() -> None:
    """Main entry point."""
    import sys

    if len(sys.argv) > 1:
        output_dir = Path(sys.argv[1])
    else:
        # Default output directory
        script_dir = Path(__file__).parent
        output_dir = script_dir.parent / "src" / "tidas_sdk" / "core" / "wrappers"

    logger.info("Starting wrapper generation...")
    generator = WrapperGenerator()
    generator.generate_all_wrappers(output_dir)
    logger.info("Wrapper generation complete!")


if __name__ == "__main__":
    main()
