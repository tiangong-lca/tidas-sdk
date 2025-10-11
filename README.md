# TIDAS TypeScript SDK

[English](README.md) | [中文](README-zh.md)

A TypeScript SDK for ILCD/TIDAS data management that provides type-safe data operations for Life Cycle Assessment (LCA) data structures.

## 🚀 Quick Start

### Installation

```bash
npm install @tiangong-lca/tidas-sdk
```

### Basic Usage

```typescript
import { createContact } from '@tiangong-lca/tidas-sdk/core';

// Create a new Contact entity
const contact = createContact();

// Set multilingual name (recommended: use setText method)
contact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('Dr. Jane Smith', 'en');
contact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('Dr. Jane Smith', 'fr');

// You can also set the multilingual array directly
contact.contactDataSet.contactInformation.dataSetInformation['common:shortName'] = [
  { '@xml:lang': 'en', '#text': 'J. Smith' },
  { '@xml:lang': 'fr', '#text': 'J. Smith' },
];

// Get the name in a specific language
const enName = contact.contactDataSet.contactInformation.dataSetInformation['common:name'].getText?.('en');

// Validate the entity
const validation = contact.validate();
console.log('Valid:', validation.success);

// Convert to JSON string
const json = contact.toJSONString(2);
console.log(json);
```

## 📦 Package Structure

The SDK provides multiple entry points for different use cases:

```typescript
// Core functionality (recommended)
import { createContact, createFlow } from '@tiangong-lca/tidas-sdk/core';

// Type definitions
import { Contact, Flow } from '@tiangong-lca/tidas-sdk/types';

// Zod schemas for validation
import { ContactSchema } from '@tiangong-lca/tidas-sdk/schemas';

// Utility functions
import { objectUtils } from '@tiangong-lca/tidas-sdk/utils';

// Everything (for convenience, but larger bundle)
import * from '@tiangong-lca/tidas-sdk';
```

## 🏗️ Features

- **Type Safety**: Full TypeScript support with generated types from ILCD schemas
- **Runtime Validation**: Zod-based validation with configurable modes (strict/weak/ignore)
- **8 Entity Types**: Support for all core TIDAS entities
- **JSON Interoperability**: Seamless conversion between objects and JSON
- **Batch Operations**: Efficient processing of multiple entities
- **Multi-language Support**: Built-in support for multi-language text fields
- **Performance Optimized**: Configurable validation for performance-critical scenarios
- **AI-Powered Suggestions**: Improve data quality using TIDAS methodology rules

## 📚 Usage Guide

### 1. Creating Entities

The SDK supports all 8 TIDAS entity types:

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

// Create individual entities
const contact = createContact();
const flow = createFlow();
const process = createProcess();

// Create entities from existing data
const existingData = { /* TIDAS data structure */ };
const processWithData = createProcess(existingData);
```

### 2. Working with Multi-language Fields

TIDAS entities support multi-language text fields:

```typescript
// Using setText/getText methods (recommended)
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('Water', 'en');
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('Wasser', 'de');
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.('Eau', 'fr');

// Get text in a specific language
const englishName = flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.getText?.('en');

// Direct array assignment
flow.flowDataSet.flowInformation.dataSetInformation['common:generalComment'] = [
  { '@xml:lang': 'en', '#text': 'Pure water for industrial processes' },
  { '@xml:lang': 'de', '#text': 'Reines Wasser für industrielle Prozesse' },
  { '@xml:lang': 'fr', '#text': 'Eau pure pour les processus industriels' },
];
```

### 3. Validation Modes

The SDK provides three validation modes to balance data quality and performance:

```typescript
import {
  createProcess,
  setGlobalValidationMode,
  getGlobalValidationMode
} from '@tiangong-lca/tidas-sdk/core';

// Strict validation (default) - Full schema validation, rejects on any error
const strictProcess = createProcess({}, { mode: 'strict' });
const result = strictProcess.validate();

// Weak validation - Non-critical issues become warnings
const weakProcess = createProcess({}, { mode: 'weak', includeWarnings: true });
const enhanced = weakProcess.validateEnhanced();
console.log('Warnings:', enhanced.warnings);

// Ignore validation - Skip validation for maximum performance
const fastProcess = createProcess({}, { mode: 'ignore' });
// Always passes validation - ideal for bulk operations

// Global validation configuration
setGlobalValidationMode('weak'); // Applies to all new entities
const process = createProcess(); // Uses weak validation

// Runtime configuration changes
process.setValidationMode('strict');
console.log('Current mode:', process.getValidationConfig().mode);
```

### 4. Batch Operations

Create and process multiple entities efficiently:

```typescript
import { createFlowsBatch, createContactsBatch } from '@tiangong-lca/tidas-sdk/core';

// Create multiple entities at once
const flowsData = [
  { flowDataSet: { /* data 1 */ } },
  { flowDataSet: { /* data 2 */ } },
  { flowDataSet: { /* data 3 */ } },
];

