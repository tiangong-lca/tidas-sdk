# Category File - Python Implementation Options

## 当前问题
Auto-generated的代码有 `Source1`, `Source2`, `Source3`... 等无意义的类名。

## 方案对比

---

## 方案1: Python Enum（最类型安全）

```python
"""
Source classification categories.
Clean implementation using Python Enum.
"""
from enum import Enum
from typing import TypedDict


class SourceCategory(Enum):
    """Source category enum with metadata."""

    IMAGES = ("0", "0", "Images")
    DATA_SET_FORMATS = ("1", "1", "Data set formats")
    DATABASES = ("2", "2", "Databases")
    COMPLIANCE_SYSTEMS = ("3", "3", "Compliance systems")
    STATISTICAL_CLASSIFICATIONS = ("4", "4", "Statistical classifications")
    PUBLICATIONS = ("5", "5", "Publications and communications")
    OTHER = ("6", "6", "Other source types")

    def __init__(self, class_id: str, level: str, text: str):
        self.class_id = class_id
        self.level = level
        self.text = text


# 使用示例
category = SourceCategory.IMAGES
print(category.class_id)  # "0"
print(category.text)      # "Images"
print(category.name)      # "IMAGES"

# 类型提示
def process_source(cat: SourceCategory) -> None:
    print(f"Processing {cat.text}")
```

**优点**:
- ✅ 类型安全（IDE自动补全）
- ✅ 不能使用无效值
- ✅ 清晰的语义

**缺点**:
- ⚠️ 需要用 `SourceCategory.IMAGES` 而不是字符串 `"0"`
- ⚠️ 与JSON序列化需要额外处理

---

## 方案2: Literal类型（最接近TypeScript）

```python
"""
Source classification categories.
Clean implementation using Literal types (TypeScript style).
"""
from typing import Literal, TypedDict


class SourceCategoryData(TypedDict):
    """Source category metadata."""
    level: str
    classId: str
    text: str


# Union type for all source categories (类型安全的字符串)
Source = Literal[
    "0",  # Images
    "1",  # Data set formats
    "2",  # Databases
    "3",  # Compliance systems
    "4",  # Statistical classifications
    "5",  # Publications and communications
    "6",  # Other source types
]

# Runtime metadata dictionary
SOURCE_CATEGORIES: dict[str, SourceCategoryData] = {
    "0": {"level": "0", "classId": "0", "text": "Images"},
    "1": {"level": "0", "classId": "1", "text": "Data set formats"},
    "2": {"level": "0", "classId": "2", "text": "Databases"},
    "3": {"level": "0", "classId": "3", "text": "Compliance systems"},
    "4": {"level": "0", "classId": "4", "text": "Statistical classifications"},
    "5": {"level": "0", "classId": "5", "text": "Publications and communications"},
    "6": {"level": "0", "classId": "6", "text": "Other source types"},
}


# 使用示例
def process_source(source_id: Source) -> None:
    """Process a source category."""
    category_data = SOURCE_CATEGORIES[source_id]
    print(f"Processing {category_data['text']}")


# 类型检查会通过
process_source("0")  # ✅ OK
# process_source("99")  # ❌ Type error: "99" is not in Literal
```

**优点**:
- ✅ 与TypeScript SDK一致
- ✅ 直接使用字符串ID（与JSON兼容）
- ✅ 类型检查支持
- ✅ 简单直观

**缺点**:
- ⚠️ 运行时不强制（可以传入任何字符串，只在类型检查时报错）

---

## 方案3: 简化的Enum（推荐 - 平衡方案）

```python
"""
Source classification categories.
Clean implementation using simple string Enum.
"""
from enum import StrEnum  # Python 3.11+
from typing import TypedDict


class SourceId(StrEnum):
    """Source category IDs as string enum."""

    IMAGES = "0"
    DATA_SET_FORMATS = "1"
    DATABASES = "2"
    COMPLIANCE_SYSTEMS = "3"
    STATISTICAL_CLASSIFICATIONS = "4"
    PUBLICATIONS = "5"
    OTHER = "6"


class SourceCategoryData(TypedDict):
    """Source category metadata."""
    level: str
    classId: str
    text: str


# Metadata mapping
SOURCE_CATEGORIES: dict[SourceId, SourceCategoryData] = {
    SourceId.IMAGES: {
        "level": "0",
        "classId": "0",
        "text": "Images"
    },
    SourceId.DATA_SET_FORMATS: {
        "level": "0",
        "classId": "1",
        "text": "Data set formats"
    },
    SourceId.DATABASES: {
        "level": "0",
        "classId": "2",
        "text": "Databases"
    },
    SourceId.COMPLIANCE_SYSTEMS: {
        "level": "0",
        "classId": "3",
        "text": "Compliance systems"
    },
    SourceId.STATISTICAL_CLASSIFICATIONS: {
        "level": "0",
        "classId": "4",
        "text": "Statistical classifications"
    },
    SourceId.PUBLICATIONS: {
        "level": "0",
        "classId": "5",
        "text": "Publications and communications"
    },
    SourceId.OTHER: {
        "level": "0",
        "classId": "6",
        "text": "Other source types"
    },
}


# 使用示例
def process_source(source: SourceId | str) -> None:
    """Process a source category."""
    source_id = SourceId(source) if isinstance(source, str) else source
    data = SOURCE_CATEGORIES[source_id]
    print(f"Processing {data['text']}")


# 都可以工作
process_source(SourceId.IMAGES)  # ✅ 使用enum
process_source("0")               # ✅ 使用字符串（自动转换）

# JSON序列化友好
import json
data = {"category": SourceId.IMAGES}
json.dumps(data, default=str)  # '{"category": "0"}'
```

