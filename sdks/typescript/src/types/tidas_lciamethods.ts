/**
 * This file was automatically generated from tidas_lciamethods
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  FTMultiLang,
  GIS,
  GlobalReferenceType,
  Int6,
  LevelType,
  Perc,
  Real,
  ST,
  STMultiLang,
  String,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';

export interface Lciamethods {
  LCIAMethodDataSet: {
    '@xmlns'?: 'http://lca.jrc.it/ILCD/LCIAMethod';
    '@xmlns:common'?: 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:xsi'?: 'http://www.w3.org/2001/XMLSchema-instance';
    '@version'?: '1.1';
    '@xsi:schemaLocation'?: 'http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd';
    LCIAMethodInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        'common:name': StringMultiLang;
        methodology?: string;
        classificationInformation: {
          'common:classification': {
            'common:class': [
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
            ];
            'common:other'?: string;
          };
        };
        impactCategory?:
          | 'Climate change'
          | 'Ozone depletion'
          | 'Terrestrial Eutrophication'
          | 'Aquatic Eutrophication'
          | 'Acidification'
          | 'Photochemical ozone creation'
          | 'Land use'
          | 'Abiotic resource depletion'
          | 'Biotic resource depletion'
          | 'Ionizing radiation'
          | 'Cancer human health effects'
          | 'Non-cancer human health effects'
          | 'Respiratory inorganics'
          | 'Aquatic eco-toxicity'
          | 'Terrestrial eco-toxicity'
          | 'other';
        areaOfProtection?:
          | 'Natural resources'
          | 'Natural environment'
          | 'Human health'
          | 'Other';
        impactIndicator?: String;
        'common:generalComment'?: FTMultiLang;
        referenceToExternalDocumentation?: GlobalReferenceType;
        'common:other'?: string;
      };
      quantitativeReference: {
        referenceQuantity: GlobalReferenceType;
        'common:other'?: string;
      };
      time: {
        referenceYear: STMultiLang;
        duration: STMultiLang;
        timeRepresentativenessDescription: FTMultiLang;
        'common:other'?: string;
      };
      geography?: {
        interventionLocation?:
          | { '#text'?: string; '@latitudeAndLongitude'?: GIS }
          | string;
        intervensionSubLocation?:
          | { '#text'?: string; '@latitudeAndLongitude'?: GIS }
          | string;
        impactLocation?:
          | { '#text'?: string; '@latitudeAndLongitude'?: GIS }
          | string;
        geographicalRepresentativenessDescription?: FTMultiLang;
        'common:other'?: string;
      };
      impactModel: {
        modelName: ST;
        modelDescription: FTMultiLang;
        referenceToModelSource?: GlobalReferenceType;
        referenceToIncludedMethods?: GlobalReferenceType;
        consideredMechanisms?: STMultiLang;
        referenceToMethodologyFlowChart?: GlobalReferenceType;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    modellingAndValidation: {
      useAdviceForDataSet?: STMultiLang;
      LCIAMethodNormalisationAndWeighting: {
        typeOfDataSet:
          | 'Inventory indicator'
          | 'Mid-point indicator'
          | 'Damage indicator'
          | 'Area of Protection damage indicator'
          | 'Combined single-point indicator'
          | 'LCIA methodology documentation';
        LCIAMethodPrinciple:
          | 'Distance-to-target'
          | 'Critical surface-time'
          | 'Effective volumes'
          | 'AoP-Damage model'
          | 'Carrying capacity'
          | 'Resource dissipation'
          | 'other';
        deviationsFromLCIAMethodPrinciple?: FTMultiLang;
        normalisation?: 'true' | 'false';
        referenceToUsableNormalisationDataSets?: GlobalReferenceType;
        normalisationDescription?: STMultiLang;
        referenceToIncludedNormalisationDataSets?: GlobalReferenceType;
        weighting?: 'true' | 'false';
        referenceToUsableWeightingDataSets?: GlobalReferenceType;
        weightingDescription?: STMultiLang;
        referenceToIncludedWeightingDataSets?: GlobalReferenceType;
      };
      dataSources: {
        referenceToDataSource: GlobalReferenceType;
        'common:other'?: string;
      };
      completeness?: {
        completenessImpactCoverage?: Perc;
        inventoryItems?: Int6;
      };
      validation: {
        review: {
          '@type':
            | 'Dependent internal review'
            | 'Independent internal review'
            | 'Independent external review'
            | 'Accredited third party review'
            | 'Independent review panel'
            | 'Not reviewed';
          'common:scope'?:
            | {
                '@name':
                  | 'Raw data'
                  | 'Unit process(es), single operation'
                  | 'Unit process(es), black box'
                  | 'LCI results or Partly terminated system'
                  | 'LCIA results'
                  | 'Documentation'
                  | 'Life cycle inventory methods'
                  | 'LCIA results calculation'
                  | 'Goal and scope definition';
                'common:method':
                  | {
                      '@name':
                        | 'Validation of data sources'
                        | 'Sample tests on calculations'
                        | 'Energy balance'
                        | 'Element balance'
                        | 'Cross-check with other source'
                        | 'Cross-check with other data set'
                        | 'Expert judgement'
                        | 'Mass balance'
                        | 'Compliance with legal limitsRegulated Inputs and Outputs e.g. emission data are validated for compliance with legal limits, typically after relating and scaling the data to the regulated processes/sites etc.'
                        | 'Compliance with ISO 14040 to 14044'
                        | 'Documentation'
                        | 'Evidence collection by means of plant visits and/or interviews';
                    }
                  | {
                      '@name':
                        | 'Validation of data sources'
                        | 'Sample tests on calculations'
                        | 'Energy balance'
                        | 'Element balance'
                        | 'Cross-check with other source'
                        | 'Cross-check with other data set'
                        | 'Expert judgement'
                        | 'Mass balance'
                        | 'Compliance with legal limitsRegulated Inputs and Outputs e.g. emission data are validated for compliance with legal limits, typically after relating and scaling the data to the regulated processes/sites etc.'
                        | 'Compliance with ISO 14040 to 14044'
                        | 'Documentation'
                        | 'Evidence collection by means of plant visits and/or interviews';
                    }[];
              }
            | {
                '@name':
                  | 'Raw data'
                  | 'Unit process(es), single operation'
                  | 'Unit process(es), black box'
                  | 'LCI results or Partly terminated system'
                  | 'LCIA results'
                  | 'Documentation'
                  | 'Life cycle inventory methods'
                  | 'LCIA results calculation'
                  | 'Goal and scope definition';
                'common:method':
                  | {
                      '@name':
                        | 'Validation of data sources'
                        | 'Sample tests on calculations'
                        | 'Energy balance'
                        | 'Element balance'
                        | 'Cross-check with other source'
                        | 'Cross-check with other data set'
                        | 'Expert judgement'
                        | 'Mass balance'
                        | 'Compliance with legal limitsRegulated Inputs and Outputs e.g. emission data are validated for compliance with legal limits, typically after relating and scaling the data to the regulated processes/sites etc.'
                        | 'Compliance with ISO 14040 to 14044'
                        | 'Documentation'
                        | 'Evidence collection by means of plant visits and/or interviews';
                    }
                  | {
                      '@name':
                        | 'Validation of data sources'
                        | 'Sample tests on calculations'
                        | 'Energy balance'
                        | 'Element balance'
                        | 'Cross-check with other source'
                        | 'Cross-check with other data set'
                        | 'Expert judgement'
                        | 'Mass balance'
                        | 'Compliance with legal limitsRegulated Inputs and Outputs e.g. emission data are validated for compliance with legal limits, typically after relating and scaling the data to the regulated processes/sites etc.'
                        | 'Compliance with ISO 14040 to 14044'
                        | 'Documentation'
                        | 'Evidence collection by means of plant visits and/or interviews';
                    }[];
              }[];
          'common:reviewDetails'?: FTMultiLang;
          'common:referenceToNameOfReviewerAndInstitution'?: GlobalReferenceType;
          'common:otherReviewDetails'?: FTMultiLang;
          'common:referenceToCompleteReviewReport'?: GlobalReferenceType;
          'common:other'?: string;
        };
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
              'common:nomenclatureCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:methodologicalCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:reviewCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:documentationCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:qualityCompliance':
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
              'common:nomenclatureCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:methodologicalCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:reviewCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:documentationCompliance':
                | 'Fully compliant'
                | 'Not compliant'
                | 'Not defined';
              'common:qualityCompliance':
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
      'common:commissionerAndGoal'?: {
        'common:referenceToCommissioner'?: GlobalReferenceType;
        'common:project'?: StringMultiLang;
        'common:intendedApplications'?: FTMultiLang;
        'common:other'?: string;
      };
      dataGenerator: {
        'common:referenceToPersonOrEntityGeneratingTheDataSet': GlobalReferenceType;
        'common:other'?: string;
      };
      dataEntryBy: {
        'common:timeStamp': dateTime;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:referenceToConvertedOriginalDataSetFrom'?: GlobalReferenceType;
        'common:referenceToPersonOrEntityEnteringTheData'?: GlobalReferenceType;
        recommendationBy: {
          referenceToEntity: GlobalReferenceType;
          level:
            | 'Level I'
            | 'Level II'
            | 'Level III'
            | 'Interim'
            | 'Not recommended';
          meaning: FTMultiLang;
        };
        'common:other'?: string;
      };
      publicationAndOwnership: {
        'common:dateOfLastRevision': dateTime;
        'common:dataSetVersion': string;
        'common:referenceToPrecedingDataSetVersion'?: GlobalReferenceType;
        'common:permanentDataSetURI'?: string;
        'common:workflowAndPublicationStatus'?:
          | 'Working draft'
          | 'Final draft for internal review'
          | 'Final draft for external review'
          | 'Data set finalised; unpublished'
          | 'Under revision'
          | 'Withdrawn'
          | 'Data set finalised; subsystems published'
          | 'Data set finalised; entirely published';
        'common:referenceToUnchangedRepublication'?: GlobalReferenceType;
        'common:referenceToOwnershipOfDataSet': GlobalReferenceType;
        'common:copyright'?: 'true' | 'false';
        'common:accessRestrictions'?: FTMultiLang;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    characterisationFactors: {
      factor:
        | {
            referenceToFlowDataSet: GlobalReferenceType;
            location?: string;
            exchangeDirection: 'Input' | 'Output';
            meanValue: Real;
            minimumValue?: Real;
            maximumValue?: Real;
            uncertaintyDistributionType?:
              | 'undefined'
              | 'log-normal'
              | 'normalisation'
              | 'triangular'
              | 'uniform';
            relativeStandardDeviation95In?: Perc;
            dataDerivationTypeStatus?:
              | 'Measured'
              | 'Calculated'
              | 'Estimated'
              | 'Unknown derivation'
              | 'Missing important'
              | 'Missing unimportant';
            deviatingRecommendation:
              | 'Level I'
              | 'Level II'
              | 'Level III'
              | 'Interim'
              | 'Not recommended';
            referenceToDataSource?: GlobalReferenceType;
            generalComment?: StringMultiLang;
            'common:other'?: string;
          }
        | {
            referenceToFlowDataSet: GlobalReferenceType;
            location?: string;
            exchangeDirection: 'Input' | 'Output';
            meanValue: Real;
            minimumValue?: Real;
            maximumValue?: Real;
            uncertaintyType?:
              | 'undefined'
              | 'log-normal'
              | 'normalisation'
              | 'triangular'
              | 'uniform';
            relativeStandardDeviation95In?: Perc;
            dataDerivationTypeStatus?:
              | 'Measured'
              | 'Calculated'
              | 'Estimated'
              | 'Unknown derivation'
              | 'Missing important'
              | 'Missing unimportant';
            deviatingRecommendation:
              | 'Level I'
              | 'Level II'
              | 'Level III'
              | 'Interim'
              | 'Not recommended';
            referenceToDataSource?: {
              referenceToDataSource?: GlobalReferenceType;
            };
            generalComment?: StringMultiLang;
          }[];
      'common:other'?: string;
    };
    'common:other'?: string;
  };
}
