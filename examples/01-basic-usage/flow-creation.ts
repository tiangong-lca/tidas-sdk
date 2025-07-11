#!/usr/bin/env tsx

/**
 * Basic Flow Creation Example
 * 
 * This example demonstrates how to create a TIDAS Flow object representing
 * a material or energy flow in an LCA study.
 */

import { createZodFlow } from '../../src/core/zod-factories';

console.log('🌊 TIDAS Flow Creation Example\n');

// 1. Create a new Flow using the factory function
console.log('1. Creating a new Flow object...');
const flowResult = createZodFlow({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const flow = flowResult.proxy;
console.log('✅ Flow proxy created successfully!');

// 2. Initialize the flow structure
console.log('\n2. Setting up basic flow structure...');

flow.flowDataSet = {} as any;
flow.flowDataSet.flowInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation.name = {} as any;

console.log('✅ Flow structure initialized!');

// 3. Set basic flow information
console.log('\n3. Setting flow identification...');

// Generate UUID for this flow
flowResult.generateUUID('flowDataSet.flowInformation.dataSetInformation.common:UUID');

// Set flow names using multi-language support
flowResult.setMultiLangText(
  'flowDataSet.flowInformation.dataSetInformation.name.baseName',
  'Steel, low-alloyed',
  'en'
);

// Set additional name information
flow.flowDataSet.flowInformation.dataSetInformation.name.treatmentStandardsRoutes = 'from cradle to gate';
flow.flowDataSet.flowInformation.dataSetInformation.name.mixAndLocationTypes = 'EU-27';

// Set CAS number for chemical identification
flow.flowDataSet.flowInformation.dataSetInformation.CASNumber = '7439-89-6';

// Set synonyms
flow.flowDataSet.flowInformation.dataSetInformation['common:synonyms'] = 'Iron, Steel alloy';

console.log('✅ Flow identification set!');

// 4. Set flow properties and classification
console.log('\n4. Setting flow properties...');

// Set type of data set
flow.flowDataSet.flowInformation.dataSetInformation.typeOfDataSet = 'Elementary flow';

// Initialize classification
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation = {} as any;
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification'] = {} as any;

// Set classification class
flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification']['common:class'] = {
  '@classId': '1.1.1',
  '@level': '0',
  '#text': 'Materials'
};

console.log('✅ Flow properties set!');

// 5. Set quantitative reference
console.log('\n5. Setting quantitative reference...');

flow.flowDataSet.flowInformation.quantitativeReference = {} as any;
flow.flowDataSet.flowInformation.quantitativeReference.referenceToReferenceFlowProperty = {
  '@refObjectId': 'flow-property-uuid-here',
  '@type': 'flow property data set',
  '@version': '1.0'
};

console.log('✅ Quantitative reference set!');

// 6. Set modeling and validation information
console.log('\n6. Setting modeling information...');

flow.flowDataSet.modellingAndValidation = {} as any;
flow.flowDataSet.modellingAndValidation.LCIMethod = {} as any;

flow.flowDataSet.modellingAndValidation.LCIMethod.typeOfDataSet = 'Partly terminated system';
flowResult.setMultiLangText(
  'flowDataSet.modellingAndValidation.LCIMethod.deviationsFromLCIMethodPrinciple',
  'Standard LCA methodology applied',
  'en'
);

console.log('✅ Modeling information set!');

// 7. Set administrative information
console.log('\n7. Setting administrative information...');

flow.flowDataSet.administrativeInformation = {} as any;
flow.flowDataSet.administrativeInformation.dataEntryBy = {} as any;
flow.flowDataSet.administrativeInformation.publicationAndOwnership = {} as any;

// Set timestamp
flowResult.setCurrentTimestamp('flowDataSet.administrativeInformation.dataEntryBy.common:timeStamp');

// Set version and status
flow.flowDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0';
flow.flowDataSet.administrativeInformation.publicationAndOwnership['common:workflowAndPublicationStatus'] = 'Published';

console.log('✅ Administrative information set!');

// 8. Read back the flow information
console.log('\n8. Reading flow information:');
console.log(`   Name: ${flowResult.getMultiLangText('flowDataSet.flowInformation.dataSetInformation.name.baseName', 'en')}`);
console.log(`   CAS Number: ${flow.flowDataSet.flowInformation.dataSetInformation.CASNumber}`);
console.log(`   Type: ${flow.flowDataSet.flowInformation.dataSetInformation.typeOfDataSet}`);
console.log(`   UUID: ${flow.flowDataSet.flowInformation.dataSetInformation['common:UUID']}`);
console.log(`   Classification: ${flow.flowDataSet.flowInformation.dataSetInformation.classificationInformation['common:classification']['common:class']['#text']}`);
console.log(`   Treatment: ${flow.flowDataSet.flowInformation.dataSetInformation.name.treatmentStandardsRoutes}`);
console.log(`   Location: ${flow.flowDataSet.flowInformation.dataSetInformation.name.mixAndLocationTypes}`);

// 9. Build the final object
console.log('\n9. Building final flow object...');
const finalFlow = flowResult.buildObject();

console.log('Final flow structure (first level):');
console.log(JSON.stringify(finalFlow, null, 2));

// 10. Validate the flow
console.log('\n10. Validating flow data...');
const validation = flowResult.validate();

if (validation.success) {
  console.log('✅ Flow validation successful!');
  console.log('Flow is ready for use in LCA studies.');
} else {
  console.log('❌ Flow validation failed:');
  validation.error?.issues.forEach((issue, index) => {
    console.log(`   ${index + 1}. ${issue.message} at path: ${issue.path.join('.')}`);
  });
}

// 11. Show access log summary
console.log('\n11. Access summary:');
const accessLog = flowResult.getAccessLog();
const accessSummary = accessLog.reduce((acc, entry) => {
  acc[entry.type] = (acc[entry.type] || 0) + 1;
  return acc;
}, {} as Record<string, number>);

console.log(`   Total operations: ${accessLog.length}`);
console.log(`   Sets: ${accessSummary.set || 0}`);
console.log(`   Gets: ${accessSummary.get || 0}`);

console.log('\n🎉 Flow creation example completed!');
console.log('\n📋 Key Concepts Demonstrated:');
console.log('✅ Flow object creation with factory function');
console.log('✅ Multi-language text handling for flow names');
console.log('✅ Chemical identification (CAS numbers)');
console.log('✅ Flow classification and properties');
console.log('✅ Quantitative reference setup');
console.log('✅ LCI method information');
console.log('✅ Administrative metadata management');