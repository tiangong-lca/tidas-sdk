# TIDAS SDK Examples

This directory contains comprehensive examples demonstrating how to use the TIDAS TypeScript SDK for working with ILCD/Tidas data.

## Examples Overview

### 01-basic-object-creation.ts

**Basic Object Creation Patterns**

- Direct instantiation with and without data
- Factory function usage (`createContact`, `createProcess`, `createFlow`)
- Builder pattern for fluent object construction
- JSON conversion (to/from JSON)
- Object manipulation (cloning, merging, updating)
- Validation integration
- Multi-language text handling

**Key Concepts Demonstrated:**

- 10 different creation and manipulation patterns
- Type-safe object creation
- Runtime validation options
- Multi-language support
- UUID generation and management

### 02-mock-data-generation.ts

**Mock Data Generation with @anatine/zod-mock**

- Generating mock data using Zod schemas
- Creating objects with pre-filled mock data
- Customizing mock data with specific fields
- Filling missing fields in existing objects
- Performance comparison between manual and mock creation
- Combining real data with mock data
- Validation of mock-generated data

**Key Concepts Demonstrated:**

- 10 different mock generation scenarios
- Performance testing and optimization
- Schema-driven mock data generation
- Custom field injection
- Incremental data filling

## Running the Examples

To run these examples, make sure you have the TIDAS SDK properly installed and built:

```bash
# Install dependencies
npm install

# Build the SDK
npm run build

# Run TypeScript examples directly
npx tsx examples/01-basic-object-creation.ts
npx tsx examples/02-mock-data-generation.ts
```

## Example Structure

Each example is self-contained and demonstrates specific aspects of the SDK:

1. **Import statements** - Shows which parts of the SDK to import
2. **Console output** - Provides clear feedback about what's happening
3. **Error handling** - Demonstrates proper error handling patterns
4. **Multiple scenarios** - Each file contains 10+ different usage scenarios
5. **Comments and documentation** - Explains what each section does

## Key SDK Features Demonstrated

### Object Creation

- **Direct instantiation**: `new TidasContact()`
- **Factory functions**: `createContact(data)`
- **Builder pattern**: `buildContact().withName().build()`
- **Mock generation**: `TidasContact.createMock()`

### Data Manipulation

- **Deep cloning**: `contact.clone({ generateNewUUID: true })`
- **Merging**: `contact.merge(additionalData)`
- **Path-based updates**: `contact.set('path.to.field', value)`
- **Batch updates**: `contact.update({ 'field1': value1, 'field2': value2 })`

### Validation

- **Runtime validation**: `contact.validate()`
- **Validation options**: `{ enableValidation: true, throwOnValidationError: false }`
- **Type checking**: `contact.isValid()`

### Multi-language Support

- **Get text**: `contact.getMultiLangText('path', 'en')`
- **Set text**: `contact.setMultiLangText('path', 'text', 'zh')`
- **Multiple languages**: Support for 'en', 'zh', 'fr', etc.

### JSON Operations

- **Serialization**: `contact.toJSON({ pretty: true })`
- **Deserialization**: `fromJSON(jsonString, 'contact')`
- **Custom options**: `{ includeEmpty: false, excludeFields: ['@xmlns'] }`

### Mock Data Generation

- **Schema-based mocking**: Uses Zod schemas to generate realistic test data
- **Custom field injection**: Override specific fields with custom values
- **Missing field filling**: Complete partial objects with mock data
- **Performance optimization**: Compare creation methods

## Best Practices Demonstrated

1. **Type Safety**: All examples use proper TypeScript types
2. **Error Handling**: Comprehensive try-catch blocks
3. **Validation**: Show both successful and failed validation scenarios
4. **Performance**: Demonstrate efficient patterns and performance comparisons
5. **Documentation**: Clear comments explaining each concept
6. **Real-world Usage**: Practical examples that mirror actual use cases

## Next Steps

After reviewing these examples, you might want to:

1. **Explore the source code** in `src/core/` to understand the implementation
2. **Write tests** using the patterns shown in the mock generation example
3. **Build applications** using the factory functions and builder patterns
4. **Integrate validation** into your data processing pipelines
5. **Use mock data** for testing and development

## Support

For questions about these examples or the TIDAS SDK:

1. Check the main README.md in the project root
2. Review the source code documentation
3. Look at the test files in the `test/` directory
4. Consult the development documentation in `docs/`
