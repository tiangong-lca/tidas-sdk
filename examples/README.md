# TIDAS SDK Examples

This directory contains examples demonstrating how to use the published `@tiangong-lca/tidas-sdk` npm package.

## Setup

The examples use the published npm package instead of the local source code. To run the examples:

1. **Install dependencies** (from the examples directory):

   ```bash
   cd examples
   npm install
   ```

2. **Run individual examples**:

   ```bash
   # Basic entity usage
   npm run run-basic

   # Validation configuration demo
   npm run run-validation

   # Advanced usage patterns
   npm run run-advanced

   # Validation modes demo
   npm run run-validation-modes
   ```

## Example Categories

### 01-basic-usage/

- **entities-usage.ts**: Complete demonstration of all 8 TIDAS entity types
- **validation-config-demo.ts**: Basic validation configuration examples

### 02-advanced-features/

- **advanced-usage-patterns.ts**: Advanced patterns including batch operations, JSON import/export, entity relationships, and performance testing

### 03-validation-modes/

- **validation-config-demo.ts**: Comprehensive validation configuration demo with strict/weak/ignore modes

## Key Features Demonstrated

- ✅ **Entity Creation**: All 8 TIDAS entity types (Contact, Flow, Process, Source, FlowProperty, UnitGroup, LCIAMethod, LifeCycleModel)
- ✅ **Validation Modes**: Strict, weak, and ignore validation with configuration options
- ✅ **Batch Operations**: Creating and processing multiple entities efficiently
- ✅ **JSON Interoperability**: Converting between objects and JSON
- ✅ **Entity Relationships**: Building related entities with proper references
- ✅ **Multi-language Support**: Working with multi-language text fields
- ✅ **Performance Optimization**: Validation configuration for performance-critical scenarios
- ✅ **Global Configuration**: Managing validation settings globally and per-entity

## Package Structure

The examples import from the published package using these entry points:

```typescript
// Core functionality (entities, factories, validation)
import { createContact, createFlow } from '@tiangong-lca/tidas-sdk/core';

// Type definitions
import { Contact, Flow } from '@tiangong-lca/tidas-sdk/types';

// Zod schemas (if needed)
import { ContactSchema } from '@tiangong-lca/tidas-sdk/schemas';

// Utilities (if needed)
import { objectUtils } from '@tiangong-lca/tidas-sdk/utils';
```

## Development Notes

- These examples use the published npm package, not the local source code
- The examples directory has its own `package.json` and dependencies
- TypeScript execution is handled by `tsx` for direct `.ts` file execution
- All examples are self-contained and can be run independently

## Troubleshooting

If you encounter issues:

1. **Ensure you're in the examples directory**: `cd examples`
2. **Install dependencies**: `npm install`
3. **Check package version**: Ensure `@tiangong-lca/tidas-sdk` version matches your needs
4. **TypeScript errors**: The examples use the published types, ensure they're compatible

## Contributing

When adding new examples:

1. Use imports from `@tiangong-lca/tidas-sdk/*` (not relative paths)
2. Add appropriate npm scripts to `package.json`
3. Include comprehensive comments explaining the demonstrated features
4. Test examples work with the published package version
