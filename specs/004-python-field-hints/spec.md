# Feature Specification: Python SDK Field Hints and Code Completion

**Feature Branch**: `004-python-field-hints`
**Created**: 2025-11-03
**Status**: Draft
**Input**: User description: "相比于typescript sdk，生成的python sdk的内容缺失了一个重要特性: 创建的对象没有字段的代码提示，需要增加这个特性，考虑如何修改factories.py或者TidasEntity的实现"

## Overview

The Python SDK currently lacks IDE code completion and field hints when developers access nested fields on entity objects, unlike the TypeScript SDK which provides full IntelliSense support. This creates a poor developer experience where users must reference documentation or JSON schema files to discover available fields, significantly slowing down development and increasing the likelihood of errors.

This feature will enhance the Python SDK to provide full IDE code completion support for entity fields, making it as intuitive to use as the TypeScript SDK.

## User Scenarios & Testing

### User Story 1 - IDE Code Completion for Entity Fields (Priority: P1)

As a Python developer using the TIDAS SDK, I want IDE code completion when accessing entity fields so that I can discover available fields without consulting documentation and avoid typos when accessing nested properties.

**Why this priority**: This is the core value proposition. Without code completion, Python developers have a significantly worse experience compared to TypeScript developers, which may discourage SDK adoption. This directly impacts developer productivity and error rates.

**Independent Test**: Create a Contact entity, type `contact.` in an IDE (PyCharm, VS Code), and verify that IDE shows all available top-level fields with type information.

**Acceptance Scenarios**:

1. **Given** a developer has created a Contact entity, **When** they type `contact.` in their IDE, **Then** the IDE displays all available fields (contactDataSet, etc.) with autocomplete suggestions
2. **Given** a developer accesses nested fields like `contact.contactDataSet.`, **When** they type the dot, **Then** the IDE displays available nested fields (contactInformation, administrativeInformation, etc.)
3. **Given** a developer accesses deep nested fields, **When** they type `contact.contactDataSet.contactInformation.`, **Then** the IDE displays the next level of fields with correct types
4. **Given** a developer hovers over a field name, **When** the IDE tooltip appears, **Then** it shows the field's type information and optional documentation

---

### User Story 2 - Type-Safe Field Access (Priority: P2)

As a Python developer, I want my IDE to warn me when I access non-existent fields so that I catch errors at development time rather than runtime.

**Why this priority**: While code completion is valuable, type safety adds an additional layer of protection against errors. This is especially important for large codebases where manual testing may miss edge cases.

**Independent Test**: Type `contact.invalidField` in an IDE with type checking enabled (mypy, Pylance), and verify that the IDE shows a type error warning.

**Acceptance Scenarios**:

1. **Given** a developer accesses a non-existent field, **When** running type checking, **Then** the type checker reports an error indicating the field doesn't exist
2. **Given** a developer assigns a value of wrong type to a field, **When** type checking runs, **Then** an error is reported about type mismatch
3. **Given** a developer uses auto-complete to select a field, **When** they complete the selection, **Then** the resulting code passes type checking

---

### User Story 3 - Multi-Language Field Support (Priority: P3)

As a developer working with multi-language text fields, I want code completion for the `set_text()` and `get_text()` methods so that I can easily work with localized content.

**Why this priority**: Multi-language fields are a key feature of TIDAS/ILCD, but less critical than basic field access. Most developers will master this after learning basic entity manipulation.

**Independent Test**: Access a multi-language name field, type `.`, and verify IDE suggests both `set_text()` and `get_text()` methods with parameter hints.

**Acceptance Scenarios**:

1. **Given** a developer accesses a multi-language field like `contact.contactDataSet.contactInformation.dataSetInformation.name`, **When** they type `.`, **Then** IDE suggests `set_text()` and `get_text()` methods
2. **Given** a developer starts typing `set_text(`, **When** the parameter hint appears, **Then** it shows the expected parameters (value: str, lang: str)

---

### Edge Cases

- What happens when a user accesses an optional field that doesn't exist in the data? (IDE should still show the field as available but typed as Optional)
- How does code completion work for fields that are lists or dictionaries? (Should show appropriate list/dict methods)
- What happens with dynamically added fields that aren't in the schema? (Type system should allow dict-like access as fallback)
- How do we handle fields with special characters like `common:UUID`? (Should still be accessible via attribute or dict syntax)

