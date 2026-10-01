// Generated directly from TIDAS JSON Schema: tidas_processes.json
import { z } from 'zod';
import {
  jsonSchemaOneOf,
  jsonSchemaTuple,
  withJsonSchemaConditional,
  withJsonSchemaDependencies,
} from './../core/validation/json-schema';
import {
  AnnualSupplyOrProductionVolumeMultiLangSchema,
  CommonOtherSchema,
  FTMultiLangSchema,
  RequiredFTMultiLangSchema,
  GISSchema,
  GlobalReferenceTypeSchema,
  Int6Schema,
  LevelTypeSchema,
  MatRSchema,
  MatVSchema,
  PercSchema,
  RealSchema,
  StringMultiLangSchema,
  RequiredStringMultiLangSchema,
  StringSchema,
  UUIDSchema,
  VersionSchema,
  YearSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';
import { LocationsCategorySchema } from './tidas_locations_category.schema';
import { ProcessesCategorySchema } from './tidas_processes_category.schema';

export const ProcessReviewSchema = withJsonSchemaConditional(
  z.object({
    '@type': z.intersection(
      z.union([
        z.literal('Dependent internal review'),
        z.literal('Independent internal review'),
        z.literal('Independent external review'),
        z.literal('Accredited third party review'),
        z.literal('Independent review panel'),
        z.literal('Not reviewed'),
      ]),
      z.string(),
    ),
    'common:scope': z
      .union([
        z.object({
          '@name': z.intersection(
            z.union([
              z.literal('Raw data'),
              z.literal('Unit process(es), single operation'),
              z.literal('Unit process(es), black box'),
              z.literal('LCI results or Partly terminated system'),
              z.literal('LCIA results'),
              z.literal('Documentation'),
              z.literal('Life cycle inventory methods'),
              z.literal('LCIA results calculation'),
              z.literal('Goal and scope definition'),
            ]),
            z.string(),
          ),
          'common:method': z.union([
            z.object({
              '@name': z.intersection(
                z.union([
                  z.literal('Validation of data sources'),
                  z.literal('Sample tests on calculations'),
                  z.literal('Energy balance'),
                  z.literal('Element balance'),
                  z.literal('Cross-check with other source'),
                  z.literal('Cross-check with other data set'),
                  z.literal('Expert judgement'),
                  z.literal('Mass balance'),
                  z.literal('Compliance with legal limits'),
                  z.literal('Compliance with ISO 14040 to 14044'),
                  z.literal('Documentation'),
                  z.literal(
                    'Evidence collection by means of plant visits and/or interviews',
                  ),
                ]),
                z.string(),
              ),
            }),
            z.array(
              z.object({
                '@name': z.intersection(
                  z.union([
                    z.literal('Validation of data sources'),
                    z.literal('Sample tests on calculations'),
                    z.literal('Energy balance'),
                    z.literal('Element balance'),
                    z.literal('Cross-check with other source'),
                    z.literal('Cross-check with other data set'),
                    z.literal('Expert judgement'),
                    z.literal('Mass balance'),
                    z.literal('Compliance with legal limits'),
                    z.literal('Compliance with ISO 14040 to 14044'),
                    z.literal('Documentation'),
                    z.literal(
                      'Evidence collection by means of plant visits and/or interviews',
                    ),
                  ]),
                  z.string(),
                ),
              }),
            ),
          ]),
        }),
        z.array(
          z.object({
            '@name': z.intersection(
              z.union([
                z.literal('Raw data'),
                z.literal('Unit process(es), single operation'),
                z.literal('Unit process(es), black box'),
                z.literal('LCI results or Partly terminated system'),
                z.literal('LCIA results'),
                z.literal('Documentation'),
                z.literal('Life cycle inventory methods'),
                z.literal('LCIA results calculation'),
                z.literal('Goal and scope definition'),
              ]),
              z.string(),
            ),
            'common:method': z.union([
              z.object({
                '@name': z.intersection(
                  z.union([
                    z.literal('Validation of data sources'),
                    z.literal('Sample tests on calculations'),
                    z.literal('Energy balance'),
                    z.literal('Element balance'),
                    z.literal('Cross-check with other source'),
                    z.literal('Cross-check with other data set'),
                    z.literal('Expert judgement'),
                    z.literal('Mass balance'),
                    z.literal('Compliance with legal limits'),
                    z.literal('Compliance with ISO 14040 to 14044'),
                    z.literal('Documentation'),
                    z.literal(
                      'Evidence collection by means of plant visits and/or interviews',
                    ),
                  ]),
                  z.string(),
                ),
              }),
              z.array(
                z.object({
                  '@name': z.intersection(
                    z.union([
                      z.literal('Validation of data sources'),
                      z.literal('Sample tests on calculations'),
                      z.literal('Energy balance'),
                      z.literal('Element balance'),
                      z.literal('Cross-check with other source'),
                      z.literal('Cross-check with other data set'),
                      z.literal('Expert judgement'),
                      z.literal('Mass balance'),
                      z.literal('Compliance with legal limits'),
                      z.literal('Compliance with ISO 14040 to 14044'),
                      z.literal('Documentation'),
                      z.literal(
                        'Evidence collection by means of plant visits and/or interviews',
                      ),
                    ]),
                    z.string(),
                  ),
                }),
              ),
            ]),
          }),
        ),
      ])
      .optional(),
    'common:dataQualityIndicators': z
      .object({
        'common:dataQualityIndicator': z.union([
          z.object({
            '@name': z.intersection(
              z.union([
                z.literal('Technological representativeness'),
                z.literal('Time representativeness'),
                z.literal('Geographical representativeness'),
                z.literal('Completeness'),
                z.literal('Precision'),
                z.literal('Methodological appropriateness and consistency'),
                z.literal('Overall quality'),
              ]),
              z.string(),
            ),
            '@value': z.intersection(
              z.union([
                z.literal('Very good'),
                z.literal('Good'),
                z.literal('Fair'),
                z.literal('Poor'),
                z.literal('Very poor'),
                z.literal('Not evaluated / unknown'),
                z.literal('Not applicable'),
              ]),
              z.string(),
            ),
          }),
          z.array(
            z.object({
              '@name': z.intersection(
                z.union([
                  z.literal('Technological representativeness'),
                  z.literal('Time representativeness'),
                  z.literal('Geographical representativeness'),
                  z.literal('Completeness'),
                  z.literal('Precision'),
                  z.literal('Methodological appropriateness and consistency'),
                  z.literal('Overall quality'),
                ]),
                z.string(),
              ),
              '@value': z.intersection(
                z.union([
                  z.literal('Very good'),
                  z.literal('Good'),
                  z.literal('Fair'),
                  z.literal('Poor'),
                  z.literal('Very poor'),
                  z.literal('Not evaluated / unknown'),
                  z.literal('Not applicable'),
                ]),
                z.string(),
              ),
            }),
          ),
        ]),
      })
      .optional(),
    'common:reviewDetails': FTMultiLangSchema.optional(),
    'common:referenceToNameOfReviewerAndInstitution':
      GlobalReferenceTypeSchema.optional(),
    'common:otherReviewDetails': FTMultiLangSchema.optional(),
    'common:referenceToCompleteReviewReport':
      GlobalReferenceTypeSchema.optional(),
    'common:other': CommonOtherSchema.optional(),
  }),
  z.object({ '@type': z.literal('Not reviewed').optional() }),
  z.unknown(),
  z.object({
    'common:scope': z.unknown(),
    'common:reviewDetails': z.unknown(),
    'common:referenceToNameOfReviewerAndInstitution': z.unknown(),
  }),
);

export const ProcessesSchema = z.object({
  processDataSet: z.object({
    '@xmlns:common': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Common'),
      z.string(),
    ),
    '@xmlns': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Process'),
      z.string(),
    ),
    '@xmlns:xsi': z.intersection(
      z.literal('http://www.w3.org/2001/XMLSchema-instance'),
      z.string(),
    ),
    '@version': z.intersection(z.literal('1.1'), z.string()),
    '@locations': z.intersection(z.literal('../ILCDLocations.xml'), z.string()),
    '@xsi:schemaLocation': z.string(),
    processInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        name: z.object({
          baseName: RequiredStringMultiLangSchema,
          treatmentStandardsRoutes: RequiredStringMultiLangSchema,
          mixAndLocationTypes: RequiredStringMultiLangSchema,
          functionalUnitFlowProperties: StringMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        identifierOfSubDataSet: StringSchema.optional(),
        'common:synonyms': FTMultiLangSchema.optional(),
        complementingProcesses: z
          .object({
            referenceToComplementingProcess:
              GlobalReferenceTypeSchema.optional(),
          })
          .optional(),
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
        'common:generalComment': RequiredFTMultiLangSchema,
        referenceToExternalDocumentation: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      quantitativeReference: withJsonSchemaConditional(
        withJsonSchemaConditional(
          z.object({
            '@type': z.intersection(
              z.union([
                z.literal('Reference flow(s)'),
                z.literal('Functional unit'),
                z.literal('Other parameter'),
                z.literal('Production period'),
              ]),
              z.string(),
            ),
            referenceToReferenceFlow: z
              .union([Int6Schema, z.array(Int6Schema).min(1)])
              .optional(),
            functionalUnitOrOther: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
          z.object({ '@type': z.literal('Reference flow(s)') }),
          z.object({ referenceToReferenceFlow: z.unknown() }),
          undefined,
        ),
        z.object({
          '@type': z.union([
            z.literal('Functional unit'),
            z.literal('Other parameter'),
            z.literal('Production period'),
          ]),
        }),
        z.object({ functionalUnitOrOther: z.unknown() }),
        undefined,
      ),
      time: z.object({
        'common:referenceYear': YearSchema,
        'common:dataSetValidUntil': YearSchema.optional(),
        'common:timeRepresentativenessDescription':
          FTMultiLangSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      geography: z.object({
        locationOfOperationSupplyOrProduction: z.object({
          '@location': LocationsCategorySchema,
          '@latitudeAndLongitude': GISSchema.optional(),
          descriptionOfRestrictions: FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        subLocationOfOperationSupplyOrProduction: z
          .union([
            z.object({
              '@subLocation': LocationsCategorySchema.optional(),
              '@latitudeAndLongitude': GISSchema.optional(),
              descriptionOfRestrictions: FTMultiLangSchema.optional(),
              'common:other': CommonOtherSchema.optional(),
            }),
            z
              .array(
                z.object({
                  '@subLocation': LocationsCategorySchema.optional(),
                  '@latitudeAndLongitude': GISSchema.optional(),
                  descriptionOfRestrictions: FTMultiLangSchema.optional(),
                  'common:other': CommonOtherSchema.optional(),
                }),
              )
              .min(1),
          ])
          .optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      technology: z
        .object({
          technologyDescriptionAndIncludedProcesses: RequiredFTMultiLangSchema,
          referenceToIncludedProcesses: GlobalReferenceTypeSchema.optional(),
          technologicalApplicability: FTMultiLangSchema.optional(),
          referenceToTechnologyPictogramme:
            GlobalReferenceTypeSchema.optional(),
          referenceToTechnologyFlowDiagrammOrPicture:
            GlobalReferenceTypeSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      mathematicalRelations: z
        .object({
          modelDescription: FTMultiLangSchema.optional(),
          variableParameter: z
            .union([
              z.object({
                '@name': MatVSchema,
                formula: MatRSchema.optional(),
                meanValue: RealSchema.optional(),
                minimumValue: RealSchema.optional(),
                maximumValue: RealSchema.optional(),
                uncertaintyDistributionType: z
                  .intersection(
                    z.union([
                      z.literal('undefined'),
                      z.literal('log-normal'),
                      z.literal('normal'),
                      z.literal('triangular'),
                      z.literal('uniform'),
                    ]),
                    z.string(),
                  )
                  .optional(),
                relativeStandardDeviation95In: PercSchema.optional(),
                comment: StringMultiLangSchema.optional(),
                'common:other': CommonOtherSchema.optional(),
              }),
              z
                .array(
                  z.object({
                    '@name': MatVSchema,
                    formula: MatRSchema.optional(),
                    meanValue: RealSchema.optional(),
                    minimumValue: RealSchema.optional(),
                    maximumValue: RealSchema.optional(),
                    uncertaintyDistributionType: z
                      .intersection(
                        z.union([
                          z.literal('undefined'),
                          z.literal('log-normal'),
                          z.literal('normal'),
                          z.literal('triangular'),
                          z.literal('uniform'),
                        ]),
                        z.string(),
                      )
                      .optional(),
                    relativeStandardDeviation95In: PercSchema.optional(),
                    comment: StringMultiLangSchema.optional(),
                    'common:other': CommonOtherSchema.optional(),
                  }),
                )
                .min(1),
            ])
            .optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      'common:other': CommonOtherSchema.optional(),
    }),
    modellingAndValidation: z.object({
      LCIMethodAndAllocation: z.object({
        typeOfDataSet: z
          .intersection(
            z.union([
              z.literal('Unit process, single operation'),
              z.literal('Unit process, black box'),
              z.literal('LCI result'),
              z.literal('Partly terminated system'),
              z.literal('Avoided product system'),
            ]),
            z.string(),
          )
          .optional(),
        LCIMethodPrinciple: z
          .intersection(
            z.union([
              z.literal('Attributional'),
              z.literal('Consequential'),
              z.literal('Consequential with attributional components'),
              z.literal('Not applicable'),
              z.literal('Other'),
            ]),
            z.string(),
          )
          .optional(),
        deviationsFromLCIMethodPrinciple: FTMultiLangSchema.optional(),
        LCIMethodApproaches: z
          .union([
            z.intersection(
              z.union([
                z.literal('Allocation - market value'),
                z.literal('Allocation - gross calorific value'),
                z.literal('Allocation - net calorific value'),
                z.literal('Allocation - exergetic content'),
                z.literal('Allocation - element content'),
                z.literal('Allocation - mass'),
                z.literal('Allocation - volume'),
                z.literal('Allocation - ability to bear'),
                z.literal('Allocation - marginal causality'),
                z.literal('Allocation - physical causality'),
                z.literal('Allocation - 100% to main function'),
                z.literal('Allocation - other explicit assignment'),
                z.literal('Allocation - equal distribution'),
                z.literal('Substitution - BAT'),
                z.literal('Substitution - average, market price correction'),
                z.literal(
                  'Substitution - average, technical properties correction',
                ),
                z.literal('Allocation - recycled content'),
                z.literal('Substitution - recycling potential'),
                z.literal('Substitution - average, no correction'),
                z.literal('Substitution - specific'),
                z.literal('Consequential effects - other'),
                z.literal('Not applicable'),
                z.literal('Other'),
              ]),
              z.string(),
            ),
            z
              .array(
                z.intersection(
                  z.union([
                    z.literal('Allocation - market value'),
                    z.literal('Allocation - gross calorific value'),
                    z.literal('Allocation - net calorific value'),
                    z.literal('Allocation - exergetic content'),
                    z.literal('Allocation - element content'),
                    z.literal('Allocation - mass'),
                    z.literal('Allocation - volume'),
                    z.literal('Allocation - ability to bear'),
                    z.literal('Allocation - marginal causality'),
                    z.literal('Allocation - physical causality'),
                    z.literal('Allocation - 100% to main function'),
                    z.literal('Allocation - other explicit assignment'),
                    z.literal('Allocation - equal distribution'),
                    z.literal('Substitution - BAT'),
                    z.literal(
                      'Substitution - average, market price correction',
                    ),
                    z.literal(
                      'Substitution - average, technical properties correction',
                    ),
                    z.literal('Allocation - recycled content'),
                    z.literal('Substitution - recycling potential'),
                    z.literal('Substitution - average, no correction'),
                    z.literal('Substitution - specific'),
                    z.literal('Consequential effects - other'),
                    z.literal('Not applicable'),
                    z.literal('Other'),
                  ]),
                  z.string(),
                ),
              )
              .min(1),
          ])
          .optional(),
        deviationsFromLCIMethodApproaches: FTMultiLangSchema.optional(),
        modellingConstants: FTMultiLangSchema.optional(),
        deviationsFromModellingConstants: FTMultiLangSchema.optional(),
        referenceToLCAMethodDetails: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      dataSourcesTreatmentAndRepresentativeness: z
        .object({
          dataCutOffAndCompletenessPrinciples: RequiredFTMultiLangSchema,
          deviationsFromCutOffAndCompletenessPrinciples:
            FTMultiLangSchema.optional(),
          dataSelectionAndCombinationPrinciples: FTMultiLangSchema.optional(),
          deviationsFromSelectionAndCombinationPrinciples:
            FTMultiLangSchema.optional(),
          dataTreatmentAndExtrapolationsPrinciples:
            FTMultiLangSchema.optional(),
          deviationsFromTreatmentAndExtrapolationPrinciples:
            FTMultiLangSchema.optional(),
          referenceToDataHandlingPrinciples:
            GlobalReferenceTypeSchema.optional(),
          referenceToDataSource: GlobalReferenceTypeSchema,
          percentageSupplyOrProductionCovered: PercSchema.optional(),
          annualSupplyOrProductionVolume:
            AnnualSupplyOrProductionVolumeMultiLangSchema,
          samplingProcedure: FTMultiLangSchema.optional(),
          dataCollectionPeriod: StringMultiLangSchema.optional(),
          uncertaintyAdjustments: FTMultiLangSchema.optional(),
          useAdviceForDataSet: FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      completeness: z
        .object({
          completenessProductModel: z
            .intersection(
              z.union([
                z.literal('All relevant flows quantified'),
                z.literal('Relevant flows missing'),
                z.literal('Topic not relevant'),
                z.literal('No statement'),
              ]),
              z.string(),
            )
            .optional(),
          referenceToSupportedImpactAssessmentMethods:
            GlobalReferenceTypeSchema.optional(),
          completenessElementaryFlows: z
            .union([
              z.object({
                '@type': z
                  .intersection(
                    z.union([
                      z.literal('Climate change'),
                      z.literal('Ozone depletion'),
                      z.literal('Summer smog'),
                      z.literal('Eutrophication'),
                      z.literal('Acidification'),
                      z.literal('Human toxicity'),
                      z.literal('Freshwater ecotoxicity'),
                      z.literal('Seawater eco-toxicity'),
                      z.literal('Terrestric eco-toxicity'),
                      z.literal('Radioactivity'),
                      z.literal('Land use'),
                      z.literal('Non-renewable material resource depletion'),
                      z.literal('Renewable material resource consumption'),
                      z.literal('Non-renewable primary energy depletion'),
                      z.literal('Renewable primary energy consumption'),
                      z.literal('Particulate matter/respiratory inorganics'),
                      z.literal('Species depletion'),
                      z.literal('Noise'),
                    ]),
                    z.string(),
                  )
                  .optional(),
                '@value': z
                  .intersection(
                    z.union([
                      z.literal('All relevant flows quantified'),
                      z.literal('Relevant flows missing'),
                      z.literal('Topic not relevant'),
                      z.literal('No statement'),
                    ]),
                    z.string(),
                  )
                  .optional(),
              }),
              z
                .array(
                  z.object({
                    '@type': z
                      .intersection(
                        z.union([
                          z.literal('Climate change'),
                          z.literal('Ozone depletion'),
                          z.literal('Summer smog'),
                          z.literal('Eutrophication'),
                          z.literal('Acidification'),
                          z.literal('Human toxicity'),
                          z.literal('Freshwater ecotoxicity'),
                          z.literal('Seawater eco-toxicity'),
                          z.literal('Terrestric eco-toxicity'),
                          z.literal('Radioactivity'),
                          z.literal('Land use'),
                          z.literal(
                            'Non-renewable material resource depletion',
                          ),
                          z.literal('Renewable material resource consumption'),
                          z.literal('Non-renewable primary energy depletion'),
                          z.literal('Renewable primary energy consumption'),
                          z.literal(
                            'Particulate matter/respiratory inorganics',
                          ),
                          z.literal('Species depletion'),
                          z.literal('Noise'),
                        ]),
                        z.string(),
                      )
                      .optional(),
                    '@value': z
                      .intersection(
                        z.union([
                          z.literal('All relevant flows quantified'),
                          z.literal('Relevant flows missing'),
                          z.literal('Topic not relevant'),
                          z.literal('No statement'),
                        ]),
                        z.string(),
                      )
                      .optional(),
                  }),
                )
                .min(1),
            ])
            .optional(),
          completenessOtherProblemField: FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      validation: z.object({
        review: z.union([
          ProcessReviewSchema,
          z.array(ProcessReviewSchema).min(1),
        ]),
        'common:other': CommonOtherSchema.optional(),
      }),
      complianceDeclarations: z.object({
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
            )
            .min(1),
        ]),
        'common:other': CommonOtherSchema.optional(),
      }),
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
        'common:referenceToConvertedOriginalDataSetFrom':
          GlobalReferenceTypeSchema.optional(),
        'common:referenceToPersonOrEntityEnteringTheData':
          GlobalReferenceTypeSchema,
        'common:referenceToDataSetUseApproval':
          GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      publicationAndOwnership: z.object({
        'common:dateOfLastRevision': z.iso
          .datetime({ offset: true })
          .optional(),
        'common:dataSetVersion': VersionSchema,
        'common:referenceToPrecedingDataSetVersion':
          GlobalReferenceTypeSchema.optional(),
        'common:permanentDataSetURI': z.url(),
        'common:workflowAndPublicationStatus': z
          .intersection(
            z.union([
              z.literal('Working draft'),
              z.literal('Final draft for internal review'),
              z.literal('Final draft for external review'),
              z.literal('Data set finalised; unpublished'),
              z.literal('Under revision'),
              z.literal('Withdrawn'),
              z.literal('Data set finalised; subsystems published'),
              z.literal('Data set finalised; entirely published'),
            ]),
            z.string(),
          )
          .optional(),
        'common:referenceToUnchangedRepublication':
          GlobalReferenceTypeSchema.optional(),
        'common:referenceToRegistrationAuthority':
          GlobalReferenceTypeSchema.optional(),
        'common:registrationNumber': StringSchema.optional(),
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
    exchanges: z.object({
      exchange: z.array(
        z.object({
          '@dataSetInternalID': Int6Schema,
          referenceToFlowDataSet: GlobalReferenceTypeSchema,
          location: z.union([LocationsCategorySchema, StringSchema]).optional(),
          functionType: z
            .intersection(
              z.union([
                z.literal('General reminder flow'),
                z.literal('Allocation reminder flow'),
                z.literal('System expansion reminder flow'),
              ]),
              z.string(),
            )
            .optional(),
          exchangeDirection: z.intersection(
            z.union([z.literal('Input'), z.literal('Output')]),
            z.string(),
          ),
          referenceToVariable: StringSchema.optional(),
          meanAmount: RealSchema,
          resultingAmount: RealSchema,
          minimumAmount: RealSchema.optional(),
          maximumAmount: RealSchema.optional(),
          uncertaintyDistributionType: z
            .intersection(
              z.union([
                z.literal('undefined'),
                z.literal('log-normal'),
                z.literal('normal'),
                z.literal('triangular'),
                z.literal('uniform'),
              ]),
              z.string(),
            )
            .optional(),
          relativeStandardDeviation95In: PercSchema.optional(),
          allocations: z
            .object({
              allocation: z.union([
                z.object({
                  '@internalReferenceToCoProduct': Int6Schema.optional(),
                  '@allocatedFraction': PercSchema.optional(),
                }),
                z.array(
                  z.object({
                    '@internalReferenceToCoProduct': Int6Schema.optional(),
                    '@allocatedFraction': PercSchema.optional(),
                  }),
                ),
              ]),
            })
            .optional(),
          dataSourceType: z
            .intersection(
              z.union([
                z.literal('Primary'),
                z.literal('> 90% primary'),
                z.literal('Mixed primary / secondary'),
                z.literal('Secondary'),
              ]),
              z.string(),
            )
            .optional(),
          dataDerivationTypeStatus: z.intersection(
            z.union([
              z.literal('Measured'),
              z.literal('Calculated'),
              z.literal('Estimated'),
              z.literal('Unknown derivation'),
              z.literal('Missing important'),
              z.literal('Missing unimportant'),
            ]),
            z.string(),
          ),
          referencesToDataSource: z
            .object({
              referenceToDataSource: GlobalReferenceTypeSchema.optional(),
              'common:other': CommonOtherSchema.optional(),
            })
            .optional(),
          generalComment: StringMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
      ),
      'common:other': CommonOtherSchema.optional(),
    }),
    LCIAResults: z
      .object({
        LCIAResult: jsonSchemaOneOf([
          z.object({
            referenceToLCIAMethodDataSet: GlobalReferenceTypeSchema.optional(),
            meanAmount: RealSchema,
            uncertaintyDistributionType: z
              .intersection(
                z.union([
                  z.literal('undefined'),
                  z.literal('log-normal'),
                  z.literal('normal'),
                  z.literal('triangular'),
                  z.literal('uniform'),
                ]),
                z.string(),
              )
              .optional(),
            relativeStandardDeviation95In: PercSchema.optional(),
            generalComment: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
          z
            .array(
              z.object({
                referenceToLCIAMethodDataSet:
                  GlobalReferenceTypeSchema.optional(),
                meanAmount: RealSchema,
                uncertaintyDistributionType: z
                  .intersection(
                    z.union([
                      z.literal('undefined'),
                      z.literal('log-normal'),
                      z.literal('normal'),
                      z.literal('triangular'),
                      z.literal('uniform'),
                    ]),
                    z.string(),
                  )
                  .optional(),
                relativeStandardDeviation95In: PercSchema.optional(),
                generalComment: StringMultiLangSchema.optional(),
                'common:other': CommonOtherSchema.optional(),
              }),
            )
            .min(1),
        ]).optional(),
        'common:other': CommonOtherSchema.optional(),
      })
      .optional(),
    'common:other': CommonOtherSchema.optional(),
  }),
});
