# Sub-Task 7: Main Generation Script

**Tasks**: T085-T091 (7 tasks)
**Status**: ⏳ Todo
**File**: `scripts/generate_types.py`

## Objective

Create the main orchestration script that generates all Pydantic models, runs validation, and produces a summary report. This is the entry point for regenerating all types.

## Implementation

Create `scripts/generate_types.py`:

```python
#!/usr/bin/env python3
"""
Main script to generate Pydantic models from TIDAS JSON schemas.

Usage:
    python scripts/generate_types.py
    python scripts/generate_types.py --schema-dir /path/to/schemas
    python scripts/generate_types.py --output-dir src/tidas_sdk/types
    python scripts/generate_types.py --force
"""

import argparse
import sys
import time
from pathlib import Path

from loguru import logger

from schema_parser import SchemaParser
from code_generator import CodeGenerator
from type_mapper import TypeMapper


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate Pydantic models from TIDAS JSON schemas"
    )

    parser.add_argument(
        "--schema-dir",
        type=str,
        help="Directory containing JSON schemas (default: auto-detect)",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default="src/tidas_sdk/types",
        help="Output directory for generated types (default: src/tidas_sdk/types)",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files without prompting",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    return parser.parse_args()


def setup_logging(verbose: bool) -> None:
    """Configure logging level."""
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.remove()
        logger.add(sys.stderr, level="INFO")


def generate_all_schemas(
    parser: SchemaParser,
    generator: CodeGenerator,
    output_dir: Path,
    force: bool
) -> dict:
    """Generate all schema files.

    Args:
        parser: Schema parser instance
        generator: Code generator instance
        output_dir: Output directory path
        force: Overwrite existing files

    Returns:
        Dictionary with generation statistics
    """
    stats = {
        "generated": 0,
        "skipped": 0,
        "errors": 0,
        "schemas": [],
    }

    # Get generation order (topologically sorted)
    generation_order = parser.topological_sort()
    logger.info(f"Will generate {len(generation_order)} schemas")

    # Generate each schema
    for schema_name in generation_order:
        output_file = output_dir / f"{schema_name}.py"

        # Check if file exists
        if output_file.exists() and not force:
            logger.warning(f"Skipping {schema_name} (file exists, use --force to overwrite)")
            stats["skipped"] += 1
            continue

        try:
            # Parse schema
            schema = parser.parse_schema(schema_name)
            logger.debug(f"Parsing {schema_name}...")

            # Generate code
            code = generator.generate_model(
                model_name=schema["title"],
                properties=schema["properties"],
                required=schema["required"],
                description=schema.get("description", "")
            )

            # Add file header
            header = generator.generate_file_header(schema_name)
            full_code = header + code

            # Write to file
            output_file.write_text(full_code, encoding="utf-8")

            logger.info(f"✅ Generated {schema_name}.py")
            stats["generated"] += 1
            stats["schemas"].append(schema_name)

        except Exception as e:
            logger.error(f"❌ Failed to generate {schema_name}: {e}")
            stats["errors"] += 1

    return stats


def generate_init_file(output_dir: Path, schemas: list) -> None:
    """Generate __init__.py with exports.

    Args:
        output_dir: Output directory path
        schemas: List of schema names that were generated
    """
    init_file = output_dir / "__init__.py"

    # Extract model names from schemas
    imports = []
    exports = []

    for schema_name in schemas:
        # Convert schema name to model name
        # e.g., tidas_contacts -> Contacts
        parts = schema_name.replace("tidas_", "").split("_")
        model_name = "".join(word.capitalize() for word in parts)

        imports.append(f"from .{schema_name} import {model_name}")
        exports.append(f'    "{model_name}",')

    # Create init file content
    content = '''"""Generated Pydantic types from TIDAS schemas."""

''' + "\n".join(imports) + '''

__all__ = [
''' + "\n".join(exports) + '''
]
'''

    init_file.write_text(content, encoding="utf-8")
    logger.info(f"✅ Generated __init__.py with {len(exports)} exports")


def print_summary(stats: dict, duration: float) -> None:
    """Print generation summary.

    Args:
        stats: Statistics dictionary
        duration: Generation duration in seconds
    """
    print("\n" + "=" * 60)
    print("GENERATION SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully generated: {stats['generated']} schemas")
    if stats["skipped"] > 0:
        print(f"⏭️  Skipped (existing):    {stats['skipped']} schemas")
    if stats["errors"] > 0:
        print(f"❌ Errors:                {stats['errors']} schemas")
    print(f"⏱️  Duration:              {duration:.2f} seconds")
    print("=" * 60)

    # Performance check
    if duration < 30:
        print("✅ Performance target met (<30 seconds)")
    else:
        print(f"⚠️  Performance target missed (expected <30s, got {duration:.2f}s)")


def main() -> int:
    """Main entry point."""
    args = parse_args()
    setup_logging(args.verbose)

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_dir}")

    # Initialize parser
    try:
        parser = SchemaParser(args.schema_dir)
        parser.load_all_schemas()
        logger.info(f"Loaded {len(parser.schemas)} schemas")
    except FileNotFoundError as e:
        logger.error(str(e))
        return 1

    # Initialize generator
    generator = CodeGenerator()

    # Generate all schemas
    logger.info("Starting code generation...")
    start_time = time.perf_counter()

    stats = generate_all_schemas(parser, generator, output_dir, args.force)

    duration = time.perf_counter() - start_time

    # Generate __init__.py
    if stats["generated"] > 0:
        generate_init_file(output_dir, stats["schemas"])

    # Print summary
    print_summary(stats, duration)

    # Return exit code
    if stats["errors"] > 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Make Script Executable

```bash
chmod +x /Users/biao/Code/tidas-sdk/sdks/python/scripts/generate_types.py
```

## Usage Examples

```bash
cd /Users/biao/Code/tidas-sdk/sdks/python

