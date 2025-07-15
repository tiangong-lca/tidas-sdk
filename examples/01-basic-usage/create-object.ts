#!/usr/bin/env tsx

/**
 * Example:  Contact Usage - Direct TIDAS Structure Access
 * 
 * This example demonstrates the new simplified approach where users
 * directly operate on the real TIDAS data structure without abstraction layers.
 */

import { createContact } from '../../src/core';
import { Contact } from '../../src/types';

console.log('=== Simplified Contact Usage Examples ===\n');

// Example 1: Create and directly manipulate TIDAS structure
console.log('1. Direct TIDAS Structure Access:');
const contact = createContact();

// Direct manipulation of TIDAS structure
contact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'John Smith' }
];

contact.contactDataSet.contactInformation.dataSetInformation['common:shortName'] = [
  { '@xml:lang': 'en', '#text': 'J. Smith' }
];

contact.contactDataSet.contactInformation.dataSetInformation.email = 'john.smith@example.com';
contact.contactDataSet.contactInformation.dataSetInformation.telephone = '+1-555-0199';
contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://johnsmith.example.com';

console.log('Contact name:', contact.contactDataSet.contactInformation.dataSetInformation['common:name']);
console.log('Contact email:', contact.contactDataSet.contactInformation.dataSetInformation.email);
console.log('Contact UUID:', contact.contactDataSet.contactInformation.dataSetInformation['common:UUID']);

// Example 2: Multi-language support
console.log('\n2. Multi-Language Support:');
const multiLangContact = createContact();

// Add names in multiple languages
multiLangContact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'International Contact' },
  { '@xml:lang': 'fr', '#text': 'Contact International' },
  { '@xml:lang': 'es', '#text': 'Contacto Internacional' },
  { '@xml:lang': 'de', '#text': 'Internationaler Kontakt' }
];

console.log('Multi-language names:');
multiLangContact.contactDataSet.contactInformation.dataSetInformation['common:name'].forEach(nameObj => {
  console.log(`  ${nameObj['@xml:lang']}: ${nameObj['#text']}`);
});

// Example 3: Working with contact address
console.log('\n3. Contact Address:');
const addressContact = createContact();

// Set contact address with multi-language support
addressContact.contactDataSet.contactInformation.dataSetInformation.contactAddress = [
  {
    '@xml:lang': 'en',
    '#text': 'ACME Corporation\n123 Business Street\nNew York, NY 10001\nUnited States'
  },
  {
    '@xml:lang': 'es',
    '#text': 'Corporación ACME\n123 Calle de Negocios\nNueva York, NY 10001\nEstados Unidos'
  }
];

console.log('Contact address (English):');
console.log(addressContact.contactDataSet.contactInformation.dataSetInformation.contactAddress[0]['#text']);

// Example 4: Administrative information
console.log('\n4. Administrative Information:');
const adminContact = createContact();

// Update version and timestamp
adminContact.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '2.1.0';
adminContact.contactDataSet.administrativeInformation.dataEntryBy['common:timeStamp'] = new Date().toISOString();

console.log('Version:', adminContact.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion']);
console.log('Timestamp:', adminContact.contactDataSet.administrativeInformation.dataEntryBy['common:timeStamp']);

// Example 5: Classification
console.log('\n5. Classification:');
const classifiedContact = createContact();

// Set classification
classifiedContact.contactDataSet.contactInformation.dataSetInformation.classificationInformation['common:classification'] = {
  'common:class': {
    '@level': '1',
    '@classId': 'contact-person-uuid',
    '#text': 'Contact person'
  }
};

console.log('Classification:', 
  classifiedContact.contactDataSet.contactInformation.dataSetInformation.classificationInformation['common:classification']['common:class']['#text']
);

// Example 6: Validation
console.log('\n6. Schema Validation:');
const validationResult = contact.validate();
console.log('Is valid:', validationResult.success);

if (!validationResult.success) {
  console.log('Validation errors:');
  validationResult.error.errors.forEach(error => {
    console.log(`  - ${error.path.join('.')}: ${error.message}`);
  });
} else {
  console.log('Contact passes all schema validations!');
}

// Example 7: Data export
console.log('\n7. Data Export:');
const jsonData = contact.toJSON();
console.log('JSON data structure keys:', Object.keys(jsonData));
console.log('Contact data set keys:', Object.keys(jsonData.contactDataSet || {}));

// Example 8: Clone functionality
console.log('\n8. Clone Functionality:');
const originalContact = createContact();
originalContact.contactDataSet.contactInformation.dataSetInformation.email = 'original@example.com';

const clonedContact = originalContact.clone();
clonedContact.contactDataSet.contactInformation.dataSetInformation.email = 'cloned@example.com';

console.log('Original email:', originalContact.contactDataSet.contactInformation.dataSetInformation.email);
console.log('Cloned email:', clonedContact.contactDataSet.contactInformation.dataSetInformation.email);

// Example 9: Dynamic path access (dot notation)
console.log('\n9. Dynamic Path Access:');
const dynamicContact = createContact();

// Using dot notation for nested access
(dynamicContact as any)['contactDataSet.contactInformation.dataSetInformation.email'] = 'dynamic@example.com';
(dynamicContact as any)['contactDataSet.contactInformation.dataSetInformation.telephone'] = '+1-555-0999';

console.log('Dynamic email:', (dynamicContact as any)['contactDataSet.contactInformation.dataSetInformation.email']);
console.log('Dynamic phone:', (dynamicContact as any)['contactDataSet.contactInformation.dataSetInformation.telephone']);

// Example 10: Creating from existing data
console.log('\n10. Creating from Existing Data:');
const existingData = {
  contactDataSet: {
    contactInformation: {
      dataSetInformation: {
        'common:name': [{ '@xml:lang': 'en', '#text': 'Existing Contact' }],
        email: 'existing@example.com'
      }
    }
  }
};

const fromDataContact = createContact(existingData as Partial<Contact>);
console.log('From data contact name:', fromDataContact.contactDataSet.contactInformation.dataSetInformation['common:name'][0]['#text']);
console.log('From data contact email:', fromDataContact.contactDataSet.contactInformation.dataSetInformation.email);

console.log('\n=== Examples Complete ===');
console.log('✓ Direct TIDAS structure access');
console.log('✓ Multi-language support');
console.log('✓ Contact address handling');
console.log('✓ Administrative information');
console.log('✓ Classification support');
console.log('✓ Schema validation');
console.log('✓ Data export functionality');
console.log('✓ Clone functionality');
console.log('✓ Dynamic path access');
console.log('✓ Creating from existing data');
console.log('\n✨ Simple, transparent, and schema-compliant!');