// Generated directly from TIDAS JSON Schema: tidas_unitgroups.json
import { z } from 'zod';
import { withJsonSchemaDependencies } from './../core/validation/json-schema';
import {
  CommonOtherSchema,
  FTMultiLangSchema,
  GlobalReferenceTypeSchema,
  Int5Schema,
  LevelTypeSchema,
  RealSchema,
  StringMultiLangSchema,
  RequiredStringMultiLangSchema,
  StringSchema,
  UUIDSchema,
  VersionSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';
import { UnitGroupSchema } from './tidas_unitgroups_category.schema';

export const UnitgroupsSchema = z.object({
  unitGroupDataSet: z.object({
    '@xmlns': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/UnitGroup'),
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
        'http://lca.jrc.it/ILCD/UnitGroup ../../schemas/ILCD_UnitGroupDataSet.xsd',
      ),
      z.string(),
    ),
    unitGroupInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        'common:name': RequiredStringMultiLangSchema,
        classificationInformation: z.object({
          'common:classification': z.union([
            z.object({
              'common:class': withJsonSchemaDependencies(
                z.object({
                  '@level': z.intersection(z.literal('0'), LevelTypeSchema),
                  '@classId': z.string(),
                  '#text': z.string(),
                }),
                [{ property: '@level', schema: UnitGroupSchema }],
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
        referenceToReferenceUnit: Int5Schema,
        'common:other': CommonOtherSchema.optional(),
      }),
      'common:other': CommonOtherSchema.optional(),
    }),
    modellingAndValidation: z.object({
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
    units: z.object({
      unit: z.union([
        z.object({
          '@dataSetInternalID': Int5Schema.optional(),
          name: StringSchema,
          meanValue: RealSchema,
          generalComment: StringMultiLangSchema.optional(),
          'common:other': CommonOtherSchema.optional(),
        }),
        z.array(
          z.object({
            '@dataSetInternalID': Int5Schema.optional(),
            name: StringSchema,
            meanValue: RealSchema,
            generalComment: StringMultiLangSchema.optional(),
            'common:other': CommonOtherSchema.optional(),
          }),
        ),
      ]),
      'common:other': CommonOtherSchema.optional(),
    }),
    'common:other': CommonOtherSchema.optional(),
  }),
});
