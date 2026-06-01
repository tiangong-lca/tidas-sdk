import bundledMethodologies from '../data/bundled-methodologies.json';
import contactSchema from '../runtime-assets/tidas/schemas/tidas_contacts.json';
import flowpropertySchema from '../runtime-assets/tidas/schemas/tidas_flowproperties.json';
import flowSchema from '../runtime-assets/tidas/schemas/tidas_flows.json';
import lciamethodSchema from '../runtime-assets/tidas/schemas/tidas_lciamethods.json';
import lifecyclemodelSchema from '../runtime-assets/tidas/schemas/tidas_lifecyclemodels.json';
import processSchema from '../runtime-assets/tidas/schemas/tidas_processes.json';
import runtimeRulesets from '../runtime-assets/tidas/methodologies/runtime_rulesets.json';
import sourceSchema from '../runtime-assets/tidas/schemas/tidas_sources.json';
import unitgroupSchema from '../runtime-assets/tidas/schemas/tidas_unitgroups.json';

export type TidasContractKind =
  | 'contact'
  | 'contacts'
  | 'flow'
  | 'flows'
  | 'flowproperty'
  | 'flowproperties'
  | 'lciamethod'
  | 'lciamethods'
  | 'lifecyclemodel'
  | 'lifecyclemodels'
  | 'process'
  | 'processes'
  | 'source'
  | 'sources'
  | 'unitgroup'
  | 'unitgroups';

export type TidasContractInclude = 'schema' | 'methodology' | 'ruleset';

export type TidasContractProfile = 'default' | 'ai-import';

export type TidasContractManifest = {
  schema_version: 1;
  kind: TidasCanonicalContractKind;
  profile: TidasContractProfile;
  includes: TidasContractInclude[];
  sdk_package: '@tiangong-lca/tidas-sdk';
  schema: TidasContractArtifactManifest | null;
  methodology: TidasContractArtifactManifest | null;
  ruleset: TidasContractArtifactManifest | null;
};

export type TidasContractArtifactManifest = {
  name: string;
  sha256: string;
  bytes: number;
};

export type TidasContractPack = {
  manifest: TidasContractManifest;
  schemaText?: string;
  schemaData?: unknown;
  methodologyText?: string;
  methodologyData?: unknown;
  runtimeRuleset?: unknown;
  aiContext?: {
    schema_version: 1;
    kind: TidasCanonicalContractKind;
    profile: TidasContractProfile;
    instructions: string[];
    schema_text?: string;
    methodology_text?: string;
    runtime_ruleset?: unknown;
  };
};

export type TidasCanonicalContractKind =
  | 'contact'
  | 'flow'
  | 'flowproperty'
  | 'lciamethod'
  | 'lifecyclemodel'
  | 'process'
  | 'source'
  | 'unitgroup';

type SchemaEntry = {
  fileName: string;
  data: unknown;
};

const kindAliases: Record<string, TidasCanonicalContractKind> = {
  contact: 'contact',
  contacts: 'contact',
  flow: 'flow',
  flows: 'flow',
  flowproperty: 'flowproperty',
  flowproperties: 'flowproperty',
  lciamethod: 'lciamethod',
  lciamethods: 'lciamethod',
  lifecyclemodel: 'lifecyclemodel',
  lifecyclemodels: 'lifecyclemodel',
  process: 'process',
  processes: 'process',
  source: 'source',
  sources: 'source',
  unitgroup: 'unitgroup',
  unitgroups: 'unitgroup',
};

const schemaEntries: Record<TidasCanonicalContractKind, SchemaEntry> = {
  contact: { fileName: 'tidas_contacts.json', data: contactSchema },
  flow: { fileName: 'tidas_flows.json', data: flowSchema },
  flowproperty: {
    fileName: 'tidas_flowproperties.json',
    data: flowpropertySchema,
  },
  lciamethod: { fileName: 'tidas_lciamethods.json', data: lciamethodSchema },
  lifecyclemodel: {
    fileName: 'tidas_lifecyclemodels.json',
    data: lifecyclemodelSchema,
  },
  process: { fileName: 'tidas_processes.json', data: processSchema },
  source: { fileName: 'tidas_sources.json', data: sourceSchema },
  unitgroup: { fileName: 'tidas_unitgroups.json', data: unitgroupSchema },
};

