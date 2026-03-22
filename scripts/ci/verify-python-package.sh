#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
PY_ROOT="$REPO_ROOT/sdks/python"

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

echo "[python] syncing dependencies"
(cd "$PY_ROOT" && uv sync --group dev)

before_generated_state="$(snapshot_path_state "sdks/python/src/tidas_sdk/generated")"

echo "[python] regenerating package sources"
TIDAS_TOOLS_SOURCE_MODE="${TIDAS_TOOLS_SOURCE_MODE:-clone}" \
    "$REPO_ROOT/scripts/ci/generate-python-sdk.sh"
require_stable_generation_output "sdks/python/src/tidas_sdk/generated" "$before_generated_state"

echo "[python] ruff check"
(cd "$PY_ROOT" && uv run ruff check src tests)

echo "[python] pytest"
(cd "$PY_ROOT" && uv run pytest)

echo "[python] build + twine check"
(cd "$PY_ROOT" && rm -rf dist build && uv run python -m build && uv run twine check dist/*)

echo "[python] verification complete"
