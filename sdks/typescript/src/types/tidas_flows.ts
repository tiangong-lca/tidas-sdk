/**
 * This file was automatically generated from tidas_flows
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  CASNumber,
  FTMultiLang,
  GlobalReferenceType,
  Int5,
  Perc,
  Real,
  String,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';
import type { LocationsCategory } from './tidas_locations_category';

export interface Flows {
  flowDataSet: {
    '@xmlns': 'http://lca.jrc.it/ILCD/Flow';
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:ecn': 'http://eplca.jrc.ec.europa.eu/ILCD/Extensions/2018/ECNumber';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@locations': '../ILCDLocations.xml';
    '@xsi:schemaLocation': 'http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd';
    flowInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        name: {
          baseName: StringMultiLang;
          treatmentStandardsRoutes: StringMultiLang;
          mixAndLocationTypes: StringMultiLang;
          flowProperties?: StringMultiLang;
          'common:other'?: string;
        };
        'common:synonyms'?: FTMultiLang;
        classificationInformation: any | any;
        CASNumber?: CASNumber;
        sumFormula?: String;
        'common:generalComment'?: FTMultiLang;
        'common:other'?: string;
      };
      quantitativeReference: {
        referenceToReferenceFlowProperty: Int5;
        'common:other'?: string;
      };
      geography?: {
        locationOfSupply?: LocationsCategory;
        'common:other'?: string;
      };
      technology?: {
        technologicalApplicability?: FTMultiLang;
        referenceToTechnicalSpecification?: GlobalReferenceType;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    modellingAndValidation: {
      LCIMethod: {
        typeOfDataSet: 'Elementary flow' | 'Product flow' | 'Waste flow';
        'common:other'?: string;
      };
      complianceDeclarations: {
        compliance:
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:other'?: string;
            }
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:other'?: string;
            }[];
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    administrativeInformation: {
      dataEntryBy: {
        'common:timeStamp': dateTime;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:referenceToPersonOrEntityEnteringTheData'?: GlobalReferenceType;
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
    flowProperties: {
      flowProperty:
        | {
            '@dataSetInternalID': Int5;
            referenceToFlowPropertyDataSet: GlobalReferenceType;
            meanValue: Real;
            minimumValue?: Real;
            maximumValue?: Real;
            uncertaintyDistributionType?:
              | 'undefined'
              | 'log-normal'
              | 'normal'
              | 'triangular'
              | 'uniform';
            relativeStandardDeviation95In?: Perc;
            dataDerivationTypeStatus?:
              | 'Measured'
              | 'Calculated'
              | 'Estimated'
              | 'Unknown derivation';
            generalComment?: StringMultiLang;
            'common:other'?: string;
          }
        | {
            '@dataSetInternalID': Int5;
            referenceToFlowPropertyDataSet: GlobalReferenceType;
            meanValue: Real;
            minimumValue?: Real;
            maximumValue?: Real;
            uncertaintyDistributionType?:
              | 'undefined'
              | 'log-normal'
              | 'normal'
              | 'triangular'
              | 'uniform';
            relativeStandardDeviation95In?: Perc;
            dataDerivationTypeStatus?:
              | 'Measured'
              | 'Calculated'
              | 'Estimated'
              | 'Unknown derivation';
            generalComment?: StringMultiLang;
            'common:other'?: string;
          }[];
      'common:other'?: string;
    };
    'common:other'?: string;
  };
}
