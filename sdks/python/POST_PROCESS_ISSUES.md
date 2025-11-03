# 后处理脚本问题分析和修复方案

## 问题概述

后处理脚本 `post_process_types.py` 存在一个**关键的执行顺序问题**，导致：
- ❌ 重复的类定义没有被删除
- ❌ 每个实体文件中都存在 4+ 个重复定义的类
- ❌ 这会导致 Python 运行时错误（后面的类定义会覆盖前面的）

## 问题细节

### 当前执行流程（错误）

```python
def post_process_file(file_path: Path, dry_run: bool = False):
    content = file_path.read_text()

    # Step 1: 替换类型引用 (line 999-1007)
    for old_name, new_name in CLASS_REMOVALS.items():
        if old_name in content:
            content = replace_type_references(content, old_name, new_name)
            # 问题：这也会替换类定义的名字！
            # 原始: class StringMultiLang1(BaseModel):
            # 替换后: class StringMultiLang(BaseModel):

    # Step 2: 查找并删除类定义 (line 1018-1063)
    classes_to_remove = find_classes_to_remove(content)
    # 问题：查找 "StringMultiLang1"，但已经变成 "StringMultiLang" 了
    # 结果：找不到，删除失败
```

### 实际效果示例

**原始生成的代码**：
```python
class StringMultiLang1(BaseModel):
    # ...

class StringMultiLang2(BaseModel):
    # ...

field: StringMultiLang1 | StringMultiLang2
```

**经过 Step 1 (replace_type_references) 后**：
```python
class StringMultiLang(BaseModel):  # ← 被重命名了
    # ...

class StringMultiLang(BaseModel):  # ← 被重命名了（重复！）
    # ...

field: StringMultiLang | StringMultiLang  # ← 引用被替换
```

**经过 Step 2 (find_classes_to_remove) 后**：
```python
# 查找 "StringMultiLang1" 和 "StringMultiLang2"
# ❌ 找不到（因为已经变成 "StringMultiLang"）
# ❌ 删除失败

# 结果：保留了重复的类定义
class StringMultiLang(BaseModel):  # ← 重复定义！
    # ...

class StringMultiLang(BaseModel):  # ← 重复定义！
    # ...
```

### 当前状态

所有生成的文件都存在重复定义：

| 文件 | 重复定义的类 |
|------|-------------|
| `tidas_processes.py` | StringMultiLang(2x), STMultiLang(2x), FTMultiLang(2x), GlobalReferenceType(2x) |
| `tidas_flows.py` | StringMultiLang(3x), STMultiLang(2x), FTMultiLang(2x), GlobalReferenceType(3x) |
| `tidas_contacts.py` | StringMultiLang(2x), STMultiLang(2x), FTMultiLang(3x), GlobalReferenceType(2x) |
| `tidas_sources.py` | （未检查，预计类似）|
| `tidas_flowproperties.py` | （未检查，预计类似）|

## 修复方案

### 方案 1：调整执行顺序（推荐）

**修改 `post_process_file` 函数的执行顺序**：

```python
def post_process_file(file_path: Path, dry_run: bool = False):
    content = file_path.read_text()

    # ✅ Step 1: 先查找并删除类定义（在类名还是原始名称时）
    classes_to_remove = find_classes_to_remove(content)

    if classes_to_remove and not dry_run:
        lines = content.split("\n")
        for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
            lines = remove_class_definition_by_lines(lines, start_line_idx, end_line_idx)
        content = "\n".join(lines)

    # ✅ Step 2: 再替换类型引用（把使用的地方改成新名字）
    for old_name, new_name in CLASS_REMOVALS.items():
        if old_name in content:
            content = replace_type_references(content, old_name, new_name)

    # Step 3-4: 添加导入语句等其他操作
    # ...
```

**修改位置**：
- 文件：`sdks/python/scripts/post_process_types.py`
- 函数：`post_process_file` (line 980-1391)
- 需要移动：
  - line 1018-1063 (Step 2: 删除类定义) → 移到 line 999 之前
  - line 999-1007 (Step 1: 替换引用) → 移到删除类定义之后

### 方案 2：两阶段查找（备选）

如果不想改变顺序，可以改进 `find_classes_to_remove` 函数：

```python
def find_classes_to_remove(content: str) -> list[tuple[int, int, str, str]]:
    """Find all class definitions that should be removed."""
    classes = []
    lines = content.split("\n")

    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # ✅ 检查原始名称
                if node.name in CLASS_REMOVALS:
                    # 找到原始名称的类
                    ...
                # ✅ 也检查替换后的名称
                elif node.name in CLASS_REMOVALS.values():
                    # 找到已经被替换名称的类
                    # 但这个类应该被导入而不是在这里定义
                    ...
    except SyntaxError:
        # 回退逻辑
        ...

    return classes
```

