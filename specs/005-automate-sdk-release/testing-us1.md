# 测试文档：用户故事 1 - 自动 SDK 重新生成

**功能**: 模式更新时自动重新生成 SDK (MVP)
**日期**: 2025-11-03
**状态**: 实施完成，待测试

---

## 概述

本文档提供用户故事 1 (US1) 的详细测试指南。US1 是 MVP 功能，实现当 tidas-tools submodule 更新时自动检测变更并重新生成 Python 和 TypeScript SDK。

---

## 测试环境准备

### 前置条件

1. **GitHub Secrets 配置** (用于后续阶段):
   ```bash
   # 检查 secrets 是否配置
   gh secret list

   # 如果未配置，添加占位符
   gh secret set PYPI_API_TOKEN --body "placeholder"
   gh secret set NPM_TOKEN --body "placeholder"
   ```

2. **本地工具安装**:
   - Git
   - Python 3.12+
   - Node.js 18+
   - GitHub CLI (`gh`)

3. **仓库权限**:
   - 确保有 Actions 的读写权限
   - 确保可以推送到主分支（或有权限触发 Actions）

---

## 测试场景 1: Submodule 更新检测

**目标**: 验证系统能正确检测 tidas-tools submodule 的更新

### 测试步骤

#### 1.1 本地测试检测脚本

```bash
# 从仓库根目录执行
cd /Users/biao/Code/tidas-sdk

# 测试脚本是否可执行
chmod +x scripts/ci/detect-submodule-changes.sh
./scripts/ci/detect-submodule-changes.sh
```

**预期输出**:
```json
{
  "changed": true,
  "old_commit": "abc123...",
  "new_commit": "def456...",
  "submodule_path": "tidas-tools"
}
```

**验收标准**:
- [ ] 脚本返回有效的 JSON 格式输出
- [ ] `changed` 字段正确反映 submodule 是否变更
- [ ] commit SHA 正确显示（如果有变更）

#### 1.2 触发自动工作流

```bash
# 更新 submodule 到新 commit
cd tidas-tools
git pull origin main
cd ..

# 提交 submodule 更新
git add tidas-tools
git commit -m "test: update tidas-tools for SDK regeneration test"
git push origin main
```

**验收标准**:
- [ ] GitHub Actions 自动触发 `sdk-release.yml` 工作流
- [ ] `detect-changes` job 正确识别 submodule 变更
- [ ] 后续生成作业开始执行

#### 1.3 验证变更检测结果

```bash
# 查看最新的工作流运行
gh run list --workflow=sdk-release.yml --limit 1

# 查看详细日志
gh run view --log
```

**验收标准**:
- [ ] 工作流日志显示 "Submodule changed detected"
- [ ] `changed` 输出为 `true`
- [ ] old_commit 和 new_commit 正确显示

---

## 测试场景 2: SDK 生成完整性

**目标**: 验证 Python 和 TypeScript SDK 都能成功重新生成

### 测试步骤

#### 2.1 本地测试 Python SDK 生成

```bash
# 测试 Python 生成脚本
chmod +x scripts/ci/generate-python-sdk.sh
./scripts/ci/generate-python-sdk.sh

# 检查生成的文件
ls -la sdks/python/src/tidas_sdk/
```

**预期输出**:
```
================================================================================
Python SDK Generation Summary
================================================================================
Timestamp:        2025-11-03T10:30:00Z
Source:           ./tidas-tools
Output:           ./sdks/python/src/tidas_sdk
Generated files:  X Python files
Status:           SUCCESS
================================================================================
```

**验收标准**:
- [ ] 脚本执行成功（exit code 0）
- [ ] 生成摘要显示成功状态
- [ ] 输出目录包含生成的 Python 文件
- [ ] `__generated__.py` 文件存在且包含时间戳

#### 2.2 本地测试 TypeScript SDK 生成

```bash
# 测试 TypeScript 生成脚本
chmod +x scripts/ci/generate-typescript-sdk.sh
./scripts/ci/generate-typescript-sdk.sh

# 检查生成的文件
ls -la sdks/typescript/src/
```

**预期输出**:
```
================================================================================
TypeScript SDK Generation Summary
================================================================================
Timestamp:        2025-11-03T10:30:00Z
Source:           ./tidas-tools
Output:           ./sdks/typescript/src
TypeScript files: X files
Status:           SUCCESS
================================================================================
```

**验收标准**:
- [ ] 脚本执行成功（exit code 0）
- [ ] 生成摘要显示成功状态
- [ ] 类型检查通过或报告警告
- [ ] 输出目录包含 TypeScript 文件

#### 2.3 验证 GitHub Actions 中的生成

```bash
# 触发手动工作流（用于测试）
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=all \
  -f dry_run=false \
  -f skip_validation=true

# 等待工作流完成
gh run watch

# 查看结果
gh run view
```

**验收标准**:
- [ ] Python SDK 生成作业成功完成
- [ ] TypeScript SDK 生成作业成功完成
- [ ] Artifacts 正确上传（python-sdk-generated, typescript-sdk-generated）
- [ ] 工作流摘要显示两个 SDK 都成功生成

