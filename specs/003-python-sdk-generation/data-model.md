# Data Model: Python SDK

**Feature**: 003-python-sdk-generation
**Date**: 2025-10-31

## Overview

This document defines the data model for the Python SDK, including entity classes, data structures, and their relationships. The model mirrors the TIDAS/ILCD schema structure while providing a pythonic API.

---

## Entity Hierarchy

```
TidasEntity (abstract base)
├── TidasContact
├── TidasFlow
├── TidasProcess
├── TidasSource
├── TidasFlowProperty
├── TidasUnitGroup
├── TidasLCIAMethod
└── TidasLifeCycleModel
```

---

## Core Classes

### 1. TidasEntity (Base Class)

**Purpose**: Abstract base class providing common functionality for all TIDAS entities.

**Attributes**:
```python
class TidasEntity(ABC):
    _data: dict                          # Raw entity data
    _validation_config: ValidationConfig  # Validation settings
    _validation_warnings: List[ValidationWarning]  # Collected warnings (weak mode)
    _pydantic_model: Type[BaseModel]     # Associated Pydantic model
```

**Methods**:
```python
def __init__(self, data: Optional[dict] = None,
             validation_config: Optional[ValidationConfig] = None) -> None:
    """Initialize entity with optional data and validation config."""

def validate(self) -> None:
    """
    Validate entity data according to current mode.
    - strict: Raises ValidationError on any violation
    - weak: Collects violations as warnings
    - ignore: Skips validation
    """

def get_validation_warnings(self) -> List[ValidationWarning]:
    """Return list of validation warnings from weak mode."""

def set_validation_mode(self, mode: Literal["strict", "weak", "ignore"]) -> None:
    """Change validation mode for this entity."""

def get_validation_config(self) -> ValidationConfig:
    """Return current validation configuration."""

def to_json(self) -> dict:
    """Export entity as dictionary matching TIDAS JSON structure."""

def to_json_string(self, indent: Optional[int] = None) -> str:
    """Export entity as formatted JSON string."""

def clone(self) -> Self:
    """Create a deep copy of this entity."""

def get_value(self, path: str) -> Any:
    """
    Get nested value using dot notation.
    Example: get_value("contactDataSet.contactInformation.dataSetInformation.name")
    """
```

**Lifecycle**:
```
Created → (Optional: Set Fields) → Validate → Export JSON
         ↑                                      ↓
         └──────────── Clone ←──────────────────┘
```

---

### 2. ValidationConfig

**Purpose**: Configure validation behavior per entity or globally.

**Definition**:
```python
@dataclass
class ValidationConfig:
    mode: Literal["strict", "weak", "ignore"] = "strict"
    include_warnings: bool = True  # Whether to collect warnings in weak mode
```

**Usage**:
```python
# Per-entity config
config = ValidationConfig(mode="weak")
contact = create_contact(data, validation_config=config)

# Global config
set_global_validation_mode("weak")
```

---

### 3. ValidationWarning

**Purpose**: Represent a validation issue in weak mode (non-exception).

**Definition**:
```python
@dataclass
class ValidationWarning:
    field_path: str      # Dot-notation path to field (e.g., "contactDataSet.contactInformation.dataSetInformation.common:UUID")
    message: str         # Human-readable error message
    expected: str        # Expected type or constraint
    actual: Any          # Actual value that failed validation
    severity: Literal["warning", "error"] = "warning"

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.field_path}: {self.message}"
```

**Example**:
```python
warning = ValidationWarning(
    field_path="contactDataSet.contactInformation.dataSetInformation.common:UUID",
    message="Invalid UUID format",
    expected="UUID (format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)",
    actual="not-a-uuid"
)
print(warning)
# Output: [WARNING] contactDataSet.contactInformation.dataSetInformation.common:UUID: Invalid UUID format
```

---

### 4. MultiLangText

**Purpose**: Wrapper for TIDAS multi-language text fields.

**TIDAS Format**:
```json
{
  "common:name": [
    {"@xml:lang": "en", "#text": "Dr. Jane Smith"},
    {"@xml:lang": "fr", "#text": "Dr. Jane Smith"},
    {"@xml:lang": "de", "#text": "Dr. Jane Schmidt"}
  ]
}
```

**Python Class**:
```python
class MultiLangText:
    _items: List[dict]  # List of {"@xml:lang": str, "#text": str}

    def __init__(self, initial_data: Optional[List[dict]] = None) -> None:
        """Initialize with optional language items."""

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for a specific language (updates existing or appends)."""

    def get_text(self, lang: Optional[str] = "en") -> Optional[str]:
        """
        Get text for a specific language.
        If lang is None, returns first available language.
        Returns None if language not found.
        """

    @property
    def raw(self) -> List[dict]:
        """Access raw array for advanced manipulation."""

    def __repr__(self) -> str:
        """String representation showing available languages."""
```

