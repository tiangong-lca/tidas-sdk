# TIDAS Python SDK

[English](README.md) | [中文](README-zh.md)

TIDAS Python SDK 为 ILCD/TIDAS 生命周期评价（LCA）数据提供类型安全的 Python 封装。
它基于自动生成的 Pydantic 模型，并提供更高层的工厂函数与辅助方法，方便你在 Python 中读取、
构建、验证与导出符合 ILCD 标准的数据集。

## 安装

### 通过 PyPI 安装

```bash
pip install tidas-sdk
```

### 从源码安装（本仓库）

```bash
cd sdks/python
uv sync --group dev  # 安装核心依赖及开发工具
```

## 快速开始

运行示例脚本快速体验核心功能：

```bash
uv run python examples/usage.py
```

最小示例：

```python
from tidas_sdk import create_process

process = create_process({})
process.process_data_set.process_information.data_set_information.name.base_name.set_text(
    "示例工艺", lang="zh"
)

print(process.to_json())
```

## 基本用法

### 创建实体对象

```python
from tidas_sdk import create_process, create_flow, create_source

process = create_process({})
flow = create_flow({})
source = create_source({})
```

也可以直接从 ILCD 风格的 JSON 创建：

```python
from pathlib import Path
from tidas_sdk import create_process_from_json

process = create_process_from_json(Path("process.json"))
```

如果手头已经有标准的 ILCD XML 数据集，也可以直接加载：

```python
from pathlib import Path
from tidas_sdk import create_process_from_xml, TidasProcess

process = create_process_from_xml(Path("process.xml"))
# 或使用类方法
process = TidasProcess.from_xml(Path("process.xml"))
```

### 处理多语言字段

```python
name_list = process.process_data_set.process_information.data_set_information.name.base_name
name_list.set_text("Sample Process", lang="en")
name_list.set_text("示例工艺", lang="zh")
print(name_list.get_text("en"))
```

### 校验与导出

```python
is_valid = process.validate()        # 触发 Pydantic / JSON Schema 校验
json_payload = process.to_json()     # 导出为 ILCD 兼容的字典
xml_payload = process.to_xml()       # 导出为 ILCD XML 字符串
```

## 主要特性

- **JSON → 对象**：`create_process()` 等工厂函数可以从完整或不完整的 ILCD JSON 数据构建实体对象。
- **对象 → JSON**：`to_json()` 返回符合 ILCD 结构的字典，可直接用于存储或下游工具。
- **多语言字段支持**：`MultiLangList` 提供 `set_text()` / `get_text()`，简化 `@xml:lang` / `#text` 结构的处理。
- **强类型与自动补全**：生成的 Pydantic 模型具备完整类型信息，IDE 能提供精确的类型提示和补全。
- **按需验证**：通过 `validate()` 触发 Pydantic / JSON Schema 校验，并可用 `last_validation_error()` 查看详细错误。
- **导出为 XML**：`to_xml()` 可将实体转换为 ILCD XML，方便与其他 LCA 系统集成。

完整用法示例可参考 `examples/usage.py`。

## 开发流程（针对贡献者）

```bash
# 安装或更新依赖
uv sync --group dev

# 代码检查与格式化
uv run ruff check src
uv run ruff format src

# 类型检查
uv run mypy src

# 运行测试
uv run pytest
```

## 项目结构

- `src/tidas_sdk`：核心实现与生成模型
- `examples/usage.py`：README 中提及的功能演示
- `scripts/`：代码生成与维护脚本

如需反馈或贡献，请访问 https://github.com/tiangong-lca/tidas-sdk 提交 Issue 或 Pull Request。
