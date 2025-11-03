# API Contract: Typed Field Access

**Feature**: 004-python-field-hints
**Version**: 1.0.0
**Date**: 2025-11-03

## Overview

This contract defines the API for typed field access in the Python SDK. It specifies the expected behavior, type signatures, and guarantees for all typed access methods.

---

## Contract 1: Entity Base Class Enhancements

### Signature

```python
class TidasEntity(ABC):
    """Enhanced base class with typed field support."""

    def _get_typed_field(
        self,
        field_name: str,
        wrapper_type: Type[T],
        *,
        cache: bool = True
    ) -> T:
        """Get a typed wrapper for a field.

        Args:
            field_name: Name of field in _data dict
            wrapper_type: Type of wrapper class to instantiate
            cache: Whether to cache the wrapper instance

        Returns:
            Instance of wrapper_type

        Raises:
            KeyError: If field_name doesn't exist in _data
        """

    def _ensure_field_exists(self, field_name: str) -> None:
        """Ensure field exists in _data dict.

        Args:
            field_name: Name of field to check/create

        Behavior:
            - If field exists: no-op
            - If field missing: create empty dict {}
        """
```

### Guarantees

1. **G1.1**: `_get_typed_field` with `cache=True` always returns same instance for same field
2. **G1.2**: `_ensure_field_exists` never overwrites existing field data
3. **G1.3**: Wrapper creation has O(1) complexity (dict lookup + instantiation)
4. **G1.4**: Memory overhead per entity: O(n) where n = number of accessed fields

### Test Requirements

```python
def test_get_typed_field_caching():
    """Verify wrapper caching works correctly."""
    entity = TidasContact()
    wrapper1 = entity._get_typed_field("contactDataSet", ContactDataSetWrapper)
    wrapper2 = entity._get_typed_field("contactDataSet", ContactDataSetWrapper)
    assert wrapper1 is wrapper2  # Same instance

def test_get_typed_field_no_cache():
    """Verify cache=False creates new instances."""
    entity = TidasContact()
    wrapper1 = entity._get_typed_field("contactDataSet", ContactDataSetWrapper, cache=False)
    wrapper2 = entity._get_typed_field("contactDataSet", ContactDataSetWrapper, cache=False)
    assert wrapper1 is not wrapper2  # Different instances

def test_ensure_field_exists_preserves_data():
    """Verify existing data is never overwritten."""
    entity = TidasContact()
    entity._data["contactDataSet"] = {"existing": "data"}
    entity._ensure_field_exists("contactDataSet")
    assert entity._data["contactDataSet"] == {"existing": "data"}

def test_ensure_field_exists_creates_empty():
    """Verify missing fields are created as empty dicts."""
    entity = TidasContact()
    entity._ensure_field_exists("newField")
    assert entity._data["newField"] == {}
```

---

## Contract 2: Typed Property Access

### Signature

```python
class TidasContact(TidasEntity):
    """Contact entity with typed field access."""

    @property
    def contact_data_set(self) -> ContactDataSetWrapper:
        """Access contactDataSet field with type hints.

        Returns:
            ContactDataSetWrapper: Typed wrapper for contactDataSet

        Guarantees:
            - Field exists in _data after access
            - Returns cached instance on repeated access
            - Changes to wrapper affect _data dict
        """
```

### Guarantees

1. **G2.1**: Property access creates field in `_data` if missing
2. **G2.2**: Property returns same wrapper instance on repeated access
3. **G2.3**: Wrapper modifications are immediately reflected in `_data`
4. **G2.4**: Property access time: O(1) after first access (cached)

### Test Requirements

```python
def test_property_creates_field():
    """Verify property access creates field if missing."""
    contact = create_contact()
    _ = contact.contact_data_set
    assert "contactDataSet" in contact._data

def test_property_caching():
    """Verify property returns cached wrapper."""
    contact = create_contact()
    wrapper1 = contact.contact_data_set
    wrapper2 = contact.contact_data_set
    assert wrapper1 is wrapper2

def test_property_modifications_affect_data():
    """Verify wrapper changes affect underlying dict."""
    contact = create_contact()
    info = contact.contact_data_set.contact_information.data_set_information
    info.email = "test@example.com"
    assert contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] == "test@example.com"

def test_property_read_after_dict_write():
    """Verify property reads reflect dict writes."""
    contact = create_contact()
    contact._data["contactDataSet"] = {"test": "value"}
    wrapper = contact.contact_data_set
    assert wrapper._data == {"test": "value"}
```

