# Research: Python SDK Field Hints and Code Completion

**Feature**: 004-python-field-hints
**Date**: 2025-11-03
**Status**: Complete

## Overview

This document consolidates research findings for implementing IDE code completion and type hints in the Python SDK to match the TypeScript SDK's developer experience.

## Research Questions & Findings

### R1: Property Descriptor vs Proxy Pattern

**Question**: Should we use Python property descriptors or a proxy object pattern to enable typed field access?

**Decision**: **Property Descriptors with Lazy Initialization**

**Rationale**:
- Property descriptors are idiomatic Python and work seamlessly with type checkers
- IDEs have first-class support for `@property` decorated methods
- Pydantic v2 already provides model_fields which we can introspect
- Simpler implementation than custom `__getattr__` proxy magic
- Better performance (no proxy overhead on every access)

**Alternatives Considered**:
1. **Proxy Pattern** (`__getattr__`/`__getattribute__`):
   - ❌ Harder for type checkers to understand
   - ❌ Can interfere with IDE autocomplete
   - ❌ More runtime overhead
   - ✓ More flexible for dynamic fields

2. **TypedDict Protocol**:
   - ❌ Doesn't support nested objects well
   - ❌ Requires runtime type checking overhead
   - ✓ Native Python typing support

3. **Dataclasses**:
   - ❌ Would require rewriting entity structure
   - ❌ Breaking change to existing API
   - ✓ Native IDE support

**References**:
- Python Descriptor HowTo: https://docs.python.org/3/howto/descriptor.html
- Pydantic model_fields: https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields

---

### R2: Backwards Compatibility Strategy

**Question**: How do we maintain backwards compatibility with existing dict-based access while adding property access?

**Decision**: **Dual-Mode Access with Dict Fallback**

**Rationale**:
- Keep `_data` dict as source of truth
- Properties delegate to Pydantic model for type safety
- Implement `__getitem__` and `__setitem__` for dict-style access
- Both access modes point to same underlying data structure

**Implementation Pattern**:
```python
class TidasContact(TidasEntity):
    @property
    def contact_data_set(self) -> ContactDataSetType:
        """Typed access to contactDataSet field."""
        return self._get_typed_field("contactDataSet", ContactDataSetType)

    # Dict access still works:
    # contact._data["contactDataSet"]
    # contact["contactDataSet"]  # via __getitem__
```

**Testing Strategy**:
- All existing tests must pass without modification
- Add new tests for typed access
- Validate both access modes return same data

---

### R3: Type Stub Generation

**Question**: Should we generate `.pyi` stub files or rely on inline type hints?

**Decision**: **Inline Type Hints + py.typed Marker**

**Rationale**:
- Inline hints are more maintainable (single source of truth)
- Modern IDEs prefer inline hints over stubs
- PEP 561 `py.typed` marker enables type checking for library users
- Stub files are fallback for edge cases only

**Implementation**:
1. Add `py.typed` marker file to package root
2. Ensure all public methods have complete type annotations
3. Use `typing_extensions` for Python 3.8 compatibility
4. Generate stub files only if inline hints prove insufficient

**References**:
- PEP 561 (Distributing Type Information): https://peps.python.org/pep-0561/
- mypy documentation on stub files: https://mypy.readthedocs.io/en/stable/stubs.html

---

### R4: Nested Field Access Pattern

**Question**: How do we enable IDE completion for deeply nested fields (e.g., `contact.contactDataSet.contactInformation.dataSetInformation`)?

**Decision**: **Recursive Wrapper Classes**

**Rationale**:
- Each nested level returns a typed wrapper object
- Wrappers delegate to underlying Pydantic models
- Type hints propagate through the chain
- Lazy instantiation avoids memory overhead

**Pattern**:
```python
class ContactDataSetWrapper:
    def __init__(self, entity: TidasEntity, data: Dict):
        self._entity = entity
        self._data = data

    @property
    def contact_information(self) -> ContactInformationWrapper:
        """Access nested contactInformation field."""
        return ContactInformationWrapper(
            self._entity,
            self._data.get("contactInformation", {})
        )
```

**Alternatives**:
1. **Flatten All Properties**:
   - ❌ Would create thousands of properties at top level
   - ❌ Doesn't match TIDAS/ILCD structure

2. **ChainMap/Proxy**:
   - ❌ More complex
   - ❌ Harder to type

---

### R5: Multi-Language Text Field Support

**Question**: How do we provide type hints for multi-language text fields with `set_text()` and `get_text()` methods?

**Decision**: **MultiLangText Wrapper Class**

**Rationale**:
- Already exists in codebase (implied by spec examples)
- Needs type hints added to method signatures
- IDE will autocomplete methods on multi-lang fields

**Implementation**:
```python
class MultiLangText:
    def __init__(self, data: List[Dict[str, str]]):
        self._data = data

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for specified language."""
        # Implementation...

    def get_text(self, lang: Optional[str] = None) -> Optional[str]:
        """Get text for specified language (or first if None)."""
        # Implementation...
```

---

### R6: Performance Optimization

**Question**: What performance optimizations can minimize the <5% overhead constraint?

**Decision**: **Lazy Wrapper Instantiation + Caching**

**Rationale**:
- Create wrapper objects only when accessed
- Cache wrapper instances to avoid recreation
- Use `__slots__` in wrapper classes to reduce memory
- Property access has minimal overhead (single dict lookup)

**Benchmarking Plan**:
1. Baseline: Current dict access performance
2. Measure: Property access overhead
3. Target: <5% regression on entity creation and field access

