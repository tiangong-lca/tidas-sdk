import {
  ContactBaseObject,
  ProcessBaseObject,
  FlowBaseObject,
  SourceBaseObject,
  FlowPropertyBaseObject,
  UnitGroupBaseObject,
  LCIAMethodBaseObject,
  LifeCycleModelBaseObject,
} from '../src/core/base-objects';

console.log('🚀 Testing Direct Instantiation with new Constructor\\n');

// ===== 1. Test direct instantiation =====
console.log('1️⃣ Testing direct instantiation:');

const contact = new ContactBaseObject();
console.log(contact.toJSON());
console.log('✅ Created contact:', contact.getTypeName());

const process = new ProcessBaseObject();
console.log('✅ Created process:', process.getTypeName());

const flow = new FlowBaseObject();
console.log('✅ Created flow:', flow.getTypeName());

const source = new SourceBaseObject();
console.log('✅ Created source:', source.getTypeName());

const flowProperty = new FlowPropertyBaseObject();
console.log('✅ Created flow property:', flowProperty.getTypeName());

const unitGroup = new UnitGroupBaseObject();
console.log('✅ Created unit group:', unitGroup.getTypeName());

const lciaMethod = new LCIAMethodBaseObject();
console.log('✅ Created LCIA method:', lciaMethod.getTypeName());

const lifecycleModel = new LifeCycleModelBaseObject();
console.log('✅ Created lifecycle model:', lifecycleModel.getTypeName());

// ===== 2. Test with partial data =====
console.log('\\n2️⃣ Testing with partial data:');

const contactWithData = new ContactBaseObject({
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd',
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '0197eee2-8376-774a-8e49-3ef655f5794f',
        'common:shortName': {
          '@xml:lang': 'en',
          '#text': 'Test Contact',
        },
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Test Contact',
        },
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '0',
              '@classId': '1',
              '#text': 'Group of organisations, project',
            },
          },
        },
      },
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2021-01-01T00:00:00Z',
        'common:referenceToDataSetFormat': {
          '@type': 'ILCD',
          '@refObjectId': '1234567890',
          '@version': '1.0',
          '@uri': 'http://example.com/ILCD',
          'common:shortDescription': {
            '@xml:lang': 'en',
            '#text': 'Test Description',
          },
        },
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '1.0',
        'common:permanentDataSetURI': 'http://example.com/ILCD',
        'common:referenceToOwnershipOfDataSet': {
          '@type': 'ILCD',
          '@refObjectId': '1234567890',
          '@version': '1.0',
          '@uri': 'http://example.com/ILCD',
          'common:shortDescription': {
            '@xml:lang': 'en',
            '#text': 'Test Description',
          },
        },
      },
    },
  },
});

console.log('✅ Contact with data:', contactWithData.getTypeName());
console.log(
  '✅ Contact custom field:',
  contactWithData.get('contactDataSet.customField')
);

const processWithData = new ProcessBaseObject({
  processDataSet: {
    customField: 'test process value',
  },
} as any);

console.log('✅ Process with data:', processWithData.getTypeName());
console.log(
  '✅ Process custom field:',
  processWithData.get('processDataSet.customField')
);

// ===== 3. Test schema info =====
console.log('\\n3️⃣ Testing schema info:');

const contactSchema = contact.getSchemaInfo();
console.log('✅ Contact schema info:');
console.log('  - Root key:', contactSchema.rootKey);
console.log('  - Type name:', contactSchema.typeName);
console.log('  - UUID path:', contactSchema.uuidPath);
console.log('  - Available paths:', contactSchema.availablePaths.length);

const processSchema = process.getSchemaInfo();
console.log('✅ Process schema info:');
console.log('  - Root key:', processSchema.rootKey);
console.log('  - Type name:', processSchema.typeName);
console.log('  - UUID path:', processSchema.uuidPath);
console.log('  - Available paths:', processSchema.availablePaths.length);

// ===== 4. Test UUID operations =====
console.log('\\n4️⃣ Testing UUID operations:');

console.log('✅ Contact UUID:', contact.getUUID());
console.log('✅ Process UUID:', process.getUUID());
console.log('✅ Flow UUID:', flow.getUUID());

// ===== 5. Test generic operations =====
console.log('\\n5️⃣ Testing generic operations:');

contact.set('customField', 'test value');
console.log('✅ Contact custom field:', contact.get('customField'));

process.set('nested.property', { key: 'value' });
console.log('✅ Process nested property:', process.get('nested.property'));

flow.update({
  field1: 'value1',
  'nested.field2': 'value2',
});
console.log('✅ Flow field1:', flow.get('field1'));
console.log('✅ Flow nested.field2:', flow.get('nested.field2'));

console.log('\\n🎉 Direct Instantiation Test Completed Successfully!');
console.log('🎯 All objects can be created using new Constructor() pattern!');
