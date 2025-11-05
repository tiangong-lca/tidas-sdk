#!/usr/bin/env python3
"""
Post-process generated type files to fix cross-file references.

This script:
1. Removes duplicate type definitions that should be imported from tidas_data_types
2. Adds import statements from tidas_data_types
3. Replaces type references with the correct imported types
"""

import argparse
import ast
import json
import re
import sys
from pathlib import Path

from loguru import logger


# Classes that should be removed (mapped to their replacement in tidas_data_types)
# Format: (class_name_pattern, replacement_type_name)
CLASS_REMOVALS = {
    # Multi-language types
    "StringMultiLang1Item": "MultiLangItemString",  # Used internally, not directly
    "StringMultiLang1": "StringMultiLang",
    "StringMultiLang2": "StringMultiLang",
    "STMultiLang1Item": "MultiLangItemST",  # Used internally, not directly
    "STMultiLang1": "STMultiLang",
    "STMultiLang2": "STMultiLang",
    "FTMultiLang1Item": "MultiLangItem",  # Used internally, not directly
    "FTMultiLang1": "FTMultiLang",
    "FTMultiLang2": "FTMultiLang",
    # Reference types
    "GlobalReferenceType1": "GlobalReferenceType",
    "GlobalReferenceTypeItem": "GlobalReferenceType",
    # Basic types (these should be removed if they match tidas_data_types exactly)
    "CASNumber": "CASNumber",
    "FT": "FT",
    "ST": "ST",
    "Int5": "Int5",
    "Int6": "Int6",
    "Real": "Real",
    "Perc": "Perc",
    "MatR": "MatR",
    "MatV": "MatV",
    "LevelType": "LevelType",
    "UUID": "UUID",
}

# Types to import (including type aliases)
IMPORT_TYPES = [
    # String types
    "CASNumber",
    "FT",
    "ST",
    "String",
    # Multi-language types
    "MultiLangItem",
    "MultiLangItemString",
    "MultiLangItemST",
    "StringMultiLang",
    "STMultiLang",
    "FTMultiLang",
    # Integer types
    "Int1",
    "Int5",
    "Int6",
    "LevelType",
    # Numeric types
    "Perc",
    "Real",
    "MatR",
    "MatV",
    # Reference types
    "UUID",
    "GlobalReferenceType",
    "GlobalReferenceTypeOrArray",
    # Geographic types
    "GIS",
    # Date/Time types
    "Year",
]


def find_schema_dir() -> Path | None:
    """Find the TIDAS schemas directory.

    Returns:
        Path to schemas directory or None if not found
    """
    # Try to find tidas-tools
    current = Path.cwd()
    for _ in range(5):  # Search up to 5 levels
        tidas_tools = (
            current / "tidas-tools" / "src" / "tidas_tools" / "tidas" / "schemas"
        )
        if tidas_tools.exists():
            return tidas_tools
        current = current.parent
    return None


def extract_category_refs_from_schema(schema: dict) -> set[str]:
    """Recursively extract category schema references from a JSON schema.

    Args:
        schema: JSON schema dictionary

    Returns:
        Set of category schema file names (without .json extension)
    """
    refs = set()

    def traverse(obj):
        if isinstance(obj, dict):
            # Check for $ref
            if "$ref" in obj:
                ref = obj["$ref"]
                # Extract schema name from reference
                # Refs look like: "tidas_locations_category.json" or "./tidas_locations_category.json"
                if ".json" in ref and "category" in ref.lower():
                    # Remove path components and .json extension
                    schema_name = ref.split(".json")[0].split("/")[-1]
                    refs.add(schema_name)

            # Recurse into nested structures
            for value in obj.values():
                traverse(value)
        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(schema)
    return refs


