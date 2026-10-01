// Generated directly from TIDAS JSON Schema: tidas_lifecyclemodels.json
import { z } from 'zod';
import {
  jsonSchemaNotRequired,
  jsonSchemaOneOf,
  jsonSchemaTuple,
  withJsonSchemaDependencies,
} from './../core/validation/json-schema';
import {
  CommonOtherSchema,
  FTMultiLangSchema,
  RequiredFTMultiLangSchema,
  GlobalReferenceTypeSchema,
  LevelTypeSchema,
  MatVSchema,
  RealSchema,
  StringMultiLangSchema,
  RequiredStringMultiLangSchema,
  UUIDSchema,
  VersionSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';
import { ProcessesCategorySchema } from './tidas_processes_category.schema';

export const LifecyclemodelsSchema = z.object({
  lifeCycleModelDataSet: z.object({
    '@xmlns': z.intersection(
      z.literal('http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017'),
      z.string(),
    ),
    '@xmlns:acme': z.intersection(
      z.literal('http://acme.com/custom'),
      z.string(),
    ),
    '@xmlns:common': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Common'),
      z.string(),
    ),
    '@xmlns:xsi': z.intersection(
      z.literal('http://www.w3.org/2001/XMLSchema-instance'),
      z.string(),
    ),
    '@locations': z.intersection(z.literal('../ILCDLocations.xml'), z.string()),
    '@version': z.intersection(z.literal('1.1'), z.string()),
    '@xsi:schemaLocation': z.intersection(
      z.literal(
        'http://eplca.jrc.ec.europa.eu/ILCD/LifeCycleModel/2017 ../../schemas/ILCD_LifeCycleModelDataSet.xsd',
      ),
      z.string(),
    ),
    lifeCycleModelInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        name: z.object({
          baseName: RequiredStringMultiLangSchema,
          treatmentStandardsRoutes: RequiredStringMultiLangSchema,
          mixAndLocationTypes: RequiredStringMultiLangSchema,
          functionalUnitFlowProperties: StringMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        classificationInformation: z.object({
          'common:classification': z.union([
            z.object({
              'common:class': jsonSchemaTuple(
                [
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('0'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: ProcessesCategorySchema }],
                  ),
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('1'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: ProcessesCategorySchema }],
                  ),
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('2'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: ProcessesCategorySchema }],
                  ),
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('3'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: ProcessesCategorySchema }],
                  ),
                ],
                { additionalItems: false, maxItems: 4, uniqueItems: true },
              ),
              'common:other': CommonOtherSchema.optional(),
              '@name': z.string().optional(),
              '@classes': z.string().optional(),
            }),
            z
              .array(
                z.object({
                  '@name': z.string(),
                  '@classes': z.string().optional(),
                  'common:class': z
                    .array(
                      z.object({
                        '@level': LevelTypeSchema,
                        '@classId': z.string(),
                        '#text': z.string(),
                      }),
                    )
                    .min(1),
                  'common:other': CommonOtherSchema.optional(),
                }),
              )
              .min(1),
          ]),
        }),
        referenceToResultingProcess: GlobalReferenceTypeSchema.optional(),
        'common:generalComment': FTMultiLangSchema.optional(),
        referenceToExternalDocumentation: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      quantitativeReference: z.object({
        referenceToReferenceProcess: z.number().int(),
        'common:other': CommonOtherSchema.optional(),
      }),
      technology: z.object({
        groupDeclarations: z
          .object({
            group: z
              .union([
                z.object({
                  '@id': z.string().regex(/^-?\d+$/),
                  groupName: StringMultiLangSchema.optional(),
                }),
                z.array(
                  z.object({
                    '@id': z.string().regex(/^-?\d+$/),
                    groupName: StringMultiLangSchema.optional(),
                  }),
                ),
              ])
              .optional(),
          })
          .optional(),
        processes: z.object({
          processInstance: z
            .union([
              z.array(
                z.intersection(
                  z.object({
                    '@dataSetInternalID': z.string().regex(/^-?\d+$/),
                    '@multiplicationFactor': z
                      .string()
                      .regex(/^-?\d+(\.\d+)?([eE][-+]?\d+)?$/),
                    referenceToProcess: GlobalReferenceTypeSchema,
                    groups: z
                      .object({
                        memberOf: z
                          .union([
                            z.object({
                              '@groupId': z.string().regex(/^-?\d+$/),
                            }),
                            z.array(
                              z.object({
                                '@groupId': z.string().regex(/^-?\d+$/),
                              }),
                            ),
                          ])
                          .optional(),
                      })
                      .optional(),
                    parameters: z
                      .object({
                        parameter: z
                          .union([
                            z.intersection(
                              z.object({
                                '@name': MatVSchema,
                                '#text': RealSchema.optional(),
                                parameter: RealSchema.optional(),
                              }),
                              jsonSchemaOneOf([
                                z.object({ '#text': z.unknown() }),
                                z.object({ parameter: z.unknown() }),
                              ]),
                            ),
                            z.array(
                              z.intersection(
                                z.object({
                                  '@name': MatVSchema,
                                  '#text': RealSchema.optional(),
                                  parameter: RealSchema.optional(),
                                }),
                                jsonSchemaOneOf([
                                  z.object({ '#text': z.unknown() }),
                                  z.object({ parameter: z.unknown() }),
                                ]),
                              ),
                            ),
                          ])
                          .optional(),
                      })
                      .optional(),
                    connections: z
                      .object({
                        outputExchange: z.union([
                          z.object({
                            '@dominant': z
                              .intersection(
                                z.union([
                                  z.literal('true'),
                                  z.literal('false'),
                                ]),
                                z.string(),
                              )
                              .optional(),
                            '@flowUUID': UUIDSchema,
                            downstreamProcess: z.union([
                              z.object({
                                '@id': z.string().regex(/^-?\d+$/),
                                '@flowUUID': UUIDSchema,
                                '@location': z.string().optional(),
                                '@dominant': z
                                  .intersection(
                                    z.union([
                                      z.literal('true'),
                                      z.literal('false'),
                                    ]),
                                    z.string(),
                                  )
                                  .optional(),
                                '@version': VersionSchema,
                              }),
                              z.array(
                                z.object({
                                  '@id': z.string().regex(/^-?\d+$/),
                                  '@flowUUID': UUIDSchema,
                                  '@location': z.string().optional(),
                                  '@dominant': z
                                    .intersection(
                                      z.union([
                                        z.literal('true'),
                                        z.literal('false'),
                                      ]),
                                      z.string(),
                                    )
                                    .optional(),
                                  '@version': VersionSchema,
                                }),
                              ),
                            ]),
                            '@version': VersionSchema,
                          }),
                          z.array(
                            z.object({
                              '@dominant': z
                                .intersection(
                                  z.union([
                                    z.literal('true'),
                                    z.literal('false'),
                                  ]),
                                  z.string(),
                                )
                                .optional(),
                              '@flowUUID': UUIDSchema,
                              downstreamProcess: z.union([
                                z.object({
                                  '@id': z.string().regex(/^-?\d+$/),
                                  '@flowUUID': UUIDSchema,
                                  '@location': z.string().optional(),
                                  '@dominant': z
                                    .intersection(
                                      z.union([
                                        z.literal('true'),
                                        z.literal('false'),
                                      ]),
                                      z.string(),
                                    )
                                    .optional(),
                                  '@version': VersionSchema,
                                }),
                                z.array(
                                  z.object({
                                    '@id': z.string().regex(/^-?\d+$/),
                                    '@flowUUID': UUIDSchema,
                                    '@location': z.string().optional(),
                                    '@dominant': z
                                      .intersection(
                                        z.union([
                                          z.literal('true'),
                                          z.literal('false'),
                                        ]),
                                        z.string(),
                                      )
                                      .optional(),
                                    '@version': VersionSchema,
                                  }),
                                ),
                              ]),
                              '@version': VersionSchema,
                            }),
                          ),
                        ]),
                      })
                      .optional(),
                    'common:other': CommonOtherSchema.optional(),
                    scalingFactor: RealSchema.optional(),
                    scalingFactors: RealSchema.optional(),
                  }),
                  jsonSchemaNotRequired(['scalingFactor', 'scalingFactors']),
                ),
              ),
              z.intersection(
                z.object({
                  '@dataSetInternalID': z.string().regex(/^-?\d+$/),
                  '@multiplicationFactor': z
                    .string()
                    .regex(/^-?\d+(\.\d+)?([eE][-+]?\d+)?$/),
                  referenceToProcess: GlobalReferenceTypeSchema,
                  groups: z
                    .object({
                      memberOf: z
                        .union([
                          z.object({ '@groupId': z.string().regex(/^-?\d+$/) }),
                          z.array(
                            z.object({
                              '@groupId': z.string().regex(/^-?\d+$/),
                            }),
                          ),
                        ])
                        .optional(),
                    })
                    .optional(),
                  parameters: z
                    .object({
                      parameter: z
                        .union([
                          z.intersection(
                            z.object({
                              '@name': MatVSchema,
                              parameter: RealSchema.optional(),
                              '#text': RealSchema.optional(),
                            }),
                            jsonSchemaOneOf([
                              z.object({ '#text': z.unknown() }),
                              z.object({ parameter: z.unknown() }),
                            ]),
                          ),
                          z.array(
                            z.intersection(
                              z.object({
                                '@name': MatVSchema,
                                parameter: RealSchema.optional(),
                                '#text': RealSchema.optional(),
                              }),
                              jsonSchemaOneOf([
                                z.object({ '#text': z.unknown() }),
                                z.object({ parameter: z.unknown() }),
                              ]),
                            ),
                          ),
                        ])
                        .optional(),
                    })
                    .optional(),
                  connections: z
                    .object({
                      outputExchange: z.union([
                        z.object({
                          '@dominant': z
                            .intersection(
                              z.union([z.literal('true'), z.literal('false')]),
                              z.string(),
                            )
                            .optional(),
                          '@flowUUID': UUIDSchema,
                          downstreamProcess: z.union([
                            z.object({
                              '@id': z.string().regex(/^-?\d+$/),
                              '@flowUUID': UUIDSchema,
                              '@location': z.string().optional(),
                              '@dominant': z
                                .intersection(
                                  z.union([
                                    z.literal('true'),
                                    z.literal('false'),
                                  ]),
                                  z.string(),
                                )
                                .optional(),
                              '@version': VersionSchema,
                            }),
                            z.array(
                              z.object({
                                '@id': z.string().regex(/^-?\d+$/),
                                '@flowUUID': UUIDSchema,
                                '@location': z.string().optional(),
                                '@dominant': z
                                  .intersection(
                                    z.union([
                                      z.literal('true'),
                                      z.literal('false'),
                                    ]),
                                    z.string(),
                                  )
                                  .optional(),
                                '@version': VersionSchema,
                              }),
                            ),
                          ]),
                          '@version': VersionSchema,
                        }),
                        z.array(
                          z.object({
                            '@dominant': z
                              .intersection(
                                z.union([
                                  z.literal('true'),
                                  z.literal('false'),
                                ]),
                                z.string(),
                              )
                              .optional(),
                            '@flowUUID': UUIDSchema,
                            downstreamProcess: z.union([
                              z.object({
                                '@id': z.string().regex(/^-?\d+$/),
                                '@flowUUID': UUIDSchema,
                                '@location': z.string().optional(),
                                '@dominant': z
                                  .intersection(
                                    z.union([
                                      z.literal('true'),
                                      z.literal('false'),
                                    ]),
                                    z.string(),
                                  )
                                  .optional(),
                                '@version': VersionSchema,
                              }),
                              z.array(
                                z.object({
                                  '@id': z.string().regex(/^-?\d+$/),
                                  '@flowUUID': UUIDSchema,
                                  '@location': z.string().optional(),
                                  '@dominant': z
                                    .intersection(
                                      z.union([
                                        z.literal('true'),
                                        z.literal('false'),
                                      ]),
                                      z.string(),
                                    )
                                    .optional(),
                                  '@version': VersionSchema,
                                }),
                              ),
                            ]),
                            '@version': VersionSchema,
                          }),
                        ),
                      ]),
                    })
                    .optional(),
                  'common:other': CommonOtherSchema.optional(),
                  scalingFactor: RealSchema.optional(),
                  scalingFactors: RealSchema.optional(),
                }),
                jsonSchemaNotRequired(['scalingFactor', 'scalingFactors']),
              ),
            ])
            .optional(),
        }),
        referenceToDiagram: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
    }),
    modellingAndValidation: z.object({
      dataSourcesTreatmentEtc: z
        .object({
          useAdviceForDataSet: FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      validation: z.object({
        review: z.union([
          z.object({
            'common:referenceToNameOfReviewerAndInstitution':
              GlobalReferenceTypeSchema,
            'common:otherReviewDetails': FTMultiLangSchema.optional(),
            'common:referenceToCompleteReviewReport':
              GlobalReferenceTypeSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
          z.array(
            z.object({
              'common:referenceToNameOfReviewerAndInstitution':
                GlobalReferenceTypeSchema,
              'common:otherReviewDetails': FTMultiLangSchema.optional(),
              'common:referenceToCompleteReviewReport':
                GlobalReferenceTypeSchema.optional(),
              'common:other': CommonOtherSchema.optional(),
            }),
          ),
        ]),
        'common:other': CommonOtherSchema.optional(),
      }),
      complianceDeclarations: z.union([
        z.object({
          compliance: z.union([
            z.object({
              'common:referenceToComplianceSystem': GlobalReferenceTypeSchema,
              'common:approvalOfOverallCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:nomenclatureCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:methodologicalCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:reviewCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:documentationCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:qualityCompliance': z.intersection(
                z.union([
                  z.literal('Fully compliant'),
                  z.literal('Not compliant'),
                  z.literal('Not defined'),
                ]),
                z.string(),
              ),
              'common:other': CommonOtherSchema.optional(),
            }),
            z
              .array(
                z.object({
                  'common:referenceToComplianceSystem':
                    GlobalReferenceTypeSchema,
                  'common:approvalOfOverallCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:nomenclatureCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:methodologicalCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:reviewCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:documentationCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:qualityCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:other': CommonOtherSchema.optional(),
                }),
              )
              .min(1),
          ]),
          'common:other': CommonOtherSchema.optional(),
        }),
        z
          .array(
            z.object({
              compliance: z.union([
                z.object({
                  'common:referenceToComplianceSystem':
                    GlobalReferenceTypeSchema,
                  'common:approvalOfOverallCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:nomenclatureCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:methodologicalCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:reviewCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:documentationCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:qualityCompliance': z.intersection(
                    z.union([
                      z.literal('Fully compliant'),
                      z.literal('Not compliant'),
                      z.literal('Not defined'),
                    ]),
                    z.string(),
                  ),
                  'common:other': CommonOtherSchema.optional(),
                }),
                z
                  .array(
                    z.object({
                      'common:referenceToComplianceSystem':
                        GlobalReferenceTypeSchema,
                      'common:approvalOfOverallCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:nomenclatureCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:methodologicalCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:reviewCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:documentationCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:qualityCompliance': z.intersection(
                        z.union([
                          z.literal('Fully compliant'),
                          z.literal('Not compliant'),
                          z.literal('Not defined'),
                        ]),
                        z.string(),
                      ),
                      'common:other': CommonOtherSchema.optional(),
                    }),
                  )
                  .min(1),
              ]),
              'common:other': CommonOtherSchema.optional(),
            }),
          )
          .min(1),
      ]),
      'common:other': CommonOtherSchema.optional(),
    }),
    administrativeInformation: z.object({
      'common:commissionerAndGoal': z.object({
        'common:referenceToCommissioner': GlobalReferenceTypeSchema,
        'common:project': StringMultiLangSchema.optional(),
        'common:intendedApplications': RequiredFTMultiLangSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      dataGenerator: z
        .object({
          'common:referenceToPersonOrEntityGeneratingTheDataSet':
            GlobalReferenceTypeSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      dataEntryBy: z.object({
        'common:timeStamp': dateTimeSchema,
        'common:referenceToDataSetFormat': GlobalReferenceTypeSchema,
        'common:referenceToPersonOrEntityEnteringTheData':
          GlobalReferenceTypeSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      publicationAndOwnership: z.object({
        'common:dataSetVersion': VersionSchema,
        'common:referenceToPrecedingDataSetVersion':
          GlobalReferenceTypeSchema.optional(),
        'common:permanentDataSetURI': z.url(),
        'common:referenceToOwnershipOfDataSet': GlobalReferenceTypeSchema,
        'common:copyright': z.intersection(
          z.union([z.literal('true'), z.literal('false')]),
          z.string(),
        ),
        'common:referenceToEntitiesWithExclusiveAccess':
          GlobalReferenceTypeSchema.optional(),
        'common:licenseType': z.intersection(
          z.union([
            z.literal('Free of charge for all users and uses'),
            z.literal('Free of charge for some user types or use types'),
            z.literal('Free of charge for members only'),
            z.literal('License fee'),
            z.literal('Other'),
          ]),
          z.string(),
        ),
        'common:accessRestrictions': FTMultiLangSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
    'common:other': CommonOtherSchema.optional(),
  }),
});
