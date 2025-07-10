/**
 * TIDAS-specific factory functions using ZodProxy for true property access
 */

import { z } from 'zod';
import { createZodProxy, ZodProxyOptions } from './zod-proxy';

// Import existing Zod schemas (we'll need to check what's available)
// For now, let's create basic schemas as examples

/**
 * Basic Contact schema for demonstration
 * TODO: Replace with actual generated schemas from src/schemas/
 */
import {
  ContactSchema,
  SourceSchema,
  FlowSchema,
  ProcessSchema,
  FlowPropertySchema,
  UnitGroupSchema,
  LCIAMethodSchema,
  LifeCycleModelSchema,
} from '../schemas/index';

// const ContactSchema = z.object({
//   contactDataSet: z.object({
//     '@xmlns': z.string().optional(),
//     '@xmlns:common': z.string().optional(),
//     '@version': z.string().optional(),
//     contactInformation: z
//       .object({
//         dataSetInformation: z
//           .object({
//             'common:UUID': z.string().uuid().optional(),
//             'common:name': z
//               .array(
//                 z.object({
//                   '@xml:lang': z.string(),
//                   '#text': z.string(),
//                 })
//               )
//               .or(
//                 z.object({
//                   '@xml:lang': z.string(),
//                   '#text': z.string(),
//                 })
//               )
//               .optional(),
//             'common:shortName': z
//               .array(
//                 z.object({
//                   '@xml:lang': z.string(),
//                   '#text': z.string(),
//                 })
//               )
//               .or(
//                 z.object({
//                   '@xml:lang': z.string(),
//                   '#text': z.string(),
//                 })
//               )
//               .optional(),
//             email: z.string().email().optional(),
//             telephone: z.string().optional(),
//             WWWAddress: z.string().url().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//     administrativeInformation: z
//       .object({
//         dataEntryBy: z
//           .object({
//             'common:timeStamp': z.string().optional(),
//             'common:referenceToPersonOrEntityEnteringTheData': z
//               .object({
//                 '@refObjectId': z.string().uuid().optional(),
//                 '@type': z.string().optional(),
//                 '@uri': z.string().optional(),
//                 '@version': z.string().optional(),
//                 'common:shortDescription': z
//                   .array(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .optional(),
//               })
//               .optional(),
//           })
//           .optional(),
//         publicationAndOwnership: z
//           .object({
//             'common:dataSetVersion': z.string().optional(),
//             'common:workflowAndPublicationStatus': z.string().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//   }),
// });

/**
 * Basic Flow schema for demonstration
 * TODO: Replace with actual generated schemas from src/schemas/
 */
// const FlowSchema = z.object({
//   flowDataSet: z.object({
//     '@xmlns': z.string().optional(),
//     '@xmlns:common': z.string().optional(),
//     '@version': z.string().optional(),
//     flowInformation: z
//       .object({
//         dataSetInformation: z
//           .object({
//             'common:UUID': z.string().uuid().optional(),
//             name: z
//               .object({
//                 baseName: z
//                   .array(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .or(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .optional(),
//                 flowProperties: z
//                   .array(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .optional(),
//               })
//               .optional(),
//             CASNumber: z.string().optional(),
//             typeOfDataSet: z.string().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//     modellingAndValidation: z
//       .object({
//         LCIMethod: z
//           .object({
//             typeOfDataSet: z.string().optional(),
//             deviationsFromLCIMethodPrinciple: z
//               .array(
//                 z.object({
//                   '@xml:lang': z.string(),
//                   '#text': z.string(),
//                 })
//               )
//               .optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//     administrativeInformation: z
//       .object({
//         dataEntryBy: z
//           .object({
//             'common:timeStamp': z.string().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//   }),
// });

/**
 * Basic Process schema for demonstration
 * TODO: Replace with actual generated schemas from src/schemas/
 */
