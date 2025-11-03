#!/usr/bin/env python3
"""Test script for type mapper."""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from type_mapper import TypeMapper


def test_basic_types() -> None:
    """Test basic JSON Schema type mappings."""
    mapper = TypeMapper()

    # String
    result = mapper.map_type({"type": "string"}, "name")
    assert result == "str", f"Expected 'str', got '{result}'"

    # Integer
    result = mapper.map_type({"type": "integer"}, "count")
    assert result == "int", f"Expected 'int', got '{result}'"

    # Number
    result = mapper.map_type({"type": "number"}, "value")
    assert result == "float", f"Expected 'float', got '{result}'"

    # Boolean
    result = mapper.map_type({"type": "boolean"}, "active")
    assert result == "bool", f"Expected 'bool', got '{result}'"

    print("✅ Basic types test passed")


def test_format_types() -> None:
    """Test format-specific type mappings."""
    mapper = TypeMapper()

    # UUID
    result = mapper.map_type({"type": "string", "format": "uuid"}, "id")
    assert result == "UUID", f"Expected 'UUID', got '{result}'"
    assert "from uuid import UUID" in mapper.get_imports()

    # DateTime
    mapper.reset_imports()
    result = mapper.map_type({"type": "string", "format": "date-time"}, "created")
    assert result == "datetime", f"Expected 'datetime', got '{result}'"
    assert "from datetime import datetime" in mapper.get_imports()

    print("✅ Format types test passed")


def test_array_types() -> None:
    """Test array type mappings."""
    mapper = TypeMapper()

    # Array of strings
    result = mapper.map_type({"type": "array", "items": {"type": "string"}}, "tags")
    assert result == "List[str]", f"Expected 'List[str]', got '{result}'"
    assert "from typing import List" in mapper.get_imports()

    # Array of integers
    mapper.reset_imports()
    result = mapper.map_type({"type": "array", "items": {"type": "integer"}}, "counts")
    assert result == "List[int]", f"Expected 'List[int]', got '{result}'"

    print("✅ Array types test passed")


def test_optional_types() -> None:
    """Test optional (nullable) type mappings."""
    mapper = TypeMapper()

    # Type array with null
    result = mapper.map_type({"type": ["string", "null"]}, "optional_name")
    assert result == "Optional[str]", f"Expected 'Optional[str]', got '{result}'"
    assert "from typing import Optional" in mapper.get_imports()

    print("✅ Optional types test passed")


def test_field_constraints() -> None:
    """Test extraction of Field() constraints."""
    mapper = TypeMapper()

    # String with constraints
    constraints = mapper.extract_field_constraints({
        "type": "string",
        "maxLength": 100,
        "pattern": "^[a-z]+$",
        "description": "Lowercase letters only"
    })

    assert constraints["max_length"] == 100
    assert constraints["pattern"] == "^[a-z]+$"
    assert constraints["description"] == "Lowercase letters only"
    assert "from pydantic import Field" in mapper.get_imports()

    # Integer with range
    mapper.reset_imports()
    constraints = mapper.extract_field_constraints({
        "type": "integer",
        "minimum": 0,
        "maximum": 100
    })

    assert constraints["ge"] == 0
    assert constraints["le"] == 100

    print("✅ Field constraints test passed")


def test_enum_types() -> None:
    """Test enum to Literal conversion."""
    mapper = TypeMapper()

    # String enum
    result = mapper.handle_enum(["active", "inactive", "pending"])
    assert result == 'Literal["active", "inactive", "pending"]', f"Expected Literal enum, got '{result}'"
    assert "from typing import Literal" in mapper.get_imports()

    # Number enum
    mapper.reset_imports()
    result = mapper.handle_enum([1, 2, 3])
    assert result == "Literal[1, 2, 3]", f"Expected Literal numbers, got '{result}'"

    print("✅ Enum types test passed")


def test_union_types() -> None:
    """Test oneOf/anyOf to Union conversion."""
    mapper = TypeMapper()

    # Union of different types
    schemas = [
        {"type": "string"},
        {"type": "integer"}
    ]
    result = mapper.handle_union(schemas)
    assert result == "Union[str, int]", f"Expected 'Union[str, int]', got '{result}'"
    assert "from typing import Union" in mapper.get_imports()

    print("✅ Union types test passed")


def test_required_check() -> None:
    """Test required field checking."""
    mapper = TypeMapper()

    required_fields = ["name", "email"]

    assert mapper.is_required("name", required_fields) is True
    assert mapper.is_required("age", required_fields) is False

    print("✅ Required check test passed")


def test_import_management() -> None:
    """Test import tracking and deduplication."""
    mapper = TypeMapper()

    # Generate multiple types that need imports
    mapper.map_type({"type": "string", "format": "uuid"}, "id1")
    mapper.map_type({"type": "string", "format": "uuid"}, "id2")
    mapper.map_type({"type": "array", "items": {"type": "string"}}, "tags")

    imports = mapper.get_imports()

    # Should have UUID, List imports (deduplicated)
    assert "from uuid import UUID" in imports
    assert "from typing import List" in imports
    assert len([i for i in imports if "UUID" in i]) == 1  # Only one UUID import

    # Should be sorted
    assert imports == sorted(imports)

    print("✅ Import management test passed")


def main() -> int:
    """Run all tests."""
    tests = [
        test_basic_types,
        test_format_types,
        test_array_types,
        test_optional_types,
        test_field_constraints,
        test_enum_types,
        test_union_types,
        test_required_check,
        test_import_management,
    ]

    print("Running type mapper tests...\n")

    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"❌ Test failed: {test.__name__}")
            print(f"   Error: {e}")
            return 1
        except Exception as e:
            print(f"❌ Test error: {test.__name__}")
            print(f"   Error: {e}")
            return 1

    print("\n" + "=" * 60)
    print("✅ All type mapper tests passed!")
    print("=" * 60)
    print(f"\nRequired imports example:")

    # Show example of collected imports
    mapper = TypeMapper()
    mapper.map_type({"type": "string", "format": "uuid"}, "id")
    mapper.map_type({"type": "array", "items": {"type": "integer"}}, "values")
    mapper.extract_field_constraints({"maxLength": 100})

    for imp in mapper.get_imports():
        print(f"  {imp}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
