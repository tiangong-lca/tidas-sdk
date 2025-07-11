#!/usr/bin/env tsx

/**
 * Zod Proxy Demo - True Property Access with Schema Validation
 * 
 * This example demonstrates the new Zod Proxy approach that provides
 * true property access (obj.property.subProperty = value) with 
 * real-time Schema validation.
 */

import { createZodContact, createZodFlow, createZodProcess } from '../src/core/zod-factories';

console.log('🚀 Zod Proxy Demo \n');

// 1. Create a Contact using Zod Proxy
console.log('1. Creating Contact with Zod Proxy...');
const contactResult = createZodContact({ enableLogging: true });
const contact = contactResult.proxy;

// 2. True property access - this is the magic!
console.log('📝 Setting contact data using true property access...');

// Initialize the structure
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;
contact.contactDataSet.contactInformation.dataSetInformation = {} as any;

// Set values using direct property access
contact.contactDataSet.contactInformation.dataSetInformation.email = 'john.doe@example.com';
contact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0123';
contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://johndoe.example.com';

// Set multi-language name
contact.contactDataSet.contactInformation.dataSetInformation['common:name'] = {
  '@xml:lang': 'en',
  '#text': 'John Doe'
};

// Set UUID
contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] = '123e4567-e89b-12d3-a456-426614174000';

console.log('✅ Contact data set successfully!');

// 3. Read values using property access
console.log('\n📖 Reading values using property access:');
console.log(`   Email: ${contact.contactDataSet.contactInformation.dataSetInformation.email}`);
console.log(`   Phone: ${contact.contactDataSet.contactInformation.dataSetInformation.telephone}`);
console.log(`   Website: ${contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress}`);
console.log(`   UUID: ${contact.contactDataSet.contactInformation.dataSetInformation['common:UUID']}`);

// 4. Use helper functions
console.log('\n🛠️ Using TIDAS helper functions...');
contactResult.setMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:shortName', 'J. Doe', 'en');
contactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
contactResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

const shortName = contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:shortName', 'en');
console.log(`   Short Name: ${shortName}`);

// 5. Build final object and validate
console.log('\n🔍 Building and validating object...');
const builtObject = contactResult.buildObject();
console.log('Built object structure:', JSON.stringify(builtObject, null, 2));

const validation = contactResult.validate();
if (validation.success) {
  console.log('✅ Validation successful!');
} else {
  console.log('❌ Validation failed:', validation.error?.issues);
}

// 6. Flow example with arrays
console.log('\n\n2. Flow Example with Array Handling...');
const flowResult = createZodFlow({ enableLogging: true });
const flow = flowResult.proxy;

// Initialize flow structure
flow.flowDataSet = {} as any;
flow.flowDataSet.flowInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation.name = {} as any;

// Set flow data
flow.flowDataSet.flowInformation.dataSetInformation['common:UUID'] = '456e7890-e89b-12d3-a456-426614174000';
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName = {
  '@xml:lang': 'en',
  '#text': 'Steel'
};
flow.flowDataSet.flowInformation.dataSetInformation.CASNumber = '7439-89-6';
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName['#text'] = 'Elementary flow';

console.log('✅ Flow data set successfully!');
console.log(`   Flow Name: ${flow.flowDataSet.flowInformation.dataSetInformation.name.baseName['#text']}`);
console.log(`   CAS Number: ${flow.flowDataSet.flowInformation.dataSetInformation.CASNumber}`);

// 7. Process example with complex nested structure
console.log('\n\n3. Process Example with Complex Structure...');
const processResult = createZodProcess({ enableLogging: true });
const process = processResult.proxy;

// Initialize complex nested structure
process.processDataSet = {} as any;
process.processDataSet.processInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation.name = {} as any;
process.processDataSet.processInformation.geography = {} as any;
process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction = {} as any;
process.processDataSet.processInformation.time = {} as any;

// Set process data
process.processDataSet.processInformation.dataSetInformation['common:UUID'] = '789e0123-e89b-12d3-a456-426614174000';
process.processDataSet.processInformation.dataSetInformation.name.baseName = {
  '@xml:lang': 'en',
  '#text': 'Steel Production'
};
process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location'] = 'CN';
process.processDataSet.processInformation.time.referenceYear = 2024;

console.log('✅ Process data set successfully!');
console.log(`   Process Name: ${process.processDataSet.processInformation.dataSetInformation.name.baseName['#text']}`);
console.log(`   Location: ${process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location']}`);
console.log(`   Reference Year: ${process.processDataSet.processInformation.time.referenceYear}`);

// 8. Show access logs
console.log('\n📊 Access Logs:');
console.log('Contact access log:', contactResult.getAccessLog().slice(-5)); // Last 5 entries
console.log('Flow access log:', flowResult.getAccessLog().slice(-5));
console.log('Process access log:', processResult.getAccessLog().slice(-5));

// 9. Debug information
console.log('\n🔧 Debug Information:');
console.log('Contact debug:', contactResult.debug());

// 10. Test validation with invalid data
console.log('\n\n4. Testing Validation with Invalid Data...');
const invalidContactResult = createZodContact({ throwOnValidationError: false });
const invalidContact = invalidContactResult.proxy;

// Try to set invalid email
invalidContact.contactDataSet = {} as any;
invalidContact.contactDataSet.contactInformation = {} as any;
invalidContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

try {
  invalidContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid-email'; // Invalid email format
  console.log('⚠️ Invalid email was set (validation disabled)');
} catch (error) {
  console.log('❌ Validation error caught:', error);
}

const invalidValidation = invalidContactResult.validate();
if (!invalidValidation.success) {
  console.log('❌ Validation failed as expected:', invalidValidation.error?.issues.map(i => i.message));
}

console.log('\n🎉 Zod Proxy Demo Complete!');
console.log('\n📋 Key Benefits Demonstrated:');
console.log('✅ True property access: obj.property.subProperty = value');
console.log('✅ Real-time Schema validation');
console.log('✅ TypeScript IntelliSense support');
console.log('✅ Complex nested structure handling');
console.log('✅ TIDAS-specific helper functions');
console.log('✅ Access logging for debugging');
console.log('✅ Comprehensive validation feedback');