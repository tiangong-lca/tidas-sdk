#!/usr/bin/env python3
"""Test script for code generator."""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from code_generator import CodeGenerator


def test_simple_model() -> None:
    """Test simple model generation."""
    generator = CodeGenerator()

    # Define a simple schema
    properties = {
        "uuid": {"type": "string", "format": "uuid"},
        "name": {"type": "string", "maxLength": 100},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string"},
    }
    required = ["uuid", "name"]

    # Generate code
    code = generator.generate_model(
        model_name="Person",
        properties=properties,
        required=required,
        description="A person entity",
    )

    print("Generated code:")
    print(code)
    print()

    # Verify it's valid Python
    try:
        compile(code, "<generated>", "exec")
        print("✅ Generated code is syntactically valid!")
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        raise

    # Check key components
    assert "class Person(BaseModel):" in code
    assert "uuid: UUID" in code
    assert "name: str" in code
    assert "age: Optional[int]" in code
    assert "Field(max_length=100)" in code
    assert "Field(default=None, ge=0)" in code or "Field(ge=0" in code
    assert '"""A person entity"""' in code

    print("✅ Simple model test passed")


def test_model_with_arrays() -> None:
    """Test model with array fields."""
    generator = CodeGenerator()

    properties = {
        "tags": {"type": "array", "items": {"type": "string"}},
        "scores": {"type": "array", "items": {"type": "integer"}},
    }
    required = []

    code = generator.generate_model(
        model_name="Tagged", properties=properties, required=required
    )

    # Verify array types
    assert "List[str]" in code
    assert "List[int]" in code
    assert "Optional[List[" in code  # Should be optional

    print("✅ Array model test passed")


def test_model_with_optional_fields() -> None:
    """Test model with optional fields."""
    generator = CodeGenerator()

    properties = {
        "required_field": {"type": "string"},
        "optional_field": {"type": "string"},
    }
    required = ["required_field"]

    code = generator.generate_model(
        model_name="OptionalTest", properties=properties, required=required
    )

    # Required field should not be Optional
    assert "required_field: str" in code

    # Optional field should be Optional
    assert "optional_field: Optional[str]" in code

    print("✅ Optional fields test passed")


def test_model_with_constraints() -> None:
    """Test model with field constraints."""
    generator = CodeGenerator()

    properties = {
        "username": {
            "type": "string",
            "minLength": 3,
            "maxLength": 20,
            "pattern": "^[a-zA-Z0-9_]+$",
            "description": "Username must be alphanumeric",
        },
        "score": {"type": "integer", "minimum": 0, "maximum": 100},
    }
    required = ["username"]

    code = generator.generate_model(
        model_name="User", properties=properties, required=required
    )

    # Check constraints are present
    assert "min_length=3" in code
    assert "max_length=20" in code
    assert 'pattern="^[a-zA-Z0-9_]+$"' in code
    assert "description=" in code
    assert "ge=0" in code
    assert "le=100" in code

    print("✅ Constraints test passed")


def test_field_aliases() -> None:
    """Test handling of field names with special characters."""
    generator = CodeGenerator()

    properties = {
        "common:UUID": {"type": "string", "format": "uuid"},
        "common:name": {"type": "string"},
    }
    required = ["common:UUID"]

    code = generator.generate_model(
        model_name="AliasTest", properties=properties, required=required
    )

    # Field names should be sanitized
    assert "common_UUID" in code or "common_name" in code

    # Should have alias
    assert 'alias="common:UUID"' in code or 'alias="common:name"' in code

    print("✅ Field aliases test passed")


def test_file_header() -> None:
    """Test file header generation."""
    generator = CodeGenerator()

    header = generator.generate_file_header("tidas_contacts")

    assert "Generated Pydantic models" in header
    assert "tidas_contacts.json" in header
    assert "DO NOT EDIT" in header
    assert '"""' in header

    print("✅ File header test passed")


def test_complete_module() -> None:
    """Test complete module generation with multiple models."""
    generator = CodeGenerator()

    models = [
        {
            "name": "Address",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
            },
            "required": ["city"],
            "description": "An address",
        },
        {
            "name": "Person",
            "properties": {
                "name": {"type": "string"},
                "address": {"type": "object"},
            },
            "required": ["name"],
            "description": "A person with address",
        },
    ]

    code = generator.generate_module("test_schema", models)

    # Should have header
    assert "Generated Pydantic models" in code

    # Should have both classes
    assert "class Address(BaseModel):" in code
    assert "class Person(BaseModel):" in code

    # Should be valid Python
    try:
        compile(code, "<generated>", "exec")
        print("✅ Complete module is valid Python")
    except SyntaxError as e:
        print(f"❌ Module syntax error: {e}")
        raise

    print("✅ Complete module test passed")


def test_nested_model_detection() -> None:
    """Test detection of nested objects that need separate models."""
    generator = CodeGenerator()

    # Small nested object (should not extract)
    properties_small = {
        "simple": {
            "type": "object",
            "properties": {"a": {"type": "string"}, "b": {"type": "integer"}},
        }
    }

    nested_small = generator.extract_nested_models(properties_small)
    assert len(nested_small) == 0, "Small nested objects should not be extracted"

    # Large nested object (should extract)
    properties_large = {
        "complex": {
            "type": "object",
            "properties": {
                "field1": {"type": "string"},
                "field2": {"type": "string"},
                "field3": {"type": "string"},
                "field4": {"type": "string"},
                "field5": {"type": "integer"},
            },
        }
    }

    nested_large = generator.extract_nested_models(properties_large)
    assert len(nested_large) == 1, "Large nested objects should be extracted"
    assert nested_large[0]["name"] == "Complex"

    print("✅ Nested model detection test passed")


def test_imports_included() -> None:
    """Test that necessary imports are included."""
    generator = CodeGenerator()

    properties = {
        "id": {"type": "string", "format": "uuid"},
        "created": {"type": "string", "format": "date-time"},
        "tags": {"type": "array", "items": {"type": "string"}},
    }
    required = []

    code = generator.generate_model("Test", properties, required)

    # Check imports
    assert "from typing import" in code
    assert "from pydantic import" in code
    assert "from uuid import UUID" in code
    assert "from datetime import datetime" in code

    print("✅ Imports test passed")


def main() -> int:
    """Run all tests."""
    tests = [
        test_simple_model,
        test_model_with_arrays,
        test_model_with_optional_fields,
        test_model_with_constraints,
        test_field_aliases,
        test_file_header,
        test_complete_module,
        test_nested_model_detection,
        test_imports_included,
    ]

    print("Running code generator tests...\n")
    print("=" * 60)

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
            import traceback

            traceback.print_exc()
            return 1

    print("\n" + "=" * 60)
    print("✅ All code generator tests passed!")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
