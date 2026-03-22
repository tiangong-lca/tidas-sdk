#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TS_ROOT="$REPO_ROOT/sdks/typescript"
TS_WORKSPACE="@tiangong-lca/tidas-sdk"

run_ts_workspace() {
    (
        cd "$REPO_ROOT"
        npm --workspace "$TS_WORKSPACE" "$@"
    )
}

snapshot_path_state() {
    local target="$1"
    {
        git -C "$REPO_ROOT" diff --no-ext-diff -- "$target"
        git -C "$REPO_ROOT" ls-files --others --exclude-standard -- "$target"
    }
}

require_stable_generation_output() {
    local target="$1"
    local before_state="$2"
    local after_state

    after_state="$(snapshot_path_state "$target")"
    if [ "$before_state" != "$after_state" ]; then
        echo "error: generation introduced uncommitted changes under '$target'" >&2
        git -C "$REPO_ROOT" status --short -- "$target" >&2
        exit 1
    fi
}

echo "[typescript] installing dependencies"
(
    cd "$REPO_ROOT"
    echo "[typescript] dependency root: $(pwd)"
    ls -la package.json package-lock.json

    if ! npm ci; then
        echo "[typescript] npm ci failed; falling back to npm install" >&2
        npm install
    fi
)

before_generated_state="$(snapshot_path_state "sdks/typescript/src")"

echo "[typescript] regenerating package sources"
TIDAS_TOOLS_SOURCE_MODE="${TIDAS_TOOLS_SOURCE_MODE:-clone}" \
    "$REPO_ROOT/scripts/ci/generate-typescript-sdk.sh"
require_stable_generation_output "sdks/typescript/src" "$before_generated_state"

echo "[typescript] lint"
run_ts_workspace run lint

echo "[typescript] typecheck"
run_ts_workspace run typecheck

echo "[typescript] test"
run_ts_workspace test

echo "[typescript] build"
run_ts_workspace run build

echo "[typescript] pack dry run"
run_ts_workspace pack --dry-run >/dev/null

echo "[typescript] verification complete"
