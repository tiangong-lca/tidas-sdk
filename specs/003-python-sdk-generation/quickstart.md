# Quick Start Guide: TIDAS Python SDK

**Feature**: 003-python-sdk-generation
**Target Audience**: Python developers new to the TIDAS SDK

## Overview

The TIDAS Python SDK provides type-safe, validated operations for Life Cycle Assessment (LCA) data in TIDAS/ILCD format. This guide will get you up and running in 10 minutes.

---

## Installation

### Requirements
- Python 3.8 or higher
- pip or uv package manager

### Install via pip

```bash
pip install tidas-sdk
```

### Install via uv (faster)

```bash
uv pip install tidas-sdk
```

### Verify Installation

```python
python -c "import tidas_sdk; print(f'TIDAS SDK version: {tidas_sdk.__version__}')"
```

---

## Your First Entity: Creating a Contact

Let's create a contact entity representing a researcher:

```python
from tidas_sdk import create_contact

# Create a new contact
contact = create_contact()

# Set the name (multi-language support)
contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)
contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "fr"
)

# Set email
contact.contact_data_set.contact_information.data_set_information.email = "jane.smith@example.com"

# Validate the contact
contact.validate()  # Raises ValidationError if invalid

# Export to JSON
json_string = contact.to_json_string(indent=2)
print(json_string)
```

**Output**:
```json
{
  "contactDataSet": {
    "contactInformation": {
      "dataSetInformation": {
        "common:UUID": "550e8400-e29b-41d4-a716-446655440000",
        "common:name": [
          {"@xml:lang": "en", "#text": "Dr. Jane Smith"},
          {"@xml:lang": "fr", "#text": "Dr. Jane Smith"}
        ],
        "email": "jane.smith@example.com"
      }
    }
  }
}
```

---

## Key Concepts

### 1. Entity Creation

The SDK provides factory functions for all 8 entity types:

```python
from tidas_sdk import (
    create_contact,
    create_flow,
    create_process,
    create_source,
    create_flow_property,
    create_unit_group,
    create_lcia_method,
    create_life_cycle_model
)

# Create entities
contact = create_contact()
flow = create_flow()
process = create_process()
```

### 2. Multi-Language Text Fields

TIDAS supports multi-language text for internationalization:

```python
# Set text in multiple languages
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text("Water", "en")
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text("Wasser", "de")
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text("Eau", "fr")

# Get text for specific language
english_name = flow.flow_data_set.flow_information.data_set_information.name.base_name.get_text("en")
# Returns: "Water"

# Get first available language (useful when language unknown)
any_name = flow.flow_data_set.flow_information.data_set_information.name.base_name.get_text(None)
# Returns: "Water" (first entry)
```

### 3. Validation Modes

The SDK supports three validation modes:

#### Strict Mode (default)
Raises exception on any schema violation:

```python
contact = create_contact()
# Don't set required fields...

try:
    contact.validate()
except ValidationError as e:
    print(f"Validation failed: {e.message}")
    print(f"Field: {e.field_path}")
```

#### Weak Mode
Collects violations as warnings, doesn't raise exceptions:

```python
from tidas_sdk import ValidationConfig

config = ValidationConfig(mode="weak")
contact = create_contact(validation_config=config)

# Set some invalid data
contact.contact_data_set.contact_information.data_set_information.email = "not-an-email"

contact.validate()  # Doesn't raise!

# Check warnings
warnings = contact.get_validation_warnings()
for warning in warnings:
    print(f"{warning.field_path}: {warning.message}")
```

#### Ignore Mode
Skips validation for maximum performance:

```python
config = ValidationConfig(mode="ignore")
contact = create_contact(validation_config=config)

contact.validate()  # No-op, always succeeds
```

### 4. JSON Import/Export

#### Export to JSON

```python
# As dictionary
data_dict = contact.to_json()

# As string
json_str = contact.to_json_string(indent=2)

# Save to file
with open("contact.json", "w") as f:
    f.write(contact.to_json_string(indent=2))
```

#### Import from JSON

```python
import json

# Load from file
with open("contact.json", "r") as f:
    data = json.load(f)

# Create entity from data
contact = create_contact(data)

# Validate imported data
contact.validate()
```

---

## Common Use Cases

### Use Case 1: Creating a Flow

```python
from tidas_sdk import create_flow
import uuid

# Create a flow for CO2 emissions
flow = create_flow()

# Set basic information
flow.flow_data_set.flow_information.data_set_information.uuid = uuid.uuid4()
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
    "Carbon dioxide", "en"
)
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
    "Dioxyde de carbone", "fr"
)

# Set general comment
flow.flow_data_set.flow_information.data_set_information.general_comment.set_text(
    "Greenhouse gas emission", "en"
)

# Validate and export
flow.validate()
print(flow.to_json_string(indent=2))
```

