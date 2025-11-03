# 实施任务清单：自动化 SDK 发布流水线

**功能**: 自动化 SDK 发布流水线
**分支**: `005-automate-sdk-release`
**日期**: 2025-11-03
**文档**: [spec.md](./spec.md) | [plan.md](./plan.md) | [data-model.md](./data-model.md)

---

## 任务组织原则

本任务清单按**用户故事**组织，确保每个用户故事可以**独立实施和测试**：

- **用户故事 1 (P1)**: 模式更新时自动重新生成 SDK - 核心自动化功能
- **用户故事 2 (P2)**: 自动化质量验证 - 代码检查和测试
- **用户故事 3 (P3)**: 自动化 SDK 发布 - 发布到包注册表

**MVP 范围**: 仅实施用户故事 1 (P1) 即可提供核心价值 - 自动检测 submodule 变更并重新生成 SDK。

---

## 实施策略

### 增量交付

1. **Phase 1-2**: 建立基础设施（项目设置和共享工具）
2. **Phase 3 (US1)**: 实施 MVP - 自动重新生成功能
   - 完成后即可测试：更新 submodule → SDK 自动重新生成
3. **Phase 4 (US2)**: 增加质量保障
   - 完成后即可测试：重新生成后 → 自动验证代码质量
4. **Phase 5 (US3)**: 完成端到端自动化
   - 完成后即可测试：验证通过 → 自动发布到注册表

### 并行执行机会

- **US1 内**: 脚本 T007-T010 可并行开发（不同文件）
- **US2 内**: Python 和 TypeScript 验证工作流可并行开发
- **US3 内**: 版本递增和发布脚本可并行开发

---

## Phase 1: 项目设置

**目标**: 建立项目基础结构和配置

### 任务

- [x] T001 创建 `.github/workflows/` 目录结构
- [x] T002 创建 `scripts/ci/` 目录结构
- [x] T003 配置 GitHub Secrets 占位符（文档说明）
- [x] T004 创建 `.github/workflows/README.md` 工作流说明文档

**验收标准**:
- ✅ 目录结构符合 plan.md 中定义的项目结构
- ✅ README 文档清晰说明 GitHub Secrets 配置步骤

---

## Phase 2: 基础工具层

**目标**: 实施所有用户故事依赖的共享工具和辅助脚本

### 任务

- [x] T005 实现 Submodule 变更检测脚本 `scripts/ci/detect-submodule-changes.sh`
- [x] T006 为检测脚本添加本地测试用例（验证 JSON 输出格式）

**验收标准**:
- ✅ 脚本能正确检测 tidas-tools submodule 的 commit 变更
- ✅ 输出符合 contracts/workflow-api.yaml 定义的 JSON 格式
- ✅ 本地运行 `./scripts/ci/detect-submodule-changes.sh` 返回正确结果

**阻塞关系**: Phase 2 必须完成后才能开始 Phase 3-5（US1-US3 都依赖 submodule 检测）

---

## Phase 3: 用户故事 1 - 模式更新时自动重新生成 SDK (P1) 🎯 MVP

**用户故事**: 当 TIDAS 模式定义（存储在 git submodule 中）更新时，SDK 生成流水线自动检测变更并重新生成 Python 和 TypeScript 两个 SDK。

**独立测试标准**:
1. 更新 tidas-tools submodule 到新 commit
2. 提交并推送到主分支
3. 验证 GitHub Actions 自动触发
4. 验证 Python SDK 和 TypeScript SDK 都已重新生成
5. 检查生成的文件包含最新模式定义

### 任务

#### SDK 生成脚本 (可并行 T007-T010)

- [x] T007 [P] [US1] 实现 Python SDK 生成脚本 `scripts/ci/generate-python-sdk.sh`
- [x] T008 [P] [US1] 为 Python 生成脚本添加错误处理和日志输出
- [x] T009 [P] [US1] 实现 TypeScript SDK 生成脚本 `scripts/ci/generate-typescript-sdk.sh`
- [x] T010 [P] [US1] 为 TypeScript 生成脚本添加错误处理和日志输出

#### GitHub Actions 工作流

- [x] T011 [US1] 创建自动触发工作流 `.github/workflows/sdk-release.yml`（基础版：仅检测和生成）
- [x] T012 [US1] 配置工作流 checkout 步骤（包含 submodules: recursive）
- [x] T013 [US1] 在工作流中集成 Submodule 变更检测步骤
- [x] T014 [US1] 添加条件执行逻辑：仅在检测到 submodule 变更时运行
- [x] T015 [US1] 添加 Python SDK 生成作业到工作流
- [x] T016 [US1] 添加 TypeScript SDK 生成作业到工作流
- [x] T017 [US1] 配置并发控制（concurrency group）防止竞态条件

