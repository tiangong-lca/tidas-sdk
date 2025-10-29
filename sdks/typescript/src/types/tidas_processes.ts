/**
 * This file was automatically generated from tidas_processes
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  FTMultiLang,
  GIS,
  GlobalReferenceType,
  Int6,
  LevelType,
  MatR,
  MatV,
  Perc,
  Real,
  String,
  StringMultiLang,
  UUID,
  Year,
  dateTime,
} from './tidas_data_types';
import type { LocationsCategory } from './tidas_locations_category';

export interface Processes {
  processDataSet: {
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns': 'http://lca.jrc.it/ILCD/Process';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@version': '1.1';
    '@locations': '../ILCDLocations.xml';
    '@xsi:schemaLocation': string;
    processInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        name: {
          baseName: StringMultiLang;
          treatmentStandardsRoutes: StringMultiLang;
          mixAndLocationTypes: StringMultiLang;
          functionalUnitFlowProperties?: StringMultiLang;
          'common:other'?: string;
        };
        identifierOfSubDataSet?: String;
        'common:synonyms'?: FTMultiLang;
        complementingProcesses?: {
          referenceToComplementingProcess?: GlobalReferenceType;
        };
        classificationInformation: {
          'common:classification': {
            'common:class': [
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
            ];
            'common:other'?: string;
          };
        };
        'common:generalComment': FTMultiLang;
        referenceToExternalDocumentation?: GlobalReferenceType;
        'common:other'?: string;
      };
      quantitativeReference: {
        '@type':
          | 'Reference flow(s)'
          | 'Functional unit'
          | 'Other parameter'
          | 'Production period';
        referenceToReferenceFlow: Int6;
        functionalUnitOrOther?: StringMultiLang;
        'common:other'?: string;
      };
      time: {
        'common:referenceYear': Year;
        'common:dataSetValidUntil'?: Year;
        'common:timeRepresentativenessDescription'?: FTMultiLang;
        'common:other'?: string;
      };
      geography: {
        locationOfOperationSupplyOrProduction: {
          '@location': LocationsCategory;
          '@latitudeAndLongitude'?: GIS;
          descriptionOfRestrictions?: FTMultiLang;
          'common:other'?: string;
        };
        subLocationOfOperationSupplyOrProduction?: {
          '@subLocation'?: LocationsCategory;
          '@latitudeAndLongitude'?: GIS;
          descriptionOfRestrictions?: FTMultiLang;
          'common:other'?: string;
        };
        'common:other'?: string;
      };
      technology?: {
        technologyDescriptionAndIncludedProcesses: FTMultiLang;
        referenceToIncludedProcesses?: GlobalReferenceType;
        technologicalApplicability?: FTMultiLang;
        referenceToTechnologyPictogramme?: GlobalReferenceType;
        referenceToTechnologyFlowDiagrammOrPicture?: GlobalReferenceType;
        'common:other'?: string;
      };
      mathematicalRelations?: {
        modelDescription?: FTMultiLang;
        variableParameter?: {
          '@name'?: MatV;
          formula?: MatR;
          meanValue?: Real;
          minimumValue?: Real;
          maximumValue?: Real;
          uncertaintyDistributionType?:
            | 'undefined'
            | 'log-normal'
            | 'normal'
            | 'triangular'
            | 'uniform';
          relativeStandardDeviation95In?: Perc;
          comment?: StringMultiLang;
          'common:other'?: string;
        };
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    modellingAndValidation: {
      LCIMethodAndAllocation: {
        typeOfDataSet:
          | 'Unit process, single operation'
          | 'Unit process, black box'
          | 'LCI result'
          | 'Partly terminated system'
          | 'Avoided product system';
        LCIMethodPrinciple?:
          | 'Attributional'
          | 'Consequential'
          | 'Consequential with attributional components'
          | 'Not applicable'
          | 'Other';
        deviationsFromLCIMethodPrinciple?: FTMultiLang;
        LCIMethodApproaches?:
          | 'Allocation - market value'
          | 'Allocation - gross calorific value'
          | 'Allocation - net calorific value'
          | 'Allocation - exergetic content'
          | 'Allocation - element content'
          | 'Allocation - mass'
          | 'Allocation - volume'
          | 'Allocation - ability to bear'
          | 'Allocation - marginal causality'
          | 'Allocation - physical causality'
          | 'Allocation - 100% to main function'
          | 'Allocation - other explicit assignment'
          | 'Allocation - equal distribution'
          | 'Substitution - BAT'
          | 'Substitution - average, market price correction'
          | 'Substitution - average, technical properties correction'
          | 'Allocation - recycled content'
          | 'Substitution - recycling potential'
          | 'Substitution - average, no correction'
          | 'Substitution - specific'
          | 'Consequential effects - other'
          | 'Not applicable'
          | 'Other';
        deviationsFromLCIMethodApproaches?: FTMultiLang;
        modellingConstants?: FTMultiLang;
        deviationsFromModellingConstants?: FTMultiLang;
        referenceToLCAMethodDetails?: GlobalReferenceType;
        'common:other'?: string;
      };
      dataSourcesTreatmentAndRepresentativeness?: {
        dataCutOffAndCompletenessPrinciples: FTMultiLang;
        deviationsFromCutOffAndCompletenessPrinciples?: FTMultiLang;
        dataSelectionAndCombinationPrinciples?: FTMultiLang;
        deviationsFromSelectionAndCombinationPrinciples?: FTMultiLang;
        dataTreatmentAndExtrapolationsPrinciples?: FTMultiLang;
        deviationsFromTreatmentAndExtrapolationPrinciples?: FTMultiLang;
        referenceToDataHandlingPrinciples?: GlobalReferenceType;
        referenceToDataSource: GlobalReferenceType;
        percentageSupplyOrProductionCovered?: Perc;
        annualSupplyOrProductionVolume?: StringMultiLang;
        samplingProcedure?: FTMultiLang;
        dataCollectionPeriod?: StringMultiLang;
        uncertaintyAdjustments?: FTMultiLang;
        useAdviceForDataSet?: FTMultiLang;
        'common:other'?: string;
      };
      completeness?: {
        completenessProductModel?:
          | 'All relevant flows quantified'
          | 'Relevant flows missing'
          | 'Topic not relevant'
          | 'No statement';
        referenceToSupportedImpactAssessmentMethods?: GlobalReferenceType;
        completenessElementaryFlows?: {
          '@type'?:
            | 'Climate change'
            | 'Ozone depletion'
            | 'Summer smog'
            | 'Eutrophication'
            | 'Acidification'
            | 'Human toxicity'
            | 'Freshwater ecotoxicity'
            | 'Seawater eco-toxicity'
            | 'Terrestric eco-toxicity'
            | 'Radioactivity'
            | 'Land use'
            | 'Non-renewable material resource depletion'
            | 'Renewable material resource consumption'
            | 'Non-renewable primary energy depletion'
            | 'Renewable primary energy consumption'
            | 'Particulate matter/respiratory inorganics'
            | 'Species depletion'
            | 'Noise';
          '@value'?:
            | 'All relevant flows quantified'
            | 'Relevant flows missing'
            | 'Topic not relevant'
            | 'No statement';
        };
        completenessOtherProblemField?: FTMultiLang;
        'common:other'?: string;
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
          scope:
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
                method: {
                  '@name':
                    | 'Validation of data sources'
                    | 'Sample tests on calculations'
                    | 'Energy balance'
                    | 'Element balance'
                    | 'Cross-check with other source'
                    | 'Cross-check with other data set'
                    | 'Expert judgement'
                    | 'Mass balance'
                    | 'Compliance with legal limits'
                    | 'Compliance with ISO 14040 to 14044'
                    | 'Documentation'
                    | 'Evidence collection by means of plant visits and/or interviews';
                };
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
                method: {
                  '@name':
                    | 'Validation of data sources'
                    | 'Sample tests on calculations'
                    | 'Energy balance'
                    | 'Element balance'
                    | 'Cross-check with other source'
                    | 'Cross-check with other data set'
                    | 'Expert judgement'
                    | 'Mass balance'
                    | 'Compliance with legal limits'
                    | 'Compliance with ISO 14040 to 14044'
                    | 'Documentation'
                    | 'Evidence collection by means of plant visits and/or interviews';
                };
              }[];
          dataQualityIndicators?: {
            dataQualityIndicator?: {
              '@name'?:
                | 'Technological representativeness'
                | 'Time representativeness'
                | 'Geographical representativeness'
                | 'Completeness'
                | 'Precision'
                | 'Methodological appropriateness and consistency'
                | 'Overall quality';
              '@value'?:
                | 'Very good'
                | 'Good'
                | 'Fair'
                | 'Poor'
                | 'Very poor'
                | 'Not evaluated / unknown'
                | 'Not applicable';
            };
          };
          reviewDetails?: FTMultiLang;
          'common:referenceToNameOfReviewerAndInstitution'?: GlobalReferenceType;
          'common:otherReviewDetails'?: FTMultiLang;
          'common:referenceToCompleteReviewReport'?: GlobalReferenceType;
          'common:other'?: string;
        };
        'common:other'?: string;
      };
      complianceDeclarations: {
        compliance: {
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
        };
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    administrativeInformation: {
      'common:commissionerAndGoal': {
        'common:referenceToCommissioner': GlobalReferenceType;
        'common:project'?: StringMultiLang;
        'common:intendedApplications': FTMultiLang;
        'common:other'?: string;
      };
      dataGenerator?: {
        'common:referenceToPersonOrEntityGeneratingTheDataSet'?: GlobalReferenceType;
        'common:other'?: string;
      };
      dataEntryBy: {
        'common:timeStamp': dateTime;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:referenceToConvertedOriginalDataSetFrom'?: GlobalReferenceType;
        'common:referenceToPersonOrEntityEnteringTheData': GlobalReferenceType;
        'common:referenceToDataSetUseApproval'?: GlobalReferenceType;
        'common:other'?: string;
      };
      publicationAndOwnership: {
        'common:dateOfLastRevision'?: string;
        'common:dataSetVersion': string;
        'common:referenceToPrecedingDataSetVersion'?: GlobalReferenceType;
        'common:permanentDataSetURI': string;
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
        'common:referenceToRegistrationAuthority'?: GlobalReferenceType;
        'common:registrationNumber'?: String;
        'common:referenceToOwnershipOfDataSet': GlobalReferenceType;
        'common:copyright': 'true' | 'false';
        'common:referenceToEntitiesWithExclusiveAccess'?: GlobalReferenceType;
        'common:licenseType':
          | 'Free of charge for all users and uses'
          | 'Free of charge for some user types or use types'
          | 'Free of charge for members only'
          | 'License fee'
          | 'Other';
        'common:accessRestrictions'?: FTMultiLang;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    exchanges: {
      exchange: {
        '@dataSetInternalID': Int6;
        referenceToFlowDataSet: GlobalReferenceType;
        location?: String;
        functionType?:
          | 'General reminder flow'
          | 'Allocation reminder flow'
          | 'System expansion reminder flow';
        exchangeDirection: 'Input' | 'Output';
        referenceToVariable?: String;
        meanAmount: Real;
        resultingAmount: Real;
        minimumAmount?: Real;
        maximumAmount?: Real;
        uncertaintyDistributionType?:
          | 'undefined'
          | 'log-normal'
          | 'normal'
          | 'triangular'
          | 'uniform';
        relativeStandardDeviation95In?: Perc;
        allocations?: {
          allocation?: {
            '@internalReferenceToCoProduct'?: Int6;
            '@allocatedFraction'?: Perc;
          };
        };
        dataSourceType?:
          | 'Primary'
          | '> 90% primary'
          | 'Mixed primary / secondary'
          | 'Secondary';
        dataDerivationTypeStatus:
          | 'Measured'
          | 'Calculated'
          | 'Estimated'
          | 'Unknown derivation'
          | 'Missing important'
          | 'Missing unimportant';
        referencesToDataSource?: {
          referenceToDataSource?: GlobalReferenceType;
          'common:other'?: string;
        };
        generalComment?: StringMultiLang;
        'common:other'?: string;
      }[];
      'common:other'?: string;
    };
    LCIAResults: {
      LCIAResult: {
        referenceToLCIAMethodDataSet?: GlobalReferenceType;
        meanAmount: Real;
        uncertaintyDistributionType?:
          | 'undefined'
          | 'log-normal'
          | 'normal'
          | 'triangular'
          | 'uniform';
        relativeStandardDeviation95In?: Perc;
        generalComment?: StringMultiLang;
        'common:other'?: string;
      };
      'common:other'?: string;
    };
    'common:other'?: string;
  };
}
