/** Pure consumer policy, separate from the generated public structural schemas. */
export const PROCESS_SEMANTIC_PROFILE =
  'tidas.process-allocation-reference.v1' as const;
export const ALLOCATION_SUM_TOLERANCE = 0.0010000001;
export type SemanticPath = Array<string | number>;
export type CoverageStatus =
  'passed' | 'invalid' | 'unresolved' | 'not-applicable';
export interface ExactFlowEvidence {
  uuid: string;
  version: string;
  type: 'Product flow' | 'Waste flow' | 'Elementary flow' | 'Other flow';
  /** Caller-verified content identity; the analyzer does not download or hash evidence. */
  contentHash?: string;
}
export interface ProcessSemanticOptions {
  flows?: readonly ExactFlowEvidence[];
  /** Called once per distinct exact UUID/version. Exceptions become unresolved evidence. */
  resolveFlow?: (
    uuid: string,
    version: string
  ) => ExactFlowEvidence | undefined;
}
export type ProcessSemanticIssueCode =
  | 'allocation_coproduct_reference_missing'
  | 'allocation_flow_evidence_ambiguous'
  | 'allocation_flow_evidence_invalid'
  | 'allocation_flow_evidence_unavailable'
  | 'allocation_flow_reference_inexact'
  | 'allocation_flow_resolver_failed'
  | 'allocation_flow_version_mismatch'
  | 'allocation_fraction_invalid'
  | 'allocation_legacy_sum_invalid'
  | 'allocation_mixed_modes'
  | 'allocation_target_ambiguous'
  | 'allocation_target_direction_invalid'
  | 'allocation_target_duplicate'
  | 'allocation_target_flow_type_invalid'
  | 'allocation_target_id_invalid'
  | 'allocation_targetless_malformed'
  | 'allocation_vector_malformed'
  | 'allocation_vector_sum_invalid'
  | 'exchange_internal_id_ambiguous'
  | 'exchange_internal_id_invalid'
  | 'quantitative_reference_ambiguous'
  | 'quantitative_reference_basis_missing'
  | 'quantitative_reference_duplicate'
  | 'quantitative_reference_invalid'
  | 'quantitative_reference_missing'
  | 'quantitative_reference_type_invalid';
export interface ProcessSemanticIssue {
  code: ProcessSemanticIssueCode;
  path: SemanticPath;
  severity: 'error';
  params: Record<string, string | number>;
  message: string;
  rawCode: 'process_semantics';
}
export interface ProcessSemanticAnalysis {
  profile: typeof PROCESS_SEMANTIC_PROFILE;
  tolerance: number;
  complete: boolean;
  valid: boolean;
  coverage: Array<{
    check: string;
    status: CoverageStatus;
    path: SemanticPath;
  }>;
  validationIssues: ProcessSemanticIssue[];
  reference: {
    type: string;
    ids: string[];
    calculationApplicability: 'single-reference' | 'unsupported';
  };
  interpretations: Array<{
    exchangeId: string;
    mode:
      | 'undeclared'
      | 'legacy-scalar-empty'
      | 'explicit-vector'
      | 'legacy-output-share'
      | 'legacy-targetless-full'
      | 'invalid';
    coefficients: Array<{ referenceId: string; coefficient: number }>;
    allocations?: Array<{ targetId: string; fraction: number }>;
  }>;
}
type Obj = Record<string, unknown>;
const obj = (v: unknown): Obj =>
  v !== null && typeof v === 'object' && !Array.isArray(v) ? (v as Obj) : {};
const entries = (
  v: unknown,
  path: SemanticPath
): Array<{ value: unknown; path: SemanticPath }> =>
  Array.isArray(v)
    ? v.map((value, i) => ({ value, path: [...path, i] }))
    : v === undefined
      ? []
      : [{ value: v, path }];
const id = (v: unknown): string | undefined =>
  typeof v === 'string' && /^(0|[1-9]\d{0,5})$/.test(v)
    ? v
    : typeof v === 'number' && Number.isInteger(v) && v >= 0 && v <= 999999
      ? String(v)
      : undefined;
/** Full-string decimal grammar: no whitespace, percent suffix, hexadecimal, Infinity or coercion. */
const fraction = (v: unknown): number | undefined => {
  const n =
    typeof v === 'number'
      ? v
      : typeof v === 'string' &&
          /^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$/.test(v)
        ? Number(v)
        : NaN;
  return Number.isFinite(n) && n >= 0 && n <= 100 ? n : undefined;
};