### Use Case 2: Batch Processing

```python
from tidas_sdk import create_contacts_batch, ValidationConfig

# Prepare data for multiple contacts
contacts_data = [
    {
        "contactDataSet": {
            "contactInformation": {
                "dataSetInformation": {
                    "common:name": [{"@xml:lang": "en", "#text": "Alice"}]
                }
            }
        }
    },
    {
        "contactDataSet": {
            "contactInformation": {
                "dataSetInformation": {
                    "common:name": [{"@xml:lang": "en", "#text": "Bob"}]
                }
            }
        }
    }
]

# Create in batch with weak validation for speed
config = ValidationConfig(mode="weak")
contacts = create_contacts_batch(contacts_data, validation_config=config)

print(f"Created {len(contacts)} contacts")

# Validate all and collect issues
all_warnings = []
for i, contact in enumerate(contacts):
    contact.validate()
    warnings = contact.get_validation_warnings()
    if warnings:
        all_warnings.extend([(i, w) for w in warnings])

print(f"Total warnings: {len(all_warnings)}")
```

### Use Case 3: Cloning and Modifying

```python
# Create original contact
original = create_contact()
original.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)

# Clone it
copy = original.clone()

# Modify the copy
copy.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith (Copy)", "en"
)

# Generate new UUID for the copy
import uuid
copy.contact_data_set.contact_information.data_set_information.uuid = uuid.uuid4()

# Original is unchanged
print(original.contact_data_set.contact_information.data_set_information.name.get_text("en"))
# Output: "Dr. Jane Smith"
```

### Use Case 4: Entity Relationships

```python
from tidas_sdk import create_flow, create_flow_property, create_unit_group
from tidas_sdk import ReferenceObject

# Create a unit group for mass
unit_group = create_unit_group()
unit_group.unit_group_data_set.unit_group_information.data_set_information.name.set_text(
    "Mass units", "en"
)
unit_group_uuid = unit_group.unit_group_data_set.unit_group_information.data_set_information.uuid

# Create a flow property for mass
flow_property = create_flow_property()
flow_property.flow_property_data_set.flow_properties_information.data_set_information.name.set_text(
    "Mass", "en"
)
flow_property_uuid = flow_property.flow_property_data_set.flow_properties_information.data_set_information.uuid

# Reference the unit group in the flow property
ref = ReferenceObject(
    type="unit group data set",
    ref_object_id=unit_group_uuid,
    version="1.0.0",
    uri=""
)
flow_property.flow_property_data_set.flow_properties_information.quantitative_reference.reference_to_reference_unit_group = ref.to_dict()

# Create a flow that uses this flow property
flow = create_flow()
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text("CO2", "en")

flow_property_ref = ReferenceObject(
    type="flow property data set",
    ref_object_id=flow_property_uuid,
    version="1.0.0",
    uri=""
)
flow.flow_data_set.flow_properties.flow_property = flow_property_ref.to_dict()
```

---

## Logging and Debugging

The SDK uses loguru for logging. Configure it to see what's happening:

```python
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add custom handler for debugging
logger.add(sys.stderr, level="DEBUG")

# Now SDK operations will log details
contact = create_contact()
contact.validate()
# Logs: "DEBUG | tidas_sdk.core.base:validate:123 - Validating Contact entity"
```

**Log Levels**:
- **DEBUG**: Detailed operation logs (entity creation, field access)
- **INFO**: High-level operations (batch creation counts)
- **WARNING**: Validation warnings in weak mode
- **ERROR**: Exception details

---

## Error Handling

### Validation Errors

```python
from tidas_sdk import ValidationError

contact = create_contact()

try:
    contact.validate()
except ValidationError as e:
    print(f"Field: {e.field_path}")
    print(f"Expected: {e.expected}")
    print(f"Got: {e.actual}")
    print(f"Type: {e.constraint_type}")
```

### JSON Decode Errors

```python
import json
from json import JSONDecodeError

try:
    with open("malformed.json", "r") as f:
        data = json.load(f)
    contact = create_contact(data)
except JSONDecodeError as e:
    print(f"Invalid JSON at line {e.lineno}, column {e.colno}")
    print(f"Error: {e.msg}")
```

### Configuration Errors

```python
from tidas_sdk import ConfigurationError

try:
    # SDK will check for tidas-tools schemas during code generation
    pass
except ConfigurationError as e:
    print(f"Configuration error: {e}")
    # Example: "TIDAS tools schema directory not found at ../tidas-tools/..."
```

---

## Global Configuration

### Set Global Validation Mode

