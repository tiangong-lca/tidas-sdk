# Implementation Plan: Python SDK Field Hints and Code Completion

**Branch**: `004-python-field-hints` | **Date**: 2025-11-03 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-python-field-hints/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Add IDE code completion and type hints to Python SDK entity objects to match the developer experience of the TypeScript SDK. Currently, Python developers must use dict-style access (`contact._data["contactDataSet"]`) which provides no IDE support. The solution will leverage Python's property descriptors and Pydantic models to expose typed attributes while maintaining backwards compatibility with existing dict-based access patterns.

**Technical Approach**: Create typed wrapper properties that delegate to Pydantic models, enabling IDE autocomplete while preserving the existing dictionary interface for backwards compatibility.

## Technical Context

**Language/Version**: Python 3.8+ (targeting 3.8 for widest compatibility, optimized for 3.12)
**Primary Dependencies**: Pydantic v2 (already in use), typing/typing_extensions, datamodel-code-generator (code gen)
**Storage**: N/A (SDK library, no persistent storage)
**Testing**: pytest (existing), mypy strict mode (type checking), pylance/pyright (IDE validation)
**Target Platform**: Cross-platform Python (Linux, macOS, Windows) - library SDK
**Project Type**: Library/SDK enhancement (existing monorepo structure in sdks/python/)
**Performance Goals**: <5% overhead on entity instantiation, <500ms IDE autocomplete response
**Constraints**:
- Backwards compatibility required (existing dict access must continue to work)
- Type hints compatible with Python 3.8+
- No runtime dependencies beyond existing (Pydantic v2)
- Generated code must pass mypy strict mode
**Scale/Scope**:
- 8 entity types (Contact, Flow, Process, Source, FlowProperty, UnitGroup, LCIAMethod, LifeCycleModel)
- ~50-100 nested fields per entity type
- Generated code from 18 JSON schemas

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Constitution Status**: No formal constitution defined for this project. Standard software engineering best practices will be applied:
- ✅ Test-driven development (write tests before implementation)
- ✅ Backwards compatibility (existing code must continue to work)
- ✅ Type safety (mypy strict mode compliance)
- ✅ Performance (< 5% regression)
- ✅ Documentation (docstrings, examples, type hints)

**Gates**:
1. ✅ Feature enhances existing SDK (no new projects)
2. ✅ Backwards compatible (non-breaking change)
3. ✅ Follows existing project structure
4. ✅ No new external dependencies

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (Existing SDK Structure)

```text
sdks/python/
├── src/tidas_sdk/
│   ├── __init__.py              # Public API (no changes needed)
│   ├── core/
│   │   ├── base.py              # TidasEntity base class (MODIFIED - add _get_typed_field())
│   │   ├── validation.py        # Validation config (no changes)
│   │   ├── exceptions.py        # Error types (no changes)
│   │   ├── typed_access.py      # Base classes (MultiLangText, BaseWrapper)
│   │   └── wrappers/            # AUTO-GENERATED wrapper classes
│   │       ├── __init__.py                  # Generated exports
│   │       ├── contacts_wrappers.py         # ContactsDataSetWrapper + nested
│   │       ├── flows_wrappers.py            # FlowsDataSetWrapper + nested
│   │       ├── processes_wrappers.py        # ProcessesDataSetWrapper + nested
│   │       ├── sources_wrappers.py          # SourcesDataSetWrapper + nested
│   │       ├── flowproperties_wrappers.py   # FlowpropertiesDataSetWrapper + nested
│   │       ├── unitgroups_wrappers.py       # UnitgroupsDataSetWrapper + nested
│   │       ├── lciamethods_wrappers.py      # LciamethodsDataSetWrapper + nested
│   │       └── lifecyclemodels_wrappers.py  # LifecyclemodelsDataSetWrapper + nested
│   ├── models/                  # Entity wrapper classes (MODIFY to import wrappers)
│   │   ├── __init__.py
│   │   ├── contact.py           # TidasContact (MODIFIED - add property)
│   │   ├── flow.py              # TidasFlow (MODIFY - add property)
│   │   ├── process.py           # TidasProcess (MODIFY - add property)
│   │   ├── source.py            # TidasSource (MODIFY - add property)
│   │   ├── flow_property.py     # TidasFlowProperty (MODIFY - add property)
│   │   ├── unit_group.py        # TidasUnitGroup (MODIFY - add property)
│   │   ├── lcia_method.py       # TidasLCIAMethod (MODIFY - add property)
│   │   └── life_cycle_model.py  # TidasLifeCycleModel (MODIFY - add property)
│   ├── types/                   # Generated Pydantic models (READ ONLY)
│   │   ├── tidas_contacts.py    # Contact Pydantic models
│   │   ├── tidas_flows.py       # Flow Pydantic models
│   │   └── ...                  # Other generated types
│   ├── factories.py             # Factory functions (no changes needed)
│   └── py.typed                 # CREATED - PEP 561 marker for type checking
│
├── tests/
│   ├── unit/
│   │   ├── test_typed_access.py    # NEW - Test typed property access
│   │   └── test_type_hints.py      # NEW - Test mypy compliance
│   ├── integration/
│   │   ├── test_backwards_compat.py # NEW - Ensure dict access still works
│   │   └── test_ide_completion.py   # NEW - Validate IDE experience
│   └── performance/
│       └── test_overhead.py         # NEW - Measure performance impact
│
├── examples/
│   └── 05_typed_access.py          # CREATED - Demonstrate typed field access
│
├── scripts/
│   ├── generate_types.py        # MODIFIED - Added wrapper generation call
│   └── generate_wrappers.py        # CREATED - Auto-generate wrapper classes from schemas
│
└── pyproject.toml                   # MODIFIED - Add py.typed to package-data
```

**Structure Decision**: Extend existing SDK structure in `sdks/python/` monorepo. This is an enhancement to the current implementation, not a new project. Key changes:
- **Auto-generation approach**: Created `scripts/generate_wrappers.py` that generates wrapper classes from JSON schemas
- **Integration**: Wrapper generation integrated into existing `generate_types.py` pipeline
- **Base classes**: `core/typed_access.py` contains `MultiLangText` and `BaseWrapper` base classes
- **Generated wrappers**: All wrapper classes auto-generated in `core/wrappers/` directory
- **Entity modifications**: Each entity class gets a single property that returns the generated wrapper
- **Type checking**: Add `py.typed` marker for PEP 561 compliance
- **Maintenance**: Schema changes automatically propagate through generation pipeline

## Complexity Tracking

**No violations** - This enhancement follows existing patterns and adds minimal complexity:
- Leverages existing Pydantic models (already generated)
- Uses standard Python property descriptors (no magic)
- Maintains backwards compatibility
- No new architectural patterns introduced
