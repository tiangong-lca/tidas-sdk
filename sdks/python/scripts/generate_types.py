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
        "schema_to_model": {},  # Map schema names to model names
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

            model_name = schema["title"]

            # Generate code
            code = generator.generate_model(
                model_name=model_name,
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
            stats["schema_to_model"][schema_name] = model_name

        except Exception as e:
            logger.error(f"❌ Failed to generate {schema_name}: {e}")
            stats["errors"] += 1

    return stats


def generate_init_file(output_dir: Path, schema_to_model: dict) -> None:
    """Generate __init__.py with exports.

    Args:
        output_dir: Output directory path
        schema_to_model: Dictionary mapping schema names to model class names
    """
    init_file = output_dir / "__init__.py"

    # Create imports and exports
    imports = []
    exports = []

    for schema_name, model_name in sorted(schema_to_model.items()):
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
        generate_init_file(output_dir, stats["schema_to_model"])

    # Print summary
    print_summary(stats, duration)

    # Return exit code
    if stats["errors"] > 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
