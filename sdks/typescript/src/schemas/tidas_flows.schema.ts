// Generated directly from TIDAS JSON Schema: tidas_flows.json
import { z } from 'zod';
import {
  jsonSchemaOneOf,
  jsonSchemaTuple,
  withJsonSchemaDependencies,
} from './../core/validation/json-schema';
import {
  CASNumberSchema,
  CommonOtherSchema,
  FTMultiLangSchema,
  GlobalReferenceTypeSchema,
  Int5Schema,
  LevelTypeSchema,
  PercSchema,
  RealSchema,
  StringMultiLangSchema,
  RequiredStringMultiLangSchema,
  StringSchema,
  UUIDSchema,
  VersionSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';
import { FlowsElementaryCategorySchema } from './tidas_flows_elementary_category.schema';
import { FlowsProductCategorySchema } from './tidas_flows_product_category.schema';
import { LocationsCategorySchema } from './tidas_locations_category.schema';

export const ElementaryFlowCategorizationSchema = z.object({
  'common:category': jsonSchemaTuple(
    [
      withJsonSchemaDependencies(
        z.object({
          '@level': z.intersection(z.literal('0'), LevelTypeSchema),
          '@catId': z.string(),
          '#text': z.string(),
        }),
        [{ property: '@level', schema: FlowsElementaryCategorySchema }],
      ),
      withJsonSchemaDependencies(
        z.object({
          '@level': z.intersection(z.literal('1'), LevelTypeSchema),
          '@catId': z.string(),
          '#text': z.string(),
        }),
        [{ property: '@level', schema: FlowsElementaryCategorySchema }],
      ),
      withJsonSchemaDependencies(
        z.object({
          '@level': z.intersection(z.literal('2'), LevelTypeSchema),
          '@catId': z.string(),
          '#text': z.string(),
        }),
        [{ property: '@level', schema: FlowsElementaryCategorySchema }],
      ),
    ],
    { additionalItems: false, maxItems: 3, uniqueItems: true },
  ),
  'common:other': CommonOtherSchema.optional(),
});

const FLOW_NAME_CONDITIONAL_FIELDS = [
  'treatmentStandardsRoutes',
  'mixAndLocationTypes',
] as const;

export const FlowsSchema = z
  .object({
    flowDataSet: z.object({
      '@xmlns': z.intersection(
        z.literal('http://lca.jrc.it/ILCD/Flow'),
        z.string(),
      ),
      '@xmlns:common': z.intersection(
        z.literal('http://lca.jrc.it/ILCD/Common'),
        z.string(),
      ),
      '@xmlns:ecn': z.intersection(
        z.literal(
          'http://eplca.jrc.ec.europa.eu/ILCD/Extensions/2018/ECNumber',
        ),
        z.string(),
      ),
      '@xmlns:xsi': z.intersection(
        z.literal('http://www.w3.org/2001/XMLSchema-instance'),
        z.string(),
      ),
      '@version': z.intersection(z.literal('1.1'), z.string()),
      '@locations': z.intersection(
        z.literal('../ILCDLocations.xml'),
        z.string(),
      ),
      '@xsi:schemaLocation': z.intersection(
        z.literal(
          'http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd',
        ),
        z.string(),
      ),
      flowInformation: z.object({
        dataSetInformation: z.object({
          'common:UUID': UUIDSchema,
          name: z.object({
            baseName: RequiredStringMultiLangSchema,
            treatmentStandardsRoutes: StringMultiLangSchema.optional(),
            mixAndLocationTypes: StringMultiLangSchema.optional(),
            flowProperties: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
          'common:synonyms': FTMultiLangSchema.optional(),
          classificationInformation: z.intersection(
            z.object({
              'common:elementaryFlowCategorization': z
                .union([
                  ElementaryFlowCategorizationSchema,
                  z.array(ElementaryFlowCategorizationSchema).min(1),
                ])
                .optional(),
              'common:classification': z
                .union([
                  z.object({
                    'common:class': jsonSchemaTuple(
                      [
                        withJsonSchemaDependencies(
                          z.object({
                            '@level': z.intersection(
                              z.literal('0'),
                              LevelTypeSchema,
                            ),
                            '@classId': z.string(),
                            '#text': z.string(),
                          }),
                          [
                            {
                              property: '@level',
                              schema: FlowsProductCategorySchema,
                            },
                          ],
                        ),
                        withJsonSchemaDependencies(
                          z.object({
                            '@level': z.intersection(
                              z.literal('1'),
                              LevelTypeSchema,
                            ),
                            '@classId': z.string(),
                            '#text': z.string(),
                          }),
                          [
                            {
                              property: '@level',
                              schema: FlowsProductCategorySchema,
                            },
                          ],
                        ),
                        withJsonSchemaDependencies(
                          z.object({
                            '@level': z.intersection(
                              z.literal('2'),
                              LevelTypeSchema,
                            ),
                            '@classId': z.string(),
                            '#text': z.string(),
                          }),
                          [
                            {
                              property: '@level',
                              schema: FlowsProductCategorySchema,
                            },
                          ],
                        ),
                        withJsonSchemaDependencies(
                          z.object({
                            '@level': z.intersection(
                              z.literal('3'),
                              LevelTypeSchema,
                            ),
                            '@classId': z.string(),
                            '#text': z.string(),
                          }),
                          [
                            {
                              property: '@level',
                              schema: FlowsProductCategorySchema,
                            },
                          ],
                        ),
                        withJsonSchemaDependencies(
                          z.object({
                            '@level': z.intersection(
                              z.literal('4'),
                              LevelTypeSchema,
                            ),
                            '@classId': z.string(),
                            '#text': z.string(),
                          }),
                          [
                            {
                              property: '@level',
                              schema: FlowsProductCategorySchema,
                            },
                          ],
                        ),
                      ],
                      {
                        additionalItems: false,
                        maxItems: 5,
                        uniqueItems: true,
                      },
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
                ])
                .optional(),
            }),
            jsonSchemaOneOf([
              z.object({ 'common:elementaryFlowCategorization': z.unknown() }),
              z.object({ 'common:classification': z.unknown() }),
            ]),
          ),
          CASNumber: CASNumberSchema.optional(),
          sumFormula: StringSchema.optional(),
          'common:generalComment': FTMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        quantitativeReference: z.object({
          referenceToReferenceFlowProperty: Int5Schema,
          'common:other': CommonOtherSchema.optional(),
        }),
        geography: z
          .object({
            locationOfSupply: z
              .union([
                LocationsCategorySchema,
                z.array(LocationsCategorySchema).min(1),
              ])
              .optional(),
            'common:other': CommonOtherSchema.optional(),
          })
          .optional(),
        technology: z
          .object({
            technologicalApplicability: FTMultiLangSchema.optional(),
            referenceToTechnicalSpecification:
              GlobalReferenceTypeSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          })
          .optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      modellingAndValidation: z.object({
        LCIMethod: z.object({
          typeOfDataSet: z.intersection(
            z.union([
              z.literal('Elementary flow'),
              z.literal('Product flow'),
              z.literal('Waste flow'),
              z.literal('Other flow'),
            ]),
            z.string(),
          ),
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
        dataEntryBy: z.object({
          'common:timeStamp': dateTimeSchema,
          'common:referenceToDataSetFormat': GlobalReferenceTypeSchema,
          'common:referenceToPersonOrEntityEnteringTheData':
            GlobalReferenceTypeSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        publicationAndOwnership: z.object({
          'common:dataSetVersion': VersionSchema,
          'common:referenceToPrecedingDataSetVersion':
            GlobalReferenceTypeSchema.optional(),
          'common:permanentDataSetURI': z.url().optional(),
          'common:referenceToOwnershipOfDataSet': GlobalReferenceTypeSchema,
          'common:other': CommonOtherSchema.optional(),
        }),
        'common:other': CommonOtherSchema.optional(),
      }),
      flowProperties: z.object({
        flowProperty: z.union([
          z.object({
            '@dataSetInternalID': Int5Schema,
            referenceToFlowPropertyDataSet: GlobalReferenceTypeSchema,
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
                ]),
                z.string(),
              )
              .optional(),
            generalComment: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
          z.array(
            z.object({
              '@dataSetInternalID': Int5Schema,
              referenceToFlowPropertyDataSet: GlobalReferenceTypeSchema,
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
                  ]),
                  z.string(),
                )
                .optional(),
              generalComment: StringMultiLangSchema.optional(),
              'common:other': CommonOtherSchema.optional(),
            }),
          ),
        ]),
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
  })
  .superRefine((value, ctx) => {
    const dataSet = value.flowDataSet;
    if (
      dataSet.modellingAndValidation.LCIMethod.typeOfDataSet ===
      'Elementary flow'
    ) {
      return;
    }

    const name = dataSet.flowInformation.dataSetInformation.name;
    for (const field of FLOW_NAME_CONDITIONAL_FIELDS) {
      if (name[field] === undefined) {
        ctx.addIssue({
          code: 'custom',
          path: [
            'flowDataSet',
            'flowInformation',
            'dataSetInformation',
            'name',
            field,
          ],
          message: 'Required',
        });
      }
    }
  });
