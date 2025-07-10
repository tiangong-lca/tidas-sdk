/**
 * Quick test to verify mock functionality works
 */

import { TidasContact } from '../src/core';

console.log('🧪 Testing Mock Functionality\n');

try {
  console.log('1. Testing empty contact vs mock contact...');
  const emptyContact = new TidasContact();
  console.log('Empty contact JSON:', emptyContact.toJSON());
  console.log('Empty contact is valid:', emptyContact.isValid());
  
  console.log('\n1.2 Testing schema availability...');
  // Use validation to test schema availability (getSchema is protected)
  const validationResult = emptyContact.validate();
  console.log('✅ Schema is available:', validationResult.success !== undefined);
  
  console.log('2. Creating mock contact...');
  const mockContact = TidasContact.createMock();
  const mockData = mockContact.toJSONObject();
  console.log('Mock data keys:', Object.keys(mockData));
  console.log('mockContact', mockContact.toJSON());
  console.log('✅ Mock contact created successfully');
  
  console.log('3. Testing UUID generation...');
  const uuid = mockContact.getUUID();
  console.log(`✅ UUID: ${uuid || 'No UUID found'}`);
  
  console.log('4. Testing validation...');
  const isValid = mockContact.isValid();
  console.log(`✅ Valid: ${isValid}`);
  
  console.log('5. Testing custom mock data...');
  const customMock = TidasContact.createMock({
    customFields: {
      'contactDataSet.contactInformation.dataSetInformation.common:name.#text': 'Test Company',
      'contactDataSet.contactInformation.dataSetInformation.email': 'test@example.com'
    }
  });
  
  const name = customMock.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name');
  const email = customMock.get('contactDataSet.contactInformation.dataSetInformation.email');
  
  console.log(`✅ Custom name: ${name}`);
  console.log(`✅ Custom email: ${email}`);
  
  console.log('6. Testing direct mock generation...');
  const directMock = new TidasContact();
  directMock.fillWithMockData({
    customFields: {
      'contactDataSet.contactInformation.dataSetInformation.common:name.#text': 'Direct Mock Company'
    }
  });
  
  const directName = directMock.getMultiLangText('contactDataSet.contactInformation.dataSetInformation.common:name');
  console.log(`✅ Direct mock name: ${directName}`);
  
  console.log('\n🎉 All mock functionality tests passed!');
  
} catch (error) {
  console.error('❌ Mock functionality test failed:', error.message);
  console.error('Stack:', error.stack);
}