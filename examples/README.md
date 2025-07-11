# TIDAS TypeScript SDK Examples

This directory contains comprehensive examples demonstrating how to use the TIDAS TypeScript SDK for Life Cycle Assessment (LCA) data management. The examples are organized by complexity and use case to provide a progressive learning experience.

## 📚 Example Categories

### 01-basic-usage/
**Fundamental SDK usage patterns**
- `contact-creation.ts` - Create and manage TIDAS Contact objects
- `flow-creation.ts` - Create and manage TIDAS Flow objects  
- `process-creation.ts` - Create and manage TIDAS Process objects
- `property-access.ts` - Various property access patterns and techniques

### 02-advanced-features/
**Advanced SDK capabilities and error handling**
- `validation-modes.ts` - Different validation configurations and strategies
- `error-handling.ts` - Comprehensive error handling patterns and recovery
- `multi-language.ts` - Multi-language text handling and internationalization
- `object-utilities.ts` - Advanced object manipulation utilities

### 03-integration/
**Real-world workflows and object integration**
- `complete-workflow.ts` - End-to-end LCA workflow with multiple objects
- `multiple-objects.ts` - Working with related TIDAS objects
- `data-conversion.ts` - JSON conversion and data transformation

### 04-performance/
**Performance optimization and debugging**
- `debugging.ts` - Debug tools, logging, and troubleshooting techniques
- `performance-tips.ts` - Performance optimization strategies
- `large-datasets.ts` - Handling large datasets efficiently

## 🚀 Getting Started

### Prerequisites
- Node.js 14.0 or higher
- TypeScript knowledge
- Basic understanding of LCA concepts

### Running Examples

All examples can be run directly with tsx:

```bash
# Install dependencies (from project root)
npm install

# Run a specific example
npx tsx examples/01-basic-usage/contact-creation.ts

# Or make executable and run directly
chmod +x examples/01-basic-usage/contact-creation.ts
./examples/01-basic-usage/contact-creation.ts
```

### Recommended Learning Path

1. **Start with basics**: `01-basic-usage/contact-creation.ts`
2. **Learn property access**: `01-basic-usage/property-access.ts`
3. **Explore flows and processes**: `01-basic-usage/flow-creation.ts`, `process-creation.ts`
4. **Master validation**: `02-advanced-features/validation-modes.ts`
5. **Handle errors**: `02-advanced-features/error-handling.ts`
6. **See real workflow**: `03-integration/complete-workflow.ts`
7. **Debug and optimize**: `04-performance/debugging.ts`

## 🔧 Key SDK Features Demonstrated

### Core Functionality
- ✅ **Factory Functions**: Type-safe object creation with `createZodContact()`, `createZodFlow()`, etc.
- ✅ **Zod Proxy System**: Intuitive property access with `obj.field.subfield = value`
- ✅ **Runtime Validation**: Automatic validation with detailed error reporting
- ✅ **Helper Functions**: UUID generation, timestamps, multi-language text

### Advanced Features
- ✅ **Validation Modes**: Strict, lenient, and custom validation configurations
- ✅ **Error Recovery**: Automatic error correction and graceful failure handling
- ✅ **Object Utilities**: Deep cloning, merging, and path-based manipulation
- ✅ **Access Logging**: Detailed operation tracking for debugging

### Integration Capabilities
- ✅ **Multi-Object Workflows**: Complete LCA workflows with object relationships
- ✅ **UUID References**: Proper linking between related TIDAS objects
- ✅ **Data Export**: JSON serialization and dataset export
- ✅ **Metadata Management**: Provenance tracking and administrative information

### Performance & Debugging
- ✅ **Performance Profiling**: Operation timing and optimization techniques
- ✅ **Memory Analysis**: Memory usage patterns and optimization
- ✅ **Debug Tools**: Comprehensive debugging utilities and techniques
- ✅ **State Inspection**: Internal proxy state analysis and troubleshooting

## 📖 Example Descriptions

### Basic Usage Examples

#### contact-creation.ts
Demonstrates creating a TIDAS Contact object representing a person or organization involved in LCA data creation. Shows:
- Factory function usage
- Property initialization and structure setup
- Helper functions (UUID generation, timestamps, multi-language text)
- Validation and object building

#### flow-creation.ts
Shows how to create TIDAS Flow objects representing materials or energy flows in LCA studies. Covers:
- Flow identification and naming
- Chemical identification (CAS numbers)
- Classification and properties
- Quantitative reference setup

#### process-creation.ts
Demonstrates creating TIDAS Process objects representing unit processes or systems. Includes:
- Process identification and classification
- Geography and technology description
- Exchange modeling (inputs and outputs)
- Reference flow and functional unit setup