**Optimization Techniques**:
- Use `__slots__` in all wrapper classes
- Cache frequently accessed properties
- Avoid unnecessary Pydantic validation on read
- Lazy initialization of nested wrappers

---

### R7: Type Checker Compatibility

**Question**: Which type checkers must we support and how do we ensure compatibility?

**Decision**: **Target mypy (strict), Pylance, Pyright**

**Rationale**:
- mypy: Industry standard, strict mode required
- Pylance: VS Code default (Pyright-based)
- Pyright: Fast, modern type checker

**Compatibility Strategy**:
- Test with mypy strict mode (`--strict` flag)
- Test with Pylance in VS Code
- Use standard typing constructs (avoid mypy-specific features)
- Provide type: ignore comments only where absolutely necessary

**Testing**:
```bash
# Run type checking in CI
mypy --strict src/tidas_sdk
pyright src/tidas_sdk
```

---

### R8: Code Generation Strategy

**Question**: Should we manually write typed properties or generate them from Pydantic models?

**Decision**: **Fully Automated Generation from JSON Schemas** ✅ IMPLEMENTED

**Rationale**:
- Manual code cannot stay synchronized with schema changes
- JSON schemas are the source of truth
- Existing type generation pipeline can be extended
- Hundreds of fields across 8 entities require automation
- Consistent patterns across all wrapper classes

**Implementation Approach**:
1. Created `scripts/generate_wrappers.py` that parses JSON schemas directly
2. Generates wrapper classes alongside Pydantic models
3. Integrated into `generate_types.py` pipeline
4. Handles special cases:
   - Python keywords (e.g., `class` → `class_`)
   - Complex naming (e.g., `WWWAddress` → `www_address`)
   - Multi-language fields (uses `MultiLangText` wrapper)
   - Nested objects (recursive wrapper generation)

**Output Structure**:
```
src/tidas_sdk/core/wrappers/
├── __init__.py                  # Auto-generated exports
├── contacts_wrappers.py         # ContactsDataSetWrapper + nested
├── flows_wrappers.py            # FlowsDataSetWrapper + nested
├── processes_wrappers.py        # ProcessesDataSetWrapper + nested
├── sources_wrappers.py          # SourcesDataSetWrapper + nested
├── flowproperties_wrappers.py   # FlowpropertiesDataSetWrapper + nested
├── unitgroups_wrappers.py       # UnitgroupsDataSetWrapper + nested
├── lciamethods_wrappers.py      # LciamethodsDataSetWrapper + nested
└── lifecyclemodels_wrappers.py  # LifecyclemodelsDataSetWrapper + nested
```

**Advantages Over Manual**:
- ✅ Zero maintenance cost - schema changes automatically propagate
- ✅ Perfect consistency across all 8 entity types
- ✅ No human error in typing or naming
- ✅ Docstrings extracted from schema descriptions
- ✅ Generation time: <1 second for all entities

---

## Best Practices Applied

### Python Typing Best Practices

1. **Use Protocol for Duck Typing**: If we need flexible types
2. **Generic Types**: Use `TypeVar` for reusable generic wrappers
3. **Literal Types**: For fields with fixed string values (e.g., entity types)
4. **Optional**: Use `Optional[T]` for nullable fields
5. **Union**: Use `Union[A, B]` for fields that can be multiple types

### IDE Completion Best Practices

1. **Docstrings**: Add docstrings to all properties for IDE tooltips
2. **Type Annotations**: Complete type annotations on all public API
3. **Property Decorators**: Use `@property` for read-only access
4. **Avoid Magic**: Prefer explicit over implicit (`__getattr__` is last resort)

### Backwards Compatibility Best Practices

1. **Deprecation Path**: Don't remove dict access, add property access alongside
2. **Testing**: Comprehensive backwards compatibility test suite
3. **Documentation**: Clearly document both access patterns
4. **Migration Guide**: Provide examples of migrating to typed access

---

## Implementation Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Performance regression >5% | Low | High | Benchmark early, optimize with caching |
| Type checker incompatibility | Medium | Medium | Test with multiple type checkers, use standard typing |
| Backwards compatibility breaks | Low | Critical | Comprehensive test suite, keep dict access |
| Complex nested types confuse IDEs | Medium | Medium | Limit nesting depth, provide examples |
| Memory overhead from wrappers | Low | Low | Use `__slots__`, lazy instantiation |

---

## Technology Stack Summary

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| Language | Python | 3.8+ | Target compatibility |
| Type Checking | mypy | Latest | Static type validation |
| IDE Support | Pylance/Pyright | Latest | VS Code autocomplete |
| Runtime Types | Pydantic | v2 | Data validation |
| Testing | pytest | Latest | Test framework |
| Performance | timeit/pytest-benchmark | Latest | Performance measurement |

---

## Next Steps (Phase 1)

1. Create data-model.md documenting entity field structure
2. Design typed wrapper architecture
3. Create example implementation for one entity (TidasContact)
4. Update quickstart.md with typed access examples
5. Generate contracts for typed access API

---

## References

- **Python Typing**: https://docs.python.org/3/library/typing.html
- **PEP 484** (Type Hints): https://peps.python.org/pep-0484/
- **PEP 561** (Distributing Types): https://peps.python.org/pep-0561/
- **Pydantic v2**: https://docs.pydantic.dev/latest/
- **mypy Documentation**: https://mypy.readthedocs.io/
- **Pylance**: https://github.com/microsoft/pylance-release
- **TypeScript SDK Reference**: `sdks/typescript/src/types/tidas_contacts.ts`
