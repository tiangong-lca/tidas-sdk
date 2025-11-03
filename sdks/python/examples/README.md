# TIDAS SDK Examples

This directory contains example scripts demonstrating how to use the TIDAS Python SDK.

## Running the Examples

### Prerequisites

Make sure you're in the `sdks/python` directory and have dependencies installed:

```bash
cd /Users/biao/Code/tidas-sdk/sdks/python
uv pip install -e ".[dev]"
```

### Running Examples

**Option 1: Using the run script (recommended)**

```bash
./examples/run_example.sh 01_basic_usage.py
```

**Option 2: Using uv run**

```bash
uv run python examples/01_basic_usage.py
```

**Option 3: With activated virtual environment**

```bash
source .venv/bin/activate
python examples/01_basic_usage.py
```

## Available Examples

### 01_basic_usage.py ✅

Demonstrates:
- Creating a Contact entity
- Setting multi-language text fields
- Validating entities in strict mode
- Exporting to JSON format
- JSON round-trip preservation

**Output**: Creates `output/contact.json`

### 02_batch_operations.py ✅

Demonstrates:
- Creating 1000+ entities in batch (48,000+ entities/second)
- Performance optimization with validation modes
- Bulk JSON export strategies
- Validation warning collection
- Mixed entity type processing

**Output**: Creates `output/contacts_batch.json`, `output/mixed_entities_batch.json`

### 03_validation_modes.py ✅

Demonstrates:
- Strict mode (raise errors immediately)
- Weak mode (collect all warnings)
- Ignore mode (skip validation for speed)
- When to use each mode
- Performance comparison
- Runtime mode switching
- Global configuration

### 04_relationships.py ✅

Demonstrates:
- Entity references (Flow → FlowProperty → UnitGroup)
- Building complete relationship graphs
- Reference format and structure
- Dependency ordering for export
- Referential integrity considerations

**Output**: Creates `output/relationship_graph.json`

## Example Output

All examples create output files in the `examples/output/` directory. This directory is created automatically and is ignored by git.

## Troubleshooting

### ModuleNotFoundError: No module named 'tidas_sdk'

This means you're not running from the virtual environment. Use one of the methods above.

### Import errors or type errors

Make sure you've installed the package in development mode:

```bash
uv pip install -e ".[dev]"
```

### Validation errors

The examples intentionally demonstrate validation errors to show how the SDK handles invalid data. Check the comments in each example for explanation.
