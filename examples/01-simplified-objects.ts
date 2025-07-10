/**
 * Example: Using Simplified Objects with Schema Discovery
 *
 * This example demonstrates how to use the new simplified objects system
 * that automatically discovers field structure from Zod schemas.
 */

import { 
  SimplifiedTidasObject, 
  SchemaIntrospector, 
  UniversalTidasBuilder, 
  createSimplified, 
  buildObject, 
  registerSchema 
} from '@tidas-typescript-sdk/core';
import { ContactSchema, ProcessSchema, FlowSchema } from '@tidas-typescript-sdk/schemas';
import type { Contact, Process, Flow } from '@tidas-typescript-sdk/types';
// import type { infer as zodInfer } from 'zod';
// type ProcessType = zodInfer<typeof ProcessSchema>;

console.log('🚀 TIDAS SDK - Simplified Objects with Schema Discovery\n');

// Example 1: Register schemas for easier access
console.log('📝 1. Register Schemas');
registerSchema('contact', ContactSchema);
registerSchema('process', ProcessSchema);
registerSchema('flow', FlowSchema);
console.log('✓ Schemas registered\n');

// Example 2: Create simplified contact with schema discovery
console.log('📝 2. Create Simplified Contact with Discovery');
const simplifiedContact = createSimplified<Contact>(ContactSchema);

// Discover available fields automatically
const fields = simplifiedContact.getAvailableFields();
console.log(`📋 Discovered ${fields.length} fields:`);
fields.slice(0, 5).forEach(field => {
  console.log(`  - ${field.path} (${field.type}) ${field.required ? '[Required]' : '[Optional]'}`);
});

// Discover UUID and timestamp paths
const uuidPaths = simplifiedContact.getUUIDPaths();
const timestampPaths = simplifiedContact.getTimestampPaths();
console.log(`🔑 UUID paths: ${uuidPaths.join(', ')}`);
console.log(`⏰ Timestamp paths: ${timestampPaths.join(', ')}\n`);

// Example 3: Use discovered paths to set data
console.log('📝 3. Set Data Using Discovered Paths');
simplifiedContact
  .generateUUID(0) // Generate UUID for first discovered UUID path
  .setCurrentTimestamp(0) // Set timestamp for first discovered timestamp path
  .setMultiLangText(uuidPaths[0].replace('common:UUID', 'common:name'), 'Example Company', 'en')
  .set('contactDataSet.contactInformation.dataSetInformation.email', 'contact@example.com');

// Check completion status
const status = simplifiedContact.getCompletionStatus();
console.log(`📊 Completion: ${status.percentage}% (${status.completedFields}/${status.completedFields + status.missingRequired})`);
console.log(`✅ Ready for conversion: ${status.isReady}\n`);

// Example 4: Get suggestions for missing fields
console.log('📝 4. Get Field Suggestions');
const suggestions = simplifiedContact.getFieldSuggestions();
suggestions.slice(0, 3).forEach(suggestion => {
  console.log(`💡 ${suggestion.path}: ${suggestion.suggestion}`);
  console.log(`   Reason: ${suggestion.reason}`);
});
console.log();

// Example 5: Preview what the complete object would look like
console.log('📝 5. Preview Complete Object');
try {
  const preview = simplifiedContact.preview();
  console.log('✓ Preview generated successfully');
  console.log(`Root key: ${Object.keys(preview)[0]}`);
} catch (error) {
  console.warn('⚠ Preview failed:', error instanceof Error ? error.message : 'Unknown error');
}
console.log();

// Example 6: Convert to complete object with auto-fill
console.log('📝 6. Convert to Complete Object');
try {
  const completeContact = simplifiedContact.toComplete({
    fillMissingWithDefaults: true,
    autoGenerateUUIDs: true,
    autoGenerateTimestamps: true,
    validateOnConversion: false // Skip validation for demo
  });
  
  console.log('✓ Complete contact created successfully');
  console.log(`Contact UUID: ${completeContact.contactDataSet.contactInformation.dataSetInformation['common:UUID']}`);
} catch (error) {
  console.warn('⚠ Conversion failed:', error instanceof Error ? error.message : 'Unknown error');
}
console.log();