const methodologyKeys: Partial<Record<TidasCanonicalContractKind, string>> = {
  flow: 'flows',
  process: 'processes',
};

const methodologyFileNames: Partial<Record<TidasCanonicalContractKind, string>> = {
  flow: 'tidas_flows.yaml',
  process: 'tidas_processes.yaml',
};

export function normalizeTidasContractKind(
  kind: TidasContractKind | string
): TidasCanonicalContractKind {
  const normalized = kind.trim().toLowerCase().replace(/[-_]/g, '');
  const canonical = kindAliases[normalized];
  if (!canonical) {
    throw new Error(
      `Unsupported TIDAS contract kind '${kind}'. Available kinds: ${getAvailableTidasContractKinds().join(', ')}`
    );
  }
  return canonical;
}

export function getAvailableTidasContractKinds(): TidasCanonicalContractKind[] {
  return Object.keys(schemaEntries).sort() as TidasCanonicalContractKind[];
}

export function getTidasSchemaData(kind: TidasContractKind | string): unknown {
  return schemaEntries[normalizeTidasContractKind(kind)].data;
}

export function getTidasSchemaText(kind: TidasContractKind | string): string {
  return JSON.stringify(getTidasSchemaData(kind), null, 2);
}

export function getTidasMethodologyData(
  kind: TidasContractKind | string
): unknown | null {
  const methodologyKey = methodologyKeys[normalizeTidasContractKind(kind)];
  if (!methodologyKey) {
    return null;
  }
  return (
    bundledMethodologies.methodologies[
      methodologyKey as keyof typeof bundledMethodologies.methodologies
    ] ?? null
  );
}

export function getTidasMethodologyText(
  kind: TidasContractKind | string
): string | null {
  const methodologyKey = methodologyKeys[normalizeTidasContractKind(kind)];
  if (!methodologyKey) {
    return null;
  }
  return (
    bundledMethodologies.methodologyTexts?.[
      methodologyKey as keyof typeof bundledMethodologies.methodologyTexts
    ] ?? null
  );
}

export function getTidasRuntimeRuleset(
  kind: TidasContractKind | string
): unknown | null {
  const canonical = normalizeTidasContractKind(kind);
  const source = runtimeRulesets as {
    rulesets?: Array<Record<string, unknown>>;
    rules?: Array<Record<string, unknown>>;
    [key: string]: unknown;
  };
  const rulesets = (source.rulesets ?? []).filter(
    (entry) => entry.dataset_type === canonical
  );
  const rules = (source.rules ?? []).filter(
    (entry) => entry.dataset_type === canonical
  );

  if (rulesets.length === 0 && rules.length === 0) {
    return null;
  }

  return {
    $schema: source.$schema,
    schema_version: source.schema_version,
    ruleset_version: source.ruleset_version,
    purpose: source.purpose,
    rulesets,
    rules,
  };
}

export function getTidasContractPack(
  kind: TidasContractKind | string,
  options: {
    include?: TidasContractInclude[];
    profile?: TidasContractProfile;
    includeAiContext?: boolean;
  } = {}
): TidasContractPack {
  const canonical = normalizeTidasContractKind(kind);
  const includes = options.include ?? ['schema', 'methodology', 'ruleset'];
  const profile = options.profile ?? 'default';
  const schemaText = includes.includes('schema')
    ? getTidasSchemaText(canonical)
    : undefined;
  const schemaData = includes.includes('schema')
    ? getTidasSchemaData(canonical)
    : undefined;
  const methodologyText = includes.includes('methodology')
    ? getTidasMethodologyText(canonical) ?? undefined
    : undefined;
  const methodologyData = includes.includes('methodology')
    ? getTidasMethodologyData(canonical) ?? undefined
    : undefined;
  const runtimeRuleset = includes.includes('ruleset')
    ? getTidasRuntimeRuleset(canonical) ?? undefined
    : undefined;

  const manifest: TidasContractManifest = {
    schema_version: 1,
    kind: canonical,
    profile,
    includes,
    sdk_package: '@tiangong-lca/tidas-sdk',
    schema: schemaText
      ? artifactManifest(schemaEntries[canonical].fileName, schemaText)
      : null,
    methodology: methodologyText
      ? artifactManifest(methodologyFileNames[canonical] ?? 'methodology.yaml', methodologyText)
      : null,
    ruleset: runtimeRuleset
      ? artifactManifest(
          'runtime_rulesets.json',
          JSON.stringify(runtimeRuleset, null, 2)
        )
      : null,
  };

  const pack: TidasContractPack = {
    manifest,
    schemaText,
    schemaData,
    methodologyText,
    methodologyData,
    runtimeRuleset,
  };

  if (options.includeAiContext) {
    pack.aiContext = {
      schema_version: 1,
      kind: canonical,
      profile,
      instructions: buildAiContextInstructions(canonical, profile),
      schema_text: schemaText,
      methodology_text: methodologyText,
      runtime_ruleset: runtimeRuleset,
    };
  }

  return pack;
}

