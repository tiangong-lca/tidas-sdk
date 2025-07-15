#!/usr/bin/env tsx

/**
 * Validation Configuration Demo
 * 
 * This example demonstrates how to use the optional ValidationConfig parameter
 * across all factory functions and entity classes in the TIDAS SDK.
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
  createContactsBatch,
  ValidationConfig 
} from '../../src/core';

// Example validation configuration
const strictValidationConfig: Partial<ValidationConfig> = {
  enableSchemaValidation: true,
  strictMode: true,
  validateOnAccess: true
};

const lenientValidationConfig: Partial<ValidationConfig> = {
  enableSchemaValidation: false,
  strictMode: false,
  validateOnAccess: false
};

async function demonstrateValidationConfig() {
  console.log('=== TIDAS SDK Validation Configuration Demo ===\n');

  // 1. Contact with strict validation
  console.log('1. Creating Contact with strict validation...');
  const strictContact = createContact({
    contactDataSet: {
      contactInformation: {
        dataSetInformation: {
          'common:name': [{ '@xml:lang': 'en', '#text': 'Strict Contact' }]
        }
      }
    }
  }, strictValidationConfig);
  console.log('✓ Contact created with strict validation');

  // 2. Flow with lenient validation
  console.log('\n2. Creating Flow with lenient validation...');
  const lenientFlow = createFlow({
    flowDataSet: {
      flowInformation: {
        dataSetInformation: {
          'common:name': [{ '@xml:lang': 'en', '#text': 'Lenient Flow' }]
        }
      }
    }
  }, lenientValidationConfig);
  console.log('✓ Flow created with lenient validation');

  // 3. Process with default validation (no config passed)
  console.log('\n3. Creating Process with default validation...');
  const defaultProcess = createProcess({
    processDataSet: {
      processInformation: {
        dataSetInformation: {
          'common:name': [{ '@xml:lang': 'en', '#text': 'Default Process' }]
        }
      }
    }
  });
  console.log('✓ Process created with default validation');

  // 4. Batch creation with validation config
  console.log('\n4. Creating batch of Contacts with validation config...');
  const contactBatch = createContactsBatch([
    { contactDataSet: { contactInformation: { dataSetInformation: { 'common:name': [{ '@xml:lang': 'en', '#text': 'Batch Contact 1' }] } } } },
    { contactDataSet: { contactInformation: { dataSetInformation: { 'common:name': [{ '@xml:lang': 'en', '#text': 'Batch Contact 2' }] } } } }
  ], strictValidationConfig);
  console.log(`✓ Created ${contactBatch.length} contacts in batch with strict validation`);

  // 5. Generic factory with validation config
  console.log('\n5. Using generic factory with validation config...');
  const _genericFlow = createTidasEntity('flow', {
    flowDataSet: {
      flowInformation: {
        dataSetInformation: {
          'common:name': [{ '@xml:lang': 'en', '#text': 'Generic Flow' }]
        }
      }
    }
  }, lenientValidationConfig);
  console.log('✓ Flow created using generic factory with lenient validation');

  // 6. Test all entity types with validation config
  console.log('\n6. Testing all entity types with validation config...');
  
  const entities = [
    createSource(undefined, strictValidationConfig),
    createFlowProperty(undefined, lenientValidationConfig),
    createUnitGroup(undefined, strictValidationConfig),
    createLCIAMethod(undefined, lenientValidationConfig),
    createLifeCycleModel(undefined, strictValidationConfig)
  ];
  
  console.log(`✓ Created ${entities.length} different entity types with validation configs`);

  // 7. Display validation states
  console.log('\n7. Validation state information:');
  console.log(`   - Strict Contact validation enabled: ${strictContact.getValidationConfig().enableSchemaValidation}`);
  console.log(`   - Lenient Flow validation enabled: ${lenientFlow.getValidationConfig().enableSchemaValidation}`);
  console.log(`   - Default Process validation enabled: ${defaultProcess.getValidationConfig().enableSchemaValidation}`);

  console.log('\n=== Demo completed successfully! ===');
}

// Run the demo
if (require.main === module) {
  demonstrateValidationConfig().catch(console.error);
}