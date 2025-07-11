#!/usr/bin/env tsx

/**
 * Basic Contact Creation Example
 * 
 * This example demonstrates how to create a TIDAS Contact object using
 * the Zod Proxy factory function with type-safe property access.
 */

import { createZodContact } from '../../src/core/zod-factories';

console.log('📞 TIDAS Contact Creation Example\n');

// 1. Create a new Contact using the factory function
console.log('1. Creating a new Contact object...');
const contactResult = createZodContact({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

// Extract the proxy object for easier use
const contact = contactResult.proxy;

console.log('✅ Contact proxy created successfully!');

// 2. Initialize the basic structure
console.log('\n2. Setting up basic contact structure...');

// Initialize nested structure (this is required due to the TIDAS schema)
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;
contact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('✅ Contact structure initialized!');

// 3. Set basic contact information
console.log('\n3. Setting contact information...');

// Generate a UUID for this contact
contactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');

// Set contact details using direct property access
contact.contactDataSet.contactInformation.dataSetInformation.email = 'john.smith@example.com';
contact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0199';
contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://johnsmith.example.com';

// Set multi-language contact name using helper function
contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'John Smith',
  'en'
);

contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:shortName',
  'J. Smith',
  'en'
);

console.log('✅ Contact information set successfully!');

// 4. Set administrative information
console.log('\n4. Setting administrative information...');

// Initialize administrative section
contact.contactDataSet.administrativeInformation = {} as any;
contact.contactDataSet.administrativeInformation.dataEntryBy = {} as any;
contact.contactDataSet.administrativeInformation.publicationAndOwnership = {} as any;

// Set timestamp using helper function
contactResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

// Set version and status
contact.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0';
contact.contactDataSet.administrativeInformation.publicationAndOwnership['common:workflowAndPublicationStatus'] = 'Published';

console.log('✅ Administrative information set!');

// 5. Read back the data using property access
console.log('\n5. Reading contact information:');
console.log(`   Name: ${contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'en')}`);
console.log(`   Short Name: ${contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:shortName', 'en')}`);
console.log(`   Email: ${contact.contactDataSet.contactInformation.dataSetInformation.email}`);
console.log(`   Phone: ${contact.contactDataSet.contactInformation.dataSetInformation.telephone}`);
console.log(`   Website: ${contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress}`);
console.log(`   UUID: ${contact.contactDataSet.contactInformation.dataSetInformation['common:UUID']}`);
console.log(`   Version: ${contact.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion']}`);

// 6. Build the final object
console.log('\n6. Building final contact object...');
const finalContact = contactResult.buildObject();

console.log('Final contact structure:');
console.log(JSON.stringify(finalContact, null, 2));

// 7. Validate the contact
console.log('\n7. Validating contact data...');
const validation = contactResult.validate();

if (validation.success) {
  console.log('✅ Contact validation successful!');
  console.log('Contact is ready for use.');
} else {
  console.log('❌ Contact validation failed:');
  validation.error?.issues.forEach((issue, index) => {
    console.log(`   ${index + 1}. ${issue.message} at path: ${issue.path.join('.')}`);
  });
}

// 8. Show access log (for debugging)
console.log('\n8. Access log (last 10 operations):');
const accessLog = contactResult.getAccessLog();
accessLog.slice(-10).forEach((entry, index) => {
  console.log(`   ${index + 1}. ${entry.type.toUpperCase()}: ${entry.path} ${entry.value ? `= ${JSON.stringify(entry.value)}` : ''}`);
});

console.log('\n🎉 Contact creation example completed!');
console.log('\n📋 Key Concepts Demonstrated:');
console.log('✅ Factory function usage (createZodContact)');
console.log('✅ Zod Proxy configuration options');
console.log('✅ Direct property access (contact.property.subproperty)');
console.log('✅ Helper functions (setMultiLangText, generateUUID, setCurrentTimestamp)');
console.log('✅ Object building and validation');
console.log('✅ Access logging for debugging');