export function analyzeProcessSemantics(
  process: unknown,
  options: ProcessSemanticOptions = {}
): ProcessSemanticAnalysis {
  const result: ProcessSemanticAnalysis = {
    profile: PROCESS_SEMANTIC_PROFILE,
    tolerance: ALLOCATION_SUM_TOLERANCE,
    complete: true,
    valid: true,
    coverage: [],
    validationIssues: [],
    reference: { type: '', ids: [], calculationApplicability: 'unsupported' },
    interpretations: [],
  };
  const check = (
    name: string,
    path: SemanticPath,
    status: CoverageStatus,
    code?: string,
    params: Record<string, string | number> = {}
  ) => {
    result.coverage.push({ check: name, status, path: [...path] });
    if (status === 'unresolved') result.complete = false;
    if (status === 'invalid' || status === 'unresolved') {
      result.valid = false;
      result.validationIssues.push({
        code: code as ProcessSemanticIssueCode,
        path: [...path],
        severity: 'error',
        params,
        message: code ?? name,
        rawCode: 'process_semantics',
      });
    }
  };
  const dataset = obj(obj(process).processDataSet);
  const exPath: SemanticPath = ['processDataSet', 'exchanges', 'exchange'];
  const exchanges = entries(obj(dataset.exchanges).exchange, exPath);
  const indexed = new Map<string, typeof exchanges>();
  for (const ex of exchanges) {
    const key = id(obj(ex.value)['@dataSetInternalID']);
    if (key === undefined) {
      check(
        'exchange-identity',
        [...ex.path, '@dataSetInternalID'],
        'invalid',
        'exchange_internal_id_invalid'
      );
      continue;
    }
    const matches = indexed.get(key);
    if (matches) matches.push(ex);
    else indexed.set(key, [ex]);
  }
  for (const [key, matches] of indexed)
    for (const match of matches)
      check(
        'exchange-identity',
        [...match.path, '@dataSetInternalID'],
        matches.length === 1 ? 'passed' : 'invalid',
        'exchange_internal_id_ambiguous',
        { id: key }
      );
  const qrPath: SemanticPath = [
    'processDataSet',
    'processInformation',
    'quantitativeReference',
  ];
  const qr = obj(obj(dataset.processInformation).quantitativeReference);
  const qrType = qr['@type'];
  result.reference.type = typeof qrType === 'string' ? qrType : '';
  if (qrType === 'Reference flow(s)') {
    const refs = entries(qr.referenceToReferenceFlow, [
      ...qrPath,
      'referenceToReferenceFlow',
    ]);
    if (!refs.length)
      check(
        'quantitative-reference',
        [...qrPath, 'referenceToReferenceFlow'],
        'invalid',
        'quantitative_reference_missing'
      );
    const seen = new Set<string>();
    for (const ref of refs) {
      const key = id(ref.value);
      const matches = key === undefined ? [] : (indexed.get(key) ?? []);
      const code =
        key === undefined
          ? 'quantitative_reference_invalid'
          : seen.has(key)
            ? 'quantitative_reference_duplicate'
            : matches.length === 0
              ? 'quantitative_reference_missing'
              : matches.length > 1
                ? 'quantitative_reference_ambiguous'
                : undefined;
      check(
        'quantitative-reference',
        ref.path,
        code ? 'invalid' : 'passed',
        code
      );
      if (key !== undefined) {
        seen.add(key);
        result.reference.ids.push(key);
      }
    }
    if (
      refs.length === 1 &&
      result.coverage
        .filter((c) => c.check === 'quantitative-reference')
        .every((c) => c.status === 'passed')
    )
      result.reference.calculationApplicability = 'single-reference';
  } else if (
    ['Functional unit', 'Other parameter', 'Production period'].includes(
      result.reference.type
    )
  ) {
    const texts = entries(qr.functionalUnitOrOther, [
      ...qrPath,
      'functionalUnitOrOther',
    ]);
    const validText =
      texts.length > 0 &&
      texts.every(
        ({ value }) =>
          typeof obj(value)['@xml:lang'] === 'string' &&
          typeof obj(value)['#text'] === 'string' &&
          (obj(value)['#text'] as string).trim().length > 0
      );
    check(
      'quantitative-reference',
      [...qrPath, 'functionalUnitOrOther'],
      validText ? 'passed' : 'invalid',
      'quantitative_reference_basis_missing'
    );
  } else
    check(
      'quantitative-reference',
      [...qrPath, '@type'],
      'invalid',
      'quantitative_reference_type_invalid'
    );
  const evidenceCache = new Map<
    string,
    { status: CoverageStatus; code?: string }
  >();
  const targetType = (exchange: unknown, path: SemanticPath) => {
    const ref = obj(obj(exchange).referenceToFlowDataSet);
    const uuid = ref['@refObjectId'];
    const version = ref['@version'];
    if (
      typeof uuid !== 'string' ||
      !uuid ||
      typeof version !== 'string' ||
      !version
    ) {
      check(
        'allocation-target-type',
        path,
        'unresolved',
        'allocation_flow_reference_inexact'
      );
      return;
    }
    const key = `${uuid}\u0000${version}`;
    let state = evidenceCache.get(key);
    if (!state) {
      const supplied = (options.flows ?? []).filter(
        (f) => f.uuid === uuid && f.version === version
      );
      let evidence: ExactFlowEvidence | undefined;
      let failed = false;
      if (supplied.length > 1)
        state = {
          status: 'unresolved',
          code: 'allocation_flow_evidence_ambiguous',
        };
      else {
        evidence = supplied[0];
        if (!evidence && options.resolveFlow)
          try {
            evidence = options.resolveFlow(uuid, version);
          } catch {
            failed = true;
          }
        if (!evidence)
          state = {
            status: 'unresolved',
            code: failed
              ? 'allocation_flow_resolver_failed'
              : (options.flows ?? []).some((f) => f.uuid === uuid)
                ? 'allocation_flow_version_mismatch'
                : 'allocation_flow_evidence_unavailable',
          };
        else if (evidence.uuid !== uuid || evidence.version !== version)
          state = {
            status: 'unresolved',
            code: 'allocation_flow_version_mismatch',
          };
        else if (
          ![
            'Product flow',
            'Waste flow',
            'Elementary flow',
            'Other flow',
          ].includes(evidence.type)
        )
          state = {
            status: 'unresolved',
            code: 'allocation_flow_evidence_invalid',
          };
        else
          state = ['Product flow', 'Waste flow'].includes(evidence.type)
            ? { status: 'passed' }
            : {
                status: 'invalid',
                code: 'allocation_target_flow_type_invalid',
              };
      }
      evidenceCache.set(key, state);
    }
    check('allocation-target-type', path, state.status, state.code);
  };
  const legacy: Array<{
    index: number;
    fraction: number;
    path: SemanticPath;
    direction: unknown;
  }> = [];
  let explicitCount = 0;
  for (const ex of exchanges) {
    const value = obj(ex.value);
    const key = id(value['@dataSetInternalID']) ?? '';
    const allocationContainer = obj(value.allocations);
    const raw = allocationContainer.allocation;
    const path = [...ex.path, 'allocations', 'allocation'];
    const interpretation: ProcessSemanticAnalysis['interpretations'][number] = {
      exchangeId: key,
      mode: 'invalid',
      coefficients: [],
    };
    result.interpretations.push(interpretation);
    if (
      value.allocations === undefined ||
      (!Array.isArray(raw) &&
        raw !== null &&
        typeof raw === 'object' &&
        Object.keys(obj(raw)).length === 0)
    ) {
      interpretation.mode =
        value.allocations === undefined ? 'undeclared' : 'legacy-scalar-empty';
      interpretation.coefficients = result.reference.ids.map((referenceId) => ({
        referenceId,
        coefficient: 1,
      }));
      check('allocation-vector', path, 'not-applicable');
      continue;
    }
    const allocations = entries(raw, path);
    if (
      !allocations.length ||
      allocations.some(
        (a) =>
          !a.value ||
          typeof a.value !== 'object' ||
          Array.isArray(a.value) ||
          Object.keys(obj(a.value)).length === 0
      )
    ) {
      check(
        'allocation-vector',
        path,
        'invalid',
        'allocation_vector_malformed'
      );
      continue;
    }
    const targeted = allocations.filter(
      (a) => obj(a.value)['@internalReferenceToCoProduct'] !== undefined
    );
    if (targeted.length && targeted.length !== allocations.length) {
      check('allocation-vector', path, 'invalid', 'allocation_mixed_modes');
      continue;
    }
    if (!targeted.length) {
      if (allocations.length !== 1) {
        check(
          'allocation-vector',
          path,
          'invalid',
          'allocation_targetless_malformed'
        );
        continue;
      }
      const n = fraction(obj(allocations[0].value)['@allocatedFraction']);
      if (n === undefined)
        check(
          'allocation-fraction',
          [...allocations[0].path, '@allocatedFraction'],
          'invalid',
          'allocation_fraction_invalid'
        );
      else
        legacy.push({
          index: result.interpretations.length - 1,
          fraction: n,
          path,
          direction: value.exchangeDirection,
        });
      continue;
    }
    explicitCount++;
    const seen = new Set<string>();
    const amounts = new Map<string, number>();
    let total = 0;
    let fractionsValid = true;
    const initialIssues = result.validationIssues.length;
    for (const allocation of allocations) {
      const a = obj(allocation.value);
      const target = id(a['@internalReferenceToCoProduct']);
      const targetPath = [...allocation.path, '@internalReferenceToCoProduct'];
      const matches = target === undefined ? [] : (indexed.get(target) ?? []);
      const code =
        target === undefined
          ? 'allocation_target_id_invalid'
          : seen.has(target)
            ? 'allocation_target_duplicate'
            : matches.length === 0
              ? 'allocation_coproduct_reference_missing'
              : matches.length > 1
                ? 'allocation_target_ambiguous'
                : undefined;
      check('allocation-target', targetPath, code ? 'invalid' : 'passed', code);
      if (target !== undefined) seen.add(target);
      if (matches.length === 1) {
        const direction = obj(matches[0].value).exchangeDirection;
        check(
          'allocation-target-direction',
          targetPath,
          direction === 'Input' || direction === 'Output'
            ? 'passed'
            : 'invalid',
          'allocation_target_direction_invalid'
        );
        targetType(matches[0].value, targetPath);
      }
      const n = fraction(a['@allocatedFraction']);
      check(
        'allocation-fraction',
        [...allocation.path, '@allocatedFraction'],
        n === undefined ? 'invalid' : 'passed',
        'allocation_fraction_invalid'
      );
      if (n === undefined) fractionsValid = false;
      else {
        total += n;
        if (target !== undefined) amounts.set(target, n / 100);
      }
    }
    if (fractionsValid)
      check(
        'allocation-vector',
        path,
        Math.abs(total - 100) <= ALLOCATION_SUM_TOLERANCE
          ? 'passed'
          : 'invalid',
        'allocation_vector_sum_invalid',
        { sum: total }
      );
    if (result.validationIssues.length === initialIssues) {
      interpretation.mode = 'explicit-vector';
      interpretation.allocations = allocations.map(({ value: entry }) => ({
        targetId: id(obj(entry)['@internalReferenceToCoProduct'])!,
        fraction: fraction(obj(entry)['@allocatedFraction'])!,
      }));
      interpretation.coefficients = result.reference.ids.map((referenceId) => ({
        referenceId,
        coefficient: amounts.get(referenceId) ?? 0,
      }));
    }
  }
  if (legacy.length) {
    const outputShares =
      legacy.every((l) => l.direction === 'Output') && legacy.length >= 2;
    const sum = legacy.reduce((n, l) => n + l.fraction, 0);
    for (const l of legacy) {
      const mixed = explicitCount > 0;
      const accepted =
        !mixed &&
        (outputShares
          ? Math.abs(sum - 100) <= ALLOCATION_SUM_TOLERANCE
          : Math.abs(l.fraction - 100) <= ALLOCATION_SUM_TOLERANCE);
      check(
        'allocation-legacy',
        l.path,
        accepted ? 'passed' : 'invalid',
        mixed ? 'allocation_mixed_modes' : 'allocation_legacy_sum_invalid',
        { sum: outputShares ? sum : l.fraction }
      );
      if (accepted) {
        const interpretation = result.interpretations[l.index];
        interpretation.mode = outputShares
          ? 'legacy-output-share'
          : 'legacy-targetless-full';
        interpretation.coefficients = result.reference.ids.map(
          (referenceId) => ({ referenceId, coefficient: l.fraction / 100 })
        );
      }
    }
  }
  if (!result.coverage.some((c) => c.check === 'allocation-target-type'))
    check('allocation-target-type', exPath, 'not-applicable');
  return result;
}
