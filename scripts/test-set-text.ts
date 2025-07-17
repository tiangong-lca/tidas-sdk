import { createContact } from '../src/core';

const contact = createContact();

// Quick way to set multi-language text

contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('test', 'en');

contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('测试', 'zh');

// contact.contactDataSet.contactInformation.dataSetInformation['common:name'] = [
//   { '@xml:lang': 'fr', '#text': 'test' },
// ];

console.log(
  contact.contactDataSet.contactInformation.dataSetInformation['common:name']
);

console.log(contact.toJSONString());