#### 2.4 检查生成的内容

```bash
# 下载 artifacts
gh run download <run-id>

# 检查 Python SDK artifact
ls -la python-sdk-generated/

# 检查 TypeScript SDK artifact
ls -la typescript-sdk-generated/
```

**验收标准**:
- [ ] Artifacts 包含预期的文件结构
- [ ] Python files 包含模型定义
- [ ] TypeScript files 包含类型定义和 schemas

---

## 测试场景 3: 新实体类型支持

**目标**: 验证当 submodule 包含新实体类型时，SDK 能正确生成对应的包装器

### 测试步骤

#### 3.1 模拟新实体类型添加

```bash
# 在 tidas-tools 中添加新实体类型的定义
# 注意：这需要根据实际的 tidas-tools 结构进行

cd tidas-tools
# 添加新的 schema 文件或修改现有文件
git add .
git commit -m "test: add new entity type for SDK test"
cd ..

# 提交 submodule 更新
git add tidas-tools
git commit -m "test: update submodule with new entity type"
git push origin main
```

#### 3.2 验证自动生成

```bash
# 等待工作流完成
gh run watch

# 查看生成结果
gh run view --log | grep -i "entity"
```

**验收标准**:
- [ ] 工作流自动触发
- [ ] Python SDK 生成包含新实体类型
- [ ] TypeScript SDK 生成包含新实体类型
- [ ] 类型定义与 schema 保持一致

---

## 测试场景 4: 手动触发工作流

**目标**: 验证手动触发工作流的各种参数组合

### 测试步骤

#### 4.1 测试选择性 SDK 生成

```bash
# 仅生成 Python SDK
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=python \
  -f dry_run=false

# 等待完成并验证
gh run watch
gh run view
```

**验收标准**:
- [ ] 仅 Python SDK 生成作业运行
- [ ] TypeScript SDK 作业被跳过
- [ ] 工作流摘要正确反映选择

```bash
# 仅生成 TypeScript SDK
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=typescript \
  -f dry_run=false
```

**验收标准**:
- [ ] 仅 TypeScript SDK 生成作业运行
- [ ] Python SDK 作业被跳过

#### 4.2 测试 Dry-run 模式

```bash
# Dry-run 模式生成所有 SDK
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=all \
  -f dry_run=true

gh run watch
gh run view
```

**验收标准**:
- [ ] 两个 SDK 生成作业都运行
- [ ] 日志显示 "DRY RUN MODE" 警告
- [ ] 没有实际文件被提交或修改
- [ ] 工作流摘要显示 dry-run 状态

#### 4.3 测试跳过验证

```bash
# 跳过验证步骤
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=all \
  -f skip_validation=true

gh run watch
```

**验收标准**:
- [ ] 生成步骤执行
- [ ] 验证步骤被跳过
- [ ] 工作流仍然成功完成

---

## 测试场景 5: 并发控制

**目标**: 验证并发控制机制防止竞态条件

### 测试步骤

#### 5.1 触发多个并发工作流

```bash
# 快速连续触发多个手动工作流
gh workflow run sdk-release-manual.yml -f sdk_selection=all &
sleep 1
gh workflow run sdk-release-manual.yml -f sdk_selection=all &
sleep 1
gh workflow run sdk-release-manual.yml -f sdk_selection=all &

# 查看运行列表
gh run list --workflow=sdk-release-manual.yml --limit 5
```

**验收标准**:
- [ ] 第一个工作流立即开始
- [ ] 后续工作流进入排队状态（pending）
- [ ] 只有一个工作流同时运行
- [ ] 排队的工作流按顺序执行

#### 5.2 验证并发组配置

查看工作流日志，确认并发控制生效：

```bash
gh run view <run-id> --log | grep -i "concurrency"
```

**验收标准**:
- [ ] 日志显示并发组信息
- [ ] 没有工作流被意外取消（cancel-in-progress: false）

---

## 测试场景 6: 错误处理

**目标**: 验证各种错误场景的处理

### 测试步骤

#### 6.1 测试 submodule 未初始化

```bash
# 模拟 submodule 未初始化
rm -rf tidas-tools/*

# 运行检测脚本
./scripts/ci/detect-submodule-changes.sh
```

**验收标准**:
- [ ] 脚本返回警告信息
- [ ] 建议运行 `git submodule update --init`

#### 6.2 测试依赖缺失

```bash
# 删除 node_modules（模拟依赖缺失）
rm -rf sdks/typescript/node_modules

# 运行生成脚本
./scripts/ci/generate-typescript-sdk.sh
```

**验收标准**:
- [ ] 脚本检测到依赖缺失
- [ ] 自动运行 `npm install`
- [ ] 继续生成流程

#### 6.3 测试工作流失败

通过手动触发一个必然失败的场景（如修改脚本使其返回错误）：

```bash
# 临时修改脚本使其失败（仅测试用）
# 然后触发工作流
gh workflow run sdk-release-manual.yml -f sdk_selection=all

# 查看失败结果
gh run view
```

