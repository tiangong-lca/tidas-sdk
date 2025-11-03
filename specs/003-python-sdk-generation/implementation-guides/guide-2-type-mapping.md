# Sub-Task 2: Type Mapping System

**Tasks**: T044
**Status**: ⏳ Todo
**File**: `scripts/type_mapper.py`

## Objective

Create a type mapping system that converts JSON Schema type definitions to Python type annotations compatible with Pydantic v2.

## Background (from research.md)

The type mapper handles these conversions:

| JSON Schema Type | Python Type | Notes |
|------------------|-------------|-------|
| `string` | `str` | Add `Field(max_length=N)` if maxLength |
| `string` (format: uuid) | `UUID` | From uuid module |
| `string` (format: date-time) | `datetime` | ISO8601 parsing |
| `integer` | `int` | Add `Field(ge=N, le=M)` for ranges |
| `number` | `float` | Similar constraints |
| `boolean` | `bool` | Direct mapping |
| `array` | `List[T]` | Recursive type resolution |
| `object` | Nested model | Create separate Pydantic model |
| `enum` | `Literal[...]` | Type-safe enum values |
| `anyOf/oneOf` | `Union[...]` | Pydantic handles discrimination |
| Multi-lang pattern | `MultiLangText` | Custom wrapper class |

## Implementation Steps

### Step 1: Create Type Mapper Class

Create `scripts/type_mapper.py`:

```python
"""
Type mapper for JSON Schema to Python type conversion.
"""

from typing import Any, Dict, List, Optional, Set
from loguru import logger


class TypeMapper:
    """Maps JSON Schema types to Python type annotations."""

    def __init__(self):
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
            if len(types) == 1:
                json_type = types[0]
                base_type = self._map_single_type(json_type, format_type, schema)
                if "null" in json_type:
                    return f"Optional[{base_type}]"
                return base_type
            else:
                # Multiple non-null types -> Union
                mapped_types = [self._map_single_type(t, None, schema) for t in types]
                return f"Union[{', '.join(mapped_types)}]"

        return self._map_single_type(json_type, format_type, schema)

    def _map_single_type(
        self,
        json_type: str,
        format_type: Optional[str],
        schema: Dict[str, Any]
    ) -> str:
        """Map a single JSON Schema type to Python type."""

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
            # Will be replaced with actual model name
            return "dict"  # Placeholder for nested objects

        else:
            # Fallback
            self.imports.add("from typing import Any")
            return "Any"

    def extract_field_constraints(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """Extract Pydantic Field() constraints from JSON Schema.

        Args:
            schema: JSON Schema field definition

        Returns:
            Dictionary of Field() kwargs
        """
        constraints = {}

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

    def get_imports(self) -> List[str]:
        """Get list of import statements needed for generated types.

        Returns:
            List of import statement strings
        """
        all_imports = self.imports.union(self.field_imports)
        return sorted(list(all_imports))
```

### Step 2: Add Enum Handling

Add to `TypeMapper` class:

```python
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
            quoted_values.append(f'"{value}"')
        else:
            quoted_values.append(str(value))

    return f"Literal[{', '.join(quoted_values)}]"
```

### Step 3: Add OneOf/AnyOf Handling

```python
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

    return f"Union[{', '.join(types)}]"
```

### Step 4: Test the Type Mapper

Create `test_type_mapper.py`:

```python
from scripts.type_mapper import TypeMapper

# Test basic types
mapper = TypeMapper()

# String
assert mapper.map_type({"type": "string"}, "name") == "str"

# UUID
assert mapper.map_type({"type": "string", "format": "uuid"}, "id") == "UUID"

# Array
result = mapper.map_type({"type": "array", "items": {"type": "string"}}, "tags")
assert result == "List[str]"

# With constraints
constraints = mapper.extract_field_constraints({
    "type": "string",
    "maxLength": 100,
    "pattern": "^[a-z]+$"
})
assert constraints["max_length"] == 100
assert constraints["pattern"] == "^[a-z]+$"

# Enum
enum_type = mapper.handle_enum(["active", "inactive", "pending"])
assert enum_type == 'Literal["active", "inactive", "pending"]'

print("✅ All type mapper tests passed!")
print(f"Required imports: {mapper.get_imports()}")
```

Run test:
```bash
cd /Users/biao/Code/tidas-sdk/sdks/python
uv run python test_type_mapper.py
```

## Validation Checklist

- [ ] Maps all basic JSON Schema types (string, int, float, bool, array)
- [ ] Handles format types (uuid, date-time)
- [ ] Extracts Field() constraints (maxLength, pattern, etc.)
- [ ] Handles enums with Literal types
- [ ] Handles oneOf/anyOf with Union types
- [ ] Tracks required imports
- [ ] Returns correct Optional[] for nullable fields
- [ ] Test script passes all assertions

## Common Pitfalls

1. **Circular References**: JSON Schema can have $ref pointing to itself. Handle with forward references.
2. **Nested Objects**: Create separate Pydantic models, don't inline large objects.
3. **Import Management**: Track all imports needed (typing, uuid, datetime, pydantic).
4. **Field Aliases**: TIDAS uses namespaced fields like `common:UUID` - need alias support.

## Expected Output Example

For a schema field:
```json
{
  "type": "string",
  "format": "uuid",
  "description": "Unique identifier"
}
```

Type mapper should produce:
- Type annotation: `UUID`
- Field constraints: `Field(description="Unique identifier")`
- Imports: `["from uuid import UUID", "from pydantic import Field"]`

## Next Steps

After completing type mapping, proceed to [Sub-Task 3: Code Generator](./guide-3-code-generator.md).