const flows = createFlowsBatch(flowsData, { mode: 'weak' });

// Process in batch
flows.forEach((flow, index) => {
  flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.(
    `Flow ${index + 1}`,
    'en'
  );
});

// Validate all
const validationResults = flows.map(flow => flow.validate());
const successCount = validationResults.filter(r => r.success).length;
console.log(`${successCount}/${flows.length} flows are valid`);
```

### 5. JSON Operations

Convert between entities and JSON:

```typescript
// Export to JSON
const jsonString = process.toJSONString(2); // Pretty-printed with 2-space indent
const jsonObject = process.toJSON();

// Import from JSON string
import { createProcess } from '@tiangong-lca/tidas-sdk/core';

const jsonData = '{ "processDataSet": { ... } }';
const parsedData = JSON.parse(jsonData);
const importedProcess = createProcess(parsedData);

// Verify imported data
const validation = importedProcess.validate();
if (validation.success) {
  console.log('Successfully imported and validated');
}
```

### 6. Entity Cloning

Create copies of entities:

```typescript
// Clone an existing entity
const originalContact = createContact();
originalContact.contactDataSet.contactInformation.dataSetInformation['common:name'].setText?.('Dr. Alice Johnson', 'en');

const clonedContact = originalContact.clone();

// Modify the clone independently
clonedContact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Dr. Alice Johnson (Copy)' }
];

// Generate new UUID for the clone
clonedContact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] = crypto.randomUUID();
```

### 7. Entity Relationships

Build relationships between different entity types:

```typescript
// Create related entities
const massUnitGroup = createUnitGroup();
massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Mass units' }
];

const massFlowProperty = createFlowProperty();
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Mass' }
];

// Reference unit group in flow property
const unitGroupUUID = massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation['common:UUID'];
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.quantitativeReference.referenceToReferenceUnitGroup = {
  '@type': 'unit group data set',
  '@refObjectId': unitGroupUUID,
  '@version': '1.0.0',
  '@uri': '',
  'common:shortDescription': [{ '@xml:lang': 'en', '#text': 'Mass units' }],
};

// Create a flow using this flow property
const co2Flow = createFlow();
const flowPropertyUUID = massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation['common:UUID'];
co2Flow.flowDataSet.flowProperties.flowProperty = {
  '@dataSetInternalID': '0',
  referenceToFlowPropertyDataSet: {
    '@type': 'flow property data set',
    '@refObjectId': flowPropertyUUID,
    '@version': '1.0.0',
    '@uri': '',
    'common:shortDescription': [{ '@xml:lang': 'en', '#text': 'Mass' }],
  },
  meanValue: '1.0',
};
```

### 8. AI-Powered Data Improvement

Use AI to improve data quality and compliance with TIDAS methodology rules:

```typescript
import { createProcess, suggestData } from '@tiangong-lca/tidas-sdk';

// Set your OpenAI API key (required)
process.env.OPENAI_API_KEY = 'your-api-key';

// Method 1: Using entity's suggest method
const process = createProcess({ processDataSet: { /* incomplete data */ } });
const result = await process.suggest({
  outputDiffSummary: true,  // Get text diff summary
  outputDiffHTML: true,      // Get HTML diff viewer
});

console.log(result.data);        // The improved entity
console.log(result.diffSummary); // Text diff summary
console.log(result.diffHTML);    // HTML diff visualization

// Method 2: Using the suggestData service function
const improvedResult = await suggestData(
  { processDataSet: { /* data */ } },
  'process',
  {
    skipPaths: ['administrativeInformation'],  // Skip certain paths
    maxRetries: 2,                              // Retry on validation failures
    outputDiffSummary: true
  }
);

// Method 3: Batch suggestions
import { batchSuggest } from '@tiangong-lca/tidas-sdk';

const results = await batchSuggest([
  { data: processData1, type: 'process' },
  { data: flowData, type: 'flow' },
  { data: contactData, type: 'contact' }
]);
```

### 9. Validation Error Handling

Handle validation errors gracefully:

```typescript
// Basic validation
const process = createProcess();
const validation = process.validate();

if (!validation.success) {
  console.log('Validation errors:', validation.error.issues);
  validation.error.issues.forEach(issue => {
    console.log(`- ${issue.path.join('.')}: ${issue.message}`);
  });
}

// Enhanced validation with warnings
const weakProcess = createProcess({}, { mode: 'weak', includeWarnings: true });
const enhanced = weakProcess.validateEnhanced();

if (enhanced.warnings) {
  console.log('Validation warnings:');
  enhanced.warnings.forEach(warning => {
    console.log(`[${warning.severity}] ${warning.path.join('.')}: ${warning.message}`);
  });
}
```

### 10. Performance Optimization

For performance-critical scenarios:

```typescript
// Use ignore mode for bulk operations
const startTime = performance.now();
const manyFlows = createFlowsBatch(
  Array(1000).fill({}),
  { mode: 'ignore' }  // Skip validation for maximum speed
);
const endTime = performance.now();
console.log(`Created 1000 flows in ${endTime - startTime}ms`);

