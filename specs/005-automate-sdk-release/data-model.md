# 数据模型：自动化 SDK 发布流水线

**日期**: 2025-11-03
**阶段**: 第 1 阶段（设计与契约）

## 概述

本文档定义自动化 SDK 发布流水线中涉及的关键实体、状态转换和数据流。

---

## 核心实体

### 1. PipelineExecution（流水线执行）

**描述**: 单次完整的 SDK 发布流水线运行实例

**字段**:
| 字段名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `id` | string | ✅ | 唯一标识符（GitHub run_id） |
| `trigger_type` | enum | ✅ | 触发类型：`AUTO` \| `MANUAL` |
| `trigger_source` | string | ✅ | 触发源（commit SHA 或用户名） |
| `submodule_commit` | string | ✅ | tidas-tools submodule 的 commit SHA |
| `start_time` | datetime | ✅ | 流水线开始时间 |
| `end_time` | datetime | ❌ | 流水线结束时间 |
| `status` | enum | ✅ | 状态：`PENDING` \| `RUNNING` \| `SUCCESS` \| `FAILED` \| `CANCELLED` |
| `sdk_builds` | SDKBuild[] | ✅ | 关联的 SDK 构建列表 |

**状态转换**:
```
PENDING → RUNNING → SUCCESS
              ↓
            FAILED
              ↓
          CANCELLED
```

**验证规则**:
- `trigger_type` 为 `MANUAL` 时，必须记录操作用户
- `end_time` 必须晚于 `start_time`
- 至少包含一个 `SDKBuild`

---

### 2. SDKBuild（SDK 构建）

**描述**: 单个 SDK（Python 或 TypeScript）的构建和发布过程

**字段**:
| 字段名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `id` | string | ✅ | 唯一标识符 |
| `pipeline_id` | string | ✅ | 所属流水线 ID（外键） |
| `sdk_language` | enum | ✅ | SDK 语言：`PYTHON` \| `TYPESCRIPT` |
| `version` | string | ✅ | SDK 版本号（SemVer 格式） |
| `version_bump_type` | enum | ✅ | 版本递增类型：`MAJOR` \| `MINOR` \| `PATCH` |
| `generation_status` | enum | ✅ | 生成状态 |
| `validation_report` | ValidationReport | ❌ | 验证报告 |
| `publication_status` | enum | ✅ | 发布状态 |
| `package_url` | string | ❌ | 发布后的包 URL |

**状态字段枚举**:
- **generation_status**: `PENDING` \| `GENERATING` \| `COMPLETED` \| `FAILED`
- **publication_status**: `NOT_STARTED` \| `PUBLISHING` \| `PUBLISHED` \| `FAILED` \| `SKIPPED`

**验证规则**:
- `version` 必须符合 SemVer 规范（`X.Y.Z`）
- `publication_status` 为 `PUBLISHED` 时，`package_url` 必须存在
- 同一 `pipeline_id` 内，不能有重复的 `sdk_language`

---

### 3. ValidationReport（验证报告）

**描述**: SDK 代码质量检查和测试结果

**字段**:
| 字段名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `lint_status` | enum | ✅ | 代码检查状态：`PASS` \| `FAIL` |
| `lint_errors` | LintError[] | ❌ | 代码检查错误列表 |
| `test_status` | enum | ✅ | 测试状态：`PASS` \| `FAIL` |
| `test_summary` | TestSummary | ✅ | 测试结果摘要 |
| `overall_pass` | boolean | ✅ | 总体是否通过（lint 和 test 都通过） |

**子结构 - LintError**:
| 字段名 | 类型 | 描述 |
|--------|------|------|
| `file` | string | 文件路径 |
| `line` | integer | 行号 |
| `column` | integer | 列号 |
| `rule` | string | 违反的规则 |
| `message` | string | 错误消息 |
| `severity` | enum | 严重性：`ERROR` \| `WARNING` |

**子结构 - TestSummary**:
| 字段名 | 类型 | 描述 |
|--------|------|------|
| `total` | integer | 总测试数 |
| `passed` | integer | 通过数 |
| `failed` | integer | 失败数 |
| `skipped` | integer | 跳过数 |
| `duration_seconds` | float | 测试总耗时（秒） |
| `failed_tests` | string[] | 失败的测试名称列表 |

**验证规则**:
- `overall_pass` = `(lint_status == PASS) AND (test_status == PASS)`
- `test_summary.total` = `passed + failed + skipped`

---

### 4. VersionInfo（版本信息）

**描述**: SDK 版本号及其元数据

