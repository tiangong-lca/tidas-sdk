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

## 待完成

1. **Schema 解析增强（进阶）**
   - 支持 `allOf`/`anyOf` 等组合体的字段继承与属性合并
   - 识别 `patternProperties`、复杂 `additionalProperties` 并映射为 `dict[str, T]`
   - 根据约束（min/max、pattern）生成更丰富的 `Field(...)` 参数或 `Annotated` 元信息
2. **类型映射策略（进阶）**
   - 为格式化字段（`date-time`、`uri` 等）挑选更合适的 Python 类型或 `Annotated`
   - 针对多层 Union/枚举场景实现 Literal/Enum 复用与去重
3. **JSON Schema 校验**
   - 将 `tidas-tools` 中原始 schema 缓存到 `tidas_sdk/schemas/`
   - 提供 `TidasEntity.validate(mode="jsonschema")`，使用 `jsonschema` 库报告详细错误
4. **XML 序列化**
   - 实现 `tidas_sdk.xml.serializer.dataset_to_xml`（可基于 `lxml` 或自写 DOM）
   - 确保 `process.to_xml()` 的 namespace/schemLocation 与 TypeScript 逻辑一致
5. **实体扩展**
   - Flow/Contact/Source/FlowProperty/UnitGroup/LCIAMethod/LifeCycleModel
   - 为常用字段提供便捷方法（例如 `set_name`, `reference.flows[...]`）
6. **工厂函数完善**
   - 支持 `from_json(str|Path)`、批量创建、`validate_on_init` 与自定义 `validation_mode`
7. **测试与示例**
   - 单元测试覆盖多语言、JSON → 对象 → JSON 循环、延迟验证
   - 更新 `examples/usage.py`，确保六大特性均可运行
8. **文档 & DevX**
   - `sdks/python/README.md` 增加生成步骤、可用 API
   - 在根 README 链接 Python 生成流程
9. **发布准备**
   - 打通 `pyproject` 里的工具链（ruff、mypy、pytest）
   - 添加 `Makefile`/npm script 入口方便本地生成
