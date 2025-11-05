# TIDAS Python SDK Examples

This directory contains usage examples for the TIDAS Python SDK.

## 📋 Examples

### Basic Usage
Examples demonstrating fundamental SDK usage patterns:

- [create-contact.py](./create-contact.py) - Create and validate a TIDAS contact
- [basic-validation.py](./basic-validation.py) - Basic data validation examples

### Advanced Usage
More complex examples showing advanced features:

- [complex-workflows.py](./complex-workflows.py) - Complete LCA data workflows
- [custom-validation.py](./custom-validation.py) - Custom validation rules

## 🚀 Running Examples

### Prerequisites

1. Install the development SDK:
```bash
cd ../..
uv sync
```

2. Set up environment:
```bash
source .venv/bin/activate  # or use uv run
```

### Running Individual Examples

```bash
# Run from the examples directory
uv run python create-contact.py

# Or run from the project root
uv run python sdks/python/examples/create-contact.py
```

### Running All Examples

```bash
# From examples directory
for file in *.py; do echo "Running $file"; uv run python "$file"; done
```

## 📝 Example Categories

### 1. Object Creation
Examples showing how to create TIDAS objects:

```python
from tidas_sdk import create_contact

contact = create_contact({
    "name": "Example Organization",
    "email": "contact@example.com"
})
```

### 2. Data Validation
Examples demonstrating validation capabilities:

```python
from tidas_sdk import validate_contact

result = validate_contact(contact_data)
if result.success:
    print("Data is valid")
else:
    print("Validation errors:", result.errors)
```

### 3. JSON Conversion
Examples showing serialization/deserialization:

```python
from tidas_sdk import TidasContact

# From JSON
contact = TidasContact.model_validate_json(json_string)

# To JSON
json_data = contact.model_dump_json()
```

## 🛠️ Development Notes

### Status

⚠️ **Note**: The Python SDK is currently in development. These examples will evolve as the SDK matures.

### Contributing

When adding new examples:

1. Follow the existing naming convention
2. Add clear documentation and comments
3. Include error handling where appropriate
4. Update this README with the new example
5. Test the example works with the current SDK version

### Example Structure

Each example should:

- Be self-contained and runnable
- Include necessary imports
- Demonstrate a specific feature or pattern
- Have clear output or result demonstration
- Include error handling
- Be well-documented with comments

## 🔗 Related Documentation

- **Python SDK README**: [../README.md](../README.md)
- **Development Guidelines**: [../../../CLAUDE.md](../../../CLAUDE.md)
- **Project Progress**: [../../../docs/development-progress.md](../../../docs/development-progress.md)

## 🚧 Current Limitations

Since the Python SDK is under development:

- Some examples may use placeholder implementations
- API may change between versions
- Not all TypeScript SDK features are available yet
- Documentation may be incomplete

## 📞 Getting Help

If you have issues with the examples:

1. Check the development progress documentation
2. Review the main project documentation
3. Open an issue on the GitHub repository
4. Check if you're using the correct development version
