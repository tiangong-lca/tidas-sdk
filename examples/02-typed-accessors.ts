/**
 * Example: Using Typed Accessors for Property-Style Access
 *
 * This example demonstrates how to use the typed accessor system
 * to access interface fields as properties with full code hints.
 */

import { 
  createTypedContact, 
  createTypedProcess, 
  createTypedFlow,
  createEnhancedTypedAccessor 
} from '@tidas-typescript-sdk/core';
import type { Contact, Process, Flow } from '@tidas-typescript-sdk/types';

console.log('🚀 TIDAS SDK - Typed Accessors with IntelliSense\n');

// Example 1: Basic typed accessor usage
console.log('📝 1. Basic Typed Accessor Usage');

// Create a typed contact accessor
const contact = createEnhancedTypedAccessor<Contact>({});

// Use dot notation paths with type safety
contact.set('contactDataSet.contactInformation.dataSetInformation.common:UUID', '123e4567-e89b-12d3-a456-426614174000');
contact.set('contactDataSet.contactInformation.dataSetInformation.email', 'contact@example.com');



// Get values using paths
const contactId = contact.get('contactDataSet.contactInformation.dataSetInformation.common:UUID');
const email = contact.get('contactDataSet.contactInformation.dataSetInformation.email');

console.log(`📋 Contact ID: ${contactId}`);
console.log(`📧 Email: ${email}`);

// Error Path
contact.set('contactDataSet.contactInformation.email', 'contact@example.com');
console.log(`📧 Email: ${contact.get('contactDataSet.contactInformation.email')}`);


// Check if paths exist
const hasPhone = contact.has('contactDataSet.contactInformation.dataSetInformation.telephone');
console.log(`📞 Has phone: ${hasPhone}`);

// Get all available paths
const availablePaths = contact.getAvailablePaths();
console.log(`🔍 Available paths: ${availablePaths.length} found`);
availablePaths.slice(0, 3).forEach(path => console.log(`  - ${path}`));
console.log();

// Example 2: Multi-language text handling
console.log('📝 2. Multi-Language Text Handling');

// Create multi-language text accessor
const nameAccessor = contact.getMultiLang('contactDataSet.contactInformation.dataSetInformation.common:name');

// Set text in different languages
nameAccessor.setText('Example Company', 'en');
nameAccessor.setText('Empresa de Ejemplo', 'es');
nameAccessor.setText('公司示例', 'zh');

// Get text in specific languages
console.log(`🇺🇸 English: ${nameAccessor.getText('en')}`);
console.log(`🇪🇸 Spanish: ${nameAccessor.getText('es')}`);
console.log(`🇨🇳 Chinese: ${nameAccessor.getText('zh')}`);

// Get all available languages
const languages = nameAccessor.getLanguages();
console.log(`🌍 Available languages: ${languages.join(', ')}`);
console.log();

// Example 3: UUID and timestamp handling
console.log('📝 3. UUID and Timestamp Handling');

// Set UUID with auto-generation
contact.setUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
const generatedUUID = contact.getUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
console.log(`🆔 Generated UUID: ${generatedUUID}`);

// Set current timestamp
contact.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');
const timestamp = contact.getTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');
console.log(`⏰ Timestamp: ${timestamp}`);
console.log();

// Example 4: Object cloning
console.log('📝 4. Object Cloning');

const clonedContact = contact.clone();
clonedContact.set('contactDataSet.contactInformation.dataSetInformation.email', 'cloned@example.com');

const originalEmail = contact.get('contactDataSet.contactInformation.dataSetInformation.email');
const clonedEmail = clonedContact.get('contactDataSet.contactInformation.dataSetInformation.email');

console.log(`📧 Original email: ${originalEmail}`);
console.log(`📧 Cloned email: ${clonedEmail}`);
console.log();

// Example 5: Working with different object types
console.log('📝 5. Different Object Types');

