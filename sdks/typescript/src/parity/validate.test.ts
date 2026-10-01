import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { describe, it } from 'node:test';
import { categoryValidate, validatePackageDir } from './validate';

function packageRoot() {
  return path.resolve(__dirname, '../..');
}

function repoRoot() {
  return path.resolve(packageRoot(), '../..');
}

function testDataPath(fileName: string) {
  return path.join(repoRoot(), 'test-data', fileName);
}

function makeTempDir(prefix: string) {
  return fs.mkdtempSync(path.join(os.tmpdir(), prefix));
}

function makeFlowPackageFromExample() {
  const dir = makeTempDir('tidas-sdk-validate-example-');
  fs.mkdirSync(path.join(dir, 'flows'), { recursive: true });
  fs.copyFileSync(
    testDataPath('tidas-example-flow.json'),
    path.join(dir, 'flows/example.json')
  );
  return dir;
}

function makeCustomInvalidFlowPackage() {
  const dir = makeTempDir('tidas-sdk-validate-custom-');
  fs.mkdirSync(path.join(dir, 'flows'), { recursive: true });
  fs.writeFileSync(
    path.join(dir, 'flows/bad.json'),
    JSON.stringify(
      {
        flowDataSet: {
          '@xmlns': 'http://lca.jrc.it/ILCD/Flow',
          '@xmlns:common': 'http://lca.jrc.it/ILCD/Common',
          '@xmlns:ecn':
            'http://eplca.jrc.ec.europa.eu/ILCD/Extensions/2018/ECNumber',
          '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
          '@version': '1.1',
          '@locations': '../ILCDLocations.xml',
          '@xsi:schemaLocation':
            'http://lca.jrc.it/ILCD/Flow ../../schemas/ILCD_FlowDataSet.xsd',
          flowInformation: {
            dataSetInformation: {
              'common:UUID': '12345678-1234-1234-1234-123456789abc',
              name: {
                baseName: [
                  {
                    '@xml:lang': 'en',
                    '#text': 'English 中文',
                  },
                  {
                    '@xml:lang': 'en-US',
                    '#text': 'Regional English',
                  },
                ],
                treatmentStandardsRoutes: [
                  {
                    '@xml:lang': 'en',
                    '#text': 'route',
                  },
                ],
                mixAndLocationTypes: [
                  {
                    '@xml:lang': 'en',
                    '#text': 'mix',
                  },
                ],
              },
              classificationInformation: {
                'common:classification': {
                  'common:class': [
                    {
                      '@level': '0',
                      '@classId': '1',
                      '#text': 'Top',
                    },
                    {
                      '@level': '1',
                      '@classId': '99',
                      '#text': 'Bad child',
                    },
                  ],
                },
              },
            },
            quantitativeReference: {
              referenceToReferenceFlowProperty: '1',
            },
          },
          modellingAndValidation: {
            LCIMethod: {
              typeOfDataSet: 'Product flow',
            },
            complianceDeclarations: {
              compliance: {
                'common:referenceToComplianceSystem': {
                  '@type': 'source data set',
                  '@refObjectId': '12345678-1234-1234-1234-123456789abc',
                  '@version': '00.00.000',
                  '@uri': '',
                  'common:shortDescription': [
                    {
                      '@xml:lang': 'en',
                      '#text': 'desc',
                    },
                  ],
                },
                'common:approvalOfOverallCompliance': 'Fully compliant',
              },
            },
          },
          administrativeInformation: {
            dataEntryBy: {
              'common:timeStamp': '2024-01-01T00:00:00Z',
              'common:referenceToDataSetFormat': {
                '@type': 'source data set',
                '@refObjectId': '12345678-1234-1234-1234-123456789abc',
                '@version': '00.00.000',
                '@uri': '',
                'common:shortDescription': [
                  {
                    '@xml:lang': 'en',
                    '#text': 'desc',
                  },
                ],
              },
            },
            publicationAndOwnership: {
              'common:dataSetVersion': '1.0.0',
              'common:referenceToOwnershipOfDataSet': {
                '@type': 'source data set',
                '@refObjectId': '12345678-1234-1234-1234-123456789abc',
                '@version': '00.00.000',
                '@uri': '',
                'common:shortDescription': [
                  {
                    '@xml:lang': 'en',
                    '#text': 'desc',
                  },
                ],
              },
            },
          },
          flowProperties: {
            flowProperty: [],
          },
        },
      },
      null,
      2
    ),
    'utf8'
  );
  return dir;
}

function makeInvalidSourcesCategory() {
  const dir = makeTempDir('tidas-sdk-validate-sources-');
  fs.mkdirSync(path.join(dir, 'sources'), { recursive: true });
  fs.writeFileSync(path.join(dir, 'sources/bad.json'), '{}', 'utf8');
  return dir;
}

function makeInvalidCASNumberFlowPackage() {
  const dir = makeTempDir('tidas-sdk-validate-cas-');
  fs.mkdirSync(path.join(dir, 'flows'), { recursive: true });
  const payload = JSON.parse(
    fs.readFileSync(testDataPath('tidas-example-flow.json'), 'utf8')
  );

  payload.flowDataSet.flowInformation.dataSetInformation.CASNumber = '64-17-6';
  fs.writeFileSync(
    path.join(dir, 'flows/bad-cas.json'),
    JSON.stringify(payload, null, 2),
    'utf8'
  );
  return dir;
}