**但这个方案有问题**：
- 无法区分"应该被删除的 StringMultiLang"和"新导入的 StringMultiLang"
- 可能误删正确的类定义

### 方案 3：使用 AST 直接删除（高级）

在 Step 1 执行前，先用 AST 记录要删除的类的位置：

```python
def post_process_file(file_path: Path, dry_run: bool = False):
    content = file_path.read_text()

    # ✅ Step 0: 先记录要删除的类的位置（在名字还没改变时）
    classes_to_remove_positions = []
    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if node.name in CLASS_REMOVALS:
                # 记录行号
                classes_to_remove_positions.append((node.lineno, node.name))

    # Step 1: 替换类型引用
    for old_name, new_name in CLASS_REMOVALS.items():
        content = replace_type_references(content, old_name, new_name)

    # ✅ Step 2: 使用之前记录的位置删除类（即使名字已经改变）
    lines = content.split("\n")
    for lineno, class_name in sorted(classes_to_remove_positions, reverse=True):
        # 删除从 lineno 开始的类定义
        ...
```

## 推荐修复步骤

1. **立即修复**：使用方案 1，调整执行顺序
   ```bash
   cd /Users/biao/Code/tidas-sdk/sdks/python

   # 编辑 post_process_types.py
   # 将 Step 2（删除类）移到 Step 1（替换引用）之前
   ```

2. **重新生成类型文件**：
   ```bash
   python3 scripts/generate_types.py --force
   ```

3. **验证修复**：
   ```bash
   # 检查是否还有重复定义
   python3 /tmp/check_duplicates.py src/tidas_sdk/types/tidas_processes.py
   ```

4. **运行类型检查**：
   ```bash
   uv run mypy src/tidas_sdk/types/
   ```

## 额外发现的问题

### 问题 2：重复的类使用

即使删除成功，还存在另一个问题：

```python
field: StringMultiLang | StringMultiLang  # ← 联合类型重复
```

这是因为：
- `StringMultiLang1` → `StringMultiLang`
- `StringMultiLang2` → `StringMultiLang`
- 结果：`StringMultiLang1 | StringMultiLang2` → `StringMultiLang | StringMultiLang`

**影响**：虽然不会报错，但这是冗余的类型注解。

**修复**：在替换引用后，清理重复的联合类型：
```python
# 清理 Type | Type → Type
content = re.sub(
    r'(\w+)\s*\|\s*\1(\s+)',  # 匹配 "Type | Type "
    r'\1\2',  # 替换为 "Type "
    content
)
```

## 原始 Schema 对比验证

### 原始 Schema (tidas_processes.json)

```json
{
  "baseName": {
    "$ref": "tidas_data_types.json#/$defs/StringMultiLang"
  },
  "referenceToComplementingProcess": {
    "$ref": "tidas_data_types.json#/$defs/GlobalReferenceType"
  }
}
```

### 期望生成的代码

```python
from tidas_sdk.types.tidas_data_types import (
    StringMultiLang,
    GlobalReferenceType,
)

# ✅ 不应该有类定义，直接使用导入的类型

class Name(BaseModel):
    baseName: StringMultiLang  # ✅ 使用导入的类型

class ComplementingProcesses(BaseModel):
    referenceToComplementingProcess: GlobalReferenceType  # ✅ 使用导入的类型
```

### 当前生成的代码（错误）

```python
from tidas_sdk.types.tidas_data_types import (
    StringMultiLang,  # ✅ 导入了
    GlobalReferenceType,  # ✅ 导入了
)

# ❌ 但是又重复定义了
class StringMultiLang(BaseModel):
    # ...

class StringMultiLang(BaseModel):  # ❌ 重复！
    # ...

class Name(BaseModel):
    baseName: StringMultiLang | StringMultiLang  # ❌ 引用也重复
```

## 总结

1. **主要问题**：后处理脚本的执行顺序错误
   - 应该先删除类定义，再替换引用
   - 当前是先替换引用（导致类名改变），再查找删除（找不到）

2. **影响范围**：所有生成的实体类型文件
   - 每个文件都有 4-6 个重复的类定义

3. **推荐修复**：调整 `post_process_file` 函数的执行顺序

4. **验证方式**：
   - 检查没有重复的类定义
   - 类型检查通过（mypy）
   - 导入的类型被正确使用
