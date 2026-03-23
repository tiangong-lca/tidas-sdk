# TIDAS TypeScript SDK

[English](README.md) | [中文](README-zh.md)

一个用于 ILCD/TIDAS 数据管理的 TypeScript SDK，为生命周期评估（LCA）数据结构提供类型安全的数据操作。

## 🚀 快速开始

### 安装

```bash
npm install @tiangong-lca/tidas-sdk
```

### 基本用法

```typescript
import { createContact } from '@tiangong-lca/tidas-sdk/core';

// 创建一个新的联系人实体
const contact = createContact();

// 设置多语言名称（推荐用 setText 方法）
contact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('张博士', 'zh');
contact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('Dr. Jane Smith', 'en');

// 也可以直接设置多语言数组
contact.contactDataSet.contactInformation.dataSetInformation['common:shortName'] = [
  { '@xml:lang': 'zh', '#text': '张博士' },
  { '@xml:lang': 'en', '#text': 'J. Smith' },
];

// 获取指定语言的名称
const zhName = contact.contactDataSet.contactInformation.dataSetInformation['common:name'].getText?.('zh');

// 校验实体
const validation = contact.validate();
console.log('数据有效:', validation.success);

// 转为 JSON 字符串
const json = contact.toJSONString(2);
console.log(json);
```

## 📦 包结构

SDK 为不同的使用场景提供了多个入口点：

```typescript
// 核心功能（推荐）
import { createContact, createFlow } from '@tiangong-lca/tidas-sdk/core';

// 类型定义
import { Contact, Flow } from '@tiangong-lca/tidas-sdk/types';

// 用于验证的 Zod 模式
import { ContactSchema } from '@tiangong-lca/tidas-sdk/schemas';

// 工具函数
import { objectUtils } from '@tiangong-lca/tidas-sdk/utils';

// 全部导入（方便但包体积较大）
import * from '@tiangong-lca/tidas-sdk';
```

## 🏗️ 功能特性

- **类型安全**：基于 ILCD 模式生成的完整 TypeScript 支持
- **运行时验证**：基于 Zod 的验证，支持可配置模式（严格/宽松/忽略）
- **8 种实体类型**：支持所有核心 TIDAS 实体
- **JSON 互操作性**：对象与 JSON 之间的无缝转换
- **批量操作**：高效处理多个实体
- **多语言支持**：内置多语言文本字段支持
- **性能优化**：为性能关键场景提供可配置验证
- **AI 驱动的建议**：使用 TIDAS 方法规则改进数据质量

## 📚 使用指南

### 1. 创建实体

SDK 支持所有 8 种 TIDAS 实体类型：

```typescript
import {
  createContact,
  createFlow,
  createProcess,
  createSource,
  createFlowProperty,
  createUnitGroup,
  createLCIAMethod,
  createLifeCycleModel,
} from '@tiangong-lca/tidas-sdk/core';

// 创建单个实体
const contact = createContact();
const flow = createFlow();
const process = createProcess();

// 从已有数据创建实体
const existingData = { /* TIDAS 数据结构 */ };
const processWithData = createProcess(existingData);
```

### 2. 使用多语言字段

TIDAS 实体支持多语言文本字段：

```typescript
// 使用 setText/getText 方法（推荐）
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('水', 'zh');
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('Water', 'en');
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('Wasser', 'de');

// 获取特定语言的文本
const chineseName = flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.getText?.('zh');

// 直接赋值数组
flow.flowDataSet.flowInformation.dataSetInformation['common:generalComment'] = [
  { '@xml:lang': 'zh', '#text': '用于工业过程的纯水' },
  { '@xml:lang': 'en', '#text': 'Pure water for industrial processes' },
  { '@xml:lang': 'de', '#text': 'Reines Wasser für industrielle Prozesse' },
];
```

### 3. 验证模式

SDK 提供三种验证模式来平衡数据质量和性能：

