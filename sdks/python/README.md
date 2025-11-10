# TIDAS Python SDK

Python SDK for TIDAS (TianGong Life Cycle Assessment data format) providing type-safe data manipulation and validation.

## 🚧 Status

**Version**: 0.1.0 (Ready for Release)

This SDK is ready for release. For production use of TIDAS data utilities, you can also consider the [tidas-tools](https://pypi.org/project/tidas-tools/) package.

## 📋 Features

### Planned Features

- [x] Pydantic-based data models from JSON schemas
- [x] Type-safe data manipulation
- [x] TIDAS data validation
- [x] JSON to object conversion
- [x] Property access utilities
- [x] Factory functions for entity creation

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

### Builder Pattern for Complex Entities

TIDAS entities are often deeply nested and complex. The SDK provides automatically generated Builder classes for incremental construction:

```python
import uuid
from tidas_sdk.builders.tidas_contacts_builders import ContactDataSetBuilder

# Create builder
builder = ContactDataSetBuilder()

# Set fields incrementally
builder.contactInformation.dataSetInformation.common_UUID = str(uuid.uuid4())
builder.contactInformation.dataSetInformation.set_name("Dr. Jane Smith", "en")
builder.contactInformation.dataSetInformation.set_shortName("J. Smith", "en")
builder.contactInformation.dataSetInformation.email = "jane@example.com"

# Add multi-language support
builder.contactInformation.dataSetInformation.set_name("Dr. Jane Smith", "en")
builder.contactInformation.dataSetInformation.set_name("Dr. Jane Smith", "fr")

# Build final Pydantic model
contact = builder.build()
```

**Key Features:**
- ✅ Incremental field assignment
- ✅ Auto-initialization of nested builders
- ✅ Multi-language helper methods (`set_name()`, `get_name()`)
- ✅ Optional validation (validate on `build()`, not on assignment)
- ✅ Type-safe with full IDE autocomplete

See the [Builder Pattern Guide](docs/builder-pattern-guide.md) for comprehensive examples.

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

## 🚀 发布流程

### 准备工作

在发布前，确保您的Python SDK已经完成开发并通过所有测试：

```bash
cd sdks/python

# 安装依赖
uv sync

# 运行测试
uv run pytest

# 代码检查
uv run ruff check .
uv run mypy .
```

### 构建分发包

Python包使用`build`工具来构建分发包：

```bash
# 安装构建工具
uv add --dev build

# 构建分发包
uv run python -m build
```

这将在`dist/`目录下创建两个文件：

- 一个`.tar.gz`源码包
- 一个`.whl`二进制包

### 本地测试包

在发布前，建议先在本地测试包：

```bash
# 创建测试环境
python -m venv test_env
source test_env/bin/activate  # Linux/Mac
# 或 test_env\Scripts\activate  # Windows

# 安装本地构建的包
pip install dist/tidas_sdk-0.1.0-py3-none-any.whl

# 测试导入
python -c "import tidas_sdk; print(tidas_sdk.__version__)"
```

### 发布到PyPI

#### 准备PyPI账户

确保您有PyPI账户并已配置API令牌：

1. 在[PyPI](https://pypi.org/)注册账户
2. 在账户设置中生成API令牌
3. 配置认证（推荐使用`keyring`或环境变量）

#### 安装发布工具

```bash
# 安装twine（用于上传包）
uv add --dev twine
```

#### 上传到测试PyPI（推荐先测试）

```bash
# 上传到测试PyPI
uv run twine upload --repository testpypi dist/*

# 从测试PyPI安装测试
pip install --index-url https://test.pypi.org/simple/ tidas-sdk
```

#### 上传到正式PyPI

```bash
# 上传到正式PyPI
uv run twine upload dist/*
```

### 版本管理

在`pyproject.toml`中更新版本号：

```toml
[project]
name = "tidas-sdk"
version = "0.1.1"  # 根据语义化版本规则更新
```

### 自动化发布脚本

为了简化发布过程，可以使用项目中的发布脚本：

```bash
# 使用发布脚本
./scripts/release.sh
```

### CI/CD自动化发布

项目支持通过GitHub Actions自动发布流程。当创建带有版本标签（如`v0.1.1`）的提交时，会自动触发发布流程。

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

## 🔗 Related Packages

- [tidas-tools](https://pypi.org/project/tidas-tools/): Production-ready utilities for TIDAS data
- [@tiangong-lca/tidas-sdk](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk): TypeScript SDK

## 📋 Usage Examples

### Creating Entities

The SDK provides two approaches for creating entities:

1. **Wrapper Approach** (Original):

   ```python
   from tidas_sdk import create_process
   process = create_process()
   process.process_data_set.process_information.data_set_information.name.base_name.set_text("Electricity production", "en")
   process.validate()
   ```

2. **Pydantic Model Approach** (New):
   ```python
   from tidas_sdk import create_process_model
   process = create_process_model()
   # Access data directly through the Pydantic model
   process.process_data_set.process_information.data_set_information.name.base_name = "Electricity production"
   # Validation happens automatically on instantiation
   ```

### Converting Between Approaches

You can convert between wrapper and Pydantic models:

```python
# From wrapper to Pydantic
process_wrapper = create_process()
process_model = process_wrapper.to_pydantic()

# From Pydantic to wrapper
process_model = create_process_model()
process_wrapper = TidasProcesses(process_model.model_dump())
```

### Example Script

See [examples/06_pydantic_models.py](examples/06_pydantic_models.py) for a complete example demonstrating both approaches.

### Validation

Both approaches provide validation:

- **Wrapper Approach**: Call `.validate()` method on wrapper instances
- **Pydantic Model Approach**: Automatic validation on instantiation

### Serialization

Both approaches support JSON serialization:

- **Wrapper Approach**: Call `.model_dump_json()` method on wrapper instances
- **Pydantic Model Approach**: Call `.model_dump_json()` method on Pydantic model instances
