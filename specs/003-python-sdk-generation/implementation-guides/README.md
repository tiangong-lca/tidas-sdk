# Phase 3 Implementation Guide: Code Generation System

**Status**: In Progress (7% complete)
**Tasks**: T037-T091 (55 tasks)
**Priority**: P1 (Critical Path)

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
| 1. Schema Parser | `scripts/schema_parser.py` | T037-T042 | ✅ Complete | [guide-1-schema-parser.md](./guide-1-schema-parser.md) |
| 2. Type Mapping | `scripts/type_mapper.py` | T044 | ⏳ Todo | [guide-2-type-mapping.md](./guide-2-type-mapping.md) |
| 3. Code Generator | `scripts/code_generator.py` | T043-T046 | ⏳ Todo | [guide-3-code-generator.md](./guide-3-code-generator.md) |
| 4. Pydantic Models | `src/tidas_sdk/types/*.py` | T047-T065 | ⏳ Todo | [guide-4-pydantic-models.md](./guide-4-pydantic-models.md) |
| 5. Entity Wrappers | `src/tidas_sdk/models/*.py` | T066-T074 | ⏳ Todo | [guide-5-entity-wrappers.md](./guide-5-entity-wrappers.md) |
| 6. Factory Functions | `src/tidas_sdk/factories.py` | T075-T084 | ⏳ Todo | [guide-6-factory-functions.md](./guide-6-factory-functions.md) |
| 7. Main Script | `scripts/generate_types.py` | T085-T091 | ⏳ Todo | [guide-7-main-script.md](./guide-7-main-script.md) |

## Quick Start

1. **Complete Schema Parser** (✅ Done)
   - Located at `scripts/schema_parser.py`
   - Reads all 18 JSON schemas
   - Builds dependency graph
   - Performs topological sort

2. **Next Steps** (Choose one):
   - Follow guides in order (recommended for first-time)
   - Skip to specific sub-task if familiar with code generation
   - Run test-driven: Implement tests first, then code

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

## Timeline Estimate

- Sub-task 1: ✅ Complete (1 hour)
- Sub-task 2: 2-3 hours
- Sub-task 3: 4-6 hours
- Sub-task 4: 3-4 hours
- Sub-task 5: 2-3 hours
- Sub-task 6: 2-3 hours
- Sub-task 7: 1-2 hours

**Total**: 15-22 hours

## Getting Help

- Reference `research.md` for technical decisions
- Reference `data-model.md` for entity relationships
- Check TypeScript SDK at `sdks/typescript/` for parity
- Use existing `schema_parser.py` as foundation

## Next Guide

Start with [Sub-Task 1: Schema Parser](./guide-1-schema-parser.md) (already complete) or jump to [Sub-Task 2: Type Mapping](./guide-2-type-mapping.md).
