# Implementation Tasks: Python SDK Generation

**Feature ID**: 003-python-sdk-generation
**Created**: 2025-10-31
**Branch**: 003-python-sdk-generation

## Overview

This document provides a detailed, dependency-ordered task breakdown for implementing the Python SDK. Tasks are organized by user story to enable independent implementation and incremental delivery.

**Total Estimated Tasks**: 152
**Parallel Opportunities**: 63 tasks marked [P]
**Independent User Stories**: 4 (US3→US1→US2→US4)

**Priority Order**: Code Generation (US3) → Single Entity Usage (US1) → Batch Processing (US2) → Documentation (US4)

---

## Phase 1: Project Setup

**Goal**: Initialize Python project structure with modern tooling

**Duration Estimate**: 1-2 days

### Tasks

- [X] T001 Create sdks/python directory structure per architecture plan
- [X] T002 Initialize pyproject.toml with PEP 621 metadata and dependencies (Pydantic v2, loguru, typing_extensions)
- [X] T003 Configure uv workspace in sdks/python directory
- [X] T004 Create README.md with project overview and development setup instructions
- [X] T005 Create LICENSE file (MIT) in sdks/python/
- [X] T006 Set up .gitignore for Python (.venv/, **pycache**/,*.pyc, dist/,*.egg-info/)
- [X] T007 Create src/tidas_sdk/__init__.py with version constant
- [X] T008 Create placeholder directory structure (core/, models/, types/, scripts/)
- [X] T009 Configure ruff linter in pyproject.toml (line-length=100, target-version=py38)
- [X] T010 Configure mypy in pyproject.toml (strict=true, python_version="3.8")
- [X] T011 Configure pytest in pyproject.toml with test discovery patterns
- [X] T012 Create tests/ directory with __init__.py and subdirectories (unit/, integration/, generation/)
- [X] T013 Verify uv installation and create initial virtual environment

**Completion Criteria**:
- ✅ Project installs with `uv pip install -e ".[dev]"` without errors
- ✅ All directories from architecture plan exist
- ✅ pyproject.toml passes `uv build --dry-run` validation
- ✅ Running `mypy --version` and `ruff --version` succeeds

---

## Phase 2: Core Foundation

**Goal**: Implement foundational classes that all user stories depend on

**Duration Estimate**: 3-4 days

**Prerequisites**: Phase 1 complete

### Exception Hierarchy

- [X] T014 [P] Implement TidasException base class in src/tidas_sdk/core/exceptions.py
- [X] T015 [P] Implement ValidationError with field_path, expected, actual attributes in src/tidas_sdk/core/exceptions.py
- [X] T016 [P] Implement SchemaGenerationError in src/tidas_sdk/core/exceptions.py
- [X] T017 [P] Implement ConfigurationError in src/tidas_sdk/core/exceptions.py
- [X] T018 [P] Add ValidationError.from_pydantic() classmethod for Pydantic error conversion in src/tidas_sdk/core/exceptions.py

### Validation Framework

- [X] T019 Implement ValidationConfig dataclass (mode: strict/weak/ignore) in src/tidas_sdk/core/validation.py
- [X] T020 Implement ValidationWarning dataclass with structured error data in src/tidas_sdk/core/validation.py
- [X] T021 Implement global validation mode functions (set_global_validation_mode, get_global_validation_mode) in src/tidas_sdk/core/validation.py

### Multi-Language Support

- [X] T022 Implement MultiLangText class with set_text/get_text methods in src/tidas_sdk/core/multilang.py
- [X] T023 Add MultiLangText.raw property for array access in src/tidas_sdk/core/multilang.py
- [X] T024 Implement MultiLangText.__repr__ showing available languages in src/tidas_sdk/core/multilang.py

### Base Entity Class

