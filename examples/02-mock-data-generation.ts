/**
 * Example 2: Mock Data Generation
 * 
 * This example demonstrates how to generate mock data using the integrated @anatine/zod-mock library.
 */

import {
  TidasContact,
  TidasProcess,
  TidasFlow,
  createContact,
  type MockOptions
} from '../src/core';

console.log('🎭 TIDAS SDK - Mock Data Generation Examples\n');

// Example 2.1: Generate mock data for an existing object
console.log('📝 2.1 Generate Mock Data for Existing Object');
const contact1 = new TidasContact();

try {
  const mockData = contact1.generateMock();
  console.log('Generated mock UUID:', contact1.getUUID() || 'No UUID in current data');
  
  // The mock data is generated but not applied to the current object
  contact1._data = mockData; // Apply the mock data
  console.log('Mock contact UUID:', contact1.getUUID());
  console.log('Mock contact name:', contact1.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));
} catch (error) {
  console.log('Mock generation failed:', error.message);
}

// Example 2.2: Create object with mock data using static method
console.log('\n📝 2.2 Create Object with Mock Data');
try {
  const mockContact = TidasContact.createMock();
  console.log('Mock contact created with UUID:', mockContact.getUUID());
  console.log('Mock contact name:', mockContact.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));
} catch (error) {
  console.log('Mock contact creation failed:', error.message);
}

// Example 2.3: Generate mock with custom fields
console.log('\n📝 2.3 Mock with Custom Fields');
const mockOptions: MockOptions = {
  customFields: {
    'contactDataSet.contactInformation.dataSetInformation.common:name.@xml:lang': 'en',
    'contactDataSet.contactInformation.dataSetInformation.common:name.#text': 'Custom Test Company',
    'contactDataSet.contactInformation.dataSetInformation.email': 'test@customcompany.com'
  }
};

const contact2 = new TidasContact();
try {
  contact2.fillWithMockData(mockOptions);
  console.log('Custom mock contact name:', contact2.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));
  console.log('Custom mock email:', contact2.get('contactDataSet.contactInformation.dataSetInformation.email'));
} catch (error) {
  console.log('Custom mock generation failed:', error.message);
}

// Example 2.4: Fill missing fields with mock data
console.log('\n📝 2.4 Fill Missing Fields');
const partialContact = createContact({
  contactDataSet: {
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '123e4567-e89b-12d3-a456-426614174000',
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Partial Company'
        }
        // Many fields are missing
      }
    }
  }
});

console.log('Before filling - validation:', partialContact.isValid() ? 'Valid' : 'Invalid');

try {
  partialContact.fillMissingFields();
  console.log('After filling - validation:', partialContact.isValid() ? 'Valid' : 'Invalid');
  console.log('Filled contact name (preserved):', partialContact.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));
} catch (error) {
  console.log('Fill missing fields failed:', error.message);
}

// Example 2.5: Mock data for Process objects
console.log('\n📝 2.5 Mock Process Data');
try {
  const mockProcess = TidasProcess.createMock({
    customFields: {
      'processDataSet.processInformation.dataSetInformation.common:name.baseName.@xml:lang': 'en',
      'processDataSet.processInformation.dataSetInformation.common:name.baseName.#text': 'Mock Steel Production Process',
      'processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location': 'US'
    }
  });
  
  console.log('Mock process name:', mockProcess.getMultiLangText('processDataSet.processInformation.dataSetInformation.common:name.baseName'));
  console.log('Mock process location:', mockProcess.get('processDataSet.processInformation.geography.locationOfOperationSupplyOrProduction.@location'));
} catch (error) {
  console.log('Mock process creation failed:', error.message);
}

// Example 2.6: Mock data for Flow objects
console.log('\n📝 2.6 Mock Flow Data');
try {
  const mockFlow = TidasFlow.createMock({
    customFields: {
      'flowDataSet.flowInformation.dataSetInformation.name.baseName.@xml:lang': 'en',
      'flowDataSet.flowInformation.dataSetInformation.name.baseName.#text': 'Mock Chemical Flow',
      'flowDataSet.flowInformation.dataSetInformation.CASNumber': '123-45-6'
    }
  });
  
  console.log('Mock flow name:', mockFlow.getMultiLangText('flowDataSet.flowInformation.dataSetInformation.name.baseName'));
  console.log('Mock flow CAS:', mockFlow.get('flowDataSet.flowInformation.dataSetInformation.CASNumber'));
} catch (error) {
  console.log('Mock flow creation failed:', error.message);
}

// Example 2.7: Testing with mock data
console.log('\n📝 2.7 Testing with Mock Data');
function validateContactStructure(contact: TidasContact): boolean {
  try {
    // Test basic operations
    const uuid = contact.getUUID();
    const name = contact.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name');
    const json = contact.toJSON();
    const validation = contact.validate();
    
    return uuid !== null && name.length > 0 && json.length > 0;
  } catch (error) {
    return false;
  }
}

try {
  const testContact = TidasContact.createMock();
  const structureValid = validateContactStructure(testContact);
  console.log('Mock contact structure test:', structureValid ? 'PASSED' : 'FAILED');
} catch (error) {
  console.log('Mock contact testing failed:', error.message);
}

// Example 2.8: Performance comparison
console.log('\n📝 2.8 Performance Comparison');
const iterations = 100;

// Measure manual creation time
console.time('Manual Creation');
for (let i = 0; i < iterations; i++) {
  const contact = createContact({
    contactDataSet: {
      contactInformation: {
        dataSetInformation: {
          'common:UUID': `test-uuid-${i}`,
          'common:name': {
            '@xml:lang': 'en',
            '#text': `Test Company ${i}`
          }
        }
      }
    }
  });
}
console.timeEnd('Manual Creation');

// Measure mock creation time
console.time('Mock Creation');
try {
  for (let i = 0; i < iterations; i++) {
    const mockContact = TidasContact.createMock({
      customFields: {
        'contactDataSet.contactInformation.dataSetInformation.common:UUID': `mock-uuid-${i}`
      }
    });
  }
  console.timeEnd('Mock Creation');
} catch (error) {
  console.timeEnd('Mock Creation');
  console.log('Mock creation performance test failed:', error.message);
}

// Example 2.9: Mock data validation
console.log('\n📝 2.9 Mock Data Validation');
try {
  const mockContact = TidasContact.createMock();
  const validation = mockContact.validate();
  
  console.log('Mock data validation:', validation.success ? 'VALID' : 'INVALID');
  if (!validation.success) {
    console.log('Validation errors (first 3):');
    validation.error?.issues.slice(0, 3).forEach((issue, index) => {
      console.log(`  ${index + 1}. ${issue.path.join('.')}: ${issue.message}`);
    });
  }
} catch (error) {
  console.log('Mock validation test failed:', error.message);
}

// Example 2.10: Combining real and mock data
console.log('\n📝 2.10 Combining Real and Mock Data');
const realContact = createContact({
  contactDataSet: {
    contactInformation: {
      dataSetInformation: {
        'common:UUID': 'real-company-uuid',
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Real Company Name'
        }
      }
    }
  }
});

console.log('Before mock fill - has email:', realContact.get('contactDataSet.contactInformation.dataSetInformation.email') ? 'Yes' : 'No');

try {
  realContact.fillMissingFields();
  console.log('After mock fill - has email:', realContact.get('contactDataSet.contactInformation.dataSetInformation.email') ? 'Yes' : 'No');
  console.log('Real name preserved:', realContact.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name'));
} catch (error) {
  console.log('Combining real and mock data failed:', error.message);
}

console.log('\n✅ Mock data generation examples completed!');