#### 手动触发支持

- [x] T018 [US1] 创建手动触发工作流 `.github/workflows/sdk-release-manual.yml`
- [x] T019 [US1] 定义 workflow_dispatch 输入参数（sdk_selection, dry_run）
- [x] T020 [US1] 实现手动工作流的 SDK 生成逻辑（复用自动工作流）

#### 集成测试

- [x] T021 [US1] 编写工作流测试文档 `specs/005-automate-sdk-release/testing-us1.md`
- [ ] T022 [US1] 执行端到端测试：手动触发工作流验证 SDK 生成

**验收场景验证**:

✅ **场景 1**: Submodule 更新检测
- 更新 submodule 到新版本 → 系统检测到变更 → 触发 SDK 重新生成

✅ **场景 2**: SDK 生成完整性
- SDK 重新生成触发 → 生成过程完成 → Python 和 TypeScript SDK 都包含更新后的模式定义

✅ **场景 3**: 新实体类型支持
- Submodule 更新包含新实体类型 → SDK 重新生成 → 两个 SDK 都包含新实体类型的类型化包装器

**完成里程碑**: ✅ MVP 完成 - 自动检测和重新生成功能可用

---

## Phase 4: 用户故事 2 - 自动化质量验证 (P2)

**用户故事**: SDK 重新生成后，流水线自动运行代码检查和测试，确保生成的代码符合质量标准且不会引入回归问题。

**独立测试标准**:
1. 手动触发工作流生成 SDK
2. 验证 Python 代码检查自动运行（ruff, mypy）
3. 验证 TypeScript 代码检查自动运行（eslint, tsc）
4. 验证所有测试自动运行
5. 模拟失败：引入代码错误 → 验证流水线停止并报告错误

### 任务

#### 可重用验证工作流 (可并行 T023-T026)

- [ ] T023 [P] [US2] 创建可重用验证工作流 `.github/workflows/sdk-validation.yml`
- [ ] T024 [P] [US2] 实现 Python SDK 验证步骤（ruff + mypy linting）
- [ ] T025 [P] [US2] 实现 Python SDK 测试步骤（pytest with coverage）
- [ ] T026 [P] [US2] 实现 TypeScript SDK 验证步骤（eslint + tsc typecheck）
- [ ] T027 [P] [US2] 实现 TypeScript SDK 测试步骤（jest with coverage）

#### 验证报告

- [ ] T028 [US2] 添加验证失败时的详细错误输出（lint errors, test failures）
- [ ] T029 [US2] 配置验证报告上传为 GitHub Actions artifacts
- [ ] T030 [US2] 实现验证摘要输出（passed/failed 状态到工作流输出）

#### 集成到主工作流

- [ ] T031 [US2] 在 `sdk-release.yml` 中集成 Python 验证步骤
- [ ] T032 [US2] 在 `sdk-release.yml` 中集成 TypeScript 验证步骤
- [ ] T033 [US2] 配置验证失败时停止流水线（fail-fast）
- [ ] T034 [US2] 在 `sdk-release-manual.yml` 中添加 skip_tests 参数支持

#### 测试

- [ ] T035 [US2] 编写验证测试文档 `specs/005-automate-sdk-release/testing-us2.md`
- [ ] T036 [US2] 执行测试：引入 lint 错误 → 验证流水线失败并报告
- [ ] T037 [US2] 执行测试：引入 test 失败 → 验证流水线失败并报告
- [ ] T038 [US2] 验证 skip_tests 参数正常工作

**验收场景验证**:

✅ **场景 1**: 代码质量检查自动运行
- SDK 已重新生成 → 验证阶段开始 → Python 和 TypeScript 的代码质量检查自动运行

✅ **场景 2**: 测试自动运行
- 代码质量检查通过 → 测试阶段开始 → 两个 SDK 的所有单元测试和集成测试都执行

✅ **场景 3**: 验证失败停止流水线
- 发生代码检查或测试失败 → 验证完成 → 流水线停止并报告具体失败及可操作的错误消息

✅ **场景 4**: 验证通过继续流水线
- 所有验证通过 → 流水线继续 → 系统进入发布阶段（Phase 5 实施）