def extract_field_to_category_mapping(
    schema: dict, schema_file_name: str
) -> dict[str, str]:
    """Extract mapping from field names to category module names.

    This function finds:
    1. Direct field references to category schemas (e.g., @location -> tidas_locations_category)
    2. Nested field references (e.g., @classId inside common:class -> tidas_processes_category)

    Args:
        schema: JSON schema dictionary
        schema_file_name: Name of the schema file (e.g., "tidas_processes")

    Returns:
        Dictionary mapping field names (with @ prefix or common: prefix) to category module names
    """
    field_to_category = {}

    def find_category_refs_and_nested_fields(
        obj, parent_path: list[str] = None, category_context: str | None = None
    ):
        """Recursively find properties that reference category schemas and nested fields."""
        if parent_path is None:
            parent_path = []

        current_category = category_context

        if isinstance(obj, dict):
            # Check if this is a property definition with a category $ref
            if "$ref" in obj:
                ref = obj["$ref"]
                if ".json" in ref and "category" in ref.lower():
                    # Extract category module name
                    category_name = ref.split(".json")[0].split("/")[-1]
                    # Get the field name from parent path (the property containing this $ref)
                    if parent_path:
                        field_name = parent_path[-1]
                        field_to_category[field_name] = category_name
                        # Set current category context for nested fields
                        current_category = category_name

            # Check properties
            if "properties" in obj:
                for prop_name, prop_schema in obj["properties"].items():
                    # Special handling for common:class and common:category - they reference categories
                    # and contain @classId/@catId fields that should use those categories
                    if prop_name in ["common:class", "common:category"] and isinstance(
                        prop_schema, dict
                    ):
                        # Check if it has items -> oneOf/anyOf with category refs (via $ref or dependencies)
                        if "items" in prop_schema:
                            items = prop_schema["items"]

                            # Handle items as array (with dependencies in each item)
                            if isinstance(items, list):
                                for item in items:
                                    if isinstance(item, dict):
                                        # Check dependencies for category refs
                                        if "dependencies" in item:
                                            for dep_key, dep_value in item[
                                                "dependencies"
                                            ].items():
                                                if (
                                                    isinstance(dep_value, dict)
                                                    and "$ref" in dep_value
                                                ):
                                                    ref = dep_value["$ref"]
                                                    if (
                                                        ".json" in ref
                                                        and "category" in ref.lower()
                                                    ):
                                                        category_name = ref.split(
                                                            ".json"
                                                        )[0].split("/")[-1]
                                                        # Map the field to this category
                                                        field_to_category[prop_name] = (
                                                            category_name
                                                        )
                                                        # Map @classId or @catId based on field name
                                                        if prop_name == "common:class":
                                                            field_to_category[
                                                                "@classId"
                                                            ] = category_name
                                                            logger.debug(
                                                                f"  Mapped @classId to {category_name} (in common:class via dependencies)"
                                                            )
                                                        elif (
                                                            prop_name
                                                            == "common:category"
                                                        ):
                                                            field_to_category[
                                                                "@catId"
                                                            ] = category_name
                                                            logger.debug(
                                                                f"  Mapped @catId to {category_name} (in common:category via dependencies)"
                                                            )
                                                        current_category = category_name

                            # Handle items as object with oneOf/anyOf (direct $ref approach)
                            elif isinstance(items, dict):
                                # Check for category refs in oneOf/anyOf
                                for key in ["oneOf", "anyOf"]:
                                    if key in items and isinstance(items[key], list):
                                        for option in items[key]:
                                            if isinstance(option, dict):
                                                # Check for direct category $ref
                                                if "$ref" in option:
                                                    ref = option["$ref"]
                                                    if (
                                                        ".json" in ref
                                                        and "category" in ref.lower()
                                                    ):
                                                        category_name = ref.split(
                                                            ".json"
                                                        )[0].split("/")[-1]
                                                        # Map common:class/common:category to this category
                                                        field_to_category[prop_name] = (
                                                            category_name
                                                        )
                                                        # Map @classId or @catId based on field name
                                                        if prop_name == "common:class":
                                                            field_to_category[
                                                                "@classId"
                                                            ] = category_name
                                                        elif (
                                                            prop_name
                                                            == "common:category"
                                                        ):
                                                            field_to_category[
                                                                "@catId"
                                                            ] = category_name
                                                        # Set category context for nested fields
                                                        current_category = category_name
                                                # Also check for @classId/@catId inside the option
                                                elif "properties" in option:
                                                    # Look for @classId/@catId in this option and use category context
                                                    if (
                                                        current_category
                                                        and "@classId"
                                                        in option["properties"]
                                                        and prop_name == "common:class"
                                                    ):
                                                        field_to_category[
                                                            "@classId"
                                                        ] = current_category
                                                        logger.debug(
                                                            f"  Mapped @classId to {current_category} (in common:class)"
                                                        )
                                                    elif (
                                                        current_category
                                                        and "@catId"
                                                        in option["properties"]
                                                        and prop_name
                                                        == "common:category"
                                                    ):
                                                        field_to_category["@catId"] = (
                                                            current_category
                                                        )
                                                        logger.debug(
                                                            f"  Mapped @catId to {current_category} (in common:category)"
                                                        )
                                                # Recurse into option to find nested fields
                                                if current_category:
                                                    find_category_refs_and_nested_fields(
                                                        option,
                                                        parent_path
                                                        + [prop_name, "items", key],
                                                        current_category,
                                                    )

                    # If we're inside a category context and this is @classId or @catId,
                    # map it to the current category
                    if current_category and prop_name in ["@classId", "@catId"]:
                        field_to_category[prop_name] = current_category
                        logger.debug(
                            f"  Mapped {prop_name} to {current_category} (in category context)"
                        )

                    # Recurse with category context
                    find_category_refs_and_nested_fields(
                        prop_schema,
                        parent_path + [prop_name],
                        current_category,
                    )

            # Check $defs (definitions)
            if "$defs" in obj:
                for def_name, def_schema in obj["$defs"].items():
                    find_category_refs_and_nested_fields(
                        def_schema, [def_name], current_category
                    )

            # Check allOf, anyOf, oneOf - preserve category context
            for key in ["allOf", "anyOf", "oneOf"]:
                if key in obj and isinstance(obj[key], list):
                    for item in obj[key]:
                        find_category_refs_and_nested_fields(
                            item, parent_path, current_category
                        )

            # Check items (for arrays) - preserve category context
            if "items" in obj:
                find_category_refs_and_nested_fields(
                    obj["items"], parent_path, current_category
                )

            # Recurse into other values
            for key, value in obj.items():
                if key not in [
                    "properties",
                    "$defs",
                    "allOf",
                    "anyOf",
                    "oneOf",
                    "$ref",
                    "items",
                ]:
                    find_category_refs_and_nested_fields(
                        value, parent_path, current_category
                    )

        elif isinstance(obj, list):
            for item in obj:
                find_category_refs_and_nested_fields(
                    item, parent_path, current_category
                )

    find_category_refs_and_nested_fields(schema)
    return field_to_category


