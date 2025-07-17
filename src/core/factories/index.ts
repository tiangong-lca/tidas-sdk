import { TidasContact } from '../entities/TidasContact';
import { TidasFlow } from '../entities/TidasFlow';
import { TidasProcess } from '../entities/TidasProcess';
import { TidasSource } from '../entities/TidasSource';
import { TidasFlowProperty } from '../entities/TidasFlowProperty';
import { TidasUnitGroup } from '../entities/TidasUnitGroup';
import { TidasLCIAMethod } from '../entities/TidasLCIAMethod';
import { TidasLifeCycleModel } from '../entities/TidasLifeCycleModel';
import {
  Contact,
  Flow,
  Process,
  Source,
  FlowProperty,
  UnitGroup,
  LCIAMethod,
  LifeCycleModel,
} from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';
import {
  MultiLangArray,
  MultiLangItemClass,
} from '../../types/multi-lang-types';

/**
 * Factory functions for creating TIDAS entities
 */

function deepWrapMultiLang(obj: any, seen = new WeakSet()): any {
  if (!obj || typeof obj !== 'object') return obj;
  if (obj instanceof MultiLangArray || obj instanceof MultiLangItemClass)
    return obj;
  if (seen.has(obj)) return obj;
  seen.add(obj);

  for (const key of Object.keys(obj)) {
    const val = obj[key];
    if (
      Array.isArray(val) &&
      val.length > 0 &&
      typeof val[0] === 'object' &&
      '@xml:lang' in val[0] &&
      '#text' in val[0]
    ) {
      const arr = new MultiLangArray();
      for (const item of val) {
        arr.push(
          item instanceof MultiLangItemClass
            ? item
            : new MultiLangItemClass(item['@xml:lang'], item['#text'])
        );
      }
      obj[key] = arr;
    } else if (
      val &&
      typeof val === 'object' &&
      '@xml:lang' in val &&
      '#text' in val
    ) {
      obj[key] = new MultiLangItemClass(val['@xml:lang'], val['#text']);
    } else if (typeof val === 'object' && val !== null) {
      deepWrapMultiLang(val, seen);
    }
  }
  return obj;
}

// Contact factory functions
export function createContact(
  data?: Partial<Contact>,
  validationConfig?: Partial<ValidationConfig>
): TidasContact {
  const contact = new TidasContact(data, validationConfig);
  return deepWrapMultiLang(contact);
}

export function createContactFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasContact {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const contact = createContact(data, validationConfig);
  return deepWrapMultiLang(contact);
}

export function createContactsBatch(
  dataArray: Array<Partial<Contact>>,
  validationConfig?: Partial<ValidationConfig>
): TidasContact[] {
  return dataArray.map((data) => createContact(data, validationConfig));
}

// Flow factory functions
export function createFlow(
  data?: Partial<Flow>,
  validationConfig?: Partial<ValidationConfig>
): TidasFlow {
  const flow = new TidasFlow(data, validationConfig);
  return deepWrapMultiLang(flow);
}

export function createFlowFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasFlow {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const flow = createFlow(data, validationConfig);
  return deepWrapMultiLang(flow);
}

export function createFlowsBatch(
  dataArray: Array<Partial<Flow>>,
  validationConfig?: Partial<ValidationConfig>
): TidasFlow[] {
  return dataArray.map((data) => createFlow(data, validationConfig));
}

// Process factory functions
export function createProcess(
  data?: Partial<Process>,
  validationConfig?: Partial<ValidationConfig>
): TidasProcess {
  const process = new TidasProcess(data, validationConfig);
  return deepWrapMultiLang(process);
}

export function createProcessFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasProcess {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const process = createProcess(data, validationConfig);
  return deepWrapMultiLang(process);
}

export function createProcessesBatch(
  dataArray: Array<Partial<Process>>,
  validationConfig?: Partial<ValidationConfig>
): TidasProcess[] {
  return dataArray.map((data) => createProcess(data, validationConfig));
}

// Source factory functions
export function createSource(
  data?: Partial<Source>,
  validationConfig?: Partial<ValidationConfig>
): TidasSource {
  const source = new TidasSource(data, validationConfig);
  return deepWrapMultiLang(source);
}

export function createSourceFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasSource {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const source = createSource(data, validationConfig);
  return deepWrapMultiLang(source);
}

export function createSourcesBatch(
  dataArray: Array<Partial<Source>>,
  validationConfig?: Partial<ValidationConfig>
): TidasSource[] {
  return dataArray.map((data) => createSource(data, validationConfig));
}

// FlowProperty factory functions
export function createFlowProperty(
  data?: Partial<FlowProperty>,
  validationConfig?: Partial<ValidationConfig>
): TidasFlowProperty {
  const flowProperty = new TidasFlowProperty(data, validationConfig);
  return deepWrapMultiLang(flowProperty);
}

export function createFlowPropertyFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasFlowProperty {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const flowProperty = createFlowProperty(data, validationConfig);
  return deepWrapMultiLang(flowProperty);
}

