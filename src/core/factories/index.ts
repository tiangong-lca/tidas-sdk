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

/**
 * Factory functions for creating TIDAS entities
 */

// Contact factory functions
export function createContact(data?: Partial<Contact>): TidasContact {
  return new TidasContact(data);
}

export function createContactFromJSON(jsonData: string | object): TidasContact {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createContact(data);
}

export function createContactsBatch(dataArray: Array<Partial<Contact>>): TidasContact[] {
  return dataArray.map(data => createContact(data));
}

// Flow factory functions
export function createFlow(data?: Partial<Flow>): TidasFlow {
  return new TidasFlow(data);
}

export function createFlowFromJSON(jsonData: string | object): TidasFlow {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createFlow(data);
}

export function createFlowsBatch(dataArray: Array<Partial<Flow>>): TidasFlow[] {
  return dataArray.map(data => createFlow(data));
}

// Process factory functions
export function createProcess(data?: Partial<Process>): TidasProcess {
  return new TidasProcess(data);
}

export function createProcessFromJSON(jsonData: string | object): TidasProcess {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createProcess(data);
}

export function createProcessesBatch(dataArray: Array<Partial<Process>>): TidasProcess[] {
  return dataArray.map(data => createProcess(data));
}

// Source factory functions
export function createSource(data?: Partial<Source>): TidasSource {
  return new TidasSource(data);
}

export function createSourceFromJSON(jsonData: string | object): TidasSource {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createSource(data);
}

export function createSourcesBatch(dataArray: Array<Partial<Source>>): TidasSource[] {
  return dataArray.map(data => createSource(data));
}

// FlowProperty factory functions
export function createFlowProperty(data?: Partial<FlowProperty>): TidasFlowProperty {
  return new TidasFlowProperty(data);
}

export function createFlowPropertyFromJSON(jsonData: string | object): TidasFlowProperty {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createFlowProperty(data);
}

export function createFlowPropertiesBatch(dataArray: Array<Partial<FlowProperty>>): TidasFlowProperty[] {
  return dataArray.map(data => createFlowProperty(data));
}

// UnitGroup factory functions
export function createUnitGroup(data?: Partial<UnitGroup>): TidasUnitGroup {
  return new TidasUnitGroup(data);
}

export function createUnitGroupFromJSON(jsonData: string | object): TidasUnitGroup {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createUnitGroup(data);
}

export function createUnitGroupsBatch(dataArray: Array<Partial<UnitGroup>>): TidasUnitGroup[] {
  return dataArray.map(data => createUnitGroup(data));
}

// LCIAMethod factory functions
export function createLCIAMethod(data?: Partial<LCIAMethod>): TidasLCIAMethod {
  return new TidasLCIAMethod(data);
}

export function createLCIAMethodFromJSON(jsonData: string | object): TidasLCIAMethod {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createLCIAMethod(data);
}

export function createLCIAMethodsBatch(dataArray: Array<Partial<LCIAMethod>>): TidasLCIAMethod[] {
  return dataArray.map(data => createLCIAMethod(data));
}

// LifeCycleModel factory functions
export function createLifeCycleModel(data?: Partial<LifeCycleModel>): TidasLifeCycleModel {
  return new TidasLifeCycleModel(data);
}

export function createLifeCycleModelFromJSON(jsonData: string | object): TidasLifeCycleModel {
  const data = typeof jsonData === 'string' ? JSON.parse(jsonData) : jsonData;
  return createLifeCycleModel(data);
}

export function createLifeCycleModelsBatch(dataArray: Array<Partial<LifeCycleModel>>): TidasLifeCycleModel[] {
  return dataArray.map(data => createLifeCycleModel(data));
}

// Generic factory function
export function createTidasEntity<T>(
  entityType: 'contact' | 'flow' | 'process' | 'source' | 'flowProperty' | 'unitGroup' | 'lciaMethod' | 'lifeCycleModel',
  data?: Partial<T>
): TidasContact | TidasFlow | TidasProcess | TidasSource | TidasFlowProperty | TidasUnitGroup | TidasLCIAMethod | TidasLifeCycleModel {
  switch (entityType) {
    case 'contact':
      return createContact(data as Partial<Contact>);
    case 'flow':
      return createFlow(data as Partial<Flow>);
    case 'process':
      return createProcess(data as Partial<Process>);
    case 'source':
      return createSource(data as Partial<Source>);
    case 'flowProperty':
      return createFlowProperty(data as Partial<FlowProperty>);
    case 'unitGroup':
      return createUnitGroup(data as Partial<UnitGroup>);
    case 'lciaMethod':
      return createLCIAMethod(data as Partial<LCIAMethod>);
    case 'lifeCycleModel':
      return createLifeCycleModel(data as Partial<LifeCycleModel>);
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