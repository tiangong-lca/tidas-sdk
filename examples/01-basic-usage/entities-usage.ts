/**
 * Complete TIDAS Entities Usage Examples
 *
 * This example demonstrates how to create and work with all 8 TIDAS entity types
 * using the simplified object-oriented approach.
 */

import {
  createContact,
  createFlow,
  createProcess,
  createSource,
  createFlowProperty,
  createUnitGroup,
  createLCIAMethod,
  createLifeCycleModel,
  createTidasEntity,
} from '@tiangong-lca/tidas-sdk/core';

// Example 1: Create a Contact
console.log('=== Example 1: Contact Creation ===');
const contact = createContact();

// Set basic contact information using direct TIDAS structure access

// Quick way to set multi-language text
contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('Dr. Jane Smith', 'en');

contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('Dr. Jane Smith', 'fr');

// or directly set the text
contact.contactDataSet.contactInformation.dataSetInformation[
  'common:shortName'
] = [
  { '@xml:lang': 'en', '#text': 'J. Smith' },
  { '@xml:lang': 'fr', '#text': 'J. Smith' },
];

// get the text
const enName =
  contact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ].getText?.('en');
const frName =
  contact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ].getText?.('fr');

contact.contactDataSet.contactInformation.dataSetInformation.email =
  'jane.smith@example.com';
contact.contactDataSet.contactInformation.dataSetInformation.telefax =
  '+1-555-0123';

console.log(
  'Contact name:',
  contact.contactDataSet.contactInformation.dataSetInformation['common:name']
);
console.log(
  'Contact validation:',
  contact.validate().success ? 'PASSED' : 'FAILED'
);

// Example 2: Create a Flow
console.log('\n=== Example 2: Flow Creation ===');
const flow = createFlow();

// Set flow information
flow.flowDataSet.flowInformation.dataSetInformation.name.baseName = [
  { '@xml:lang': 'en', '#text': 'Carbon dioxide' },
];

flow.flowDataSet.flowInformation.dataSetInformation['common:synonyms'] = [
  { '@xml:lang': 'en', '#text': 'CO2; carbon dioxide' },
];

flow.flowDataSet.flowInformation.dataSetInformation.CASNumber = '124-38-9';

console.log(
  'Flow name:',
  flow.flowDataSet.flowInformation.dataSetInformation.name.baseName
);
console.log('Flow validation:', flow.validate().success ? 'PASSED' : 'FAILED');

// Example 3: Create a Process
console.log('\n=== Example 3: Process Creation ===');
const process = createProcess();

// Set process information
process.processDataSet.processInformation.dataSetInformation.name.baseName = [
  { '@xml:lang': 'en', '#text': 'Electricity production, wind power' },
];

// Set technology information
if (process.processDataSet.processInformation.technology) {
  process.processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses =
    [
      {
        '@xml:lang': 'en',
        '#text':
          'Wind turbine electricity generation including construction and operation',
      },
    ];
}

// Set time period
process.processDataSet.processInformation.time.referenceYear = 2023;
process.processDataSet.processInformation.time.dataSetValidUntil = 2030;

console.log(
  'Process name:',
  process.processDataSet.processInformation.dataSetInformation.name.baseName
);
console.log(
  'Process validation:',
  process.validate().success ? 'PASSED' : 'FAILED'
);

// Example 4: Create a Source
console.log('\n=== Example 4: Source Creation ===');
const source = createSource();

// Set source information
source.sourceDataSet.sourceInformation.dataSetInformation['common:shortName'] =
  [{ '@xml:lang': 'en', '#text': 'IPCC 2013 Climate Change Report' }];

source.sourceDataSet.sourceInformation.dataSetInformation.sourceCitation =
  'IPCC, 2013: Climate Change 2013: The Physical Science Basis.';

source.sourceDataSet.sourceInformation.dataSetInformation.publicationType =
  'Article in periodical';

source.sourceDataSet.sourceInformation.dataSetInformation.sourceDescriptionOrComment =
  [
    {
      '@xml:lang': 'en',
      '#text':
        'Comprehensive report on climate change from the Intergovernmental Panel on Climate Change',
    },
  ];

console.log(
  'Source name:',
  source.sourceDataSet.sourceInformation.dataSetInformation['common:shortName']
);
console.log(
  'Source validation:',
  source.validate().success ? 'PASSED' : 'FAILED'
);

// Example 5: Create a Flow Property
console.log('\n=== Example 5: Flow Property Creation ===');
const flowProperty = createFlowProperty();

