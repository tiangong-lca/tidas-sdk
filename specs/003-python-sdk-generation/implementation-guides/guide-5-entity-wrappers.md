# Sub-Task 5: Entity Wrapper Classes

**Tasks**: T066-T074 (9 tasks)
**Status**: ✅ Complete
**Files**: `src/tidas_sdk/models/*.py` (8 entity files)
**Last Updated**: 2025-11-03

## Objective

Create wrapper classes for all 8 main TIDAS entity types. Wrappers provide a pythonic API on top of Pydantic models, adding convenience methods and multi-language text support.

## Entity List

1. `contact.py` → `TidasContact`
2. `flow.py` → `TidasFlow`
3. `process.py` → `TidasProcess`
4. `source.py` → `TidasSource`
5. `flow_property.py` → `TidasFlowProperty`
6. `unit_group.py` → `TidasUnitGroup`
7. `lcia_method.py` → `TidasLCIAMethod`
8. `life_cycle_model.py` → `TidasLifeCycleModel`

## Template Pattern

All entity wrappers follow this pattern:

```python
# src/tidas_sdk/models/contact.py
"""Contact entity wrapper."""

from typing import Optional, Dict, Any

from ..core.base import TidasEntity
from ..core.validation import ValidationConfig
from ..core.multilang import MultiLangText
from ..types.tidas_contacts import Contacts


class TidasContact(TidasEntity):
    """Wrapper for TIDAS Contact entities.

    Provides pythonic API for working with contact data.
    """

    def __init__(
        self,
        data: Optional[Dict[str, Any]] = None,
        validation_config: Optional[ValidationConfig] = None
    ):
        """Initialize contact entity.

        Args:
            data: Contact data in TIDAS JSON format
            validation_config: Validation configuration
        """
        # Initialize with empty structure if no data
        if data is None:
            data = {
                "contactDataSet": {
                    "contactInformation": {
                        "dataSetInformation": {}
                    }
                }
            }

        super().__init__(data, validation_config)

        # Set Pydantic model for validation
        self._pydantic_model = Contacts

        # Wrap multi-language fields
        self._wrap_multilang_fields()

    def _wrap_multilang_fields(self) -> None:
        """Wrap multi-language text fields with MultiLangText."""
        # Navigate to name field and wrap it
        try:
            name_path = ["contactDataSet", "contactInformation", "dataSetInformation", "common:name"]
            name_data = self._get_nested(self._data, name_path)

            if name_data is not None:
                # Replace array with MultiLangText wrapper
                self._set_nested(
                    self._data,
                    name_path,
                    MultiLangText(name_data)
                )
        except (KeyError, TypeError):
            # Field doesn't exist yet, that's ok
            pass

    def _get_nested(self, data: Dict[str, Any], path: List[str]) -> Any:
        """Get nested value from data dictionary."""
        current = data
        for key in path:
            if isinstance(current, dict):
                current = current.get(key)
                if current is None:
                    return None
            else:
                return None
        return current

    def _set_nested(self, data: Dict[str, Any], path: List[str], value: Any) -> None:
        """Set nested value in data dictionary."""
        current = data
        for key in path[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[path[-1]] = value

    @property
    def name(self) -> Optional[MultiLangText]:
        """Get the contact name field.

        Returns:
            MultiLangText wrapper for name field
        """
        try:
            return self._get_nested(
                self._data,
                ["contactDataSet", "contactInformation", "dataSetInformation", "common:name"]
            )
        except (KeyError, TypeError):
            return None

    @property
    def email(self) -> Optional[str]:
        """Get the contact email.

        Returns:
            Email address or None
        """
        try:
            return self._get_nested(
                self._data,
                ["contactDataSet", "contactInformation", "dataSetInformation", "email"]
            )
        except (KeyError, TypeError):
            return None

    @email.setter
    def email(self, value: str) -> None:
        """Set the contact email.

        Args:
            value: Email address
        """
        self._set_nested(
            self._data,
            ["contactDataSet", "contactInformation", "dataSetInformation", "email"],
            value
        )
```