def build_entity_to_category_map(
    schema_dir: Path,
) -> tuple[dict[str, list[str]], dict[str, dict[str, str]]]:
    """Build mapping from entity files to their category dependencies by analyzing schemas.

    Args:
        schema_dir: Path to directory containing JSON schemas

    Returns:
        Tuple of:
        - Dictionary mapping entity file names to list of category module names
        - Dictionary mapping entity file names to field-to-category mappings
    """
    entity_to_category = {}
    entity_field_mappings = {}

    # Find all entity schema files (not category files)
    entity_schemas = sorted(schema_dir.glob("tidas_*.json"))
    entity_schemas = [
        f
        for f in entity_schemas
        if "_category.json" not in f.name and "data_types.json" not in f.name
    ]

    for schema_file in entity_schemas:
        try:
            with open(schema_file, encoding="utf-8") as f:
                schema = json.load(f)

            # Extract category references
            category_refs = extract_category_refs_from_schema(schema)

            # Extract field-to-category mappings
            field_mapping = extract_field_to_category_mapping(schema, schema_file.stem)

            if category_refs:
                entity_name = schema_file.stem  # e.g., "tidas_processes"
                entity_to_category[entity_name] = sorted(category_refs)
                entity_field_mappings[entity_name] = field_mapping

        except Exception as e:
            logger.warning(f"Failed to analyze schema {schema_file.name}: {e}")

    return entity_to_category, entity_field_mappings


def extract_category_type_name(category_file: Path) -> str | None:
    """Extract the main type name from a category Python file.

    Looks for Literal type alias (e.g., "Locations = Literal[...]")
    or falls back to naming convention.

    Args:
        category_file: Path to category Python file

    Returns:
        Type name (e.g., "Locations") or None if not found
    """
    if not category_file.exists():
        return None

    try:
        content = category_file.read_text(encoding="utf-8")

        # Look for Literal type definition: "Locations = Literal[...]"
        pattern = r"^(\w+)\s*=\s*Literal\["
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            return match.group(1)

        # Fallback: derive from filename
        # tidas_locations_category.py -> Locations
        stem = category_file.stem  # e.g., "tidas_locations_category"
        if stem.startswith("tidas_") and stem.endswith("_category"):
            # Extract middle part: "locations"
            middle = stem[len("tidas_") : -len("_category")]
            # Convert to PascalCase: "Locations"
            return middle.capitalize()

    except Exception as e:
        logger.warning(f"Failed to extract type name from {category_file.name}: {e}")

    return None


def build_category_type_names(types_dir: Path) -> dict[str, str]:
    """Build mapping from category module names to their type names.

    Args:
        types_dir: Path to directory containing generated type files

    Returns:
        Dictionary mapping category module names to type names
    """
    category_type_names = {}

    # Find all category files
    category_files = sorted(types_dir.glob("*_category.py"))

    for category_file in category_files:
        category_module = category_file.stem  # e.g., "tidas_locations_category"
        type_name = extract_category_type_name(category_file)

        if type_name:
            category_type_names[category_module] = type_name

    return category_type_names


# Cache for entity-to-category mapping (built lazily)
_entity_to_category_cache: dict[str, list[str]] | None = None
_entity_field_mappings_cache: dict[str, dict[str, str]] | None = None
_category_type_names_cache: dict[str, str] | None = None


def get_entity_to_category_map(types_dir: Path) -> dict[str, list[str]]:
    """Get entity to category mapping (with caching).

    Args:
        types_dir: Path to directory containing generated type files

    Returns:
        Dictionary mapping entity file names to list of category module names
    """
    global _entity_to_category_cache

    if _entity_to_category_cache is None:
        schema_dir = find_schema_dir()
        if schema_dir:
            entity_map, field_mappings = build_entity_to_category_map(schema_dir)
            _entity_to_category_cache = entity_map
            global _entity_field_mappings_cache
            _entity_field_mappings_cache = field_mappings
            logger.debug(f"Built entity-to-category map: {_entity_to_category_cache}")
            logger.debug(f"Built field mappings: {_entity_field_mappings_cache}")
        else:
            logger.warning("Could not find schema directory, using empty mapping")
            _entity_to_category_cache = {}
            _entity_field_mappings_cache = {}

    return _entity_to_category_cache


def get_entity_field_mappings(types_dir: Path) -> dict[str, dict[str, str]]:
    """Get field-to-category mappings (with caching).

    Args:
        types_dir: Path to directory containing generated type files

    Returns:
        Dictionary mapping entity file names to field-to-category mappings
    """
    global _entity_field_mappings_cache

    # Ensure cache is built
    if _entity_field_mappings_cache is None:
        get_entity_to_category_map(types_dir)

    return _entity_field_mappings_cache or {}


def get_category_type_names(types_dir: Path) -> dict[str, str]:
    """Get category type names mapping (with caching).

    Args:
        types_dir: Path to directory containing generated type files

    Returns:
        Dictionary mapping category module names to type names
    """
    global _category_type_names_cache

    if _category_type_names_cache is None:
        _category_type_names_cache = build_category_type_names(types_dir)
        logger.debug(f"Built category type names map: {_category_type_names_cache}")

    return _category_type_names_cache


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Post-process generated type files to fix cross-file references"
    )

    parser.add_argument(
        "--types-dir",
        type=str,
        default="src/tidas_sdk/types",
        help="Directory containing generated type files (default: src/tidas_sdk/types)",
    )

    parser.add_argument(
        "--skip-data-types",
        action="store_true",
        help="Skip tidas_data_types.py (it's manually maintained)",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without actually modifying files",
    )

    return parser.parse_args()


def setup_logging(verbose: bool) -> None:
    """Configure logging level."""
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.remove()
        logger.add(sys.stderr, level="INFO")


def find_class_end_line(lines: list[str], start_line_idx: int) -> int:
    """Find the end line of a class definition.

    Args:
        lines: List of file lines
        start_line_idx: Starting line index of the class

    Returns:
        End line index (exclusive)
    """
    if start_line_idx >= len(lines):
        return len(lines)

    # Get the indentation of the class
    class_line = lines[start_line_idx]
    indent = len(class_line) - len(class_line.lstrip())

    # Find the next line with same or less indentation that's not blank or comment
    for i in range(start_line_idx + 1, len(lines)):
        line = lines[i]
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):  # Not empty and not comment
            line_indent = len(line) - len(line.lstrip())
            if line_indent <= indent:
                return i

    return len(lines)