**完成里程碑**: ✅ 质量保障就位 - 只有通过验证的 SDK 才会进入发布阶段

---

## Phase 5: 用户故事 3 - 自动化 SDK 发布 (P3)

**用户故事**: 验证成功后，流水线自动将更新的 SDK 发布到各自的包注册表（PyPI 和 npm）。

**独立测试标准**:
1. 使用 dry-run 模式手动触发完整流水线
2. 验证版本号按 PATCH 规则自动递增
3. 验证 PyPI 和 npm 发布命令被调用（dry-run 不实际发布）
4. 执行真实发布到测试注册表（或使用测试账号）
5. 验证发布的包可从注册表安装

### 任务

#### 版本管理脚本 (可并行 T039-T041)

- [ ] T039 [P] [US3] 实现版本递增脚本 `scripts/ci/bump-version.sh`
- [ ] T040 [P] [US3] 添加版本号验证逻辑（SemVer 格式检查）
- [ ] T041 [P] [US3] 实现 dry-run 模式（仅输出不修改文件）

#### 发布脚本

- [ ] T042 [US3] 实现 SDK 发布脚本 `scripts/ci/publish-sdk.sh`
- [ ] T043 [US3] 添加 Python SDK 发布逻辑（twine upload）
- [ ] T044 [US3] 添加 TypeScript SDK 发布逻辑（npm publish）
- [ ] T045 [US3] 实现发布重试机制（网络错误重试 3 次）
- [ ] T046 [US3] 添加版本冲突检测（版本已存在则跳过）
- [ ] T047 [US3] 实现 dry-run 模式（仅模拟发布）

#### Git Tags 和版本跟踪

- [ ] T048 [US3] 添加 Git tag 创建逻辑到发布脚本（v{version} 格式）
- [ ] T049 [US3] 实现自动提交版本号变更到仓库

#### 集成到主工作流

- [ ] T050 [US3] 在 `sdk-release.yml` 中添加版本递增步骤
- [ ] T051 [US3] 在 `sdk-release.yml` 中添加 Python SDK 发布步骤
- [ ] T052 [US3] 在 `sdk-release.yml` 中添加 TypeScript SDK 发布步骤
- [ ] T053 [US3] 配置 GitHub Secrets 使用（PYPI_API_TOKEN, NPM_TOKEN）
- [ ] T054 [US3] 在 `sdk-release-manual.yml` 中添加版本类型选择（major/minor/patch）
- [ ] T055 [US3] 实现手动工作流的 dry-run 模式

#### 原子性和回滚

- [ ] T056 [US3] 实现原子性检查：一个 SDK 发布失败则回滚所有
- [ ] T057 [US3] 添加发布失败通知（GitHub issue 或日志警告）

#### 测试

- [ ] T058 [US3] 编写发布测试文档 `specs/005-automate-sdk-release/testing-us3.md`
- [ ] T059 [US3] 执行测试：dry-run 模式验证所有步骤
- [ ] T060 [US3] 执行测试：手动触发 MINOR 版本发布
- [ ] T061 [US3] 执行测试：自动触发完整流水线（PATCH 版本）
- [ ] T062 [US3] 验证发布的包可从 PyPI 安装
- [ ] T063 [US3] 验证发布的包可从 npm 安装

**验收场景验证**:

✅ **场景 1**: 版本号自动递增
- 所有验证通过 → 发布阶段开始 → 版本号按照语义化版本规则自动递增

✅ **场景 2**: SDK 发布到注册表
- 版本号已更新 → 发布执行 → Python 和 TypeScript SDK 发布到各自的包注册表

✅ **场景 3**: 用户可安装新版本
- 发布成功 → 过程完成 → 用户可以从包注册表安装新的 SDK 版本

✅ **场景 4**: 原子性保障
- 任何 SDK 发布失败 → 错误发生 → 系统报告失败且不发布任何其他 SDK

**完成里程碑**: ✅ 端到端自动化完成 - 从 submodule 更新到包发布的全自动流程

---

## Phase 6: 完善与跨领域关注点

**目标**: 性能优化、文档完善、错误处理增强

### 任务

#### 性能优化

- [ ] T064 [P] 配置 GitHub Actions 缓存（Python pip cache, Node.js npm cache）
- [ ] T065 [P] 优化工作流矩阵策略（如果需要测试多版本）

#### 文档

