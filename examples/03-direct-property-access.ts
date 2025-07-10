#!/usr/bin/env tsx

/**
 * Example: Direct Property Access
 * 
 * This example demonstrates the new direct property access functionality
 * allowing you to access and modify nested properties using dot notation
 * like: obj.property.subProperty = value
 */

import { createEnhancedTypedAccessor, createDirectPropertyAccessor } from '../src/core/typed-accessors';
import type { Contact } from '../src/types';

console.log('🚀 Direct Property Access Example\n');

// 1. Create a contact with enhanced typed accessor
const contact = createEnhancedTypedAccessor<Contact>({});

// 2. Access the direct property accessor
const directAccess = contact.createDirectAccessor ? contact.createDirectAccessor() : contact;

console.log('📝 Setting up contact using direct property access...');

// 3. Direct property access and modification
// This is the new functionality - direct property access!
try {
  // Set up the contact data structure using direct property access
  directAccess.contactDataSet = {};
  directAccess.contactDataSet.contactInformation = {};
  directAccess.contactDataSet.contactInformation.dataSetInformation = {};
  
  // Set values directly
  directAccess.contactDataSet.contactInformation.dataSetInformation.email = 'test@example.com';
  directAccess.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0123';
  directAccess.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://example.com';
  
  console.log('✅ Direct property access successful!');
  
  // 4. Read values using direct property access
  console.log('📖 Reading values using direct property access:');
  console.log(`   Email: ${directAccess.contactDataSet.contactInformation.dataSetInformation.email}`);
  console.log(`   Phone: ${directAccess.contactDataSet.contactInformation.dataSetInformation.telephone}`);
  console.log(`   Website: ${directAccess.contactDataSet.contactInformation.dataSetInformation.WWWAddress}`);
  
  // 5. Modify existing values
  console.log('\\n🔄 Modifying values using direct property access...');
  directAccess.contactDataSet.contactInformation.dataSetInformation.email = 'updated@example.com';
  directAccess.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-9999';
  
  console.log('✅ Values modified successfully!');
  console.log(`   New Email: ${directAccess.contactDataSet.contactInformation.dataSetInformation.email}`);
  console.log(`   New Phone: ${directAccess.contactDataSet.contactInformation.dataSetInformation.telephone}`);
  
} catch (error) {
  console.error('❌ Direct property access error:', error);
}

// 6. Demonstrate compatibility with existing method access
console.log('\\n🔄 Comparing with method-based access:');
console.log('   Method access email:', contact.get('contactDataSet.contactInformation.dataSetInformation.email'));
console.log('   Direct access email:', directAccess.contactDataSet?.contactInformation?.dataSetInformation?.email);

// 7. Test deep property creation
console.log('\\n🏗️ Testing deep property creation:');
try {
  // This should create all intermediate objects automatically
  directAccess.contactDataSet.administrativeInformation = {};
  directAccess.contactDataSet.administrativeInformation.dataEntryBy = {};
  directAccess.contactDataSet.administrativeInformation.dataEntryBy.timeStamp = new Date().toISOString();
  
  console.log('✅ Deep property creation successful!');
  console.log(`   Timestamp: ${directAccess.contactDataSet.administrativeInformation.dataEntryBy.timeStamp}`);
  
} catch (error) {
  console.error('❌ Deep property creation error:', error);
}

// 8. Test with alternative approach - using createDirectPropertyAccessor directly
console.log('\\n🔧 Testing createDirectPropertyAccessor directly:');
const simpleObject = { nested: { value: 42 } };
const directProxy = createDirectPropertyAccessor(simpleObject, 'root', (newValue) => {
  console.log('   📊 Object changed:', JSON.stringify(newValue, null, 2));
});

console.log('   Original nested value:', directProxy.nested.value);
directProxy.nested.value = 100;
console.log('   Modified nested value:', directProxy.nested.value);

// Create new deep structure
directProxy.deep = {};
directProxy.deep.level1 = {};
directProxy.deep.level1.level2 = {};
directProxy.deep.level1.level2.value = 'deep value';

console.log('   Deep structure created:', directProxy.deep.level1.level2.value);

// 9. Show final contact data
console.log('\\n📋 Final contact data:');
console.log(JSON.stringify(contact.data, null, 2));

console.log('\\n🎉 Direct Property Access Example Complete!');