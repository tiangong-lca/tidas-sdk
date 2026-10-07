import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { test } from 'node:test';
import {
  analyzeProcessSemantics,
  type ExactFlowEvidence,
} from './process-semantics';
const fixture = JSON.parse(
  readFileSync(
    join(__dirname, '../../../tests/fixtures/process-semantics.v1.json'),
    'utf8'
  )
);
for (const c of fixture.cases)
  test(`process semantics conformance: ${c.name}`, () => {
    const before = JSON.stringify(c.process);
    const r = analyzeProcessSemantics(c.process, { flows: c.flows });
    assert.equal(r.profile, fixture.profile);
    assert.equal(r.tolerance, fixture.tolerance);
    assert.equal(r.valid, c.expected.valid);
    assert.equal(r.complete, c.expected.complete);
    assert.deepEqual(
      r.validationIssues.map((i) => i.code),
      c.expected.codes
    );
    if (c.expected.modes)
      assert.deepEqual(
        r.interpretations.map((i) => i.mode),
        c.expected.modes
      );
    if (c.expected.coefficients)
      assert.deepEqual(
        r.interpretations.map((i) => i.coefficients[0]?.coefficient),
        c.expected.coefficients
      );
    assert.deepEqual(analyzeProcessSemantics(c.process, { flows: c.flows }), r);
    assert.equal(JSON.stringify(c.process), before);
  });
test('bounded resolver caches exact identity and preserves accurate singleton/array paths', () => {
  const c = fixture.cases.find(
    (candidate: { name: string }) => candidate.name === 'duplicate targets'
  );
  let calls = 0;
  const r = analyzeProcessSemantics(c.process, {
    resolveFlow: () => {
      calls++;
      return c.flows[0];
    },
  });
  assert.equal(calls, 1);
  assert.deepEqual(r.validationIssues[0].path, [
    'processDataSet',
    'exchanges',
    'exchange',
    'allocations',
    'allocation',
    1,
    '@internalReferenceToCoProduct',
  ]);
});
test('resolver exceptions, mismatched identity and invalid evidence remain unresolved', () => {
  const c = fixture.cases[0];
  for (const resolveFlow of [
    () => {
      throw new Error('offline');
    },
    () => ({ ...c.flows[0], version: '02.00.000' }),
    () => ({ ...c.flows[0], type: 'invalid' }) as ExactFlowEvidence,
  ]) {
    const r = analyzeProcessSemantics(c.process, { resolveFlow });
    assert.equal(r.complete, false);
    assert.equal(r.valid, false);
  }
});
test('full vector projection preserves all targets independently of selected qref', () => {
  const c = fixture.cases.find(
    (candidate: { name: string }) => candidate.name === 'multiple targets'
  );
  const r = analyzeProcessSemantics(c.process, { flows: c.flows });
  assert.deepEqual(r.interpretations[0].allocations, [
    { targetId: '0', fraction: 70 },
    { targetId: '1', fraction: 30 },
  ]);
});
