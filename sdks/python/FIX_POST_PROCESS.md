# 修复后处理脚本的执行顺序问题

## 问题

在 `sdks/python/scripts/post_process_types.py` 的 `post_process_file` 函数中，执行顺序错误导致重复的类定义没有被删除。

## 需要修改的代码

### 文件位置
`sdks/python/scripts/post_process_types.py`

### 修改内容

**当前代码结构（第980-1391行）**：
```python
def post_process_file(file_path: Path, dry_run: bool = False):
    content = file_path.read_text(encoding="utf-8")
    original_content = content
    stats = {...}
    used_import_types = set()

    # ❌ 错误：Step 1 - 先替换引用（line 999-1017）
    for old_name, new_name in CLASS_REMOVALS.items():
        if old_name in content:
            content = replace_type_references(content, old_name, new_name)
            # 这会把 class StringMultiLang1 改成 class StringMultiLang
            stats["types_replaced"] += 1
            used_import_types.add(new_name)

    # ❌ 错误：Step 2 - 后删除类定义（line 1018-1063）
    classes_to_remove = find_classes_to_remove(content)
    # 但此时类名已经变了，找不到 StringMultiLang1，删除失败
```

**修复后的代码结构**：
```python
def post_process_file(file_path: Path, dry_run: bool = False):
    content = file_path.read_text(encoding="utf-8")
    original_content = content
    stats = {...}
    used_import_types = set()

    # ✅ 正确：Step 1 - 先删除类定义（在原始名称时）
    classes_to_remove = find_classes_to_remove(content)

    if classes_to_remove and not dry_run:
        lines = content.split("\n")
        for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
            logger.debug(
                f"  Removing class: {class_name} (replaced with {replacement})"
            )
            lines = remove_class_definition_by_lines(
                lines, start_line_idx, end_line_idx
            )
            stats["classes_removed"] += 1
            used_import_types.add(replacement)
            # Track multi-lang item types
            if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if replacement == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif replacement == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif replacement == "FTMultiLang":
                    used_import_types.add("MultiLangItem")
        content = "\n".join(lines)
    elif classes_to_remove:
        # Dry run
        for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
            logger.debug(
                f"  Would remove class: {class_name} (replaced with {replacement})"
            )
            stats["classes_removed"] += 1
            used_import_types.add(replacement)
            if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if replacement == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif replacement == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif replacement == "FTMultiLang":
                    used_import_types.add("MultiLangItem")

    # ✅ 正确：Step 2 - 再替换引用（在类删除后）
    for old_name, new_name in CLASS_REMOVALS.items():
        if old_name in content:
            logger.debug(f"  Replacing type reference: {old_name} -> {new_name}")
            if not dry_run:
                content = replace_type_references(content, old_name, new_name)
            stats["types_replaced"] += 1
            used_import_types.add(new_name)
            # Track multi-lang item types
            if new_name in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
                if new_name == "StringMultiLang":
                    used_import_types.add("MultiLangItemString")
                elif new_name == "STMultiLang":
                    used_import_types.add("MultiLangItemST")
                elif new_name == "FTMultiLang":
                    used_import_types.add("MultiLangItem")

    # Step 3: 处理category导入和字段类型替换（保持不变）
    # ...

    # Step 4: 添加导入语句（保持不变）
    # ...

    # Step 5: 写入文件（保持不变）
    # ...
```

## 具体修改步骤

### 步骤 1：备份原文件
```bash
cd /Users/biao/Code/tidas-sdk/sdks/python
cp scripts/post_process_types.py scripts/post_process_types.py.backup
```

### 步骤 2：修改代码

打开 `scripts/post_process_types.py`，找到 `post_process_file` 函数（第980行）。

**需要移动的代码块**：

1. **找到 Step 1（原line 999-1017）** - 替换引用的代码：
   ```python
   # Step 1: Replace type references first (before removing classes)
   # Build replacement map from CLASS_REMOVALS
   for old_name, new_name in CLASS_REMOVALS.items():
       if old_name in content:
           logger.debug(f"  Replacing type reference: {old_name} -> {new_name}")
           if not dry_run:
               content = replace_type_references(content, old_name, new_name)
           stats["types_replaced"] += 1
           used_import_types.add(new_name)

           # For multi-language types, also need the item types
           if new_name in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
               if new_name == "StringMultiLang":
                   used_import_types.add("MultiLangItemString")
               elif new_name == "STMultiLang":
                   used_import_types.add("MultiLangItemST")
               elif new_name == "FTMultiLang":
                   used_import_types.add("MultiLangItem")
   ```

