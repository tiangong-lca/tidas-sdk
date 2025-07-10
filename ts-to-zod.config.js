/**
 * ts-to-zod configuration - Auto-generated with dependency analysis
 * Processing order determined by import dependencies
 * @type {import("ts-to-zod").TsToZodConfig}
 */
module.exports = [
  {
    name: "data_types",
    input: "src/types/tidas_data_types.ts",
    output: "src/schemas/tidas_data_types.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "contacts",
    input: "src/types/tidas_contacts.ts",
    output: "src/schemas/tidas_contacts.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "contacts_category",
    input: "src/types/tidas_contacts_category.ts",
    output: "src/schemas/tidas_contacts_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "flowproperties",
    input: "src/types/tidas_flowproperties.ts",
    output: "src/schemas/tidas_flowproperties.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "flowproperties_category",
    input: "src/types/tidas_flowproperties_category.ts",
    output: "src/schemas/tidas_flowproperties_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "locations_category",
    input: "src/types/tidas_locations_category.ts",
    output: "src/schemas/tidas_locations_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "flows",
    input: "src/types/tidas_flows.ts",
    output: "src/schemas/tidas_flows.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "flows_elementary_category",
    input: "src/types/tidas_flows_elementary_category.ts",
    output: "src/schemas/tidas_flows_elementary_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "flows_product_category",
    input: "src/types/tidas_flows_product_category.ts",
    output: "src/schemas/tidas_flows_product_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "lciamethods",
    input: "src/types/tidas_lciamethods.ts",
    output: "src/schemas/tidas_lciamethods.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "lciamethods_category",
    input: "src/types/tidas_lciamethods_category.ts",
    output: "src/schemas/tidas_lciamethods_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "lifecyclemodels",
    input: "src/types/tidas_lifecyclemodels.ts",
    output: "src/schemas/tidas_lifecyclemodels.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "processes",
    input: "src/types/tidas_processes.ts",
    output: "src/schemas/tidas_processes.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "processes_category",
    input: "src/types/tidas_processes_category.ts",
    output: "src/schemas/tidas_processes_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "sources",
    input: "src/types/tidas_sources.ts",
    output: "src/schemas/tidas_sources.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "sources_category",
    input: "src/types/tidas_sources_category.ts",
    output: "src/schemas/tidas_sources_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "unitgroups",
    input: "src/types/tidas_unitgroups.ts",
    output: "src/schemas/tidas_unitgroups.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  },
  {
    name: "unitgroups_category",
    input: "src/types/tidas_unitgroups_category.ts",
    output: "src/schemas/tidas_unitgroups_category.schema.ts",
    getSchemaName: (id) => `${id}Schema`,
    skipValidation: true
  }
];