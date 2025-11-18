import { createContact } from '../src/core';

const contact = createContact();

// Quick way to set multi-language text

contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('test', 'en');

contact.contactDataSet.contactInformation.dataSetInformation[
  'common:name'
].setText?.('测试', 'zh');

console.log(
  contact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ][0]['#text']
);

console.log(
  contact.contactDataSet.contactInformation.dataSetInformation[
    'common:name'
  ].getText?.('fr')
);

console.log(contact.toJSONString());