// Example 7: Use Universal Builder with auto-discovery
console.log('📝 7. Universal Builder with Auto-Discovery');
const contactBuilder = buildObject<Contact>('contact')
  .withUUID() // Auto-generate UUID for discovered paths
  .withTimestamp() // Auto-generate timestamp for discovered paths
  .setName('Built Company') // Smart setter that finds name fields
  .set('contactDataSet.contactInformation.dataSetInformation.email', 'built@example.com');

// Show discovered capabilities
const builderFields = contactBuilder.getAvailableFields();
const builderSuggestions = contactBuilder.getSuggestions();
console.log(`🔍 Builder discovered ${builderFields.length} fields`);
console.log(`💡 Builder has ${builderSuggestions.length} suggestions`);

try {
  const builtContact = contactBuilder.buildComplete({
    fillMissingWithDefaults: true,
    validateOnConversion: false
  });
  console.log('✓ Contact built successfully via Universal Builder');
} catch (error) {
  console.warn('⚠ Builder failed:', error instanceof Error ? error.message : 'Unknown error');
}
console.log();

// Example 8: Schema Introspection
console.log('📝 8. Schema Introspection');
const contactFields = SchemaIntrospector.extractFieldsFromSchema(ContactSchema);
const contactUUIDs = SchemaIntrospector.findUUIDPaths(ContactSchema);
const contactMultiLang = SchemaIntrospector.findMultiLangPaths(ContactSchema);
const contactRoot = SchemaIntrospector.extractRootKey(ContactSchema);

console.log(`📋 Schema analysis:`);
console.log(`  - Fields: ${contactFields.length}`);
console.log(`  - UUID paths: ${contactUUIDs.length}`);
console.log(`  - Multi-lang paths: ${contactMultiLang.length}`);
console.log(`  - Root key: ${contactRoot}`);
console.log();

// Example 9: Working with other object types
console.log('📝 9. Other Object Types');

// Process object
const simplifiedProcess = createSimplified<Process>('process');
const processUUIDs = simplifiedProcess.getUUIDPaths();
console.log(`🏭 Process UUID paths: ${processUUIDs.join(', ')}`);

// Flow object  
const simplifiedFlow = createSimplified<Flow>('flow');
const flowUUIDs = simplifiedFlow.getUUIDPaths();
console.log(`🌊 Flow UUID paths: ${flowUUIDs.join(', ')}`);
console.log();

// Example 10: Validation and Error Handling
console.log('📝 10. Validation and Error Handling');
const partialContact = createSimplified<Contact>(ContactSchema);
partialContact.set('contactDataSet.contactInformation.dataSetInformation.email', 'test@example.com');

const validation = partialContact.validatePartial();
console.log(`❌ Missing required: ${validation.missingRequired.length}`);
console.log(`⚠ Invalid fields: ${validation.invalidFields.length}`);
console.log(`✅ Can convert: ${validation.canConvert}`);

if (validation.missingRequired.length > 0) {
  console.log('Missing required fields:');
  validation.missingRequired.slice(0, 3).forEach(field => {
    console.log(`  - ${field}`);
  });
}

console.log('\n🎉 Simplified Objects Demo Complete!');
console.log('\nKey Features Demonstrated:');
console.log('✅ Automatic schema discovery');
console.log('✅ Field metadata extraction');
console.log('✅ Smart path detection (UUID, timestamp, multi-lang)');
console.log('✅ Completion status tracking');
console.log('✅ Field suggestions');
console.log('✅ Universal builder with discovery');
console.log('✅ Validation and error handling');
console.log('✅ Support for all object types');