// Set flow property information
flowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Mass' }];

flowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
  'common:generalComment'
] = [{ '@xml:lang': 'en', '#text': 'Mass flow property for material flows' }];

console.log(
  'Flow Property name:',
  flowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
    'common:name'
  ]
);
console.log(
  'Flow Property validation:',
  flowProperty.validate().success ? 'PASSED' : 'FAILED'
);

// Example 6: Create a Unit Group
console.log('\n=== Example 6: Unit Group Creation ===');
const unitGroup = createUnitGroup();

// Set unit group information
unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
  'common:name'
].setText?.('Mass units', 'en');

// Add multiple units to the unit group
unitGroup.unitGroupDataSet.units = {
  unit: [
    {
      '@dataSetInternalID': '0',
      name: 'kg',
      meanValue: '1.0',
      generalComment: [
        { '@xml:lang': 'en', '#text': 'kilogram - reference unit' },
      ],
    },
    {
      '@dataSetInternalID': '1',
      name: 'g',
      meanValue: '0.001',
      generalComment: [{ '@xml:lang': 'en', '#text': 'gram' }],
    },
    {
      '@dataSetInternalID': '2',
      name: 't',
      meanValue: '1000.0',
      generalComment: [{ '@xml:lang': 'en', '#text': 'metric ton' }],
    },
  ],
};

console.log(
  'Unit Group name:',
  unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
    'common:name'
  ]
);
console.log(
  'Unit Group validation:',
  unitGroup.validate().success ? 'PASSED' : 'FAILED'
);

// Example 7: Create an LCIA Method
console.log('\n=== Example 7: LCIA Method Creation ===');
const lciaMethod = createLCIAMethod();

// Set LCIA method information
lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Climate change - GWP 100' }];

lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.methodology =
  'IPCC 2013 methodology for global warming potential calculation';

lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.impactCategory =
  'Climate change';

lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation.areaOfProtection =
  'Natural environment';

console.log(
  'LCIA Method name:',
  lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation[
    'common:name'
  ]
);
console.log(
  'LCIA Method validation:',
  lciaMethod.validate().success ? 'PASSED' : 'FAILED'
);

// Example 8: Create a Life Cycle Model
console.log('\n=== Example 8: Life Cycle Model Creation ===');
const lifeCycleModel = createLifeCycleModel();

// Set life cycle model information
lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name.baseName =
  [{ '@xml:lang': 'en', '#text': 'Wind Power Plant Life Cycle Model' }];

lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name.treatmentStandardsRoutes =
  [{ '@xml:lang': 'en', '#text': 'Wind LCM' }];

// Set life cycle model comments
lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation[
  'common:generalComment'
] = [
  {
    '@xml:lang': 'en',
    '#text':
      'Product system model for wind power electricity generation with functional unit: 1 kWh electricity from wind power',
  },
];

// Set reference to process
lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.quantitativeReference.referenceToReferenceProcess =
  '0';

console.log(
  'Life Cycle Model name:',
  lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation
    .dataSetInformation.name.baseName
);
console.log(
  'Life Cycle Model validation:',
  lifeCycleModel.validate().success ? 'PASSED' : 'FAILED'
);

// Example 9: Using the Generic Factory Function
console.log('\n=== Example 9: Generic Factory Usage ===');
const genericContact = createTidasEntity('contact');
const genericFlow = createTidasEntity('flow');
const genericProcess = createTidasEntity('process');

console.log('Generic contact created:', genericContact.constructor.name);
console.log('Generic flow created:', genericFlow.constructor.name);
console.log('Generic process created:', genericProcess.constructor.name);

// Example 10: JSON Serialization and Validation
console.log('\n=== Example 10: JSON Operations ===');

// Convert objects to JSON
const contactJson = contact.toJSONString(2);
const flowJson = flow.toJSONString(2);

console.log('Contact JSON length:', contactJson.length);
console.log('Flow JSON length:', flowJson.length);

// Validate all created objects
const entities = [
  contact,
  flow,
  process,
  source,
  flowProperty,
  unitGroup,
  lciaMethod,
  lifeCycleModel,
];
const validationResults = entities.map((entity) => ({
  type: entity.constructor.name,
  valid: entity.validate().success,
}));

console.log('\n=== Validation Summary ===');
validationResults.forEach((result) => {
  console.log(`${result.type}: ${result.valid ? 'VALID' : 'INVALID'}`);
});

console.log('\n=== All TIDAS Entity Types Implemented Successfully! ===');
