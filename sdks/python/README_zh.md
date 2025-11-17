# TIDAS Python SDK

用于 TIDAS（天工生命周期评估数据格式）的 Python SDK，提供类型安全的数据操作和验证。

## 🚧 状态

**版本**: 0.1.0（准备发布）

此 SDK 已准备好发布。如需在生产环境中使用 TIDAS 数据工具，您也可以考虑使用 [tidas-tools](https://pypi.org/project/tidas-tools/) 包。

## 📋 功能特性

### 已实现功能

- [x] 基于 JSON Schema 的 Pydantic 数据模型
- [x] 类型安全的数据操作
- [x] TIDAS 数据验证
- [x] JSON 到对象的转换
- [x] 属性访问工具
- [x] 实体创建的工厂函数

### 当前实现

- 基础项目结构
- 已配置 Pydantic 依赖
- 类型系统规划
- 开发环境设置

## 🔧 开发环境设置

### 前置要求

- Python 3.12+
- uv（推荐）或 pip

### 安装

```bash
# 克隆仓库
git clone https://github.com/tiangong-lca/tidas-sdk.git
cd tidas-sdk/sdks/python

# 安装依赖
uv sync

# 或使用 pip
pip install -e .
```

### 开发命令

```bash
# 安装开发依赖
uv sync --dev

# 运行测试
uv run pytest

# 运行代码检查
uv run ruff check

# 类型检查
uv run mypy .

# 代码格式化
uv run black .

# 运行测试并生成覆盖率报告
uv run pytest --cov=src/tidas_sdk --cov-report=html
```

## 📚 使用说明

### 基础用法（规划中）

```python
from tidas_sdk import TidasContact

# 创建联系人
contact = TidasContact(
    name="示例组织",
    email="contact@example.com"
)

# 验证联系人
contact.validate()

# 转换为 JSON
contact_json = contact.model_dump_json()
```

### 复杂实体的构建器模式

TIDAS 实体通常具有深度嵌套和复杂性。SDK 提供自动生成的构建器类，用于增量构建：

```python
import uuid
from tidas_sdk.builders.tidas_contacts_builders import ContactDataSetBuilder

# 创建构建器
builder = ContactDataSetBuilder()

# 逐步设置字段
builder.contactInformation.dataSetInformation.common_UUID = str(uuid.uuid4())
builder.contactInformation.dataSetInformation.set_name("张三博士", "zh")
builder.contactInformation.dataSetInformation.set_shortName("张三", "zh")
builder.contactInformation.dataSetInformation.email = "zhang@example.com"

# 添加多语言支持
builder.contactInformation.dataSetInformation.set_name("Dr. Zhang San", "en")
builder.contactInformation.dataSetInformation.set_name("张三博士", "zh")

# 构建最终的 Pydantic 模型
contact = builder.build()
```

**主要特性：**
- ✅ 增量字段赋值
- ✅ 嵌套构建器自动初始化
- ✅ 多语言辅助方法（`set_name()`、`get_name()`）
- ✅ 可选验证（在 `build()` 时验证，而非赋值时）
- ✅ 类型安全，完整的 IDE 自动补全

查看[构建器模式指南](docs/builder-pattern-guide.md)获取完整示例。

## 🏗️ 项目结构

```
sdks/python/
├── src/
│   └── tidas_sdk/          # 主包
├── tests/                  # 测试套件
├── examples/               # 使用示例
├── scripts/                # 开发脚本
├── pyproject.toml          # 项目配置
└── README.md               # 本文件
```

## 🧪 测试

```bash
# 运行所有测试
uv run pytest

# 运行测试并生成覆盖率报告
uv run pytest --cov=src/tidas_sdk --cov-report=term-missing

# 运行特定测试
uv run pytest tests/test_example.py
```

## 📖 文档

- **开发指南**: [../../CLAUDE.md](../../CLAUDE.md)
- **项目进度**: [../../docs/development-progress.md](../../docs/development-progress.md)
- **需求文档**: [../../docs/requirement-design.md](../../docs/requirement-design.md)

## 🤝 贡献

我们欢迎贡献！请：

1. 遵循主仓库中的开发指南
2. 为新功能添加测试
3. 确保代码通过代码检查和类型检查
4. 根据需要更新文档

## 🚀 发布流程

### 准备工作

在发布前，确保您的 Python SDK 已经完成开发并通过所有测试：

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

Python 包使用 `build` 工具来构建分发包：

```bash
# 安装构建工具
uv add --dev build

# 构建分发包
uv run python -m build
```

这将在 `dist/` 目录下创建两个文件：

- 一个 `.tar.gz` 源码包
- 一个 `.whl` 二进制包

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

### 发布到 PyPI

#### 准备 PyPI 账户

确保您有 PyPI 账户并已配置 API 令牌：

1. 在 [PyPI](https://pypi.org/) 注册账户
2. 在账户设置中生成 API 令牌
3. 配置认证（推荐使用 `keyring` 或环境变量）

#### 安装发布工具

```bash
# 安装 twine（用于上传包）
uv add --dev twine
```

#### 上传到测试 PyPI（推荐先测试）

```bash
# 上传到测试 PyPI
uv run twine upload --repository testpypi dist/*

# 从测试 PyPI 安装测试
pip install --index-url https://test.pypi.org/simple/ tidas-sdk
```

#### 上传到正式 PyPI

```bash
# 上传到正式 PyPI
uv run twine upload dist/*
```

### 版本管理

在 `pyproject.toml` 中更新版本号：

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

### CI/CD 自动化发布

项目支持通过 GitHub Actions 自动发布流程。当创建带有版本标签（如 `v0.1.1`）的提交时，会自动触发发布流程。

## 📄 许可证

MIT 许可证 - 查看 [LICENSE](../LICENSE) 文件了解详情。

## 🔗 相关包

- [tidas-tools](https://pypi.org/project/tidas-tools/): 生产级 TIDAS 数据工具
- [@tiangong-lca/tidas-sdk](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk): TypeScript SDK

## 📋 使用示例

### 创建实体

SDK 提供两种创建实体的方式：

1. **包装器方式**（原始）：

   ```python
   from tidas_sdk import create_process
   process = create_process()
   process.process_data_set.process_information.data_set_information.name.base_name.set_text("电力生产", "zh")
   process.validate()
   ```

2. **Pydantic 模型方式**（新）：
   ```python
   from tidas_sdk import create_process_model
   process = create_process_model()
   # 直接通过 Pydantic 模型访问数据
   process.process_data_set.process_information.data_set_information.name.base_name = "电力生产"
   # 在实例化时自动进行验证
   ```

### 在两种方式之间转换

您可以在包装器和 Pydantic 模型之间转换：

```python
# 从包装器转换为 Pydantic
process_wrapper = create_process()
process_model = process_wrapper.to_pydantic()

# 从 Pydantic 转换为包装器
process_model = create_process_model()
process_wrapper = TidasProcesses(process_model.model_dump())
```

### 示例脚本

查看 [examples/06_pydantic_models.py](examples/06_pydantic_models.py) 获取演示两种方式的完整示例。

### 验证

两种方式都提供验证：

- **包装器方式**: 在包装器实例上调用 `.validate()` 方法
- **Pydantic 模型方式**: 在实例化时自动验证

### 序列化

两种方式都支持 JSON 序列化：

- **包装器方式**: 在包装器实例上调用 `.model_dump_json()` 方法
- **Pydantic 模型方式**: 在 Pydantic 模型实例上调用 `.model_dump_json()` 方法
