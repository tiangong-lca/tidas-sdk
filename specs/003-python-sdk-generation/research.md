# Research Findings: Python SDK Generation

**Feature**: 003-python-sdk-generation
**Date**: 2025-10-31

## Overview

This document captures research findings and technology decisions for the Python SDK implementation. Each section addresses a specific technical decision point identified during planning.

---

## 1. Pydantic v2 for Data Validation

### Decision

Use Pydantic v2.x as the primary validation and data modeling framework.

### Rationale

- **Industry Standard**: Pydantic is the de facto Python library for data validation, used by FastAPI, LangChain, and thousands of projects
- **Performance**: v2 includes Rust-based core (pydantic-core) offering 5-17x speed improvements over v1
- **Type Safety**: First-class type hint support with excellent IDE integration
- **Validation Flexibility**: Supports custom validators, field constraints, and multiple validation modes
- **JSON Schema Compatibility**: Can generate and consume JSON schemas, aligning with TIDAS schema source

### Alternatives Considered

- **attrs + cattrs**: More lightweight but lacks built-in validation; would require custom validation layer
- **dataclasses + marshmallow**: Standard library dataclasses with marshmallow validation; less type-safe, more boilerplate
- **Custom validation**: Full control but significant development effort; not worth reinventing

### Implementation Notes

- Pin to `pydantic>=2.0,<3.0` for stability
- Use `model_validate()` for runtime validation
- Leverage `ConfigDict` for model configuration (strict mode, etc.)
- Use `Field()` for constraints (min_length, max_length, pattern, etc.)

### References

