#!/usr/bin/env python3
"""
Generate Pydantic models from TIDAS JSON schemas using datamodel-code-generator.

This script replaces the custom AST-based code generator with a battle-tested library.
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

from loguru import logger


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


def find_schema_dir(provided_dir: str | None) -> Path:
    """Find the TIDAS schemas directory.

    Args:
        provided_dir: User-provided directory path or None

    Returns:
        Path to schemas directory

    Raises:
        FileNotFoundError: If schemas directory not found
    """
    if provided_dir:
        schema_dir = Path(provided_dir)
        if not schema_dir.exists():
            raise FileNotFoundError(f"Schema directory not found: {schema_dir}")
        return schema_dir

    # Try to find tidas-tools
    current = Path.cwd()
    for _ in range(5):  # Search up to 5 levels
        tidas_tools = current / "tidas-tools" / "src" / "tidas_tools" / "tidas" / "schemas"
        if tidas_tools.exists():
            return tidas_tools
        current = current.parent

    raise FileNotFoundError(
        "Could not find TIDAS schemas directory. "
        "Please specify with --schema-dir or ensure tidas-tools is in parent directories."
    )


def generate_schema(
    schema_file: Path,
    output_dir: Path,
    force: bool
) -> tuple[bool, str]:
    """Generate Pydantic model for a single schema file.

    Args:
        schema_file: Path to JSON schema file
        output_dir: Output directory
        force: Whether to overwrite existing files

    Returns:
        Tuple of (success: bool, error_message: str)
    """
    output_file = output_dir / schema_file.name.replace(".json", ".py")

    # Check if file exists
    if output_file.exists() and not force:
        return False, f"File exists (use --force to overwrite)"

    # Run datamodel-codegen with optimization flags
    cmd = [
        "datamodel-codegen",
        "--input", str(schema_file),
        "--input-file-type", "jsonschema",
        "--output", str(output_file),
        "--output-model-type", "pydantic_v2.BaseModel",
        # Code quality improvements
        "--use-standard-collections",  # Use list instead of List
        "--use-union-operator",  # Use | instead of Union
        "--target-python-version", "3.12",
        "--field-constraints",  # Use Field() with constraints
        # Deduplication and cleanup (reduces numbered suffixes)
        "--reuse-model",  # Reuse models with identical content
        "--collapse-root-models",  # Merge RootModel wrappers
        "--union-mode", "smart",  # Intelligent union handling
        # Better naming
        "--use-title-as-name",  # Use schema title as class name
        "--use-schema-description",  # Add docstrings from descriptions
        "--disable-timestamp",  # Remove generation timestamp
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        logger.debug(f"Generated {output_file.name}")
        if result.stdout:
            logger.debug(f"stdout: {result.stdout}")
        return True, ""
    except subprocess.CalledProcessError as e:
        error_msg = f"Failed: {e.stderr if e.stderr else str(e)}"
        logger.error(f"{schema_file.name}: {error_msg}")
        return False, error_msg


def generate_init_file(output_dir: Path, generated_files: list[str]) -> None:
    """Generate __init__.py with exports.

    Args:
        output_dir: Output directory path
        generated_files: List of generated Python file names
    """
    init_file = output_dir / "__init__.py"

    # Extract model names (use 'Model' which is the top-level class)
    imports = []
    exports = []

    for file_name in sorted(generated_files):
        module_name = file_name.replace(".py", "")
        # Import the Model class from each module
        imports.append(f"from .{module_name} import Model as {module_name.title().replace('_', '')}")
        exports.append(f'    "{module_name.title().replace("_", "")}",')

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

    # Find schema directory
    try:
        schema_dir = find_schema_dir(args.schema_dir)
        logger.info(f"Schema directory: {schema_dir}")
    except FileNotFoundError as e:
        logger.error(str(e))
        return 1

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory: {output_dir}")

    # Find all schema files
    all_schema_files = sorted(schema_dir.glob("tidas_*.json"))
    if not all_schema_files:
        logger.error(f"No schema files found in {schema_dir}")
        return 1

    # Skip category files (will be generated by separate clean generator)
    # Also skip data_types (manually maintained for better multi-lang support)
    skip_patterns = ['_category.json', 'data_types.json']
    schema_files = [
        f for f in all_schema_files
        if not any(pattern in f.name for pattern in skip_patterns)
    ]

    logger.info(f"Found {len(all_schema_files)} schemas total")
    logger.info(f"Skipping {len(all_schema_files) - len(schema_files)} category/base schemas (manually created)")
    logger.info(f"Will generate {len(schema_files)} entity schemas")

    # Generate all schemas
    logger.info("Starting code generation...")
    start_time = time.perf_counter()

    stats = {
        "generated": 0,
        "skipped": 0,
        "errors": 0,
        "files": [],
    }

    for schema_file in schema_files:
        success, error = generate_schema(schema_file, output_dir, args.force)

        if success:
            logger.info(f"✅ Generated {schema_file.name}")
            stats["generated"] += 1
            stats["files"].append(schema_file.name.replace(".json", ".py"))
        elif error.startswith("File exists"):
            logger.warning(f"⏭️  Skipped {schema_file.name}: {error}")
            stats["skipped"] += 1
        else:
            stats["errors"] += 1

    duration = time.perf_counter() - start_time

    # Generate __init__.py
    if stats["generated"] > 0:
        generate_init_file(output_dir, stats["files"])

    # Print summary
    print_summary(stats, duration)

    # Generate clean category files (Issue 2 fix)
    print("\n" + "=" * 60)
    print("GENERATING CLEAN CATEGORY FILES")
    print("=" * 60)
    category_script = Path(__file__).parent / "generate_category_types.py"
    if category_script.exists():
        result = subprocess.run(
            [sys.executable, str(category_script)],
            capture_output=False,
            check=False
        )
        if result.returncode != 0:
            print("⚠️  Category generation had warnings/errors")
    else:
        print("⚠️  Category generator script not found")

    # Return exit code
    return 1 if stats["errors"] > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
