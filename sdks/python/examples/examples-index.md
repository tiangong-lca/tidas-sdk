# Python SDK Examples Index

This document provides an overview of all available examples in the Python SDK.

## 📋 Available Examples

### 1. Basic Usage (`01_basic_usage.py`)
**Focus**: Fundamental object creation and manipulation
**Topics**:
- Creating TIDAS objects
- Basic property access
- Simple validation
- JSON serialization

### 2. Batch Operations (`02_batch_operations.py`)
**Focus**: Working with multiple objects efficiently
**Topics**:
- Batch creation of objects
- Bulk validation
- Performance optimization
- Memory management

### 3. Validation Modes (`03_validation_modes.py`)
**Focus**: Different validation strategies
**Topics**:
- Strict vs. weak validation
- Custom validation rules
- Error handling patterns
- Validation reporting

### 4. Relationships (`04_relationships.py`)
**Focus**: Managing object relationships
**Topics**:
- Linked data structures
- Reference handling
- Cascade operations
- Relationship validation

### 5. Typed Access (`05_typed_access.py`)
**Focus**: Advanced type-safe property access
**Topics**:
- Type-safe navigation
- Property proxies
- Dynamic access patterns
- Performance considerations

## 🚀 Running Examples

### Prerequisites

Make sure you have the development environment set up:

```bash
cd ../..
uv sync
source .venv/bin/activate
```

### Running Individual Examples

```bash
# From the examples directory
python 01_basic_usage.py

# Or using uv
uv run python 01_basic_usage.py
```

### Running All Examples

Use the provided shell script:

```bash
./run_example.sh
```

Or run manually:

```bash
for example in 0*.py; do
    echo "Running $example..."
    python "$example"
    echo "---"
done
```

## 📊 Example Dependencies

All examples assume:

- Python 3.8+ installed
- Development SDK installed (`uv sync`)
- Access to example data files in `./output/`
- Proper environment variables set (if needed)

## 🔧 Customization

### Modifying Examples

When customizing examples:

1. Keep the original example as a backup
2. Update import paths if needed
3. Test with your specific data
4. Update documentation accordingly

### Creating New Examples

Follow the established pattern:

1. Number sequentially: `06_new_example.py`
2. Include comprehensive documentation
3. Add error handling
4. Update this index
5. Test thoroughly

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure the SDK is properly installed
2. **Data Files**: Check that required data files exist in `./output/`
3. **Version Compatibility**: Examples may require specific SDK versions
4. **Performance**: Some examples may be resource-intensive

### Getting Help

- Check the main README: [../README.md](../README.md)
- Review development guidelines: [../../../CLAUDE.md](../../../CLAUDE.md)
- Open an issue on GitHub

## 📝 Notes

- Examples are designed to be educational and may not represent production-ready code
- Some examples may include placeholder data or simplified logic
- Always adapt examples to your specific use case and requirements
- Keep examples updated with SDK changes
