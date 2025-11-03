# 快速入门：自动化 SDK 发布流水线

**日期**: 2025-11-03
**面向对象**: 开发人员和维护者

## 概述

本指南帮助您快速了解和使用自动化 SDK 发布流水线。完成配置后，每当 `tidas-tools` submodule 更新时，流水线将自动：
1. 重新生成 Python 和 TypeScript SDK
2. 运行代码质量检查和测试
3. 发布到 PyPI 和 npm（如果验证通过）

---

## 前置要求

### 1. 环境准备

**必需工具**:
- Git
- Python 3.8+ (推荐 3.12)
- Node.js 14+
- GitHub 账号（具有仓库写权限）

**可选工具**:
- `gh` CLI (用于管理 GitHub Secrets)
- `act` (用于本地测试 GitHub Actions)

### 2. 权限配置

确保您有以下权限：
- GitHub 仓库的 **Admin** 或 **Maintain** 权限（用于配置 Secrets）
- PyPI 账号和 API token（用于发布 Python SDK）
- npm 账号和 Access token（用于发布 TypeScript SDK）

---

## 配置步骤

### 第 1 步：配置 GitHub Secrets

#### 方法 A: 使用 GitHub Web UI

1. 访问仓库 Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 添加以下 secrets:

| Name | Value | 获取方式 |
|------|-------|---------|
| `PYPI_API_TOKEN` | `pypi-...` | [创建 PyPI API Token](https://pypi.org/manage/account/token/) |
| `NPM_TOKEN` | `npm_...` | [创建 npm Access Token](https://www.npmjs.com/settings/~/tokens) |

#### 方法 B: 使用 `gh` CLI

```bash
# PyPI Token
gh secret set PYPI_API_TOKEN

# npm Token
gh secret set NPM_TOKEN
```

**验证配置**:
```bash
gh secret list
# 应显示 PYPI_API_TOKEN 和 NPM_TOKEN
```

---

### 第 2 步：初始化工作流文件

运行配置脚本创建工作流文件：

```bash
# 从仓库根目录执行
./scripts/ci/setup-workflows.sh
```

这将创建以下文件：
```
.github/workflows/
├── sdk-release.yml          # 自动触发工作流
├── sdk-release-manual.yml   # 手动触发工作流
└── sdk-validation.yml       # 可重用验证工作流
```

---

### 第 3 步：提交并推送

```bash
git add .github/workflows/ scripts/ci/
git commit -m "feat: add automated SDK release pipeline"
git push origin main
```

---

## 使用方式

### 场景 1: 自动发布（推荐）

**触发条件**: 当 `tidas-tools` submodule 更新并推送到主分支时

**步骤**:
```bash
# 1. 更新 submodule
cd tidas-tools
git pull origin main
cd ..

# 2. 提交 submodule 更新
git add tidas-tools
git commit -m "chore: update tidas-tools schema definitions"

# 3. 推送到主分支
git push origin main
```

**结果**:
- GitHub Actions 自动检测 submodule 变更
- 触发 SDK 重新生成和发布流水线
- Python 和 TypeScript SDK 版本自动递增 PATCH（如 `0.1.5` → `0.1.6`）
- 发布到 PyPI 和 npm

**监控流水线**:
```bash
# 查看最新工作流运行状态
gh run list --workflow="sdk-release.yml" --limit 1

# 查看详细日志
gh run view <run-id> --log
```

---

### 场景 2: 手动触发（用于测试或特殊发布）

**使用 GitHub Web UI**:
1. 访问 Actions → SDK Release (Manual)
2. 点击 "Run workflow"
3. 配置参数：
   - **sdk_selection**: 选择要构建的 SDK (`all`, `python`, 或 `typescript`)
   - **version_bump_python**: Python 版本递增类型 (`major`, `minor`, `patch`)
   - **version_bump_typescript**: TypeScript 版本递增类型
   - **dry_run**: 演习模式（不实际发布）
4. 点击 "Run workflow"

**使用 `gh` CLI**:
```bash
# 发布所有 SDK，Python MINOR，TypeScript PATCH
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=all \
  -f version_bump_python=minor \
  -f version_bump_typescript=patch

# 仅发布 Python SDK，MAJOR 版本
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=python \
  -f version_bump_python=major

# 演习模式（不实际发布）
gh workflow run sdk-release-manual.yml \
  -f sdk_selection=all \
  -f dry_run=true
```

---

### 场景 3: 本地测试脚本

在推送前本地测试各个脚本：

#### 测试 Submodule 变更检测
```bash
./scripts/ci/detect-submodule-changes.sh
# 输出 JSON 显示 submodule 是否变更
```

#### 测试 SDK 生成
```bash
# Python SDK
./scripts/ci/generate-python-sdk.sh
ls sdks/python/src/tidas_sdk/models/

# TypeScript SDK
./scripts/ci/generate-typescript-sdk.sh
ls sdks/typescript/src/types/
```

#### 测试版本递增
```bash
# 演习模式
./scripts/ci/bump-version.sh \
  --language python \
  --type minor \
  --dry-run

# 实际修改（谨慎！）
./scripts/ci/bump-version.sh \
  --language python \
  --type patch
```

---

## 故障排查

### 问题 1: 流水线未自动触发

**检查清单**:
- [ ] Submodule 确实有更新？运行 `git diff HEAD^ HEAD --submodule=log tidas-tools`
- [ ] 推送到了正确的分支（main）？
- [ ] 工作流文件存在且语法正确？访问 Actions 页面查看解析错误

**解决方案**:
```bash
# 手动触发验证
gh workflow run sdk-release-manual.yml -f sdk_selection=all -f dry_run=true
```

---

### 问题 2: SDK 生成失败

**可能原因**:
- tidas-tools submodule 模式格式变更
- 生成工具依赖缺失

**调试步骤**:
```bash
# 1. 本地测试生成
./scripts/ci/generate-python-sdk.sh

# 2. 检查 tidas-tools 内容
ls -la tidas-tools/

# 3. 查看详细日志
gh run view <run-id> --log | grep "generation"
```

---

### 问题 3: 验证失败（Lint 或 Test）

**常见原因**:
- 生成的代码不符合项目代码风格
- 生成的代码导致现有测试失败

**解决方案**:
```bash
# 1. 本地运行验证
cd sdks/python
pytest
ruff check .
mypy src

cd ../typescript
npm test
npm run lint
npm run typecheck

# 2. 修复代码风格问题
ruff check . --fix

# 3. 更新测试（如果需要）
```

---

### 问题 4: 发布失败

**检查清单**:
- [ ] Secrets 配置正确？运行 `gh secret list`
- [ ] Token 权限足够？PyPI token 需要 "Upload packages"，npm token 需要 "Automation"
- [ ] 版本号唯一？该版本未在 PyPI/npm 上发布过

**解决方案**:
```bash
# 重新生成 token
# PyPI: https://pypi.org/manage/account/token/
# npm: npm token create

# 更新 secret
gh secret set PYPI_API_TOKEN
gh secret set NPM_TOKEN

# 手动重试发布（需要先 bump 版本）
gh workflow run sdk-release-manual.yml -f sdk_selection=all
```

---

### 问题 5: 版本已存在

**情况**: 流水线因版本已发布而跳过

**原因**: 之前已发布相同版本，或手动发布后忘记更新版本号

**解决方案**:
```bash
# 手动递增版本号
./scripts/ci/bump-version.sh --language python --type patch
./scripts/ci/bump-version.sh --language typescript --type patch

# 提交版本更新
git add sdks/python/pyproject.toml sdks/typescript/package.json
git commit -m "chore: bump SDK versions"
git push
```

---

## 高级用法

### 自定义版本递增逻辑

修改 `scripts/ci/bump-version.sh` 实现自定义逻辑，例如：
- 根据 commit message 自动判断版本类型（feat → MINOR, fix → PATCH, BREAKING CHANGE → MAJOR）
- 读取 `CHANGELOG.md` 确定版本号

### 添加发布前审批

在工作流中添加 `environment` 配置：

```yaml
jobs:
  publish:
    environment:
      name: production
      url: https://pypi.org/project/tidas-sdk/
    steps:
      # ... 发布步骤
```

然后在 GitHub Settings → Environments → production 中配置审批者。

### 集成通知

在工作流末尾添加通知步骤：

```yaml
- name: Notify success
  if: success()
  run: |
    # 发送 Slack/Email/Discord 通知
```

---

## 最佳实践

1. **定期检查流水线日志**: 即使成功，也查看警告信息
2. **使用 dry-run 测试**: 重大变更前先演习
3. **保持 secrets 更新**: Token 定期轮换
4. **监控发布质量**: 检查发布的包是否正常工作
5. **记录版本变更**: 更新 CHANGELOG.md（可自动化）

---

## 下一步

- 阅读 [数据模型文档](./data-model.md) 了解内部结构
- 阅读 [工作流 API 契约](./contracts/workflow-api.yaml) 了解详细配置
- 查看 [实施任务列表](./tasks.md) 了解开发进度（由 `/speckit.tasks` 生成）

---

## 获取帮助

- **文档**: 查看 `specs/005-automate-sdk-release/` 目录下的所有文档
- **GitHub Issues**: 提交问题到项目 issue tracker
- **社区**: 联系项目维护者

**祝您使用愉快！** 🚀
