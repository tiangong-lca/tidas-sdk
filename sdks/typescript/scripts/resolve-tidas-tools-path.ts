import { existsSync } from 'node:fs';
import path from 'node:path';

function repoRoot() {
  return path.resolve(__dirname, '../../..');
}

function candidateRoots() {
  const root = repoRoot();

  return [
    process.env.TIDAS_TOOLS_PATH,
    path.join(root, 'tidas-tools'),
    path.join(path.dirname(root), 'tidas-tools'),
  ].filter((value): value is string => Boolean(value));
}

function isToolsRoot(candidate: string) {
  return existsSync(path.join(candidate, 'src/tidas_tools/tidas'));
}

export function resolveTidasToolsRepoRoot() {
  for (const candidate of candidateRoots()) {
    if (isToolsRoot(candidate)) {
      return candidate;
    }
  }

  return null;
}

export function requireTidasToolsRepoRoot(message?: string) {
  const resolved = resolveTidasToolsRepoRoot();

  if (!resolved) {
    throw new Error(
      message ??
        'Could not resolve the upstream tidas-tools checkout. Set TIDAS_TOOLS_PATH or place a sibling ../tidas-tools checkout next to this repository.'
    );
  }

  return resolved;
}

export function resolveTidasToolsPackageDir() {
  const repoRoot = resolveTidasToolsRepoRoot();
  return repoRoot ? path.join(repoRoot, 'src/tidas_tools') : null;
}

export function requireTidasToolsPackageDir(message?: string) {
  return path.join(requireTidasToolsRepoRoot(message), 'src/tidas_tools');
}

export function resolveTidasToolsDir() {
  const packageDir = resolveTidasToolsPackageDir();
  return packageDir ? path.join(packageDir, 'tidas') : null;
}

export function requireTidasToolsDir(message?: string) {
  return path.join(requireTidasToolsPackageDir(message), 'tidas');
}

export function requireTidasToolsSchemaDir(message?: string) {
  return path.join(requireTidasToolsDir(message), 'schemas');
}
