/**
 * This file was automatically generated from tidas_lifecyclemodels
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSON Schema file,
 * and run the generation script to regenerate this file.
 */

import type {
  CommonOther,
  FTMultiLang,
  GlobalReferenceType,
  LevelType,
  MatV,
  Real,
  StringMultiLang,
  UUID,
  dateTime,
} from './tidas_data_types';

export interface Lifecyclemodels {
  lifeCycleModelDataSet: {
    '@xmlns': 'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017';
    '@xmlns:acme': 'http://acme.com/custom';
    '@xmlns:common': 'http://lca.jrc.it/ILCD/Common';
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance';
    '@locations': '../ILCDLocations.xml';
    '@version': '1.1';
    '@xsi:schemaLocation': 'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017 ../../schemas/ILCD_LifeCycleModelDataSet.xsd';
    lifeCycleModelInformation: {
      dataSetInformation: {
        'common:UUID': UUID;
        name: {
          baseName: StringMultiLang;
          treatmentStandardsRoutes: StringMultiLang;
          mixAndLocationTypes: StringMultiLang;
          functionalUnitFlowProperties?: StringMultiLang;
          'common:other'?: CommonOther;
        };
        classificationInformation: {
          'common:classification': {
            'common:class': [
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
              { '@level': LevelType; '@classId': string; '#text': string },
            ];
            'common:other'?: CommonOther;
          };
        };
        referenceToResultingProcess?: GlobalReferenceType;
        'common:generalComment'?: FTMultiLang;
        referenceToExternalDocumentation?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      quantitativeReference: {
        referenceToReferenceProcess: string;
        'common:other'?: CommonOther;
      };
      technology: {
        groupDeclarations?: {
          group?:
            | { '@id'?: string; groupName?: StringMultiLang }
            | { '@id'?: string; groupName?: StringMultiLang }[];
        };
        processes: {
          processInstance?:
            | {
                '@dataSetInternalID': string;
                '@multiplicationFactor': string;
                referenceToProcess: GlobalReferenceType;
                scalingFactors?: Real;
                groups?: {
                  memberOf?:
                    | { '@groupId'?: string }
                    | { '@groupId'?: string }[];
                };
                parameters?: {
                  parameter?: { '@name'?: MatV } | { '@name'?: MatV }[];
                };
                connections?: {
                  outputExchange?:
                    | {
                        '@dominant'?: 'true' | 'false';
                        '@flowUUID': UUID;
                        downstreamProcess:
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }[];
                      }
                    | {
                        '@dominant'?: 'true' | 'false';
                        '@flowUUID': UUID;
                        downstreamProcess:
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }[];
                      }[];
                };
                'common:other'?: CommonOther;
              }[]
            | {
                '@dataSetInternalID': string;
                '@multiplicationFactor': string;
                referenceToProcess: GlobalReferenceType;
                scalingFactors?: Real;
                groups?: {
                  memberOf?:
                    | { '@groupId'?: string }
                    | { '@groupId'?: string }[];
                };
                parameters?: {
                  parameter?:
                    | { '@name'?: string; parameter?: Real }
                    | { '@name'?: string; parameter?: Real }[];
                };
                connections?: {
                  outputExchange:
                    | {
                        '@dominant'?: 'true' | 'false';
                        '@flowUUID': UUID;
                        downstreamProcess:
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }[];
                      }
                    | {
                        '@dominant'?: 'true' | 'false';
                        '@flowUUID': UUID;
                        downstreamProcess:
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }
                          | {
                              '@id': string;
                              '@flowUUID': UUID;
                              '@location'?: string;
                              '@dominant'?: 'true' | 'false';
                            }[];
                      }[];
                };
                'common:other'?: CommonOther;
              };
        };
        referenceToDiagram?: GlobalReferenceType;
        'common:other'?: CommonOther;
      };
    };
    modellingAndValidation: {
      dataSourcesTreatmentEtc?: {
        useAdviceForDataSet?: FTMultiLang;
        'common:other'?: CommonOther;
      };
      validation: {
        review:
          | {
              'common:referenceToNameOfReviewerAndInstitution': GlobalReferenceType;
              'common:otherReviewDetails'?: FTMultiLang;
              'common:referenceToCompleteReviewReport'?: GlobalReferenceType;
              'common:other'?: CommonOther;
            }
          | {
              'common:referenceToNameOfReviewerAndInstitution': GlobalReferenceType;
              'common:otherReviewDetails'?: FTMultiLang;
              'common:referenceToCompleteReviewReport'?: GlobalReferenceType;
              'common:other'?: CommonOther;
            }[];
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
              'common:other'?: CommonOther;
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
        'common:referenceToPersonOrEntityEnteringTheData': GlobalReferenceType;
        'common:other'?: CommonOther;
      };
      publicationAndOwnership: {
        'common:dataSetVersion': string;
        'common:referenceToPrecedingDataSetVersion'?: GlobalReferenceType;
        'common:permanentDataSetURI': string;
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
    'common:other'?: CommonOther;
  };
}
