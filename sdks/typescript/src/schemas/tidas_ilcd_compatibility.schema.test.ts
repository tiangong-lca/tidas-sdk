import assert from 'node:assert/strict';
import { describe, it } from 'node:test';
import { ProcessesSchema } from './tidas_processes.schema';
import { FlowsSchema } from './tidas_flows.schema';
import { ContactsSchema } from './tidas_contacts.schema';
import { UnitgroupsSchema } from './tidas_unitgroups.schema';
import { LciamethodsSchema } from './tidas_lciamethods.schema';
import { LifecyclemodelsSchema } from './tidas_lifecyclemodels.schema';

const reference = {
  '@type': 'process data set', '@refObjectId': '11111111-1111-1111-1111-111111111111',
  '@version': '01.00.000', '@uri': '../processes/process.xml',
  'common:shortDescription': { '@xml:lang': 'en', '#text': 'Example process' },
};

describe('ILCD-compatible generated schema boundaries', () => {
  it('accepts ordered parameters with optional mean values and rejects missing names/empty lists', () => {
    const schema = (ProcessesSchema as any).shape.processDataSet.shape.processInformation.shape.mathematicalRelations.unwrap().shape.variableParameter;
    const parameters = [{ '@name': 'a', meanValue: '0' }, { '@name': 'b', formula: 'a + 2' }];
    assert.deepEqual(schema.parse(parameters), parameters);
    assert.equal(schema.safeParse(parameters[1]).success, true);
    assert.equal(schema.safeParse([]).success, false);
    assert.equal(schema.safeParse([{ meanValue: '1' }]).success, false);
  });

  it('retains repeated locations and independent named classification systems', () => {
    const locations = (FlowsSchema as any).shape.flowDataSet.shape.flowInformation.shape.geography.unwrap().shape.locationOfSupply;
    assert.deepEqual(locations.parse(['DE', 'CN']), ['DE', 'CN']);
    const classifications = (ContactsSchema as any).shape.contactDataSet.shape.contactInformation.shape.dataSetInformation.shape.classificationInformation.shape['common:classification'];
    const systems = ['A', 'B'].map((name) => ({ '@name': name, '@classes': `https://example.org/${name}`, 'common:class': [{ '@level': '0', '@classId': name, '#text': name }] }));
    assert.deepEqual(classifications.parse(systems), systems);
    assert.equal(classifications.safeParse([]).success, false);
  });

  it('requires unit names and numeric factors while retaining zero and optional unit IDs', () => {
    const schema = (UnitgroupsSchema as any).shape.unitGroupDataSet.shape.units.shape.unit;
    assert.equal(schema.safeParse({ name: 'kg', meanValue: '0' }).success, true);
    assert.equal(schema.safeParse({ name: 'kg' }).success, false);
    assert.equal(schema.safeParse({ meanValue: '1' }).success, false);
  });

  it('accepts canonical and legacy model scaling separately, and rejects conflicts', () => {
    const schema = (LifecyclemodelsSchema as any).shape.lifeCycleModelDataSet.shape.lifeCycleModelInformation.shape.technology.shape.processes.shape.processInstance;
    const instance = { '@dataSetInternalID': '0', '@multiplicationFactor': '1', referenceToProcess: reference, parameters: { parameter: { '@name': 'p', '#text': '1.5' } } };
    assert.equal(schema.safeParse({ ...instance, scalingFactor: '0' }).success, true);
    assert.equal(schema.safeParse({ ...instance, scalingFactors: '0' }).success, true);
    assert.equal(schema.safeParse({ ...instance, scalingFactor: '0', scalingFactors: '0' }).success, false);
    assert.equal(schema.safeParse({ ...instance, parameters: { parameter: { '#text': '1.5' } } }).success, false);
  });

  it('accepts canonical LCIA geography and rejects simultaneous legacy spelling', () => {
    const schema = (LciamethodsSchema as any).shape.LCIAMethodDataSet.shape.LCIAMethodInformation.shape.geography;
    const canonical = { interventionSubLocation: 'Region A' };
    assert.equal(schema.safeParse(canonical).success, true);
    assert.equal(schema.safeParse({ ...canonical, intervensionSubLocation: 'Region B' }).success, false);
  });
});
