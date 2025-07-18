/**
 * This file was automatically generated from tidas_contacts
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  GlobalReferenceType,
  LevelType,
  ST,
  STMultiLang,
  String,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';

export interface Contacts {
  contactDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Contact';
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd';
    contactInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        'common:shortName': StringMultiLang;
        'common:name': StringMultiLang;
        classificationInformation: {
          'common:classification': {
            'common:class':
              | [
                  { '@level': LevelType; '@classId': string; '#text': string },
                  { '@level': LevelType; '@classId': string; '#text': string },
                ]
              | { '@level': LevelType; '@classId': string; '#text': string };
          };
          'common:other'?: string;
        };
        contactAddress?: STMultiLang;
        email?: String;
        telephone?: String;
        telefax?: String;
        WWWAddress?: ST;
        centralContactPoint?: STMultiLang;
        contactDescriptionOrComment?: STMultiLang;
        referenceToContact?: GlobalReferenceType;
        referenceToLogo?: GlobalReferenceType;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': dateTime;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:other'?: string;
      };
      publicationAndOwnership: {
        'common:dataSetVersion': string;
        'common:referenceToPrecedingDataSetVersion'?: GlobalReferenceType;
        'common:permanentDataSetURI'?: string;
        'common:referenceToOwnershipOfDataSet': GlobalReferenceType;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    'common:other'?: string;
  };
  'common:other'?: string;
}