**字段**:
| 字段名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `sdk_language` | enum | ✅ | SDK 语言 |
| `current_version` | string | ✅ | 当前版本（从 pyproject.toml/package.json 读取） |
| `next_version` | string | ✅ | 下一个版本（计算后的版本） |
| `bump_type` | enum | ✅ | 递增类型 |
| `published_at` | datetime | ❌ | 发布时间 |
| `git_tag` | string | ✅ | Git tag 名称（如 `v0.1.6`） |

**版本计算逻辑**:
```python
def calculate_next_version(current: str, bump_type: str) -> str:
    major, minor, patch = map(int, current.split('.'))

    if bump_type == 'MAJOR':
        return f"{major + 1}.0.0"
    elif bump_type == 'MINOR':
        return f"{major}.{minor + 1}.0"
    else:  # PATCH
        return f"{major}.{minor}.{patch + 1}"
```

**验证规则**:
- `current_version` 和 `next_version` 都必须符合 SemVer
- `next_version` 必须大于 `current_version`
- `git_tag` 必须匹配格式 `v{next_version}`

---

### 5. ManualTriggerInput（手动触发输入）

**描述**: 用户手动触发流水线时提供的输入参数

**字段**:
| 字段名 | 类型 | 必需 | 描述 | 默认值 |
|--------|------|------|------|--------|
| `sdk_selection` | enum[] | ✅ | 选择构建的 SDK：`PYTHON`, `TYPESCRIPT`, `ALL` | `ALL` |
| `version_bump_python` | enum | ❌ | Python SDK 版本递增类型 | `PATCH` |
| `version_bump_typescript` | enum | ❌ | TypeScript SDK 版本递增类型 | `PATCH` |
| `skip_tests` | boolean | ❌ | 是否跳过测试（调试用） | `false` |
| `dry_run` | boolean | ❌ | 是否为演习模式（不实际发布） | `false` |

**验证规则**:
- 如果 `sdk_selection` 包含 `PYTHON`，则 `version_bump_python` 必需
- 如果 `sdk_selection` 包含 `TYPESCRIPT`，则 `version_bump_typescript` 必需
- `skip_tests` 为 `true` 时，必须强制 `dry_run = true`（安全机制）

---

## 数据流

### 自动触发流程

```
1. Git Push (with submodule update)
   ↓
2. Detect submodule change
   ↓
3. Create PipelineExecution (trigger_type=AUTO)
   ↓
4. For each SDK (Python, TypeScript):
   a. Create SDKBuild (version_bump_type=PATCH)
   b. Generate SDK code
   c. Run validation → ValidationReport
   d. If validation.overall_pass:
      - Publish to registry
      - Update publication_status=PUBLISHED
   e. Else:
      - Update generation_status=FAILED
      - Stop pipeline
   ↓
5. Update PipelineExecution.status = SUCCESS/FAILED
```

### 手动触发流程

```
1. User triggers workflow with ManualTriggerInput
   ↓
2. Create PipelineExecution (trigger_type=MANUAL)
   ↓
3. For each selected SDK:
   a. Create SDKBuild with user-specified version_bump_type
   b. [Same as auto trigger steps 4b-4e]
   ↓
4. If dry_run=true:
   - Log what would be published
   - Skip actual publication
   ↓
5. Update PipelineExecution.status
```

---

## 关系图

```
PipelineExecution
    ├── 1:N → SDKBuild
    │            ├── 1:1 → ValidationReport
    │            │            ├── 0:N → LintError
    │            │            └── 1:1 → TestSummary
    │            └── 1:1 → VersionInfo
    │
    └── 0:1 → ManualTriggerInput (仅手动触发时)
```

---

## 存储与持久化

**注**: 此流水线为无状态 CI/CD 流程，不需要独立数据库。

**数据来源**:
- **输入数据**: Git 仓库、Submodule commit、用户输入
- **临时数据**: GitHub Actions 工作流运行时变量和作业输出
- **输出数据**: Git tags、包注册表、GitHub Actions 日志

**持久化位置**:
| 实体 | 持久化位置 | 查询方式 |
|------|-----------|---------|
| `PipelineExecution` | GitHub Actions run history | GitHub API/UI |
| `SDKBuild` | GitHub Actions job logs | 日志解析 |
| `ValidationReport` | Job artifacts (JSON) | 下载 artifact |
| `VersionInfo` | Git tags + package.json/pyproject.toml | Git CLI |

---

## 扩展性考虑

**未来可能的扩展**:
1. **多模式源支持**: 支持多个 submodules 或外部 API 作为模式源
2. **增量构建**: 仅重新生成变更的模块
3. **发布审批流**: 在发布前增加人工审批步骤
4. **回滚机制**: 自动回滚有问题的发布

**数据模型影响**:
- 增加 `SchemaSource` 实体（多模式源）
- `SDKBuild` 增加 `incremental` 字段
- `PipelineExecution` 增加 `approval_status` 状态