---

## Contract 3: Nested Wrapper Chain

### Signature

```python
class ContactDataSetWrapper:
    """Wrapper for Contact's contactDataSet field."""

    __slots__ = ('_entity', '_data')

    def __init__(self, entity: TidasEntity, data: Dict[str, Any]):
        """Initialize wrapper.

        Args:
            entity: Parent entity (for accessing validation config, etc.)
            data: Dict data for this level (reference, not copy)

        Guarantees:
            - Stores reference to data, not copy
            - Changes to data are reflected in parent
        """

    @property
    def contact_information(self) -> ContactInformationWrapper:
        """Access contactInformation field.

        Returns:
            ContactInformationWrapper: Typed wrapper for nested field

        Guarantees:
            - Creates field in data dict if missing
            - Returns new wrapper instance each time (not cached at this level)
        """
```

### Guarantees

1. **G3.1**: Wrapper stores reference to data dict, not copy
2. **G3.2**: Nested property access creates intermediate dicts
3. **G3.3**: All wrappers in chain point to same entity's `_data`
4. **G3.4**: Wrapper uses `__slots__` for memory efficiency

### Test Requirements

```python
def test_wrapper_stores_reference():
    """Verify wrapper stores reference, not copy."""
    entity = TidasContact()
    wrapper = entity.contact_data_set
    wrapper._data["test"] = "value"
    assert entity._data["contactDataSet"]["test"] == "value"

def test_nested_property_creates_intermediate():
    """Verify nested access creates intermediate dicts."""
    contact = create_contact()
    info = contact.contact_data_set.contact_information
    assert "contactInformation" in contact._data["contactDataSet"]

def test_wrapper_chain_references_same_data():
    """Verify all wrappers reference same root data."""
    contact = create_contact()
    ds = contact.contact_data_set
    ci = ds.contact_information
    dsi = ci.data_set_information
    dsi.email = "test@example.com"
    assert contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] == "test@example.com"

def test_wrapper_uses_slots():
    """Verify wrapper uses __slots__ for memory efficiency."""
    wrapper = ContactDataSetWrapper(None, {})
    assert not hasattr(wrapper, '__dict__')  # No __dict__ means __slots__ is used
```

---

## Contract 4: Multi-Language Text Fields

### Signature

```python
class MultiLangText:
    """Wrapper for multi-language text fields."""

    __slots__ = ('_data',)

    def __init__(self, data: List[Dict[str, str]]):
        """Initialize multi-lang wrapper.

        Args:
            data: List of {"@xml:lang": "en", "#text": "value"} dicts
        """

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for specified language.

        Args:
            value: Text content
            lang: Language code (ISO 639-1)

        Behavior:
            - Updates existing entry if lang exists
            - Appends new entry if lang doesn't exist

        Guarantees:
            - Modifications are reflected in underlying data
            - No duplicate lang entries
        """

    def get_text(self, lang: Optional[str] = None) -> Optional[str]:
        """Get text for specified language.

        Args:
            lang: Language code, or None for first available

        Returns:
            Text content, or None if not found

        Guarantees:
            - Returns None if data is empty
            - Returns None if specified lang not found
            - Returns first entry if lang is None
        """

    @property
    def raw(self) -> List[Dict[str, str]]:
        """Access raw multi-lang array.

        Returns:
            Reference to underlying list (not copy)

        Guarantees:
            - Returns actual reference, modifications affect original
        """
```

### Guarantees

1. **G4.1**: `set_text` never creates duplicate language entries
2. **G4.2**: `get_text(None)` returns first language if any exist
3. **G4.3**: `raw` returns reference, not copy
4. **G4.4**: All operations are O(n) where n = number of languages

### Test Requirements

