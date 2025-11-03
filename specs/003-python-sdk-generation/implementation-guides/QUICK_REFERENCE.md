# Phase 3 Quick Reference Card

**Last Updated**: 2025-11-03

## Implementation Workflow

```
Start → Guide 1 (✅) → Guide 2 (✅) → Guide 3 (✅) → Guide 4 (✅) → Guide 5 (✅) → Guide 6 (⏳) → Guide 7 (✅) → Done
        Schema         Type          Code          Models        Wrappers      Factories      Main
        Parser         Mapper        Generator                                                Script
```

## Status at a Glance

| Guide | Component | File | Tasks | Status | Time Est. |
|-------|-----------|------|-------|--------|-----------|
| [1](./guide-1-schema-parser.md) | Schema Parser | `scripts/schema_parser.py` | T037-T042 (6) | ✅ Done | 1h |
| [2](./guide-2-type-mapping.md) | Type Mapper | `scripts/type_mapper.py` | T044 (1) | ✅ Done | 2-3h |
| [3](./guide-3-code-generator.md) | Code Generator | `scripts/code_generator.py` | T043-T046 (2) | ✅ Done | 4-6h |
| [4](./guide-4-pydantic-models.md) | Pydantic Models | `src/tidas_sdk/types/*.py` | T047-T065 (19) | ✅ Done | 3-4h |
| [5](./guide-5-entity-wrappers.md) | Entity Wrappers | `src/tidas_sdk/models/*.py` | T066-T074 (9) | ✅ Done | 2-3h |
| [6](./guide-6-factory-functions.md) | Factories | `src/tidas_sdk/factories.py` | T075-T084 (10) | ⏳ Todo | 2-3h |
| [7](./guide-7-main-script.md) | Main Script | `scripts/generate_types.py` | T085-T091 (6) | ✅ Partial (4/6) | 1-2h |

**Total Progress**: 44/55 tasks complete (80%)
**Time Remaining**: ~2-3 hours

## Quick Commands

```bash
# Change to SDK directory
cd /Users/biao/Code/tidas-sdk/sdks/python

# Test schema parser (Guide 1)
uv run python -c "from scripts.schema_parser import SchemaParser; p=SchemaParser(); p.load_all_schemas(); print(f'Loaded {len(p.schemas)} schemas')"

# Test type mapper (Guide 2)
uv run python test_type_mapper.py

# Test code generator (Guide 3)
uv run python test_code_generator.py

# Generate all types (Guide 4 + 7)
uv run python scripts/generate_types.py --force --verbose

# Validate generated code
PYTHONPATH="src:$PYTHONPATH" uv run mypy src/tidas_sdk/types --strict

# Test wrappers (Guide 5)
uv run python test_wrappers.py

# Test factories (Guide 6)
uv run python test_factories.py
```

## Key Files Structure

```
sdks/python/
├── scripts/                          # Code generation scripts
│   ├── schema_parser.py             ✅ Guide 1 (Done)
│   ├── type_mapper.py               ✅ Guide 2 (Done)
│   ├── code_generator.py            ✅ Guide 3 (Done)
│   └── generate_types.py            ✅ Guide 7 (Mostly Complete)
├── src/tidas_sdk/
│   ├── types/                       ✅ Guide 4 (18 files generated)
│   │   ├── tidas_contacts.py
│   │   ├── tidas_flows.py
│   │   └── ... (all 18 schemas)
│   ├── models/                      ✅ Guide 5 (8 wrappers created)
│   │   ├── contact.py
│   │   ├── flow.py
│   │   └── ... (all 8 entities)
│   └── factories.py                 ⏳ Guide 6 (To implement)
└── tests/
    └── generation/                  (Structure created)
```

## Decision Points

### Sequential vs Parallel Implementation

**Sequential (Recommended for first-time)**:
- Follow guides 1→2→3→4→5→6→7 in order
- Test each component before moving on
- Lower risk, easier debugging

**Parallel (For experienced developers)**:
- Guides 2 & 3 can be done in parallel
- Guides 5 & 6 can be done in parallel after Guide 4
- Higher risk, faster completion

## Common Pitfalls & Solutions

| Problem | Solution | Guide |
|---------|----------|-------|
| Can't find schemas | Set TIDAS_TOOLS_PATH or use --schema-dir | 1 |
| Import errors | Check PYTHONPATH includes src/ | All |
| Type errors | Use `from __future__ import annotations` | 2, 3 |
| Black formatting fails | Wrap in try/except, verify AST first | 3 |
| Circular references | Use forward references with quotes | 3, 4 |
| Multi-lang not working | Check _wrap_multilang_fields() called | 5 |
| UUID not generated | Check _ensure_uuid() helper | 6 |
| Generation too slow | Profile with cProfile, cache schemas | 7 |

## Validation Checklist

After completing all guides:

```bash
# File count check
ls -1 src/tidas_sdk/types/*.py | wc -l  # Should be 19 (18 + __init__)
ls -1 src/tidas_sdk/models/*.py | wc -l  # Should be 9 (8 + __init__)

# Type checking
PYTHONPATH="src:$PYTHONPATH" uv run mypy src/tidas_sdk --strict

# Linting
uv run ruff check src/tidas_sdk

# Formatting
uv run black --check src/tidas_sdk

# Import test
uv run python -c "from tidas_sdk import create_contact, create_flow; print('✅ Imports work')"

# Basic functionality test
uv run python -c "
from tidas_sdk import create_contact
c = create_contact()
c.name.set_text('Test', 'en')
assert c.name.get_text('en') == 'Test'
print('✅ Basic functionality works')
"
```

## Success Metrics

Phase 3 complete when ALL these are true:

- [ ] Schema parser loads all 18 schemas
- [ ] Type mapper handles all JSON Schema types
- [ ] Code generator produces valid AST
- [ ] All 18 Pydantic models generated
- [ ] All 8 entity wrappers created
- [ ] All 16 factory functions work (8 single + 8 batch)
- [ ] Main script runs in <30 seconds
- [ ] mypy --strict passes on all generated code
- [ ] ruff check passes
- [ ] Can create and validate entities
- [ ] All tests pass

## Getting Help

- **Conceptual**: Review [research.md](../research.md) for design decisions
- **Architecture**: Review [data-model.md](../data-model.md) for entity structure
- **Reference**: Check TypeScript SDK at `../../../sdks/typescript/`
- **Debugging**: Use `logger.debug()` liberally, run with `--verbose`

## Time Optimization Tips

1. **Use test files**: Create test_*.py for each guide (already provided in guides)
2. **Incremental testing**: Test after each guide, not at the end
3. **Copy patterns**: Once one entity works, copy pattern to others
4. **Batch operations**: Use scripts to generate multiple entities at once
5. **Skip formatting**: Use `--no-format` flag during development, format at end

## Next Phase Preview

After Phase 3, you'll have:
- ✅ All entity types available as Python classes
- ✅ Type-safe API with IDE autocomplete
- ✅ Factory functions for easy entity creation

Phase 4 will focus on:
- Creating example scripts showing real usage
- Writing integration tests
- Validating the API is user-friendly

Ready to start? Begin with [Guide 1: Schema Parser](./guide-1-schema-parser.md) (already complete!) or jump to [Guide 2: Type Mapping](./guide-2-type-mapping.md).