describe('package validation parity', () => {
  it('uses runtime JSON schemas for the example flow package', () => {
    const inputDir = makeFlowPackageFromExample();
    const report = validatePackageDir(inputDir);
    const locations = report.issues.map((issue) => issue.location);

    assert.strictEqual(report.ok, false);
    assert.strictEqual(report.summary.category_count, 1);
    assert.strictEqual(report.summary.issue_count, 6);
    assert.strictEqual(report.summary.error_count, 6);
    assert.strictEqual(report.categories.length, 1);
    assert.strictEqual(report.categories[0]?.category, 'flows');
    assert.strictEqual(report.categories[0]?.summary.issue_count, 6);
    assert.deepStrictEqual(
      new Set(report.issues.map((issue) => issue.issue_code)),
      new Set(['schema_error'])
    );
    for (const expectedLocation of [
      'flowDataSet',
      'flowDataSet/administrativeInformation/publicationAndOwnership',
      'flowDataSet/flowInformation/dataSetInformation/classificationInformation/common:elementaryFlowCategorization',
    ]) {
      assert.ok(locations.includes(expectedLocation), JSON.stringify(locations));
    }
    assert.ok(
      !locations.includes('flowDataSet/flowInformation/dataSetInformation/name')
    );
    assert.ok(
      !locations.includes(
        'flowDataSet/flowInformation/dataSetInformation/common:other'
      )
    );
    assert.ok(
      !locations.includes(
        'flowDataSet/administrativeInformation/dataEntryBy/common:timeStamp'
      )
    );
  });

  it('reports root-level required-property errors from JSON Schema', () => {
    const inputDir = makeInvalidSourcesCategory();
    const report = validatePackageDir(inputDir);

    assert.strictEqual(report.ok, false);
    assert.strictEqual(report.summary.issue_count, 1);
    const requiredIssue = report.issues.find(
      (issue) =>
        issue.issue_code === 'schema_error' &&
        issue.category === 'sources' &&
        issue.location === '<root>'
    );
    assert.ok(requiredIssue);
    assert.strictEqual(requiredIssue.context.validator, 'required');
    assert.strictEqual(requiredIssue.context.argument, 'sourceDataSet');
    assert.ok(requiredIssue.message.includes('sourceDataSet'));
  });

  it('enforces CAS number check digits through runtime JSON Schema formats', () => {
    const inputDir = makeInvalidCASNumberFlowPackage();
    const report = validatePackageDir(inputDir);

    assert.strictEqual(report.ok, false);
    const casIssue = report.issues.find(
      (issue) =>
        issue.issue_code === 'schema_error' &&
        issue.location ===
          'flowDataSet/flowInformation/dataSetInformation/CASNumber'
    );
    assert.ok(casIssue);
    assert.strictEqual(casIssue.context.validator, 'format');
    assert.strictEqual(casIssue.context.argument, 'cas-number');
  });

  it('avoids cascading classification issues when the schema structure is missing', () => {
    const inputDir = makeInvalidSourcesCategory();
    const report = categoryValidate(
      path.join(inputDir, 'sources'),
      'sources',
      false
    );

    assert.strictEqual(report.summary.issue_count, 1);
    assert.deepStrictEqual(
      report.issues.map((issue) => issue.issue_code),
      ['schema_error']
    );
  });

  it('adds localized text and classification hierarchy issues on top of schema issues', () => {
    const inputDir = makeCustomInvalidFlowPackage();
    const report = validatePackageDir(inputDir);
    const issueCodes = report.issues.map((issue) => issue.issue_code);
    const schemaLocations = report.issues
      .filter((issue) => issue.issue_code === 'schema_error')
      .map((issue) => issue.location);

    assert.ok(report.summary.issue_count > 3);
    assert.ok(
      report.issues.filter((issue) => issue.issue_code === 'schema_error')
        .length > 0
    );
    assert.strictEqual(
      report.issues.filter(
        (issue) => issue.issue_code === 'localized_text_language_error'
      ).length,
      1
    );
    assert.strictEqual(
      report.issues.filter(
        (issue) =>
          issue.issue_code === 'localized_text_language_not_in_tidas_enum'
      ).length,
      1
    );
    assert.ok(
      report.issues.filter(
        (issue) => issue.issue_code === 'classification_hierarchy_error'
      ).length > 0
    );
    for (const expectedCode of [
      'schema_error',
      'localized_text_language_error',
      'localized_text_language_not_in_tidas_enum',
      'classification_hierarchy_error',
    ]) {
      assert.ok(issueCodes.includes(expectedCode));
    }
    // common:classification is now anyOf(strict single-system object | named
    // multi-system array). An invalid classification that matches neither branch
    // surfaces a single schema_error at the common:classification node (anyOf
    // failures don't report per-item); classification ordering is still checked
    // by the hierarchy gate below.
    for (const expectedLocation of [
      'flowDataSet/flowInformation/dataSetInformation/name/baseName',
      'flowDataSet/flowInformation/dataSetInformation/classificationInformation/common:classification',
    ]) {
      assert.ok(schemaLocations.includes(expectedLocation));
    }
    for (const [issueCode, location] of [
      [
        'localized_text_language_error',
        'flowDataSet/flowInformation/dataSetInformation/name/baseName/0',
      ],
      [
        'localized_text_language_not_in_tidas_enum',
        'flowDataSet/flowInformation/dataSetInformation/name/baseName/1',
      ],
      ['classification_hierarchy_error', '<root>'],
    ] as const) {
      assert.ok(
        report.issues.some(
          (issue) =>
            issue.issue_code === issueCode && issue.location === location
        )
      );
    }
  });
});