## Requirements

### Functional Requirements

- **FR-001**: Entity objects MUST provide IDE code completion for all schema-defined fields
- **FR-002**: Entity objects MUST provide type hints that enable IDE type checking
- **FR-003**: Code completion MUST work for nested fields at any depth level
- **FR-004**: Multi-language text fields MUST expose `set_text()` and `get_text()` methods with type hints
- **FR-005**: Type hints MUST be compatible with Python 3.8+ type system
- **FR-006**: Code completion MUST work in major Python IDEs (VS Code with Pylance, PyCharm, vim with LSP)
- **FR-007**: Type checking with mypy MUST pass in strict mode for valid field access
- **FR-008**: Invalid field access MUST trigger type checker warnings
- **FR-009**: Factory functions MUST return properly typed entity objects
- **FR-010**: Generated entity classes MUST preserve backwards compatibility with existing code
- **FR-011**: Performance of entity instantiation MUST NOT degrade by more than 5% compared to current implementation
- **FR-012**: Type stubs (.pyi files) MUST be generated if needed for external type checkers

### Key Entities

- **TidasEntity**: Base class that will be enhanced with property descriptors or attribute access patterns to enable code completion while maintaining dictionary-like access
- **Generated Entity Classes**: (TidasContact, TidasFlow, etc.) Will expose typed properties for each schema field
- **MultiLangText**: Wrapper class that needs proper method signatures for `set_text()` and `get_text()`
- **Factory Functions**: Return types must be properly annotated to enable downstream type checking

## Success Criteria

### Measurable Outcomes

- **SC-001**: Developers can discover 100% of entity fields through IDE autocomplete without consulting documentation
- **SC-002**: Type checking with mypy in strict mode passes for all example code in the repository
- **SC-003**: IDE (VS Code with Pylance) provides autocomplete suggestions within 500ms of typing a dot after an entity object
- **SC-004**: Invalid field access is detected by type checkers before runtime in 95%+ of cases
- **SC-005**: Code completion works correctly for nested fields at least 5 levels deep
- **SC-006**: Developer productivity improves: time to write correct field access code reduces by 60% compared to current dict-based approach
- **SC-007**: Runtime errors due to field name typos reduce by 80% in user code
- **SC-008**: Python SDK field access experience is rated equivalent to TypeScript SDK by 90% of developers who use both

### User Experience Metrics

- Developers can write field access code without switching to documentation
- IDE tooltips provide immediate feedback on field types
- Type errors are caught during development rather than at runtime
- Learning curve for new SDK users decreases due to discoverability

## Assumptions

- Developers are using modern Python IDEs that support type hints (VS Code, PyCharm, vim with LSP)
- Python 3.8+ is the target (to use TypedDict and other modern typing features)
- Type checking tools (mypy, Pylance) are configured correctly in developer environments
- The current dictionary-based access pattern can be enhanced without breaking existing code
- Generated Pydantic models can be leveraged for type information
- Performance impact of property descriptors or proxy objects is acceptable (< 5% overhead)

## Out of Scope

- Real-time validation during field access (validation remains explicit via `validate()` method)
- Dynamic schema changes at runtime (type hints are based on generated code)
- Field completion for custom/extended fields not in TIDAS schema
- IDE plugins or extensions (relying on standard Python type system)
- Migration tools for existing code (backwards compatibility maintained)
- Code completion in non-Python-aware editors (plain text editors, basic vim without LSP)

## Dependencies

- Existing Pydantic v2 models generated from JSON schemas
- Python typing module and typing_extensions for Python 3.8 compatibility
- IDE language servers (Pylance for VS Code, PyCharm's built-in type system)
- Current TidasEntity base class and factory function architecture

## Future Enhancements

- Generate comprehensive type stub (.pyi) files for better IDE support
- Provide runtime validation hints when accessing fields in strict mode
- Support for custom field extensions while maintaining type safety
- Integration with JSON schema documentation to show field descriptions in IDE tooltips
- Performance optimization using __slots__ for entity classes
- Support for typed field access in Jupyter notebooks with enhanced autocomplete

## References

- TypeScript SDK implementation: Compare field access patterns
- Pydantic v2 model access patterns: Understand existing type support
- Python typing best practices: PEP 484, 544, 589 (TypedDict)
- IDE language server protocols: How autocomplete and type checking work
