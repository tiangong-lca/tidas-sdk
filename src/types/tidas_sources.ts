/**
 * This file was automatically generated from tidas_sources
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  FTMultiLang,
  GlobalReferenceType,
  LevelType,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';

export interface Sources {
  sourceDataSet: {
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns': 'http://lca.jrc.it/ILCD/Source';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd';
    sourceInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        'common:shortName': StringMultiLang;
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': LevelType;
              '@classId': string;
              '#text': string;
            };
            'common:other'?: string;
          };
        };
        sourceCitation?: string;
        publicationType?:
          | 'Undefined'
          | 'Article in periodical'
          | 'Chapter in anthology'
          | 'Monograph'
          | 'Direct measurement'
          | 'Oral communication'
          | 'Personal written communication'
          | 'Questionnaire'
          | 'Software or database'
          | 'Other unpublished and grey literature';
        sourceDescriptionOrComment?: FTMultiLang;
        referenceToDigitalFile?: { '@uri'?: string };
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
        permanentDataSetURI?: string;
        'common:referenceToOwnershipOfDataSet': GlobalReferenceType;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    'common:other'?: string;
  };
}