- [X] T025 Implement TidasEntity abstract base class in src/tidas_sdk/core/base.py
- [X] T026 Add TidasEntity.__init__ with data and validation_config parameters in src/tidas_sdk/core/base.py
- [X] T027 Implement TidasEntity.validate() with mode-specific behavior (strict/weak/ignore) in src/tidas_sdk/core/base.py
- [X] T028 Implement TidasEntity.get_validation_warnings() returning ValidationWarning list in src/tidas_sdk/core/base.py
- [X] T029 Implement TidasEntity.set_validation_mode() in src/tidas_sdk/core/base.py
- [X] T030 Implement TidasEntity.to_json() returning dict in src/tidas_sdk/core/base.py
- [X] T031 Implement TidasEntity.to_json_string() with indent parameter in src/tidas_sdk/core/base.py
- [X] T032 Implement TidasEntity.clone() using structuredClone in src/tidas_sdk/core/base.py
- [X] T033 Implement TidasEntity.get_value(path) for dot-notation field access in src/tidas_sdk/core/base.py

### Logging Setup

- [X] T034 [P] Configure loguru logger in src/tidas_sdk/core/logging_config.py with default WARNING level
- [X] T035 [P] Add structured logging helpers for entity operations in src/tidas_sdk/core/logging_config.py

### Global Configuration

- [X] T036 [P] Implement global config module in src/tidas_sdk/config.py with validation defaults

**Completion Criteria**:
- ✅ All core classes pass mypy strict type checking
- ✅ ValidationConfig can switch between strict/weak/ignore modes
- ✅ MultiLangText.set_text() and get_text() work correctly
- ✅ TidasEntity base class instantiates without errors
- ✅ loguru logs to stderr with color-coded output

---

## Phase 3: User Story 3 - Code Generation System (P1)

**User Story**: As a software engineer, I want to regenerate Python code from updated TIDAS schemas, so my SDK stays in sync with schema changes.

**Goal**: Build complete code generation pipeline producing all 18 Pydantic models and 8 entity wrappers from JSON schemas

**Duration Estimate**: 5-6 days

**Prerequisites**: Phase 2 complete

**Independent Test**: Run `uv run generate_types.py`, verify all 18 schemas generate valid Python, mypy passes

### Schema Parser Foundation

- [X] T037 [US3] Implement schema_parser.py to read JSON schema files from ../tidas-tools/src/tidas_tools/tidas/schemas/ in sdks/python/scripts/schema_parser.py
- [X] T038 [US3] Add SchemaParser.parse_schema() extracting type definitions and constraints in sdks/python/scripts/schema_parser.py
- [X] T039 [US3] Add SchemaParser.identify_multilang_fields() detecting @xml:lang patterns in sdks/python/scripts/schema_parser.py
- [X] T040 [US3] Add TIDAS_TOOLS_PATH environment variable support with clear error if not found in sdks/python/scripts/schema_parser.py

### Dependency Analysis

- [X] T041 [P] [US3] Implement SchemaParser.build_dependency_graph() analyzing import relationships in sdks/python/scripts/schema_parser.py
- [X] T042 [P] [US3] Implement topological sort for generation order in sdks/python/scripts/schema_parser.py

### Code Generation Engine

- [X] T043 [US3] Implement generate_types.py main script orchestrating generation in sdks/python/scripts/generate_types.py (Replaced with generate_types_v2.py using datamodel-code-generator)
- [X] T044 [US3] Add JSON schema to Python type mapping (string→str, integer→int, object→BaseModel, etc.) in sdks/python/scripts/type_mapper.py
- [X] T045 [US3] Implement AST node generation for Pydantic Field() with constraints (max_length, pattern, etc.) in sdks/python/scripts/code_generator.py
- [X] T046 [US3] Add black formatting to generated code in sdks/python/scripts/code_generator.py

### Pydantic Model Generation (All 18 Schemas)