**验收标准**:
- [ ] 工作流正确标记为失败
- [ ] 错误信息清晰可见
- [ ] 后续步骤被正确跳过
- [ ] 汇总作业报告失败状态

---

## 测试场景 7: 完整端到端测试

**目标**: 执行完整的自动化流程

### 测试步骤

#### 7.1 准备测试

```bash
# 确保仓库处于干净状态
git status

# 确保 submodule 已初始化
git submodule update --init --recursive
```

#### 7.2 执行完整流程

```bash
# 1. 更新 submodule
cd tidas-tools
git pull origin main
cd ..

# 2. 提交 submodule 更新
git add tidas-tools
git commit -m "test: end-to-end SDK regeneration test"

# 3. 推送并触发自动工作流
git push origin main

# 4. 监控工作流执行
gh run watch

# 5. 查看详细日志
gh run view --log

# 6. 下载生成的 artifacts
gh run download
```

**验收标准**:
- [ ] 工作流在推送后自动触发
- [ ] `detect-changes` 正确识别 submodule 变更
- [ ] Python SDK 生成成功
- [ ] TypeScript SDK 生成成功
- [ ] Artifacts 正确上传并可下载
- [ ] 工作流摘要完整且准确
- [ ] 整个流程在预期时间内完成（< 10 分钟）

---

## 回归测试清单

每次修改工作流或脚本后，运行以下快速回归测试：

- [ ] 本地运行 `detect-submodule-changes.sh` 成功
- [ ] 本地运行 `generate-python-sdk.sh` 成功
- [ ] 本地运行 `generate-typescript-sdk.sh` 成功
- [ ] 手动触发工作流（dry-run）成功
- [ ] 手动触发工作流（实际生成）成功
- [ ] 检查 GitHub Actions 页面无语法错误

---

## 性能基准测试

记录各阶段的执行时间，确保满足性能目标（< 10 分钟完整流程）：

| 阶段 | 目标时间 | 实际时间 | 状态 |
|------|---------|---------|------|
| Submodule 检测 | < 30s | _待测试_ | ⏳ |
| Python SDK 生成 | < 3min | _待测试_ | ⏳ |
| TypeScript SDK 生成 | < 3min | _待测试_ | ⏳ |
| Artifact 上传 | < 1min | _待测试_ | ⏳ |
| **总计** | **< 10min** | _待测试_ | ⏳ |

---

## 已知限制和注意事项

### MVP 阶段限制

1. **无自动验证**: 当前版本不包含自动代码质量检查（Phase 4）
2. **无自动发布**: 不会自动发布到 PyPI/npm（Phase 5）
3. **生成逻辑占位符**: Python SDK 生成逻辑为占位符，需要根据实际 tidas-tools 格式实现

### 测试环境限制

1. **GitHub Actions 额度**: 注意 GitHub Actions 免费额度（公共仓库无限，私有仓库 2000 分钟/月）
2. **Submodule 权限**: 确保 GitHub Actions 有权限访问 tidas-tools submodule
3. **Secrets 可见性**: 在 MVP 阶段，PYPI_API_TOKEN 和 NPM_TOKEN 为占位符

---

## 故障排查

### 问题 1: 工作流未触发

**可能原因**:
- Submodule 路径配置错误
- 工作流文件语法错误
- 分支名称不匹配（非 main 分支）

**解决方案**:
```bash
# 检查工作流语法
gh workflow view sdk-release.yml

# 手动触发测试
gh workflow run sdk-release-manual.yml -f sdk_selection=all -f dry_run=true
```

### 问题 2: 检测脚本失败

**可能原因**:
- Git history 不足（fetch-depth 太小）
- Submodule 未初始化
- jq 工具未安装

**解决方案**:
```bash
# 检查 fetch-depth 配置
# 确保 actions/checkout@v4 使用 fetch-depth: 2

# 本地测试
./scripts/ci/detect-submodule-changes.sh
```

### 问题 3: SDK 生成失败

**可能原因**:
- 依赖未安装
- tidas-tools 格式变更
- 生成逻辑未实现

**解决方案**:
```bash
# 本地调试
cd sdks/python
uv venv && source .venv/bin/activate
cd ../..
./scripts/ci/generate-python-sdk.sh
```

---

## 下一步计划

完成 User Story 1 测试后，准备实施：

1. **Phase 4 (US2)**: 自动化质量验证
   - 添加 ruff/mypy 验证
   - 添加 eslint/tsc 验证
   - 运行测试套件

2. **Phase 5 (US3)**: 自动化 SDK 发布
   - 版本号管理
   - 发布到 PyPI
   - 发布到 npm

---

## 测试完成标准

User Story 1 被认为通过测试，当：

- [ ] 所有 7 个测试场景都通过
- [ ] 回归测试清单全部完成
- [ ] 性能基准测试在目标范围内
- [ ] 无阻塞性 bug
- [ ] 文档已更新

---

## 测试执行记录

**测试执行日期**: _待填写_
**测试执行人**: _待填写_
**测试结果**: _待填写_
**发现的问题**: _待填写_

---

**注**: 本文档将在测试过程中持续更新。
