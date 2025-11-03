# Feature Specification: Python SDK Generation

**Feature ID**: 003-python-sdk-generation
**Created**: 2025-10-31
**Status**: Draft
**Branch**: 003-python-sdk-generation

## Overview

### Purpose
Provide Python developers with a feature-complete SDK for managing TIDAS/ILCD Life Cycle Assessment (LCA) data that mirrors the capabilities and user experience of the existing TypeScript SDK.

### Context
The TypeScript SDK successfully provides type-safe data operations for TIDAS/ILCD formats with automatic code generation from JSON schemas. Python developers working in LCA, sustainability analysis, and environmental data management need equivalent functionality with a Python-native experience while maintaining API consistency across language SDKs.

### Goals
- Enable Python developers to work with TIDAS/ILCD data using familiar Python patterns and conventions
- Automate code generation from tidas-tools JSON schemas to ensure schema consistency across SDKs
- Provide runtime data validation with configurable strictness levels
- Support all 8 TIDAS entity types with full CRUD operations
- Deliver comprehensive documentation and examples matching TypeScript SDK coverage
- Maintain API consistency with TypeScript SDK for cross-language project compatibility

## Clarifications

### Session 2025-10-31

- Q: When validation fails or JSON parsing errors occur, how should the SDK handle these errors? → A: Raise Python exceptions with structured error data - Pythonic, stacktrace-friendly
- Q: How should the SDK access tidas-tools JSON schemas during code generation? → A: Relative path from SDK repo to tidas-tools - assume side-by-side clone
- Q: In "weak" validation mode, which schema violations should be treated as warnings versus errors? → A: All violations become warnings - weak mode never raises exceptions
- Q: Should the SDK provide logging capabilities for debugging and observability? → A: Use loguru as logging module
- Q: How should the SDK be packaged and distributed to end users? → A: Use uv to manage - uv for development, PyPI for distribution

## User Scenarios & Testing

### Primary User Flows

**Scenario 1: Data Scientist Creating LCA Process Data**
1. Developer installs tidas-sdk via pip
2. Imports process creation function and types
3. Creates a new Process entity with auto-generated UUID
4. Sets multi-language name and description fields using helper methods
5. Adds process exchanges (inputs/outputs) with proper flow references
6. Validates data against TIDAS schema with detailed error messages
7. Exports validated data to JSON file for database import

**Scenario 2: Researcher Batch Processing LCA Datasets**
1. Developer loads 500+ flow datasets from JSON files
2. Creates Flow entities in batch with weak validation mode for performance
3. Updates specific fields across all entities (e.g., methodology version)
4. Validates all entities and collects validation warnings
5. Filters entities with critical issues for manual review
6. Exports clean datasets to JSON with proper formatting

**Scenario 3: Software Engineer Building Data Pipeline**
1. Developer generates Python classes from updated TIDAS schemas using `uv run generate`
2. Reviews generated code structure matching TypeScript SDK organization
3. Integrates generated classes into existing ETL pipeline
4. Uses type hints for IDE autocomplete and static type checking
5. Configures validation mode per environment (strict in dev, weak in prod)
6. Builds and publishes updated package to PyPI using `uv build` and `uv publish`

**Scenario 4: Student Learning LCA Data Standards**
1. Student follows Getting Started tutorial from documentation
2. Creates first Contact entity with provided example code
3. Experiments with multi-language text field helpers (setText/getText)
4. Makes intentional validation errors to understand schema requirements
5. Reviews detailed validation error messages with field path information
6. Successfully creates valid Contact and exports to JSON

### Acceptance Criteria

1. **Installation & Setup**: User can install SDK via `pip install tidas-sdk` or `uv pip install tidas-sdk` and import core functionality within 2 minutes
2. **Code Generation**: Running generation script produces Python modules from all 18 JSON schemas without errors in under 30 seconds
3. **Entity Creation**: User can create any of the 8 entity types with 5-10 lines of code
4. **Multi-language Support**: setText/getText methods work consistently across all multi-language fields
5. **Validation Modes**: User can switch between strict/weak/ignore validation modes per entity or globally
6. **Batch Operations**: Creating 1000 entities with validation-ignore mode completes in under 1 second
7. **Type Safety**: Type hints enable IDE autocomplete for all entity attributes and methods
8. **Error Messages**: Validation errors include field path, expected type/format, and actual value
9. **JSON Interop**: Entity-to-JSON and JSON-to-entity conversion preserves all data without loss
10. **Documentation**: Each entity type has documented example code that executes without modification

