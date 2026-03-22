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

export function resolveTidasToolsDir() {
  for (const candidate of candidateRoots()) {
    if (isToolsRoot(candidate)) {
      return path.join(candidate, 'src/tidas_tools/tidas');
    }
  }

  return null;
}

export function requireTidasToolsDir(message?: string) {
  const resolved = resolveTidasToolsDir();

  if (!resolved) {
    throw new Error(
      message ??
        'Could not resolve the upstream tidas-tools checkout. Set TIDAS_TOOLS_PATH or place a sibling ../tidas-tools checkout next to this repository.'
    );
  }

  return resolved;
}

export function requireTidasToolsSchemaDir(message?: string) {
  return path.join(requireTidasToolsDir(message), 'schemas');
}
