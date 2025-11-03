# Python SDK Type Generation Improvements

**Date**: 2025-10-31
**Status**: ✅ Partially Completed (Hybrid Approach)

## Problem Statement

Initial auto-generation using `datamodel-code-generator` produced code with quality issues:

### Issues Found

1. **Numbered Class Suffixes**
   ```python
   # ❌ Auto-generated (problematic)
   class Contact1(BaseModel):  # "1" suffix is meaningless
   class Contact2(BaseModel):  # "2" suffix is meaningless
   class Contact(RootModel[Contact1 | Contact2 | ...]):  # Union of numbered classes
   ```

2. **Duplicate Type Definitions**
   - `StringMultiLang1`, `StringMultiLang2` (identical classes)
   - `GlobalReferenceType1`, `GlobalReferenceTypeItem` (similar)
   - Each entity file re-defined base types from `data_types.json`

3. **Poor Semantic Clarity**
   - Class names like `Contact1` don't convey meaning
   - Category enums represented as multiple BaseModel classes
   - No reuse of common types across files

## Solution Implemented: Hybrid Approach

### Approach Overview

**Mix of auto-generation + manual curation**:
- ✅ Auto-generate main entity schemas (contacts, flows, processes, etc.)
- ✅ Manually create base types (`data_types.py`)
- ✅ Manually create category files (demonstrated with `contacts_category.py`)
- ✅ Optimize `datamodel-code-generator` parameters to reduce duplication

### What Was Done

#### 1. Optimized Generation Parameters ✅

Updated `scripts/generate_types_v2.py` with:
```python
cmd = [
    "datamodel-codegen",
    # ... existing params ...
    "--reuse-model",  # Reuse identical models
    "--collapse-root-models",  # Merge RootModel wrappers
    "--union-mode", "smart",  # Intelligent union handling
    "--use-title-as-name",  # Better class names
    "--use-schema-description",  # Add docstrings
]
```

**Result**: Reduced some duplication, but numbered suffixes still present for complex unions.

#### 2. Generation Script Improvements ✅

```python
# Skip category and base type files (manually created)
skip_patterns = ['_category.json', 'data_types.json']
schema_files = [
    f for f in all_schema_files
    if not any(pattern in f.name for pattern in skip_patterns)
]
```

**Result**:
- Only generates 8 main entity files (was 18)
- Generation time: **9.69 seconds** (was 59 seconds) - 83% faster
- Cleaner, more maintainable codebase

#### 3. Manual Base Types (`tidas_data_types.py`) ✅

Created clean, reusable type definitions:

```python
# Clean multi-language types
class MultiLangItemString(BaseModel):
    lang: str = Field(alias='@xml:lang')
    text: Annotated[str, Field(alias='#text', max_length=500)]

StringMultiLang = list[MultiLangItemString] | MultiLangItemString
STMultiLang = list[MultiLangItemST] | MultiLangItemST
FTMultiLang = list[MultiLangItem] | MultiLangItem

# Clean base types
class UUID(RootModel[str]):
    """Unique Universal Identifier."""
    root: Annotated[str, Field(pattern=r'^[0-9a-f]{8}-...$')]

class GlobalReferenceType(BaseModel):
    """Reference to another dataset."""
    type_: str = Field(alias='@type')
    ref_object_id: str = Field(alias='@refObjectId')
    # ... other fields
```

**Benefits**:
- No numbered suffixes
- Clear, semantic names
- Single source of truth
- Reusable across all schemas

#### 4. Manual Category Example (`tidas_contacts_category.py`) ✅

Created as a **demonstration** of the improved approach:

```python
# Clean category definition
Contact = Literal[
    '1',    # Group of organisations, project
    '2',    # Organisations
    '2.1',  # Private companies
    # ... all categories
]

# Runtime metadata
CONTACT_CATEGORIES: dict[str, ContactCategory] = {
    '1': {'level': '0', 'classId': '1', 'text': 'Group of organisations, project'},
    # ...
}
```

**Benefits**:
- No `Contact1`, `Contact2`, etc. classes
- Uses Literal types (matches TypeScript approach)
- Runtime lookup dictionary for metadata
- Much more readable

### Current File Structure

