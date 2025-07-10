/**
 * Automatically generated index file for all Tidas types
 */

export * from './tidas_contacts';
export * from './tidas_contacts_category';
export * from './tidas_data_types';
export * from './tidas_flowproperties';
export * from './tidas_flowproperties_category';
export * from './tidas_flows';
export * from './tidas_flows_elementary_category';
export * from './tidas_flows_product_category';
export * from './tidas_lciamethods';
export * from './tidas_lciamethods_category';
export * from './tidas_lifecyclemodels';
export * from './tidas_locations_category';
export * from './tidas_processes';
export * from './tidas_processes_category';
export * from './tidas_sources';
export * from './tidas_sources_category';
export * from './tidas_unitgroups';
export * from './tidas_unitgroups_category';

// Re-export commonly used types with simpler names
export { Contacts as Contact } from './tidas_contacts';
export { Flows as Flow } from './tidas_flows';
export { Processes as Process } from './tidas_processes';
export { Sources as Source } from './tidas_sources';
export { Flowproperties as FlowProperty } from './tidas_flowproperties';
export { Unitgroups as UnitGroup } from './tidas_unitgroups';
export { Lciamethods as LCIAMethod } from './tidas_lciamethods';
export { Lifecyclemodels as LifeCycleModel } from './tidas_lifecyclemodels';

// Legacy aliases for backward compatibility
export { Flows as FlowDataSet } from './tidas_flows';
export { Lifecyclemodels as LifeCycleModelDataSet } from './tidas_lifecyclemodels';
export { Processes as ProcessDataSet } from './tidas_processes';

// Import types for union type
import type { Contacts } from './tidas_contacts';
import type { Flows } from './tidas_flows';
import type { Processes } from './tidas_processes';
import type { Sources } from './tidas_sources';
import type { Flowproperties } from './tidas_flowproperties';
import type { Unitgroups } from './tidas_unitgroups';
import type { Lciamethods } from './tidas_lciamethods';
import type { Lifecyclemodels } from './tidas_lifecyclemodels';

// Union type for all data sets
export type DataSet = 
  | Contacts
  | Flows
  | Processes
  | Sources
  | Flowproperties
  | Unitgroups
  | Lciamethods
  | Lifecyclemodels;
