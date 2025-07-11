#!/usr/bin/env tsx

/**
 * Property Access Patterns Example
 * 
 * This example demonstrates various property access patterns available
 * in the TIDAS SDK using the Zod Proxy system.
 */

import { createZodContact, createZodFlow } from '../../src/core/zod-factories';
import { get, set } from '../../src/utils/object-utils';

console.log('🔗 TIDAS Property Access Patterns Example\n');

// 1. Direct Property Access
console.log('1. Direct Property Access Patterns\n');

const contactResult = createZodContact({ enableLogging: true });
const contact = contactResult.proxy;

// Initialize structure
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;
contact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('   a) Simple property assignment:');
contact.contactDataSet.contactInformation.dataSetInformation.email = 'test@example.com';
console.log(`      Set email: ${contact.contactDataSet.contactInformation.dataSetInformation.email}`);

console.log('\n   b) Nested property access:');
contact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0123';
const phone = contact.contactDataSet.contactInformation.dataSetInformation.telephone;
console.log(`      Retrieved phone: ${phone}`);

console.log('\n   c) Special character properties (XML attributes):');
contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] = '123e4567-e89b-12d3-a456-426614174000';
const uuid = contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'];
console.log(`      UUID: ${uuid}`);

// 2. Multi-language Text Access
console.log('\n\n2. Multi-language Text Access Patterns\n');

console.log('   a) Using helper functions (recommended):');
contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'John Doe',
  'en'
);
contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'Jean Dupont', 
  'fr'
);

const nameEn = contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'en');
const nameFr = contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'fr');
console.log(`      Name (EN): ${nameEn}`);
console.log(`      Name (FR): ${nameFr}`);

console.log('\n   b) Direct object assignment:');
contact.contactDataSet.contactInformation.dataSetInformation['common:shortName'] = {
  '@xml:lang': 'en',
  '#text': 'J. Doe'
};
console.log(`      Short name: ${contact.contactDataSet.contactInformation.dataSetInformation['common:shortName']['#text']}`);

// 3. Array Access Patterns  
console.log('\n\n3. Array Access Patterns\n');

const flowResult = createZodFlow({ enableLogging: true });
const flow = flowResult.proxy;

// Initialize structure with arrays
flow.flowDataSet = {} as any;
flow.flowDataSet.flowInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'] = [] as any;

console.log('   a) Array index access:');
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'][0] = {
  '@name': 'Categories',
  'common:class': {
    '@classId': '1.1',
    '#text': 'Materials'
  }
};

const firstClassification = flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'][0];
console.log(`      First classification: ${firstClassification['common:class']['#text']}`);

console.log('\n   b) Adding multiple array elements:');
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'][1] = {
  '@name': 'Subcategories',
  'common:class': {
    '@classId': '1.1.1',
    '#text': 'Metals'
  }
};

const arrayLength = flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'].length;
console.log(`      Array now has ${arrayLength} elements`);

// 4. Using Object Utilities
console.log('\n\n4. Using Object Utilities for Property Access\n');

// Build object first to use utilities
const builtContact = contactResult.buildObject();

console.log('   a) Using get() utility:');
const emailFromUtil = get(builtContact, 'contactDataSet.contactInformation.dataSetInformation.email');
console.log(`      Email via get(): ${emailFromUtil}`);

console.log('\n   b) Using set() utility:');
set(builtContact, 'contactDataSet.contactInformation.dataSetInformation.faxNumber', '+1-555-0124');
const fax = get(builtContact, 'contactDataSet.contactInformation.dataSetInformation.faxNumber');
console.log(`      Fax set via utility: ${fax}`);

console.log('\n   c) Array access with utilities:');
const classification = get(builtContact, 'contactDataSet.contactInformation.dataSetInformation.classificationInformation.common:classification[0].common:class.#text', 'Not found');
console.log(`      Classification via get(): ${classification}`);

// 5. Conditional Property Access
console.log('\n\n5. Conditional Property Access\n');

console.log('   a) Checking property existence:');
const hasEmail = 'email' in (contact.contactDataSet?.contactInformation?.dataSetInformation || {});
console.log(`      Has email property: ${hasEmail}`);

