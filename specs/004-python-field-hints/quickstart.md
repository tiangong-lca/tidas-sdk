# Quick Start: Python SDK Typed Field Access

**Feature**: 004-python-field-hints
**Audience**: Python developers using TIDAS SDK
**Time to Complete**: 5-10 minutes

## Before & After Comparison

### Current Experience (Dict Access)

```python
from tidas_sdk import create_contact

contact = create_contact()

# NO IDE autocomplete - must reference docs or schema
# Risk of typos, no type checking
contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:name"] = [
    {"@xml:lang": "en", "#text": "Dr. Jane Smith"}
]

# Complex, error-prone
uuid = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["common:UUID"]
```

### New Experience (Typed Access) ✨

```python
from tidas_sdk import create_contact

contact = create_contact()

# IDE shows all available fields as you type!
# contact.  → shows: contact_data_set
# contact.contact_data_set.  → shows: contact_information, administrative_information
# Full autocomplete chain!

contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)
# ↑ IDE shows: set_text(value: str, lang: str = "en") -> None

# Clean, type-safe
uuid = contact.contact_data_set.contact_information.data_set_information.uuid
# ↑ IDE knows this is type: str
```

---

## Installation

The typed access feature is included in Python SDK v0.2.0+:

```bash
pip install tidas-sdk>=0.2.0

# Or with uv (faster)
uv pip install tidas-sdk>=0.2.0
```

**Requirements**: Python 3.8 or higher

---

## Getting Started

### Step 1: Create an Entity

```python
from tidas_sdk import create_contact

# Create a new contact entity
contact = create_contact()

# The entity now supports both access patterns:
# 1. Typed access (NEW): contact.contact_data_set.field
# 2. Dict access (EXISTING): contact._data["contactDataSet"]["field"]
```

### Step 2: Use IDE Autocomplete

Type `contact.` and press `Ctrl+Space` (or `Cmd+Space` on Mac):

```python
contact.  # IDE shows: contact_data_set, validate(), to_json(), clone(), etc.
```

Continue typing to drill down:

```python
contact.contact_data_set.  # IDE shows: contact_information, administrative_information
contact.contact_data_set.contact_information.  # IDE shows: data_set_information
contact.contact_data_set.contact_information.data_set_information.
# ↑ IDE shows: uuid, short_name, name, classification_information, contact_address,
#              email, telephone, www_address, etc.
```

### Step 3: Set Field Values

```python
# Set UUID
contact.contact_data_set.contact_information.data_set_information.uuid = "550e8400-e29b-41d4-a716-446655440000"

# Set multi-language name
name = contact.contact_data_set.contact_information.data_set_information.name
name.set_text("Dr. Jane Smith", "en")
name.set_text("Dr. Jane Schmidt", "de")

# Set simple fields
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"
contact.contact_data_set.contact_information.data_set_information.telephone = "+1-555-0123"
```

### Step 4: Read Field Values

```python
# Get UUID
uuid = contact.contact_data_set.contact_information.data_set_information.uuid
print(f"UUID: {uuid}")

# Get multi-language text
name = contact.contact_data_set.contact_information.data_set_information.name
english_name = name.get_text("en")  # "Dr. Jane Smith"
german_name = name.get_text("de")   # "Dr. Jane Schmidt"
first_available = name.get_text()   # Returns first language (english in this case)

# Get optional fields (IDE knows these are Optional[str])
email = contact.contact_data_set.contact_information.data_set_information.email
# Type: Optional[str] - IDE shows you it might be None
```

---

## Common Patterns

### Pattern 1: Nested Field Access

**Scenario**: Access deeply nested fields without intermediate None checks

```python
from tidas_sdk import create_contact

contact = create_contact()

# Wrappers handle None/empty dicts gracefully
info = contact.contact_data_set.contact_information.data_set_information

# All fields are accessible, even if not yet set
info.name.set_text("John Doe", "en")
info.email = "john@example.com"
info.telephone = "+1-555-9999"
```

### Pattern 2: Multi-Language Content

**Scenario**: Work with internationalized text fields

```python
# Set multiple languages
name = contact.contact_data_set.contact_information.data_set_information.name
name.set_text("Dr. Jane Smith", "en")
name.set_text("Dr. Jane Schmidt", "de")
name.set_text("Dr. Jeanne Dubois", "fr")

# Get specific language
english = name.get_text("en")  # "Dr. Jane Smith"
german = name.get_text("de")   # "Dr. Jane Schmidt"

# Get first available (when you don't know which languages exist)
any_lang = name.get_text()  # Returns first entry

# Access raw data if needed
all_entries = name.raw  # List[{"@xml:lang": "en", "#text": "..."}]
```

### Pattern 3: Optional Fields

**Scenario**: Safely access fields that might not exist

```python
# IDE shows email is Optional[str]
email = contact.contact_data_set.contact_information.data_set_information.email

if email is not None:
    print(f"Email: {email}")
else:
    print("No email provided")

# Or use default
email = email or "no-email@example.com"
```

### Pattern 4: Type-Safe Assignment

**Scenario**: Let IDE catch type errors before runtime

```python
# This works - IDE is happy
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"

# This causes IDE warning - type error!
# contact.contact_data_set.contact_information.data_set_information.email = 12345
# IDE shows: Type "int" is not assignable to type "str | None"
```

---

## Migration Guide

### Existing Code (Dict Access)

Your existing code continues to work unchanged:

