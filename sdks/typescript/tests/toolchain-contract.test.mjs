import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { createRequire } from 'node:module';
import {
  mkdirSync,
  mkdtempSync,
  readFileSync,
  readdirSync,
  rmSync,
  writeFileSync,
} from 'node:fs';
import { basename, dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { tmpdir } from 'node:os';
import test from 'node:test';
import { parse as parseYaml } from 'yaml';

const TEST_DIR = dirname(fileURLToPath(import.meta.url));
const PACKAGE_ROOT = dirname(TEST_DIR);
const REPOSITORY_ROOT = dirname(dirname(PACKAGE_ROOT));
const REPOSITORY_PACKAGE_JSON_PATH = join(REPOSITORY_ROOT, 'package.json');
const PNPM_WORKSPACE_PATH = join(REPOSITORY_ROOT, 'pnpm-workspace.yaml');
const NODE_PIN_PATH = join(REPOSITORY_ROOT, '.nvmrc');
const PACKAGE_JSON_PATH = join(PACKAGE_ROOT, 'package.json');
const REPOSITORY_PACKAGE_JSON = readJson(REPOSITORY_PACKAGE_JSON_PATH);
const PACKAGE_JSON = readJson(PACKAGE_JSON_PATH);
const PACKAGE_MANAGER = 'pnpm@11.24.0';
const PACKAGE_MANAGER_VERSION = PACKAGE_MANAGER.slice('pnpm@'.length);
const NODE_VERSION = '24.19.0';
const NODE_RUNTIME = `node@${NODE_VERSION}`;

const TYPESCRIPT_WORKFLOWS = [
  'ci.yml',
  'publish.yml',
  'sync-from-tidas-tools.yml',
  'tag-release-from-merge.yml',
];

const PACKAGE_LOCKFILE_NAMES = new Set([
  'bun.lock',
  'bun.lockb',
  'npm-shrinkwrap.json',
  'package-lock.json',
  'pnpm-lock.yaml',
  'pnpm-lock.yml',
  'yarn.lock',
]);

const NPM_PACKAGE_COMMAND_PATTERN =
  /(?:\bnpx\b|\bnpm\b[^\r\n]*\b(?:add|audit|cache|ci|config|dedupe|exec|fund|i|install|link|list|ls|outdated|pack|pkg|prune|publish|rebuild|remove|run|test|uninstall|unlink|update|version|view|whoami)\b)/i;

const BANNED_LEGACY_TOOLS = [
  'ts-to-zod',
  'typescript-eslint',
  '@typescript-eslint',
  'ts-jest',
  'ts-node',
];

const PUBLISH_FORBIDDEN_TOOLS = new Set([
  '@typescript-eslint/eslint-plugin',
  '@typescript-eslint/parser',
  'eslint',
  'jest',
  'json-schema-to-typescript',
  'json-schema-to-zod',
  'oxlint',
  'oxlint-tsgolint',
  'prettier',
  'ts-jest',
  'ts-json-schema-generator',
  'ts-node',
  'ts-to-zod',
  'tsx',
  'typescript',
  'typescript-eslint',
  'typescript-json-schema',
]);

test('all first-party manifests declare only direct TypeScript 7.x', () => {
  const manifests = [
    join(REPOSITORY_ROOT, 'package.json'),
    ...findFiles(PACKAGE_ROOT, (path) => basename(path) === 'package.json'),
  ];
  const declarations = [];

  for (const manifestPath of manifests) {
    const manifest = readJson(manifestPath);
    for (const section of [
      'dependencies',
      'devDependencies',
      'optionalDependencies',
      'peerDependencies',
    ]) {
      if (manifest[section]?.typescript !== undefined) {
        declarations.push({
          manifest: displayPath(manifestPath),
          section,
          range: manifest[section].typescript,
        });
      }
    }
  }

  assert.ok(
    declarations.length > 0,
    'a direct TypeScript dependency must be declared'
  );
  assert.deepEqual(
    declarations.filter(({ range }) => !isTypeScript7Range(range)),
    [],
    `direct TypeScript declarations must be 7.x:\n${formatJson(declarations)}`
  );

  const requireFromPackage = createRequire(PACKAGE_JSON_PATH);
  const installedVersion = readJson(
    requireFromPackage.resolve('typescript/package.json')
  ).version;
  assert.equal(
    majorVersion(installedVersion),
    7,
    `the directly installed TypeScript must be 7.x, received ${installedVersion}`
  );
});

test('the workspace pins the exact supported pnpm and Node.js versions', () => {
  assert.equal(REPOSITORY_PACKAGE_JSON.packageManager, PACKAGE_MANAGER);
  assert.deepEqual(REPOSITORY_PACKAGE_JSON.engines, {
    node: NODE_VERSION,
    pnpm: PACKAGE_MANAGER_VERSION,
  });
  assert.deepEqual(PACKAGE_JSON.engines, { node: NODE_VERSION });
  assert.equal(readFileSync(NODE_PIN_PATH, 'utf8').trim(), NODE_VERSION);

  const installedVersion = execFileSync(
    'pnpm',
    ['--version'],
    commandOptions(REPOSITORY_ROOT)
  ).trim();
  assert.equal(
    installedVersion,
    PACKAGE_MANAGER_VERSION,
    `the active pnpm must match ${PACKAGE_MANAGER}, received ${installedVersion}`
  );
});

test('every TypeScript workflow pins the exact supported Node.js runtime', () => {
  for (const workflowName of TYPESCRIPT_WORKFLOWS) {
    const workflowPath = join(
      REPOSITORY_ROOT,
      '.github',
      'workflows',
      workflowName
    );
    const workflow = parseYaml(readFileSync(workflowPath, 'utf8'));
    const setupSteps = Object.values(workflow.jobs ?? {}).flatMap((job) =>
      (job.steps ?? []).filter(
        (step) =>
          typeof step.uses === 'string' && step.uses.startsWith('pnpm/setup@')
      )
    );

    assert.equal(
      setupSteps.length,
      1,
      `${workflowName} must contain one pnpm/setup step`
    );
    assert.equal(
      setupSteps[0].with?.runtime,
      NODE_RUNTIME,
      `${workflowName} must use ${NODE_RUNTIME}`
    );
  }
});

test('pnpm-lock.yaml is the repository only package-manager lockfile', () => {
  const lockfiles = findFiles(REPOSITORY_ROOT, (path) =>
    PACKAGE_LOCKFILE_NAMES.has(basename(path))
  ).map(displayPath);

  assert.deepEqual(
    lockfiles,
    ['pnpm-lock.yaml'],
    `remove non-pnpm or nested package-manager lockfiles:\n${formatJson(lockfiles)}`
  );
});

test('pnpm supply-chain exceptions are exact, versioned Oxlint artifacts', () => {
  const workspace = parseYaml(readFileSync(PNPM_WORKSPACE_PATH, 'utf8'));
  const exceptions = workspace.minimumReleaseAgeExclude ?? [];

  assert.equal(
    exceptions.length,
    19,
    'the reviewed policy excludes the retired macOS Intel binding'
  );
  assert.equal(exceptions.includes('@oxlint/binding-darwin-x64@1.80.0'), false);
  assert.deepEqual(
    exceptions.filter(
      (entry) =>
        !/^(?:oxlint|@oxlint\/binding-[a-z0-9-]+)@1\.80\.0$/.test(entry)
    ),
    [],
    `minimum-release-age exceptions must stay exact and versioned:\n${formatJson(exceptions)}`
  );
});

test('the complete installed and locked pnpm workspace trees contain only TypeScript 7', () => {
  const installedTree = pnpmList(REPOSITORY_ROOT, 'typescript', {
    recursive: true,
  });
  const installed = collectDependencyVersions(installedTree, 'typescript');

  assert.ok(
    installed.length > 0,
    'the recursive pnpm workspace tree must contain direct TypeScript 7.x'
  );
  assert.deepEqual(
    installed.filter(({ version }) => majorVersion(version) !== 7),
    [],
    `pnpm workspace install tree contains non-7 TypeScript:\n${formatJson(installed)}`
  );

  const lockedTree = pnpmList(REPOSITORY_ROOT, 'typescript', {
    recursive: true,
    lockfileOnly: true,
  });
  const locked = collectDependencyVersions(lockedTree, 'typescript');

  assert.ok(
    locked.length > 0,
    'the recursive pnpm lock tree must pin direct TypeScript 7.x'
  );
  assert.deepEqual(
    locked.filter(({ version }) => majorVersion(version) !== 7),
    [],
    `pnpm workspace lock tree contains non-7 TypeScript:\n${formatJson(locked)}`
  );
});

test('dependency-tree inspection is recursive from the pnpm workspace root', () => {
  assert.deepEqual(pnpmListArguments('typescript', { recursive: true }), [
    'list',
    'typescript',
    '--recursive',
    '--depth',
    'Infinity',
    '--json',
  ]);
  assert.deepEqual(
    pnpmListArguments('typescript', {
      recursive: true,
      lockfileOnly: true,
    }),
    [
      'list',
      'typescript',
      '--recursive',
      '--depth',
      'Infinity',
      '--json',
      '--lockfile-only',
    ]
  );
});

test('package, config, and script surfaces contain no banned legacy tooling', () => {
  const governedFiles = [
    join(REPOSITORY_ROOT, 'package.json'),
    ...findFiles(PACKAGE_ROOT, (path) => {
      const name = basename(path);
      const packageRelativePath = relative(PACKAGE_ROOT, path);
      return (
        name === 'package.json' ||
        name === 'package-lock.json' ||
        /^tsconfig(?:\..+)?\.json$/.test(name) ||
        /(?:^|[.])config[.]/.test(name) ||
        packageRelativePath.startsWith(`scripts${pathSeparator()}`)
      );
    }),
  ];
  const findings = [];

  for (const path of governedFiles) {
    const content = readFileSync(path, 'utf8').toLowerCase();
    for (const bannedTool of BANNED_LEGACY_TOOLS) {
      if (content.includes(bannedTool)) {
        findings.push({ file: displayPath(path), bannedTool });
      }
    }
  }

  assert.deepEqual(
    findings,
    [],
    `legacy tool references remain on governed surfaces:\n${formatJson(findings)}`
  );
});

test('active package-management commands use pnpm instead of npm or npx', () => {
  const findings = [];
  const manifestPaths = [
    REPOSITORY_PACKAGE_JSON_PATH,
    ...findFiles(PACKAGE_ROOT, (path) => basename(path) === 'package.json'),
  ];

  for (const manifestPath of manifestPaths) {
    const scripts = readJson(manifestPath).scripts ?? {};
    for (const [name, command] of Object.entries(scripts)) {
      if (NPM_PACKAGE_COMMAND_PATTERN.test(command)) {
        findings.push({
          file: displayPath(manifestPath),
          surface: `scripts.${name}`,
          command,
        });
      }
    }
  }

  const workflowRoot = join(REPOSITORY_ROOT, '.github', 'workflows');
  for (const workflowPath of findFiles(workflowRoot, (path) =>
    /\.ya?ml$/.test(path)
  )) {
    collectCommandLines(workflowPath, findings);
  }

  const automationRoots = [
    join(REPOSITORY_ROOT, 'scripts'),
    join(REPOSITORY_ROOT, '.specify', 'scripts'),
  ];
  for (const automationRoot of automationRoots) {
    for (const scriptPath of findFiles(automationRoot, (path) =>
      /\.(?:bash|sh|zsh)$/.test(path)
    )) {
      collectCommandLines(scriptPath, findings);
    }
  }

  const hookRoot = join(REPOSITORY_ROOT, '.githooks');
  for (const hookPath of findFiles(hookRoot, () => true)) {
    collectCommandLines(hookPath, findings);
  }

  assert.deepEqual(
    findings,
    [],
    `active npm or npx package-management commands remain:\n${formatJson(findings)}`
  );
});

test('every maintained example script enters through pnpm', () => {
  const examplesPackagePath = join(PACKAGE_ROOT, 'examples', 'package.json');
  const examplesPackage = readJson(examplesPackagePath);
  const scripts = examplesPackage.scripts ?? {};
  const findings = Object.entries(scripts)
    .filter(([, command]) => !/^pnpm(?:\s|$)/.test(command))
    .map(([name, command]) => ({ name, command }));

  assert.equal(
    examplesPackage.dependencies?.[PACKAGE_JSON.name],
    'workspace:*',
    'examples must refuse a registry fallback for the local SDK workspace'
  );
  assert.ok(
    Object.keys(scripts).length > 0,
    'example scripts must be declared'
  );
  assert.deepEqual(
    findings,
    [],
    `example scripts must use pnpm explicitly:\n${formatJson(findings)}`
  );
});

test('published dependencies contain no compiler, generator, lint, or test tooling', () => {
  const publishedDependencies = Object.keys(PACKAGE_JSON.dependencies ?? {});
  const forbiddenDependencies = publishedDependencies.filter(
    (dependency) =>
      PUBLISH_FORBIDDEN_TOOLS.has(dependency) ||
      dependency.startsWith('@types/') ||
      dependency.includes('typescript-eslint')
  );

  assert.deepEqual(
    forbiddenDependencies,
    [],
    `move build-only tooling out of published dependencies: ${forbiddenDependencies.join(', ')}`
  );
});

test('the package publishes only to the public npm registry', () => {
  assert.deepEqual(PACKAGE_JSON.publishConfig, {
    access: 'public',
    registry: 'https://registry.npmjs.org/',
  });
});

test('all package tsconfigs avoid TypeScript 7 removed module resolution options', () => {
  const configPaths = findFiles(PACKAGE_ROOT, (path) =>
    /^tsconfig(?:\..+)?\.json$/.test(basename(path))
  );
  const findings = [];

  for (const configPath of configPaths) {
    const compilerOptions = readJson(configPath).compilerOptions ?? {};
    const moduleResolution = String(
      compilerOptions.moduleResolution ?? ''
    ).toLowerCase();

    if (moduleResolution === 'node' || moduleResolution === 'node10') {
      findings.push({
        file: displayPath(configPath),
        option: 'moduleResolution',
        value: compilerOptions.moduleResolution,
      });
    }
    if (Object.hasOwn(compilerOptions, 'baseUrl')) {
      findings.push({
        file: displayPath(configPath),
        option: 'baseUrl',
        value: compilerOptions.baseUrl,
      });
    }
  }

  assert.deepEqual(
    findings,
    [],
    `removed tsconfig options remain:\n${formatJson(findings)}`
  );
});

test('the Node coverage command scopes first-party code and enforces the recorded ratchets', () => {
  const coverageCommand = PACKAGE_JSON.scripts?.['test:coverage'] ?? '';
  const coverageIncludes = [
    ...coverageCommand.matchAll(
      /--test-coverage-include=(?:"([^"]+)"|'([^']+)'|(\S+))/g
    ),
  ].map((match) => match[1] ?? match[2] ?? match[3]);

  assert.deepEqual(coverageIncludes, [
    'src/**',
    'scripts/**',
    '../../scripts/ci/tidas-tools-assets.mjs',
  ]);
  assert.doesNotMatch(coverageCommand, /--test-coverage-include='/);
  assert.match(coverageCommand, /--test-coverage-lines=95(?:\s|$)/);
  assert.match(coverageCommand, /--test-coverage-branches=75(?:\s|$)/);
  assert.match(coverageCommand, /--test-coverage-functions=70(?:\s|$)/);
});

function processSemanticConsumerContract(apiExpression) {
  const fixtures = readJson(join(PACKAGE_ROOT, 'tests/fixtures/process-semantics.v1.json'));
  return `const semanticApi = ${apiExpression};
const semanticFixtures = ${JSON.stringify(fixtures)};
for (const fixture of semanticFixtures.cases) {
  const before = JSON.stringify(fixture.process);
  const result = semanticApi.analyzeProcessSemantics(fixture.process, { flows: fixture.flows });
  if (result.profile !== semanticFixtures.profile || result.tolerance !== semanticFixtures.tolerance ||
      result.valid !== fixture.expected.valid || result.complete !== fixture.expected.complete ||
      JSON.stringify(result.validationIssues.map(issue => issue.code)) !== JSON.stringify(fixture.expected.codes) ||
      JSON.stringify(fixture.process) !== before ||
      (fixture.expected.coefficients && JSON.stringify(result.interpretations.map(i => i.coefficients[0]?.coefficient)) !== JSON.stringify(fixture.expected.coefficients)) ||
      (fixture.expected.coefficientVectors && JSON.stringify(result.interpretations.map(i => i.coefficients.map(c => c.coefficient))) !== JSON.stringify(fixture.expected.coefficientVectors)) ||
      (fixture.expected.allocationVectors && JSON.stringify(result.interpretations.map(i => i.allocations)) !== JSON.stringify(fixture.expected.allocationVectors))) {
    throw new Error('Packed process semantic conformance failed: ' + fixture.name);
  }
}
`;
}

test(
  'a built and packed SDK exposes every entry point to clean CJS, ESM, and TS7 consumers without bringing TypeScript',
  { timeout: 120_000 },
  () => {
    const fixtureRoot = mkdtempSync(join(tmpdir(), 'tidas-sdk-pack-contract-'));

    try {
      const packRoot = join(fixtureRoot, 'pack');
      const consumerRoot = join(fixtureRoot, 'consumer');
      mkdirSync(packRoot);
      mkdirSync(consumerRoot);

      // `pnpm pack` does not run `prepublishOnly`; always prove that the tarball
      // was produced from a fresh build instead of a stale local `dist/` tree.
      execFileSync('pnpm', ['run', 'build'], commandOptions(PACKAGE_ROOT));
      const packOutput = execFileSync(
        'pnpm',
        ['pack', '--json', '--pack-destination', packRoot],
        commandOptions(PACKAGE_ROOT)
      );
      const packMetadata = JSON.parse(packOutput);
      assert.equal(
        packMetadata.name,
        PACKAGE_JSON.name,
        'pnpm pack must describe the SDK tarball'
      );
      assertPackedExports(packMetadata.files ?? []);

      const tarball = readdirSync(packRoot)
        .filter((file) => file.endsWith('.tgz'))
        .map((file) => join(packRoot, file));
      assert.equal(
        tarball.length,
        1,
        `expected one pnpm tarball, received ${tarball.length}`
      );

      writeFileSync(
        join(consumerRoot, 'package.json'),
        `${JSON.stringify(
          {
            name: 'tidas-sdk-pack-consumer',
            private: true,
            packageManager: PACKAGE_MANAGER,
            dependencies: {
              [PACKAGE_JSON.name]: `file:${tarball[0]}`,
              zod: PACKAGE_JSON.dependencies.zod,
            },
          },
          null,
          2
        )}\n`,
        { encoding: 'utf8', flag: 'wx' }
      );
      execFileSync(
        'pnpm',
        [
          'install',
          '--ignore-scripts',
          '--no-frozen-lockfile',
          '--no-lockfile',
        ],
        commandOptions(consumerRoot)
      );

      const exportSpecifiers = Object.keys(PACKAGE_JSON.exports).map(
        packageSpecifier
      );
      assert.equal(
        exportSpecifiers.length,
        9,
        `the packed consumer contract expects nine SDK exports, received ${exportSpecifiers.length}`
      );
      writeFileSync(
        join(consumerRoot, 'require-check.cjs'),
        `${exportSpecifiers
          .map(
            (specifier) =>
              `assertModule(${JSON.stringify(specifier)}, require(${JSON.stringify(specifier)}));`
          )
          .join(
            '\n'
          )}\n${processSemanticConsumerContract("require('@tiangong-lca/tidas-sdk')")}\nconst publicRules = require('@tiangong-lca/tidas-sdk/contracts').getTidasPublicRules('flow');\nif (publicRules.status !== 'covered' || publicRules.rules.length === 0) {\n  throw new TypeError('Expected the packed CommonJS contract to expose covered Flow public rules.');\n}\n\nfunction assertModule(specifier, value) {\n  if ((typeof value !== 'object' && typeof value !== 'function') || value === null) {\n    throw new TypeError(\`Expected \${specifier} to load as a CommonJS module.\`);\n  }\n}\n`,
        { encoding: 'utf8', flag: 'wx' }
      );
      execFileSync(
        process.execPath,
        [join(consumerRoot, 'require-check.cjs')],
        commandOptions(consumerRoot)
      );

      writeFileSync(
        join(consumerRoot, 'import-check.mjs'),
        `${exportSpecifiers
          .map(
            (specifier, index) =>
              `const module${index} = await import(${JSON.stringify(specifier)});\nassertModule(${JSON.stringify(specifier)}, module${index});`
          )
          .join(
            '\n'
          )}\n${processSemanticConsumerContract("(await import('@tiangong-lca/tidas-sdk')).default")}\nconst contracts = await import('@tiangong-lca/tidas-sdk/contracts');\nconst publicRules = contracts.getTidasPublicRules('process');\nif (publicRules.status !== 'covered' || publicRules.rules.length === 0) {\n  throw new TypeError('Expected the packed ES contract to expose covered Process public rules.');\n}\n\nfunction assertModule(specifier, value) {\n  if (typeof value !== 'object' || value === null) {\n    throw new TypeError(\`Expected \${specifier} to load as an ES module.\`);\n  }\n}\n`,
        { encoding: 'utf8', flag: 'wx' }
      );
      execFileSync(
        process.execPath,
        [join(consumerRoot, 'import-check.mjs')],
        commandOptions(consumerRoot)
      );

      const typecheckSource = `${exportSpecifiers
        .map(
          (specifier, index) =>
            `import * as entry${index} from ${JSON.stringify(specifier)};\nvoid entry${index};`
        )
        .join(
          '\n'
        )}\nimport { analyzeProcessSemantics, type NormalizedValidationIssue } from '@tiangong-lca/tidas-sdk';\nconst semanticAnalysis = analyzeProcessSemantics({}, { flows: [{ uuid: 'id', version: '01.00.000', type: 'Waste flow' }] });\nconst semanticIssues: NormalizedValidationIssue[] = semanticAnalysis.validationIssues;\nvoid semanticIssues;\nimport { ProcessSchema } from '@tiangong-lca/tidas-sdk/schemas';\nimport { getTidasPublicRules, type TidasPublicRuleSelection } from '@tiangong-lca/tidas-sdk/contracts';\nimport { z } from 'zod';\nconst publicRules: TidasPublicRuleSelection = getTidasPublicRules('flow');\nif (publicRules.status === 'covered') publicRules.rules[0]?.id;\ntype ProcessOutput = z.output<typeof ProcessSchema>;\ntype ProcessResults = NonNullable<ProcessOutput['processDataSet']['LCIAResults']>;\ntype LCIAResultOutput = ProcessResults['LCIAResult'];\ntype IsUnknown<T> = unknown extends T ? ([T] extends [unknown] ? true : false) : false;\ntype AssertFalse<T extends false> = T;\ntype LCIAResultMustRemainTyped = AssertFalse<IsUnknown<LCIAResultOutput>>;\nvoid (undefined as unknown as LCIAResultMustRemainTyped);\n`;
      writeFileSync(join(consumerRoot, 'imports.ts'), typecheckSource, {
        encoding: 'utf8',
        flag: 'wx',
      });
      writeFileSync(join(consumerRoot, 'imports.mts'), typecheckSource, {
        encoding: 'utf8',
        flag: 'wx',
      });
      writeFileSync(
        join(consumerRoot, 'tsconfig.json'),
        `${JSON.stringify(
          {
            compilerOptions: {
              target: 'ES2022',
              module: 'Node16',
              moduleResolution: 'Node16',
              strict: true,
              noEmit: true,
              skipLibCheck: false,
              types: [],
            },
            include: ['./imports.ts', './imports.mts'],
          },
          null,
          2
        )}\n`,
        { encoding: 'utf8', flag: 'wx' }
      );
      const requireFromPackage = createRequire(PACKAGE_JSON_PATH);
      const typeScriptPackagePath = requireFromPackage.resolve(
        'typescript/package.json'
      );
      const typeScriptPackage = readJson(typeScriptPackagePath);
      const typeScriptCli = join(
        dirname(typeScriptPackagePath),
        typeScriptPackage.bin.tsc
      );
      const typeScriptVersion = execFileSync(
        process.execPath,
        [typeScriptCli, '--version'],
        commandOptions(consumerRoot)
      ).trim();
      assert.equal(
        majorVersion(typeScriptVersion.replace(/^Version\s+/, '')),
        7,
        `packed consumer contract must use TypeScript 7, received ${typeScriptVersion}`
      );
      execFileSync(
        process.execPath,
        [typeScriptCli, '--project', join(consumerRoot, 'tsconfig.json')],
        commandOptions(consumerRoot)
      );

      const consumerTree = pnpmList(consumerRoot, 'typescript');
      const installedTypeScript = collectDependencyVersions(
        consumerTree,
        'typescript'
      );
      assert.deepEqual(
        installedTypeScript,
        [],
        `the published SDK pulled compiler tooling into the consumer:\n${formatJson(
          installedTypeScript
        )}`
      );
    } finally {
      rmSync(fixtureRoot, { recursive: true, force: true });
    }
  }
);

function assertPackedExports(packedFileMetadata) {
  const packedFiles = new Set(
    packedFileMetadata.map(({ path }) => String(path).replaceAll('\\', '/'))
  );
  const missingConditions = [];
  const missingFiles = [];

  for (const [exportKey, conditions] of Object.entries(PACKAGE_JSON.exports)) {
    for (const condition of ['import', 'require', 'types']) {
      const target = conditions?.[condition];
      if (typeof target !== 'string') {
        missingConditions.push({ export: exportKey, condition });
        continue;
      }

      const packedPath = target.replace(/^\.\//, '').replaceAll('\\', '/');
      if (!packedFiles.has(packedPath)) {
        missingFiles.push({ export: exportKey, condition, path: packedPath });
      }
    }
  }

  assert.deepEqual(
    missingConditions,
    [],
    `every export must declare import, require, and types conditions:\n${formatJson(
      missingConditions
    )}`
  );
  assert.deepEqual(
    missingFiles,
    [],
    `packed tarball is missing exported JS or declaration files:\n${formatJson(
      missingFiles
    )}`
  );
}

function packageSpecifier(exportKey) {
  return exportKey === '.'
    ? PACKAGE_JSON.name
    : `${PACKAGE_JSON.name}${exportKey.slice(1)}`;
}

test('schema generator source invokes neither npx, ts-to-zod, nor Compiler API', () => {
  const generatorPaths = findFiles(PACKAGE_ROOT, (path) => {
    const packageRelativePath = relative(PACKAGE_ROOT, path);
    return (
      packageRelativePath.startsWith(`scripts${pathSeparator()}`) &&
      /(?:generat|schema-to).+\.(?:[cm]?[jt]s)$/.test(basename(path))
    );
  });
  const forbiddenPatterns = [
    { name: 'npx', pattern: /\bnpx\b/ },
    { name: 'ts-to-zod', pattern: /ts-to-zod/i },
    {
      name: 'TypeScript Compiler API import',
      pattern:
        /(?:from\s*['"]typescript['"]|require\(\s*['"]typescript['"]\s*\)|import\(\s*['"]typescript['"]\s*\))/,
    },
  ];
  const findings = [];

  for (const generatorPath of generatorPaths) {
    const content = readFileSync(generatorPath, 'utf8');
    for (const { name, pattern } of forbiddenPatterns) {
      if (pattern.test(content)) {
        findings.push({
          file: displayPath(generatorPath),
          forbiddenPattern: name,
        });
      }
    }
  }

  assert.deepEqual(
    findings,
    [],
    `schema generator still depends on a legacy compiler path:\n${formatJson(findings)}`
  );
});

function commandOptions(cwd) {
  return {
    cwd,
    encoding: 'utf8',
    env: process.env,
    stdio: ['ignore', 'pipe', 'pipe'],
  };
}

function pnpmList(
  cwd,
  dependency,
  { recursive = false, lockfileOnly = false } = {}
) {
  const result = spawnSync(
    'pnpm',
    pnpmListArguments(dependency, { recursive, lockfileOnly }),
    commandOptions(cwd)
  );

  assert.ifError(result.error);
  assert.equal(
    result.status,
    0,
    `pnpm list failed in ${cwd}:\n${result.stderr || result.stdout}`
  );
  return JSON.parse(result.stdout || '[]');
}

function pnpmListArguments(
  dependency,
  { recursive = false, lockfileOnly = false } = {}
) {
  const args = ['list', dependency];
  if (recursive) {
    args.push('--recursive');
  }
  args.push('--depth', 'Infinity', '--json');
  if (lockfileOnly) {
    args.push('--lockfile-only');
  }
  return args;
}

function collectDependencyVersions(tree, dependencyName) {
  const roots = Array.isArray(tree) ? tree : [tree];
  return roots.flatMap((root) =>
    collectDependencyVersionsFromNode(root, dependencyName, [])
  );
}

function collectDependencyVersionsFromNode(tree, dependencyName, ancestry) {
  const matches = [];
  for (const section of [
    'dependencies',
    'devDependencies',
    'optionalDependencies',
  ]) {
    for (const [name, metadata] of Object.entries(tree?.[section] ?? {})) {
      const entry = `${name}@${metadata.version ?? 'unknown'}`;
      const dependencyPath = [...ancestry, entry];
      if (name === dependencyName) {
        matches.push({
          version: metadata.version,
          path: dependencyPath.join(' > '),
        });
      }
      matches.push(
        ...collectDependencyVersionsFromNode(
          metadata,
          dependencyName,
          dependencyPath
        )
      );
    }
  }
  return matches;
}

function collectCommandLines(path, findings) {
  const lines = readFileSync(path, 'utf8').split(/\r?\n/);
  for (const [index, line] of lines.entries()) {
    const trimmed = line.trim();
    if (trimmed.startsWith('#') || !NPM_PACKAGE_COMMAND_PATTERN.test(line)) {
      continue;
    }
    findings.push({
      file: displayPath(path),
      line: index + 1,
      command: trimmed,
    });
  }
}

function findFiles(root, predicate) {
  const files = [];
  for (const entry of readdirSync(root, { withFileTypes: true })) {
    if (
      entry.name === '.git' ||
      entry.name === '.pnpm-store' ||
      entry.name === 'coverage' ||
      entry.name === 'dist' ||
      entry.name === 'node_modules'
    ) {
      continue;
    }
    const path = join(root, entry.name);
    if (entry.isDirectory()) {
      files.push(...findFiles(path, predicate));
    } else if (entry.isFile() && predicate(path)) {
      files.push(path);
    }
  }
  return files.sort((left, right) =>
    left < right ? -1 : left > right ? 1 : 0
  );
}

function readJson(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function majorVersion(version) {
  const match = String(version ?? '').match(/^(\d+)/);
  return match ? Number(match[1]) : Number.NaN;
}

function isTypeScript7Range(range) {
  return /^(?:[~^])?7(?:\.|$)/.test(String(range).trim());
}

function displayPath(path) {
  return relative(REPOSITORY_ROOT, path) || '.';
}

function pathSeparator() {
  return process.platform === 'win32' ? '\\' : '/';
}

function formatJson(value) {
  return JSON.stringify(value, null, 2);
}