#### property-access.ts
Comprehensive guide to property access patterns in the SDK:
- Direct property assignment and retrieval
- Multi-language text handling
- Array access and manipulation
- Conditional and safe property access
- Performance optimization techniques

### Advanced Features Examples

#### validation-modes.ts
Explores different validation strategies and configurations:
- Strict validation (throws on error)
- Lenient validation (logs warnings)
- Custom validation configuration
- Incremental validation best practices
- Performance impact analysis

#### error-handling.ts
Comprehensive error handling and recovery patterns:
- Validation error analysis and categorization
- Safe property access techniques
- Type coercion error handling
- Automatic error correction strategies
- Custom error types and monitoring

### Integration Examples

#### complete-workflow.ts
End-to-end LCA workflow demonstrating:
- Creating all major TIDAS object types
- Establishing relationships through UUID references
- Building a complete steel production dataset
- Cross-object validation and consistency
- Dataset export and serialization

### Performance Examples

#### debugging.ts
Comprehensive debugging tools and techniques:
- Access logging and operation analysis
- Internal state inspection
- Validation debugging strategies
- Performance profiling
- Memory usage analysis
- Advanced debugging utilities

## 🛠️ Common Patterns

### Object Creation Pattern
```typescript
// 1. Create object using factory function
const result = createZodContact({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

// 2. Get proxy for property access
const contact = result.proxy;

// 3. Initialize required structure
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;
// ... more initialization

// 4. Set properties using direct access
contact.contactDataSet.contactInformation.dataSetInformation.email = 'user@example.com';

// 5. Use helper functions
result.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
result.setMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'Contact Name', 'en');

// 6. Build and validate
const finalObject = result.buildObject();
const validation = result.validate();
```

### Error Handling Pattern
```typescript
// Safe property access
const email = contact.contactDataSet?.contactInformation?.dataSetInformation?.email || 'No email';

// Validation with error analysis
const validation = result.validate();
if (!validation.success) {
  validation.error?.issues.forEach((issue: any) => {
    console.log(`Error: ${issue.message} at ${issue.path.join('.')}`);
  });
}

// Try-catch for operations
try {
  // Potentially failing operation
  result.someOperation();
} catch (error) {
  console.log('Operation failed:', (error as Error).message);
}
```

### Multi-Object Integration Pattern
```typescript
// 1. Create all required objects
const contactResult = createZodContact();
const flowResult = createZodFlow();
const processResult = createZodProcess();

// 2. Set up each object
// ... object initialization and data setting

// 3. Create relationships using UUIDs
const contactUUID = contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'];
process.processDataSet.administrativeInformation.dataEntryBy['common:referenceToPersonOrEntityEnteringTheData'] = {
  '@refObjectId': contactUUID,
  '@type': 'contact data set',
  '@version': '1.0'
};

// 4. Validate all objects
const allValid = [contactResult, flowResult, processResult].every(result => 
  result.validate().success
);
```

## 🎯 Learning Objectives

By working through these examples, you will learn to:

1. **Master Basic Operations**
   - Create TIDAS objects using factory functions
   - Access and modify properties using the proxy system
   - Use helper functions for common operations
   - Validate objects and handle validation results

2. **Handle Complex Scenarios**
   - Configure validation modes for different use cases
   - Implement comprehensive error handling
   - Work with multi-language content
   - Optimize performance for large datasets

3. **Build Real Workflows**
   - Create complete LCA datasets with multiple object types
   - Establish proper relationships between objects
   - Export and serialize data for external use
   - Maintain data quality and consistency

4. **Debug and Optimize**
   - Use debugging tools to troubleshoot issues
   - Profile performance and identify bottlenecks
   - Monitor memory usage and optimize for efficiency
   - Implement comprehensive logging and monitoring

## 🔍 Troubleshooting

### Common Issues

1. **Type Errors**: The SDK uses strict TypeScript types. Use `as any` for dynamic properties when needed.
2. **Validation Failures**: Check the validation error details for specific issues and required fields.
3. **Property Access**: Ensure proper structure initialization before setting nested properties.
4. **Performance**: Disable logging for production use and large datasets.

### Getting Help

- Check the validation error messages for specific guidance
- Use the `debug()` method to inspect internal state
- Enable logging to trace property access patterns
- Refer to the TIDAS schema documentation for data structure requirements

## 📚 Additional Resources

- **TIDAS Schema Documentation**: Official TIDAS/ILCD schema specifications
- **SDK API Documentation**: Generated TypeScript documentation
- **LCA Methodology**: Background on Life Cycle Assessment concepts
- **TypeScript Handbook**: For TypeScript-specific questions

## 🤝 Contributing

Found an issue or have an improvement suggestion for the examples?
- Open an issue in the project repository
- Submit a pull request with improvements
- Share your own example implementations

---

**Happy coding with TIDAS TypeScript SDK!** 🚀