**Usage Examples**:
```python
# Setting text
name = MultiLangText()
name.set_text("Dr. Jane Smith", "en")
name.set_text("Dr. Jane Smith", "fr")
name.set_text("Dr. Jane Schmidt", "de")

# Getting text
english_name = name.get_text("en")  # "Dr. Jane Smith"
french_name = name.get_text("fr")   # "Dr. Jane Smith"
first_name = name.get_text(None)    # "Dr. Jane Smith" (first available)
spanish_name = name.get_text("es")  # None (not found)

# Raw access
for item in name.raw:
    print(f"{item['@xml:lang']}: {item['#text']}")

# Integration in entities
contact = create_contact()
contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)
```

---

## Entity-Specific Classes

### 5. TidasContact

**Purpose**: Represents a contact or organization in TIDAS format.

**Key Fields**:
- `contact_data_set.contact_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:name` (MultiLangText): Full name
  - `common:short_name` (MultiLangText): Abbreviated name
  - `email` (str): Contact email
  - `www_address` (str): Website URL

**Relationships**:
- Referenced by: Process (data entry contact), Source (author)

**Example**:
```python
contact = create_contact()
contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"
contact.validate()
```

---

### 6. TidasFlow

**Purpose**: Represents a material or energy flow in LCA.

**Key Fields**:
- `flow_data_set.flow_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `name.base_name` (MultiLangText): Flow name
  - `classification_information.common:classification` (list): Categorization
- `flow_data_set.flow_properties`:
  - `flow_property` (ReferenceObject): Link to FlowProperty

**Flow Types**:
- Elementary flows (environmental exchanges)
- Product flows (intermediate/final products)
- Waste flows

**Relationships**:
- References: FlowProperty (via flow_property)
- Referenced by: Process (exchanges)

**Example**:
```python
flow = create_flow()
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
    "Carbon dioxide", "en"
)
flow.flow_data_set.flow_information.data_set_information.name.base_name.set_text(
    "Dioxyde de carbone", "fr"
)
```

---

### 7. TidasProcess

**Purpose**: Represents a process (unit process or system) in LCA.

**Key Fields**:
- `process_data_set.process_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `name.base_name` (MultiLangText): Process name
  - `common:general_comment` (MultiLangText): Description
- `process_data_set.exchanges`:
  - `exchange` (List[Exchange]): Input/output flows

**Relationships**:
- References: Flow (exchanges), Contact (data entry), Source (publication)
- Most complex entity with numerous nested structures

**Example**:
```python
process = create_process()
process.process_data_set.process_information.data_set_information.name.base_name.set_text(
    "Electricity production, photovoltaic", "en"
)
```

---

### 8. TidasSource

**Purpose**: Represents a literature source or publication.

**Key Fields**:
- `source_data_set.source_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:short_name` (MultiLangText): Short citation
  - `publication_type` (str): Type of publication

**Relationships**:
- References: Contact (author)
- Referenced by: Process, Flow (data sources)

---

### 9. TidasFlowProperty

**Purpose**: Represents a quantifiable property of flows (mass, energy, volume).

**Key Fields**:
- `flow_property_data_set.flow_properties_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:name` (MultiLangText): Property name

**Relationships**:
- References: UnitGroup
- Referenced by: Flow

**Common Examples**: Mass, Energy content, Volume

---

### 10. TidasUnitGroup

**Purpose**: Represents a group of measurement units.

**Key Fields**:
- `unit_group_data_set.unit_group_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:name` (MultiLangText): Unit group name
- `unit_group_data_set.units.unit` (List[Unit]): Individual units

**Relationships**:
- Referenced by: FlowProperty

**Common Examples**: Mass units (kg, g, ton), Energy units (MJ, kWh), Volume units (m³, L)

---

### 11. TidasLCIAMethod

**Purpose**: Represents an LCIA (Life Cycle Impact Assessment) method.

**Key Fields**:
- `lcia_method_data_set.lcia_method_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:name` (MultiLangText): Method name
- `lcia_method_data_set.characterisation_factors` (list): Impact factors

**Common Examples**: ReCiPe, CML, TRACI

---

### 12. TidasLifeCycleModel

**Purpose**: Represents a life cycle model or methodology.

**Key Fields**:
- `life_cycle_model_data_set.life_cycle_model_information.data_set_information`:
  - `common:UUID` (UUID): Unique identifier
  - `common:name` (MultiLangText): Model name

---

## Exception Classes

### 13. TidasException (Base)

**Purpose**: Base class for all SDK-specific exceptions.

```python
class TidasException(Exception):
    """Base exception for all TIDAS SDK errors."""
    pass
```

---