- [Pydantic v2 Documentation](https://docs.pydantic.dev/latest/)
- [Pydantic Performance Benchmarks](https://docs.pydantic.dev/latest/concepts/performance/)
- [TypeScript SDK Zod patterns](../../../sdks/typescript/src/schemas/) (for parity)

---

## 2. AST-Based Code Generation

### Decision

Use Python AST (Abstract Syntax Tree) manipulation for generating Pydantic models from JSON schemas.

### Rationale

- **Correctness**: AST generation produces syntactically valid Python by construction
- **Maintainability**: Changes to generation logic are localized and testable
- **Formatting**: Can use `ast.unparse()` + `black` for consistent code style
- **Flexibility**: Allows complex generation patterns (inheritance, decorators, type unions)
- **Debugging**: Generated AST can be inspected and validated before code emission

### Alternatives Considered

- **String Templates (Jinja2)**: Simpler for basic cases but error-prone for complex types; formatting challenges; hard to ensure syntactic validity
- **datamodel-code-generator**: Existing tool for JSON Schema → Pydantic, but less control over output structure and TIDAS-specific patterns
- **Manual Code Writing**: Not sustainable for 18 schemas; defeats purpose of automation

### Implementation Strategy

```python
import ast
from typing import List

def generate_pydantic_model(schema: dict) -> ast.Module:
    # Create ClassDef node
    class_node = ast.ClassDef(
        name=schema["title"],
        bases=[ast.Name(id="BaseModel")],
        keywords=[],
        body=[],
        decorator_list=[]
    )

    # Add fields
    for field_name, field_schema in schema["properties"].items():
        ann_assign = create_field_annotation(field_name, field_schema)
        class_node.body.append(ann_assign)

    # Create module
    module = ast.Module(body=[class_node], type_ignores=[])
    ast.fix_missing_locations(module)

    return module

# Use black for final formatting
import black
code = ast.unparse(module)
formatted_code = black.format_str(code, mode=black.FileMode())
```

### References

- [Python ast module](https://docs.python.org/3/library/ast.html)
- [black code formatter](https://black.readthedocs.io/)

---

## 3. loguru for Structured Logging

### Decision

Use loguru as the logging library instead of standard library `logging`.

### Rationale

- **Better Defaults**: Colored output, automatic timestamps, exception tracing with no configuration
- **Simpler API**: Single `logger` object, no handler/formatter setup needed
- **Structured Logging**: Easy to add context with `logger.bind()` and `logger.contextualize()`
- **Better Error Messages**: Automatically includes exception traceback with syntax highlighting
- **Async-Safe**: Thread-safe and async-aware out of the box
- **User-Friendly**: End users can configure with simple patterns: `logger.add()`, `logger.remove()`

### Alternatives Considered

- **Standard logging**: More portable but verbose configuration; less intuitive for end users
- **structlog**: More powerful for structured logging but overkill for SDK needs; steeper learning curve
- **No logging**: Simplest but removes observability; validation warnings would be lost in weak mode

### Implementation Pattern

```python
from loguru import logger

# SDK setup (in __init__.py)
logger.remove()  # Remove default handler
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="WARNING"  # Default: only warnings and errors
)

# Usage in code
logger.info("Generating types from 18 schemas")
logger.debug("Processing schema: tidas_contacts.json")
logger.warning("Validation warning: {field} {message}", field=path, message=msg)
logger.error("Failed to generate {entity}", entity=name)

# User configuration (in their code)
from loguru import logger
logger.remove()  # Remove default
logger.add(sys.stderr, level="DEBUG")  # Enable debug output
```

### References

- [loguru Documentation](https://loguru.readthedocs.io/)
- [Comparison with standard logging](https://loguru.readthedocs.io/en/stable/resources/migration.html)

---

## 4. uv for Package Management

### Decision

Use uv as the primary package manager and build tool for development.

### Rationale

- **Speed**: 10-100x faster than pip for dependency resolution and installation
- **Modern**: Built-in support for PEP 621 (pyproject.toml metadata)
- **Compatibility**: Works seamlessly with PyPI packages; end users can still use pip
- **Developer Experience**: Single tool for venv creation, dependency management, script running, building, and publishing
- **Reproducibility**: Lock file support for deterministic builds
- **Future-Proof**: Rapidly growing adoption in Python community (by Astral, creators of ruff)

### Alternatives Considered

- **pip + venv**: Standard but slow; no lock files; manual build setup
- **Poetry**: Popular but slower than uv; more opinionated; heavier weight
- **PDM**: Good alternative but less ecosystem momentum than uv
- **pip-tools**: Good for lock files but still requires separate venv management

### Development Workflow

```bash
# Project setup
cd sdks/python
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
uv pip install -e ".[dev]"

# Run scripts
uv run scripts/generate_types.py
uv run pytest
uv run mypy src

# Build and publish
uv build
uv publish --token $PYPI_TOKEN
```

### End User Experience

```bash
# Users can still use pip
pip install tidas-sdk

# Or use uv for speed
uv pip install tidas-sdk
```

### References

- [uv Documentation](https://github.com/astral-sh/uv)
- [uv Performance Benchmarks](https://github.com/astral-sh/uv#performance)

---

## 5. Multi-Language Text API Design

### Decision

Implement multi-language fields as custom descriptor classes with pythonic `set_text()` / `get_text()` methods.

### Rationale

- **User-Friendly**: Explicit methods are discoverable and self-documenting
- **Type-Safe**: Can provide proper type hints for IDE autocomplete
- **Flexible**: Supports both simple cases (single language) and complex (multiple languages)
- **Compatible**: Provides raw array access for advanced users needing direct manipulation
- **Parity**: Mirrors TypeScript SDK's `setText()` / `getText()` API for consistency

### Alternatives Considered

- **Property-based API**: `entity.name['en'] = "value"` - less discoverable, no method chaining
- **Attribute access**: `entity.name_en = "value"` - doesn't support dynamic languages, inflexible
- **Raw arrays only**: `entity.name = [{'@xml:lang': 'en', '#text': 'value'}]` - verbose, error-prone

### Implementation Design

```python
from typing import List, Optional

class MultiLangText:
    """Wrapper for multi-language text fields in TIDAS format."""

    def __init__(self, initial_data: Optional[List[dict]] = None):
        self._items = initial_data or []

    def set_text(self, value: str, lang: str = "en") -> None:
        """Set text for a specific language."""
        # Update existing or append new
        for item in self._items:
            if item["@xml:lang"] == lang:
                item["#text"] = value
                return
        self._items.append({"@xml:lang": lang, "#text": value})

    def get_text(self, lang: Optional[str] = "en") -> Optional[str]:
        """Get text for a specific language, or first available if lang=None."""
        if lang is None:
            return self._items[0]["#text"] if self._items else None

        for item in self._items:
            if item["@xml:lang"] == lang:
                return item["#text"]
        return None

    @property
    def raw(self) -> List[dict]:
        """Access raw array for advanced manipulation."""
        return self._items

    def __repr__(self):
        langs = [item["@xml:lang"] for item in self._items]
        return f"MultiLangText({langs})"

# Usage
contact = create_contact()
name = contact.contact_data_set.contact_information.data_set_information.name

# Pythonic API
name.set_text("Dr. Jane Smith", "en")
name.set_text("Dr. Jane Smith", "fr")
english_name = name.get_text("en")

# Raw access for edge cases
for lang_item in name.raw:
    print(f"{lang_item['@xml:lang']}: {lang_item['#text']}")
```

### References

- [TypeScript SDK MultiLangArray](../../../sdks/typescript/src/types/multi-lang-types.ts)
- [Python Descriptor Protocol](https://docs.python.org/3/howto/descriptor.html)

---

## 6. Validation Mode Implementation

### Decision

Implement validation modes using Pydantic's validation context and custom error handling.

### Rationale

- **Pydantic-Native**: Leverages built-in validation infrastructure
- **Performance**: Ignore mode bypasses validation entirely for speed
- **Flexibility**: Weak mode collects errors without raising exceptions
- **User Control**: Mode configurable per-entity and globally

### Implementation Strategy

```python
from pydantic import ValidationError as PydanticValidationError
from typing import Literal, List

ValidationMode = Literal["strict", "weak", "ignore"]

class ValidationConfig:
    def __init__(self, mode: ValidationMode = "strict"):
        self.mode = mode

class ValidationWarning:
    def __init__(self, field_path: str, message: str, expected: str, actual: Any):
        self.field_path = field_path
        self.message = message
        self.expected = expected
        self.actual = actual

class TidasEntity:
    def __init__(self, data: dict, validation_config: ValidationConfig):
        self._data = data
        self._validation_config = validation_config
        self._validation_warnings: List[ValidationWarning] = []

    def validate(self) -> None:
        """Validate entity data according to current mode."""
        if self._validation_config.mode == "ignore":
            return

        try:
            # Use Pydantic validation
            self._pydantic_model.model_validate(self._data)
        except PydanticValidationError as e:
            if self._validation_config.mode == "strict":
                # Convert to our exception type and raise
                raise ValidationError.from_pydantic(e)
            else:  # weak mode
                # Collect as warnings
                for error in e.errors():
                    warning = ValidationWarning(
                        field_path=".".join(str(p) for p in error["loc"]),
                        message=error["msg"],
                        expected=error["type"],
                        actual=error.get("input")
                    )
                    self._validation_warnings.append(warning)
                    logger.warning(
                        f"Validation warning: {warning.field_path} - {warning.message}"
                    )

    def get_validation_warnings(self) -> List[ValidationWarning]:
        """Get collected validation warnings from weak mode."""
        return self._validation_warnings.copy()
```

### Alternatives Considered

- **Try/Catch Everywhere**: Wrap every operation; too invasive, poor performance
- **Validation Decorators**: Cleaner but harder to control mode at runtime
- **Separate Validator Class**: More modular but adds complexity for users

### References

- [Pydantic Validation Context](https://docs.pydantic.dev/latest/concepts/validators/)
- [TypeScript SDK Validation Modes](../../../sdks/typescript/src/core/config/ValidationConfig.ts)

---

## 7. JSON Schema to Pydantic Mapping

### Decision

Create custom mapping layer that preserves TIDAS-specific patterns and constraints.

### Rationale

- **Precision**: Direct control over type mapping ensures TIDAS semantics preserved
- **Constraints**: Can map JSON Schema constraints to Pydantic Field() constraints
- **Special Cases**: Handle multi-language fields, UUID validation, enum categories
- **Documentation**: Generate docstrings from schema descriptions

### Key Mappings

| JSON Schema Type             | Pydantic Type             | Notes                                            |
| ---------------------------- | ------------------------- | ------------------------------------------------ |
| `string`                     | `str`                     | Add `Field(max_length=N)` if maxLength specified |
| `string` (format: uuid)      | `UUID` (from uuid module) | Automatic UUID validation                        |
| `string` (format: date-time) | `datetime`                | ISO8601 parsing                                  |
| `integer`                    | `int`                     | Add `Field(ge=N, le=M)` for min/max              |
| `number`                     | `float`                   | Similar constraints                              |
| `boolean`                    | `bool`                    | Direct mapping                                   |
| `array`                      | `List[T]`                 | Recursive type resolution                        |
| `object`                     | Nested model              | Create separate Pydantic model                   |
| `enum`                       | `Literal[...]`            | Type-safe enum values                            |
| `anyOf/oneOf`                | `Union[...]`              | Pydantic handles discrimination                  |
| Multi-lang pattern           | `MultiLangText`           | Custom wrapper class                             |

### Implementation Pattern

```python
def json_type_to_python(schema: dict) -> str:
    """Convert JSON Schema type to Python type annotation."""
    json_type = schema.get("type")
    format_type = schema.get("format")

    if json_type == "string":
        if format_type == "uuid":
            return "UUID"
        elif format_type == "date-time":
            return "datetime"
        else:
            return "str"
    elif json_type == "integer":
        return "int"
    elif json_type == "number":
        return "float"
    elif json_type == "boolean":
        return "bool"
    elif json_type == "array":
        item_type = json_type_to_python(schema["items"])
        return f"List[{item_type}]"
    elif json_type == "object":
        return schema.get("title", "dict")  # Use title as class name

    return "Any"

def extract_field_constraints(schema: dict) -> dict:
    """Extract Pydantic Field() constraints from JSON Schema."""
    constraints = {}

    if "maxLength" in schema:
        constraints["max_length"] = schema["maxLength"]
    if "minLength" in schema:
        constraints["min_length"] = schema["minLength"]
    if "pattern" in schema:
        constraints["pattern"] = schema["pattern"]
    if "minimum" in schema:
        constraints["ge"] = schema["minimum"]
    if "maximum" in schema:
        constraints["le"] = schema["maximum"]
    if "description" in schema:
        constraints["description"] = schema["description"]

    return constraints
```

### References

- [JSON Schema Specification](https://json-schema.org/specification)
- [Pydantic Field Types](https://docs.pydantic.dev/latest/concepts/fields/)
- [TIDAS Schema Examples](../../../tidas-tools/src/tidas_tools/tidas/schemas/)

---

## 8. Testing Strategy

### Decision

Multi-layered testing approach: unit tests, integration tests, example verification, and performance benchmarks.

### Rationale

- **Comprehensive Coverage**: Different test types catch different issue categories
- **Regression Prevention**: Generated code changes are automatically validated
- **Documentation**: Examples double as acceptance tests
- **Performance**: Benchmarks ensure success criteria met

### Test Structure

```
tests/
├── unit/
│   ├── test_base_entity.py          # TidasEntity class
│   ├── test_validation.py           # Validation modes
│   ├── test_multilang.py            # MultiLangText
│   ├── test_exceptions.py           # Exception types
│   └── test_factories.py            # Factory functions
├── integration/
│   ├── test_entity_lifecycle.py     # Create, validate, export
│   ├── test_batch_operations.py    # Batch creation/validation
│   ├── test_validation_modes.py    # Mode switching
│   └── test_json_roundtrip.py      # JSON serialization
├── generation/
│   ├── test_schema_parser.py        # JSON schema parsing
│   ├── test_type_generation.py     # Pydantic model generation
│   └── test_generated_code.py      # Validate all 18 generated files
├── performance/
│   ├── test_creation_speed.py       # Entity creation benchmarks
│   ├── test_validation_speed.py    # Validation performance
│   └── test_batch_performance.py   # Batch operations
└── examples/
    └── test_examples.py             # Run all example scripts
```

### Key Test Patterns

```python
# Unit test example
def test_weak_validation_collects_warnings():
    config = ValidationConfig(mode="weak")
    contact = create_contact(invalid_data, config)

    contact.validate()  # Should not raise

    warnings = contact.get_validation_warnings()
    assert len(warnings) > 0
    assert any("UUID" in w.message for w in warnings)

# Integration test example
def test_json_roundtrip_preserves_data():
    original = create_contact(sample_data)
    json_str = original.to_json_string()

    parsed_data = json.loads(json_str)
    restored = create_contact(parsed_data)

    assert restored.to_json() == original.to_json()

# Performance benchmark
def test_batch_creation_performance():
    start = time.perf_counter()
    contacts = create_contacts_batch(
        [{}] * 1000,
        validation_config=ValidationConfig(mode="ignore")
    )
    duration = time.perf_counter() - start

    assert duration < 1.0, f"Took {duration}s, expected <1s"
    assert len(contacts) == 1000
```

### Coverage Goals

- **Unit Tests**: 90%+ line coverage
- **Integration Tests**: All user scenarios from spec covered
- **Generated Code**: All 18 schemas generate and pass mypy
- **Examples**: All examples execute without errors

### References

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-benchmark](https://pytest-benchmark.readthedocs.io/)

---

## 9. Distribution and Installation

### Decision

Publish to PyPI with pre-generated code included in package; use pyproject.toml for metadata.

### Rationale

- **User Convenience**: Users don't need tidas-tools or generation scripts
- **Installation Speed**: Pre-generated code means faster pip install (no build step)
- **Reproducibility**: Generated code is version controlled and tested
- **Standard Practice**: Matches how most Python packages are distributed

### Package Structure

```
tidas-sdk/
├── src/
│   └── tidas_sdk/
│       ├── __init__.py
│       ├── core/
│       ├── models/          # Generated (committed to git)
│       ├── types/           # Generated (committed to git)
│       └── ...
├── tests/
├── examples/
├── pyproject.toml
├── README.md
└── LICENSE
```

### pyproject.toml Configuration

```toml
[project]
name = "tidas-sdk"
version = "0.1.0"
description = "Python SDK for TIDAS/ILCD Life Cycle Assessment data"
authors = [{name = "TIDAS Team"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "pydantic>=2.0,<3.0",
    "loguru>=0.7.0",
    "typing-extensions>=4.0.0; python_version<'3.10'",
]
keywords = ["tidas", "ilcd", "lca", "life-cycle-assessment"]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "mypy>=1.0",
    "ruff>=0.1.0",
    "black>=23.0",
]

[project.urls]
Homepage = "https://github.com/tiangong-lca/tidas-sdk"
Documentation = "https://tidas-sdk.readthedocs.io"
Repository = "https://github.com/tiangong-lca/tidas-sdk"

[build-system]
requires = ["setuptools>=65", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
```

### Release Workflow

```bash
# 1. Regenerate code from latest schemas
uv run scripts/generate_types.py

# 2. Run full test suite
uv run pytest

# 3. Run type checking
uv run mypy src

# 4. Update version in pyproject.toml

# 5. Build package
uv build

# 6. Publish to PyPI
uv publish --token $PYPI_TOKEN

# 7. Tag release
git tag v0.1.0
git push origin v0.1.0
```

### References

- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 621 - pyproject.toml](https://peps.python.org/pep-0621/)

---

## Summary of Decisions

| Area                 | Decision                              | Key Benefit                                 |
| -------------------- | ------------------------------------- | ------------------------------------------- |
| Validation Framework | Pydantic v2                           | Industry standard, performance, type safety |
| Code Generation      | AST manipulation                      | Correctness, maintainability                |
| Logging              | loguru                                | Better defaults, simpler API                |
| Package Manager      | uv                                    | Speed, modern tooling                       |
| Multi-Language API   | Descriptor with set_text/get_text     | Pythonic, discoverable                      |
| Validation Modes     | Pydantic + custom handling            | Flexible, performant                        |
| Schema Mapping       | Custom mapping layer                  | Preserves TIDAS semantics                   |
| Testing              | Multi-layered (unit/integration/perf) | Comprehensive coverage                      |
| Distribution         | PyPI with pre-generated code          | User convenience, standard practice         |

All decisions align with project goals of TypeScript SDK parity, Python ecosystem best practices, and LCA domain requirements.

---

**Research Complete**: 2025-10-31
**Next Phase**: Design artifacts (data-model.md, contracts/, quickstart.md)