```python
from tidas_sdk import set_global_validation_mode, get_global_validation_mode

# Set mode for all new entities
set_global_validation_mode("weak")

# All entities created after this use weak mode
contact1 = create_contact()
contact2 = create_contact()

# Check current mode
current_mode = get_global_validation_mode()
print(f"Global mode: {current_mode}")  # "weak"
```

### Per-Entity Override

```python
from tidas_sdk import ValidationConfig, set_global_validation_mode

# Global default is weak
set_global_validation_mode("weak")

# But this specific entity uses strict
strict_config = ValidationConfig(mode="strict")
critical_contact = create_contact(validation_config=strict_config)
```

---

## Performance Tips

### 1. Use Ignore Mode for Bulk Operations

```python
from tidas_sdk import ValidationConfig

# Create 1000 entities without validation overhead
config = ValidationConfig(mode="ignore")
contacts = create_contacts_batch([{}] * 1000, validation_config=config)
# Completes in <1 second
```

### 2. Validate Once at the End

```python
# Disable validation during construction
config = ValidationConfig(mode="ignore")
contact = create_contact(validation_config=config)

# Set all fields...
contact.contact_data_set.contact_information.data_set_information.name.set_text("...", "en")
contact.contact_data_set.contact_information.data_set_information.email = "..."

# Enable validation and check at the end
contact.set_validation_mode("strict")
contact.validate()
```

### 3. Batch JSON Export

```python
import json

contacts = create_contacts_batch(data_list)

# Export all at once
all_data = [c.to_json() for c in contacts]

with open("contacts_batch.json", "w") as f:
    json.dump(all_data, f, indent=2)
```

---

## IDE Support

The SDK provides full type hints for IDE autocomplete:

```python
from tidas_sdk import create_contact

contact = create_contact()

# Type hints enable autocomplete:
# contact.contact_data_set.  <-- IDE shows available fields
#     contact_information.    <-- IDE shows nested fields
#         data_set_information.  <-- IDE shows final fields
#             name.              <-- IDE shows MultiLangText methods
#                 set_text()     <-- IDE shows parameters and docs
```

**Supported IDEs**:
- PyCharm
- VS Code with Python extension
- Any IDE with Python type hint support

---

## Next Steps

### Learn More

- **API Reference**: Full API documentation with all classes and methods
- **Migration Guide**: Coming from TypeScript SDK? See the migration guide
- **Examples**: Check `examples/` directory for complete working examples
- **Advanced Topics**: Validation customization, schema extensions, performance optimization

### Example Code

The SDK includes 4+ working examples:

```bash
# Clone the repository
git clone https://github.com/tiangong-lca/tidas-sdk
cd tidas-sdk/sdks/python

# Run examples
python examples/01_basic_usage.py
python examples/02_batch_operations.py
python examples/03_validation_modes.py
python examples/04_relationships.py
```

### Get Help

- **Documentation**: https://tidas-sdk.readthedocs.io
- **Issues**: https://github.com/tiangong-lca/tidas-sdk/issues
- **Discussions**: https://github.com/tiangong-lca/tidas-sdk/discussions

---

## Quick Reference

### Entity Creation Functions

```python
create_contact(data=None, validation_config=None)
create_flow(data=None, validation_config=None)
create_process(data=None, validation_config=None)
create_source(data=None, validation_config=None)
create_flow_property(data=None, validation_config=None)
create_unit_group(data=None, validation_config=None)
create_lcia_method(data=None, validation_config=None)
create_life_cycle_model(data=None, validation_config=None)
```

### Batch Creation Functions

```python
create_contacts_batch(data_list, validation_config=None)
create_flows_batch(data_list, validation_config=None)
# ... similar for all entity types
```

### Validation Configuration

```python
ValidationConfig(mode="strict")   # Raise errors (default)
ValidationConfig(mode="weak")     # Collect warnings
ValidationConfig(mode="ignore")   # Skip validation
```

### Common Methods (All Entities)

```python
entity.validate()                         # Validate data
entity.get_validation_warnings()          # Get warnings (weak mode)
entity.set_validation_mode(mode)          # Change mode
entity.to_json()                          # Export as dict
entity.to_json_string(indent=2)           # Export as JSON string
entity.clone()                            # Deep copy
entity.get_value("path.to.field")         # Nested field access
```

### Multi-Language Text Methods

```python
field.set_text(value, lang="en")     # Set text for language
field.get_text(lang="en")            # Get text for language
field.get_text(None)                 # Get first available
field.raw                            # Access raw array
```

---

**Quick Start Complete!** You're now ready to use the TIDAS Python SDK for LCA data management.

For more details, see the full API Reference and explore the example code.

---

**Guide Version**: 1.0
**Last Updated**: 2025-10-31