```python
def test_set_text_updates_existing():
    """Verify set_text updates existing language."""
    data = [{"@xml:lang": "en", "#text": "old"}]
    mlt = MultiLangText(data)
    mlt.set_text("new", "en")
    assert data[0]["#text"] == "new"
    assert len(data) == 1  # No duplicate

def test_set_text_adds_new_language():
    """Verify set_text adds new language entry."""
    data = [{"@xml:lang": "en", "#text": "English"}]
    mlt = MultiLangText(data)
    mlt.set_text("Deutsch", "de")
    assert len(data) == 2
    assert data[1] == {"@xml:lang": "de", "#text": "Deutsch"}

def test_get_text_specific_language():
    """Verify get_text returns correct language."""
    data = [
        {"@xml:lang": "en", "#text": "English"},
        {"@xml:lang": "de", "#text": "Deutsch"}
    ]
    mlt = MultiLangText(data)
    assert mlt.get_text("en") == "English"
    assert mlt.get_text("de") == "Deutsch"
    assert mlt.get_text("fr") is None

def test_get_text_first_available():
    """Verify get_text(None) returns first language."""
    data = [
        {"@xml:lang": "de", "#text": "Deutsch"},
        {"@xml:lang": "en", "#text": "English"}
    ]
    mlt = MultiLangText(data)
    assert mlt.get_text() == "Deutsch"  # First entry

def test_raw_returns_reference():
    """Verify raw property returns reference."""
    data = [{"@xml:lang": "en", "#text": "test"}]
    mlt = MultiLangText(data)
    raw = mlt.raw
    raw.append({"@xml:lang": "de", "#text": "test2"})
    assert len(data) == 2  # Original list modified
```

---

## Contract 5: Backwards Compatibility

### Signature

```python
class TidasContact(TidasEntity):
    """Contact with dual-mode access."""

    def __getitem__(self, key: str) -> Any:
        """Dict-style read access.

        Args:
            key: Field name in _data dict

        Returns:
            Value from _data[key]

        Raises:
            KeyError: If key doesn't exist

        Guarantees:
            - Equivalent to _data[key]
            - No caching, direct passthrough
        """

    def __setitem__(self, key: str, value: Any) -> None:
        """Dict-style write access.

        Args:
            key: Field name in _data dict
            value: Value to set

        Guarantees:
            - Equivalent to _data[key] = value
            - Invalidates cached wrappers for this key
        """
```

### Guarantees

1. **G5.1**: Dict access (`entity["key"]`) works identically to `entity._data["key"]`
2. **G5.2**: Typed access and dict access always return same data
3. **G5.3**: Changes via dict access are visible via typed access
4. **G5.4**: Changes via typed access are visible via dict access
5. **G5.5**: All existing tests pass without modification

### Test Requirements

```python
def test_dict_access_works():
    """Verify dict-style access still works."""
    contact = create_contact()
    contact["contactDataSet"] = {"test": "value"}
    assert contact["contactDataSet"] == {"test": "value"}

def test_typed_and_dict_access_equivalent():
    """Verify both access modes return same data."""
    contact = create_contact()
    contact.contact_data_set.contact_information.data_set_information.email = "typed@example.com"
    assert contact["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] == "typed@example.com"

def test_dict_write_visible_via_typed():
    """Verify dict writes are visible via typed access."""
    contact = create_contact()
    contact._data["contactDataSet"] = {"contactInformation": {"dataSetInformation": {"email": "dict@example.com"}}}
    assert contact.contact_data_set.contact_information.data_set_information.email == "dict@example.com"

def test_typed_write_visible_via_dict():
    """Verify typed writes are visible via dict access."""
    contact = create_contact()
    contact.contact_data_set.contact_information.data_set_information.email = "typed@example.com"
    assert contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"] == "typed@example.com"

def test_existing_tests_pass():
    """Verify all existing tests pass without modification."""
    # This is a meta-test: run entire existing test suite
    # pytest tests/ --ignore=tests/unit/test_typed_access.py
    # All tests must pass
```

---

## Contract 6: Type Checking Compliance

### Signature

```python
# All public methods and properties must have complete type annotations

@property
def contact_data_set(self) -> ContactDataSetWrapper:
    """Return type is explicit, not inferred."""

def set_text(self, value: str, lang: str = "en") -> None:
    """All parameters and return types annotated."""
```

### Guarantees

1. **G6.1**: mypy strict mode passes for all SDK code
2. **G6.2**: Pylance in VS Code provides autocomplete
3. **G6.3**: Pyright type checking passes
4. **G6.4**: Type hints are compatible with Python 3.8+