## Functional Requirements

### Code Generation System

**REQ-1: Schema Discovery & Processing**
- System shall locate tidas-tools schemas using relative path `../tidas-tools/src/tidas_tools/tidas/schemas/` from SDK repository root
- System shall support TIDAS_TOOLS_PATH environment variable to override default relative path
- System shall raise clear error with setup instructions if tidas-tools schemas directory not found
- System shall scan located schemas directory for all JSON schema files
- System shall parse JSON schemas to extract type definitions, constraints, and relationships
- System shall identify multi-language field patterns (`@xml:lang`, `#text` structure)
- System shall detect dependency relationships between schemas (e.g., Process depends on Flow)
- System shall generate schemas in dependency order to handle forward references

**REQ-2: Python Class Generation**
- System shall generate Pydantic model classes with proper inheritance hierarchy
- System shall create type hints using Python 3.8+ typing syntax
- System shall generate dataclasses for simple value objects where appropriate
- System shall preserve schema validation constraints as Pydantic validators
- System shall generate docstrings from schema descriptions and examples

**REQ-3: Multi-language Field Handling**
- System shall generate specialized classes for multi-language text fields
- Generated classes shall provide setText(value, lang='en') and getText(lang='en') methods
- System shall support both array-based multi-language fields (multiple translations) and single-object fields
- System shall default to 'en' language when language parameter is omitted

**REQ-4: Validation Schema Generation**
- System shall generate Pydantic validation rules matching Zod schemas in TypeScript SDK
- System shall apply string length constraints (e.g., max 500 chars for short strings)
- System shall validate UUID format for identifier fields
- System shall enforce required vs optional field constraints
- System shall validate enum values against allowed categories

### Entity Management

**REQ-5: Entity Base Class**
- All entity classes shall inherit from common TidasEntity base class
- Base class shall provide validate() method that raises ValidationError exception in strict mode, collects warnings in weak mode, or skips validation in ignore mode
- Base class shall provide get_validation_warnings() method returning list of ValidationWarning objects from weak mode validation
- Base class shall provide to_json() and to_json_string() methods
- Base class shall provide clone() method for deep copying
- Base class shall provide get_value(path) for nested field access using dot notation

**REQ-6: Factory Functions**
- System shall provide create_contact(), create_flow(), create_process(), etc. functions
- Factory functions shall accept optional initial data dictionary
- Factory functions shall accept optional validation configuration
- Factory functions shall generate new UUID if not provided in initial data
- Batch factory functions (create_contacts_batch) shall efficiently create multiple entities

**REQ-7: Validation Configuration**
- User shall configure validation mode per entity: strict, weak, or ignore
- User shall set global validation mode affecting all new entities
- Strict mode shall raise ValidationError exception for any schema violation
- Weak mode shall convert all schema violations to warnings (never raises ValidationError), allowing data processing to continue with validation issues logged
- Ignore mode shall skip validation entirely for maximum performance (no validation, no warnings)

**REQ-8: Multi-language Text Operations**
- Users shall set multi-language text using entity.field.set_text(value, lang='en')
- Users shall retrieve text using entity.field.get_text(lang='en')
- Users shall access raw multi-language array structure for advanced manipulation
- System shall preserve all language variants when updating single language

### Data Operations

**REQ-9: JSON Serialization**
- to_json() shall return dictionary matching TIDAS/ILCD JSON structure
- to_json_string() shall return formatted JSON string with optional indentation
- System shall exclude None values from JSON output
- System shall exclude empty objects and arrays from JSON output
- System shall handle circular references gracefully

**REQ-10: JSON Deserialization**
- Factory functions shall accept JSON dictionary as initial data
- System shall validate JSON structure during entity creation, raising ValidationError for schema violations
- System shall raise JSONDecodeError for malformed JSON with helpful error messages indicating location and cause
- System shall handle missing optional fields gracefully (no exception raised)
- System shall preserve unknown fields when validation mode is weak/ignore

**REQ-11: Relationship Management**
- Users shall reference other entities using UUID fields
- System shall provide type-safe reference objects with refObjectId, type, version fields
- System shall not enforce referential integrity (references stored as data only)
- Documentation shall provide examples of creating entity relationships

