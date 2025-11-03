# Phase 3 Implementation Guide: Code Generation System

**Status**: In Progress (80% complete - 44/55 tasks)
**Tasks**: T037-T091 (55 tasks)
**Priority**: P1 (Critical Path)
**Last Updated**: 2025-11-03

## Overview

Phase 3 implements the complete code generation pipeline that transforms TIDAS JSON schemas into Python code. This is the most critical phase as all entity types depend on generated code.

## Architecture

```
TIDAS JSON Schemas (18 files)
        ↓
   Schema Parser
        ↓
Type Mapping & Analysis
        ↓
AST Code Generation
        ↓
├─→ Pydantic Models (18 files)
├─→ Entity Wrappers (8 classes)
└─→ Factory Functions (16 functions)
```

## Sub-Tasks Breakdown

| Sub-Task | File | Tasks | Status | Guide |
|----------|------|-------|--------|-------|
| 1. Schema Parser | `scripts/schema_parser.py` | T037-T042 (6) | ✅ Complete | [guide-1-schema-parser.md](./guide-1-schema-parser.md) |
| 2. Type Mapping | `scripts/type_mapper.py` | T044 (1) | ✅ Complete | [guide-2-type-mapping.md](./guide-2-type-mapping.md) |
| 3. Code Generator | `scripts/code_generator.py` | T045-T046 (2) | ✅ Complete | [guide-3-code-generator.md](./guide-3-code-generator.md) |
| 4. Pydantic Models | `src/tidas_sdk/types/*.py` | T047-T065 (19) | ✅ Complete | [guide-4-pydantic-models.md](./guide-4-pydantic-models.md) |
| 5. Entity Wrappers | `src/tidas_sdk/models/*.py` | T066-T074 (9) | ✅ Complete | [guide-5-entity-wrappers.md](./guide-5-entity-wrappers.md) |
| 6. Factory Functions | `src/tidas_sdk/factories.py` | T075-T084 (10) | ⏳ Todo | [guide-6-factory-functions.md](./guide-6-factory-functions.md) |
| 7. Script Enhancement | `scripts/generate_types.py` | T085-T091 (6) | ✅ Partial (4/6) | [guide-7-main-script.md](./guide-7-main-script.md) |

## Current Status & Next Steps

### ✅ Completed (44/55 tasks)
1. **Schema Parser** (6 tasks) - All JSON schemas parsed with dependency graph ✅
2. **Type Mapping** (1 task) - JSON Schema to Python type conversion ✅
3. **Code Generator** (2 tasks) - AST-based Pydantic model generation ✅
4. **Pydantic Models** (19 tasks) - All 18 schemas generated using datamodel-code-generator ✅
5. **Entity Wrappers** (9 tasks) - All 8 entity classes (Contact, Flow, Process, etc.) ✅
6. **Script Enhancement** (4/6 tasks) - CLI, logging, mypy verification ✅

### ⏳ Remaining Work (11 tasks)
1. **Factory Functions** (10 tasks) - create_contact(), create_flow(), batch functions, etc.
2. **Integration** (1 task) - Export factory functions from main __init__.py

### 🎯 Next Steps
- **Focus**: Implement factory functions (Guide 6)
- **Location**: `src/tidas_sdk/factories.py`
- **Estimated Time**: 2-3 hours

## Prerequisites

Before starting Phase 3, ensure:
- ✅ Phase 1 (Setup) complete
- ✅ Phase 2 (Core Foundation) complete
- ✅ tidas-tools repository cloned at `/Users/biao/Code/tidas-tools`
- ✅ Python 3.12+ environment active
- ✅ All dependencies installed (`uv pip install -e ".[dev]"`)

## Key Decisions (from research.md)

1. **AST-Based Generation**: Use Python's `ast` module for syntactically correct code
2. **Pydantic v2**: Leverage Pydantic for validation and type safety
3. **Black Formatting**: Auto-format generated code for consistency
4. **Dependency Order**: Generate schemas in topological order to handle references

## Testing Strategy

Each sub-task has validation criteria:
- **Schema Parser**: Test with sample schema, verify dependency graph
- **Type Mapper**: Test all JSON Schema → Python type mappings
- **Code Generator**: Generate sample class, verify AST structure
- **Models**: Run mypy strict on generated code
- **Wrappers**: Instantiate each entity type
- **Factories**: Create entities and validate structure
- **Main Script**: Generate all 18 schemas, verify no errors

## Expected Outcomes

After completing Phase 3:
- ✅ All 18 Pydantic models generated in `src/tidas_sdk/types/`
- ✅ All 8 entity wrapper classes in `src/tidas_sdk/models/`
- ✅ Factory functions for all entity types in `src/tidas_sdk/factories.py`
- ✅ Generation completes in <30 seconds
- ✅ Generated code passes `mypy --strict`
- ✅ Generated code scores >9.0 on `pylint`

## Timeline Progress

- Sub-task 1: ✅ Complete (Schema Parser)
- Sub-task 2: ✅ Complete (Type Mapping)
- Sub-task 3: ✅ Complete (Code Generator)
- Sub-task 4: ✅ Complete (Pydantic Models - 18 files)
- Sub-task 5: ✅ Complete (Entity Wrappers - 8 classes)
- Sub-task 6: ⏳ Remaining (Factory Functions - 2-3 hours estimated)
- Sub-task 7: ✅ Mostly Complete (4/6 tasks done)

**Original Estimate**: 15-22 hours
**Time Spent**: ~13-17 hours
**Remaining**: 2-3 hours

## Getting Help

- Reference `research.md` for technical decisions
- Reference `data-model.md` for entity relationships
- Check TypeScript SDK at `sdks/typescript/` for parity
- Use existing `schema_parser.py` as foundation

## Next Guide

Start with [Sub-Task 1: Schema Parser](./guide-1-schema-parser.md) (already complete) or jump to [Sub-Task 2: Type Mapping](./guide-2-type-mapping.md).
