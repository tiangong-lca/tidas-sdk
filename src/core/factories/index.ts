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
  LifeCycleModel 
} from '../../types';
import { ValidationConfig } from '../config/ValidationConfig';

/**
 * Factory functions for creating TIDAS entities
 */

// Contact factory functions
export function createContact(data?: Partial<Contact>, validationConfig?: Partial<ValidationConfig>): TidasContact {
  return new TidasContact(data, validationConfig);
}

export function createContactFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasContact {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createContact(data, validationConfig);
}

export function createContactsBatch(dataArray: Array<Partial<Contact>>, validationConfig?: Partial<ValidationConfig>): TidasContact[] {
  return dataArray.map(data => createContact(data, validationConfig));
}

// Flow factory functions
export function createFlow(data?: Partial<Flow>, validationConfig?: Partial<ValidationConfig>): TidasFlow {
  return new TidasFlow(data, validationConfig);
}

export function createFlowFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasFlow {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createFlow(data, validationConfig);
}

export function createFlowsBatch(dataArray: Array<Partial<Flow>>, validationConfig?: Partial<ValidationConfig>): TidasFlow[] {
  return dataArray.map(data => createFlow(data, validationConfig));
}

// Process factory functions
export function createProcess(data?: Partial<Process>, validationConfig?: Partial<ValidationConfig>): TidasProcess {
  return new TidasProcess(data, validationConfig);
}

export function createProcessFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasProcess {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createProcess(data, validationConfig);
}

export function createProcessesBatch(dataArray: Array<Partial<Process>>, validationConfig?: Partial<ValidationConfig>): TidasProcess[] {
  return dataArray.map(data => createProcess(data, validationConfig));
}

// Source factory functions
export function createSource(data?: Partial<Source>, validationConfig?: Partial<ValidationConfig>): TidasSource {
  return new TidasSource(data, validationConfig);
}

export function createSourceFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasSource {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createSource(data, validationConfig);
}

export function createSourcesBatch(dataArray: Array<Partial<Source>>, validationConfig?: Partial<ValidationConfig>): TidasSource[] {
  return dataArray.map(data => createSource(data, validationConfig));
}

// FlowProperty factory functions
export function createFlowProperty(data?: Partial<FlowProperty>, validationConfig?: Partial<ValidationConfig>): TidasFlowProperty {
  return new TidasFlowProperty(data, validationConfig);
}

export function createFlowPropertyFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasFlowProperty {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createFlowProperty(data, validationConfig);
}

export function createFlowPropertiesBatch(dataArray: Array<Partial<FlowProperty>>, validationConfig?: Partial<ValidationConfig>): TidasFlowProperty[] {
  return dataArray.map(data => createFlowProperty(data, validationConfig));
}

// UnitGroup factory functions
export function createUnitGroup(data?: Partial<UnitGroup>, validationConfig?: Partial<ValidationConfig>): TidasUnitGroup {
  return new TidasUnitGroup(data, validationConfig);
}

export function createUnitGroupFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasUnitGroup {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createUnitGroup(data, validationConfig);
}

export function createUnitGroupsBatch(dataArray: Array<Partial<UnitGroup>>, validationConfig?: Partial<ValidationConfig>): TidasUnitGroup[] {
  return dataArray.map(data => createUnitGroup(data, validationConfig));
}

// LCIAMethod factory functions
export function createLCIAMethod(data?: Partial<LCIAMethod>, validationConfig?: Partial<ValidationConfig>): TidasLCIAMethod {
  return new TidasLCIAMethod(data, validationConfig);
}

export function createLCIAMethodFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasLCIAMethod {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createLCIAMethod(data, validationConfig);
}

export function createLCIAMethodsBatch(dataArray: Array<Partial<LCIAMethod>>, validationConfig?: Partial<ValidationConfig>): TidasLCIAMethod[] {
  return dataArray.map(data => createLCIAMethod(data, validationConfig));
}

// LifeCycleModel factory functions
export function createLifeCycleModel(data?: Partial<LifeCycleModel>, validationConfig?: Partial<ValidationConfig>): TidasLifeCycleModel {
  return new TidasLifeCycleModel(data, validationConfig);
}

export function createLifeCycleModelFromJSON(jsonData: string | object, validationConfig?: Partial<ValidationConfig>): TidasLifeCycleModel {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createLifeCycleModel(data, validationConfig);
}

export function createLifeCycleModelsBatch(dataArray: Array<Partial<LifeCycleModel>>, validationConfig?: Partial<ValidationConfig>): TidasLifeCycleModel[] {
  return dataArray.map(data => createLifeCycleModel(data, validationConfig));
}

// Generic factory function
export function createTidasEntity<T>(
  entityType: 'contact' | 'flow' | 'process' | 'source' | 'flowProperty' | 'unitGroup' | 'lciaMethod' | 'lifeCycleModel',
  data?: Partial<T>,
  validationConfig?: Partial<ValidationConfig>
): TidasContact | TidasFlow | TidasProcess | TidasSource | TidasFlowProperty | TidasUnitGroup | TidasLCIAMethod | TidasLifeCycleModel {
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
      return createFlowProperty(data as Partial<FlowProperty>, validationConfig);
    case 'unitGroup':
      return createUnitGroup(data as Partial<UnitGroup>, validationConfig);
    case 'lciaMethod':
      return createLCIAMethod(data as Partial<LCIAMethod>, validationConfig);
    case 'lifeCycleModel':
      return createLifeCycleModel(data as Partial<LifeCycleModel>, validationConfig);
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