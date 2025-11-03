# TIDAS Python SDK

Python SDK for TIDAS/ILCD Life Cycle Assessment (LCA) data format.

## Features

- Type-safe operations for all 8 TIDAS entity types
- Multi-language text field support
- Flexible validation modes (strict, weak, ignore)
- High-performance batch operations
- JSON import/export
- Full IDE autocomplete support

## Installation

```bash
pip install tidas-sdk
```

Or with uv (faster):

```bash
uv pip install tidas-sdk
```

## Quick Start

```python
from tidas_sdk import create_contact

# Create a new contact
contact = create_contact()

# Set name with multi-language support
contact.contact_data_set.contact_information.data_set_information.name.set_text(
    "Dr. Jane Smith", "en"
)
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"

# Validate and export
contact.validate()
json_str = contact.to_json_string(indent=2)
print(json_str)
```

## Documentation

- [Quick Start Guide](docs/quickstart.md)
- [API Reference](docs/api_reference.md)
- [Migration Guide](docs/migration_guide.md) (from TypeScript SDK)
- [Examples](examples/)

## Development Setup

### Requirements

- Python 3.8+
- uv (recommended) or pip

### Setup

```bash
cd sdks/python

# Create virtual environment
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install development dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run type checking
uv run mypy src/tidas_sdk

# Run linting
uv run ruff check src/
```

### Code Generation

The SDK includes a code generation system that creates Pydantic models from TIDAS JSON schemas:

```bash
# Generate types from schemas
uv run python scripts/generate_types.py
```

## Supported Entity Types

- Contact
- Flow
- Process
- Source
- Flow Property
- Unit Group
- LCIA Method
- Life Cycle Model

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## Links

- Homepage: https://github.com/tiangong-lca/tidas-sdk
- Documentation: https://tidas-sdk.readthedocs.io
- Issues: https://github.com/tiangong-lca/tidas-sdk/issues
