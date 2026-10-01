// Generated directly from TIDAS JSON Schema: tidas_lciamethods.json
import { z } from 'zod';
import {
  jsonSchemaNotRequired,
  jsonSchemaTuple,
  withJsonSchemaConditional,
  withJsonSchemaDependencies,
} from './../core/validation/json-schema';
import {
  CommonOtherSchema,
  FTMultiLangSchema,
  RequiredFTMultiLangSchema,
  GISSchema,
  GlobalReferenceTypeSchema,
  Int6Schema,
  LevelTypeSchema,
  PercSchema,
  RealSchema,
  STMultiLangSchema,
  STSchema,
  StringMultiLangSchema,
  RequiredStringMultiLangSchema,
  StringSchema,
  UUIDSchema,
  VersionSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';
import { LCIAMethodSchema } from './tidas_lciamethods_category.schema';

export const LciamethodsSchema = z.object({
  LCIAMethodDataSet: z.object({
    '@xmlns': z
      .intersection(z.literal('http://lca.jrc.it/ILCD/LCIAMethod'), z.string())
      .optional(),
    '@xmlns:common': z
      .intersection(z.literal('http://lca.jrc.it/ILCD/Common'), z.string())
      .optional(),
    '@xmlns:xsi': z
      .intersection(
        z.literal('http://www.w3.org/2001/XMLSchema-instance'),
        z.string(),
      )
      .optional(),
    '@version': z.intersection(z.literal('1.1'), z.string()).optional(),
    '@xsi:schemaLocation': z
      .intersection(
        z.literal(
          'http://lca.jrc.it/ILCD/LCIAMethod ../../schemas/ILCD_LCIAMethodDataSet.xsd',
        ),
        z.string(),
      )
      .optional(),
    LCIAMethodInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        'common:name': RequiredStringMultiLangSchema,
        methodology: z
          .union([z.string(), z.array(z.string()).min(1)])
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
                    [{ property: '@level', schema: LCIAMethodSchema }],
                  ),
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('1'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: LCIAMethodSchema }],
                  ),
                  withJsonSchemaDependencies(
                    z.object({
                      '@level': z.intersection(z.literal('2'), LevelTypeSchema),
                      '@classId': z.string(),
                      '#text': z.string(),
                    }),
                    [{ property: '@level', schema: LCIAMethodSchema }],
                  ),
                ],
                { additionalItems: false, maxItems: 3, uniqueItems: true },
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
        impactCategory: z
          .union([
            z.intersection(
              z.union([
                z.literal('Climate change'),
                z.literal('Ozone depletion'),
                z.literal('Terrestrial Eutrophication'),
                z.literal('Aquatic Eutrophication'),
                z.literal('Acidification'),
                z.literal('Photochemical ozone creation'),
                z.literal('Land use'),
                z.literal('Abiotic resource depletion'),
                z.literal('Biotic resource depletion'),
                z.literal('Ionizing radiation'),
                z.literal('Cancer human health effects'),
                z.literal('Non-cancer human health effects'),
                z.literal('Respiratory inorganics'),
                z.literal('Aquatic eco-toxicity'),
                z.literal('Terrestrial eco-toxicity'),
                z.literal('other'),
              ]),
              z.string(),
            ),
            z
              .array(
                z.intersection(
                  z.union([
                    z.literal('Climate change'),
                    z.literal('Ozone depletion'),
                    z.literal('Terrestrial Eutrophication'),
                    z.literal('Aquatic Eutrophication'),
                    z.literal('Acidification'),
                    z.literal('Photochemical ozone creation'),
                    z.literal('Land use'),
                    z.literal('Abiotic resource depletion'),
                    z.literal('Biotic resource depletion'),
                    z.literal('Ionizing radiation'),
                    z.literal('Cancer human health effects'),
                    z.literal('Non-cancer human health effects'),
                    z.literal('Respiratory inorganics'),
                    z.literal('Aquatic eco-toxicity'),
                    z.literal('Terrestrial eco-toxicity'),
                    z.literal('other'),
                  ]),
                  z.string(),
                ),
              )
              .min(1),
          ])
          .optional(),
        areaOfProtection: z
          .union([
            z.intersection(
              z.union([
                z.literal('Natural resources'),
                z.literal('Natural environment'),
                z.literal('Human health'),
                z.literal('Man-made environment'),
                z.literal('Other'),
              ]),
              z.string(),
            ),
            z
              .array(
                z.intersection(
                  z.union([
                    z.literal('Natural resources'),
                    z.literal('Natural environment'),
                    z.literal('Human health'),
                    z.literal('Man-made environment'),
                    z.literal('Other'),
                  ]),
                  z.string(),
                ),
              )
              .min(1),
          ])
          .optional(),
        impactIndicator: StringSchema.optional(),
        'common:generalComment': FTMultiLangSchema.optional(),
        referenceToExternalDocumentation: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      quantitativeReference: z.object({
        referenceQuantity: GlobalReferenceTypeSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      time: z.object({
        referenceYear: STMultiLangSchema,
        duration: STMultiLangSchema,
        timeRepresentativenessDescription: RequiredFTMultiLangSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      geography: z
        .intersection(
          z.object({
            interventionLocation: z
              .union([
                z.object({
                  '#text': z.string(),
                  '@latitudeAndLongitude': GISSchema.optional(),
                }),
                z.string(),
              ])
              .optional(),
            impactLocation: z
              .union([
                z.object({
                  '#text': z.string(),
                  '@latitudeAndLongitude': GISSchema.optional(),
                }),
                z.string(),
              ])
              .optional(),
            geographicalRepresentativenessDescription:
              FTMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
            interventionSubLocation: z
              .union([
                z.union([
                  z.object({
                    '#text': z.string(),
                    '@latitudeAndLongitude': GISSchema.optional(),
                  }),
                  z.string(),
                ]),
                z
                  .array(
                    z.union([
                      z.object({
                        '#text': z.string(),
                        '@latitudeAndLongitude': GISSchema.optional(),
                      }),
                      z.string(),
                    ]),
                  )
                  .min(1),
              ])
              .optional(),
            intervensionSubLocation: z
              .union([
                z.object({
                  '#text': z.string().optional(),
                  '@latitudeAndLongitude': GISSchema.optional(),
                }),
                z.string(),
              ])
              .optional(),
          }),
          jsonSchemaNotRequired([
            'interventionSubLocation',
            'intervensionSubLocation',
          ]),
        )
        .optional(),
      impactModel: z.object({
        modelName: STSchema,
        modelDescription: RequiredFTMultiLangSchema,
        referenceToModelSource: GlobalReferenceTypeSchema.optional(),
        referenceToIncludedMethods: GlobalReferenceTypeSchema.optional(),
        consideredMechanisms: STMultiLangSchema.optional(),
        referenceToMethodologyFlowChart: GlobalReferenceTypeSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
    modellingAndValidation: z.object({
      useAdviceForDataSet: STMultiLangSchema.optional(),
      LCIAMethodNormalisationAndWeighting: z.object({
        typeOfDataSet: z.intersection(
          z.union([
            z.literal('Inventory indicator'),
            z.literal('Mid-point indicator'),
            z.literal('Damage indicator'),
            z.literal('Area of Protection damage indicator'),
            z.literal('Combined single-point indicator'),
            z.literal('LCIA methodology documentation'),
          ]),
          z.string(),
        ),
        LCIAMethodPrinciple: z.union([
          z.intersection(
            z.union([
              z.literal('Distance-to-target'),
              z.literal('Critical surface-time'),
              z.literal('Effective volumes'),
              z.literal('AoP-Damage model'),
              z.literal('Carrying capacity'),
              z.literal('Resource dissipation'),
              z.literal('other'),
            ]),
            z.string(),
          ),
          z
            .array(
              z.intersection(
                z.union([
                  z.literal('Distance-to-target'),
                  z.literal('Critical surface-time'),
                  z.literal('Effective volumes'),
                  z.literal('AoP-Damage model'),
                  z.literal('Carrying capacity'),
                  z.literal('Resource dissipation'),
                  z.literal('other'),
                ]),
                z.string(),
              ),
            )
            .min(1),
        ]),
        deviationsFromLCIAMethodPrinciple: FTMultiLangSchema.optional(),
        normalisation: z.boolean().optional(),
        referenceToUsableNormalisationDataSets:
          GlobalReferenceTypeSchema.optional(),
        normalisationDescription: STMultiLangSchema.optional(),
        referenceToIncludedNormalisationDataSets:
          GlobalReferenceTypeSchema.optional(),
        weighting: z.boolean().optional(),
        referenceToUsableWeightingDataSets:
          GlobalReferenceTypeSchema.optional(),
        weightingDescription: STMultiLangSchema.optional(),
        referenceToIncludedWeightingDataSets:
          GlobalReferenceTypeSchema.optional(),
      }),
      dataSources: z.object({
        referenceToDataSource: GlobalReferenceTypeSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      completeness: z
        .object({
          completenessImpactCoverage: PercSchema.optional(),
          inventoryItems: Int6Schema.optional(),
        })
        .optional(),
      validation: z.object({
        review: z.union([
          withJsonSchemaConditional(
            z.intersection(
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
                'common:reviewDetails': FTMultiLangSchema.optional(),
                'common:referenceToNameOfReviewerAndInstitution':
                  GlobalReferenceTypeSchema.optional(),
                'common:otherReviewDetails': FTMultiLangSchema.optional(),
                'common:referenceToCompleteReviewReport':
                  GlobalReferenceTypeSchema.optional(),
                'common:other': CommonOtherSchema.optional(),
                scope: z
                  .union([
                    z.intersection(
                      z.intersection(
                        z.object({
                          '@name': z.intersection(
                            z.union([
                              z.literal(
                                'Substance properties, physical and chemical',
                              ),
                              z.literal('Substance properties, biological'),
                              z.literal('Model for Transport and Fate'),
                              z.literal('Model for Exposure'),
                              z.literal('Model for Effect'),
                              z.literal('Model for Damage'),
                              z.literal('Characterisation factors'),
                              z.literal('Application of model'),
                              z.literal('Normalisation'),
                              z.literal('Weighting'),
                              z.literal('Documentation'),
                            ]),
                            z.string(),
                          ),
                          method: z
                            .union([
                              z.object({
                                '@name': z.intersection(
                                  z.union([
                                    z.literal(
                                      'Recollection / Validation of data',
                                    ),
                                    z.literal('Recalculation'),
                                    z.literal('Cross-check with other source'),
                                    z.literal(
                                      'Cross-check with other LCIA method(ology)',
                                    ),
                                    z.literal('Expert judgement'),
                                  ]),
                                  z.string(),
                                ),
                              }),
                              z.array(
                                z.object({
                                  '@name': z.intersection(
                                    z.union([
                                      z.literal(
                                        'Recollection / Validation of data',
                                      ),
                                      z.literal('Recalculation'),
                                      z.literal(
                                        'Cross-check with other source',
                                      ),
                                      z.literal(
                                        'Cross-check with other LCIA method(ology)',
                                      ),
                                      z.literal('Expert judgement'),
                                    ]),
                                    z.string(),
                                  ),
                                }),
                              ),
                            ])
                            .optional(),
                          'common:method': z
                            .union([
                              z.object({
                                '@name': z.intersection(
                                  z.union([
                                    z.literal(
                                      'Recollection / Validation of data',
                                    ),
                                    z.literal('Recalculation'),
                                    z.literal('Cross-check with other source'),
                                    z.literal(
                                      'Cross-check with other LCIA method(ology)',
                                    ),
                                    z.literal('Expert judgement'),
                                  ]),
                                  z.string(),
                                ),
                              }),
                              z.array(
                                z.object({
                                  '@name': z.intersection(
                                    z.union([
                                      z.literal(
                                        'Recollection / Validation of data',
                                      ),
                                      z.literal('Recalculation'),
                                      z.literal(
                                        'Cross-check with other source',
                                      ),
                                      z.literal(
                                        'Cross-check with other LCIA method(ology)',
                                      ),
                                      z.literal('Expert judgement'),
                                    ]),
                                    z.string(),
                                  ),
                                }),
                              ),
                            ])
                            .optional(),
                        }),
                        z.union([
                          z.object({ method: z.unknown() }),
                          z.object({ 'common:method': z.unknown() }),
                        ]),
                      ),
                      jsonSchemaNotRequired(['method', 'common:method']),
                    ),
                    z.array(
                      z.intersection(
                        z.intersection(
                          z.object({
                            '@name': z.intersection(
                              z.union([
                                z.literal(
                                  'Substance properties, physical and chemical',
                                ),
                                z.literal('Substance properties, biological'),
                                z.literal('Model for Transport and Fate'),
                                z.literal('Model for Exposure'),
                                z.literal('Model for Effect'),
                                z.literal('Model for Damage'),
                                z.literal('Characterisation factors'),
                                z.literal('Application of model'),
                                z.literal('Normalisation'),
                                z.literal('Weighting'),
                                z.literal('Documentation'),
                              ]),
                              z.string(),
                            ),
                            method: z
                              .union([
                                z.object({
                                  '@name': z.intersection(
                                    z.union([
                                      z.literal(
                                        'Recollection / Validation of data',
                                      ),
                                      z.literal('Recalculation'),
                                      z.literal(
                                        'Cross-check with other source',
                                      ),
                                      z.literal(
                                        'Cross-check with other LCIA method(ology)',
                                      ),
                                      z.literal('Expert judgement'),
                                    ]),
                                    z.string(),
                                  ),
                                }),
                                z.array(
                                  z.object({
                                    '@name': z.intersection(
                                      z.union([
                                        z.literal(
                                          'Recollection / Validation of data',
                                        ),
                                        z.literal('Recalculation'),
                                        z.literal(
                                          'Cross-check with other source',
                                        ),
                                        z.literal(
                                          'Cross-check with other LCIA method(ology)',
                                        ),
                                        z.literal('Expert judgement'),
                                      ]),
                                      z.string(),
                                    ),
                                  }),
                                ),
                              ])
                              .optional(),
                            'common:method': z
                              .union([
                                z.object({
                                  '@name': z.intersection(
                                    z.union([
                                      z.literal(
                                        'Recollection / Validation of data',
                                      ),
                                      z.literal('Recalculation'),
                                      z.literal(
                                        'Cross-check with other source',
                                      ),
                                      z.literal(
                                        'Cross-check with other LCIA method(ology)',
                                      ),
                                      z.literal('Expert judgement'),
                                    ]),
                                    z.string(),
                                  ),
                                }),
                                z.array(
                                  z.object({
                                    '@name': z.intersection(
                                      z.union([
                                        z.literal(
                                          'Recollection / Validation of data',
                                        ),
                                        z.literal('Recalculation'),
                                        z.literal(
                                          'Cross-check with other source',
                                        ),
                                        z.literal(
                                          'Cross-check with other LCIA method(ology)',
                                        ),
                                        z.literal('Expert judgement'),
                                      ]),
                                      z.string(),
                                    ),
                                  }),
                                ),
                              ])
                              .optional(),
                          }),
                          z.union([
                            z.object({ method: z.unknown() }),
                            z.object({ 'common:method': z.unknown() }),
                          ]),
                        ),
                        jsonSchemaNotRequired(['method', 'common:method']),
                      ),
                    ),
                  ])
                  .optional(),
                'common:scope': z
                  .union([
                    z.object({
                      '@name': z.intersection(
                        z.union([
                          z.literal(
                            'Substance properties, physical and chemical',
                          ),
                          z.literal('Substance properties, biological'),
                          z.literal('Model for Transport and Fate'),
                          z.literal('Model for Exposure'),
                          z.literal('Model for Effect'),
                          z.literal('Model for Damage'),
                          z.literal('Characterisation factors'),
                          z.literal('Application of model'),
                          z.literal('Normalisation'),
                          z.literal('Weighting'),
                          z.literal('Documentation'),
                        ]),
                        z.string(),
                      ),
                      'common:method': z.union([
                        z.object({
                          '@name': z.intersection(
                            z.union([
                              z.literal('Recollection / Validation of data'),
                              z.literal('Recalculation'),
                              z.literal('Cross-check with other source'),
                              z.literal(
                                'Cross-check with other LCIA method(ology)',
                              ),
                              z.literal('Expert judgement'),
                            ]),
                            z.string(),
                          ),
                        }),
                        z.array(
                          z.object({
                            '@name': z.intersection(
                              z.union([
                                z.literal('Recollection / Validation of data'),
                                z.literal('Recalculation'),
                                z.literal('Cross-check with other source'),
                                z.literal(
                                  'Cross-check with other LCIA method(ology)',
                                ),
                                z.literal('Expert judgement'),
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
                            z.literal(
                              'Substance properties, physical and chemical',
                            ),
                            z.literal('Substance properties, biological'),
                            z.literal('Model for Transport and Fate'),
                            z.literal('Model for Exposure'),
                            z.literal('Model for Effect'),
                            z.literal('Model for Damage'),
                            z.literal('Characterisation factors'),
                            z.literal('Application of model'),
                            z.literal('Normalisation'),
                            z.literal('Weighting'),
                            z.literal('Documentation'),
                          ]),
                          z.string(),
                        ),
                        'common:method': z.union([
                          z.object({
                            '@name': z.intersection(
                              z.union([
                                z.literal('Recollection / Validation of data'),
                                z.literal('Recalculation'),
                                z.literal('Cross-check with other source'),
                                z.literal(
                                  'Cross-check with other LCIA method(ology)',
                                ),
                                z.literal('Expert judgement'),
                              ]),
                              z.string(),
                            ),
                          }),
                          z.array(
                            z.object({
                              '@name': z.intersection(
                                z.union([
                                  z.literal(
                                    'Recollection / Validation of data',
                                  ),
                                  z.literal('Recalculation'),
                                  z.literal('Cross-check with other source'),
                                  z.literal(
                                    'Cross-check with other LCIA method(ology)',
                                  ),
                                  z.literal('Expert judgement'),
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
              }),
              jsonSchemaNotRequired(['scope', 'common:scope']),
            ),
            z.object({ '@type': z.literal('Not reviewed').optional() }),
            z.unknown(),
            z.intersection(
              z.object({
                'common:reviewDetails': z.unknown(),
                'common:referenceToNameOfReviewerAndInstitution': z.unknown(),
              }),
              z.union([
                z.object({ scope: z.unknown() }),
                z.object({ 'common:scope': z.unknown() }),
              ]),
            ),
          ),
          z
            .array(
              withJsonSchemaConditional(
                z.intersection(
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
                    'common:reviewDetails': FTMultiLangSchema.optional(),
                    'common:referenceToNameOfReviewerAndInstitution':
                      GlobalReferenceTypeSchema.optional(),
                    'common:otherReviewDetails': FTMultiLangSchema.optional(),
                    'common:referenceToCompleteReviewReport':
                      GlobalReferenceTypeSchema.optional(),
                    'common:other': CommonOtherSchema.optional(),
                    scope: z
                      .union([
                        z.intersection(
                          z.intersection(
                            z.object({
                              '@name': z.intersection(
                                z.union([
                                  z.literal(
                                    'Substance properties, physical and chemical',
                                  ),
                                  z.literal('Substance properties, biological'),
                                  z.literal('Model for Transport and Fate'),
                                  z.literal('Model for Exposure'),
                                  z.literal('Model for Effect'),
                                  z.literal('Model for Damage'),
                                  z.literal('Characterisation factors'),
                                  z.literal('Application of model'),
                                  z.literal('Normalisation'),
                                  z.literal('Weighting'),
                                  z.literal('Documentation'),
                                ]),
                                z.string(),
                              ),
                              method: z
                                .union([
                                  z.object({
                                    '@name': z.intersection(
                                      z.union([
                                        z.literal(
                                          'Recollection / Validation of data',
                                        ),
                                        z.literal('Recalculation'),
                                        z.literal(
                                          'Cross-check with other source',
                                        ),
                                        z.literal(
                                          'Cross-check with other LCIA method(ology)',
                                        ),
                                        z.literal('Expert judgement'),
                                      ]),
                                      z.string(),
                                    ),
                                  }),
                                  z.array(
                                    z.object({
                                      '@name': z.intersection(
                                        z.union([
                                          z.literal(
                                            'Recollection / Validation of data',
                                          ),
                                          z.literal('Recalculation'),
                                          z.literal(
                                            'Cross-check with other source',
                                          ),
                                          z.literal(
                                            'Cross-check with other LCIA method(ology)',
                                          ),
                                          z.literal('Expert judgement'),
                                        ]),
                                        z.string(),
                                      ),
                                    }),
                                  ),
                                ])
                                .optional(),
                              'common:method': z
                                .union([
                                  z.object({
                                    '@name': z.intersection(
                                      z.union([
                                        z.literal(
                                          'Recollection / Validation of data',
                                        ),
                                        z.literal('Recalculation'),
                                        z.literal(
                                          'Cross-check with other source',
                                        ),
                                        z.literal(
                                          'Cross-check with other LCIA method(ology)',
                                        ),
                                        z.literal('Expert judgement'),
                                      ]),
                                      z.string(),
                                    ),
                                  }),
                                  z.array(
                                    z.object({
                                      '@name': z.intersection(
                                        z.union([
                                          z.literal(
                                            'Recollection / Validation of data',
                                          ),
                                          z.literal('Recalculation'),
                                          z.literal(
                                            'Cross-check with other source',
                                          ),
                                          z.literal(
                                            'Cross-check with other LCIA method(ology)',
                                          ),
                                          z.literal('Expert judgement'),
                                        ]),
                                        z.string(),
                                      ),
                                    }),
                                  ),
                                ])
                                .optional(),
                            }),
                            z.union([
                              z.object({ method: z.unknown() }),
                              z.object({ 'common:method': z.unknown() }),
                            ]),
                          ),
                          jsonSchemaNotRequired(['method', 'common:method']),
                        ),
                        z.array(
                          z.intersection(
                            z.intersection(
                              z.object({
                                '@name': z.intersection(
                                  z.union([
                                    z.literal(
                                      'Substance properties, physical and chemical',
                                    ),
                                    z.literal(
                                      'Substance properties, biological',
                                    ),
                                    z.literal('Model for Transport and Fate'),
                                    z.literal('Model for Exposure'),
                                    z.literal('Model for Effect'),
                                    z.literal('Model for Damage'),
                                    z.literal('Characterisation factors'),
                                    z.literal('Application of model'),
                                    z.literal('Normalisation'),
                                    z.literal('Weighting'),
                                    z.literal('Documentation'),
                                  ]),
                                  z.string(),
                                ),
                                method: z
                                  .union([
                                    z.object({
                                      '@name': z.intersection(
                                        z.union([
                                          z.literal(
                                            'Recollection / Validation of data',
                                          ),
                                          z.literal('Recalculation'),
                                          z.literal(
                                            'Cross-check with other source',
                                          ),
                                          z.literal(
                                            'Cross-check with other LCIA method(ology)',
                                          ),
                                          z.literal('Expert judgement'),
                                        ]),
                                        z.string(),
                                      ),
                                    }),
                                    z.array(
                                      z.object({
                                        '@name': z.intersection(
                                          z.union([
                                            z.literal(
                                              'Recollection / Validation of data',
                                            ),
                                            z.literal('Recalculation'),
                                            z.literal(
                                              'Cross-check with other source',
                                            ),
                                            z.literal(
                                              'Cross-check with other LCIA method(ology)',
                                            ),
                                            z.literal('Expert judgement'),
                                          ]),
                                          z.string(),
                                        ),
                                      }),
                                    ),
                                  ])
                                  .optional(),
                                'common:method': z
                                  .union([
                                    z.object({
                                      '@name': z.intersection(
                                        z.union([
                                          z.literal(
                                            'Recollection / Validation of data',
                                          ),
                                          z.literal('Recalculation'),
                                          z.literal(
                                            'Cross-check with other source',
                                          ),
                                          z.literal(
                                            'Cross-check with other LCIA method(ology)',
                                          ),
                                          z.literal('Expert judgement'),
                                        ]),
                                        z.string(),
                                      ),
                                    }),
                                    z.array(
                                      z.object({
                                        '@name': z.intersection(
                                          z.union([
                                            z.literal(
                                              'Recollection / Validation of data',
                                            ),
                                            z.literal('Recalculation'),
                                            z.literal(
                                              'Cross-check with other source',
                                            ),
                                            z.literal(
                                              'Cross-check with other LCIA method(ology)',
                                            ),
                                            z.literal('Expert judgement'),
                                          ]),
                                          z.string(),
                                        ),
                                      }),
                                    ),
                                  ])
                                  .optional(),
                              }),
                              z.union([
                                z.object({ method: z.unknown() }),
                                z.object({ 'common:method': z.unknown() }),
                              ]),
                            ),
                            jsonSchemaNotRequired(['method', 'common:method']),
                          ),
                        ),
                      ])
                      .optional(),
                    'common:scope': z
                      .union([
                        z.object({
                          '@name': z.intersection(
                            z.union([
                              z.literal(
                                'Substance properties, physical and chemical',
                              ),
                              z.literal('Substance properties, biological'),
                              z.literal('Model for Transport and Fate'),
                              z.literal('Model for Exposure'),
                              z.literal('Model for Effect'),
                              z.literal('Model for Damage'),
                              z.literal('Characterisation factors'),
                              z.literal('Application of model'),
                              z.literal('Normalisation'),
                              z.literal('Weighting'),
                              z.literal('Documentation'),
                            ]),
                            z.string(),
                          ),
                          'common:method': z.union([
                            z.object({
                              '@name': z.intersection(
                                z.union([
                                  z.literal(
                                    'Recollection / Validation of data',
                                  ),
                                  z.literal('Recalculation'),
                                  z.literal('Cross-check with other source'),
                                  z.literal(
                                    'Cross-check with other LCIA method(ology)',
                                  ),
                                  z.literal('Expert judgement'),
                                ]),
                                z.string(),
                              ),
                            }),
                            z.array(
                              z.object({
                                '@name': z.intersection(
                                  z.union([
                                    z.literal(
                                      'Recollection / Validation of data',
                                    ),
                                    z.literal('Recalculation'),
                                    z.literal('Cross-check with other source'),
                                    z.literal(
                                      'Cross-check with other LCIA method(ology)',
                                    ),
                                    z.literal('Expert judgement'),
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
                                z.literal(
                                  'Substance properties, physical and chemical',
                                ),
                                z.literal('Substance properties, biological'),
                                z.literal('Model for Transport and Fate'),
                                z.literal('Model for Exposure'),
                                z.literal('Model for Effect'),
                                z.literal('Model for Damage'),
                                z.literal('Characterisation factors'),
                                z.literal('Application of model'),
                                z.literal('Normalisation'),
                                z.literal('Weighting'),
                                z.literal('Documentation'),
                              ]),
                              z.string(),
                            ),
                            'common:method': z.union([
                              z.object({
                                '@name': z.intersection(
                                  z.union([
                                    z.literal(
                                      'Recollection / Validation of data',
                                    ),
                                    z.literal('Recalculation'),
                                    z.literal('Cross-check with other source'),
                                    z.literal(
                                      'Cross-check with other LCIA method(ology)',
                                    ),
                                    z.literal('Expert judgement'),
                                  ]),
                                  z.string(),
                                ),
                              }),
                              z.array(
                                z.object({
                                  '@name': z.intersection(
                                    z.union([
                                      z.literal(
                                        'Recollection / Validation of data',
                                      ),
                                      z.literal('Recalculation'),
                                      z.literal(
                                        'Cross-check with other source',
                                      ),
                                      z.literal(
                                        'Cross-check with other LCIA method(ology)',
                                      ),
                                      z.literal('Expert judgement'),
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
                  }),
                  jsonSchemaNotRequired(['scope', 'common:scope']),
                ),
                z.object({ '@type': z.literal('Not reviewed').optional() }),
                z.unknown(),
                z.intersection(
                  z.object({
                    'common:reviewDetails': z.unknown(),
                    'common:referenceToNameOfReviewerAndInstitution':
                      z.unknown(),
                  }),
                  z.union([
                    z.object({ scope: z.unknown() }),
                    z.object({ 'common:scope': z.unknown() }),
                  ]),
                ),
              ),
            )
            .min(1),
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
      'common:commissionerAndGoal': z
        .object({
          'common:referenceToCommissioner':
            GlobalReferenceTypeSchema.optional(),
          'common:project': StringMultiLangSchema.optional(),
          'common:intendedApplications': FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        })
        .optional(),
      dataGenerator: z.object({
        'common:referenceToPersonOrEntityGeneratingTheDataSet':
          GlobalReferenceTypeSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      dataEntryBy: z.object({
        'common:timeStamp': dateTimeSchema,
        'common:referenceToDataSetFormat': GlobalReferenceTypeSchema,
        'common:referenceToConvertedOriginalDataSetFrom':
          GlobalReferenceTypeSchema.optional(),
        'common:referenceToPersonOrEntityEnteringTheData':
          GlobalReferenceTypeSchema.optional(),
        recommendationBy: z.object({
          referenceToEntity: GlobalReferenceTypeSchema,
          level: z.intersection(
            z.union([
              z.literal('Level I'),
              z.literal('Level II'),
              z.literal('Level III'),
              z.literal('Interim'),
              z.literal('Not recommended'),
            ]),
            z.string(),
          ),
          meaning: RequiredFTMultiLangSchema,
        }),
        'common:other': CommonOtherSchema.optional(),
      }),
      publicationAndOwnership: z.object({
        'common:dateOfLastRevision': dateTimeSchema,
        'common:dataSetVersion': VersionSchema,
        'common:referenceToPrecedingDataSetVersion':
          GlobalReferenceTypeSchema.optional(),
        'common:permanentDataSetURI': z.url().optional(),
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
        'common:referenceToOwnershipOfDataSet': GlobalReferenceTypeSchema,
        'common:copyright': z
          .intersection(
            z.union([z.literal('true'), z.literal('false')]),
            z.string(),
          )
          .optional(),
        'common:accessRestrictions': FTMultiLangSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
    characterisationFactors: z.object({
      factor: z.union([
        z.intersection(
          z.object({
            referenceToFlowDataSet: GlobalReferenceTypeSchema,
            location: z.string().optional(),
            exchangeDirection: z.intersection(
              z.union([z.literal('Input'), z.literal('Output')]),
              z.string(),
            ),
            meanValue: RealSchema,
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
            dataDerivationTypeStatus: z
              .intersection(
                z.union([
                  z.literal('Measured'),
                  z.literal('Calculated'),
                  z.literal('Estimated'),
                  z.literal('Unknown derivation'),
                  z.literal('Missing important'),
                  z.literal('Missing unimportant'),
                ]),
                z.string(),
              )
              .optional(),
            deviatingRecommendation: z.intersection(
              z.union([
                z.literal('Level I'),
                z.literal('Level II'),
                z.literal('Level III'),
                z.literal('Interim'),
                z.literal('Not recommended'),
              ]),
              z.string(),
            ),
            generalComment: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
            referencesToDataSource: z
              .object({
                referenceToDataSource: GlobalReferenceTypeSchema,
                'common:other': CommonOtherSchema.optional(),
              })
              .optional(),
            referenceToDataSource: z
              .union([
                GlobalReferenceTypeSchema,
                z.object({
                  referenceToDataSource: GlobalReferenceTypeSchema,
                  'common:other': CommonOtherSchema.optional(),
                }),
              ])
              .optional(),
          }),
          jsonSchemaNotRequired([
            'referenceToDataSource',
            'referencesToDataSource',
          ]),
        ),
        z.array(
          z.intersection(
            z.object({
              referenceToFlowDataSet: GlobalReferenceTypeSchema,
              location: z.string().optional(),
              exchangeDirection: z.intersection(
                z.union([z.literal('Input'), z.literal('Output')]),
                z.string(),
              ),
              meanValue: RealSchema,
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
              dataDerivationTypeStatus: z
                .intersection(
                  z.union([
                    z.literal('Measured'),
                    z.literal('Calculated'),
                    z.literal('Estimated'),
                    z.literal('Unknown derivation'),
                    z.literal('Missing important'),
                    z.literal('Missing unimportant'),
                  ]),
                  z.string(),
                )
                .optional(),
              deviatingRecommendation: z.intersection(
                z.union([
                  z.literal('Level I'),
                  z.literal('Level II'),
                  z.literal('Level III'),
                  z.literal('Interim'),
                  z.literal('Not recommended'),
                ]),
                z.string(),
              ),
              generalComment: StringMultiLangSchema.optional(),
              referencesToDataSource: z
                .object({
                  referenceToDataSource: GlobalReferenceTypeSchema,
                  'common:other': CommonOtherSchema.optional(),
                })
                .optional(),
              referenceToDataSource: z
                .union([
                  GlobalReferenceTypeSchema,
                  z.object({
                    referenceToDataSource: GlobalReferenceTypeSchema,
                    'common:other': CommonOtherSchema.optional(),
                  }),
                ])
                .optional(),
              'common:other': CommonOtherSchema.optional(),
            }),
            jsonSchemaNotRequired([
              'referenceToDataSource',
              'referencesToDataSource',
            ]),
          ),
        ),
      ]),
      'common:other': CommonOtherSchema.optional(),
    }),
    'common:other': CommonOtherSchema.optional(),
  }),
});