```
src/tidas_sdk/types/
├── __init__.py                           # Exports
├── tidas_data_types.py                   # ✅ Manual (clean base types)
├── tidas_contacts_category.py            # ✅ Manual (clean category example)
├── tidas_contacts.py                     # ⚠️  Auto-generated (has duplicates)
├── tidas_flows.py                        # ⚠️  Auto-generated (has duplicates)
├── tidas_processes.py                    # ⚠️  Auto-generated (has duplicates)
├── tidas_sources.py                      # ⚠️  Auto-generated
├── tidas_flowproperties.py               # ⚠️  Auto-generated
├── tidas_unitgroups.py                   # ⚠️  Auto-generated
├── tidas_lciamethods.py                  # ⚠️  Auto-generated
└── tidas_lifecyclemodels.py              # ⚠️  Auto-generated
```

**Note**: Auto-generated entity files still contain duplicate base type definitions because `datamodel-code-generator` inlines all `$ref` references. This is a known limitation.

## Validation Results

✅ **All 19 files pass mypy --strict**
✅ **Generation time: 9.69 seconds** (vs. 59s originally)
✅ **Manual files demonstrate clean patterns**

## Known Limitations & Future Work

### Limitation 1: Duplicate Types in Entity Files

**Issue**: Generated entity files still re-define base types:
```python
# In tidas_contacts.py (auto-generated)
class StringMultiLang1Item(BaseModel):  # Duplicate!
    field_xml_lang: str = Field(..., alias='@xml:lang')
    text: str = Field(..., alias='#text', max_length=500)
```

**Workaround**: Types are duplicated but functional. Not a runtime issue.

**Future Fix**: Post-process generated files to replace duplicates with imports:
```python
# Post-processing could replace with:
from .tidas_data_types import StringMultiLang, STMultiLang, UUID, GlobalReferenceType
```

### Limitation 2: Category Files Not All Manual

**Issue**: Only `contacts_category.py` manually created as example.

**Status**: 8 other category files could be manually improved but currently use auto-generated versions (functional but have numbered suffixes).

**Future Fix**: Gradually convert remaining category files to manual versions following the `contacts_category.py` pattern.

### Limitation 3: No Import Deduplication

**Issue**: `datamodel-code-generator` doesn't support external type references.

**Future Fix Options**:
1. Post-processing script to deduplicate and add imports
2. Use a different code generator (e.g., custom TypeScript-style generator)
3. Manual maintenance of entity files (not scalable)

## Recommendations

### Immediate (Done)
- [X] Use hybrid approach: auto + manual
- [X] Skip category/base files in generation
- [X] Create clean manual examples

### Short-term (Next Sprint)
- [ ] Create post-processing script to deduplicate types in entity files
- [ ] Manually create remaining 8 category files
- [ ] Add import statements for base types

### Long-term (Future)
- [ ] Consider custom code generator matching TypeScript approach
- [ ] Investigate json-schema-to-pydantic alternatives
- [ ] Create validation suite for generated types

## Usage Guide

### Regenerating Types

```bash
# Generate only main entity schemas (skips categories and data_types)
uv run python scripts/generate_types_v2.py --force

# Manually created files won't be overwritten:
# - src/tidas_sdk/types/tidas_data_types.py
# - src/tidas_sdk/types/tidas_contacts_category.py
```

### Adding New Manual Types

1. Create file in `src/tidas_sdk/types/`
2. Add to skip list in `generate_types_v2.py` if needed
3. Export in `__init__.py`

### Validation

```bash
# Type check
PYTHONPATH="src:$PYTHONPATH" uv run mypy src/tidas_sdk/types --strict

# Import test
uv run python -c "from tidas_sdk.types import tidas_contacts; print('OK')"
```

## Comparison: Before vs. After

### Before (Full Auto-generation)
- ❌ 18 files with numbered suffixes
- ❌ 59 seconds generation time
- ❌ Poor readability
- ✅ All types included

### After (Hybrid Approach)
- ✅ 8 auto-generated + 2 manual files
- ✅ 9.69 seconds generation time
- ✅ Clean manual base types
- ✅ Demonstrated improvement path
- ⚠️  Some duplication remains (acceptable)

## Conclusion

The hybrid approach successfully:
1. **Reduced generation time by 83%**
2. **Eliminated numbered suffixes in manual files**
3. **Created clean, reusable base types**
4. **Demonstrated path for future improvements**

While not perfect (entity files still have some duplication), this is a **pragmatic, maintainable solution** that balances automation with code quality.

The manual files (`data_types.py`, `contacts_category.py`) serve as **templates** for future improvements to other files.

---

**Status**: ✅ Ready for Phase 4 (Entity Wrappers)
**Quality**: Good (with documented improvement path)
**Maintainability**: High (clear patterns, easy to extend)
