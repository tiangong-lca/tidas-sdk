#!/usr/bin/env tsx

/**
 * Basic Process Creation Example
 * 
 * This example demonstrates how to create a TIDAS Process object representing
 * a unit process or system in an LCA study with exchanges.
 */

import { createZodProcess } from '../../src/core/zod-factories';

console.log('⚙️ TIDAS Process Creation Example\n');

// 1. Create a new Process using the factory function
console.log('1. Creating a new Process object...');
const processResult = createZodProcess({
  enableLogging: true,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const process = processResult.proxy;
console.log('✅ Process proxy created successfully!');

// 2. Initialize the process structure
console.log('\n2. Setting up basic process structure...');

process.processDataSet = {} as any;
process.processDataSet.processInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation.name = {} as any;

console.log('✅ Process structure initialized!');

// 3. Set basic process identification
console.log('\n3. Setting process identification...');

// Generate UUID for this process
processResult.generateUUID('processDataSet.processInformation.dataSetInformation.common:UUID');

// Set process name using multi-language support
processResult.setMultiLangText(
  'processDataSet.processInformation.dataSetInformation.name.baseName',
  'Steel production, electric arc furnace',
  'en'
);

// Set process type and treatment
process.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes = 'production';
process.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes = 'EU-27 average';
process.processDataSet.processInformation.dataSetInformation.name.functionalUnitFlowProperties = '1 kg steel';

console.log('✅ Process identification set!');

// 4. Set classification information
console.log('\n4. Setting process classification...');

process.processDataSet.processInformation.dataSetInformation.classificationInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation.classificationInformation['common:classification'] = [] as any;

// Add classification entry
process.processDataSet.processInformation.dataSetInformation.classificationInformation['common:classification'][0] = {
  '@name': 'ISIC',
  'common:class': {
    '@classId': '2410',
    '@level': '0',
    '#text': 'Manufacture of basic iron and steel'
  }
};

console.log('✅ Process classification set!');

// 5. Set geography information
console.log('\n5. Setting geography information...');

process.processDataSet.processInformation.geography = {} as any;
process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction = {} as any;

process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location'] = 'EU-27';
processResult.setMultiLangText(
  'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.common:shortDescription',
  'European Union 27 countries average',
  'en'
);

console.log('✅ Geography information set!');

// 6. Set technology and time information
console.log('\n6. Setting technology and time information...');

process.processDataSet.processInformation.technology = {} as any;
processResult.setMultiLangText(
  'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
  'Electric arc furnace steel production with scrap steel as main input',
  'en'
);

process.processDataSet.processInformation.time = {} as any;
process.processDataSet.processInformation.time.referenceYear = 2023;
process.processDataSet.processInformation.time.dataSetValidUntil = 2030;
processResult.setMultiLangText(
  'processDataSet.processInformation.time.timeRepresentativenessDescription',
  'Data represents average conditions for the reference year',
  'en'
);

console.log('✅ Technology and time information set!');

// 7. Set exchanges (inputs and outputs)
console.log('\n7. Setting process exchanges...');

process.processDataSet.exchanges = {} as any;
process.processDataSet.exchanges.exchange = [] as any;

// Input: Scrap steel
process.processDataSet.exchanges.exchange[0] = {
  '@dataSetInternalID': '1',
  referenceToFlowDataSet: {
    '@refObjectId': 'scrap-steel-uuid-here',
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Scrap steel'
  },
  meanAmount: 1.1,
  resultingAmount: 1.1,
  dataDerivationTypeStatus: 'Measured',
  inputGroup: '5'
};

// Input: Electricity
process.processDataSet.exchanges.exchange[1] = {
  '@dataSetInternalID': '2',
  referenceToFlowDataSet: {
    '@refObjectId': 'electricity-uuid-here',
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Electricity, medium voltage'
  },
  meanAmount: 0.5,
  resultingAmount: 0.5,
  dataDerivationTypeStatus: 'Calculated',
  inputGroup: '4'
};

// Output: Steel (reference product)
process.processDataSet.exchanges.exchange[2] = {
  '@dataSetInternalID': '3',
  referenceToFlowDataSet: {
    '@refObjectId': 'steel-uuid-here',
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Steel, low-alloyed'
  },
  meanAmount: 1.0,
  resultingAmount: 1.0,
  dataDerivationTypeStatus: 'Measured',
  outputGroup: '0',
  referenceToVariable: 'steel_output'
};

// Output: CO2 emissions
process.processDataSet.exchanges.exchange[3] = {
  '@dataSetInternalID': '4',
  referenceToFlowDataSet: {
    '@refObjectId': 'co2-uuid-here',
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Carbon dioxide'
  },
  meanAmount: 0.2,
  resultingAmount: 0.2,
  dataDerivationTypeStatus: 'Calculated',
  outputGroup: '4'
};

console.log('✅ Process exchanges set!');

// 8. Set administrative information
console.log('\n8. Setting administrative information...');

process.processDataSet.administrativeInformation = {} as any;
process.processDataSet.administrativeInformation.dataEntryBy = {} as any;
process.processDataSet.administrativeInformation.publicationAndOwnership = {} as any;

// Set timestamp and version
processResult.setCurrentTimestamp('processDataSet.administrativeInformation.dataEntryBy.common:timeStamp');
process.processDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0';
process.processDataSet.administrativeInformation.publicationAndOwnership['common:workflowAndPublicationStatus'] = 'Published';

console.log('✅ Administrative information set!');

// 9. Read back the process information
console.log('\n9. Reading process information:');
console.log(`   Name: ${processResult.getMultiLangText('processDataSet.processInformation.dataSetInformation.name.baseName', 'en')}`);
console.log(`   Location: ${process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location']}`);
console.log(`   Reference Year: ${process.processDataSet.processInformation.time.referenceYear}`);
console.log(`   Valid Until: ${process.processDataSet.processInformation.time.dataSetValidUntil}`);
console.log(`   Functional Unit: ${process.processDataSet.processInformation.dataSetInformation.name.functionalUnitFlowProperties}`);
console.log(`   Number of Exchanges: ${process.processDataSet.exchanges.exchange.length}`);

// Show exchange summary
console.log('\n   Exchange Summary:');
process.processDataSet.exchanges.exchange.forEach((exchange: any, index: number) => {
  const isInput = exchange.inputGroup !== undefined;
  const direction = isInput ? 'Input' : 'Output';
  console.log(`   ${index + 1}. ${direction}: ${exchange.referenceToFlowDataSet['common:shortDescription']} (${exchange.meanAmount} units)`);
});

// 10. Build the final object
console.log('\n10. Building final process object...');
const finalProcess = processResult.buildObject();

// Show structure overview (not full object due to size)
console.log('Process structure overview:');
console.log(`- processDataSet`);
console.log(`  - processInformation (${Object.keys(finalProcess.processDataSet?.processInformation || {}).length} sections)`);
console.log(`  - exchanges (${finalProcess.processDataSet?.exchanges?.exchange?.length || 0} exchanges)`);
console.log(`  - administrativeInformation`);

// 11. Validate the process
console.log('\n11. Validating process data...');
const validation = processResult.validate();

if (validation.success) {
  console.log('✅ Process validation successful!');
  console.log('Process is ready for use in LCA calculations.');
} else {
  console.log('❌ Process validation failed:');
  validation.error?.issues.slice(0, 5).forEach((issue: any, index: number) => {
    console.log(`   ${index + 1}. ${issue.message} at path: ${issue.path.join('.')}`);
  });
  if (validation.error?.issues.length! > 5) {
    console.log(`   ... and ${validation.error?.issues.length! - 5} more issues`);
  }
}

// 12. Show access log summary
console.log('\n12. Access summary:');
const accessLog = processResult.getAccessLog();
const accessSummary = accessLog.reduce((acc, entry) => {
  acc[entry.type] = (acc[entry.type] || 0) + 1;
  return acc;
}, {} as Record<string, number>);

console.log(`   Total operations: ${accessLog.length}`);
console.log(`   Sets: ${accessSummary.set || 0}`);
console.log(`   Gets: ${accessSummary.get || 0}`);

console.log('\n🎉 Process creation example completed!');
console.log('\n📋 Key Concepts Demonstrated:');
console.log('✅ Process object creation with complex structure');
console.log('✅ Process identification and classification');
console.log('✅ Geography and technology description');
console.log('✅ Time representativeness');
console.log('✅ Exchange modeling (inputs and outputs)');
console.log('✅ Reference flow and functional unit');
console.log('✅ Administrative metadata management');
console.log('✅ Complex object validation');