### Test Requirements

```python
def test_mypy_strict_passes():
    """Verify mypy strict mode passes."""
    # Run: mypy --strict src/tidas_sdk
    # Exit code must be 0

def test_type_annotations_complete():
    """Verify all public methods have type annotations."""
    import inspect
    from tidas_sdk import TidasContact

    for name, method in inspect.getmembers(TidasContact):
        if not name.startswith('_'):  # Public method
            sig = inspect.signature(method)
            assert sig.return_annotation != inspect.Signature.empty, f"{name} missing return type"
            for param_name, param in sig.parameters.items():
                if param_name != 'self':
                    assert param.annotation != inspect.Parameter.empty, f"{name}.{param_name} missing type"
```

---

## Contract 7: Performance Requirements

### Guarantees

1. **G7.1**: Entity instantiation overhead < 5% vs current implementation
2. **G7.2**: Field access overhead < 5% vs dict access
3. **G7.3**: Memory overhead < 10% per entity
4. **G7.4**: Wrapper creation time: O(1)

### Test Requirements

```python
import timeit

def test_instantiation_overhead():
    """Verify entity creation overhead < 5%."""
    baseline = timeit.timeit(
        "create_contact()",
        setup="from tidas_sdk import create_contact",
        number=1000
    )
    # Compare to historical baseline
    assert baseline < 1.05 * HISTORICAL_BASELINE

def test_field_access_overhead():
    """Verify field access overhead < 5%."""
    setup = """
from tidas_sdk import create_contact
contact = create_contact()
contact._data["contactDataSet"] = {"contactInformation": {"dataSetInformation": {"email": "test@example.com"}}}
"""

    dict_access = timeit.timeit(
        'email = contact._data["contactDataSet"]["contactInformation"]["dataSetInformation"]["email"]',
        setup=setup,
        number=10000
    )

    typed_access = timeit.timeit(
        'email = contact.contact_data_set.contact_information.data_set_information.email',
        setup=setup,
        number=10000
    )

    assert typed_access < 1.05 * dict_access

def test_memory_overhead():
    """Verify memory overhead < 10%."""
    import sys
    from tidas_sdk import create_contact

    # Baseline: dict-only access
    contact1 = create_contact()
    baseline_size = sys.getsizeof(contact1._data)

    # With wrappers: access all fields
    contact2 = create_contact()
    _ = contact2.contact_data_set.contact_information.data_set_information
    with_wrappers_size = sys.getsizeof(contact2._data) + sys.getsizeof(contact2._wrappers_cache)

    overhead = (with_wrappers_size - baseline_size) / baseline_size
    assert overhead < 0.10  # < 10%
```

---

## Contract 8: Error Handling

### Guarantees

1. **G8.1**: Invalid field access raises `AttributeError` with helpful message
2. **G8.2**: Type mismatches are caught by type checkers, not at runtime
3. **G8.3**: Optional field access returns `None`, doesn't raise
4. **G8.4**: Missing required fields are caught during validation, not access

### Test Requirements

```python
def test_invalid_field_raises_attribute_error():
    """Verify invalid field access raises AttributeError."""
    contact = create_contact()
    with pytest.raises(AttributeError, match="has no attribute 'invalid_field'"):
        _ = contact.contact_data_set.invalid_field

def test_optional_field_returns_none():
    """Verify optional fields return None when missing."""
    contact = create_contact()
    assert contact.contact_data_set.contact_information.data_set_information.email is None

def test_type_mismatch_caught_by_type_checker():
    """Verify type mismatches are caught by mypy."""
    # This should fail type checking but not raise at runtime
    # Run: mypy test_script.py
    # Expected: error: Incompatible types in assignment
    # contact.contact_data_set.contact_information.data_set_information.email = 12345
```

---

## Summary

This contract defines 8 key areas:

1. **Base Class**: `_get_typed_field`, `_ensure_field_exists` methods
2. **Properties**: Typed property access for all entities
3. **Wrappers**: Nested wrapper chain behavior
4. **Multi-Lang**: `set_text`, `get_text` API
5. **Compatibility**: Dict access continues to work
6. **Type Checking**: mypy compliance
7. **Performance**: < 5% overhead
8. **Errors**: Helpful error messages

All guarantees must be validated by tests before feature is considered complete.
