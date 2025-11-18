# GitHub Actions 工作流说明

本目录包含自动化 SDK 发布流水线的 GitHub Actions 工作流配置。

## 工作流列表

### 1. `sdk-release.yml` - 自动 SDK 发布工作流

**触发条件**:
- 推送到 `main` 分支且 `tidas-tools` submodule 有更新

**功能**:
- 自动检测 submodule 变更
- 重新生成 Python 和 TypeScript SDK
- 执行代码质量检查和测试
- 自动递增 PATCH 版本
- 发布到 PyPI 和 npm

### 2. `sdk-release-manual.yml` - 手动 SDK 发布工作流

**触发方式**: 手动触发（workflow_dispatch）

**输入参数**:
- `sdk_selection`: 选择要构建的 SDK (all/python/typescript)
- `version_bump_python`: Python 版本递增类型 (major/minor/patch)
- `version_bump_typescript`: TypeScript 版本递增类型 (major/minor/patch)
- `skip_tests`: 跳过测试（调试用，强制 dry-run）
- `dry_run`: 演习模式（不实际发布）

### 3. `sdk-validation.yml` - 可重用验证工作流

**用途**: 被其他工作流调用，执行 SDK 的代码质量检查和测试

**输入参数**:
- `sdk_language`: SDK 语言 (python/typescript)
- `sdk_path`: SDK 根目录路径
- `skip_tests`: 是否跳过测试

## GitHub Secrets 配置

在使用这些工作流之前，需要在仓库设置中配置以下 Secrets：

### 必需的 Secrets

#### 1. `PYPI_API_TOKEN`
- **用途**: 发布 Python SDK 到 PyPI
- **获取方式**:
  1. 登录 [PyPI](https://pypi.org/)
  2. 前往 Account Settings → API tokens
  3. 点击 "Add API token"
  4. 选择 Scope（推荐选择项目特定 scope）
  5. 复制生成的 token（格式：`pypi-...`）

#### 2. `NPM_TOKEN`
- **用途**: 发布 TypeScript SDK 到 npm
- **获取方式**:
  1. 登录 [npm](https://www.npmjs.com/)
  2. 点击头像 → Access Tokens
  3. 点击 "Generate New Token"
  4. 选择 "Automation" 类型
  5. 复制生成的 token

### 配置步骤

1. 访问仓库 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 添加上述两个 secrets：
   - Name: `PYPI_API_TOKEN`, Value: `pypi-xxxxxxxx...`
   - Name: `NPM_TOKEN`, Value: `npm_xxxxxxxx...`

### 验证配置

运行以下命令验证 secrets 已配置：

```bash
gh secret list
```

应该看到：
```
PYPI_API_TOKEN  Updated YYYY-MM-DD
NPM_TOKEN       Updated YYYY-MM-DD
```

## 本地测试

虽然 GitHub Actions 工作流在云端运行，但可以本地测试辅助脚本：

### 测试 Submodule 变更检测
```bash
./scripts/ci/detect-submodule-changes.sh
```

### 测试 SDK 生成
```bash
# Python SDK
./scripts/ci/generate-python-sdk.sh

# TypeScript SDK
./scripts/ci/generate-typescript-sdk.sh
```

### 测试版本递增（dry-run）
```bash
./scripts/ci/bump-version.sh --language python --type patch --dry-run
```

## 故障排查

### 问题 1: 工作流未自动触发

**检查**:
- Submodule 是否真的有更新？运行 `git diff HEAD^ HEAD --submodule=log tidas-tools`
- 是否推送到了 `main` 分支？

**解决方案**:
- 手动触发 `sdk-release-manual.yml` 进行测试

### 问题 2: Secrets 未找到

**错误信息**: `Error: Input required and not supplied: pypi-token`

**解决方案**:
1. 确认 secrets 已在仓库设置中配置
2. 检查 secret 名称是否正确（大小写敏感）
3. 重新生成 token 并更新 secret

### 问题 3: 权限不足

**错误信息**: `Error: Resource not accessible by integration`

**解决方案**:
1. 检查工作流文件中的 `permissions` 配置
2. 确保 `GITHUB_TOKEN` 有 `contents: write` 权限（用于创建 Git tags）

## 监控和日志

### 查看工作流运行状态
```bash
# 列出最近的工作流运行
gh run list --workflow=sdk-release.yml --limit 5

# 查看特定运行的详细日志
gh run view <run-id> --log
```

### 下载验证报告
验证失败时，可以从 Actions 页面下载 artifacts：
- `validation-report-python`
- `validation-report-typescript`

## 性能优化

### 缓存配置
工作流已配置缓存以加速构建：
- Python pip cache: `~/.cache/pip`
- Node.js npm cache: `~/.npm`

### 并发控制
使用 `concurrency` 配置防止并发执行导致的版本冲突：
```yaml
concurrency:
  group: sdk-release-${{ github.ref }}
  cancel-in-progress: false
```

## 更多信息

- **功能规格**: [specs/005-automate-sdk-release/spec.md](../../specs/005-automate-sdk-release/spec.md)
- **实施计划**: [specs/005-automate-sdk-release/plan.md](../../specs/005-automate-sdk-release/plan.md)
- **快速入门**: [specs/005-automate-sdk-release/quickstart.md](../../specs/005-automate-sdk-release/quickstart.md)
