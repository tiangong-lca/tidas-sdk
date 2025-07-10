/**
 * Test modular imports
 * This example demonstrates how to use modular imports from different subpaths
 */

// Test importing from main package
import { TidasContact, TidasProcess, TidasFlow } from '@tidas-typescript-sdk';

// Test importing from /types subpath
import { Contact, Process, Flow } from '@tidas-typescript-sdk/types';

// Test importing from /schemas subpath
import { ContactsSchema, ProcessesSchema, FlowsSchema } from '@tidas-typescript-sdk/schemas';

// Test importing from /core subpath
import { TidasBase } from '@tidas-typescript-sdk/core';

// Test importing from /utils subpath
import { deepClone, merge } from '@tidas-typescript-sdk/utils';

console.log('🚀 Testing Modular Imports\n');

// Test main package imports
console.log('✅ Main package imports work:');
const contact1 = new TidasContact();
console.log('- TidasContact created');

const process1 = new TidasProcess();
console.log('- TidasProcess created');

const flow1 = new TidasFlow();
console.log('- TidasFlow created');

// Test type imports (these are TypeScript types, so they don't show at runtime)
console.log('\n✅ Type imports work (TypeScript compilation):');
console.log('- Contact type imported from /types');
console.log('- Process type imported from /types');
console.log('- Flow type imported from /types');

// Test schema imports
console.log('\n✅ Schema imports work:');
console.log('- ContactsSchema imported from /schemas');
console.log('- ProcessesSchema imported from /schemas');
console.log('- FlowsSchema imported from /schemas');

// Test core imports
console.log('\n✅ Core imports work:');
console.log('- TidasBase imported from /core');

// Test utils imports
console.log('\n✅ Utils imports work:');
const testObj = { a: 1, b: { c: 2 } };
const cloned = deepClone(testObj);
const merged = merge(testObj, { b: { d: 3 } });
console.log('- deepClone function works:', cloned);
console.log('- merge function works:', merged);

console.log('\n🎉 All modular imports are working correctly!');

// Example usage with modular imports
console.log('\n📝 Example: Creating objects using modular imports');

// Using types from /types
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
          '#text': 'Modular Import Test Company'
        }
      }
    }
  }
};

// Using classes from main package
const contact2 = new TidasContact(contactData);
console.log('Contact name:', contact2.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));

// Using validation from /schemas
import { validateWithZod } from '@tidas-typescript-sdk/schemas';
const validation = validateWithZod(contactData, ContactsSchema);
console.log('Validation result:', validation.success ? 'Valid' : 'Invalid');

console.log('\n✅ Modular imports test completed successfully!');