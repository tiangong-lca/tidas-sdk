/**
 * Advanced TIDAS Entity Usage Patterns
 *
 * This example demonstrates advanced patterns for working with TIDAS entities:
 * - Batch operations
 * - JSON import/export
 * - Entity relationships
 * - Data validation workflows
 */

import {
  createContactsBatch,
  createFlowsBatch,
  createProcessesBatch,
  createContact,
  createFlow,
  createProcess,
  createUnitGroup,
  createFlowProperty,
  TidasContact,
  TidasFlow,
  TidasProcess,
} from '@tiangong-lca/tidas-sdk/core';

import { Contact, Flow, Process } from '@tiangong-lca/tidas-sdk/types';

// Example 1: Batch Entity Creation
console.log('=== Example 1: Batch Entity Creation ===');

const contactsData: Partial<Contact>[] = [
  {}, // Empty data - will use defaults
  {}, // Empty data - will use defaults
  {}, // Empty data - will use defaults
];

const contacts = createContactsBatch(contactsData);

// Set different names for each contact
contacts[0].contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Dr. Alice Johnson' }];
contacts[1].contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Prof. Bob Wilson' }];
contacts[2].contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Ms. Carol Davis' }];

console.log(`Created ${contacts.length} contacts`);
contacts.forEach((contact, index) => {
  const name =
    contact.contactDataSet.contactInformation.dataSetInformation[
      'common:name'
    ].getText?.('en');
  console.log(`Contact ${index + 1}: ${name}`);
});

// Example 2: Building Related Entities (Flow -> Process relationship)
console.log('\n=== Example 2: Building Related Entities ===');

// Create a unit group for mass
const massUnitGroup = createUnitGroup();
massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Mass units' }];

// Create a flow property for mass
const massFlowProperty = createFlowProperty();
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Mass' }];

// Reference the unit group in the flow property
const unitGroupUUID =
  massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
    'common:UUID'
  ];
massFlowProperty.flowPropertyDataSet.flowPropertiesInformation.quantitativeReference.referenceToReferenceUnitGroup =
  {
    '@type': 'unit group data set',
    '@refObjectId': unitGroupUUID,
    '@version': '1.0.0',
    '@uri': '',
    'common:shortDescription': [{ '@xml:lang': 'en', '#text': 'Mass units' }],
  };

// Create a CO2 flow
const co2Flow = createFlow();
co2Flow.flowDataSet.flowInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Carbon dioxide' },
];

// Add flow property to the flow
const flowPropertyUUID =
  massFlowProperty.flowPropertyDataSet.flowPropertiesInformation
    .dataSetInformation['common:UUID'];
co2Flow.flowDataSet.flowProperties.flowProperty = {
  '@dataSetInternalID': '0',
  referenceToFlowPropertyDataSet: {
    '@type': 'flow property data set',
    '@refObjectId': flowPropertyUUID,
    '@version': '1.0.0',
    '@uri': '',
    'common:shortDescription': [{ '@xml:lang': 'en', '#text': 'Mass' }],
  },
  meanValue: '1.0',
};

// Create a process that emits CO2
const combustionProcess = createProcess();
combustionProcess.processDataSet.processInformation.dataSetInformation.name.baseName =
  [{ '@xml:lang': 'en', '#text': 'Natural gas combustion' }];

// Add CO2 as an output exchange
const co2FlowUUID =
  co2Flow.flowDataSet.flowInformation.dataSetInformation['common:UUID'];
combustionProcess.processDataSet.exchanges.exchange = [
  {
    '@dataSetInternalID': '0',
    referenceToFlowDataSet: {
      '@type': 'flow data set',
      '@refObjectId': co2FlowUUID,
      '@version': '1.0.0',
      '@uri': '',
      'common:shortDescription': [
        { '@xml:lang': 'en', '#text': 'Carbon dioxide' },
      ],
    },
    exchangeDirection: 'Output',
    meanAmount: '2.75', // kg CO2 per kWh natural gas
    resultingAmount: '2.75',
    dataDerivationTypeStatus: 'Calculated',
    'common:other': 'kg CO2 per kWh natural gas',
  },
];

console.log('Created related entities:');
console.log(
  '- Unit Group:',
  massUnitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text']
);
console.log(
  '- Flow Property:',
  massFlowProperty.flowPropertyDataSet.flowPropertiesInformation
    .dataSetInformation['common:name']?.[0]?.['#text']
);
console.log(
  '- Flow:',
  co2Flow.flowDataSet.flowInformation.dataSetInformation['common:name']?.[0]?.[
    '#text'
  ]
);
console.log(
  '- Process:',
  combustionProcess.processDataSet.processInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text']
);