def find_classes_to_remove(content: str) -> list[tuple[int, int, str, str]]:
    """Find all class definitions that should be removed.

    Uses AST parsing for accurate identification.

    Returns:
        List of (start_line_idx, end_line_idx, class_name, replacement_type) tuples
        Using line indices instead of character positions for safer deletion
    """
    classes = []
    lines = content.split("\n")

    try:
        tree = ast.parse(content)

        # Collect all class nodes with their line numbers
        class_nodes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_nodes.append(node)

        # Sort by line number
        class_nodes.sort(key=lambda n: n.lineno)

        for node in class_nodes:
            class_name = node.name

            if class_name in CLASS_REMOVALS:
                # Get line index (0-based)
                start_line_idx = node.lineno - 1
                end_line_idx = find_class_end_line(lines, start_line_idx)

                replacement = CLASS_REMOVALS[class_name]
                # Store line indices instead of character positions
                classes.append((start_line_idx, end_line_idx, class_name, replacement))

        # Sort by line number (reverse order for safe removal from end to start)
        classes.sort(key=lambda x: x[0], reverse=True)

    except SyntaxError as e:
        logger.warning(f"Could not parse file with AST: {e}. Falling back to regex.")
        # Fallback to regex-based approach using line numbers
        for class_name, replacement in CLASS_REMOVALS.items():
            pattern = re.compile(
                rf"^class\s+{re.escape(class_name)}\s*[\(:]", re.MULTILINE
            )
            for match in pattern.finditer(content):
                # Find line number from character position
                start_char = match.start()
                start_line_idx = content[:start_char].count("\n")
                end_line_idx = find_class_end_line(lines, start_line_idx)
                classes.append((start_line_idx, end_line_idx, class_name, replacement))
        classes.sort(key=lambda x: x[0], reverse=True)

    return classes


def remove_class_definition_by_lines(
    lines: list[str], start_line_idx: int, end_line_idx: int
) -> list[str]:
    """Remove a class definition from lines using line indices.

    Args:
        lines: List of file lines
        start_line_idx: Starting line index of the class (inclusive)
        end_line_idx: Ending line index of the class (exclusive)

    Returns:
        Modified list of lines
    """
    if start_line_idx >= len(lines) or start_line_idx < 0:
        return lines

    # Find trailing blank lines after the class
    trailing_blank = 0
    for i in range(end_line_idx, min(end_line_idx + 3, len(lines))):
        if not lines[i].strip():
            trailing_blank += 1
        else:
            break

    # Remove the class and trailing blank lines (up to 2)
    lines_to_remove = end_line_idx - start_line_idx + min(trailing_blank, 2)
    return lines[:start_line_idx] + lines[start_line_idx + lines_to_remove :]


def replace_type_references(content: str, old_name: str, new_name: str) -> str:
    """Replace all references to old_name with new_name."""
    if old_name == new_name:
        return content

    # Pattern to match type references (as part of type hints, unions, etc.)
    # Match the name when it's:
    # - Standalone: StringMultiLang1 | StringMultiLang2
    # - In unions: StringMultiLang1 | StringMultiLang2 | str
    # - In type hints: field: StringMultiLang1
    # - In RootModel: RootModel[StringMultiLang1]

    # Word boundary regex (but handle special cases for type hints)
    pattern = r"\b" + re.escape(old_name) + r"\b"

    def replace_func(match):
        # Check if we're in a string (don't replace)
        start = match.start()
        # Simple check: if we're inside quotes, don't replace
        before = content[:start]
        after_quotes = before.count('"') - before.count('\\"')
        if after_quotes % 2 != 0:
            return match.group(0)
        return new_name

    return re.sub(pattern, replace_func, content)


