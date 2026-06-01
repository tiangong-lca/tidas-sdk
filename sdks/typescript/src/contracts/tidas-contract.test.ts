import {
  getAvailableTidasContractKinds,
  getTidasContractPack,
  getTidasMethodologyText,
  getTidasRuntimeRuleset,
  getTidasSchemaText,
  normalizeTidasContractKind,
} from './tidas-contract';

describe('TIDAS contract helpers', () => {
  it('normalizes singular, plural, and dashed kind aliases', () => {
    expect(normalizeTidasContractKind('processes')).toBe('process');
    expect(normalizeTidasContractKind('life-cycle-model')).toBe(
      'lifecyclemodel'
    );
    expect(getAvailableTidasContractKinds()).toContain('flow');
  });

  it('returns full schema text for process and flow contracts', () => {
    expect(JSON.parse(getTidasSchemaText('process'))).toHaveProperty(
      'properties'
    );
    expect(JSON.parse(getTidasSchemaText('flow'))).toHaveProperty(
      'properties'
    );
  });

  it('returns bundled methodology YAML text where available', () => {
    expect(getTidasMethodologyText('process')).toContain(
      'Process Dataset Content Rules'
    );
    expect(getTidasMethodologyText('flow')).toContain(
      'Flow Dataset Content Rules'
    );
    expect(getTidasMethodologyText('source')).toBeNull();
  });

  it('filters runtime rulesets by canonical kind', () => {
    const processRuleset = getTidasRuntimeRuleset('process') as {
      rules?: Array<{ dataset_type?: string }>;
    };
    expect(processRuleset.rules?.length).toBeGreaterThan(0);
    expect(
      processRuleset.rules?.every((rule) => rule.dataset_type === 'process')
    ).toBe(true);
    expect(getTidasRuntimeRuleset('source')).toBeNull();
  });

  it('builds a reproducible AI context pack manifest', () => {
    const pack = getTidasContractPack('process', {
      profile: 'ai-import',
      includeAiContext: true,
    });

    expect(pack.manifest.kind).toBe('process');
    expect(pack.manifest.profile).toBe('ai-import');
    expect(pack.manifest.schema?.sha256).toMatch(/^[a-f0-9]{64}$/);
    expect(pack.manifest.methodology?.sha256).toMatch(/^[a-f0-9]{64}$/);
    expect(pack.manifest.ruleset?.sha256).toMatch(/^[a-f0-9]{64}$/);
    expect(pack.aiContext?.instructions.join(' ')).toContain('Foundry');
  });
});
