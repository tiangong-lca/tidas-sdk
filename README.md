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
- **Runtime Validation**: Zod-based validation with configurable modes
- **8 Entity Types**: Support for all core TIDAS entities
- **JSON Interoperability**: Seamless conversion between objects and JSON
- **Batch Operations**: Efficient processing of multiple entities
- **Multi-language Support**: Built-in support for multi-language text fields
- **Performance Optimized**: Configurable validation for performance-critical scenarios

## 📚 Examples

The `examples/` directory contains comprehensive usage examples. To run them:

```bash
cd examples
npm install
npm run run-basic  # Basic entity usage
```

See [examples/README.md](examples/README.md) for detailed information.

## 🔧 Development

This repository contains the source code for the SDK. The examples use the published npm package.

### Build Commands

```bash
npm run build          # Compile TypeScript
npm run dev            # Watch mode
npm run generate-types # Generate types from schemas
npm run test           # Run tests
npm run lint           # Lint code
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

Current version: 0.1.6

## 🔗 Links

- [npm package](https://www.npmjs.com/package/@tiangong-lca/tidas-sdk)
- [GitHub repository](https://github.com/tiangong-lca/tidas-sdk)