// Generated directly from TIDAS JSON Schema: tidas_sources.json
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
  dateTimeSchema,
} from './tidas_data_types.schema';
import { SourceSchema } from './tidas_sources_category.schema';

export const SourcesSchema = z.object({
  sourceDataSet: z.object({
    '@xmlns:common': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Common'),
      z.string(),
    ),
    '@xmlns': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Source'),
      z.string(),
    ),
    '@xmlns:xsi': z.intersection(
      z.literal('http://www.w3.org/2001/XMLSchema-instance'),
      z.string(),
    ),
    '@version': z.intersection(z.literal('1.1'), z.string()),
    '@xsi:schemaLocation': z.intersection(
      z.literal(
        'http://lca.jrc.it/ILCD/Source ../../schemas/ILCD_SourceDataSet.xsd',
      ),
      z.string(),
    ),
    sourceInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        'common:shortName': RequiredStringMultiLangSchema,
        classificationInformation: z.object({
          'common:classification': z.union([
            z.object({
              'common:class': withJsonSchemaDependencies(
                z.object({
                  '@level': z.intersection(z.literal('0'), LevelTypeSchema),
                  '@classId': z.string(),
                  '#text': z.string(),
                }),
                [{ property: '@level', schema: SourceSchema }],
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
        sourceCitation: z.string().optional(),
        publicationType: z
          .intersection(
            z.union([
              z.literal('Undefined'),
              z.literal('Article in periodical'),
              z.literal('Chapter in anthology'),
              z.literal('Monograph'),
              z.literal('Direct measurement'),
              z.literal('Oral communication'),
              z.literal('Personal written communication'),
              z.literal('Questionnaire'),
              z.literal('Software or database'),
              z.literal('Other unpublished and grey literature'),
            ]),
            z.string(),
          )
          .optional(),
        sourceDescriptionOrComment: FTMultiLangSchema.optional(),
        referenceToDigitalFile: z
          .union([
            z.object({ '@uri': z.string().optional() }),
            z.array(z.object({ '@uri': z.string().optional() })).min(1),
          ])
          .optional(),
        referenceToContact: GlobalReferenceTypeSchema.optional(),
        referenceToLogo: GlobalReferenceTypeSchema.optional(),
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
    'common:other': CommonOtherSchema.optional(),
  }),
});