def add_import_statement(
    content: str,
    import_types: list[str],
    category_imports: list[tuple[str, str]] | None = None,
) -> str:
    """Add import statements after existing imports.

    Args:
        content: File content
        import_types: Types to import from tidas_data_types
        category_imports: List of (category_module, type_name) tuples to import
    """
    lines = content.split("\n")

    # Find the position where we should insert new imports
    # If data_types import exists, find its start position
    # Otherwise find the end of all existing imports
    data_types_import_start = -1
    data_types_import_end = -1
    last_import_end_idx = -1
    in_multiline_import = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            last_import_end_idx = i
            # Check if this is a multi-line import
            if "(" in line and ")" not in line:
                in_multiline_import = True
            # Check if this is the data_types import
            if "from tidas_sdk.types.tidas_data_types import" in line:
                data_types_import_start = i
        elif in_multiline_import:
            last_import_end_idx = i
            if ")" in line:
                in_multiline_import = False
                if data_types_import_start != -1:
                    data_types_import_end = i
                break  # Found the end of multi-line import

    # Check if imports already exist
    has_data_types_import = any(
        "from tidas_sdk.types.tidas_data_types import" in line for line in lines
    )

    # Find existing category imports and their imported types
    existing_category_imports: dict[str, set[str]] = {}
    in_multiline_category_import = False
    current_category_module = None

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Check if this line starts a category import
        if "from tidas_sdk.types." in line and "_category import" in line:
            # Extract module name
            parts = line.split("from tidas_sdk.types.")[1].split(" import")[0]
            current_category_module = parts.strip()

            # Check if it's a single-line import: "from ... import TypeName"
            if "(" not in line and ")" not in line:
                # Single type import
                imported_type = line.split("import")[1].strip()
                if current_category_module not in existing_category_imports:
                    existing_category_imports[current_category_module] = set()
                existing_category_imports[current_category_module].add(imported_type)
                current_category_module = None
            elif "(" in line and ")" not in line:
                # Start of multi-line import
                in_multiline_category_import = True
                if current_category_module not in existing_category_imports:
                    existing_category_imports[current_category_module] = set()
            elif ")" in line and in_multiline_category_import:
                # End of multi-line import - extract last type if present
                if current_category_module:
                    last_type = line.split(",")[-1].strip().rstrip(")")
                    if last_type:
                        existing_category_imports[current_category_module].add(
                            last_type
                        )
                in_multiline_category_import = False
                current_category_module = None
        elif in_multiline_category_import and current_category_module:
            # Inside multi-line import - extract type name
            type_name = stripped.rstrip(",").rstrip(")")
            if type_name:
                existing_category_imports[current_category_module].add(type_name)

    # Build import statements
    new_imports = []

    if import_types and not has_data_types_import:
        import_types_str = ",\n    ".join(sorted(import_types))
        import_stmt = f"""from tidas_sdk.types.tidas_data_types import (
    {import_types_str}
)"""
        new_imports.append(import_stmt)

    # Add category imports (before data_types import if it exists)
    # Group imports by module to handle multiple types from same module
    category_imports_by_module: dict[str, list[str]] = {}
    if category_imports:
        for category_module, type_name in category_imports:
            # Check if this specific type already exists in imports
            if (
                category_module in existing_category_imports
                and type_name in existing_category_imports[category_module]
            ):
                logger.debug(
                    f"Category import already exists: {category_module}.{type_name}"
                )
                continue

            if category_module not in category_imports_by_module:
                category_imports_by_module[category_module] = []
            # If module already has imports, merge with existing types
            if category_module in existing_category_imports:
                # Add existing types to the list
                for existing_type in existing_category_imports[category_module]:
                    if existing_type not in category_imports_by_module[category_module]:
                        category_imports_by_module[category_module].append(
                            existing_type
                        )
            category_imports_by_module[category_module].append(type_name)

    # First, update existing category imports to add new types
    # This must happen BEFORE creating new_imports
    modules_to_remove = []
    for category_module, type_names in list(category_imports_by_module.items()):
        if category_module in existing_category_imports:
            # Find the existing import statement
            import_start_idx = -1
            import_end_idx = -1

            for i, line in enumerate(lines):
                if f"from tidas_sdk.types.{category_module} import" in line:
                    import_start_idx = i
                    # Check if it's multi-line
                    if "(" in line and ")" not in line:
                        # Find closing parenthesis
                        for j in range(i + 1, len(lines)):
                            if ")" in lines[j]:
                                import_end_idx = j
                                break
                    else:
                        import_end_idx = i
                    break

            if import_start_idx != -1 and import_end_idx != -1:
                # Always update the import to include all types in type_names
                # Multi-line import (always use multi-line when we have multiple types)
                type_names_str = ",\n    ".join(sorted(type_names))
                new_import_lines = [
                    f"from tidas_sdk.types.{category_module} import (",
                    f"    {type_names_str}",
                    ")",
                ]
                if import_end_idx > import_start_idx:
                    # Replace existing multi-line import
                    lines[import_start_idx : import_end_idx + 1] = new_import_lines
                else:
                    # Convert single-line to multi-line
                    lines[import_start_idx] = new_import_lines[0]
                    lines.insert(import_start_idx + 1, new_import_lines[1])
                    lines.insert(import_start_idx + 2, new_import_lines[2])

                # Remove from category_imports_by_module so we don't add it again
                del category_imports_by_module[category_module]

    # Now create import statements for modules that don't exist yet
    new_imports = []

    if import_types and not has_data_types_import:
        import_types_str = ",\n    ".join(sorted(import_types))
        import_stmt = f"""from tidas_sdk.types.tidas_data_types import (
    {import_types_str}
)"""
        new_imports.append(import_stmt)

    # Add remaining category imports (those not already in file)
    for category_module, type_names in category_imports_by_module.items():
        if len(type_names) == 1:
            category_import_stmt = (
                f"from tidas_sdk.types.{category_module} import {type_names[0]}"
            )
            new_imports.append(category_import_stmt)
        else:
            # Multiple types from same module - use multi-line import
            type_names_str = ",\n    ".join(sorted(type_names))
            category_import_stmt = f"""from tidas_sdk.types.{category_module} import (
    {type_names_str}
)"""
            new_imports.append(category_import_stmt)

    if new_imports:
        # Separate category imports and data_types import
        category_imports_list = [imp for imp in new_imports if "_category" in imp]
        data_types_import = [imp for imp in new_imports if "tidas_data_types" in imp]

        # If data_types import exists, insert category imports before it
        if data_types_import_start != -1 and category_imports_list:
            # Insert category imports before data_types import
            insert_idx = data_types_import_start
            for category_import in reversed(
                category_imports_list
            ):  # Reverse to maintain order
                lines.insert(insert_idx, "")
                lines.insert(insert_idx, category_import)

        # If no data_types import but we need to add it, or if we only have category imports
        elif last_import_end_idx != -1:
            # Insert after the last import
            insert_idx = last_import_end_idx + 1
            # Insert category imports first
            for category_import in category_imports_list:
                lines.insert(insert_idx, category_import)
                insert_idx += 1
                lines.insert(insert_idx, "")
                insert_idx += 1
            # Then insert data_types import if needed
            for data_import in data_types_import:
                lines.insert(insert_idx, data_import)
                insert_idx += 1
                lines.insert(insert_idx, "")
                insert_idx += 1
        else:
            # No imports found, add after the header comment
            insert_idx = 2  # After "# generated by datamodel-codegen" lines
            # Insert category imports first
            for category_import in category_imports_list:
                lines.insert(insert_idx, category_import)
                insert_idx += 1
                lines.insert(insert_idx, "")
                insert_idx += 1
            # Then insert data_types import if needed
            for data_import in data_types_import:
                lines.insert(insert_idx, data_import)
                insert_idx += 1
                lines.insert(insert_idx, "")
                insert_idx += 1

    return "\n".join(lines)