function artifactManifest(
  name: string,
  content: string
): TidasContractArtifactManifest {
  return {
    name,
    sha256: sha256(content),
    bytes: new TextEncoder().encode(content).byteLength,
  };
}

function buildAiContextInstructions(
  kind: TidasCanonicalContractKind,
  profile: TidasContractProfile
): string[] {
  const base = [
    `Generate or repair only canonical TIDAS ${kind} data.`,
    'Use the JSON schema as the structural contract.',
    'Use the methodology YAML as the semantic authoring contract when present.',
    'Treat runtime ruleset blocker rules as gate requirements.',
    'Return candidate data only; do not claim that database writes have happened.',
  ];

  if (profile === 'ai-import') {
    base.push(
      'Preserve source provenance and unresolved assumptions so Foundry can build evidence and repair queues.',
      'Prefer explicit null or issue reporting over inventing unsupported numeric values.'
    );
  }

  return base;
}

function sha256(input: string): string {
  const bytes = new TextEncoder().encode(input);
  const words = bytesToWords(bytes);
  const bitLength = bytes.length * 8;
  words[bitLength >> 5] |= 0x80 << (24 - (bitLength % 32));
  words[(((bitLength + 64) >> 9) << 4) + 15] = bitLength;

  const hash = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f,
    0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
  ];
  const k = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b,
    0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
    0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,
    0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152,
    0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
    0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819,
    0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
    0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
    0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ];
  const schedule = new Array<number>(64);

  for (let i = 0; i < words.length; i += 16) {
    for (let t = 0; t < 64; t++) {
      if (t < 16) {
        schedule[t] = words[i + t] | 0;
      } else {
        const s0 =
          rotateRight(schedule[t - 15], 7) ^
          rotateRight(schedule[t - 15], 18) ^
          (schedule[t - 15] >>> 3);
        const s1 =
          rotateRight(schedule[t - 2], 17) ^
          rotateRight(schedule[t - 2], 19) ^
          (schedule[t - 2] >>> 10);
        schedule[t] =
          (schedule[t - 16] + s0 + schedule[t - 7] + s1) | 0;
      }
    }

    let [a, b, c, d, e, f, g, h] = hash;
    for (let t = 0; t < 64; t++) {
      const s1 = rotateRight(e, 6) ^ rotateRight(e, 11) ^ rotateRight(e, 25);
      const ch = (e & f) ^ (~e & g);
      const temp1 = (h + s1 + ch + k[t] + schedule[t]) | 0;
      const s0 = rotateRight(a, 2) ^ rotateRight(a, 13) ^ rotateRight(a, 22);
      const maj = (a & b) ^ (a & c) ^ (b & c);
      const temp2 = (s0 + maj) | 0;

      h = g;
      g = f;
      f = e;
      e = (d + temp1) | 0;
      d = c;
      c = b;
      b = a;
      a = (temp1 + temp2) | 0;
    }

    hash[0] = (hash[0] + a) | 0;
    hash[1] = (hash[1] + b) | 0;
    hash[2] = (hash[2] + c) | 0;
    hash[3] = (hash[3] + d) | 0;
    hash[4] = (hash[4] + e) | 0;
    hash[5] = (hash[5] + f) | 0;
    hash[6] = (hash[6] + g) | 0;
    hash[7] = (hash[7] + h) | 0;
  }

  return hash
    .map((value) => (value >>> 0).toString(16).padStart(8, '0'))
    .join('');
}

function bytesToWords(bytes: Uint8Array): number[] {
  const words: number[] = [];
  for (let i = 0; i < bytes.length; i++) {
    words[i >> 2] |= bytes[i] << (24 - (i % 4) * 8);
  }
  return words;
}

function rotateRight(value: number, bits: number): number {
  return (value >>> bits) | (value << (32 - bits));
}