### Error Handling

**REQ-15: Exception Types & Structure**
- System shall define ValidationError exception for schema validation failures in strict mode, including field path, expected type/constraint, and actual value
- System shall use standard JSONDecodeError for JSON parsing failures (raised regardless of validation mode)
- System shall define TidasException base class for all SDK-specific exceptions
- System shall define ValidationWarning for weak mode violations, with same structured data as ValidationError but as warnings
- All exceptions shall include structured error data accessible as exception attributes
- Exception messages shall be human-readable and actionable (e.g., "Field 'contactDataSet.contactInformation.dataSetInformation.common:UUID' must be valid UUID format, got 'invalid-uuid'")
- Weak mode shall collect all violations as ValidationWarning objects accessible via entity.get_validation_warnings() method

### Logging & Observability

**REQ-16: Logging Infrastructure**
- System shall use loguru library for all logging operations
- System shall log code generation progress (schema discovery, class generation, file writes) at INFO level
- System shall log validation warnings from weak mode at WARNING level
- System shall log entity creation and operations at DEBUG level
- Users shall configure log level and output via loguru's standard configuration API
- System shall use structured logging with contextual information (entity type, field paths, operation names)
- Default configuration shall log WARNING and above to stderr, with color-coded output

### Documentation & Examples

**REQ-12: API Documentation**
- All public classes and methods shall have docstrings with type information
- Documentation shall include "Quick Start" guide for first-time users
- Documentation shall include comprehensive API reference generated from code
- Each entity type shall have dedicated usage guide with code examples

**REQ-13: Example Code**
- Examples directory shall include 4+ complete working examples
- Examples shall cover: basic entity creation, batch operations, validation modes, relationships, logging configuration
- Each example shall include comments explaining TIDAS concepts
- Examples shall be executable with `python examples/01-basic-usage.py` syntax
- Examples shall demonstrate configuring loguru for different verbosity levels

**REQ-14: Migration Guide**
- Documentation shall include TypeScript-to-Python API mapping table
- Guide shall highlight Python-specific idioms (e.g., snake_case vs camelCase)
- Guide shall explain equivalent patterns for common TypeScript SDK usage

### Package Management & Distribution

**REQ-17: Development Tooling**
- Project shall use uv for dependency management, virtual environment creation, and build tooling
- Project shall define dependencies in pyproject.toml following PEP 621 standard
- Development workflow shall use uv commands (uv pip install, uv run, uv build)
- Generated code shall be committed to repository for reproducible builds

**REQ-18: Package Distribution**
- SDK shall be distributed via PyPI as `tidas-sdk` package
- Package shall include all generated Python code (users do not need tidas-tools)
- Package shall use modern build system (pyproject.toml with setuptools or hatchling backend)
- Package shall be installable via `pip install tidas-sdk` or `uv pip install tidas-sdk`
- Package metadata shall specify Python version compatibility (>=3.8) and required dependencies

## Success Criteria

### Developer Productivity
- End user installs SDK and creates first valid TIDAS entity within 10 minutes
- SDK developer regenerates all code from schemas in under 30 seconds using uv
- IDE provides autocomplete suggestions for 90%+ of entity attributes
- Validation error messages allow developer to fix issues without consulting schema docs
- Batch processing 1000 entities completes in under 5 seconds (validation-ignore mode)

### Code Quality
- Generated code passes mypy strict type checking without errors
- Generated code passes pylint with score > 9.0
- 100% of generated public methods have docstrings
- Code follows PEP 8 style guidelines

### Functional Completeness
- All 8 TIDAS entity types support full create, read, validate, export lifecycle
- All 18 JSON schemas generate valid Python code without manual edits
- Multi-language text operations work identically to TypeScript SDK behavior
- Validation modes produce consistent results with TypeScript SDK validation

### Documentation Coverage
- 100% of public API methods have docstring documentation
- Examples demonstrate 80%+ of common SDK usage patterns
- Documentation loads in user's browser and renders correctly
- Quick Start tutorial executable without errors by first-time user

### Performance
- SDK initialization (import time) completes in under 500ms
- Creating single entity with strict validation completes in under 10ms
- Batch creating 100 entities with weak validation completes in under 100ms
- JSON export of 50-field entity completes in under 5ms