// Example 3: JSON Import/Export Workflow
console.log('\n=== Example 3: JSON Import/Export Workflow ===');

// Export a contact to JSON
const exportedContactJSON = contacts[0].toJSONString(2);
console.log(
  'Exported contact JSON size:',
  exportedContactJSON.length,
  'characters'
);
console.log('Exported contact:', exportedContactJSON);

// Import from JSON (simulated - you would typically load from file)
const importedContactData = JSON.parse(exportedContactJSON);
const importedContact = createContact(importedContactData);

// Verify the imported contact
const originalName =
  contacts[0].contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text'];
const importedName =
  importedContact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text'];

console.log('Original contact name:', originalName);
console.log('Imported contact name:', importedName);
console.log('Import successful:', originalName === importedName);

// Example 4: Validation Workflow
console.log('\n=== Example 4: Validation Workflow ===');

// Create a flow with incomplete data to test validation
const incompleteFlow = createFlow();
// Intentionally leave some required fields empty

const validationResult = incompleteFlow.validate();
if (!validationResult.success) {
  console.log('Validation failed as expected for incomplete flow');
  console.log(
    'Number of validation errors:',
    validationResult.error?.issues?.length || 0
  );
} else {
  console.log('Flow validation passed (default values provided)');
}

// Create a complete flow and validate
const completeFlow = createFlow();
completeFlow.flowDataSet.flowInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Complete flow example' },
];

const completeValidation = completeFlow.validate();
console.log(
  'Complete flow validation:',
  completeValidation.success ? 'PASSED' : 'FAILED'
);

// Example 5: Entity Cloning and Modification
console.log('\n=== Example 5: Entity Cloning and Modification ===');

// Clone an existing contact
const originalContact = contacts[0];
const clonedContact = originalContact.clone();

// Modify the clone
clonedContact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Dr. Alice Johnson (Cloned)' }];

// Generate new UUID for the clone
clonedContact.contactDataSet.contactInformation.dataSetInformation[
  'common:UUID'
] = crypto.randomUUID();

const originalContactName =
  originalContact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text'];
const clonedContactName =
  clonedContact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ]?.[0]?.['#text'];

console.log('Original contact:', originalContactName);
console.log('Cloned contact:', clonedContactName);
console.log(
  'UUIDs are different:',
  originalContact.contactDataSet.contactInformation.dataSetInformation[
    'common:UUID'
  ] !==
    clonedContact.contactDataSet.contactInformation.dataSetInformation[
      'common:UUID'
    ]
);

// Example 6: Multi-language Support
console.log('\n=== Example 6: Multi-language Support ===');

const multiLangFlow = createFlow();

// Add multi-language names
multiLangFlow.flowDataSet.flowInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Water' },
  { '@xml:lang': 'de', '#text': 'Wasser' },
  { '@xml:lang': 'fr', '#text': 'Eau' },
  { '@xml:lang': 'es', '#text': 'Agua' },
];

// Add multi-language descriptions
multiLangFlow.flowDataSet.flowInformation.dataSetInformation[
  'common:generalComment'
] = [
  { '@xml:lang': 'en', '#text': 'Pure water for industrial processes' },
  { '@xml:lang': 'de', '#text': 'Reines Wasser für industrielle Prozesse' },
  { '@xml:lang': 'fr', '#text': 'Eau pure pour les processus industriels' },
];

console.log('Multi-language flow names:');
multiLangFlow.flowDataSet.flowInformation.dataSetInformation[
  'common:name'
]?.forEach((name) => {
  console.log(`- ${name['@xml:lang']}: ${name['#text']}`);
});

// Example 7: Performance Measurement
console.log('\n=== Example 7: Performance Measurement ===');

const startTime = performance.now();

// Create 100 flows rapidly
const manyFlows = createFlowsBatch(Array(100).fill({}));

// Set basic properties on all flows
manyFlows.forEach((flow, index) => {
  flow.flowDataSet.flowInformation.dataSetInformation['common:name'] = [
    { '@xml:lang': 'en', '#text': `Flow ${index + 1}` },
  ];
});

const endTime = performance.now();
console.log(
  `Created and configured ${manyFlows.length} flows in ${(endTime - startTime).toFixed(2)}ms`
);

// Validate all flows
const validationStartTime = performance.now();
const validationResults = manyFlows.map((flow) => flow.validate().success);
const validationEndTime = performance.now();

const successfulValidations = validationResults.filter(
  (result) => result
).length;
console.log(
  `Validated ${manyFlows.length} flows in ${(validationEndTime - validationStartTime).toFixed(2)}ms`
);
console.log(
  `${successfulValidations}/${manyFlows.length} flows passed validation`
);

console.log('\n=== Advanced Usage Patterns Complete! ===');