### 14. ValidationError

**Purpose**: Raised when entity data violates schema constraints (strict mode).

```python
class ValidationError(TidasException):
    field_path: str
    expected: str
    actual: Any
    constraint_type: str  # "type", "format", "length", "required", etc.

    def __init__(self, field_path: str, expected: str, actual: Any,
                 constraint_type: str = "validation"):
        self.field_path = field_path
        self.expected = expected
        self.actual = actual
        self.constraint_type = constraint_type

        message = f"Field '{field_path}' {expected}, got {actual!r}"
        super().__init__(message)

    @classmethod
    def from_pydantic(cls, pydantic_error: PydanticValidationError) -> "ValidationError":
        """Convert Pydantic validation error to TIDAS ValidationError."""
        # Take first error for simplicity
        error = pydantic_error.errors()[0]
        return cls(
            field_path=".".join(str(p) for p in error["loc"]),
            expected=error["msg"],
            actual=error.get("input"),
            constraint_type=error["type"]
        )
```

**Example**:
```python
try:
    contact.validate()
except ValidationError as e:
    print(f"Validation failed: {e.message}")
    print(f"Field: {e.field_path}")
    print(f"Expected: {e.expected}")
    print(f"Got: {e.actual}")
```

---

### 15. SchemaGenerationError

**Purpose**: Raised when code generation from schemas fails.

```python
class SchemaGenerationError(TidasException):
    schema_file: str
    reason: str

    def __init__(self, schema_file: str, reason: str):
        self.schema_file = schema_file
        self.reason = reason
        super().__init__(f"Failed to generate code from {schema_file}: {reason}")
```

---

### 16. ConfigurationError

**Purpose**: Raised when SDK configuration is invalid.

```python
class ConfigurationError(TidasException):
    """Raised when SDK configuration is invalid."""
    pass
```

**Example**:
```python
if not os.path.exists(schema_path):
    raise ConfigurationError(
        f"TIDAS tools schema directory not found at {schema_path}. "
        "Ensure tidas-tools is cloned alongside tidas-sdk or set TIDAS_TOOLS_PATH."
    )
```

---

## Supporting Data Structures

### 17. ReferenceObject

**Purpose**: Type-safe representation of entity references.

```python
@dataclass
class ReferenceObject:
    type: str              # Entity type (e.g., "flow property data set")
    ref_object_id: UUID    # UUID of referenced entity
    version: str           # Version string
    uri: str               # URI (often empty in practice)
    short_description: Optional[MultiLangText] = None  # Brief description

    def to_dict(self) -> dict:
        """Convert to TIDAS JSON format."""
        return {
            "@type": self.type,
            "@refObjectId": str(self.ref_object_id),
            "@version": self.version,
            "@uri": self.uri,
            "common:shortDescription": self.short_description.raw if self.short_description else []
        }
```

**Usage**:
```python
# Create reference to a flow property
ref = ReferenceObject(
    type="flow property data set",
    ref_object_id=flow_property_uuid,
    version="1.0.0",
    uri=""
)

# Use in flow
flow.flow_data_set.flow_properties.flow_property = ref.to_dict()
```

---

## Entity Relationships

### Relationship Diagram

```
Contact
   ↑
   │ (author)
   │
Source ←────┐
             │
             │ (publication)
Process ─────┤
   ↑         │
   │         │
   │ (exchange)
   │         │
Flow ────────┘
   ↓
   │ (property)
   │
FlowProperty
   ↓
   │ (units)
   │
UnitGroup

LCIAMethod ← (independent)

LifeCycleModel ← (independent)
```

### Relationship Types

1. **One-to-Many**:
   - Contact → Process (one contact can be data entry for many processes)
   - FlowProperty → Flow (one property can apply to many flows)
   - UnitGroup → FlowProperty (one unit group can be used by many properties)

2. **Many-to-Many**:
   - Process ↔ Flow (via exchanges: one process has many flows, one flow used by many processes)
   - Process ↔ Source (one process cites many sources, one source cited by many processes)

3. **Reference-Only**:
   - SDK stores references as data (UUID + metadata)
   - No referential integrity enforcement
   - Users responsible for ensuring referenced entities exist

---

## Data Model Invariants

### Required Fields

Each entity type must have:
1. **UUID**: Unique identifier (`common:UUID` field)
2. **Name**: Multi-language name field
3. **Version**: Version string (typically in administrative information)

### Validation Rules

1. **UUID Format**: Must be valid UUID v4 format
2. **Multi-Language**: At least one language entry required for multi-lang fields
3. **References**: Referenced UUIDs must be valid UUID format (but not checked for existence)
4. **Enums**: Category fields must match allowed values from category schemas
5. **Constraints**: String length, numeric ranges as defined in schemas

### State Transitions

