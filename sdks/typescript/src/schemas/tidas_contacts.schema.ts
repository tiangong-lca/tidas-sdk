// Generated directly from TIDAS JSON Schema: tidas_contacts.json
import { z } from 'zod';
import {
  jsonSchemaTuple,
  withJsonSchemaDependencies,
} from './../core/validation/json-schema';
import { ContactSchema } from './tidas_contacts_category.schema';
import {
  CommonOtherSchema,
  GlobalReferenceTypeSchema,
  LevelTypeSchema,
  STMultiLangSchema,
  STSchema,
  RequiredStringMultiLangSchema,
  StringSchema,
  UUIDSchema,
  VersionSchema,
  dateTimeSchema,
} from './tidas_data_types.schema';

export const ContactsSchema = z.object({
  contactDataSet: z.object({
    '@xmlns': z.intersection(
      z.literal('http://lca.jrc.it/ILCD/Contact'),
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
        'http://lca.jrc.it/ILCD/Contact ../../schemas/ILCD_ContactDataSet.xsd',
      ),
      z.string(),
    ),
    contactInformation: z.object({
      dataSetInformation: z.object({
        'common:UUID': UUIDSchema,
        'common:shortName': RequiredStringMultiLangSchema,
        'common:name': RequiredStringMultiLangSchema,
        classificationInformation: z.object({
          'common:classification': z.union([
            z.object({
              'common:class': z.union([
                jsonSchemaTuple(
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
                      [{ property: '@level', schema: ContactSchema }],
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
                      [{ property: '@level', schema: ContactSchema }],
                    ),
                  ],
                  { additionalItems: false, maxItems: 2, uniqueItems: true },
                ),
                withJsonSchemaDependencies(
                  z.object({
                    '@level': z.intersection(z.literal('0'), LevelTypeSchema),
                    '@classId': z.string(),
                    '#text': z.string(),
                  }),
                  [{ property: '@level', schema: ContactSchema }],
                ),
              ]),
              '@name': z.string().optional(),
              '@classes': z.string().optional(),
              'common:other': CommonOtherSchema.optional(),
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
          'common:other': CommonOtherSchema.optional(),
        }),
        contactAddress: STMultiLangSchema.optional(),
        email: z.intersection(StringSchema, z.email()).optional(),
        telephone: StringSchema.optional(),
        telefax: StringSchema.optional(),
        WWWAddress: STSchema.optional(),
        centralContactPoint: STMultiLangSchema.optional(),
        contactDescriptionOrComment: STMultiLangSchema.optional(),
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
  'common:other': CommonOtherSchema.optional(),
});
