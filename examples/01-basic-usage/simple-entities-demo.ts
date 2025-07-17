#!/usr/bin/env tsx

/**
 * Simple TIDAS Entities Demo
 *
 * This example demonstrates basic entity creation with correct type usage
 * based on the actual generated types from the SDK.
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
} from '@tiangong-lca/tidas-sdk/core';

console.log('=== Simple TIDAS Entities Demo ===\n');

// Example 1: Create a Contact with correct structure
console.log('1. Creating Contact...');
const contact = createContact();

// Set basic contact information using the correct structure
contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'] =
  'contact-uuid-123';
contact.contactDataSet.contactInformation.dataSetInformation[
  'common:shortName'
] = [{ '@xml:lang': 'en', '#text': 'J. Smith' }];
contact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
  { '@xml:lang': 'en', '#text': 'Dr. Jane Smith' },
];

// Set required classification information
contact.contactDataSet.contactInformation.dataSetInformation.classificationInformation =
  {
    'common:classification': {
      'common:class': [
        { '@level': '0', '@classId': 'contact', '#text': 'Contact' },
        { '@level': '1', '@classId': 'person', '#text': 'Person' },
      ],
    },
  };

console.log('✓ Contact created successfully');
console.log(
  'Contact validation:',
  contact.validate().success ? 'PASSED' : 'FAILED'
);

// Example 2: Create a Flow with correct structure
console.log('\n2. Creating Flow...');
const flow = createFlow();

// Set flow information using the correct nested structure
flow.flowDataSet.flowInformation.dataSetInformation['common:UUID'] =
  'flow-uuid-456';
flow.flowDataSet.flowInformation.dataSetInformation.name = {
  baseName: [{ '@xml:lang': 'en', '#text': 'Carbon dioxide' }],
  treatmentStandardsRoutes: [{ '@xml:lang': 'en', '#text': 'Standard CO2' }],
  mixAndLocationTypes: [{ '@xml:lang': 'en', '#text': 'Global average' }],
};

// Set required classification and quantitative reference
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation =
  {};
flow.flowDataSet.flowInformation.quantitativeReference = {
  referenceToReferenceFlowProperty: '0',
};

console.log('✓ Flow created successfully');
console.log('Flow validation:', flow.validate().success ? 'PASSED' : 'FAILED');

// Example 3: Create a Process with correct structure
console.log('\n3. Creating Process...');
const process = createProcess();

// Set process information
process.processDataSet.processInformation.dataSetInformation['common:UUID'] =
  'process-uuid-789';
process.processDataSet.processInformation.dataSetInformation.name = {
  baseName: [
    { '@xml:lang': 'en', '#text': 'Electricity production, wind power' },
  ],
  treatmentStandardsRoutes: [
    { '@xml:lang': 'en', '#text': 'Wind electricity' },
  ],
  mixAndLocationTypes: [{ '@xml:lang': 'en', '#text': 'Onshore wind' }],
};

// Set required fields
process.processDataSet.processInformation.dataSetInformation.classificationInformation =
  {};
process.processDataSet.processInformation.dataSetInformation[
  'common:generalComment'
] = [
  { '@xml:lang': 'en', '#text': 'Wind power electricity generation process' },
];

// Set time information with correct property names
process.processDataSet.processInformation.time = {
  referenceYear: 2023,
  dataSetValidUntil: 2030,
};

console.log('✓ Process created successfully');
console.log(
  'Process validation:',
  process.validate().success ? 'PASSED' : 'FAILED'
);

// Example 4: Create other entities with minimal required data
console.log('\n4. Creating other entities...');

const source = createSource();
source.sourceDataSet.sourceInformation.dataSetInformation['common:UUID'] =
  'source-uuid-101';
source.sourceDataSet.sourceInformation.dataSetInformation['common:shortName'] =
  [{ '@xml:lang': 'en', '#text': 'IPCC Report' }];

const flowProperty = createFlowProperty();
flowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
  'common:UUID'
] = 'flowprop-uuid-102';
flowProperty.flowPropertyDataSet.flowPropertiesInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Mass' }];

const unitGroup = createUnitGroup();
unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
  'common:UUID'
] = 'unitgroup-uuid-103';
unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Mass units' }];

const lciaMethod = createLCIAMethod();
lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation[
  'common:UUID'
] = 'lcia-uuid-104';
lciaMethod.LCIAMethodDataSet.LCIAMethodInformation.dataSetInformation[
  'common:name'
] = [{ '@xml:lang': 'en', '#text': 'Climate change - GWP 100' }];

const lifeCycleModel = createLifeCycleModel();
lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation[
  'common:UUID'
] = 'lcm-uuid-105';
lifeCycleModel.lifeCycleModelDataSet.lifeCycleModelInformation.dataSetInformation.name =
  {
    baseName: [
      { '@xml:lang': 'en', '#text': 'Wind Power Plant Life Cycle Model' },
    ],
    treatmentStandardsRoutes: [{ '@xml:lang': 'en', '#text': 'Wind LCM' }],
    mixAndLocationTypes: [
      { '@xml:lang': 'en', '#text': 'Onshore wind system' },
    ],
  };

console.log('✓ All entities created successfully');

// Example 5: JSON serialization
console.log('\n5. JSON Operations...');
const contactJson = contact.toJSONString(2);
console.log('Contact JSON length:', contactJson.length);

// Example 6: Validation summary
console.log('\n6. Validation Summary...');
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

validationResults.forEach((result) => {
  console.log(`${result.type}: ${result.valid ? 'VALID' : 'INVALID'}`);
});

console.log('\n=== Simple Demo Completed Successfully! ===');

// Run the demo
if (require.main === module) {
  // This will run when the file is executed directly
}