```
New Entity (empty data)
   ↓
Populated (fields set via API)
   ↓
Validated (validate() called, passed)
   ↓
Exported (to_json() / to_json_string())
   ↓
Serialized (JSON string/file)
```

**State Invariant**: An entity can be exported without validation (user discretion), but validation should always pass for well-formed data.

---

## Generated Code Structure

### Generated Pydantic Models (in `types/`)

```python
# types/tidas_contacts.py
from pydantic import BaseModel, Field, UUID4
from datetime import datetime

class Contacts(BaseModel):
    """Generated from tidas_contacts.json schema."""

    contact_data_set: ContactDataSet

    class Config:
        populate_by_name = True  # Allow both snake_case and original names

class ContactDataSet(BaseModel):
    contact_information: ContactInformation
    # ... more fields

class ContactInformation(BaseModel):
    data_set_information: DataSetInformation
    # ... more fields

class DataSetInformation(BaseModel):
    uuid: UUID4 = Field(alias="common:UUID")
    name: List[dict] = Field(alias="common:name")  # Multi-lang
    short_name: Optional[List[dict]] = Field(default=None, alias="common:shortName")
    # ... more fields
```

### Entity Wrapper Classes (in `models/`)

```python
# models/contact.py
from ..core.base import TidasEntity
from ..types.tidas_contacts import Contacts
from ..core.multilang import MultiLangText

class TidasContact(TidasEntity):
    """Wrapper class for Contact entities with pythonic API."""

    def __init__(self, data: Optional[dict] = None,
                 validation_config: Optional[ValidationConfig] = None):
        super().__init__(data, validation_config)
        self._pydantic_model = Contacts

        # Wrap multi-language fields
        self._wrap_multilang_fields()

    def _wrap_multilang_fields(self):
        """Replace multi-lang arrays with MultiLangText instances."""
        name_data = self._data.get("contactDataSet", {}).get("contactInformation", {}).get("dataSetInformation", {}).get("common:name")
        if name_data:
            self.contact_data_set.contact_information.data_set_information.name = MultiLangText(name_data)
```

---

## Usage Patterns

### Creating an Entity

```python
# Empty entity with defaults
contact = create_contact()

# Entity from existing data
data = {
    "contactDataSet": {
        "contactInformation": {
            "dataSetInformation": {
                "common:UUID": "550e8400-e29b-41d4-a716-446655440000",
                "common:name": [{"@xml:lang": "en", "#text": "Dr. Smith"}]
            }
        }
    }
}
contact = create_contact(data)
```

### Setting Fields

```python
# Multi-language text
contact.contact_data_set.contact_information.data_set_information.name.set_text("Dr. Jane Smith", "en")

# Simple fields
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"

# Nested access via dot notation
contact.get_value("contactDataSet.contactInformation.dataSetInformation.email")
```

### Validation

```python
# Strict mode (default) - raises exception
try:
    contact.validate()
except ValidationError as e:
    print(f"Validation failed: {e}")

# Weak mode - collects warnings
config = ValidationConfig(mode="weak")
contact = create_contact(data, validation_config=config)
contact.validate()  # Doesn't raise
warnings = contact.get_validation_warnings()
for warning in warnings:
    print(warning)

# Ignore mode - skips validation
config = ValidationConfig(mode="ignore")
contact = create_contact(data, validation_config=config)
contact.validate()  # No-op
```

### JSON Export

```python
# As dictionary
data_dict = contact.to_json()

# As formatted string
json_str = contact.to_json_string(indent=2)

# Write to file
with open("contact.json", "w") as f:
    f.write(contact.to_json_string(indent=2))
```

### Cloning

```python
contact_copy = contact.clone()
contact_copy.contact_data_set.contact_information.data_set_information.name.set_text("Copy", "en")
# Original contact.name unchanged
```

---

## Data Model Summary

| Entity | Purpose | Key Relationships | Complexity |
|--------|---------|-------------------|------------|
| Contact | People/orgs | Referenced by Process, Source | Low |
| Source | Literature | References Contact | Low |
| UnitGroup | Measurement units | Referenced by FlowProperty | Low |
| FlowProperty | Flow properties | References UnitGroup, Referenced by Flow | Medium |
| Flow | Material/energy flows | References FlowProperty, Referenced by Process | Medium |
| Process | LCA processes | References Flow, Contact, Source | High |
| LCIAMethod | Impact methods | Independent | Medium |
| LifeCycleModel | Lifecycle models | Independent | Medium |

**Total Classes**: 8 entity classes + 1 base + 7 support classes = 16 core classes

**Generated Classes**: 18 Pydantic models (one per JSON schema) + nested models = ~100+ generated classes

---

**Data Model Version**: 1.0
**Last Updated**: 2025-10-31