export function createFlowPropertiesBatch(
  dataArray: Array<Partial<FlowProperty>>,
  validationConfig?: Partial<ValidationConfig>
): TidasFlowProperty[] {
  return dataArray.map((data) => createFlowProperty(data, validationConfig));
}

// UnitGroup factory functions
export function createUnitGroup(
  data?: Partial<UnitGroup>,
  validationConfig?: Partial<ValidationConfig>
): TidasUnitGroup {
  const unitGroup = new TidasUnitGroup(data, validationConfig);
  return deepWrapMultiLang(unitGroup);
}

export function createUnitGroupFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasUnitGroup {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const unitGroup = createUnitGroup(data, validationConfig);
  return deepWrapMultiLang(unitGroup);
}

export function createUnitGroupsBatch(
  dataArray: Array<Partial<UnitGroup>>,
  validationConfig?: Partial<ValidationConfig>
): TidasUnitGroup[] {
  return dataArray.map((data) => createUnitGroup(data, validationConfig));
}

// LCIAMethod factory functions
export function createLCIAMethod(
  data?: Partial<LCIAMethod>,
  validationConfig?: Partial<ValidationConfig>
): TidasLCIAMethod {
  const lciaMethod = new TidasLCIAMethod(data, validationConfig);
  return deepWrapMultiLang(lciaMethod);
}

export function createLCIAMethodFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasLCIAMethod {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const lciaMethod = createLCIAMethod(data, validationConfig);
  return deepWrapMultiLang(lciaMethod);
}

export function createLCIAMethodsBatch(
  dataArray: Array<Partial<LCIAMethod>>,
  validationConfig?: Partial<ValidationConfig>
): TidasLCIAMethod[] {
  return dataArray.map((data) => createLCIAMethod(data, validationConfig));
}

// LifeCycleModel factory functions
export function createLifeCycleModel(
  data?: Partial<LifeCycleModel>,
  validationConfig?: Partial<ValidationConfig>
): TidasLifeCycleModel {
  const lifeCycleModel = new TidasLifeCycleModel(data, validationConfig);
  return deepWrapMultiLang(lifeCycleModel);
}

export function createLifeCycleModelFromJSON(
  jsonData: string | object,
  validationConfig?: Partial<ValidationConfig>
): TidasLifeCycleModel {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  const lifeCycleModel = createLifeCycleModel(data, validationConfig);
  return deepWrapMultiLang(lifeCycleModel);
}

export function createLifeCycleModelsBatch(
  dataArray: Array<Partial<LifeCycleModel>>,
  validationConfig?: Partial<ValidationConfig>
): TidasLifeCycleModel[] {
  return dataArray.map((data) => createLifeCycleModel(data, validationConfig));
}

// Generic factory function
export function createTidasEntity<T>(
  entityType:
    | 'contact'
    | 'flow'
    | 'process'
    | 'source'
    | 'flowProperty'
    | 'unitGroup'
    | 'lciaMethod'
    | 'lifeCycleModel',
  data?: Partial<T>,
  validationConfig?: Partial<ValidationConfig>
):
  | TidasContact
  | TidasFlow
  | TidasProcess
  | TidasSource
  | TidasFlowProperty
  | TidasUnitGroup
  | TidasLCIAMethod
  | TidasLifeCycleModel {
  switch (entityType) {
    case 'contact':
      return createContact(data as Partial<Contact>, validationConfig);
    case 'flow':
      return createFlow(data as Partial<Flow>, validationConfig);
    case 'process':
      return createProcess(data as Partial<Process>, validationConfig);
    case 'source':
      return createSource(data as Partial<Source>, validationConfig);
    case 'flowProperty':
      return createFlowProperty(
        data as Partial<FlowProperty>,
        validationConfig
      );
    case 'unitGroup':
      return createUnitGroup(data as Partial<UnitGroup>, validationConfig);
    case 'lciaMethod':
      return createLCIAMethod(data as Partial<LCIAMethod>, validationConfig);
    case 'lifeCycleModel':
      return createLifeCycleModel(
        data as Partial<LifeCycleModel>,
        validationConfig
      );
    default:
      throw new Error(`Unknown entity type: ${entityType}`);
  }
}

// Export entity classes
export { TidasContact } from '../entities/TidasContact';
export { TidasFlow } from '../entities/TidasFlow';
export { TidasProcess } from '../entities/TidasProcess';
export { TidasSource } from '../entities/TidasSource';
export { TidasFlowProperty } from '../entities/TidasFlowProperty';
export { TidasUnitGroup } from '../entities/TidasUnitGroup';
export { TidasLCIAMethod } from '../entities/TidasLCIAMethod';
export { TidasLifeCycleModel } from '../entities/TidasLifeCycleModel';

// Export base classes
export { TidasEntity } from '../base/TidasEntity';
export type { ValidationResult } from '../base/TidasEntity';