// Configure properties without validation overhead
manyFlows.forEach((flow, index) => {
  flow.flowDataSet.flowInformation.dataSetInformation.name.baseName.setText?.(
    `Flow ${index}`,
    'en'
  );
});

// Validate only when needed
const validationResults = manyFlows.map(f => f.validate());
```

## 📚 Examples

The `examples/` directory contains comprehensive usage examples:

- `01-basic-usage/` - Simple entity creation and basic operations
- `02-advanced-features/` - Advanced patterns including batch operations and relationships
- `03-validation-modes/` - Comprehensive validation configuration examples

To run the examples:

```bash
cd examples
npm install
npm run run-basic      # Basic entity usage
npm run run-advanced   # Advanced usage patterns
npm run run-validation # Validation configuration demo
```

See [examples/README.md](examples/README.md) for detailed information.

## 🔧 Development

This repository contains the source code for the SDK. The examples use the published npm package.

### Build Commands

```bash
npm run build               # Compile TypeScript
npm run dev                 # Watch mode
npm run generate-types      # Generate types from schemas
npm run generate-schemas    # Generate Zod schemas
npm run test                # Run tests
npm run lint                # Lint code
npm run format              # Format code
```

### Project Structure

```
tidas-typescript/
├── src/
│   ├── types/           # Generated TypeScript types (18 files)
│   ├── schemas/         # Generated Zod schemas (18 files)
│   ├── core/            # Core functionality
│   │   ├── base/        # TidasEntity base class
│   │   ├── entities/    # 8 entity classes
│   │   ├── factories/   # Factory functions
│   │   └── config/      # Validation configuration
│   ├── utils/           # Utility functions
│   └── services/        # AI suggestion service
├── examples/            # Usage examples
├── scripts/             # Code generation scripts
└── dist/               # Compiled output
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests and examples
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🏷️ Version

Current version: 0.1.16

## 🔗 Links

- [npm package](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk)
- [GitHub repository](https://github.com/tiangong-lca/tidas-sdk)

## 📖 API Reference

### Core Entities

All entity types follow the same pattern:

- `TidasContact` - Contact/organization information
- `TidasFlow` - Material or energy flows
- `TidasProcess` - Process datasets
- `TidasSource` - Literature sources
- `TidasFlowProperty` - Flow properties (e.g., mass, energy)
- `TidasUnitGroup` - Unit groups for measurements
- `TidasLCIAMethod` - LCIA methodology data
- `TidasLifeCycleModel` - Life cycle models

### Factory Functions

- `createContact(data?, config?)` - Create Contact entity
- `createFlow(data?, config?)` - Create Flow entity
- `createProcess(data?, config?)` - Create Process entity
- `createSource(data?, config?)` - Create Source entity
- `createFlowProperty(data?, config?)` - Create FlowProperty entity
- `createUnitGroup(data?, config?)` - Create UnitGroup entity
- `createLCIAMethod(data?, config?)` - Create LCIAMethod entity
- `createLifeCycleModel(data?, config?)` - Create LifeCycleModel entity

Batch factory functions:

- `createContactsBatch(dataArray, config?)` - Create multiple Contacts
- `createFlowsBatch(dataArray, config?)` - Create multiple Flows
- `createProcessesBatch(dataArray, config?)` - Create multiple Processes
- (Similar batch functions for all entity types)

### Entity Methods

All entities inherit these methods from `TidasEntity`:

- `validate()` - Validate entity data (legacy format)
- `validateEnhanced()` - Enhanced validation with warnings
- `toJSON()` - Convert to plain JavaScript object
- `toJSONString(indent?)` - Convert to JSON string
- `clone()` - Create a deep copy of the entity
- `getValue(path)` - Get nested value using dot notation
- `getValidationConfig()` - Get current validation configuration
- `setValidationMode(mode)` - Set validation mode
- `setValidationConfig(config)` - Set validation configuration
- `suggest(options?)` - AI-powered data improvement

### Validation Configuration

```typescript
interface ValidationConfig {
  mode: 'strict' | 'weak' | 'ignore';
  includeWarnings?: boolean;
}

// Global configuration functions
setGlobalValidationMode(mode: 'strict' | 'weak' | 'ignore'): void
getGlobalValidationMode(): 'strict' | 'weak' | 'ignore'
setGlobalValidationConfig(config: Partial<ValidationConfig>): void
resetGlobalConfig(): void
```

### AI Suggestion Service

```typescript
// Suggest improvements for data
suggestData(
  data: any,
  dataType: DataType,
  options?: SuggestOptions
): Promise<SuggestResult>

// Batch suggestions
batchSuggest(
  items: Array<{ data: any; type: DataType }>,
  options?: SuggestOptions
): Promise<SuggestResult[]>

// Validate API key
validateApiKey(): boolean

// Get available data types
getAvailableDataTypes(): string[]
```
