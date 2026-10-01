/**
 * This file was automatically generated from tidas_processes
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  AnnualSupplyOrProductionVolumeMultiLang,
  CommonOther,
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
  Version,
  Year,
  dateTime,
} from './tidas_data_types';
import type { LocationsCategory } from './tidas_locations_category';

export interface ProcessReview {
  '@type':
    | 'Dependent internal review'
    | 'Independent internal review'
    | 'Independent external review'
    | 'Accredited third party review'
    | 'Independent review panel'
    | 'Not reviewed';
  /**
   * Scope of review regarding which aspects and components of the data set was reviewed or verified. In case of aggregated e.g. LCI results also and on which level of detail (e.g. LCI results only, included unit processes, ...) the review / verification was performed.
   */
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
                | 'Compliance with legal limits'
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
                | 'Compliance with legal limits'
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
                | 'Compliance with legal limits'
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
                | 'Compliance with legal limits'
                | 'Compliance with ISO 14040 to 14044'
                | 'Documentation'
                | 'Evidence collection by means of plant visits and/or interviews';
            }[];
      }[];
  /**
   * Data quality indicators serve to provide the reviewed key information on the data set in a defined, computer-readable (and hence searchable) form. This serves to support LCA practitioners to identify/select the highest quality and most appropriate data sets.
   */
  'common:dataQualityIndicators'?: {
    'common:dataQualityIndicator':
      | {
          '@name':
            | 'Technological representativeness'
            | 'Time representativeness'
            | 'Geographical representativeness'
            | 'Completeness'
            | 'Precision'
            | 'Methodological appropriateness and consistency'
            | 'Overall quality';
          '@value':
            | 'Very good'
            | 'Good'
            | 'Fair'
            | 'Poor'
            | 'Very poor'
            | 'Not evaluated / unknown'
            | 'Not applicable';
        }
      | {
          '@name':
            | 'Technological representativeness'
            | 'Time representativeness'
            | 'Geographical representativeness'
            | 'Completeness'
            | 'Precision'
            | 'Methodological appropriateness and consistency'
            | 'Overall quality';
          '@value':
            | 'Very good'
            | 'Good'
            | 'Fair'
            | 'Poor'
            | 'Very poor'
            | 'Not evaluated / unknown'
            | 'Not applicable';
        }[];
  };
  /**
   * Summary of the review. All the following items should be explicitly addressed: Representativeness, completeness, and precision of Inputs and Outputs for the process in its documented location, technology and time i.e. both completeness of technical model (product, waste, and elementary flows) and completeness of coverage of the relevant problem fields (environmental, human health, resource use) for this specific good, service, or process. Plausibility of data. Correctness and appropriateness of the data set documentation. Appropriateness of system boundaries, cut-off rules, LCI modelling choices such as e.g. allocation, consistency of included processes and of LCI methodology. If the data set comprises pre-calculated LCIA results, the correspondence of the Input and Output elementary flows (including their geographical validity) with the applied LCIA method(s) should be addressed by the reviewer. An overall quality statement on the data set may be included here.
   */
  'common:reviewDetails'?: FTMultiLang;
  /**
   * "Contact data set" of reviewer. The full name of reviewer(s) and institution(s) as well as a contact address and/or email should be provided in that contact data set.
   */
  'common:referenceToNameOfReviewerAndInstitution'?: GlobalReferenceType;
  /**
   * Further information from the review process, especially comments received from third parties once the data set has been published or additional reviewer comments from an additional external review.
   */
  'common:otherReviewDetails'?: FTMultiLang;
  /**
   * "Source data set" of the complete review report.
   */
  'common:referenceToCompleteReviewReport'?: GlobalReferenceType;
  'common:other'?: CommonOther;
}

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
          'common:other'?: CommonOther;
        };
        identifierOfSubDataSet?: String;
        'common:synonyms'?: FTMultiLang;
        complementingProcesses?: {
          referenceToComplementingProcess?: GlobalReferenceType;
        };
        classificationInformation: {
          'common:classification':
            | {
                'common:class': [
                  { '@level': LevelType; '@classId': string; '#text': string },
                  { '@level': LevelType; '@classId': string; '#text': string },
                  { '@level': LevelType; '@classId': string; '#text': string },
                  { '@level': LevelType; '@classId': string; '#text': string },
                ];
                'common:other'?: CommonOther;
                '@name'?: string;
                '@classes'?: string;
              }
            | {
                '@name': string;
                '@classes'?: string;
                'common:class': {
                  '@level': LevelType;
                  '@classId': string;
                  '#text': string;
                }[];
                'common:other'?: CommonOther;
              }[];
        };
        'common:generalComment': FTMultiLang;
        referenceToExternalDocumentation?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      quantitativeReference: {
        '@type':
          | 'Reference flow(s)'
          | 'Functional unit'
          | 'Other parameter'
          | 'Production period';
        referenceToReferenceFlow?: Int6 | Int6[];
        functionalUnitOrOther?: StringMultiLang;
        'common:other'?: CommonOther;
      };
      time: {
        'common:referenceYear': Year;
        'common:dataSetValidUntil'?: Year;
        'common:timeRepresentativenessDescription'?: FTMultiLang;
        'common:other'?: CommonOther;
      };
      geography: {
        locationOfOperationSupplyOrProduction: {
          '@location': LocationsCategory;
          '@latitudeAndLongitude'?: GIS;
          descriptionOfRestrictions?: FTMultiLang;
          'common:other'?: CommonOther;
        };
        subLocationOfOperationSupplyOrProduction?:
          | {
              '@subLocation'?: LocationsCategory;
              '@latitudeAndLongitude'?: GIS;
              descriptionOfRestrictions?: FTMultiLang;
              'common:other'?: CommonOther;
            }
          | {
              '@subLocation'?: LocationsCategory;
              '@latitudeAndLongitude'?: GIS;
              descriptionOfRestrictions?: FTMultiLang;
              'common:other'?: CommonOther;
            }[];
        'common:other'?: CommonOther;
      };
      technology?: {
        technologyDescriptionAndIncludedProcesses: FTMultiLang;
        referenceToIncludedProcesses?: GlobalReferenceType;
        technologicalApplicability?: FTMultiLang;
        referenceToTechnologyPictogramme?: GlobalReferenceType;
        referenceToTechnologyFlowDiagrammOrPicture?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      mathematicalRelations?: {
        modelDescription?: FTMultiLang;
        variableParameter?:
          | {
              '@name': MatV;
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
              'common:other'?: CommonOther;
            }
          | {
              '@name': MatV;
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
              'common:other'?: CommonOther;
            }[];
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    modellingAndValidation: {
      LCIMethodAndAllocation: {
        typeOfDataSet?:
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
          | 'Other'
          | (
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
              | 'Other'
            )[];
        deviationsFromLCIMethodApproaches?: FTMultiLang;
        modellingConstants?: FTMultiLang;
        deviationsFromModellingConstants?: FTMultiLang;
        referenceToLCAMethodDetails?: GlobalReferenceType;
        'common:other'?: CommonOther;
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
        annualSupplyOrProductionVolume: AnnualSupplyOrProductionVolumeMultiLang;
        samplingProcedure?: FTMultiLang;
        dataCollectionPeriod?: StringMultiLang;
        uncertaintyAdjustments?: FTMultiLang;
        useAdviceForDataSet?: FTMultiLang;
        'common:other'?: CommonOther;
      };
      completeness?: {
        completenessProductModel?:
          | 'All relevant flows quantified'
          | 'Relevant flows missing'
          | 'Topic not relevant'
          | 'No statement';
        referenceToSupportedImpactAssessmentMethods?: GlobalReferenceType;
        completenessElementaryFlows?:
          | {
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
            }
          | {
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
            }[];
        completenessOtherProblemField?: FTMultiLang;
        'common:other'?: CommonOther;
      };
      validation: {
        review: ProcessReview | ProcessReview[];
        'common:other'?: CommonOther;
      };
      complianceDeclarations: {
        compliance:
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:nomenclatureCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:methodologicalCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:reviewCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:documentationCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:qualityCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:other'?: CommonOther;
            }
          | {
              'common:referenceToComplianceSystem': GlobalReferenceType;
              'common:approvalOfOverallCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:nomenclatureCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:methodologicalCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:reviewCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:documentationCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:qualityCompliance':
                'Fully compliant' | 'Not compliant' | 'Not defined';
              'common:other'?: CommonOther;
            }[];
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    administrativeInformation: {
      'common:commissionerAndGoal': {
        'common:referenceToCommissioner': GlobalReferenceType;
        'common:project'?: StringMultiLang;
        'common:intendedApplications': FTMultiLang;
        'common:other'?: CommonOther;
      };
      dataGenerator?: {
        'common:referenceToPersonOrEntityGeneratingTheDataSet'?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      dataEntryBy: {
        'common:timeStamp': dateTime;
        'common:referenceToDataSetFormat': GlobalReferenceType;
        'common:referenceToConvertedOriginalDataSetFrom'?: GlobalReferenceType;
        'common:referenceToPersonOrEntityEnteringTheData': GlobalReferenceType;
        'common:referenceToDataSetUseApproval'?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      publicationAndOwnership: {
        'common:dateOfLastRevision'?: string;
        'common:dataSetVersion': Version;
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
        'common:other'?: CommonOther;
      };
      'common:other'?: CommonOther;
    };
    exchanges: {
      exchange: {
        '@dataSetInternalID': Int6;
        referenceToFlowDataSet: GlobalReferenceType;
        location?: LocationsCategory | String;
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
          'undefined' | 'log-normal' | 'normal' | 'triangular' | 'uniform';
        relativeStandardDeviation95In?: Perc;
        allocations?: {
          allocation:
            | {
                '@internalReferenceToCoProduct'?: Int6;
                '@allocatedFraction'?: Perc;
              }
            | {
                '@internalReferenceToCoProduct'?: Int6;
                '@allocatedFraction'?: Perc;
              }[];
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
          'common:other'?: CommonOther;
        };
        generalComment?: StringMultiLang;
        'common:other'?: CommonOther;
      }[];
      'common:other'?: CommonOther;
    };
    LCIAResults?: {
      LCIAResult?:
        | {
            referenceToLCIAMethodDataSet?: GlobalReferenceType;
            meanAmount: Real;
            uncertaintyDistributionType?:
              'undefined' | 'log-normal' | 'normal' | 'triangular' | 'uniform';
            relativeStandardDeviation95In?: Perc;
            generalComment?: StringMultiLang;
            'common:other'?: CommonOther;
          }
        | {
            referenceToLCIAMethodDataSet?: GlobalReferenceType;
            meanAmount: Real;
            uncertaintyDistributionType?:
              'undefined' | 'log-normal' | 'normal' | 'triangular' | 'uniform';
            relativeStandardDeviation95In?: Perc;
            generalComment?: StringMultiLang;
            'common:other'?: CommonOther;
          }[];
      'common:other'?: CommonOther;
    };
    'common:other'?: CommonOther;
  };
}
