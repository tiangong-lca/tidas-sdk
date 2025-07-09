/**
 * This file was automatically generated from tidas_unitgroups
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
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
            'common:other'?: string;
          };
        };
        'common:generalComment'?: FTMultiLang;
        'common:other'?: string;
      };
      quantitativeReference: {
        referenceToReferenceUnit: Int5;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    modellingAndValidation: {
      complianceDeclarations: {
        compliance: {
          'common:referenceToComplianceSystem': GlobalReferenceType;
          'common:approvalOfOverallCompliance':
            | 'Fully compliant'
            | 'Not compliant'
            | 'Not defined';
          'common:other'?: string;
        };
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
    units?: {
      unit?:
        | {
            '@dataSetInternalID'?: Int5;
            name?: String;
            meanValue?: Real;
            generalComment?: StringMultiLang;
            'common:other'?: string;
          }
        | {
            '@dataSetInternalID'?: Int5;
            name?: String;
            meanValue?: Real;
            generalComment?: StringMultiLang;
          }[];
      'common:other'?: string;
    };
    'common:other'?: string;
  };
}