2. **找到 Step 2（原line 1018-1063）** - 删除类定义的代码：
   ```python
   # Step 2: Find and remove duplicate class definitions (after references are replaced)
   classes_to_remove = find_classes_to_remove(content)

   if classes_to_remove and not dry_run:
       # Work with lines for safer deletion
       lines = content.split("\n")

       # Remove classes from end to start to maintain line indices
       for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
           logger.debug(
               f"  Removing class: {class_name} (replaced with {replacement})"
           )
           lines = remove_class_definition_by_lines(
               lines, start_line_idx, end_line_idx
           )
           stats["classes_removed"] += 1
           used_import_types.add(replacement)

           # For multi-language types, also need the item types
           if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
               if replacement == "StringMultiLang":
                   used_import_types.add("MultiLangItemString")
               elif replacement == "STMultiLang":
                   used_import_types.add("MultiLangItemST")
               elif replacement == "FTMultiLang":
                   used_import_types.add("MultiLangItem")

       # Reconstruct content from lines
       content = "\n".join(lines)
   elif classes_to_remove:
       # Dry run: just count
       for start_line_idx, end_line_idx, class_name, replacement in classes_to_remove:
           logger.debug(
               f"  Would remove class: {class_name} (replaced with {replacement})"
           )
           stats["classes_removed"] += 1
           used_import_types.add(replacement)

           # For multi-language types, also need the item types
           if replacement in ["StringMultiLang", "STMultiLang", "FTMultiLang"]:
               if replacement == "StringMultiLang":
                   used_import_types.add("MultiLangItemString")
               elif replacement == "STMultiLang":
                   used_import_types.add("MultiLangItemST")
               elif replacement == "FTMultiLang":
                   used_import_types.add("MultiLangItem")
   ```

3. **交换顺序**：
   - 将 Step 2（删除类定义）的代码移到 Step 1（替换引用）之前
   - 更新注释：
     - 原 Step 1 → 新 Step 2
     - 原 Step 2 → 新 Step 1

4. **更新注释**：
   - 新 Step 1 注释：`# Step 1: Find and remove duplicate class definitions (before replacing references)`
   - 新 Step 2 注释：`# Step 2: Replace type references (after removing class definitions)`

### 步骤 3：重新生成类型文件

```bash
cd /Users/biao/Code/tidas-sdk/sdks/python

# 重新生成所有类型文件
python3 scripts/generate_types.py --force --verbose
```

### 步骤 4：验证修复

```bash
# 检查是否还有重复定义
for f in src/tidas_sdk/types/tidas_{processes,flows,contacts,sources}.py; do
    echo "=== $(basename $f) ==="
    python3 /tmp/check_duplicates.py "$f"
done

# 期望输出：No duplicate class definitions found.
```

### 步骤 5：运行类型检查

```bash
cd /Users/biao/Code/tidas-sdk/sdks/python

# 确保在虚拟环境中
uv run mypy src/tidas_sdk/types/ --no-error-summary

# 或者
PYTHONPATH="src:$PYTHONPATH" uv run mypy src/tidas_sdk/types/
```

## 额外优化：清理重复的联合类型

修复执行顺序后，还可能存在冗余的联合类型（例如 `StringMultiLang | StringMultiLang`）。

可以在替换引用后添加清理步骤：

```python
# Step 2: Replace type references (after removing class definitions)
for old_name, new_name in CLASS_REMOVALS.items():
    if old_name in content:
        if not dry_run:
            content = replace_type_references(content, old_name, new_name)
        # ...

# ✅ 新增：清理重复的联合类型
if not dry_run:
    # 清理 "Type | Type" → "Type"
    import re
    original_content_before_cleanup = content
    content = re.sub(
        r'(\w+)\s*\|\s*\1\b',  # 匹配 "Type | Type"（相邻重复）
        r'\1',  # 替换为 "Type"
        content
    )
    if content != original_content_before_cleanup:
        logger.debug("  Cleaned up duplicate union types")
```

将这段代码添加到 Step 2 的结尾（在 for 循环之后）。

## 验证清单

修复完成后，验证以下内容：

- [ ] 所有 `tidas_*.py` 文件都正确导入了 `tidas_data_types` 中的类型
- [ ] 没有重复的类定义（运行 `check_duplicates.py` 应该返回 "No duplicate"）
- [ ] `field_classId` 和 `field_catId` 使用了正确的 category 类型
- [ ] `text` 字段使用了对应的 `Tidas*Text` 类型
- [ ] 没有冗余的联合类型（如 `Type | Type`）
- [ ] 类型检查通过（`mypy src/tidas_sdk/types/`）
- [ ] 可以成功导入模块：
  ```bash
  python3 -c "from tidas_sdk.types import tidas_processes; print('✅ Import successful')"
  ```

## 预期结果

修复后，生成的文件应该是这样的：

```python
# tidas_processes.py

from tidas_sdk.types.tidas_data_types import (
    StringMultiLang,
    GlobalReferenceType,
    # ... 其他导入
)

from tidas_sdk.types.tidas_processes_category import (
    Processes,
    TidasProcessesText
)

# ✅ 不应该有重复的类定义

class Name(BaseModel):
    baseName: StringMultiLang  # ✅ 使用导入的类型，不重复
    # ...

class CommonClas(BaseModel):
    field_classId: Processes  # ✅ 使用 category 类型
    text: TidasProcessesText  # ✅ 使用 Text 类型
    # ...
```