**优点**:
- ✅ 类型安全 + 运行时验证
- ✅ JSON序列化友好（StrEnum自动转为字符串）
- ✅ 既可以用enum也可以用字符串
- ✅ 清晰的语义名称

**缺点**:
- ⚠️ 需要Python 3.11+ (或使用`str, Enum`的变通方案)

---

## 方案4: 混合方案（最灵活）

```python
"""
Source classification categories.
Hybrid approach combining Literal types with constants.
"""
from typing import Literal, TypedDict, Final


# Type-safe ID type
SourceId = Literal["0", "1", "2", "3", "4", "5", "6"]

# Semantic constants (方便使用)
class Sources:
    """Source category ID constants."""
    IMAGES: Final = "0"
    DATA_SET_FORMATS: Final = "1"
    DATABASES: Final = "2"
    COMPLIANCE_SYSTEMS: Final = "3"
    STATISTICAL_CLASSIFICATIONS: Final = "4"
    PUBLICATIONS: Final = "5"
    OTHER: Final = "6"


class SourceCategoryData(TypedDict):
    """Source category metadata."""
    level: str
    classId: str
    text: str


SOURCE_CATEGORIES: dict[SourceId, SourceCategoryData] = {
    Sources.IMAGES: {"level": "0", "classId": "0", "text": "Images"},
    Sources.DATA_SET_FORMATS: {"level": "0", "classId": "1", "text": "Data set formats"},
    Sources.DATABASES: {"level": "0", "classId": "2", "text": "Databases"},
    Sources.COMPLIANCE_SYSTEMS: {"level": "0", "classId": "3", "text": "Compliance systems"},
    Sources.STATISTICAL_CLASSIFICATIONS: {"level": "0", "classId": "4", "text": "Statistical classifications"},
    Sources.PUBLICATIONS: {"level": "0", "classId": "5", "text": "Publications and communications"},
    Sources.OTHER: {"level": "0", "classId": "6", "text": "Other source types"},
}


# 使用示例
def process_source(source_id: SourceId) -> None:
    """Process a source category."""
    data = SOURCE_CATEGORIES[source_id]
    print(f"Processing {data['text']}")


# 多种使用方式
process_source(Sources.IMAGES)  # ✅ 使用常量（清晰）
process_source("0")              # ✅ 使用字符串（灵活）
```

**优点**:
- ✅ 类型安全的Literal
- ✅ 语义清晰的常量
- ✅ JSON兼容
- ✅ 灵活使用

---

## 推荐：根据Python版本选择

### Python 3.11+
**推荐方案3（StrEnum）** - 最佳平衡

### Python 3.8-3.10
**推荐方案2（Literal + TypedDict）** - 与TypeScript一致，当前手动实现使用的方案

### 如果需要最强类型安全
**推荐方案1（复杂Enum）**

---

## 代码对比

### 当前 (❌ 问题)
```python
class Source1(BaseModel):  # 无意义的名字
    field_level: Literal['0'] = Field('0', alias='@level')
    field_classId: Literal['0'] = Field('0', alias='@classId')
    text: Literal['Images'] = Field('Images', alias='#text')

class Source2(BaseModel):  # 无意义的名字
    # ...
```

### 改进后 (✅ 清晰)
```python
# 方案2: Literal (推荐 - 与TypeScript一致)
Source = Literal["0", "1", "2", "3", "4", "5", "6"]
SOURCE_CATEGORIES: dict[str, SourceCategoryData] = {...}

# 或方案3: StrEnum (推荐 - Python 3.11+)
class SourceId(StrEnum):
    IMAGES = "0"
    DATABASES = "2"
    # ...
```

---

## 我的建议

**采用方案2（Literal + TypedDict）** 因为：
1. ✅ 与TypeScript SDK设计一致
2. ✅ Python 3.8+兼容
3. ✅ JSON序列化零成本
4. ✅ 已有手动示例（tidas_contacts_category.py）
5. ✅ 简单易懂

这正是我在SOLUTION_DESIGN.md中建议的方案！
