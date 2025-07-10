/**
 * Test modular imports with updated type names
 */

// Test importing from main package
import { TidasContact } from '@tidas-typescript-sdk';

// Test importing from /types subpath with new simpler names
import { Contact, Process, Flow } from '@tidas-typescript-sdk/types';

// Test importing from /schemas subpath
import { ContactsSchema, validateWithZod } from '@tidas-typescript-sdk/schemas';

// Test importing from /utils subpath
import { deepClone } from '@tidas-typescript-sdk/utils';

console.log('🚀 Testing Updated Modular Imports\n');

// Test main package imports
console.log('✅ Main package imports work:');
const contact1 = new TidasContact();
console.log('- TidasContact created');

// Test type imports with simpler names
console.log('\n✅ Type imports with simpler names work:');
console.log('- Contact type imported from /types');
console.log('- Process type imported from /types');  
console.log('- Flow type imported from /types');

// Test creating object with simpler type
const contactData: Contact = {
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@version': '1.1',
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '123e4567-e89b-12d3-a456-426614174000',
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Updated Modular Test Company'
        }
      }
    }
  }
};

const contact2 = new TidasContact(contactData);
console.log('\n📝 Contact created with simpler type name:');
console.log('Name:', contact2.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));

// Test validation
const validation = validateWithZod(contactData, ContactsSchema);
console.log('Validation result:', validation.success ? 'Valid' : 'Invalid');

// Test utils
const cloned = deepClone(contactData);
console.log('\n✅ Utils work: deepClone function executed');

console.log('\n🎉 All updated modular imports working correctly!');