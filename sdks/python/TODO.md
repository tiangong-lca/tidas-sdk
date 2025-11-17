# Python SDK TODO

> 目标：基于自研生成器构建具备 `sdks/python/examples/usage.py` 中六大特性的 SDK。

## 已完成

- [x] 初始化 `tidas_sdk` 包目录结构（`core/`, `entities/`, `generated/`, `xml/`）
- [x] 多语言工具 `MultiLangList` 及递归包装工具
- [x] `TidasBaseModel`/`TidasEntity` 基类，支持“跳过验证的构造 + 后续校验”
- [x] `TidasProcess` 实体及工厂（含命名空间、UUID、时间戳和多语言默认值）
- [x] 自研生成器骨架 `sdks/python/scripts/generate_sdk.py`
- [x] 生成器增强：解析 `$defs`/`$ref`、内联对象建模、枚举/Union 映射、MultiLang 自动识别
- [x] CI 入口脚本 `scripts/ci/generate-python-sdk.sh`
- [x] JSON Schema 校验：`TidasEntity.validate(mode=...)` 支持 Pydantic/JSON Schema 双模式
- [x] XML 序列化：`dataset_to_xml` 递归处理属性/文本/多语言列表
- [x] 工厂函数增强：Process 支持 `from_json`、批量创建、可配置验证模式

## 待完成

1. **Schema 解析增强（进阶）**
   - 支持 `allOf`/`anyOf` 等组合体的字段继承与属性合并
   - 识别 `patternProperties`、复杂 `additionalProperties` 并映射为 `dict[str, T]`
   - 根据约束（min/max、pattern）生成更丰富的 `Field(...)` 参数或 `Annotated` 元信息
2. **类型映射策略（进阶）**
   - 为格式化字段（`date-time`、`uri` 等）挑选更合适的 Python 类型或 `Annotated`
   - 针对多层 Union/枚举场景实现 Literal/Enum 复用与去重
3. **实体扩展**
   - Flow/Contact/Source/FlowProperty/UnitGroup/LCIAMethod/LifeCycleModel
   - 为常用字段提供便捷方法（例如 `set_name`, `reference.flows[...]`）
4. **工厂函数完善（其余实体）**
   - 其余实体同步 `from_json`、批量创建、验证模式等便捷 API
5. **测试与示例**
   - 单元测试覆盖多语言、JSON → 对象 → JSON 循环、延迟验证
   - 更新 `examples/usage.py`，确保六大特性均可运行
6. **文档 & DevX**
   - `sdks/python/README.md` 增加生成步骤、可用 API
   - 在根 README 链接 Python 生成流程
7. **发布准备**
   - 打通 `pyproject` 里的工具链（ruff、mypy、pytest）
   - 添加 `Makefile`/npm script 入口方便本地生成
8. **CI 集成验证**
   - 在 CI 流程中调用 `scripts/ci/generate-python-sdk.sh` 以确保 schema 变更可自动生成
   - 生成后执行基础功能验证（如运行示例或关键单元测试）并输出摘要，防止生成器回归