// Create typed process accessor
const process = createEnhancedTypedAccessor<Process>({});
process.set('processDataSet.processInformation.dataSetInformation.common:UUID', '456e7890-e89b-12d3-a456-426614174000');

const processMultiLang = process.getMultiLang('processDataSet.processInformation.dataSetInformation.name.baseName');
processMultiLang.setText('Steel Production', 'en');
processMultiLang.setText('Producción de Acero', 'es');

console.log(`🏭 Process name (EN): ${processMultiLang.getText('en')}`);
console.log(`🏭 Process name (ES): ${processMultiLang.getText('es')}`);

// Error Path
process.set('processDataSet.baseName', 'Steel Production');
console.log(`🏭 Process name (EN): ${process.get('processDataSet.baseName')}`);

// Create typed flow accessor
const flow = createEnhancedTypedAccessor<Flow>({});
flow.set('flowDataSet.flowInformation.dataSetInformation.common:UUID', '789e0123-e89b-12d3-a456-426614174000');
flow.set('flowDataSet.flowInformation.dataSetInformation.CASNumber', '7439-89-6');

const flowName = flow.getMultiLang('flowDataSet.flowInformation.dataSetInformation.name.baseName');
flowName.setText('Iron', 'en');

console.log(`🌊 Flow name: ${flowName.getText('en')}`);
console.log(`🧪 CAS Number: ${flow.get('flowDataSet.flowInformation.dataSetInformation.CASNumber')}`);
console.log();

// Example 6: Raw data access
console.log('📝 6. Raw Data Access');

// Get the complete raw data object
const rawContactData = contact.data;
console.log(`📄 Raw data keys: ${Object.keys(rawContactData).join(', ')}`);

// Verify the data structure
if (rawContactData.contactDataSet) {
  console.log('✅ Contact data set structure is valid');
  const commonUUID = rawContactData.contactDataSet.contactInformation?.dataSetInformation?.['common:UUID'];
  if (commonUUID) {
    console.log(`✅ UUID found in data: ${commonUUID}`);
  }
}
console.log();

// Example 7: Property deletion
console.log('📝 7. Property Deletion');

// Add a temporary property
contact.set('contactDataSet.contactInformation.dataSetInformation.temporaryField', 'temp value');
console.log(`🔧 Temporary field added: ${contact.get('contactDataSet.contactInformation.dataSetInformation.temporaryField')}`);

// Delete the property
const deleted = contact.delete('contactDataSet.contactInformation.dataSetInformation.temporaryField');
console.log(`🗑️ Property deleted: ${deleted}`);

// Verify deletion
const afterDeletion = contact.get('contactDataSet.contactInformation.dataSetInformation.temporaryField');
console.log(`🔍 After deletion: ${afterDeletion || 'undefined'}`);
console.log();

// Example 8: Nested object access
console.log('📝 8. Nested Object Access');

// Set nested data structure
contact.set('contactDataSet.contactInformation.dataSetInformation.classificationInformation', {
  'common:classification': {
    'common:class': {
      '@level': '1',
      '@classId': 'company',
      '#text': 'Company'
    }
  }
});

// Access nested properties
const classLevel = contact.get('contactDataSet.contactInformation.dataSetInformation.classificationInformation.common:classification.common:class.@level');
const classText = contact.get('contactDataSet.contactInformation.dataSetInformation.classificationInformation.common:classification.common:class.#text');

console.log(`📊 Classification level: ${classLevel}`);
console.log(`📊 Classification text: ${classText}`);
console.log();

console.log('🎉 Typed Accessors Demo Complete!');
console.log('\nKey Features Demonstrated:');
console.log('✅ Type-safe property access with dot notation');
console.log('✅ Multi-language text handling');
console.log('✅ UUID and timestamp utilities');
console.log('✅ Object cloning');
console.log('✅ Property deletion');
console.log('✅ Nested object access');
console.log('✅ Raw data access');
console.log('✅ Path discovery and validation');