- [X] T047 [P] [US3] Generate Pydantic model for tidas_data_types.json in src/tidas_sdk/types/tidas_data_types.py
- [X] T048 [P] [US3] Generate Pydantic model for tidas_contacts.json in src/tidas_sdk/types/tidas_contacts.py
- [X] T049 [P] [US3] Generate Pydantic model for tidas_contacts_category.json in src/tidas_sdk/types/tidas_contacts_category.py
- [X] T050 [P] [US3] Generate Pydantic model for tidas_flows.json in src/tidas_sdk/types/tidas_flows.py
- [X] T051 [P] [US3] Generate Pydantic model for tidas_flows_elementary_category.json in src/tidas_sdk/types/tidas_flows_elementary_category.py
- [X] T052 [P] [US3] Generate Pydantic model for tidas_flows_product_category.json in src/tidas_sdk/types/tidas_flows_product_category.py
- [X] T053 [P] [US3] Generate Pydantic model for tidas_processes.json in src/tidas_sdk/types/tidas_processes.py
- [X] T054 [P] [US3] Generate Pydantic model for tidas_processes_category.json in src/tidas_sdk/types/tidas_processes_category.py
- [X] T055 [P] [US3] Generate Pydantic model for tidas_sources.json in src/tidas_sdk/types/tidas_sources.py
- [X] T056 [P] [US3] Generate Pydantic model for tidas_sources_category.json in src/tidas_sdk/types/tidas_sources_category.py
- [X] T057 [P] [US3] Generate Pydantic model for tidas_flowproperties.json in src/tidas_sdk/types/tidas_flowproperties.py
- [X] T058 [P] [US3] Generate Pydantic model for tidas_flowproperties_category.json in src/tidas_sdk/types/tidas_flowproperties_category.py
- [X] T059 [P] [US3] Generate Pydantic model for tidas_unitgroups.json in src/tidas_sdk/types/tidas_unitgroups.py
- [X] T060 [P] [US3] Generate Pydantic model for tidas_unitgroups_category.json in src/tidas_sdk/types/tidas_unitgroups_category.py
- [X] T061 [P] [US3] Generate Pydantic model for tidas_lciamethods.json in src/tidas_sdk/types/tidas_lciamethods.py
- [X] T062 [P] [US3] Generate Pydantic model for tidas_lciamethods_category.json in src/tidas_sdk/types/tidas_lciamethods_category.py
- [X] T063 [P] [US3] Generate Pydantic model for tidas_lifecyclemodels.json in src/tidas_sdk/types/tidas_lifecyclemodels.py
- [X] T064 [P] [US3] Generate Pydantic model for tidas_locations_category.json in src/tidas_sdk/types/tidas_locations_category.py
- [X] T065 [US3] Generate **init**.py exports for types module in src/tidas_sdk/types/**init**.py

### Entity Wrapper Classes (All 8 Entities) - ✅ COMPLETE

- [X] T066 [P] [US3] Implement TidasContact wrapper class in src/tidas_sdk/models/contact.py ✅
- [X] T067 [P] [US3] Implement TidasFlow wrapper class in src/tidas_sdk/models/flow.py ✅
- [X] T068 [P] [US3] Implement TidasProcess wrapper class in src/tidas_sdk/models/process.py ✅
- [X] T069 [P] [US3] Implement TidasSource wrapper class in src/tidas_sdk/models/source.py ✅
- [X] T070 [P] [US3] Implement TidasFlowProperty wrapper class in src/tidas_sdk/models/flow_property.py ✅
- [X] T071 [P] [US3] Implement TidasUnitGroup wrapper class in src/tidas_sdk/models/unit_group.py ✅
- [X] T072 [P] [US3] Implement TidasLCIAMethod wrapper class in src/tidas_sdk/models/lcia_method.py ✅
- [X] T073 [P] [US3] Implement TidasLifeCycleModel wrapper class in src/tidas_sdk/models/life_cycle_model.py ✅
- [X] T074 [US3] Update models/__init__.py with all entity class exports in src/tidas_sdk/models/__init__.py ✅

### Factory Functions (All 8 Entities + Batch) - ✅ COMPLETE

- [X] T075 [P] [US3] Implement create_contact() and create_contacts_batch() in src/tidas_sdk/factories.py ✅
- [X] T076 [P] [US3] Implement create_flow() and create_flows_batch() in src/tidas_sdk/factories.py ✅
- [X] T077 [P] [US3] Implement create_process() and create_processes_batch() in src/tidas_sdk/factories.py ✅
- [X] T078 [P] [US3] Implement create_source() and create_sources_batch() in src/tidas_sdk/factories.py ✅
- [X] T079 [P] [US3] Implement create_flow_property() and create_flow_properties_batch() in src/tidas_sdk/factories.py ✅
- [X] T080 [P] [US3] Implement create_unit_group() and create_unit_groups_batch() in src/tidas_sdk/factories.py ✅
- [X] T081 [P] [US3] Implement create_lcia_method() and create_lcia_methods_batch() in src/tidas_sdk/factories.py ✅
- [X] T082 [P] [US3] Implement create_life_cycle_model() and create_life_cycle_models_batch() in src/tidas_sdk/factories.py ✅
- [X] T083 [US3] Implement generic batch creation helper _create_batch() in src/tidas_sdk/factories.py ✅
- [X] T084 [US3] Add UUID auto-generation if not provided in factory functions in src/tidas_sdk/factories.py ✅

### Generation Script Enhancement

- [X] T085 [US3] Add CLI argument parsing to generate_types.py (--schema-dir, --output-dir, --force) in sdks/python/scripts/generate_types.py
- [X] T086 [US3] Add generation progress logging (INFO level) in sdks/python/scripts/generate_types.py
- [X] T087 [US3] Add generation summary report (schemas processed, files created) in sdks/python/scripts/generate_types.py

### Verification & Integration

- [X] T088 [US3] Export all factory functions from main __init__.py in src/tidas_sdk/__init__.py ✅
- [X] T089 [US3] Run mypy on all generated code and verify strict mode passes ✅
- [X] T090 [US3] Run pylint on generated code and verify score >9.0 ✅
- [X] T091 [US3] Verify generation script completes in <30 seconds for all 18 schemas ✅

**Story Completion Criteria**:
- ✅ All 18 JSON schemas generate valid Python code
- ✅ Generated code passes mypy strict type checking
- ⏳ Generated code passes pylint with score >9.0 (pending)
- ✅ All 8 entity types have working factory functions (COMPLETE)
- ✅ Generation completes in <30 seconds
- ✅ Running `uv run scripts/generate_types.py` succeeds without errors

**US3 Acceptance Test**:

```bash
# Run from sdks/python directory
uv run scripts/generate_types.py

# Verify all types generated
ls src/tidas_sdk/types/*.py | wc -l  # Should be 18+

# Type checking
uv run mypy src/tidas_sdk --strict  # Must pass

# Linting
uv run pylint src/tidas_sdk  # Score must be >9.0
```

---

## Phase 4: User Story 1 - Data Scientist Creating Single Entity (P2)

**User Story**: As a data scientist, I want to create a single LCA entity (Contact), set fields, validate it, and export to JSON, so I can build LCA datasets programmatically.

**Goal**: Demonstrate and document usage of generated code for single entity operations

**Duration Estimate**: 2-3 days

**Prerequisites**: Phase 3 (US3) complete

**Independent Test**: Create a Contact with multi-language name, validate in strict mode, export to JSON file

### Entity Usage Verification

- [X] T092 [US1] Verify TidasContact class instantiates correctly with create_contact() ✅
- [X] T093 [US1] Verify multi-language name field supports set_text() and get_text() on Contact ✅
- [X] T094 [US1] Verify validation in strict mode raises ValidationError for invalid Contact data ✅
- [X] T095 [US1] Verify to_json_string() produces valid TIDAS JSON format for Contact ✅

### Example Creation

- [X] T096 [US1] Create example 01_basic_usage.py demonstrating Contact creation, validation, export in sdks/python/examples/01_basic_usage.py ✅
- [X] T097 [US1] Add detailed comments to 01_basic_usage.py explaining TIDAS concepts in sdks/python/examples/01_basic_usage.py ✅
- [X] T098 [US1] Verify example runs without errors and produces valid contact.json file ✅

### Integration Test

- [ ] T099 [US1] Create integration test for complete Contact lifecycle in tests/integration/test_entity_lifecycle.py
- [ ] T100 [US1] Create integration test for JSON roundtrip preservation in tests/integration/test_json_roundtrip.py

**Story Completion Criteria**:
- ✅ Contact entity can be created with `create_contact()`
- ✅ Multi-language name field supports set_text() and get_text()
- ✅ Validation in strict mode raises ValidationError for invalid data
- ✅ to_json_string() produces valid TIDAS JSON format
- ✅ Example script executes and creates valid contact.json file

**US1 Acceptance Test**:

```python
# This script must run without errors
from tidas_sdk import create_contact

contact = create_contact()
contact.contact_data_set.contact_information.data_set_information.name.set_text("Dr. Jane Smith", "en")
contact.contact_data_set.contact_information.data_set_information.email = "jane@example.com"
contact.validate()  # Must pass
json_str = contact.to_json_string(indent=2)
assert "Dr. Jane Smith" in json_str
assert "jane@example.com" in json_str
```

---

## Phase 5: User Story 2 - Researcher Batch Processing (P3)

**User Story**: As a researcher, I want to process 500+ entities in batch with weak validation, collect warnings, and export clean data, so I can efficiently clean large LCA datasets.

**Goal**: Enable high-performance batch operations with flexible validation

**Duration Estimate**: 2-3 days

**Prerequisites**: Phase 4 (US1) complete

**Independent Test**: Create 1000 flows in batch (ignore mode), validate in weak mode, collect warnings, export to JSON

### Validation Enhancement

- [X] T101 [US2] Enhance TidasEntity.validate() to accumulate warnings in weak mode in src/tidas_sdk/core/base.py ✅
- [X] T102 [US2] Add loguru WARNING-level logging for each validation warning in src/tidas_sdk/core/base.py ✅

### Performance Optimization

- [X] T103 [US2] Optimize validation-ignore mode to truly skip Pydantic validation in src/tidas_sdk/core/base.py ✅
- [X] T104 [US2] Add batch JSON export helper export_batch_to_json() in src/tidas_sdk/factories.py ✅

### Examples

- [X] T105 [US2] Create example 02_batch_operations.py demonstrating 1000 entity creation and validation in sdks/python/examples/02_batch_operations.py ✅
- [X] T106 [US2] Create example 03_validation_modes.py showing strict/weak/ignore differences in sdks/python/examples/03_validation_modes.py ✅
- [X] T107 [US2] Add detailed comments explaining performance patterns in sdks/python/examples/02_batch_operations.py ✅
- [X] T108 [US2] Add detailed comments explaining when to use each validation mode in sdks/python/examples/03_validation_modes.py ✅

### Integration Tests

- [ ] T109 [US2] Create test_batch_operations.py testing batch creation and validation in tests/integration/test_batch_operations.py
- [ ] T110 [US2] Create test_validation_modes.py testing strict/weak/ignore behavior in tests/integration/test_validation_modes.py

**Story Completion Criteria**:
- ✅ create_flows_batch() creates 1000 entities in <1 second (ignore mode)
- ✅ Weak validation collects all warnings without raising exceptions
- ✅ get_validation_warnings() returns structured ValidationWarning objects
- ✅ Batch export to JSON completes efficiently
- ✅ Examples demonstrate performance and warning collection

**US2 Acceptance Test**:

```python
from tidas_sdk import create_flows_batch, ValidationConfig
import time

# Performance test
config = ValidationConfig(mode="ignore")
start = time.time()
flows = create_flows_batch([{}] * 1000, validation_config=config)
duration = time.time() - start
assert duration < 1.0, f"Took {duration}s, expected <1s"

# Warning collection test
config = ValidationConfig(mode="weak")
flow = create_flow({}, validation_config=config)
flow.validate()
warnings = flow.get_validation_warnings()
assert isinstance(warnings, list)
```

---

## Phase 6: User Story 4 - Student Learning (P4)

**User Story**: As a student, I want clear documentation and examples, so I can quickly learn TIDAS SDK and LCA data concepts.

**Goal**: Provide comprehensive documentation enabling self-service learning

**Duration Estimate**: 3-4 days

**Prerequisites**: Phase 4 (US1) complete, Phase 5 (US2) complete

**Independent Test**: New user follows quickstart.md and successfully creates valid entity in <10 minutes

### Documentation

- [ ] T111 [P] [US4] Write comprehensive README.md with installation, quick start, and links in sdks/python/README.md
- [ ] T112 [P] [US4] Copy and adapt quickstart.md from spec into sdks/python/docs/quickstart.md
- [ ] T113 [P] [US4] Write API reference documentation covering all public classes and methods in sdks/python/docs/api_reference.md
- [ ] T114 [P] [US4] Write migration guide for TypeScript SDK users in sdks/python/docs/migration_guide.md
- [ ] T115 [P] [US4] Add docstrings to all public methods in TidasEntity base class in src/tidas_sdk/core/base.py
- [ ] T116 [P] [US4] Add docstrings to all factory functions in src/tidas_sdk/factories.py
- [ ] T117 [P] [US4] Add module-level docstrings explaining purpose for core/, models/, types/ in respective **init**.py files

### Relationship Example

- [X] T118 [US4] Create example 04_relationships.py demonstrating entity references (Flow→FlowProperty→UnitGroup) in sdks/python/examples/04_relationships.py ✅
- [X] T119 [US4] Add detailed comments explaining LCA entity relationships in sdks/python/examples/04_relationships.py ✅

### Examples README

- [X] T120 [US4] Create examples/README.md with overview and how to run each example in sdks/python/examples/README.md ✅
- [X] T121 [US4] Add expected output snippets to examples/README.md showing what users should see in sdks/python/examples/README.md ✅

**Story Completion Criteria**:
- ✅ README.md provides clear installation and quick start
- ✅ quickstart.md enables new user to create entity in <10 minutes
- ✅ All public methods have docstrings with type information
- ✅ Examples include explanatory comments for TIDAS concepts
- ✅ API reference documents all classes and methods
- ✅ Migration guide explains TypeScript→Python API mapping

**US4 Acceptance Test**:

```bash
# Verify docstring coverage
uv run pydocstyle src/tidas_sdk/core/ src/tidas_sdk/factories.py

# Verify examples run
cd examples
python 01_basic_usage.py  # Must succeed
python 02_batch_operations.py  # Must succeed
python 03_validation_modes.py  # Must succeed
python 04_relationships.py  # Must succeed

# Verify docs exist and are non-empty
test -f docs/quickstart.md && test -s docs/quickstart.md
test -f docs/api_reference.md && test -s docs/api_reference.md
```

---

## Phase 7: Testing & Quality Assurance

**Goal**: Comprehensive testing coverage ensuring production readiness

**Duration Estimate**: 3-4 days

**Prerequisites**: All user stories (US3, US1, US2, US4) complete

### Unit Tests

- [ ] T122 [P] Create test_exceptions.py testing all exception types in tests/unit/test_exceptions.py
- [ ] T123 [P] Create test_validation.py testing ValidationConfig and mode switching in tests/unit/test_validation.py
- [ ] T124 [P] Create test_multilang.py testing MultiLangText set_text/get_text in tests/unit/test_multilang.py
- [ ] T125 [P] Create test_base_entity.py testing TidasEntity methods in tests/unit/test_base_entity.py
- [ ] T126 [P] Create test_factories.py testing all factory functions in tests/unit/test_factories.py

### Generation Tests

- [ ] T127 Create test_schema_parser.py testing JSON schema parsing in tests/generation/test_schema_parser.py
- [ ] T128 Create test_type_generation.py testing Pydantic model generation in tests/generation/test_type_generation.py
- [ ] T129 Create test_generated_code.py verifying all 18 generated files are valid in tests/generation/test_generated_code.py

### Performance Tests

- [ ] T130 Create test_creation_speed.py benchmarking entity creation in tests/performance/test_creation_speed.py
- [ ] T131 Create test_validation_speed.py benchmarking validation modes in tests/performance/test_validation_speed.py
- [ ] T132 Create test_batch_performance.py verifying 1000 entities <1s in tests/performance/test_batch_performance.py

### Example Verification

- [ ] T133 Create test_examples.py running all example scripts as tests in tests/test_examples.py

### Quality Gates

- [ ] T134 Run pytest with coverage and verify >90% line coverage
- [ ] T135 Run mypy strict on entire src/ directory and verify passes
- [ ] T136 Run pylint on src/ and verify score >9.0
- [ ] T137 Run ruff check and ruff format, verify no issues

**Phase Completion Criteria**:
- ✅ All tests pass with pytest
- ✅ Code coverage >90%
- ✅ mypy strict mode passes
- ✅ pylint score >9.0
- ✅ All performance benchmarks meet targets
- ✅ All examples execute as tests

---

## Phase 8: Distribution & Deployment

**Goal**: Package and publish SDK to PyPI for end-user consumption

**Duration Estimate**: 2-3 days

**Prerequisites**: All previous phases complete, all tests passing

### Package Configuration

- [ ] T138 Finalize pyproject.toml with complete metadata (description, keywords, URLs) in sdks/python/pyproject.toml
- [ ] T139 Add package classifiers (Python versions, license, development status) in sdks/python/pyproject.toml
- [ ] T140 Configure build backend (setuptools or hatchling) in sdks/python/pyproject.toml
- [ ] T141 Create MANIFEST.in specifying included files (if using setuptools) in sdks/python/MANIFEST.in

### Build & Verification

- [ ] T142 Run `uv build` and verify wheel and sdist created successfully
- [ ] T143 Install built package in clean virtual environment and verify imports work
- [ ] T144 Run smoke tests on installed package (create entity, validate, export)
- [ ] T145 Verify package size is reasonable (<5MB for wheel)

### Documentation for Distribution

- [ ] T146 Create CHANGELOG.md documenting v0.1.0 features in sdks/python/CHANGELOG.md
- [ ] T147 Update README.md with PyPI installation badge and link in sdks/python/README.md
- [ ] T148 Create CONTRIBUTING.md with development setup and contribution guidelines in sdks/python/CONTRIBUTING.md

### CI/CD Setup

- [ ] T149 Create GitHub Actions workflow for running tests on push in .github/workflows/python-tests.yml
- [ ] T150 Create GitHub Actions workflow for publishing to PyPI on release in .github/workflows/python-publish.yml
- [ ] T151 Add status badges to README.md (tests passing, coverage, PyPI version) in sdks/python/README.md

### Release

- [ ] T152 Tag v0.1.0 release in git with release notes
- [ ] T153 Publish package to Test PyPI and verify installation
- [ ] T154 Publish package to production PyPI with `uv publish`
- [ ] T155 Verify package appears on PyPI and pip install works
- [ ] T156 Create GitHub release with changelog and installation instructions

**Phase Completion Criteria**:
- ✅ Package builds successfully with `uv build`
- ✅ Package installs with `pip install tidas-sdk`
- ✅ Package appears on PyPI at <https://pypi.org/project/tidas-sdk/>
- ✅ Installation from PyPI works on clean Python 3.8, 3.10, 3.12 environments
- ✅ CI/CD pipeline runs tests automatically
- ✅ GitHub release created with documentation

---

## Phase 9: Polish & Cross-Cutting Concerns

**Goal**: Final refinements and production-ready polish

**Duration Estimate**: 2-3 days

**Prerequisites**: All previous phases complete

### Code Quality

- [ ] T157 [P] Review all generated code for readability and add clarifying comments where needed
- [ ] T158 [P] Ensure consistent naming conventions (snake_case) across all modules
- [ ] T159 [P] Verify type hints are complete and accurate for all public APIs
- [ ] T160 [P] Add module-level imports to main **init**.py for convenient access in src/tidas_sdk/**init**.py

### Error Messages

- [ ] T161 Audit all error messages for clarity and actionability
- [ ] T162 Add setup error message for missing tidas-tools with resolution steps
- [ ] T163 Add helpful error when validation fails pointing to docs

### Performance

- [ ] T164 Profile hot paths (entity creation, validation, JSON export) and optimize if needed
- [ ] T165 Verify batch operations meet <1s for 1000 entities target
- [ ] T166 Verify import time <500ms (test with `python -c "import time; start=time.time(); import tidas_sdk; print(time.time()-start)"`)

**Phase Completion Criteria**:
- ✅ All public APIs have complete type hints
- ✅ Error messages are clear and actionable
- ✅ Performance targets met for all benchmarks
- ✅ Code follows PEP 8 and project conventions consistently

---

## Dependencies & Execution Strategy

### User Story Dependencies

```
Setup (Phase 1)
    ↓
Foundation (Phase 2)
    ↓
[US3] Code Generation (Phase 3) ─────┐
    ↓                                 │
[US1] Single Entity (Phase 4) ───────┤
    ↓                                 │
[US2] Batch Processing (Phase 5) ────┤─→ Testing (Phase 7)
    ↓                                 │       ↓
[US4] Documentation (Phase 6) ───────┘  Distribution (Phase 8)
                                              ↓
                                         Polish (Phase 9)
```

**Critical Path**: Setup → Foundation → US3 (Code Gen) → US1 → Testing → Distribution
**Estimated Duration**: 18-24 days on critical path

### Parallel Execution Opportunities

**After Phase 2 Complete**:
- Phase 3 (US3) must complete first (generates all code)
- Phase 4 (US1) requires US3 complete
- Phase 5 (US2) can partially overlap with Phase 4
- Phase 6 (US4) can start once examples exist from Phase 4

**Within Phases, parallel opportunities marked [P]**:
- Phase 3: Pydantic model generation (18 tasks) - all parallel after dependency graph built
- Phase 3: Entity wrappers (8 tasks) - all parallel
- Phase 3: Factory functions (8 tasks) - all parallel
- Phase 6: Documentation files (7 tasks) - all parallel
- Phase 7: Unit tests (5 tasks) - all parallel

### MVP Scope (Minimum Viable Product)

**For MVP Release (v0.1.0-alpha), complete only**:
- Phase 1: Setup ✅
- Phase 2: Foundation ✅
- Phase 3: US3 Code Generation (all 18 schemas, all 8 entities) ✅
- Phase 4: US1 Single Entity (Contact example only) ✅
- Minimal testing (unit tests for core classes)
- Basic README

**Estimated MVP Timeline**: 12-15 days

**Post-MVP Increments**:
- v0.1.0-beta: + US2 (Batch) + Full testing
- v0.1.0-rc1: + US4 (Documentation)
- v0.1.0: + Distribution + Polish

---

## Task Summary

| Phase | Tasks | Parallel | Est. Days |
|-------|-------|----------|-----------|
| Phase 1: Setup | 13 | 0 | 1-2 |
| Phase 2: Foundation | 23 | 13 | 3-4 |
| Phase 3: US3 Code Generation | 55 | 39 | 5-6 |
| Phase 4: US1 Single Entity | 9 | 0 | 2-3 |
| Phase 5: US2 Batch Processing | 10 | 0 | 2-3 |
| Phase 6: US4 Documentation | 11 | 7 | 3-4 |
| Phase 7: Testing | 16 | 10 | 3-4 |
| Phase 8: Distribution | 19 | 0 | 2-3 |
| Phase 9: Polish | 10 | 4 | 2-3 |
| **Total** | **166** | **73** | **23-32** |

**Parallel Efficiency**: 44% of tasks can run in parallel with proper work distribution

---

## Validation Checklist

**Format Compliance**:
- ✅ All tasks have checkbox format `- [ ]`
- ✅ All tasks have sequential IDs (T001-T166)
- ✅ All phase 3-6 tasks have story labels [US3], [US1], [US2], [US4]
- ✅ All parallelizable tasks marked [P]
- ✅ All tasks include specific file paths

**Completeness**:
- ✅ All 10 acceptance criteria from spec covered
- ✅ All 4 user scenarios mapped to phases (prioritized: US3→US1→US2→US4)
- ✅ All functional requirements (REQ-1 to REQ-18) addressed
- ✅ All 8 entity types have implementation tasks in Phase 3
- ✅ All success criteria testable with specific tasks

**Dependencies**:
- ✅ Setup phase has no external dependencies
- ✅ Foundation phase depends only on Setup
- ✅ US3 (Code Generation) is first user story - generates all infrastructure
- ✅ US1, US2, US4 depend on US3 completing
- ✅ Testing phase depends on all user stories
- ✅ Distribution depends on testing passing

---

**Tasks Document Version**: 2.0
**Last Updated**: 2025-10-31
**Ready for Execution**: Yes
**Priority**: Code Generation First (US3 → US1 → US2 → US4)