## Implementation Steps

### Step 1: Identify Multi-Language Fields

For each entity, identify which fields are multi-language by checking the JSON schema:

```python
# Quick check script
from scripts.schema_parser import SchemaParser

parser = SchemaParser()
parser.load_all_schemas()

for entity in ["tidas_contacts", "tidas_flows", "tidas_processes"]:
    schema = parser.parse_schema(entity)
    multilang = parser.identify_multilang_fields(schema["properties"])
    print(f"{entity}: {multilang}")
```

### Step 2: Create Wrapper for Each Entity

Use the template above, customizing:
1. Import correct Pydantic model
2. Adjust empty data structure
3. Add properties for commonly-used fields
4. Wrap all multi-language fields

### Step 3: Add Convenience Properties

For frequently accessed fields, add @property methods:

```python
@property
def uuid(self) -> Optional[str]:
    """Get entity UUID."""
    return self._get_nested(self._data, ["contactDataSet", "contactInformation", "dataSetInformation", "common:UUID"])

@uuid.setter
def uuid(self, value: str) -> None:
    """Set entity UUID."""
    self._set_nested(self._data, ["contactDataSet", "contactInformation", "dataSetInformation", "common:UUID"], value)
```

### Step 4: Update models/__init__.py

```python
# src/tidas_sdk/models/__init__.py
"""Entity model classes for TIDAS SDK."""

from .contact import TidasContact
from .flow import TidasFlow
from .process import TidasProcess
from .source import TidasSource
from .flow_property import TidasFlowProperty
from .unit_group import TidasUnitGroup
from .lcia_method import TidasLCIAMethod
from .life_cycle_model import TidasLifeCycleModel

__all__ = [
    "TidasContact",
    "TidasFlow",
    "TidasProcess",
    "TidasSource",
    "TidasFlowProperty",
    "TidasUnitGroup",
    "TidasLCIAMethod",
    "TidasLifeCycleModel",
]
```

## Testing

Test each wrapper:

```python
# test_wrappers.py
from tidas_sdk.models import TidasContact
from tidas_sdk.core.validation import ValidationConfig

# Test empty creation
contact = TidasContact()
assert contact is not None

# Test with data
data = {
    "contactDataSet": {
        "contactInformation": {
            "dataSetInformation": {
                "common:name": [{"@xml:lang": "en", "#text": "Test"}]
            }
        }
    }
}
contact = TidasContact(data)

# Test multi-language access
name = contact.name
assert name is not None
assert name.get_text("en") == "Test"

# Test property setter
contact.email = "test@example.com"
assert contact.email == "test@example.com"

print("✅ All wrapper tests passed!")
```

## Completion Status ✅

All entity wrapper classes have been successfully implemented!

### Implemented Wrappers

- ✅ `contact.py` - TidasContact (T066)
- ✅ `flow.py` - TidasFlow (T067)
- ✅ `process.py` - TidasProcess (T068)
- ✅ `source.py` - TidasSource (T069)
- ✅ `flow_property.py` - TidasFlowProperty (T070)
- ✅ `unit_group.py` - TidasUnitGroup (T071)
- ✅ `lcia_method.py` - TidasLCIAMethod (T072)
- ✅ `life_cycle_model.py` - TidasLifeCycleModel (T073)
- ✅ `models/__init__.py` - All exports configured (T074)

### Verification Results

- ✅ All 8 wrapper classes created and inherit from TidasEntity
- ✅ Proper initialization with default structures
- ✅ Type hints complete (passes mypy --strict)
- ✅ Docstrings added for all public methods
- ✅ models/__init__.py exports all classes
- ✅ All files located at `/Users/biao/Code/tidas-sdk/sdks/python/src/tidas_sdk/models/`

**Note**: Multi-language field wrapping with MultiLangText is handled by the base TidasEntity class, so explicit wrapping in each entity is not required at this stage.

## Next Steps

Proceed to [Sub-Task 6: Factory Functions](./guide-6-factory-functions.md) to implement the creation functions.
