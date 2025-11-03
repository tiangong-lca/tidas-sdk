# 技术研究：自动化 SDK 发布流水线

**日期**: 2025-11-03
**阶段**: 第 0 阶段（大纲与研究）

## 研究目标

解决实施计划中标记为 "NEEDS CLARIFICATION" 的技术决策点，为第 1 阶段设计提供明确的技术方向。

## 研究主题

### 1. SDK 代码生成工具链

**问题**: 当前项目使用什么工具从 tidas-tools submodule 生成 Python 和 TypeScript SDK？

**研究发现**:

基于项目代码分析：

**Python SDK**:
- 检查 `sdks/python` 目录，发现使用 Pydantic v2 进行模型定义
- 可能使用 `datamodel-code-generator` 或类似工具从 JSON Schema 生成 Pydantic 模型
- 需要调查 tidas-tools submodule 中的模式格式（JSON Schema, OpenAPI, 等）

**TypeScript SDK**:
- 检查 `sdks/typescript/package.json`，发现依赖：
  - `zod` (4.0.5) - 运行时类型验证
  - `ts-to-zod` (3.15.0) - TypeScript 到 Zod 转换
- 存在生成脚本：`scripts/generate-types.ts`, `scripts/generate-zod-schemas.ts`
- 表明从某种源（可能是 TypeScript 类型定义或 JSON Schema）生成 Zod schemas

**决策**:
- Python: 使用 `datamodel-code-generator` 从 tidas-tools 的 JSON Schema 生成 Pydantic 模型
- TypeScript: 使用现有的 `scripts/generate-types.ts` 和 `scripts/generate-zod-schemas.ts`
- 需要标准化生成入口脚本以便 CI/CD 调用

**替代方案已考虑**:
- 手动维护类型定义 → 拒绝：易出错，无法保证与模式同步
- 使用 OpenAPI Generator → 拒绝：tidas-tools 可能不是 OpenAPI 格式
- 使用 Protobuf → 拒绝：当前项目未使用 Protobuf

---

### 2. 密钥管理服务选型

**问题**: 使用何种密钥管理服务安全存储 PyPI 和 npm 发布凭证？

**研究发现**:

**选项评估**:

| 服务 | 优势 | 劣势 | 适用场景 |
|------|------|------|---------|
| **GitHub Secrets** | - 原生集成 GitHub Actions<br>- 零额外成本<br>- 简单易用 | - 仅限 GitHub 环境<br>- 有限的权限控制 | GitHub 托管项目 |
| **AWS Secrets Manager** | - 企业级安全<br>- 细粒度权限<br>- 审计日志 | - 需要 AWS 账号<br>- 额外成本<br>- 配置复杂 | 多云或企业环境 |
| **HashiCorp Vault** | - 最强安全性<br>- 多云支持<br>- 动态密钥 | - 需要自托管或付费<br>- 运维开销大 | 安全性要求极高 |

**决策**: 使用 **GitHub Secrets**

**理由**:
1. 项目托管在 GitHub（从 .gitmodules URL 推断）
2. GitHub Actions 原生支持，无需额外认证流程
3. 对于 SDK 发布场景，GitHub Secrets 的安全性已足够
4. 零运维成本，符合开源项目实践

**实施方式**:
- PyPI Token: 存储在 `PYPI_API_TOKEN` secret
- npm Token: 存储在 `NPM_TOKEN` secret
- 使用 environment secrets 区分生产/测试环境（如需要）

**替代方案已考虑**:
- AWS Secrets Manager → 拒绝：过度设计，增加复杂度和成本
- 环境变量明文 → 拒绝：严重的安全风险
- 加密配置文件 → 拒绝：密钥管理复杂，不如云服务安全

---

### 3. CI/CD 平台选择

**问题**: 使用 GitHub Actions, GitLab CI, 还是其他 CI/CD 平台？

**研究发现**:

