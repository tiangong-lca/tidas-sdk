// Generated directly from TIDAS JSON Schema: tidas_flowproperties.json
import { z } from 'zod';
import { withJsonSchemaDependencies } from './../core/validation/json-schema';
import {
  CommonOtherSchema,
  FTMultiLangSchema,
  GlobalReferenceTypeSchema,
  LevelTypeSchema,
  RequiredStringMultiLangSchema,
  UUIDSchema,
  VersionSchema,
} from './tidas_data_types.schema';
import { FlowPropertySchema } from './tidas_flowproperties_category.schema';

export const FlowpropertiesSchema = z.object({
  flowPropertyDataSet: z.object({
    '@xmlns': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/FlowProperty'),
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
    '@version': z.intersection(z.literal('1.1'), z.string()),
    '@xsi:schemaLocation': z.intersection(
      z.literal(
        'http://lca.jrc.it/ILCD/FlowProperty ../../schemas/ILCD_FlowPropertyDataSet.xsd',
      ),
      z.string(),
    ),
    flowPropertiesInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        'common:name': RequiredStringMultiLangSchema,
        'common:synonyms': FTMultiLangSchema.optional(),
        classificationInformation: z.object({
          'common:classification': z.union([
            z.object({
              'common:class': withJsonSchemaDependencies(
                z.object({
                  '@level': LevelTypeSchema,
                  '@classId': z.string(),
                  '#text': z.string(),
                }),
                [{ property: '@level', schema: FlowPropertySchema }],
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
        'common:generalComment': FTMultiLangSchema.optional(),
        'common:other': CommonOtherSchema.optional(),
      }),
      quantitativeReference: z.object({
        referenceToReferenceUnitGroup: GlobalReferenceTypeSchema,
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
    modellingAndValidation: z
      .object({
        dataSourcesTreatmentAndRepresentativeness: z
          .object({
            referenceToDataSource: GlobalReferenceTypeSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          })
          .optional(),
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
                }),
              )
              .min(1),
          ]),
          'common:other': CommonOtherSchema.optional(),
        }),
        'common:other': CommonOtherSchema.optional(),
      })
      .optional(),
    administrativeInformation: z.object({
      dataEntryBy: z.object({
        'common:timeStamp': z.iso.datetime({ offset: true }),
        'common:referenceToDataSetFormat': GlobalReferenceTypeSchema,
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
    'common:other': CommonOtherSchema.optional(),
  }),
});