// const ProcessSchema = z.object({
//   processDataSet: z.object({
//     '@xmlns': z.string().optional(),
//     '@xmlns:common': z.string().optional(),
//     '@version': z.string().optional(),
//     processInformation: z
//       .object({
//         dataSetInformation: z
//           .object({
//             'common:UUID': z.string().uuid().optional(),
//             name: z
//               .object({
//                 baseName: z
//                   .array(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .or(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .optional(),
//               })
//               .optional(),
//             classificationInformation: z
//               .object({
//                 'common:classification': z
//                   .array(
//                     z.object({
//                       'common:class': z
//                         .array(
//                           z.object({
//                             '@classId': z.string().optional(),
//                             '@level': z.string().optional(),
//                             '#text': z.string().optional(),
//                           })
//                         )
//                         .optional(),
//                     })
//                   )
//                   .optional(),
//               })
//               .optional(),
//           })
//           .optional(),
//         geography: z
//           .object({
//             locationOfOperationSupplyOrProduction: z
//               .object({
//                 '@location': z.string().optional(),
//                 'common:shortDescription': z
//                   .array(
//                     z.object({
//                       '@xml:lang': z.string(),
//                       '#text': z.string(),
//                     })
//                   )
//                   .optional(),
//               })
//               .optional(),
//           })
//           .optional(),
//         time: z
//           .object({
//             referenceYear: z.string().optional(),
//             dataSetValidUntil: z.string().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//     exchanges: z
//       .object({
//         exchange: z
//           .array(
//             z.object({
//               '@dataSetInternalID': z.string().optional(),
//               referenceToFlowDataSet: z
//                 .object({
//                   '@refObjectId': z.string().uuid().optional(),
//                   '@type': z.string().optional(),
//                   '@uri': z.string().optional(),
//                   '@version': z.string().optional(),
//                 })
//                 .optional(),
//               meanAmount: z.number().optional(),
//               resultingAmount: z.number().optional(),
//               uncertaintyDistributionType: z.string().optional(),
//             })
//           )
//           .optional(),
//       })
//       .optional(),
//     administrativeInformation: z
//       .object({
//         dataEntryBy: z
//           .object({
//             'common:timeStamp': z.string().optional(),
//           })
//           .optional(),
//       })
//       .optional(),
//   }),
// });

// Type definitions
export type ZodContact = z.infer<typeof ContactSchema>;
export type ZodFlow = z.infer<typeof FlowSchema>;
export type ZodProcess = z.infer<typeof ProcessSchema>;
export type ZodFlowProperty = z.infer<typeof FlowPropertySchema>;
export type ZodUnitGroup = z.infer<typeof UnitGroupSchema>;
export type ZodLCIAMethod = z.infer<typeof LCIAMethodSchema>;
export type ZodLifeCycleModel = z.infer<typeof LifeCycleModelSchema>;
export type ZodSource = z.infer<typeof SourceSchema>;

/**
 * TIDAS-specific proxy options with sensible defaults
 */
interface TidasProxyOptions extends ZodProxyOptions {
  autoGenerateUUID?: boolean;
  autoGenerateTimestamp?: boolean;
  defaultLanguage?: string;
}

/**
 * Enhanced proxy result with TIDAS-specific helpers
 */
interface TidasProxyResult<T> {
  proxy: T;
  getAccessLog: () => any[];
  getValues: () => Record<string, any>;
  buildObject: () => any;
  validate: () => any;
  debug: () => any;
  // TIDAS-specific helpers
  setMultiLangText: (path: string, text: string, lang?: string) => void;
  getMultiLangText: (path: string, lang?: string) => string;
  generateUUID: (path: string) => void;
  setCurrentTimestamp: (path: string) => void;
}

/**
 * Create enhanced proxy with TIDAS-specific functionality
 */
