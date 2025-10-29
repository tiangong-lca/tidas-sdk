import * as fs from 'fs';
import * as path from 'path';

/**
 * Generate an HTML page showing the diff between two JSON objects using Monaco Editor
 *
 * @param original - Original JSON object
 * @param improved - Improved/modified JSON object
 * @param options - Optional configuration
 * @returns HTML string containing the diff viewer
 */
export function generateDiffHTML(original: any, improved: any): string {
  const originalJson = JSON.stringify(original, null, 2);
  const improvedJson = JSON.stringify(improved, null, 2);

  return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Diff Viewer</title>
    <style>
        body { margin: 0; padding: 0; }
        #container { height: 100vh; }
    </style>
</head>
<body>
    <div id="container"></div>
    
    <script src="https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs/loader.js"></script>
    <script>
        require.config({ paths: { vs: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs' } });
        
        require(['vs/editor/editor.main'], function () {
            const originalText = ${JSON.stringify(originalJson)};
            const modifiedText = ${JSON.stringify(improvedJson)};
            
            const originalModel = monaco.editor.createModel(originalText, 'json');
            const modifiedModel = monaco.editor.createModel(modifiedText, 'json');

            const diffEditor = monaco.editor.createDiffEditor(document.getElementById('container'), {
                enableSplitViewResizing: true,
                renderSideBySide: true,
                readOnly: true,
                automaticLayout: true,
                fontSize: 14,
                minimap: { enabled: false }
            });

            diffEditor.setModel({
                original: originalModel,
                modified: modifiedModel
            });
        });
    </script>
</body>
</html>`;
}

/**
 * Save diff HTML to a file
 *
 * @param original - Original JSON object
 * @param improved - Improved/modified JSON object
 * @param outputPath - Path where to save the HTML file
 * @param options - Optional configuration
 */
export async function saveDiffToFile(
  original: any,
  improved: any,
  outputPath: string,
  options?: {
    title?: string;
    description?: string;
    theme?: 'light' | 'dark';
  }
): Promise<void> {
  const html = generateDiffHTML(original, improved);
  await fs.promises.writeFile(outputPath, html, 'utf-8');
  console.log(`Diff viewer saved to: ${outputPath}`);
}

/**
 * Generate a simple text-based diff summary
 *
 * @param original - Original JSON object
 * @param improved - Improved/modified JSON object
 * @param paths - Optional array of paths to focus on
 * @returns Text summary of differences
 */
export function generateDiffSummary(
  original: any,
  improved: any,
  paths?: string[]
): string {
  const summary: string[] = [];
  summary.push('=== Diff Summary ===\n');

  // If paths are specified, only compare those
  if (paths && paths.length > 0) {
    for (const path of paths) {
      const originalValue = getValueByPath(original, path);
      const improvedValue = getValueByPath(improved, path);

      if (JSON.stringify(originalValue) !== JSON.stringify(improvedValue)) {
        summary.push(`📝 ${path}:`);
        const originalStr = originalValue !== undefined 
          ? JSON.stringify(originalValue, null, 2).substring(0, 100)
          : 'undefined';
        const improvedStr = improvedValue !== undefined
          ? JSON.stringify(improvedValue, null, 2).substring(0, 100)
          : 'undefined';
        summary.push(`  Before: ${originalStr}...`);
        summary.push(`  After:  ${improvedStr}...`);
        summary.push('');
      }
    }
  } else {
    // Compare all properties recursively
    const diffs = findDifferences(original, improved);
    for (const diff of diffs) {
      summary.push(`📝 ${diff.path}:`);
      summary.push(`  Before: ${diff.original}`);
      summary.push(`  After:  ${diff.improved}`);
      summary.push('');
    }
  }

  return summary.join('\n');
}

/**
 * Helper function to get value by dot-notation path
 */
function getValueByPath(obj: any, path: string): any {
  const parts = path.split('.');
  let current = obj;

  for (const part of parts) {
    if (current && typeof current === 'object' && part in current) {
      current = current[part];
    } else {
      return undefined;
    }
  }

  return current;
}

/**
 * Helper function to find all differences between two objects
 */
function findDifferences(
  original: any,
  improved: any,
  path = ''
): Array<{ path: string; original: string; improved: string }> {
  const diffs: Array<{ path: string; original: string; improved: string }> = [];

  // Handle primitive values
  if (typeof original !== 'object' || typeof improved !== 'object') {
    if (JSON.stringify(original) !== JSON.stringify(improved)) {
      diffs.push({
        path: path || 'root',
        original: JSON.stringify(original).substring(0, 100),
        improved: JSON.stringify(improved).substring(0, 100),
      });
    }
    return diffs;
  }

  // Handle arrays
  if (Array.isArray(original) || Array.isArray(improved)) {
    if (JSON.stringify(original) !== JSON.stringify(improved)) {
      diffs.push({
        path: path || 'root',
        original: Array.isArray(original)
          ? `[${original.length} items]`
          : String(original),
        improved: Array.isArray(improved)
          ? `[${improved.length} items]`
          : String(improved),
      });
    }
    return diffs;
  }

  // Handle objects
  const allKeys = new Set([
    ...Object.keys(original || {}),
    ...Object.keys(improved || {}),
  ]);

  for (const key of allKeys) {
    const newPath = path ? `${path}.${key}` : key;
    const originalValue = original?.[key];
    const improvedValue = improved?.[key];

    if (JSON.stringify(originalValue) !== JSON.stringify(improvedValue)) {
      // For nested objects, recurse if both are objects
      if (
        typeof originalValue === 'object' &&
        typeof improvedValue === 'object' &&
        !Array.isArray(originalValue) &&
        !Array.isArray(improvedValue)
      ) {
        diffs.push(...findDifferences(originalValue, improvedValue, newPath));
      } else {
        diffs.push({
          path: newPath,
          original:
            originalValue !== undefined
              ? JSON.stringify(originalValue).substring(0, 100)
              : 'undefined',
          improved:
            improvedValue !== undefined
              ? JSON.stringify(improvedValue).substring(0, 100)
              : 'undefined',
        });
      }
    }
  }

  return diffs;
}

/**
 * Open diff viewer in browser (Node.js environment)
 */
export async function openDiffInBrowser(
  original: any,
  improved: any,
  options?: {
    title?: string;
    description?: string;
    theme?: 'light' | 'dark';
  }
): Promise<void> {
  const { exec } = await import('child_process');
  const { promisify } = await import('util');
  const execAsync = promisify(exec);

  // Create temp file
  const tempDir = await import('os').then((os) => os.tmpdir());
  const tempFile = path.join(tempDir, `diff-viewer-${Date.now()}.html`);

  // Save HTML to temp file
  await saveDiffToFile(original, improved, tempFile, options);

  // Open in default browser
  const platform = process.platform;
  const command =
    platform === 'darwin'
      ? 'open'
      : platform === 'win32'
        ? 'start'
        : 'xdg-open';

  try {
    await execAsync(`${command} "${tempFile}"`);
    console.log('Diff viewer opened in browser');
  } catch (error) {
    console.error('Failed to open browser:', error);
    console.log(`Please open manually: ${tempFile}`);
  }
}

export default {
  generateDiffHTML,
  saveDiffToFile,
  generateDiffSummary,
  openDiffInBrowser,
};
