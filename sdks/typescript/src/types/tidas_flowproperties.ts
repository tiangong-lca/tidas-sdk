/**
 * This file was automatically generated from tidas_flowproperties
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  CommonOther,
  FTMultiLang,
  GlobalReferenceType,
  LevelType,
  StringMultiLang,
  UUID,
} from './tidas_data_types';

export interface Flowproperties {
  flowPropertyDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/FlowProperty';
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd';
    flowPropertiesInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        'common:name': StringMultiLang;
        'common:synonyms'?: FTMultiLang;
        classificationInformation: {
          'common:classification': {
            'common:class': {
              '@level': LevelType;
              '@classId': string;
              '#text': string;
            };
            'common:other'?: CommonOther;
          };
        };
        'common:generalComment'?: FTMultiLang;
        'common:other'?: CommonOther;
      };
      quantitativeReference: {
        referenceToReferenceUnitGroup: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    modellingAndValidation?: {
      dataSourcesTreatmentAndRepresentativeness?: {
        referenceToDataSource?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      complianceDeclarations: {
        compliance:
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
            }
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
            }[];
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': string;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      publicationAndOwnership: {
        'common:dataSetVersion': string;
        'common:referenceToPrecedingDataSetVersion'?: GlobalReferenceType;
        'common:permanentDataSetURI'?: string;
        'common:referenceToOwnershipOfDataSet': GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    'common:other'?: CommonOther;
  };
}