function createTidasProxy<T extends z.ZodSchema>(
  schema: T,
  options: TidasProxyOptions = {}
): TidasProxyResult<z.infer<T>> {
  const defaultOptions: TidasProxyOptions = {
    enableLogging: true,
    throwOnValidationError: false,
    autoCreateArrays: true,
    autoGenerateUUID: false,
    autoGenerateTimestamp: false,
    defaultLanguage: 'en',
    ...options,
  };

  const zodProxy = createZodProxy(schema, defaultOptions);

  // Helper function to generate UUID
  const generateUUID = (): string => {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(
      /[xy]/g,
      function (c) {
        const r = (Math.random() * 16) | 0;
        const v = c === 'x' ? r : (r & 0x3) | 0x8;
        return v.toString(16);
      }
    );
  };

  // Helper function to get current timestamp
  const getCurrentTimestamp = (): string => {
    return new Date().toISOString();
  };

  // Helper function to set multi-language text
  const setMultiLangText = (
    path: string,
    text: string,
    lang: string = defaultOptions.defaultLanguage || 'en'
  ): void => {
    const multiLangValue = {
      '@xml:lang': lang,
      '#text': text,
    };

    // Access the proxy through the path and set the value
    const pathParts = path.split('.');
    let current: any = zodProxy.proxy;

    for (let i = 0; i < pathParts.length - 1; i++) {
      const part = pathParts[i];
      if (!current[part]) {
        current[part] = {};
      }
      current = current[part];
    }

    const lastPart = pathParts[pathParts.length - 1];
    current[lastPart] = multiLangValue;
  };

  // Helper function to get multi-language text
  const getMultiLangText = (
    path: string,
    lang: string = defaultOptions.defaultLanguage || 'en'
  ): string => {
    const pathParts = path.split('.');
    let current: any = zodProxy.proxy;

    try {
      for (const part of pathParts) {
        current = current[part];
        if (!current) return '';
      }

      if (Array.isArray(current)) {
        const found = current.find((item) => item['@xml:lang'] === lang);
        return found ? found['#text'] : '';
      } else if (current && typeof current === 'object') {
        return current['@xml:lang'] === lang ? current['#text'] || '' : '';
      }

      return String(current || '');
    } catch {
      return '';
    }
  };

  // Helper function to generate UUID at path
  const generateUUIDAtPath = (path: string): void => {
    const pathParts = path.split('.');
    let current: any = zodProxy.proxy;

    for (let i = 0; i < pathParts.length - 1; i++) {
      const part = pathParts[i];
      if (!current[part]) {
        current[part] = {};
      }
      current = current[part];
    }

    const lastPart = pathParts[pathParts.length - 1];
    current[lastPart] = generateUUID();
  };

  // Helper function to set current timestamp at path
  const setCurrentTimestampAtPath = (path: string): void => {
    const pathParts = path.split('.');
    let current: any = zodProxy.proxy;

    for (let i = 0; i < pathParts.length - 1; i++) {
      const part = pathParts[i];
      if (!current[part]) {
        current[part] = {};
      }
      current = current[part];
    }

    const lastPart = pathParts[pathParts.length - 1];
    current[lastPart] = getCurrentTimestamp();
  };

  return {
    ...zodProxy,
    setMultiLangText,
    getMultiLangText,
    generateUUID: generateUUIDAtPath,
    setCurrentTimestamp: setCurrentTimestampAtPath,
  };
}

/**
 * Create a Contact proxy with type-safe property access
 */
export function createZodContact(
  options: TidasProxyOptions = {}
): TidasProxyResult<ZodContact> {
  return createTidasProxy(ContactSchema, options);
}

/**
 * Create a Flow proxy with type-safe property access
 */
export function createZodFlow(
  options: TidasProxyOptions = {}
): TidasProxyResult<ZodFlow> {
  return createTidasProxy(FlowSchema, options);
}

/**
 * Create a Process proxy with type-safe property access
 */
export function createZodProcess(
  options: TidasProxyOptions = {}
): TidasProxyResult<ZodProcess> {
  return createTidasProxy(ProcessSchema, options);
}


/**
 * Utility function to create a proxy from any schema
 */
export function createZodTidasProxy<T extends z.ZodSchema>(
  schema: T,
  options: TidasProxyOptions = {}
): TidasProxyResult<z.infer<T>> {
  return createTidasProxy(schema, options);
}

// Export schemas for external use
export { ContactSchema, FlowSchema, ProcessSchema };