```typescript
import {
  createProcess,
  setGlobalValidationMode,
  getGlobalValidationMode
} from '@tiangong-lca/tidas-sdk/core';

// 严格验证（默认）- 完整的模式验证，任何错误都会拒绝
const strictProcess = createProcess({}, { mode: 'strict' });
const result = strictProcess.validate();

// 宽松验证 - 非关键问题变为警告
const weakProcess = createProcess({}, { mode: 'weak', includeWarnings: true });
const enhanced = weakProcess.validateEnhanced();
console.log('警告:', enhanced.warnings);

// 忽略验证 - 跳过验证以获得最大性能
const fastProcess = createProcess({}, { mode: 'ignore' });
// 总是通过验证 - 适合批量操作

// 全局验证配置
setGlobalValidationMode('weak'); // 应用于所有新实体
const process = createProcess(); // 使用宽松验证

// 运行时配置更改
process.setValidationMode('strict');
console.log('当前模式:', process.getValidationConfig().mode);
```

### 4. 批量操作

高效创建和处理多个实体：

```typescript
import { createFlowsBatch, createContactsBatch } from '@tiangong-lca/tidas-sdk/core';

// 一次创建多个实体
const flowsData = [
  { flowDataSet: { /* 数据 1 */ } },
  { flowDataSet: { /* 数据 2 */ } },
  { flowDataSet: { /* 数据 3 */ } },
];

const flows = createFlowsBatch(flowsData, { mode: 'weak' });

// 批量处理
flows.forEach((flow, index) => {
  flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.(
    `流 ${index + 1}`,
    'zh'
  );
});

// 批量验证
const validationResults = flows.map(flow => flow.validate());
const successCount = validationResults.filter(r => r.success).length;
console.log(`${successCount}/${flows.length} 个流有效`);
```

### 5. JSON 操作

实体与 JSON 之间的转换：

```typescript
// 导出为 JSON
const jsonString = process.toJSONString(2); // 格式化输出，2 空格缩进
const jsonObject = process.toJSON();

// 从 JSON 字符串导入
import { createProcess } from '@tiangong-lca/tidas-sdk/core';

const jsonData = '{ "processDataSet": { ... } }';
const parsedData = JSON.parse(jsonData);
const importedProcess = createProcess(parsedData);

// 验证导入的数据
const validation = importedProcess.validate();
if (validation.success) {
  console.log('成功导入并验证');
}
```

### 6. 实体克隆

创建实体的副本：

```typescript
// 克隆现有实体
const originalContact = createContact();
originalContact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('张博士', 'zh');

const clonedContact = originalContact.clone();

// 独立修改克隆体
clonedContact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'zh', '#text': '张博士（副本）' }
];

// 如需手动生成 UUID，可先从 @tiangong-lca/tidas-sdk/utils 引入 randomUUID

// 为克隆体生成新的 UUID
clonedContact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] = randomUUID();
```

### 7. 实体关系

构建不同实体类型之间的关系：

```typescript
// 创建相关实体
const massUnitGroup = createUnitGroup();
massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'zh', '#text': '质量单位' }
];

const massFlowProperty = createFlowProperty();
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'zh', '#text': '质量' }
];

// 在流属性中引用单位组
const unitGroupUUID = massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation['common:UUID'];
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.quantitativeReference.referenceToReferenceUnitGroup = {
  '@type': 'unit group data set',
  '@refObjectId': unitGroupUUID,
  '@version': '1.0.0',
  '@uri': '',
  'common:shortDescription': [{ '@xml:lang': 'zh', '#text': '质量单位' }],
};

// 创建使用此流属性的流
const co2Flow = createFlow();
const flowPropertyUUID = massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation['common:UUID'];
co2Flow.flowDataSet.flowProperties.flowProperty = {
  '@dataSetInternalID': '0',
  referenceToFlowPropertyDataSet: {
    '@type': 'flow property data set',
    '@refObjectId': flowPropertyUUID,
    '@version': '1.0.0',
    '@uri': '',
    'common:shortDescription': [{ '@xml:lang': 'zh', '#text': '质量' }],
  },
  meanValue: '1.0',
};
```

