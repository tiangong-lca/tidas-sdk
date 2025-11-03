# 实施计划：自动化 SDK 发布流水线

**分支**: `005-automate-sdk-release` | **日期**: 2025-11-03 | **规格**: [spec.md](./spec.md)
**输入**: 功能规格来自 `/specs/005-automate-sdk-release/spec.md`

**注意**: 此模板由 `/speckit.plan` 命令填写。执行工作流参见 `.specify/templates/commands/plan.md`。

## 概述

当 TIDAS 模式定义（存储在 git submodule tidas-tools 中）更新时，自动触发流水线重新生成 Python 和 TypeScript SDK，执行代码质量检查和测试，并将验证通过的 SDK 发布到包注册表（PyPI 和 npm）。支持自动触发和手动触发两种模式，自动触发时递增 PATCH 版本，手动触发时可选择版本递增策略。

## 技术背景

**语言/版本**:
- Python SDK: Python 3.8+ (目标 3.12)
- TypeScript SDK: TypeScript 5.8+, Node.js 14+
- CI/CD 配置: YAML (GitHub Actions)

**主要依赖**:
- Python: pytest, mypy, ruff, pydantic>=2.0
- TypeScript: jest, eslint, typescript, prettier
- NEEDS CLARIFICATION: SDK 代码生成工具链是什么？

**存储**:
- Git submodule (tidas-tools) 作为模式定义源
- 包注册表: PyPI (Python), npm (TypeScript)
- NEEDS CLARIFICATION: 密钥管理服务选型（GitHub Secrets, AWS Secrets Manager, 等）

**测试**:
- Python: pytest (单元测试和集成测试)
- TypeScript: jest (单元测试和集成测试)
- 代码质量: mypy + ruff (Python), eslint + tsc (TypeScript)

**目标平台**:
- CI/CD 环境: NEEDS CLARIFICATION (GitHub Actions, GitLab CI, 或其他)
- 包发布目标: PyPI (公共/私有), npm registry (公共/私有)

**项目类型**: 单一仓库，多 SDK (Python + TypeScript)

**性能目标**:
- 完整流水线执行时间: <10 分钟（检测到发布完成）
- SDK 重新生成: <3 分钟
- 质量检查 + 测试: <5 分钟
- 发布阶段: <2 分钟

**约束条件**:
- 必须支持 submodule 更新检测机制
- 必须支持部分失败回滚（原子性发布）
- 必须处理并发触发（防止竞态条件）
- NEEDS CLARIFICATION: 网络访问限制和防火墙配置

**规模/范围**:
- 支持的 SDK: 2 个（Python, TypeScript）
- 预期触发频率: NEEDS CLARIFICATION（每天几次？每周？）
- 并发流水线数: NEEDS CLARIFICATION（是否需要队列机制？）

## 宪章检查

*门禁: 必须在第 0 阶段研究前通过。第 1 阶段设计后重新检查。*

**注**: 项目宪章文件 (`.specify/memory/constitution.md`) 当前为空模板，无特定原则需要验证。

**初步评估** (第 0 阶段前):
- ✅ 无违反项 - 宪章待定义
- 本功能为 CI/CD 基础设施改进，不引入新的架构复杂性
- 遵循现有项目结构（Python SDK 和 TypeScript SDK）

**第 1 阶段后重新评估**:
- ✅ 设计完成，无新的架构复杂性引入
- ✅ 使用标准 GitHub Actions 工作流，无自定义基础设施
- ✅ 脚本设计遵循单一职责原则，便于测试和维护
- ✅ 数据模型清晰，无过度抽象

**结论**: 通过宪章检查，可进入第 2 阶段（任务分解）。

## 项目结构

### 文档（本功能）

```text
specs/005-automate-sdk-release/
├── spec.md              # 功能规格
├── plan.md              # 本文件 (/speckit.plan 命令输出)
├── research.md          # 第 0 阶段输出 (/speckit.plan 命令)
├── data-model.md        # 第 1 阶段输出 (/speckit.plan 命令)
├── quickstart.md        # 第 1 阶段输出 (/speckit.plan 命令)
├── contracts/           # 第 1 阶段输出 (/speckit.plan 命令)
│   └── workflow-api.yaml   # CI/CD 工作流配置接口定义
└── tasks.md             # 第 2 阶段输出 (/speckit.tasks 命令 - 不由 /speckit.plan 创建)
```

### 源代码（仓库根目录）

```text
.github/
└── workflows/
    ├── sdk-release.yml          # 主发布工作流（自动触发）
    ├── sdk-release-manual.yml   # 手动触发工作流
    └── sdk-validation.yml       # 可重用的验证工作流

scripts/
└── ci/
    ├── detect-submodule-changes.sh    # 检测 submodule 变更
    ├── generate-python-sdk.sh         # 生成 Python SDK
    ├── generate-typescript-sdk.sh     # 生成 TypeScript SDK
    ├── bump-version.sh                # 版本号管理
    └── publish-sdk.sh                 # 发布到包注册表

sdks/
├── python/
│   ├── src/
│   ├── tests/
│   ├── pyproject.toml
│   └── .github/                 # Python SDK 特定工作流（如果需要）
│
└── typescript/
    ├── src/
    ├── tests/
    ├── package.json
    └── .github/                 # TypeScript SDK 特定工作流（如果需要）

tidas-tools/                     # Git submodule（模式定义源）
```

**结构决策**:
- 使用 **GitHub Actions** 作为 CI/CD 平台（基于现有 GitHub 仓库结构）
- CI/CD 配置文件位于 `.github/workflows/`
- 辅助脚本位于 `scripts/ci/` 目录，便于本地测试和调试
- 不修改现有 SDK 目录结构，仅添加自动化工具

## 复杂度跟踪

**无复杂度违规** - 宪章检查通过，无需额外复杂度证明。