### Compatibility
- SDK works on Python 3.8, 3.9, 3.10, 3.11, 3.12 without modifications
- SDK installs successfully on Linux, macOS, Windows platforms
- SDK has minimal required dependencies: Pydantic (v2.x), loguru, typing_extensions
- Generated code remains compatible when tidas-tools schemas are updated

## Key Entities

### Generated Classes
- **MultiLangText**: Wrapper class for multi-language text fields with setText/getText methods
- **TidasEntity**: Abstract base class for all entity types with validation and serialization
- **Contact**: Generated class for contact/organization data
- **Flow**: Generated class for material/energy flow data
- **Process**: Generated class for process dataset
- **Source**: Generated class for literature source references
- **FlowProperty**: Generated class for flow properties (mass, energy, etc.)
- **UnitGroup**: Generated class for measurement unit groups
- **LCIAMethod**: Generated class for LCIA methodology data
- **LifeCycleModel**: Generated class for life cycle model definitions

### Data Structures
- **ValidationConfig**: Mode (strict/weak/ignore), includeWarnings flag
- **ReferenceObject**: Type, refObjectId, version, URI, shortDescription for entity references

### Exception Classes
- **TidasException**: Base exception class for all SDK-specific errors
- **ValidationError**: Raised in strict mode when entity data violates schema constraints, includes field path and constraint details
- **ValidationWarning**: Warning object (not exception) created in weak mode for schema violations, same structure as ValidationError
- **JSONDecodeError**: Standard Python exception for malformed JSON (imported from json module)

## Dependencies & Assumptions

### Development Dependencies
- tidas-tools repository cloned alongside tidas-sdk repository (side-by-side directory structure) for code generation
- uv package manager for dependency management and build tooling
- Python 3.10+ for development (SDK supports Python 3.8+ for end users)

### Runtime Dependencies (End Users)
- Python 3.8+ runtime environment
- Pydantic library (v2.x) for validation and data classes
- loguru library for logging and observability
- typing_extensions for backporting newer type hint features to Python 3.8

### Assumptions
- TypeScript SDK implementation is stable and represents target API design
- TIDAS JSON schemas in tidas-tools are complete and valid
- Developers have tidas-tools and tidas-sdk repositories cloned in same parent directory for code generation workflow
- Developers use uv for local development (dependency installation, running scripts, building packages)
- End users do not need tidas-tools repository or uv (generated code included in PyPI package)
- End users can install via pip or uv (both work with PyPI packages)
- Users have basic Python knowledge (functions, classes, imports)
- Users understand LCA concepts (flows, processes, exchanges) at introductory level
- Development happens on Unix-like environment (Linux/macOS) with Python 3.10+

## Open Questions

None. Specification is complete based on TypeScript SDK reference implementation.

## Risks & Mitigations

### Risk: Schema Changes Breaking Generated Code
**Impact**: High - invalid generated code blocks all SDK functionality
**Mitigation**: Automated test suite validates generated code after each schema update; CI fails if generation produces invalid Python

### Risk: Pydantic Version Compatibility Issues
**Impact**: Medium - different Pydantic versions may have breaking API changes
**Mitigation**: Pin Pydantic to stable major version (v2.x); test against multiple Pydantic minor versions in CI

### Risk: Performance Gap vs TypeScript SDK
**Impact**: Medium - Python inherently slower may disappoint users expecting TypeScript-level performance
**Mitigation**: Document expected performance characteristics; optimize hot paths (batch operations, JSON serialization); provide validation-ignore mode for performance-critical code

### Risk: Documentation Drift from TypeScript SDK
**Impact**: Low - inconsistent documentation confuses users working with both SDKs
**Mitigation**: Maintain shared conceptual documentation in tidas-tools; generate SDK-specific docs from shared source; include API comparison table in docs

## Future Enhancements

The following features are explicitly excluded from this specification but may be added in future versions:

- AI-powered data improvement using TIDAS methodology rules (TypeScript SDK feature)
- Database integration (direct load/save to PostgreSQL, MongoDB, etc.)
- XML serialization/deserialization for ILCD XML format
- Schema migration tools for upgrading old TIDAS data to new schema versions
- Visual entity relationship diagram generation
- Integration with popular LCA software (openLCA, Brightway, etc.)
- Async API for I/O operations
- NumPy/Pandas integration for bulk data analysis
- Command-line tools for common operations

---

**Specification Version**: 1.0
**Last Updated**: 2025-10-31