- [ ] T066 更新项目 README.md 添加自动化流水线说明
- [ ] T067 创建故障排查指南 `docs/troubleshooting-sdk-release.md`
- [ ] T068 记录 GitHub Secrets 配置步骤到 `docs/setup-secrets.md`

#### 错误处理和监控

- [ ] T069 添加工作流失败通知（GitHub issue 自动创建）
- [ ] T070 实现工作流运行摘要（发布版本、耗时统计）
- [ ] T071 添加边缘情况处理：破坏性模式变更检测警告
- [ ] T072 添加边缘情况处理：并发触发队列机制验证

#### 测试和验证

- [ ] T073 执行完整端到端测试（自动触发路径）
- [ ] T074 执行完整端到端测试（手动触发所有参数组合）
- [ ] T075 验证所有验收场景（US1-US3 共 11 个场景）
- [ ] T076 性能基准测试：验证流水线在 10 分钟内完成

---

## 任务统计

**总任务数**: 76

**按用户故事分布**:
- Phase 1 (Setup): 4 任务
- Phase 2 (Foundation): 2 任务
- Phase 3 (US1 - P1 MVP): 16 任务
- Phase 4 (US2 - P2): 16 任务
- Phase 5 (US3 - P3): 25 任务
- Phase 6 (Polish): 13 任务

**并行执行机会**:
- Phase 3: 4 个脚本任务可并行 (T007-T010)
- Phase 4: 5 个验证工作流任务可并行 (T023-T027)
- Phase 5: 3 个版本管理任务可并行 (T039-T041)
- Phase 6: 2 个缓存配置任务可并行 (T064-T065)

**总并行机会**: 14 个任务可并行执行

---

## 依赖关系图

```
Phase 1 (Setup)
  ↓
Phase 2 (Foundation: Submodule Detection)
  ↓
Phase 3 (US1: SDK Generation) ← MVP Milestone
  ↓
Phase 4 (US2: Validation)
  ↓
Phase 5 (US3: Publication)
  ↓
Phase 6 (Polish)
```

**关键路径**: Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5

**可选路径**: Phase 6 可与 Phase 5 并行开始（文档和优化不阻塞功能开发）

---

## 并行执行示例

### Phase 3 并行执行 (US1)

```
同时开始：
├─ T007: Python 生成脚本（开发者 A）
├─ T009: TypeScript 生成脚本（开发者 B）
└─ T011: 工作流文件骨架（开发者 C）

完成后串行：
T008 → T015 (Python 集成)
T010 → T016 (TypeScript 集成)
T011 → T012 → T013 → T014 → T017
```

### Phase 4 并行执行 (US2)

```
同时开始：
├─ T024-T025: Python 验证和测试（开发者 A）
└─ T026-T027: TypeScript 验证和测试（开发者 B）

完成后串行：
T023 → T028-T030 → T031-T034
```

---

## MVP 快速路径

**最小可行产品**：仅实施 Phase 1-3 (US1)

最快实现路径：
1. T001-T004: 项目设置（1 小时）
2. T005-T006: Submodule 检测（2 小时）
3. T007-T010: SDK 生成脚本（并行，4 小时）
4. T011-T020: 工作流配置（4 小时）
5. T021-T022: 测试验证（1 小时）

**预计 MVP 完成时间**: 1-2 个工作日（12-16 小时）

**MVP 验证标准**:
- ✅ Submodule 更新自动触发工作流
- ✅ Python SDK 自动重新生成
- ✅ TypeScript SDK 自动重新生成
- ✅ 手动触发工作流正常运行

---

## 实施建议

1. **优先完成 MVP (Phase 1-3)**: 快速验证核心价值
2. **增量添加验证 (Phase 4)**: 确保代码质量
3. **最后实现发布 (Phase 5)**: 完成端到端自动化
4. **持续完善 (Phase 6)**: 优化性能和用户体验

**成功标准**: 所有 11 个验收场景通过 + 性能目标达成（<10 分钟完整流水线）

---

## 附录：任务 ID 格式说明

- `T###`: 任务序号（按执行顺序）
- `[P]`: 可并行执行标记（不同文件，无依赖）
- `[US#]`: 用户故事标记（US1, US2, US3）
- 文件路径: 每个任务包含明确的文件路径，便于 LLM 直接执行

**示例**: `T007 [P] [US1] 实现 Python SDK 生成脚本 scripts/ci/generate-python-sdk.sh`
- 任务 ID: T007
- 可并行: [P]
- 属于用户故事 1: [US1]
- 文件路径: `scripts/ci/generate-python-sdk.sh`