console.log('\n   b) Safe property access with defaults:');
const websiteUrl = contact.contactDataSet?.contactInformation?.dataSetInformation?.WWWAddress || 'No website provided';
console.log(`      Website: ${websiteUrl}`);

console.log('\n   c) Optional chaining example:');
const organizationName = contact.contactDataSet?.contactInformation?.dataSetInformation?.['common:name']?.['#text'] || 'Unknown';
console.log(`      Organization: ${organizationName}`);

// 6. Property Modification Patterns
console.log('\n\n6. Property Modification Patterns\n');

console.log('   a) Updating existing properties:');
const oldEmail = contact.contactDataSet.contactInformation.dataSetInformation.email;
contact.contactDataSet.contactInformation.dataSetInformation.email = 'updated@example.com';
const newEmail = contact.contactDataSet.contactInformation.dataSetInformation.email;
console.log(`      Old email: ${oldEmail}`);
console.log(`      New email: ${newEmail}`);

console.log('\n   b) Adding new properties dynamically:');
contact.contactDataSet.contactInformation.dataSetInformation.department = 'Engineering';
console.log(`      Department added: ${contact.contactDataSet.contactInformation.dataSetInformation.department}`);

console.log('\n   c) Removing properties:');
delete contact.contactDataSet.contactInformation.dataSetInformation.department;
const departmentExists = 'department' in contact.contactDataSet.contactInformation.dataSetInformation;
console.log(`      Department exists after deletion: ${departmentExists}`);

// 7. Validation During Property Access
console.log('\n\n7. Validation During Property Access\n');

const strictContactResult = createZodContact({ 
  enableLogging: true, 
  throwOnValidationError: false 
});
const strictContact = strictContactResult.proxy;

// Initialize structure
strictContact.contactDataSet = {} as any;
strictContact.contactDataSet.contactInformation = {} as any;
strictContact.contactDataSet.contactInformation.dataSetInformation = {} as any;

console.log('   a) Valid email assignment:');
strictContact.contactDataSet.contactInformation.dataSetInformation.email = 'valid@example.com';
console.log('      ✅ Valid email accepted');

console.log('\n   b) Invalid email assignment (validation will catch this):');
try {
  strictContact.contactDataSet.contactInformation.dataSetInformation.email = 'invalid-email-format';
  console.log('      ⚠️ Invalid email was set (validation may be disabled)');
} catch (error) {
  console.log('      ❌ Invalid email rejected by validation');
}

// 8. Access Logging and Debugging
console.log('\n\n8. Access Logging and Debugging\n');

console.log('   Recent access log entries:');
const accessLog = contactResult.getAccessLog();
accessLog.slice(-5).forEach((entry, index) => {
  console.log(`      ${index + 1}. ${entry.type.toUpperCase()}: ${entry.path}`);
});

console.log('\n   Current values map:');
const values = contactResult.getValues();
Object.keys(values).slice(0, 5).forEach(key => {
  console.log(`      ${key}: ${JSON.stringify(values[key])}`);
});

// 9. Performance Considerations
console.log('\n\n9. Performance Considerations\n');

console.log('   a) Efficient property access (cache references):');
const dataSetInfo = contact.contactDataSet.contactInformation.dataSetInformation;
dataSetInfo.email = 'cached@example.com';
dataSetInfo.telephone = '+1-555-CACHE';
console.log('      ✅ Used cached reference for multiple assignments');

console.log('\n   b) Batch property updates:');
const updates = {
  'contactDataSet.contactInformation.dataSetInformation.email': 'batch@example.com',
  'contactDataSet.contactInformation.dataSetInformation.telephone': '+1-555-BATCH',
  'contactDataSet.contactInformation.dataSetInformation.WWWAddress': 'https://batch.example.com'
};

// Note: This would work with object utilities on built object
console.log('      ✅ Batch updates prepared (use with object utilities)');

console.log('\n🎉 Property access patterns example completed!');
console.log('\n📋 Access Patterns Demonstrated:');
console.log('✅ Direct property assignment and retrieval');
console.log('✅ Multi-language text handling');
console.log('✅ Array access and manipulation');
console.log('✅ Object utility functions');
console.log('✅ Conditional and safe property access');
console.log('✅ Property modification patterns');
console.log('✅ Validation during access');
console.log('✅ Access logging and debugging');
console.log('✅ Performance optimization techniques');