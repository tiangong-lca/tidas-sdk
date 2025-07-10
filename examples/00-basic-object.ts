/**
 * Example 1: Basic Object Creation
 *
 * This example demonstrates various ways to create TIDAS objects using the SDK.
 */
import { TidasContact, createContact, buildContact, ValidationOptions } from '@tidas-typescript-sdk';
import { fromJSON } from '@tidas-typescript-sdk/core';
import { Contact } from '@tidas-typescript-sdk/types';
import { ContactSchema } from '@tidas-typescript-sdk/schemas';

console.log('🚀 TIDAS SDK - Basic Object Creation Examples\n');

// Example 1.1: Direct instantiation
console.log('📝 1.1 Direct Instantiation');
const contact1 = new TidasContact();
console.log('Empty contact created:', contact1.getUUID() || 'No UUID yet');

// Example 1.2: Direct instantiation with data
console.log('\n📝 1.2 Direct Instantiation with Initial Data');
const contact2 = new TidasContact({
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact',
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@version': '1.1',
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd',
    contactInformation: {
      dataSetInformation: {
        'common:UUID': '123e4567-e89b-12d3-a456-426614174000',
        'common:shortName': {
          '@xml:lang': 'en',
          '#text': 'ExCo'
        },
        'common:name': {
          '@xml:lang': 'en',
          '#text': 'Example Company'
        },
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': '1',
              '@classId': 'company',
              '#text': 'Company'
            }
          }
        }
      }
    },
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': '2023-10-27T10:00:00Z',
        'common:referenceToDataSetFormat': {
          '@type': 'contactDataSet',
          '@refObjectId': '123e4567-e89b-12d3-a456-426614174000',
          '@version': '1.1',
          '@uri': 'http://example.com/dataset',
          'common:shortDescription': {
            '@xml:lang': 'en',
            '#text': 'Example Company'
          }
        }
      },
      publicationAndOwnership: {
        'common:dataSetVersion': '1.1',
        'common:permanentDataSetURI': 'http://example.com/dataset',
        'common:referenceToOwnershipOfDataSet': {
          '@type': 'contactDataSet',
          '@refObjectId': '123e4567-e89b-12d3-a456-426614174000',
          '@version': '1.1',
          '@uri': 'http://example.com/dataset',
          'common:shortDescription': {
            '@xml:lang': 'en',
            '#text': 'Example Company'
          }
        },
        'common:other': 'Example Company',
        },
        
      }
    }
  }
);
console.log('Contact with data created:', contact2.getUUID());
