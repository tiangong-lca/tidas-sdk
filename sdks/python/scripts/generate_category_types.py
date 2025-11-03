#!/usr/bin/env python3
"""
Generate clean category type files from JSON schemas.

Uses Literal types + TypedDict approach (matching TypeScript SDK pattern).
Avoids numbered class suffixes (Source1, Source2, etc.).
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any


class CategoryGenerator:
    """Generate clean category type files using Literal + TypedDict."""

    def __init__(self, schema_path: Path, output_path: Path):
        self.schema_path = schema_path
        self.output_path = output_path
        self.schema = self.load_schema()
        self.categories = self.extract_categories()

    def load_schema(self) -> Dict[str, Any]:
        """Load JSON schema."""
        with open(self.schema_path, encoding="utf-8") as f:
            return json.load(f)

    def extract_categories(self) -> List[Dict[str, str]]:
        """Extract category definitions from schema oneOf."""
        categories = []

        # Navigate to category definitions (usually in oneOf within $defs)
        if "$defs" in self.schema:
            for def_name, def_schema in self.schema["$defs"].items():
                if "oneOf" in def_schema:
                    for option in def_schema["oneOf"]:
                        category = self.extract_category_from_option(option)
                        if category:
                            categories.append(category)

        # Also check top-level oneOf
        if "oneOf" in self.schema:
            for option in self.schema["oneOf"]:
                category = self.extract_category_from_option(option)
                if category:
                    categories.append(category)

        return categories

    def extract_category_from_option(
        self, option: Dict[str, Any]
    ) -> Dict[str, str] | None:
        """Extract category info from a oneOf option.

        Supports two formats:
        1. Standard format with properties: {properties: {@level, @classId, #text}}
        2. Simple const format: {const: "...", description: "..."}
        """
        result = {}

        # Handle simple const + description format (e.g., tidas_locations_category.json)
        if "const" in option and "description" in option:
            result["level"] = "0"  # Locations don't have hierarchy levels
            result["classId"] = str(option["const"])
            result["text"] = str(option["description"])
            return result

        # Handle standard properties format
        if "properties" not in option:
            return None

        props = option["properties"]

        # Extract @level
        if "@level" in props:
            if "const" in props["@level"]:
                result["level"] = props["@level"]["const"]
            elif "enum" in props["@level"] and props["@level"]["enum"]:
                result["level"] = props["@level"]["enum"][0]

        # Extract @classId or @catId
        for key in ["@classId", "@catId"]:
            if key in props:
                if "const" in props[key]:
                    result["classId"] = props[key]["const"]
                elif "enum" in props[key] and props[key]["enum"]:
                    result["classId"] = props[key]["enum"][0]
                break

        # Extract #text
        if "#text" in props:
            if "const" in props["#text"]:
                result["text"] = props["#text"]["const"]
            elif "enum" in props["#text"] and props["#text"]["enum"]:
                result["text"] = props["#text"]["enum"][0]

        # Only return if we have all required fields
        if "level" in result and "classId" in result and "text" in result:
            return result

        return None

    def get_type_name(self) -> str:
        """Get type name from filename."""
        # e.g., tidas_contacts_category.json -> Contact
        # e.g., tidas_flows_elementary_category.json -> FlowElementary
        name = self.schema_path.stem
        name = name.replace("tidas_", "").replace("_category", "")

        # Convert snake_case to PascalCase
        parts = name.split("_")
        return "".join(word.capitalize() for word in parts)

    def get_variable_name(self) -> str:
        """Get variable name from type name."""
        type_name = self.get_type_name()
        # e.g., FlowElementary -> FLOW_ELEMENTARY
        # Insert underscore before capital letters and convert to uppercase
        import re

        name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", type_name)
        return name.upper()

    def get_max_level(self) -> int:
        """Get maximum level value."""
        if not self.categories:
            return 0
        levels = [int(cat["level"]) for cat in self.categories]
        return max(levels)

    def generate(self) -> str:
        """Generate Python category file content using Literal + TypedDict."""
        type_name = self.get_type_name()
        var_name = self.get_variable_name()
        max_level = self.get_max_level()

        lines = [
            '"""',
            f"{type_name} classification categories.",
            "",
            "Clean implementation using Literal types (matches TypeScript SDK pattern).",
            "DO NOT auto-generate - regenerate using generate_category_types.py",
            '"""',
            "",
            "from typing import Literal, TypedDict",
            "",
            "",
            f"class {type_name}CategoryData(TypedDict):",
            f'    """{type_name} category metadata."""',
            "",
            f"    level: Literal[{', '.join(repr(str(i)) for i in range(max_level + 1))}]",
            "    classId: str",
            "    text: str",
            "",
            "",
            f"# Type-safe union of all {type_name.lower()} category IDs",
            f"{type_name} = Literal[",
        ]

        # Add category IDs with comments
        for cat in self.categories:
            class_id = cat["classId"]
            text = cat["text"]
            lines.append(f"    '{class_id}',  # {text}")

        lines.append("]")
        lines.append("")
        lines.append("")

        # Generate Text Literal type (all unique text values)
        text_type_name = f"Tidas{type_name}Text"
        unique_texts = sorted(set(cat["text"] for cat in self.categories))

        # For very large Text types (e.g., FlowsProduct with 3751 values),
        # use str type with a comment instead of Literal to avoid type checker issues
        if len(unique_texts) > 200:
            lines.append(
                f"# Type-safe union of all {type_name.lower()} category text values"
            )
            lines.append(
                f"# Note: This is a very large Literal type with ~{len(unique_texts)} values."
            )
            lines.append(f"# The full list is generated from {var_name}_CATEGORIES.")
            lines.append(
                f"# For type checking purposes, we use str as the actual type since"
            )
            lines.append(
                f"# Python's type checker may have issues with such large Literal types."
            )
            lines.append(
                f"# In practice, the values are validated at runtime using {var_name}_CATEGORIES."
            )
            lines.append(
                f"{text_type_name} = str  # Effectively all text values from {var_name}_CATEGORIES"
            )
        else:
            lines.append(
                f"# Type-safe union of all {type_name.lower()} category text values"
            )
            lines.append(f"{text_type_name} = Literal[")

            # Add text values
            for text in unique_texts:
                # Escape single quotes in text
                escaped_text = text.replace("'", "\\'")
                lines.append(f"    '{escaped_text}',")

            lines.append("]")

        lines.append("")
        lines.append("")
        lines.append("# Runtime metadata for lookups")
        lines.append(f"{var_name}_CATEGORIES: dict[str, {type_name}CategoryData] = {{")

        # Add runtime metadata
        for cat in self.categories:
            lines.append(f"    '{cat['classId']}': {{")
            lines.append(f"        'level': '{cat['level']}',")
            lines.append(f"        'classId': '{cat['classId']}',")
            # Escape single quotes in text
            text = cat["text"].replace("'", "\\'")
            lines.append(f"        'text': '{text}',")
            lines.append("    },")

        lines.append("}")
        lines.append("")
        lines.append("")
        # Add Text type to __all__ if it was generated as Literal
        if len(unique_texts) <= 200:
            lines.append(
                f"__all__ = ['{type_name}', '{text_type_name}', '{type_name}CategoryData', '{var_name}_CATEGORIES']"
            )
        else:
            lines.append(
                f"__all__ = ['{type_name}', '{text_type_name}', '{type_name}CategoryData', '{var_name}_CATEGORIES']"
            )
        lines.append("")

        return "\n".join(lines)

    def save(self) -> None:
        """Generate and save category file."""
        if not self.categories:
            print(f"⚠️  No categories found in {self.schema_path.name}")
            return

        content = self.generate()
        self.output_path.write_text(content, encoding="utf-8")
        print(f"✓ Generated {self.output_path.name}")
        print(f"  - Type: {self.get_type_name()}")
        print(f"  - Categories: {len(self.categories)}")


def main():
    """Generate all category files."""
    script_dir = Path(__file__).parent
    # Find tidas-tools directory
    tidas_tools_schemas = None
    for parent in [script_dir.parent.parent.parent, script_dir.parent.parent]:
        candidate = parent / "tidas-tools" / "src" / "tidas_tools" / "tidas" / "schemas"
        if candidate.exists():
            tidas_tools_schemas = candidate
            break

    if not tidas_tools_schemas:
        print("❌ Could not find tidas-tools schemas directory")
        return 1

    output_dir = script_dir.parent / "src" / "tidas_sdk" / "types"

    category_files = [
        "tidas_contacts_category.json",
        "tidas_flows_elementary_category.json",
        "tidas_flows_product_category.json",
        "tidas_processes_category.json",
        "tidas_flowproperties_category.json",
        "tidas_lciamethods_category.json",
        "tidas_locations_category.json",
        "tidas_sources_category.json",
        "tidas_unitgroups_category.json",
    ]

    print("=" * 60)
    print("GENERATING CLEAN CATEGORY FILES")
    print("=" * 60)
    print(f"Schema directory: {tidas_tools_schemas}")
    print(f"Output directory: {output_dir}")
    print()

    success_count = 0
    error_count = 0

    for filename in category_files:
        schema_path = tidas_tools_schemas / filename
        output_path = output_dir / filename.replace(".json", ".py")

        if schema_path.exists():
            try:
                generator = CategoryGenerator(schema_path, output_path)
                generator.save()
                success_count += 1
                print()
            except Exception as e:
                print(f"✗ Error generating {filename}: {e}")
                import traceback

                traceback.print_exc()
                error_count += 1
                print()
        else:
            print(f"⚠️  Schema not found: {filename}")
            error_count += 1

    print("=" * 60)
    print("CATEGORY GENERATION SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully generated: {success_count} files")
    if error_count > 0:
        print(f"❌ Errors/Warnings: {error_count}")
    print("=" * 60)

    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
