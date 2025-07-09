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
export { Flows as FlowDataSet } from './tidas_flows';
export { Lifecyclemodels as LifeCycleModelDataSet } from './tidas_lifecyclemodels';
export { Processes as ProcessDataSet } from './tidas_processes';

// Import types for union type
import type { Flows } from './tidas_flows';
import type { Lifecyclemodels } from './tidas_lifecyclemodels';
import type { Processes } from './tidas_processes';

// Union type for all data sets
export type DataSet = 
  | Flows
  | Lifecyclemodels
  | Processes;