### 8. AI 驱动的数据改进

使用 AI 改进数据质量并符合 TIDAS 方法规则：

```typescript
import { createProcess, suggestData } from '@tiangong-lca/tidas-sdk';

// 设置 OpenAI API 密钥（必需）
process.env.OPENAI_API_KEY = 'your-api-key';

// 方法 1：使用实体的 suggest 方法
const process = createProcess({ processDataSet: { /* 不完整的数据 */ } });
const result = await process.suggest({
  outputDiffSummary: true,  // 获取文本差异摘要
  outputDiffHTML: true,      // 获取 HTML 差异查看器
});

console.log(result.data);        // 改进后的实体
console.log(result.diffSummary); // 文本差异摘要
console.log(result.diffHTML);    // HTML 差异可视化

// 方法 2：使用 suggestData 服务函数
const improvedResult = await suggestData(
  { processDataSet: { /* 数据 */ } },
  'process',
  {
    skipPaths: ['administrativeInformation'],  // 跳过某些路径
    maxRetries: 2,                              // 验证失败时重试
    outputDiffSummary: true
  }
);

// 方法 3：批量建议
import { batchSuggest } from '@tiangong-lca/tidas-sdk';

const results = await batchSuggest([
  { data: processData1, type: 'process' },
  { data: flowData, type: 'flow' },
  { data: contactData, type: 'contact' }
]);
```

### 9. 验证错误处理

优雅地处理验证错误：

```typescript
// 基本验证
const process = createProcess();
const validation = process.validate();

if (!validation.success) {
  console.log('验证错误:', validation.error.issues);
  validation.error.issues.forEach(issue => {
    console.log(`- ${issue.path.join('.')}: ${issue.message}`);
  });
}

// 带警告的增强验证
const weakProcess = createProcess({}, { mode: 'weak', includeWarnings: true });
const enhanced = weakProcess.validateEnhanced();

if (enhanced.warnings) {
  console.log('验证警告:');
  enhanced.warnings.forEach(warning => {
    console.log(`[${warning.severity}] ${warning.path.join('.')}: ${warning.message}`);
  });
}
```

### 10. 性能优化

对于性能关键场景：

```typescript
// 批量操作使用忽略模式
const startTime = performance.now();
const manyFlows = createFlowsBatch(
  Array(1000).fill({}),
  { mode: 'ignore' }  // 跳过验证以获得最大速度
);
const endTime = performance.now();
console.log(`创建 1000 个流耗时 ${endTime - startTime}ms`);

// 配置属性而不产生验证开销
manyFlows.forEach((flow, index) => {
  flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.(
    `流 ${index}`,
    'zh'
  );
});

// 仅在需要时验证
const validationResults = manyFlows.map(f => f.validate());
```

## 📚 示例

`examples/` 目录包含了全面的使用示例：

- `01-basic-usage/` - 简单的实体创建和基本操作
- `02-advanced-features/` - 高级模式，包括批量操作和关系
- `03-validation-modes/` - 全面的验证配置示例

运行示例：

```bash
cd examples
npm install
npm run run-basic      # 基本实体使用
npm run run-advanced   # 高级使用模式
npm run run-validation # 验证配置演示
```

详细信息请参见 [examples/README.md](examples/README.md)。

## 🔧 开发

此仓库包含 SDK 的源代码。示例使用已发布的 npm 包。

### 构建命令

```bash
npm run build               # 编译 TypeScript
npm run dev                 # 监视模式
npm run generate-types      # 从模式生成类型
npm run generate-schemas    # 生成 Zod 模式
npm run test                # 运行测试
npm run lint                # 代码检查
npm run format              # 格式化代码
```

