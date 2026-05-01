/**
 * This file was automatically generated from tidas_unitgroups
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  CommonOther,
  FTMultiLang,
  GlobalReferenceType,
  Int5,
  LevelType,
  Real,
  String,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';

export interface Unitgroups {
  unitGroupDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/UnitGroup';
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/UnitGroup ../../schemas/ILCD_UnitGroupDataSet.xsd';
    unitGroupInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        'common:name': StringMultiLang;
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
        referenceToReferenceUnit: Int5;
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    modellingAndValidation: {
      complianceDeclarations: {
        compliance:
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:other'?: CommonOther;
            }
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:other'?: CommonOther;
            }[];
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': dateTime;
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
    units?: {
      unit?:
        | {
            '@dataSetInternalID'?: Int5;
            name?: String;
            meanValue?: Real;
            generalComment?: StringMultiLang;
            'common:other'?: CommonOther;
          }
        | {
            '@dataSetInternalID'?: Int5;
            name?: String;
            meanValue?: Real;
            generalComment?: StringMultiLang;
          }[];
      'common:other'?: CommonOther;
    };
    'common:other'?: CommonOther;
  };
}
