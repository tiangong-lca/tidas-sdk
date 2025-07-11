#!/usr/bin/env tsx

/**
 * Complete TIDAS Workflow Example
 * 
 * This example demonstrates a complete LCA workflow using multiple
 * TIDAS objects (Contact, Flow, Process) and their relationships.
 */

import { 
  createZodContact, 
  createZodFlow, 
  createZodProcess,
  createZodSource,
  createZodFlowProperty,
  createZodUnitGroup
} from '../../src/core/zod-factories';

console.log('🔄 Complete TIDAS LCA Workflow Example\n');

// Step 1: Create the data originator (Contact)
console.log('Step 1: Creating Data Originator Contact\n');

const contactResult = createZodContact({
  enableLogging: false, // Disable for cleaner output
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const contact = contactResult.proxy;

// Initialize and populate contact
contact.contactDataSet = {} as any;
contact.contactDataSet.contactInformation = {} as any;
contact.contactDataSet.contactInformation.dataSetInformation = {} as any;

contactResult.generateUUID('contactDataSet.contactInformation.dataSetInformation.common:UUID');
contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:name',
  'LCA Research Institute',
  'en'
);
contactResult.setMultiLangText(
  'contactDataSet.contactInformation.dataSetInformation.common:shortName',
  'LCA-RI',
  'en'
);

contact.contactDataSet.contactInformation.dataSetInformation.email = 'research@lca-institute.org';
contact.contactDataSet.contactInformation.dataSetInformation.WWWAddress = 'https://lca-institute.org';

// Administrative info
contact.contactDataSet.administrativeInformation = {} as any;
contact.contactDataSet.administrativeInformation.dataEntryBy = {} as any;
contact.contactDataSet.administrativeInformation.publicationAndOwnership = {} as any;

contactResult.setCurrentTimestamp('contactDataSet.administrativeInformation.dataEntryBy.common:timeStamp');
contact.contactDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0';

const contactUUID = contact.contactDataSet.contactInformation.dataSetInformation['common:UUID'];
console.log(`✅ Contact created: ${contactResult.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name', 'en')} (${contactUUID})`);

// Step 2: Create a Unit Group
console.log('\nStep 2: Creating Unit Group for Mass\n');

const unitGroupResult = createZodUnitGroup({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const unitGroup = unitGroupResult.proxy;

// Initialize unit group structure
unitGroup.unitGroupDataSet = {} as any;
unitGroup.unitGroupDataSet.unitGroupInformation = {} as any;
unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation = {} as any;

unitGroupResult.generateUUID('unitGroupDataSet.unitGroupInformation.dataSetInformation.common:UUID');
unitGroupResult.setMultiLangText(
  'unitGroupDataSet.unitGroupInformation.dataSetInformation.common:name',
  'Mass units',
  'en'
);

// Set reference unit
unitGroup.unitGroupDataSet.unitGroupInformation.quantitativeReference = {} as any;
unitGroup.unitGroupDataSet.unitGroupInformation.quantitativeReference.referenceToReferenceUnit = 'kg';

const unitGroupUUID = unitGroup.unitGroupDataSet.unitGroupInformation.dataSetInformation['common:UUID'];
console.log(`✅ Unit Group created: Mass units (${unitGroupUUID})`);

// Step 3: Create a Flow Property
console.log('\nStep 3: Creating Flow Property for Mass\n');

const flowPropertyResult = createZodFlowProperty({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const flowProperty = flowPropertyResult.proxy;

// Initialize flow property structure
flowProperty.flowPropertyDataSet = {} as any;
flowProperty.flowPropertyDataSet.flowPropertyInformation = {} as any;
flowProperty.flowPropertyDataSet.flowPropertyInformation.dataSetInformation = {} as any;

flowPropertyResult.generateUUID('flowPropertyDataSet.flowPropertyInformation.dataSetInformation.common:UUID');
flowPropertyResult.setMultiLangText(
  'flowPropertyDataSet.flowPropertyInformation.dataSetInformation.common:name',
  'Mass',
  'en'
);

// Reference to unit group
flowProperty.flowPropertyDataSet.flowPropertyInformation.quantitativeReference = {} as any;
flowProperty.flowPropertyDataSet.flowPropertyInformation.quantitativeReference.referenceToReferenceUnitGroup = {
  '@refObjectId': unitGroupUUID,
  '@type': 'unit group data set',
  '@version': '1.0'
};

const flowPropertyUUID = flowProperty.flowPropertyDataSet.flowPropertyInformation.dataSetInformation['common:UUID'];
console.log(`✅ Flow Property created: Mass (${flowPropertyUUID})`);

// Step 4: Create Material Flows
console.log('\nStep 4: Creating Material Flows\n');

// Input flow: Iron ore
const ironOreResult = createZodFlow({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const ironOre = ironOreResult.proxy;

ironOre.flowDataSet = {} as any;
ironOre.flowDataSet.flowInformation = {} as any;
ironOre.flowDataSet.flowInformation.dataSetInformation = {} as any;
ironOre.flowDataSet.flowInformation.dataSetInformation.name = {} as any;

ironOreResult.generateUUID('flowDataSet.flowInformation.dataSetInformation.common:UUID');
ironOreResult.setMultiLangText(
  'flowDataSet.flowInformation.dataSetInformation.name.baseName',
  'Iron ore',
  'en'
);

ironOre.flowDataSet.flowInformation.dataSetInformation.CASNumber = '1317-60-8';
// Note: These assignments may have type issues in the actual implementation
// ironOre.flowDataSet.flowInformation.dataSetInformation.typeOfDataSet = 'Elementary flow';

// Reference to flow property
ironOre.flowDataSet.flowInformation.quantitativeReference = {} as any;
ironOre.flowDataSet.flowInformation.quantitativeReference.referenceToReferenceFlowProperty = {
  '@refObjectId': flowPropertyUUID,
  '@type': 'flow property data set',
  '@version': '1.0'
};

const ironOreUUID = ironOre.flowDataSet.flowInformation.dataSetInformation['common:UUID'];
console.log(`✅ Iron ore flow created (${ironOreUUID})`);

// Output flow: Steel
const steelResult = createZodFlow({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const steel = steelResult.proxy;

steel.flowDataSet = {} as any;
steel.flowDataSet.flowInformation = {} as any;
steel.flowDataSet.flowInformation.dataSetInformation = {} as any;
steel.flowDataSet.flowInformation.dataSetInformation.name = {} as any;

steelResult.generateUUID('flowDataSet.flowInformation.dataSetInformation.common:UUID');
steelResult.setMultiLangText(
  'flowDataSet.flowInformation.dataSetInformation.name.baseName',
  'Steel, low-alloyed',
  'en'
);

steel.flowDataSet.flowInformation.dataSetInformation.CASNumber = '7439-89-6';

const steelUUID = steel.flowDataSet.flowInformation.dataSetInformation['common:UUID'];
console.log(`✅ Steel flow created (${steelUUID})`);

// Step 5: Create a Source for data documentation
console.log('\nStep 5: Creating Data Source\n');

const sourceResult = createZodSource({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const source = sourceResult.proxy;

source.sourceDataSet = {} as any;
source.sourceDataSet.sourceInformation = {} as any;
source.sourceDataSet.sourceInformation.dataSetInformation = {} as any;

sourceResult.generateUUID('sourceDataSet.sourceInformation.dataSetInformation.common:UUID');
sourceResult.setMultiLangText(
  'sourceDataSet.sourceInformation.dataSetInformation.common:shortName',
  'Steel Production Data 2023',
  'en'
);

source.sourceDataSet.sourceInformation.dataSetInformation.sourceType = 'Article in periodical';
source.sourceDataSet.sourceInformation.dataSetInformation.publicationType = 'Journal';

const sourceUUID = source.sourceDataSet.sourceInformation.dataSetInformation['common:UUID'];
console.log(`✅ Source created: Steel Production Data 2023 (${sourceUUID})`);

// Step 6: Create the main Process
console.log('\nStep 6: Creating Steel Production Process\n');

const processResult = createZodProcess({
  enableLogging: false,
  throwOnValidationError: false,
  defaultLanguage: 'en'
});

const process = processResult.proxy;

// Initialize process structure
process.processDataSet = {} as any;
process.processDataSet.processInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation = {} as any;
process.processDataSet.processInformation.dataSetInformation.name = {} as any;

processResult.generateUUID('processDataSet.processInformation.dataSetInformation.common:UUID');
processResult.setMultiLangText(
  'processDataSet.processInformation.dataSetInformation.name.baseName',
  'Steel production, blast furnace route',
  'en'
);

// Set process details
process.processDataSet.processInformation.dataSetInformation.name.treatmentStandardsRoutes = 'production';
process.processDataSet.processInformation.dataSetInformation.name.mixAndLocationTypes = 'EU-27 average';
process.processDataSet.processInformation.dataSetInformation.name.functionalUnitFlowProperties = '1 kg steel';

// Geography
process.processDataSet.processInformation.geography = {} as any;
process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction = {} as any;
process.processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction['@location'] = 'EU-27';

// Time
process.processDataSet.processInformation.time = {} as any;
process.processDataSet.processInformation.time.referenceYear = 2023;
process.processDataSet.processInformation.time.dataSetValidUntil = 2030;

// Technology description
process.processDataSet.processInformation.technology = {} as any;
processResult.setMultiLangText(
  'processDataSet.processInformation.technology.technologyDescriptionAndIncludedProcesses',
  'Integrated steel production via blast furnace and basic oxygen furnace route. Includes coke making, sintering, blast furnace operation, and steel making.',
  'en'
);

// Step 7: Define Process Exchanges
console.log('\nStep 7: Defining Process Exchanges\n');

process.processDataSet.exchanges = {} as any;
process.processDataSet.exchanges.exchange = [] as any;

// Input: Iron ore
process.processDataSet.exchanges.exchange[0] = {
  '@dataSetInternalID': '1',
  referenceToFlowDataSet: {
    '@refObjectId': ironOreUUID,
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Iron ore input'
  },
  meanAmount: 1.6,
  resultingAmount: 1.6,
  dataDerivationTypeStatus: 'Measured',
  inputGroup: '5', // Material inputs
  'common:generalComment': 'Iron ore consumption per kg steel produced'
};

// Input: Coal (for coke production)
const coalUUID = 'coal-uuid-placeholder';
process.processDataSet.exchanges.exchange[1] = {
  '@dataSetInternalID': '2',
  referenceToFlowDataSet: {
    '@refObjectId': coalUUID,
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Coal for coke making'
  },
  meanAmount: 0.8,
  resultingAmount: 0.8,
  dataDerivationTypeStatus: 'Calculated',
  inputGroup: '5'
};

// Output: Steel (reference product)
process.processDataSet.exchanges.exchange[2] = {
  '@dataSetInternalID': '3',
  referenceToFlowDataSet: {
    '@refObjectId': steelUUID,
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Steel, low-alloyed, reference product'
  },
  meanAmount: 1.0,
  resultingAmount: 1.0,
  dataDerivationTypeStatus: 'Measured',
  outputGroup: '0', // Reference product
  referenceToVariable: 'steel_production'
};

// Output: CO2 emissions
const co2UUID = 'co2-uuid-placeholder';
process.processDataSet.exchanges.exchange[3] = {
  '@dataSetInternalID': '4',
  referenceToFlowDataSet: {
    '@refObjectId': co2UUID,
    '@type': 'flow data set',
    '@version': '1.0',
    'common:shortDescription': 'Carbon dioxide, fossil'
  },
  meanAmount: 2.1,
  resultingAmount: 2.1,
  dataDerivationTypeStatus: 'Calculated',
  outputGroup: '4' // Direct emissions to air
};

console.log(`✅ Process exchanges defined: ${process.processDataSet.exchanges.exchange.length} exchanges`);

// Step 8: Set Administrative Information with References
console.log('\nStep 8: Setting Administrative Information\n');

process.processDataSet.administrativeInformation = {} as any;
process.processDataSet.administrativeInformation.dataEntryBy = {} as any;
process.processDataSet.administrativeInformation.publicationAndOwnership = {} as any;

// Reference to data originator
process.processDataSet.administrativeInformation.dataEntryBy['common:referenceToPersonOrEntityEnteringTheData'] = {
  '@refObjectId': contactUUID,
  '@type': 'contact data set',
  '@version': '1.0',
  'common:shortDescription': 'LCA Research Institute'
};

// Reference to data source
process.processDataSet.administrativeInformation.dataEntryBy['common:referenceToDataSource'] = {
  '@refObjectId': sourceUUID,
  '@type': 'source data set',
  '@version': '1.0',
  'common:shortDescription': 'Steel Production Data 2023'
};

processResult.setCurrentTimestamp('processDataSet.administrativeInformation.dataEntryBy.common:timeStamp');
process.processDataSet.administrativeInformation.publicationAndOwnership['common:dataSetVersion'] = '1.0.0';

const processUUID = process.processDataSet.processInformation.dataSetInformation['common:UUID'];
console.log(`✅ Process administrative info set with references`);

// Step 9: Build and Validate All Objects
console.log('\nStep 9: Building and Validating Complete Dataset\n');

const objects = [
  { name: 'Contact', result: contactResult },
  { name: 'Unit Group', result: unitGroupResult },
  { name: 'Flow Property', result: flowPropertyResult },
  { name: 'Iron Ore Flow', result: ironOreResult },
  { name: 'Steel Flow', result: steelResult },
  { name: 'Source', result: sourceResult },
  { name: 'Process', result: processResult }
];

console.log('Validation Summary:');
objects.forEach(obj => {
  const validation = obj.result.validate();
  const status = validation.success ? '✅ PASS' : '❌ FAIL';
  const errorCount = validation.success ? 0 : validation.error?.issues.length || 0;
  console.log(`   ${obj.name}: ${status} ${errorCount > 0 ? `(${errorCount} issues)` : ''}`);
});

// Step 10: Create Dataset Relationships Map
console.log('\nStep 10: Dataset Relationships\n');

const relationships = {
  process: {
    uuid: processUUID,
    name: 'Steel production, blast furnace route',
    references: {
      inputs: [
        { uuid: ironOreUUID, name: 'Iron ore', amount: 1.6 },
        { uuid: coalUUID, name: 'Coal', amount: 0.8 }
      ],
      outputs: [
        { uuid: steelUUID, name: 'Steel, low-alloyed', amount: 1.0 },
        { uuid: co2UUID, name: 'CO2 emissions', amount: 2.1 }
      ],
      dataOriginator: { uuid: contactUUID, name: 'LCA Research Institute' },
      dataSource: { uuid: sourceUUID, name: 'Steel Production Data 2023' },
      flowProperty: { uuid: flowPropertyUUID, name: 'Mass' },
      unitGroup: { uuid: unitGroupUUID, name: 'Mass units' }
    }
  }
};

console.log('Process-centered relationship map:');
console.log(`📊 Process: ${relationships.process.name} (${relationships.process.uuid})`);
console.log(`   📥 Inputs: ${relationships.process.references.inputs.length} flows`);
relationships.process.references.inputs.forEach(input => {
  console.log(`      - ${input.name}: ${input.amount} kg`);
});
console.log(`   📤 Outputs: ${relationships.process.references.outputs.length} flows`);
relationships.process.references.outputs.forEach(output => {
  console.log(`      - ${output.name}: ${output.amount} kg`);
});
console.log(`   👤 Data Originator: ${relationships.process.references.dataOriginator.name}`);
console.log(`   📄 Data Source: ${relationships.process.references.dataSource.name}`);
console.log(`   📏 Flow Property: ${relationships.process.references.flowProperty.name}`);
console.log(`   📐 Unit Group: ${relationships.process.references.unitGroup.name}`);

// Step 11: Export Final Objects
console.log('\nStep 11: Exporting Final Objects\n');

const finalDataset = {
  metadata: {
    created: new Date().toISOString(),
    creator: 'TIDAS TypeScript SDK Complete Workflow Example',
    version: '1.0.0',
    description: 'Complete LCA dataset for steel production'
  },
  objects: {
    contact: contactResult.buildObject(),
    unitGroup: unitGroupResult.buildObject(),
    flowProperty: flowPropertyResult.buildObject(),
    flows: {
      ironOre: ironOreResult.buildObject(),
      steel: steelResult.buildObject()
    },
    source: sourceResult.buildObject(),
    process: processResult.buildObject()
  },
  relationships: relationships
};

console.log(`✅ Complete dataset exported with ${Object.keys(finalDataset.objects).length} main object types`);
console.log(`   - Objects ready for JSON serialization: ${JSON.stringify(finalDataset).length} characters`);

// Step 12: Workflow Summary
console.log('\nStep 12: Workflow Summary\n');

console.log('🎉 Complete TIDAS LCA workflow demonstrated!');
console.log('\n📋 Workflow Steps Completed:');
console.log('✅ 1. Created data originator contact');
console.log('✅ 2. Defined unit group for mass measurements');
console.log('✅ 3. Created flow property for mass');
console.log('✅ 4. Defined material flows (iron ore, steel)');
console.log('✅ 5. Created data source documentation');
console.log('✅ 6. Built complete process with exchanges');
console.log('✅ 7. Linked all objects through UUID references');
console.log('✅ 8. Validated complete dataset');
console.log('✅ 9. Created relationship mapping');
console.log('✅ 10. Exported ready-to-use dataset');

console.log('\n🔗 Key Integration Concepts Demonstrated:');
console.log('✅ Multi-object creation and coordination');
console.log('✅ UUID-based reference linking');
console.log('✅ Hierarchical data structure building');
console.log('✅ Cross-object validation');
console.log('✅ Metadata and provenance tracking');
console.log('✅ Complete LCA process modeling');
console.log('✅ Dataset export and serialization');

console.log('\n📊 Final Dataset Statistics:');
console.log(`Objects created: ${Object.keys(finalDataset.objects).length + Object.keys(finalDataset.objects.flows).length}`);
console.log(`Process exchanges: ${process.processDataSet.exchanges.exchange.length}`);
console.log(`Cross-references: ${Object.keys(relationships.process.references).length}`);
console.log(`Total validation issues: ${objects.reduce((acc, obj) => acc + (obj.result.validate().error?.issues.length || 0), 0)}`);

// Optional: Show sample of final JSON structure
console.log('\n📄 Sample of exported JSON structure:');
console.log(JSON.stringify({
  metadata: finalDataset.metadata,
  objectCount: Object.keys(finalDataset.objects).length,
  sampleProcess: {
    uuid: processUUID,
    name: relationships.process.name,
    exchangeCount: process.processDataSet.exchanges.exchange.length
  }
}, null, 2));