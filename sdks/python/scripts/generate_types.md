# generate_types.py 生成逻辑文档

## 概述

`generate_types.py` 是一个使用 `datamodel-code-generator` 库从 TIDAS JSON schemas 自动生成 Pydantic v2 模型的脚本。它取代了之前的自定义 AST 代码生成器，采用更成熟稳定的开源库来确保代码质量和可维护性。

## 主要功能

1. **自动查找 Schema 目录**：智能定位 TIDAS schemas 目录
2. **批量生成 Pydantic 模型**：从 JSON Schema 生成 Python 类型定义
3. **生成模块导出文件**：自动创建 `__init__.py` 统一导出
4. **集成下游生成器**：协调调用类别文件和包装器生成脚本
5. **性能监控**：跟踪生成时间，目标 <30 秒

## 整体工作流程

```
开始
  ↓
解析命令行参数 (parse_args)
  ↓
配置日志级别 (setup_logging)
  ↓
查找 Schema 目录 (find_schema_dir)
  ↓
创建输出目录
  ↓
筛选 Schema 文件 (跳过 category 和 data_types)
  ↓
批量生成 Pydantic 模型 (generate_schema)
  ↓
生成 __init__.py (generate_init_file)
  ↓
打印生成摘要 (print_summary)
  ↓
调用 generate_category_types.py
  ↓
调用 generate_wrappers.py
  ↓
返回退出码
```

## 核心函数详解

### 1. `parse_args()` - 参数解析

解析命令行参数：

- `--schema-dir`: 指定 schema 目录路径（可选，默认自动查找）
- `--output-dir`: 输出目录（默认：`src/tidas_sdk/types`）
- `--force`: 强制覆盖已存在文件
- `--verbose/-v`: 启用详细日志

### 2. `setup_logging(verbose)` - 日志配置

根据 `verbose` 参数设置日志级别：

- `verbose=True`: DEBUG 级别
- `verbose=False`: INFO 级别

使用 `loguru` 库进行日志管理。

### 3. `find_schema_dir(provided_dir)` - Schema 目录查找

**自动查找逻辑**：

1. 如果用户提供了 `--schema-dir`，直接使用该路径
2. 否则，从当前目录向上搜索最多 5 层，查找：
   ```
   {current_dir}/tidas-tools/src/tidas_tools/tidas/schemas
   ```

**返回值**：`Path` 对象指向 schema 目录

**异常**：如果找不到目录，抛出 `FileNotFoundError`

### 4. `generate_schema(schema_file, output_dir, force)` - 单文件生成

**功能**：为单个 JSON schema 文件生成对应的 Pydantic 模型文件

**流程**：

1. 确定输出文件名：`{schema_name}.json` → `{schema_name}.py`
2. 检查文件是否存在：
   - 存在且未使用 `--force`：返回跳过状态
   - 否则继续生成
3. 调用 `datamodel-codegen` 生成代码

**datamodel-codegen 关键参数**：

```python
--input-file-type jsonschema        # 输入类型：JSON Schema
--output-model-type pydantic_v2.BaseModel  # 使用 Pydantic v2
--use-standard-collections          # 使用 list 而不是 List
--use-union-operator                # 使用 | 而不是 Union
--target-python-version 3.12        # 目标 Python 版本
--field-constraints                 # 使用 Field() 约束
--reuse-model                       # 重用相同内容的模型
--collapse-root-models              # 合并 RootModel 包装器
--union-mode smart                  # 智能联合类型处理
--use-title-as-name                 # 使用 schema title 作为类名
--use-schema-description            # 从描述生成文档字符串
--disable-timestamp                 # 移除生成时间戳
```

**返回值**：`(success: bool, error_message: str)`

### 5. `generate_init_file(output_dir, generated_files)` - 初始化文件生成

**功能**：生成 `__init__.py` 文件，统一导出所有生成的模型

**生成逻辑**：

1. 从每个生成的文件名提取模块名
2. 导入每个模块的 `Model` 类，并重命名为驼峰形式
3. 生成 `__all__` 列表

**示例输出**：

```python
"""Generated Pydantic types from TIDAS schemas."""

from .tidas_contacts import Model as TidasContacts
from .tidas_flows import Model as TidasFlows
...

__all__ = [
    "TidasContacts",
    "TidasFlows",
    ...
]
```

### 6. `print_summary(stats, duration)` - 摘要输出

打印生成统计信息：

- ✅ 成功生成数量
- ⏭️ 跳过数量（文件已存在）
- ❌ 错误数量
- ⏱️ 耗时
- 性能检查（目标 <30 秒）

## 主流程 (main)

### 阶段 1：初始化和准备

```python
# 1. 解析参数
args = parse_args()
setup_logging(args.verbose)

# 2. 查找 schema 目录
schema_dir = find_schema_dir(args.schema_dir)

# 3. 创建输出目录
output_dir = Path(args.output_dir)
output_dir.mkdir(parents=True, exist_ok=True)
```

### 阶段 2：筛选 Schema 文件

```python
# 查找所有 tidas_*.json 文件
all_schema_files = sorted(schema_dir.glob("tidas_*.json"))

# 跳过以下模式的文件：
skip_patterns = ['_category.json', 'data_types.json']
# - category 文件：由 generate_category_types.py 单独生成（避免编号后缀）
# - data_types：手动维护，支持多语言对齐
```

**跳过原因**：

- `_category.json`: 使用专门的生成器生成更干净的类别类型（Literal + TypedDict）
- `data_types.json`: 手动维护以确保多语言 SDK 之间的类型对齐

