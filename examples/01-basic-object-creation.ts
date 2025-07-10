/**
 * Example 1: Basic Object Creation
 *
 * This example demonstrates various ways to create TIDAS objects using the SDK.
 */
import { TidasContact } from '@tidas-typescript-sdk';

console.log('🚀 TIDAS SDK - Basic Object Creation Examples\n');

// Example 1.1: Direct instantiation
console.log('📝 1.1 Direct Instantiation');
const contact1 = new TidasContact();
console.log('Empty contact created:', contact1.getUUID() || 'No UUID yet');

// Example 1.2: Direct instantiation with data
console.log('\n📝 1.2 Direct Instantiation with Initial Data');
const contact2 = new TidasContact({
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@version': '1.1',
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '123e4567-e89b-12d3-a456-426614174000',
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Example Company',
        },
        'common:shortName': {
          '@xml:lang': 'en',
          '#text': 'ExCo',
        },
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '1',
              '@classId': 'company',
              '#text': 'Company',
            },
          },
        },
      },
    },
  },
});
console.log('Contact with data created:', contact2.getUUID());

// Example 1.3: Using factory functions
console.log('\n📝 1.3 Factory Functions');
const contact3 = createContact({
  contactDataSet: {
    contactInformation: {
      dataSetInformation: {
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Green Energy Corp',
        },
      },
    },
  },
});
console.log(
  'Contact via factory:',
  contact3.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name'
  )
);

// Example 1.4: Using builder pattern
console.log('\n📝 1.4 Builder Pattern');
const contact4 = buildContact()
  .withUUID('456e7890-e89b-12d3-a456-426614174000')
  .withName('Solar Solutions Ltd', 'en')
  .withName('太阳能解决方案有限公司', 'zh')
  .withEmail('info@solarsolutions.com')
  .withPhone('+1-555-0123')
  .build();

console.log(
  'Built contact name (EN):',
  contact4.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'en'
  )
);
console.log(
  'Built contact name (ZH):',
  contact4.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'zh'
  )
);

// Example 1.5: Creating with validation
console.log('\n📝 1.5 Creating with Validation');
const validationOptions: ValidationOptions = {
  enableValidation: true,
  throwOnValidationError: false,
};

const contact5 = createContact(
  {
    contactDataSet: {
      contactInformation: {
        dataSetInformation: {
          'common:UUID': 'invalid-uuid', // This will cause validation to fail
          'common:name': {
            '@xml:lang': 'en',
            '#text': 'Test Company',
          },
        },
      },
    },
  },
  validationOptions
);

const validationResult = contact5.validate();
console.log(
  'Validation result:',
  validationResult.success ? 'Valid' : 'Invalid'
);
if (!validationResult.success) {
  console.log('Validation errors:', validationResult.error?.issues.slice(0, 2)); // Show first 2 errors
}

// Example 1.6: Creating Process objects
console.log('\n📝 1.6 Process Creation');
const process1 = createProcess({
  processDataSet: {
    processInformation: {
      dataSetInformation: {
        'common:name': {
          baseName: {
            '@xml:lang': 'en',
            '#text': 'Steel Production',
          },
        },
      },
      geography: {
        locationOfOperationSupplyOrProduction: {
          '@location': 'CN',
        },
      },
      time: {
        referenceYear: 2024,
      },
    },
  },
});

console.log(
  'Process name:',
  process1.getMultiLangText(
    'processDataSet.processInformation.dataSetInformation.common:name.baseName'
  )
);
console.log(
  'Process location:',
  process1.get(
    'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location'
  )
);

// Example 1.7: Creating Flow objects
console.log('\n📝 1.7 Flow Creation');
const flow1 = buildFlow()
  .withBaseName('Carbon Dioxide', 'en')
  .withBaseName('二氧化碳', 'zh')
  .withCASNumber('124-38-9')
  .withTypeOfDataSet('Elementary flow')
  .build();

console.log(
  'Flow name (EN):',
  flow1.getMultiLangText(
    'flowDataSet.flowInformation.dataSetInformation.name.baseName',
    'en'
  )
);
console.log(
  'Flow CAS:',
  flow1.get('flowDataSet.flowInformation.dataSetInformation.CASNumber')
);

// Example 1.8: JSON conversion
console.log('\n📝 1.8 JSON Conversion');
const contactJSON = contact4.toJSON({ pretty: true });
console.log(
  'Contact as JSON (first 200 chars):',
  contactJSON.substring(0, 200) + '...'
);

// Convert back from JSON
const contactFromJSON = fromJSON<TidasContact>(contactJSON, 'contact');
console.log(
  'Recreated from JSON:',
  contactFromJSON.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'en'
  )
);

// Example 1.9: Object manipulation
console.log('\n📝 1.9 Object Manipulation');
const contact6 = createContact();

// Chain multiple operations
contact6
  .set(
    'contactDataSet.contactInformation.dataSetInformation.common:UUID',
    contact6.generateUUID()
  )
  .setMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'Dynamic Corp',
    'en'
  )
  .setMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'Dynamique Corp',
    'fr'
  )
  .update({
    'contactDataSet.contactInformation.dataSetInformation.email':
      'contact@dynamic.com',
    'contactDataSet.contactInformation.dataSetInformation.telephoneNumber':
      '+33-1-23-45-67-89',
  });

console.log('Manipulated contact UUID:', contact6.getUUID());
console.log(
  'Manipulated contact name (FR):',
  contact6.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:name',
    'fr'
  )
);

// Example 1.10: Cloning and merging
console.log('\n📝 1.10 Cloning and Merging');
const clonedContact = contact6.clone({ generateNewUUID: true });
console.log('Original UUID:', contact6.getUUID());
console.log('Cloned UUID:', clonedContact.getUUID());

// Merge additional data
clonedContact.merge({
  contactDataSet: {
    contactInformation: {
      dataSetInformation: {
        'common:shortName': {
          '@xml:lang': 'en',
          '#text': 'DynCorp',
        },
      },
    },
  },
});

console.log(
  'After merge - Short name:',
  clonedContact.getMultiLangText(
    'contactDataSet.contactInformation.dataSetInformation.common:shortName'
  )
);

console.log('\n✅ Basic object creation examples completed!');