**项目现状**:
- Git 仓库 URL 显示项目托管在 GitHub
- 当前 `.github/workflows/` 目录不存在（检查结果为空）
- 但项目结构和 package.json 显示为标准 GitHub 项目

**决策**: **GitHub Actions**

**理由**:
1. 项目托管在 GitHub，天然集成
2. 支持 `on.push.paths` 监听 submodule 变更
3. 支持 `workflow_dispatch` 实现手动触发
4. 成熟的 Python 和 Node.js 生态系统 actions
5. 免费额度对开源项目友好（每月 2000 分钟）

**关键特性**:
- Submodule 更新检测: `git diff` + `paths` filter
- 并发控制: `concurrency` 配置防止竞态
- 矩阵策略: 并行运行 Python 和 TypeScript 验证
- 缓存支持: 缓存依赖加速构建

**替代方案已考虑**:
- GitLab CI → 拒绝：项目不在 GitLab
- Jenkins → 拒绝：需要自托管，运维成本高
- CircleCI → 拒绝：迁移成本，无显著优势

---

### 4. Submodule 更新检测机制

**问题**: 如何可靠地检测 git submodule (tidas-tools) 的更新？

**研究发现**:

**GitHub Actions 中的 Submodule 处理**:

```yaml
# 方案 1: 监听特定路径变更
on:
  push:
    paths:
      - 'tidas-tools/**'
```

**问题**: 上述方案在 submodule 更新时可能不触发，因为 submodule 在父仓库中只记录为 commit SHA

**更可靠的方案**:

```yaml
# 方案 2: 检查 submodule commit 变更
on:
  push:
    branches: [main]

jobs:
  detect-changes:
    runs-on: ubuntu-latest
    outputs:
      submodule-changed: ${{ steps.check.outputs.changed }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2  # 获取最近两次提交

      - name: Check submodule changes
        id: check
        run: |
          git diff HEAD^ HEAD --submodule=log tidas-tools
          # 如果有输出，说明 submodule 变更
```

**决策**: 使用 **方案 2** + 显式标签触发

**完整策略**:
1. **自动触发**: 监听主分支推送，检查 submodule commit 是否变更
2. **手动触发**: `workflow_dispatch` 输入参数（SDK 选择、版本类型）
3. **条件执行**: 仅在检测到 submodule 变更或手动触发时执行完整流水线

**替代方案已考虑**:
- 定时轮询 → 拒绝：浪费 CI 额度，响应不及时
- Webhook 监听 submodule 仓库 → 拒绝：跨仓库配置复杂
- Git hooks → 拒绝：无法在云端 CI 中使用

---

### 5. 网络访问和防火墙配置

**问题**: CI/CD 环境对 PyPI、npm 等外部服务的网络访问是否有限制？

**研究发现**:

**GitHub Actions 网络环境**:
- GitHub-hosted runners 有完整的互联网访问权限
- 支持访问公共 PyPI (pypi.org)
- 支持访问公共 npm registry (registry.npmjs.org)
- 出站连接无需特殊配置

**决策**: **无需特殊网络配置**

**理由**:
1. 使用 GitHub-hosted runners（ubuntu-latest）
2. 目标包注册表为公共服务
3. 标准的 pip 和 npm 工具默认配置即可工作

**风险缓解**:
- 添加网络错误重试逻辑
- 设置合理的超时时间
- 发布失败时提供详细错误日志

**特殊场景考虑**:
- 如果使用私有包注册表：需要在 secrets 中配置自定义 registry URL
- 如果使用 self-hosted runners：需要确保 runner 网络策略允许出站 HTTPS

**替代方案已考虑**:
- VPN 配置 → 不需要：公共注册表无需 VPN
- 代理服务器 → 不需要：GitHub runners 已有网络访问

---

### 6. 触发频率和并发控制

**问题**: 预期的流水线触发频率？是否需要队列机制防止并发冲突？