def post_process_file(file_path: Path, dry_run: bool = False) -> dict:
    """Post-process a single type file.

    Returns:
        Dictionary with statistics about changes made
    """
    logger.info(f"Processing {file_path.name}")

    content = file_path.read_text(encoding="utf-8")
    original_content = content
    stats = {
        "classes_removed": 0,
        "types_replaced": 0,
        "import_added": False,
    }

    # Track which types are actually used in this file
    used_import_types = set()

    # Step 1: Find and remove duplicate class definitions (before replacing references)
    # This must happen first, while class names are still in their original form
    classes_to_remove = find_classes_to_remove(content)

    if classes_to_remove and not dry_run:
        # Work with lines for safer deletion
        lines = content.split("\n")

        # Remove classes from end to start to maintain line indices
        for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
            logger.debug(
                f"  Removing class: {class_name} (replaced with {replacement})"
            )
            lines = remove_class_definition_by_lines(
                lines, start_line_idx, end_line_idx
            )
            stats["classes_removed"] += 1
            used_import_types.add(replacement)

            # For multi-language types, also need the item types
            if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if replacement == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif replacement == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif replacement == "FTMultiLang":
                    used_import_types.add("MultiLangItem")

        # Reconstruct content from lines
        content = "\n".join(lines)
    elif classes_to_remove:
        # Dry run: just count
        for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
            logger.debug(
                f"  Would remove class: {class_name} (replaced with {replacement})"
            )
            stats["classes_removed"] += 1
            used_import_types.add(replacement)

            # For multi-language types, also need the item types
            if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if replacement == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif replacement == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif replacement == "FTMultiLang":
                    used_import_types.add("MultiLangItem")

    # Step 2: Replace type references (after removing class definitions)
    # Now it's safe to replace references without affecting class names
    for old_name, new_name in CLASS_REMOVALS.items():
        if old_name in content:
            logger.debug(f"  Replacing type reference: {old_name} -> {new_name}")
            if not dry_run:
                content = replace_type_references(content, old_name, new_name)
            stats["types_replaced"] += 1
            used_import_types.add(new_name)

            # For multi-language types, also need the item types
            if new_name in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if new_name == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif new_name == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif new_name == "FTMultiLang":
                    used_import_types.add("MultiLangItem")

    # Step 2.5: Clean up duplicate union types (e.g., "Type | Type" -> "Type")
    if not dry_run:
        import re
        original_before_cleanup = content
        # Match and remove adjacent duplicate types in unions
        content = re.sub(
            r'\b(\w+)\s*\|\s*\1\b',  # Match "TypeName | TypeName"
            r'\1',  # Replace with just "TypeName"
            content
        )
        if content != original_before_cleanup:
            logger.debug("  Cleaned up duplicate union types")

    # Step 3: Detect category imports needed (auto-detected from schemas)
    category_imports = []
    file_stem = file_path.stem  # e.g., "tidas_processes"

    # Get entity-to-category mapping (auto-detected from schemas)
    types_dir = file_path.parent
    entity_to_category_map = get_entity_to_category_map(types_dir)
    category_type_names = get_category_type_names(types_dir)
    entity_field_mappings = get_entity_field_mappings(types_dir)

    if file_stem in entity_to_category_map:
        for category_module in entity_to_category_map[file_stem]:
            if category_module in category_type_names:
                type_name = category_type_names[category_module]
                category_imports.append((category_module, type_name))
                logger.debug(f"  Will import {type_name} from {category_module}")

    # Step 3.5: Replace field types with imported category types
    # Get field mappings for this entity
    if file_stem in entity_field_mappings:
        field_mapping = entity_field_mappings[file_stem]

        for field_name, category_module in field_mapping.items():
            if category_module in category_type_names:
                category_type = category_type_names[category_module]

                # Convert schema field name to Python field name
                # "@location" -> "field_location"
                # "@classId" -> "field_classId"
                # "@catId" -> "field_catId"
                # "common:class" -> "field_classId" (for classes within common:class array items)
                # "common:category" -> "field_catId" (for classes within common:category array items)
                # Handle other fields like "locationOfSupply" -> "locationOfSupply"
                python_field_names = []

                # Handle @ prefixed fields (e.g., @location, @classId, @catId)
                if field_name.startswith("@"):
                    python_field_names.append(f"field_{field_name[1:]}")
                # Handle common:class - map to field_classId (used in array item classes)
                elif field_name == "common:class":
                    python_field_names.append("field_classId")
                # Handle common:category - map to field_catId (used in array item classes)
                elif field_name == "common:category":
                    python_field_names.append("field_catId")
                # Handle other common: prefixed fields
                elif field_name.startswith("common:"):
                    python_field_names.append(f"common_{field_name[7:]}")
                # Handle other fields (camelCase, usually unchanged in Python)
                else:
                    python_field_names.append(field_name)

                # Replace field type: str -> CategoryType for all matching field names
                for python_field_name in python_field_names:
                    # First, fix any corrupted content (e.g., "strFlowsElementary" -> "FlowsElementary")
                    # This can happen if previous replacement went wrong
                    fix_corrupted_pattern = rf"(\s+{re.escape(python_field_name)}:\s+)str{re.escape(category_type)}(\s*(?:Field|=))"
                    if re.search(fix_corrupted_pattern, content):
                        if not dry_run:
                            content = re.sub(
                                fix_corrupted_pattern,
                                rf"\1{category_type}\2",
                                content,
                            )
                            logger.debug(
                                f"  Fixed corrupted field type for {python_field_name}"
                            )

                    # Pattern: field_name: str = Field(..., alias='...')
                    # Also handle union types: field_name: str | None
                    # Be careful with word boundaries to avoid partial matches
                    patterns = [
                        # Simple type annotation: field_name: str = Field(...)
                        (rf"(\s+{re.escape(python_field_name)}:\s+)str(\s*=)", True),
                        # Union type with str first: field_name: str | Type
                        (
                            rf"(\s+{re.escape(python_field_name)}:\s+)str(\s*\|\s*\w)",
                            True,
                        ),
                        # Union type with str: field_name: Type | str
                        (
                            rf"(\s+{re.escape(python_field_name)}:\s+\w+\s*\|\s*)str(\s*=)",
                            True,
                        ),
                        # Optional str: field_name: str | None
                        (
                            rf"(\s+{re.escape(python_field_name)}:\s+)str(\s*\|\s*None)",
                            True,
                        ),
                    ]

                    replaced = False
                    for pattern, simple_replacement in patterns:
                        matches = list(re.finditer(pattern, content))
                        if matches:
                            if not dry_run:
                                # Replace all occurrences (work backwards to maintain positions)
                                for match in reversed(matches):
                                    if simple_replacement:
                                        # Simple replacement: str -> CategoryType
                                        # pattern group 1 is before "str", group 2 is after "str"
                                        start, end = match.span()

                                        # For patterns like (\s+field_name:\s+)str(\s*=)
                                        # group(1) = "    field_name: "
                                        # group(2) = " ="
                                        # "str" is between group(1) and group(2)
                                        # We want: "    field_name: " + "FlowsElementary" + " ="
                                        if len(match.groups()) >= 2:
                                            before_str = match.group(
                                                1
                                            )  # e.g., "    field_name: "
                                            after_str = match.group(2)  # e.g., " ="
                                            replacement = (
                                                before_str + category_type + after_str
                                            )
                                        else:
                                            # Fallback: replace "str" in the matched string
                                            matched_text = match.group(0)
                                            replacement = matched_text.replace(
                                                "str", category_type, 1
                                            )

                                        content = (
                                            content[:start]
                                            + replacement
                                            + content[end:]
                                        )
                                    replaced = True

                            if replaced:
                                stats["types_replaced"] += len(matches)
                                logger.debug(
                                    f"  Replaced {len(matches)} occurrences of {python_field_name}: str with {category_type}"
                                )
                                break

    # Step 3.6: Replace text field types based on category context
    # If a class has field_catId or field_classId with a category type,
    # replace text: str with the corresponding Text type
    if file_stem in entity_field_mappings:
        field_mapping = entity_field_mappings[file_stem]

        # Map category modules to their Text types
        # Text types are auto-generated by generate_category_types.py
        # Format: Tidas{TypeName}Text (e.g., TidasFlowsElementaryText)
        category_text_types = {}
        for category_module, type_name in category_type_names.items():
            if category_module.endswith("_category"):
                # Generate Text type name: Tidas + TypeName + Text
                # e.g., FlowsElementary -> TidasFlowsElementaryText
                text_type_name = f"Tidas{type_name}Text"
                category_text_types[category_module] = text_type_name

                # Verify the Text type exists in the category file
                category_file = types_dir / f"{category_module}.py"
                if category_file.exists():
                    category_content = category_file.read_text(encoding="utf-8")
                    if text_type_name not in category_content:
                        # Text type might not exist yet (will be generated by generate_category_types.py)
                        logger.debug(
                            f"  Text type {text_type_name} not found in {category_module}.py (may need regeneration)"
                        )

        # Find classes with category fields and replace their text fields
        # Pattern: class ClassName(BaseModel): ... field_catId: CategoryType ... text: str
        class_pattern = r"class\s+(\w+)\s*\([^)]*\):"
        classes = list(re.finditer(class_pattern, content))

        # Collect all classes that need text replacement first
        classes_to_update = []
        for class_match in classes:
            class_name = class_match.group(1)
            class_start = class_match.end()

            # Find the end of this class (next class or end of file)
            next_class_match = None
            for next_match in classes:
                if next_match.start() > class_start:
                    next_class_match = next_match
                    break

            class_end = next_class_match.start() if next_class_match else len(content)
            class_content = content[class_start:class_end]

            # Check if this class has field_catId or field_classId with category type
            text_type_to_use = None
            category_module_to_import = None

            # Check for field_catId: CategoryType
            catid_pattern = r"field_catId:\s*(\w+)\s*="
            catid_match = re.search(catid_pattern, class_content)
            if catid_match:
                catid_type = catid_match.group(1)
                # Find which category module this type comes from
                for cat_module, type_name in category_type_names.items():
                    if type_name == catid_type and cat_module in category_text_types:
                        text_type_to_use = category_text_types[cat_module]
                        category_module_to_import = cat_module
                        break

            # Check for field_classId: CategoryType
            if not text_type_to_use:
                classid_pattern = r"field_classId:\s*(\w+)\s*="
                classid_match = re.search(classid_pattern, class_content)
                if classid_match:
                    classid_type = classid_match.group(1)
                    # Find which category module this type comes from
                    for cat_module, type_name in category_type_names.items():
                        if (
                            type_name == classid_type
                            and cat_module in category_text_types
                        ):
                            text_type_to_use = category_text_types[cat_module]
                            category_module_to_import = cat_module
                            break

            # Check if text field needs to be replaced or already uses Text type
            if text_type_to_use:
                text_pattern = r"(\s+text:\s+)str(\s*=)"
                text_match = re.search(text_pattern, class_content)
                if text_match:
                    # text: str needs to be replaced
                    classes_to_update.append(
                        {
                            "name": class_name,
                            "start": class_start,
                            "end": class_end,
                            "content": class_content,
                            "text_type": text_type_to_use,
                            "category_module": category_module_to_import,
                            "text_match": text_match,
                        }
                    )
                else:
                    # Check if text field already uses the Text type
                    # This ensures we add the import even if text was already replaced
                    text_type_pattern = (
                        rf"(\s+text:\s+){re.escape(text_type_to_use)}(\s*=)"
                    )
                    if re.search(text_type_pattern, class_content):
                        # Text type is already used, ensure import is added
                        if category_module_to_import:
                            text_type_name = category_text_types[
                                category_module_to_import
                            ]
                            # Check if this specific Text type is already in category_imports
                            text_type_already_imported = any(
                                m == category_module_to_import and t == text_type_name
                                for m, t in category_imports
                            )
                            if not text_type_already_imported:
                                # Add the Text type to imports (main type may already be there)
                                category_imports.append(
                                    (category_module_to_import, text_type_name)
                                )
                                logger.debug(
                                    f"  Ensured import for {text_type_name} (already used in {class_name})"
                                )

        # Now replace in reverse order to avoid index shifts
        for class_info in reversed(classes_to_update):

            class_name = class_info["name"]
            class_start = class_info["start"]
            text_type_to_use = class_info["text_type"]
            category_module_to_import = class_info["category_module"]
            text_match = class_info["text_match"]

            # Replace text: str with text: TextType
            if not dry_run:
                # Calculate absolute position in full content
                abs_match_start = class_start + text_match.start()
                abs_match_end = class_start + text_match.end()

                # Replace str with text_type_to_use
                replacement = (
                    f"{text_match.group(1)}{text_type_to_use}{text_match.group(2)}"
                )
                content = (
                    content[:abs_match_start] + replacement + content[abs_match_end:]
                )
            stats["types_replaced"] += 1
            logger.debug(
                f"  Replaced text: str with {text_type_to_use} in {class_name}"
            )

            # Track that we need to import this Text type
            if category_module_to_import:
                # Add Text type to imports (we'll handle this in Step 4)
                text_type_name = category_text_types[category_module_to_import]
                # Check if this specific Text type is already in category_imports
                text_type_already_imported = any(
                    m == category_module_to_import and t == text_type_name
                    for m, t in category_imports
                )
                if not text_type_already_imported:
                    # Add Text type to imports (main type may already be there)
                    category_imports.append((category_module_to_import, text_type_name))
                    logger.debug(
                        f"  Added import for {text_type_name} (replaced text in {class_name})"
                    )

    # Step 4: Add import statements if needed
    if used_import_types or category_imports:
        # Add all potentially needed imports (we import more than strictly needed for safety)
        if not dry_run:
            content = add_import_statement(
                content,
                IMPORT_TYPES if used_import_types else [],
                category_imports if category_imports else None,
            )
        stats["import_added"] = True
        logger.debug(
            f"  Added import for {len(used_import_types)} base types and {len(category_imports)} category types"
        )

    # Step 4: Write file if changed
    if content != original_content:
        if not dry_run:
            file_path.write_text(content, encoding="utf-8")
            logger.info(f"  ✅ Updated {file_path.name}")
        else:
            logger.info(f"  📝 Would update {file_path.name}")
    else:
        logger.debug(f"  No changes needed for {file_path.name}")

    return stats