# Basic usage (auto-detects schema directory)
uv run python scripts/generate_types.py

# Verbose output
uv run python scripts/generate_types.py --verbose

# Force overwrite existing files
uv run python scripts/generate_types.py --force

# Custom schema directory
uv run python scripts/generate_types.py --schema-dir /path/to/schemas

# Custom output directory
uv run python scripts/generate_types.py --output-dir src/my_types
```

## Expected Output

```
2025-10-31 15:30:00 | INFO     | generate_types:main:120 - Output directory: src/tidas_sdk/types
2025-10-31 15:30:00 | INFO     | schema_parser:__init__:35 - Using schema directory: /Users/biao/Code/tidas-tools/src/tidas_tools/tidas/schemas
2025-10-31 15:30:00 | INFO     | generate_types:main:127 - Loaded 18 schemas
2025-10-31 15:30:00 | INFO     | generate_types:main:134 - Starting code generation...
2025-10-31 15:30:00 | INFO     | generate_types:generate_all_schemas:95 - Will generate 18 schemas
2025-10-31 15:30:01 | INFO     | generate_types:generate_all_schemas:113 - ✅ Generated tidas_data_types.py
2025-10-31 15:30:02 | INFO     | generate_types:generate_all_schemas:113 - ✅ Generated tidas_contacts_category.py
...
2025-10-31 15:30:25 | INFO     | generate_types:generate_init_file:145 - ✅ Generated __init__.py with 18 exports

============================================================
GENERATION SUMMARY
============================================================
✅ Successfully generated: 18 schemas
⏱️  Duration:              24.73 seconds
============================================================
✅ Performance target met (<30 seconds)
```

## Validation Script

Create `scripts/validate_generated.py`:

```python
#!/usr/bin/env python3
"""Validate generated types."""

import sys
from pathlib import Path

def check_files_exist():
    """Check all expected files exist."""
    types_dir = Path("src/tidas_sdk/types")
    expected = 18  # 18 schemas

    py_files = list(types_dir.glob("tidas_*.py"))
    actual = len(py_files)

    if actual != expected:
        print(f"❌ Expected {expected} files, found {actual}")
        return False

    print(f"✅ All {expected} type files exist")
    return True


def check_imports():
    """Check files can be imported."""
    try:
        from tidas_sdk.types import tidas_contacts
        from tidas_sdk.types import tidas_flows
        print("✅ Type files can be imported")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def main():
    """Run all checks."""
    checks = [
        check_files_exist,
        check_imports,
    ]

    results = [check() for check in checks]

    if all(results):
        print("\n✅ All validation checks passed!")
        return 0
    else:
        print("\n❌ Some validation checks failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

Run validation:
```bash
uv run python scripts/validate_generated.py
```

## Final Validation

After generation, run complete validation:

```bash
# 1. Type check
PYTHONPATH="src:$PYTHONPATH" uv run mypy src/tidas_sdk/types --strict

# 2. Lint
uv run ruff check src/tidas_sdk/types

# 3. Format check
uv run black --check src/tidas_sdk/types

# 4. Validate script
uv run python scripts/validate_generated.py

# 5. Import test
uv run python -c "from tidas_sdk import create_contact; print('✅ SDK imports work')"
```

## Checklist

- [ ] Main script created and executable
- [ ] CLI arguments implemented (--schema-dir, --output-dir, --force)
- [ ] Progress logging implemented
- [ ] Error handling for each schema
- [ ] Summary report generated
- [ ] Performance timing (<30 seconds)
- [ ] __init__.py generated with exports
- [ ] Validation script passes
- [ ] All generated files pass mypy strict
- [ ] All generated files pass ruff
- [ ] Can import from tidas_sdk

## Troubleshooting

**Issue**: Script can't find schemas
- Check TIDAS_TOOLS_PATH environment variable
- Verify tidas-tools repository is cloned
- Use --schema-dir argument

**Issue**: Black formatting fails
- Ensure black is installed: `uv pip install black`
- Check generated AST is valid
- Try formatting manually to see error

**Issue**: Generation takes >30 seconds
- Profile with `python -m cProfile`
- Check if schemas are being parsed multiple times
- Consider caching parsed schemas

## Success Criteria

Phase 3 is complete when:
- ✅ All 18 schemas generate without errors
- ✅ Generation completes in <30 seconds
- ✅ All generated code passes mypy --strict
- ✅ All generated code passes ruff check
- ✅ Can import and use generated types
- ✅ Summary report shows 0 errors

## Next Phase

After completing Phase 3, proceed to Phase 4: Single Entity Usage (User Story 1).