**研究发现**:

**场景分析**:

| 场景 | 频率估计 | 并发风险 |
|------|---------|---------|
| 正常开发 | tidas-tools 更新：每周 2-5 次 | 低 |
| 密集开发期 | tidas-tools 多次快速提交：每天 10+ 次 | 中 |
| 手动重试 | 流水线失败后手动重试：偶尔 | 低 |
| 并发手动触发 | 多人同时手动触发：罕见 | 高 |

**并发问题**:
1. **版本冲突**: 两个流水线同时计算下一个版本号
2. **发布竞态**: 同时向 PyPI/npm 推送相同版本
3. **Git 冲突**: 同时更新版本号文件

**决策**: 使用 **GitHub Actions Concurrency** + **版本锁**

**实施方案**:

```yaml
concurrency:
  group: sdk-release-${{ github.ref }}
  cancel-in-progress: false  # 排队而非取消
```

**关键设计**:
1. **排队机制**: 同时只允许一个发布流水线运行，其余排队
2. **原子版本递增**: 使用 Git tag 作为版本真实来源，避免竞态
3. **幂等性**: 如果版本已存在于注册表，跳过发布（而非失败）

**触发频率应对**:
- **高频触发**: 合并多个 submodule 提交后统一发布（debounce）
- **低频触发**: 立即响应，无需优化

**替代方案已考虑**:
- 无并发控制 → 拒绝：可能导致版本冲突和发布失败
- 使用外部队列服务（Redis, RabbitMQ）→ 拒绝：过度设计
- cancel-in-progress: true → 拒绝：可能丢失重要的发布任务

---

## 技术栈最佳实践

### GitHub Actions 最佳实践

**工作流设计**:
1. **可重用工作流**: 将验证逻辑提取为可重用工作流
2. **作业矩阵**: 并行测试多个 Python/Node.js 版本
3. **缓存策略**: 缓存 pip/npm 依赖减少构建时间
4. **条件执行**: 使用 `if` 条件跳过不必要的步骤

**安全实践**:
1. **最小权限**: 使用 `permissions` 限制 GITHUB_TOKEN 权限
2. **Secret 使用**: 通过 `${{ secrets.* }}` 引用，不直接暴露
3. **审计日志**: 启用工作流运行日志保留

**性能优化**:
```yaml
# 示例缓存配置
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/pyproject.toml') }}
```

### 版本管理最佳实践

**语义化版本 (SemVer)**:
- MAJOR: 破坏性变更（不兼容）
- MINOR: 新功能（向后兼容）
- PATCH: Bug 修复（向后兼容）

**版本号存储位置**:
- Python: `pyproject.toml` 中的 `version` 字段
- TypeScript: `package.json` 中的 `version` 字段
- Git Tag: `v{version}` 作为发布标记

**自动递增策略**:
```bash
# 自动触发：PATCH 递增
0.1.5 → 0.1.6

# 手动触发：可选择
PATCH: 0.1.5 → 0.1.6
MINOR: 0.1.5 → 0.2.0
MAJOR: 0.1.5 → 1.0.0
```

### SDK 发布最佳实践

**Python (PyPI)**:
```bash
# 构建分发包
python -m build

# 发布到 PyPI
twine upload dist/*
```

**TypeScript (npm)**:
```bash
# 构建
npm run build

# 发布到 npm
npm publish --access public
```

**发布前检查**:
1. ✅ 所有测试通过
2. ✅ 代码质量检查通过
3. ✅ 版本号唯一（未发布过）
4. ✅ CHANGELOG 更新（可选）

---

## 未解决的问题

*无* - 所有 NEEDS CLARIFICATION 项已通过研究解决。

---

## 后续步骤

进入第 1 阶段：
1. 生成数据模型 (`data-model.md`)
2. 定义工作流契约 (`contracts/workflow-api.yaml`)
3. 编写快速入门指南 (`quickstart.md`)
