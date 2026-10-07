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
    if (c.expected.allocationVectors)
      assert.deepEqual(
        r.interpretations.map((i) => i.allocations),
        c.expected.allocationVectors
      );
    if (c.expected.coefficientVectors)
      assert.deepEqual(
        r.interpretations.map((i) => i.coefficients.map((f) => f.coefficient)),
        c.expected.coefficientVectors
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

test('numeric nonfinite fractions are invalid without mutating the input', () => {
  for (const value of [NaN, Infinity, -Infinity]) {
    const c = structuredClone(fixture.cases[0]);
    c.process.processDataSet.exchanges.exchange.allocations.allocation[0][
      '@allocatedFraction'
    ] = value;
    const r = analyzeProcessSemantics(c.process, { flows: c.flows });
    assert.deepEqual(
      r.validationIssues.map((i) => i.code),
      ['allocation_fraction_invalid']
    );
    assert.ok(
      Object.is(
        c.process.processDataSet.exchanges.exchange.allocations.allocation[0][
          '@allocatedFraction'
        ],
        value
      )
    );
  }
});
test('malformed and wrong-UUID resolver evidence is explicitly invalid evidence', () => {
  const c = fixture.cases[0];
  for (const evidence of [{}, [], 4, { ...c.flows[0], uuid: 'another-uuid' }]) {
    const r = analyzeProcessSemantics(c.process, {
      resolveFlow: () => evidence as ExactFlowEvidence,
    });
    assert.equal(r.complete, false);
    assert.deepEqual(
      r.validationIssues.map((i) => i.code),
      ['allocation_flow_evidence_invalid']
    );
  }
});
test('malformed declarations and missing quantitative-reference basis produce stable invalid findings', () => {
  const cases = [
    [undefined, 'quantitative_reference_missing'],
    [[], 'quantitative_reference_missing'],
    ['01', 'quantitative_reference_invalid'],
  ] as const;
  for (const [reference, expected] of cases) {
    const c = structuredClone(fixture.cases[0]);
    c.process.processDataSet.processInformation.quantitativeReference.referenceToReferenceFlow =
      reference;
    const r = analyzeProcessSemantics(c.process, { flows: c.flows });
    assert.equal(r.validationIssues[0].code, expected);
  }
  for (const declaration of [
    null,
    [],
    'invalid',
    [{}],
    [{ '@allocatedFraction': '100' }, { '@allocatedFraction': '100' }],
  ]) {
    const c = structuredClone(fixture.cases[0]);
    c.process.processDataSet.exchanges.exchange.allocations.allocation =
      declaration;
    assert.equal(
      analyzeProcessSemantics(c.process, { flows: c.flows }).valid,
      false
    );
  }
  const process = {
    processDataSet: {
      processInformation: {
        quantitativeReference: { '@type': 'Functional unit' },
      },
      exchanges: { exchange: { '@dataSetInternalID': '0' } },
    },
  };
  assert.equal(
    analyzeProcessSemantics(process).validationIssues[0].code,
    'quantitative_reference_basis_missing'
  );
});
