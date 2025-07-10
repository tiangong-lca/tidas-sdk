/**
 * Automatically generated index file for all Tidas types
 */


// Re-export commonly used types with simpler names
export { Contacts as Contact } from './tidas_contacts';
export { Flows as Flow } from './tidas_flows';
export { Processes as Process } from './tidas_processes';
export { Sources as Source } from './tidas_sources';
export { Flowproperties as FlowProperty } from './tidas_flowproperties';
export { Unitgroups as UnitGroup } from './tidas_unitgroups';
export { Lciamethods as LCIAMethod } from './tidas_lciamethods';
export { Lifecyclemodels as LifeCycleModel } from './tidas_lifecyclemodels';

// Import types for union type
import type { Contacts as Contact } from './tidas_contacts';
import type { Flows as Flow } from './tidas_flows';
import type { Processes as Process } from './tidas_processes';
import type { Sources as Source } from './tidas_sources';
import type { Flowproperties as FlowProperty } from './tidas_flowproperties';
import type { Unitgroups as UnitGroup } from './tidas_unitgroups';
import type { Lciamethods as LCIAMethod } from './tidas_lciamethods';
import type { Lifecyclemodels as LifeCycleModel } from './tidas_lifecyclemodels';

// Union type for all data sets
export type DataSet = 
  | Contact
  | Flow
  | Process
  | Source
  | FlowProperty
  | UnitGroup
  | LCIAMethod
  | LifeCycleModel;