```python
# Old code still works!
contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] = "old@example.com"

# Both access modes point to same data
typed_email = contact.contact_data_set.contact_information.data_set_information.email
dict_email = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"]

assert typed_email == dict_email  # Always true
```

### Gradual Migration

Migrate incrementally - no need to change everything at once:

```python
# Mix both styles during migration
contact = create_contact()

# Use typed access for new code (cleaner, safer)
contact.contact_data_set.contact_information.data_set_information.name.set_text("Name", "en")

# Keep dict access where it already works
if "contactDataSet" in contact._data:
    # Existing code unchanged
    pass
```

---

## IDE Setup

### VS Code with Pylance

1. Install Python extension (includes Pylance)
2. Open settings: `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux)
3. Search for "Type Checking Mode"
4. Set to "basic" or "strict"

**Verify**: Type `contact.` - you should see autocomplete dropdown

### PyCharm

1. Ensure Python interpreter is configured
2. Type checking works out of the box
3. `Ctrl+Space` for autocomplete

**Verify**: Type `contact.` - you should see completion suggestions

### Vim/Neovim with LSP

1. Install pyright language server:
   ```bash
   npm install -g pyright
   ```

2. Configure LSP client (example for coc.nvim):
   ```json
   {
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "pyright.enable": true
   }
   ```

3. Type `contact.` and trigger completion (`Ctrl+Space` or `Ctrl+N`)

---

## Type Checking with mypy

Enable static type checking in your project:

```bash
# Install mypy
pip install mypy

# Run type checker
mypy your_script.py

# Or check entire project
mypy src/
```

**Example mypy output**:

```python
# your_script.py
contact.contact_data_set.contact_information.data_set_information.email = 12345
# mypy error: Incompatible types in assignment (expression has type "int",
#            variable has type "str | None")
```

---

## Performance Considerations

### Lazy Loading

Wrappers are created only when accessed:

```python
contact = create_contact()  # Fast - no wrappers created yet

# First access creates wrapper (small one-time cost)
info = contact.contact_data_set  # Creates ContactDataSetWrapper

# Subsequent accesses use cached wrapper (no overhead)
info2 = contact.contact_data_set  # Returns cached instance
assert info is info2  # Same object
```

### Memory Usage

- **Overhead**: <10% per entity (due to wrapper caching)
- **Optimization**: Wrappers use `__slots__` to minimize memory
- **Trade-off**: Slight memory increase for much better developer experience

### Access Speed

- **Typed access**: ~5% slower than raw dict access (negligible)
- **Caching**: Mitigates performance impact
- **Reality**: Developer time savings far outweigh microseconds

---

## Examples

### Complete Contact Creation

```python
from tidas_sdk import create_contact
import uuid

# Create contact
contact = create_contact()

# Set metadata
info = contact.contact_data_set.contact_information.data_set_information
info.uuid = str(uuid.uuid4())
info.name.set_text("Dr. Jane Smith", "en")
info.name.set_text("Dr. Jane Schmidt", "de")
info.short_name.set_text("J. Smith", "en")
info.email = "jane.smith@research.org"
info.telephone = "+1-555-0123"
info.www_address = "https://research.org/jane"

# Validate
contact.validate()

# Export
json_str = contact.to_json_string(indent=2)
print(json_str)
```

### Working with Flow Entities

```python
from tidas_sdk import create_flow

flow = create_flow()

# Access flow-specific fields with autocomplete
flow_info = flow.flow_data_set.flow_information.data_set_information
flow_info.name.base_name.set_text("Carbon Dioxide", "en")
flow_info.name.base_name.set_text("Kohlendioxid", "de")

# Set flow properties
flow_info.cas_number = "124-38-9"
flow_info.general_comment.set_text("CO2 emissions", "en")

# Validate and export
flow.validate()
```

---

## Troubleshooting

### Issue: No Autocomplete in IDE

**Solution**:
1. Ensure TIDAS SDK v0.2.0+ installed: `pip show tidas-sdk`
2. Restart IDE/LSP server
3. Check Python interpreter is correct
4. Verify `py.typed` file exists in package: `python -c "import tidas_sdk; print(tidas_sdk.__file__)"`

### Issue: Type Checker Errors

**Solution**:
1. Update mypy: `pip install --upgrade mypy`
2. Check Python version compatibility (3.8+)
3. Verify type stubs are installed: `mypy --version`

### Issue: Dict Access Stopped Working

**Solution**: This shouldn't happen! Both work simultaneously:
```python
# Both always work
typed = contact.contact_data_set.contact_information.data_set_information.email
dict_access = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"]
```

If you find a case where dict access breaks, please file a bug report.

---

## Next Steps

1. **Try it out**: Install SDK, create entity, experience autocomplete
2. **Read examples**: Check `examples/05_typed_access.py` for more patterns
3. **Enable type checking**: Add mypy to your project
4. **Gradual migration**: Update one module at a time to typed access

---

## Resources

- **API Reference**: Complete typed API documentation
- **Examples**: `sdks/python/examples/05_typed_access.py`
- **GitHub Issues**: Report bugs or request features
- **TypeScript SDK**: See how TypeScript SDK provides similar experience

---

## Feedback

This is a new feature! We'd love your feedback:

- Does autocomplete work in your IDE?
- Are the type hints helpful?
- Any fields missing type annotations?
- Performance concerns?

File issues at: https://github.com/tiangong-lca/tidas-sdk/issues
