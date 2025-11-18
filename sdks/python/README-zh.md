# TIDAS Python SDK

[English](README.md) | [中文](README-zh.md)

TIDAS Python SDK 为 ILCD/TIDAS 生命周期评价数据模型提供类型安全的封装，让你在 Python 中轻松创建、验证与转换 LCA 数据对象。

## 状态

- 当前版本：0.1.0（预览版）
- 发布方式：源码安装（PyPI 发布计划中）

## 前置条件

- Python 3.12+
- 使用 [uv](https://docs.astral.sh/uv/) 管理依赖与执行脚本  
  _如未安装，可运行 `curl -LsSf https://astral.sh/uv/install.sh | sh`_

## 安装

```bash
cd sdks/python
uv sync --group dev  # 安装核心依赖及开发工具
```

## 快速开始

运行示例脚本快速体验核心功能：

```bash
uv run python examples/usage.py
```

最小化示例：

```python
from tidas_sdk import create_process

process = create_process({})
process.process_data_set.process_information.data_set_information.name.base_name.set_text(
    "示例工艺", lang="zh"
)

print(process.to_json())
```

## `examples/usage.py` 展示的特性

- **JSON 初始化对象**：`create_process()` 可以从完整或不完整的 JSON 数据构建 `TidasProcess`（见 `creat_object_from_json()`）。
- **对象导出为 JSON**：`to_json()` 返回符合 ILCD 规范的字典结构，便于与其他系统交互（见 `convert_object_to_json()`）。
- **属性访问与多语言支持**：可通过点号访问嵌套字段，多语言字段提供 `set_text()` 与 `get_text()` 方法（见 `properties_access()`）。
- **类型提示与自动补全**：生成的类具备完整类型信息，IDE 可提供精准提示（见 `type_hinting_and_autocompletion()`）。
- **按需验证**：待数据补全后再调用 `validate()`，并可通过 `last_validation_error()` 查看详细错误（见 `validation_on_demand()`）。
- **导出为 XML**：`to_xml()` 可输出符合 ILCD 标准的 XML 字符串（见 `convert_to_xml()`）。

## 开发流程

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