### 项目结构

```
tidas-typescript/
├── src/
│   ├── types/           # 生成的 TypeScript 类型（18 个文件）
│   ├── schemas/         # 生成的 Zod 模式（18 个文件）
│   ├── core/            # 核心功能
│   │   ├── base/        # TidasEntity 基类
│   │   ├── entities/    # 8 个实体类
│   │   ├── factories/   # 工厂函数
│   │   └── config/      # 验证配置
│   ├── utils/           # 工具函数
│   └── services/        # AI 建议服务
├── examples/            # 使用示例
├── scripts/             # 代码生成脚本
└── dist/               # 编译输出
```

## 🤝 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 添加测试和示例
5. 提交 Pull Request

## 📄 许可证

MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件。

## 🏷️ 版本

当前版本：0.1.16

## 🔗 链接

- [npm 包](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk)
- [GitHub 仓库](https://github.com/tiangong-lca/tidas-sdk)

## 📖 API 参考

### 核心实体

所有实体类型遵循相同的模式：

- `TidasContact` - 联系人/组织信息
- `TidasFlow` - 物质或能量流
- `TidasProcess` - 过程数据集
- `TidasSource` - 文献来源
- `TidasFlowProperty` - 流属性（例如质量、能量）
- `TidasUnitGroup` - 测量单位组
- `TidasLCIAMethod` - LCIA 方法数据
- `TidasLifeCycleModel` - 生命周期模型

### 工厂函数

- `createContact(data?, config?)` - 创建联系人实体
- `createFlow(data?, config?)` - 创建流实体
- `createProcess(data?, config?)` - 创建过程实体
- `createSource(data?, config?)` - 创建来源实体
- `createFlowProperty(data?, config?)` - 创建流属性实体
- `createUnitGroup(data?, config?)` - 创建单位组实体
- `createLCIAMethod(data?, config?)` - 创建 LCIA 方法实体
- `createLifeCycleModel(data?, config?)` - 创建生命周期模型实体

批量工厂函数：

- `createContactsBatch(dataArray, config?)` - 创建多个联系人
- `createFlowsBatch(dataArray, config?)` - 创建多个流
- `createProcessesBatch(dataArray, config?)` - 创建多个过程
- （所有实体类型都有类似的批量函数）

### 实体方法

所有实体从 `TidasEntity` 继承这些方法：

- `validate()` - 验证实体数据（传统格式）
- `validateEnhanced()` - 带警告的增强验证
- `toJSON()` - 转换为普通 JavaScript 对象
- `toJSONString(indent?)` - 转换为 JSON 字符串
- `clone()` - 创建实体的深拷贝
- `getValue(path)` - 使用点表示法获取嵌套值
- `getValidationConfig()` - 获取当前验证配置
- `setValidationMode(mode)` - 设置验证模式
- `setValidationConfig(config)` - 设置验证配置
- `suggest(options?)` - AI 驱动的数据改进

### 验证配置

```typescript
interface ValidationConfig {
  mode: 'strict' | 'weak' | 'ignore';
  includeWarnings?: boolean;
}

// 全局配置函数
setGlobalValidationMode(mode: 'strict' | 'weak' | 'ignore'): void
getGlobalValidationMode(): 'strict' | 'weak' | 'ignore'
setGlobalValidationConfig(config: Partial<ValidationConfig>): void
resetGlobalConfig(): void
```

### AI 建议服务

```typescript
// 为数据建议改进
suggestData(
  data: any,
  dataType: DataType,
  options?: SuggestOptions
): Promise<SuggestResult>

// 批量建议
batchSuggest(
  items: Array<{ data: any; type: DataType }>,
  options?: SuggestOptions
): Promise<SuggestResult[]>

// 验证 API 密钥
validateApiKey(): boolean

// 获取可用的数据类型
getAvailableDataTypes(): string[]
```
