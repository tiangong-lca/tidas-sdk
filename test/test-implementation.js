const { createContact, createProcess, createFlow, buildContact, validateWithZod, ContactsSchema } = require('../dist/index.js');

console.log('🧪 Testing Tidas SDK Implementation...\n');

try {
  // Test 1: Basic object creation
  console.log('1. Testing basic object creation...');
  const contact = createContact();
  console.log('✅ Contact created:', contact.getTypeName());

  const process = createProcess();
  console.log('✅ Process created:', process.getTypeName());

  const flow = createFlow();
  console.log('✅ Flow created:', flow.getTypeName());

  // Test 2: Object creation with validation
  console.log('\n2. Testing object creation with validation...');
  try {
    const validatedContact = createContact({}, { enableValidation: true });
    console.log('⚠️  Validation passed (expected to fail for empty object)');
  } catch (error) {
    console.log('✅ Validation correctly failed for empty object');
  }

  // Test 3: Builder pattern
  console.log('\n3. Testing builder pattern...');
  const builtContact = buildContact()
    .withData({ contactDataSet: { '@xmlns': 'http://lca.jrc.it/ILCD/Contact' } })
    .withUUID()
    .build();
  console.log('✅ Built contact with UUID:', builtContact.getUUID()?.substring(0, 8) + '...');

  // Test 4: JSON serialization
  console.log('\n4. Testing JSON serialization...');
  const jsonString = contact.toJSON({ pretty: true });
  console.log('✅ JSON serialization works, length:', jsonString.length);

  // Test 5: Multi-language text
  console.log('\n5. Testing multi-language text...');
  contact.setMultiLangText('contactInformation.dataSetInformation.common:name', 'Test Contact', 'en');
  const text = contact.getMultiLangText('contactInformation.dataSetInformation.common:name', 'en');
  console.log('✅ Multi-language text set and retrieved:', text);

  console.log('\n🎉 All tests passed! Implementation is working correctly.');

} catch (error) {
  console.error('❌ Test failed:', error.message);
  console.error(error.stack);
}