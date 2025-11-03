#!/bin/bash
# Helper script to run TIDAS SDK examples

set -e

# Check if example file is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <example_file.py>"
    echo ""
    echo "Available examples:"
    ls -1 examples/*.py 2>/dev/null | grep -v run_ | xargs -n1 basename
    exit 1
fi

EXAMPLE_FILE="$1"

# Check if running from sdks/python directory
if [ ! -f "pyproject.toml" ]; then
    echo "Error: Please run this script from the sdks/python directory"
    echo "  cd /path/to/tidas-sdk/sdks/python"
    echo "  ./examples/run_example.sh $EXAMPLE_FILE"
    exit 1
fi

# Check if example file exists
if [ ! -f "examples/$EXAMPLE_FILE" ]; then
    echo "Error: Example file 'examples/$EXAMPLE_FILE' not found"
    echo ""
    echo "Available examples:"
    ls -1 examples/*.py 2>/dev/null | grep -v run_ | xargs -n1 basename
    exit 1
fi

# Check if package is installed
if ! uv run python -c "import tidas_sdk" 2>/dev/null; then
    echo "📦 Package not installed. Installing in development mode..."
    uv pip install -e ".[dev]"
    echo "✅ Installation complete"
    echo ""
fi

# Run the example
echo "🚀 Running example: $EXAMPLE_FILE"
echo "=================================================="
echo ""
uv run python "examples/$EXAMPLE_FILE"

echo ""
echo "=================================================="
echo "✅ Example completed successfully"
