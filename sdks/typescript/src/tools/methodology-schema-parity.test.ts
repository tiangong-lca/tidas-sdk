import bundledMethodologies from '../data/bundled-methodologies.json';
import {
  compareMethodologyWithSchema,
  validateBundledMethodologies,
} from './methodology-schema-parity';

describe('methodology-schema parity tools', () => {
  it('mirrors the Python methodology/schema comparison rules on synthetic input', () => {
    const methodology = {
      metadata: {
        ignored: true,
      },
      global_rules: {
        ignored: true,
      },
      processDataSet: {
        '<rules>': {
          ignored: true,
        },
        processInformation: {
          dataSetInformation: {
            uuid: {},
            customOnly: {},
          },
        },
        exchanges: {
          exchange: {
            meanAmount: {},
          },
        },
      },
    };

    const schema = {
      type: 'object',
      properties: {
        processDataSet: {
          type: 'object',
          properties: {
            processInformation: {
              type: 'object',
              properties: {
                dataSetInformation: {
                  type: 'object',
                  properties: {
                    'common:UUID': {
                      type: 'string',
                    },
                  },
                },
              },
            },
            exchanges: {
              type: 'object',
              properties: {
                exchange: {
                  type: 'array',
                  items: {
                    type: 'object',
                    properties: {
                      meanAmount: {
                        type: 'number',
                      },
                    },
                  },
                },
              },
            },
            missingTop: {
              type: 'string',
            },
          },
        },
      },
    };

    const result = compareMethodologyWithSchema(methodology, schema);

    expect(result.errors).toEqual([]);
    expect(result.warnings).toEqual(
      expect.arrayContaining([
        "Field 'processDataSet.processInformation.dataSetInformation.customOnly' in YAML methodology not found in schema",
        "Schema field 'processDataSet.missingTop' not covered in YAML methodology",
      ])
    );
    expect(result.warnings).toHaveLength(2);
  });

  it('validates the bundled methodologies against bundled runtime schemas', () => {
    const report = validateBundledMethodologies();
    const methodologyKeys = Object.keys(bundledMethodologies.methodologies ?? {}).sort();

    expect(report.ok).toBe(true);
    expect(report.summary.file_count).toBe(methodologyKeys.length);
    expect(report.summary.error_count).toBe(0);
    expect(report.files.map((file) => file.methodology_key)).toEqual(methodologyKeys);
    expect(report.files).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          methodology_key: methodologyKeys[0],
          methodology_file: expect.stringMatching(/^tidas_.+\.yaml$/),
          schema_file: expect.stringMatching(/^tidas_.+\.json$/),
          status: expect.stringMatching(/^(ok|warning)$/),
          errors: [],
          warnings: expect.any(Array),
        }),
      ])
    );
  });
});