def main() -> int:
    """Main entry point."""
    args = parse_args()
    setup_logging(args.verbose)

    types_dir = Path(args.types_dir)
    if not types_dir.exists():
        logger.error(f"Types directory not found: {types_dir}")
        return 1

    # Find all generated type files
    type_files = sorted(types_dir.glob("tidas_*.py"))

    if args.skip_data_types:
        type_files = [f for f in type_files if f.name != "tidas_data_types.py"]

    logger.info(f"Found {len(type_files)} type files to process")

    if args.dry_run:
        logger.info("🔍 DRY RUN MODE - No files will be modified")

    total_stats = {
        "files_processed": 0,
        "files_modified": 0,
        "total_classes_removed": 0,
        "total_types_replaced": 0,
    }

    for type_file in type_files:
        try:
            stats = post_process_file(type_file, dry_run=args.dry_run)
            total_stats["files_processed"] += 1
            if (
                stats["classes_removed"] > 0
                or stats["types_replaced"] > 0
                or stats["import_added"]
            ):
                total_stats["files_modified"] += 1
            total_stats["total_classes_removed"] += stats["classes_removed"]
            total_stats["total_types_replaced"] += stats["types_replaced"]
        except Exception as e:
            logger.error(f"Error processing {type_file.name}: {e}")
            if args.verbose:
                import traceback

                traceback.print_exc()
            return 1

    # Print summary
    print("\n" + "=" * 60)
    print("POST-PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Files processed:    {total_stats['files_processed']}")
    print(f"Files modified:     {total_stats['files_modified']}")
    print(f"Classes removed:    {total_stats['total_classes_removed']}")
    print(f"Type references replaced: {total_stats['total_types_replaced']}")
    print("=" * 60)

    if args.dry_run:
        print("\n🔍 This was a dry run. Use without --dry-run to apply changes.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
