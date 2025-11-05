# TIDAS Python SDK

Python SDK for TIDAS (TianGong Life Cycle Assessment data format) providing type-safe data manipulation and validation.

## 🚧 Status

**Version**: 0.1.0 (Development)

This SDK is currently under development. For production use of TIDAS data utilities, consider using the [tidas-tools](https://pypi.org/project/tidas-tools/) package.

## 📋 Features

### Planned Features

- [x] Pydantic-based data models from JSON schemas
- [x] Type-safe data manipulation
- [ ] TIDAS data validation
- [ ] JSON to object conversion
- [ ] Property access utilities
- [ ] Factory functions for entity creation

### Current Implementation

- Basic project structure
- Pydantic dependencies configured
- Type system planning
- Development environment setup

## 🔧 Development Setup

### Prerequisites

- Python 3.12+
- uv (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/tiangong-lca/tidas-sdk.git
cd tidas-sdk/sdks/python

# Install dependencies
uv sync

# Or using pip
pip install -e .
```

### Development Commands

```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Run linting
uv run ruff check

# Type checking
uv run mypy .

# Format code
uv run black .

# Run tests with coverage
uv run pytest --cov=src/tidas_sdk --cov-report=html
```

## 📚 Usage

### Basic Usage (Planned)

```python
from tidas_sdk import TidasContact

# Create a contact
contact = TidasContact(
    name="Example Organization",
    email="contact@example.com"
)

# Validate the contact
contact.validate()

# Convert to JSON
contact_json = contact.model_dump_json()
```

### Current Development

The SDK is currently under development. The API will evolve as we implement features.

## 🏗️ Project Structure

```
sdks/python/
├── src/
│   └── tidas_sdk/          # Main package
├── tests/                  # Test suite
├── examples/               # Usage examples
├── scripts/                # Development scripts
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/tidas_sdk --cov-report=term-missing

# Run specific test
uv run pytest tests/test_example.py
```

## 📖 Documentation

- **Development Guidelines**: [../../CLAUDE.md](../../CLAUDE.md)
- **Project Progress**: [../../docs/development-progress.md](../../docs/development-progress.md)
- **Requirements**: [../../docs/requirement-design.md](../../docs/requirement-design.md)

## 🤝 Contributing

We welcome contributions! Please:

1. Follow the development guidelines in the main repository
2. Add tests for new functionality
3. Ensure code passes linting and type checking
4. Update documentation as needed

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

## 🔗 Related Packages

- [tidas-tools](https://pypi.org/project/tidas-tools/): Production-ready utilities for TIDAS data
- [@tiangong-lca/tidas-sdk](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk): TypeScript SDK