### 阶段 3：批量生成

```python
stats = {
    "generated": 0,    # 成功生成数
    "skipped": 0,     # 跳过数
    "errors": 0,      # 错误数
    "files": [],      # 生成的文件列表
}

for schema_file in schema_files:
    success, error = generate_schema(schema_file, output_dir, args.force)
    # 更新统计信息
```

### 阶段 4：生成导出文件

```python
if stats["generated"] > 0:
    generate_init_file(output_dir, stats["files"])
```

### 阶段 5：调用下游生成器

脚本会按顺序调用两个下游生成器：

#### 5.1 生成类别文件

```python
category_script = Path(__file__).parent / "generate_category_types.py"
subprocess.run([sys.executable, str(category_script)], ...)
```

**目的**：生成干净的类别类型文件，使用 `Literal` + `TypedDict` 模式，避免 `datamodel-codegen` 生成的编号后缀（如 `Source1`, `Source2`）

**生成的类别**：

- `tidas_contacts_category.json`
- `tidas_flows_elementary_category.json`
- `tidas_flows_product_category.json`
- `tidas_processes_category.json`
- `tidas_flowproperties_category.json`
- `tidas_lciamethods_category.json`
- `tidas_locations_category.json`
- `tidas_sources_category.json`
- `tidas_unitgroups_category.json`

#### 5.2 生成类型包装器

```python
wrapper_script = Path(__file__).parent / "generate_wrappers.py"
subprocess.run([sys.executable, str(wrapper_script)], ...)
```

**目的**：生成类型化的包装器类，提供 IDE 自动完成和类型提示功能（Feature 004）

**生成的包装器实体**：

- contacts
- flows
- processes
- sources
- flowproperties
- unitgroups
- lciamethods
- lifecyclemodels

## 依赖关系

### 外部依赖

- **datamodel-code-generator**: JSON Schema → Pydantic 模型转换
- **loguru**: 日志记录
- **Pydantic v2**: 生成的模型基类

### 内部依赖脚本

1. **generate_category_types.py**
   - 位置：同目录下
   - 作用：生成干净的类别类型文件
   - 触发条件：主脚本完成实体模型生成后

2. **generate_wrappers.py**
   - 位置：同目录下
   - 作用：生成类型化包装器类
   - 触发条件：类别文件生成后

## 文件筛选规则

### 包含的文件

- 匹配模式：`tidas_*.json`
- 排除模式：`*_category.json`, `*data_types.json`

### 文件命名约定

- 输入：`tidas_{entity}.json`
- 输出：`tidas_{entity}.py`
- 模型类：每个文件包含一个 `Model` 类（顶层类）

## 错误处理

1. **Schema 目录未找到**
   - 异常：`FileNotFoundError`
   - 处理：记录错误并返回退出码 1

2. **无 Schema 文件**
   - 检查：`glob` 结果为空
   - 处理：记录错误并返回退出码 1

3. **生成失败**
   - 捕获：`subprocess.CalledProcessError`
   - 处理：记录错误信息，更新错误统计，继续处理下一个文件

4. **下游脚本执行失败**
   - 处理：打印警告信息，但不影响主流程退出码
   - 主脚本的退出码仅基于实体模型生成结果

## 性能目标

- **目标**：总生成时间 < 30 秒
- **监控**：使用 `time.perf_counter()` 测量
- **反馈**：在摘要中显示性能状态

## 使用示例

### 基本使用

```bash
# 自动查找 schema 目录并生成
python scripts/generate_types.py

# 指定 schema 目录
python scripts/generate_types.py --schema-dir /path/to/schemas

# 强制覆盖已存在文件
python scripts/generate_types.py --force

# 启用详细日志
python scripts/generate_types.py --verbose
```

### 典型输出

```
Schema directory: /path/to/tidas-tools/src/tidas_tools/tidas/schemas
Output directory: src/tidas_sdk/types
Found 15 schemas total
Skipping 2 category/base schemas (manually created)
Will generate 13 entity schemas
Starting code generation...
✅ Generated tidas_contacts.json
✅ Generated tidas_flows.json
...

============================================================
GENERATION SUMMARY
============================================================
✅ Successfully generated: 13 schemas
⏱️  Duration:              12.45 seconds
============================================================
✅ Performance target met (<30 seconds)

============================================================
GENERATING CLEAN CATEGORY FILES
============================================================
...

============================================================
GENERATING TYPED WRAPPERS
============================================================
...
```

## 设计理念

1. **可靠性**：使用成熟的 `datamodel-codegen` 而非自定义生成器
2. **可维护性**：清晰的模块化设计，易于扩展
3. **性能**：批量处理，并行化潜力
4. **用户体验**：详细的日志和摘要输出
5. **灵活性**：支持自定义 schema 目录和输出目录
6. **集成性**：自动协调多个生成器脚本，形成完整的代码生成流程

## 注意事项

1. **文件覆盖**：默认情况下，已存在的文件会被跳过。使用 `--force` 强制覆盖。

2. **下游脚本依赖**：确保 `generate_category_types.py` 和 `generate_wrappers.py` 在相同目录下。

3. **Python 版本**：生成的代码针对 Python 3.12，但兼容 Python 3.8+。

4. **Schema 格式**：输入必须是有效的 JSON Schema 格式。

5. **类别文件**：`_category.json` 文件不会通过 `datamodel-codegen` 生成，而是使用专门的生成器以确保代码质量和多语言对齐。
