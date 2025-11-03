# Sub-Task 6: Factory Functions

**Tasks**: T075-T084 (10 tasks)
**Status**: ⏳ Todo
**File**: `src/tidas_sdk/factories.py`

## Objective

Implement factory functions for creating entity instances. Provides consistent API: `create_contact()`, `create_flow()`, etc.

## Implementation

Create `src/tidas_sdk/factories.py`:

```python
"""
Factory functions for creating TIDAS entities.
"""

from typing import Any, Dict, List, Optional
from uuid import uuid4

from .core.validation import ValidationConfig, get_default_validation_config
from .models import (
    TidasContact,
    TidasFlow,
    TidasProcess,
    TidasSource,
    TidasFlowProperty,
    TidasUnitGroup,
    TidasLCIAMethod,
    TidasLifeCycleModel,
)


# Single entity factories

def create_contact(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasContact:
    """Create a new Contact entity.

    Args:
        data: Optional contact data in TIDAS JSON format
        validation_config: Validation configuration (uses global default if None)

    Returns:
        TidasContact instance
    """
    if validation_config is None:
        validation_config = get_default_validation_config()

    contact = TidasContact(data, validation_config)

    # Auto-generate UUID if not provided
    if data is None or "contactDataSet" not in data:
        _ensure_uuid(contact, ["contactDataSet", "contactInformation", "dataSetInformation", "common:UUID"])

    return contact


def create_flow(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasFlow:
    """Create a new Flow entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    flow = TidasFlow(data, validation_config)
    if data is None or "flowDataSet" not in data:
        _ensure_uuid(flow, ["flowDataSet", "flowInformation", "dataSetInformation", "common:UUID"])

    return flow


def create_process(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasProcess:
    """Create a new Process entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    process = TidasProcess(data, validation_config)
    if data is None or "processDataSet" not in data:
        _ensure_uuid(process, ["processDataSet", "processInformation", "dataSetInformation", "common:UUID"])

    return process


def create_source(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasSource:
    """Create a new Source entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    source = TidasSource(data, validation_config)
    if data is None or "sourceDataSet" not in data:
        _ensure_uuid(source, ["sourceDataSet", "sourceInformation", "dataSetInformation", "common:UUID"])

    return source


def create_flow_property(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasFlowProperty:
    """Create a new FlowProperty entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    return TidasFlowProperty(data, validation_config)


def create_unit_group(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasUnitGroup:
    """Create a new UnitGroup entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    return TidasUnitGroup(data, validation_config)


def create_lcia_method(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasLCIAMethod:
    """Create a new LCIAMethod entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    return TidasLCIAMethod(data, validation_config)


def create_life_cycle_model(
    data: Optional[Dict[str, Any]] = None,
    validation_config: Optional[ValidationConfig] = None
) -> TidasLifeCycleModel:
    """Create a new LifeCycleModel entity."""
    if validation_config is None:
        validation_config = get_default_validation_config()

    return TidasLifeCycleModel(data, validation_config)


# Batch factories

def create_contacts_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasContact]:
    """Create multiple Contact entities in batch.

    Args:
        data_list: List of contact data dictionaries
        validation_config: Validation configuration for all entities

    Returns:
        List of TidasContact instances
    """
    return [create_contact(data, validation_config) for data in data_list]


def create_flows_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasFlow]:
    """Create multiple Flow entities in batch."""
    return [create_flow(data, validation_config) for data in data_list]


def create_processes_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasProcess]:
    """Create multiple Process entities in batch."""
    return [create_process(data, validation_config) for data in data_list]


def create_sources_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasSource]:
    """Create multiple Source entities in batch."""
    return [create_source(data, validation_config) for data in data_list]


def create_flow_properties_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasFlowProperty]:
    """Create multiple FlowProperty entities in batch."""
    return [create_flow_property(data, validation_config) for data in data_list]


def create_unit_groups_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasUnitGroup]:
    """Create multiple UnitGroup entities in batch."""
    return [create_unit_group(data, validation_config) for data in data_list]


def create_lcia_methods_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasLCIAMethod]:
    """Create multiple LCIAMethod entities in batch."""
    return [create_lcia_method(data, validation_config) for data in data_list]


def create_life_cycle_models_batch(
    data_list: List[Dict[str, Any]],
    validation_config: Optional[ValidationConfig] = None
) -> List[TidasLifeCycleModel]:
    """Create multiple LifeCycleModel entities in batch."""
    return [create_life_cycle_model(data, validation_config) for data in data_list]


# Helper functions

def _ensure_uuid(entity: Any, path: List[str]) -> None:
    """Ensure UUID exists at specified path, generate if missing.

    Args:
        entity: Entity instance
        path: Path to UUID field
    """
    current = entity._data
    for key in path[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    uuid_key = path[-1]
    if uuid_key not in current or not current[uuid_key]:
        current[uuid_key] = str(uuid4())
```

## Update Main __init__.py

Export factories from main package:

```python
# src/tidas_sdk/__init__.py
"""TIDAS Python SDK"""

__version__ = "0.1.0"

from .factories import (
    create_contact,
    create_flow,
    create_process,
    create_source,
    create_flow_property,
    create_unit_group,
    create_lcia_method,
    create_life_cycle_model,
    create_contacts_batch,
    create_flows_batch,
    create_processes_batch,
    create_sources_batch,
    create_flow_properties_batch,
    create_unit_groups_batch,
    create_lcia_methods_batch,
    create_life_cycle_models_batch,
)
from .core import ValidationConfig, ValidationError
from .config import set_global_validation_mode, get_global_validation_mode

__all__ = [
    "__version__",
    # Single entity factories
    "create_contact",
    "create_flow",
    "create_process",
    "create_source",
    "create_flow_property",
    "create_unit_group",
    "create_lcia_method",
    "create_life_cycle_model",
    # Batch factories
    "create_contacts_batch",
    "create_flows_batch",
    "create_processes_batch",
    "create_sources_batch",
    "create_flow_properties_batch",
    "create_unit_groups_batch",
    "create_lcia_methods_batch",
    "create_life_cycle_models_batch",
    # Configuration
    "ValidationConfig",
    "ValidationError",
    "set_global_validation_mode",
    "get_global_validation_mode",
]
```

## Testing

```python
# test_factories.py
from tidas_sdk import create_contact, create_contacts_batch, ValidationConfig

# Test single creation
contact = create_contact()
assert contact is not None
print(f"✅ Created contact with auto-generated UUID")

# Test with data
data = {"contactDataSet": {"contactInformation": {"dataSetInformation": {}}}}
contact = create_contact(data)
assert contact is not None

# Test batch creation
contacts = create_contacts_batch([{}, {}, {}])
assert len(contacts) == 3
print(f"✅ Created {len(contacts)} contacts in batch")

# Test with validation config
config = ValidationConfig(mode="ignore")
contact = create_contact(validation_config=config)
assert contact.get_validation_config().mode == "ignore"

print("✅ All factory tests passed!")
```

## Checklist

- [ ] All 8 single entity factories implemented
- [ ] All 8 batch factories implemented
- [ ] Auto-generates UUIDs when data is None
- [ ] Uses global validation config by default
- [ ] Main __init__.py exports all factories
- [ ] Test script passes
- [ ] Type hints complete
- [ ] Docstrings added

## Next Steps

Proceed to [Sub-Task 7: Main Generation Script](./guide-7-main-script.md).
