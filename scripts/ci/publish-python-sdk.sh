#!/usr/bin/env bash

# Local helper to build and publish the Python SDK to PyPI
# without going through GitHub Actions.

set -euo pipefail

PYTHON_SDK_ROOT="${PYTHON_SDK_ROOT:-./sdks/python}"

GREEN="$(tput setaf 2 || true)"
RED="$(tput setaf 1 || true)"
YELLOW="$(tput setaf 3 || true)"
NC="$(tput sgr0 || true)"

log() { printf "%b[INFO]%b %s\n" "$GREEN" "$NC" "$*" >&2; }
warn() { printf "%b[WARN]%b %s\n" "$YELLOW" "$NC" "$*" >&2; }
err() { printf "%b[ERR ]%b %s\n" "$RED" "$NC" "$*" >&2; }

usage() {
    cat <<EOF
Usage: $0 [--repository-url URL] [--dry-run]

Build and publish the Python SDK under: $PYTHON_SDK_ROOT

Options:
  --repository-url URL  Override the default PyPI repository
                        (e.g. https://test.pypi.org/legacy/)
  --dry-run             Build the package but do not upload

Environment:
  PYPI_API_TOKEN        API token for the target PyPI repository
EOF
}

REPOSITORY_URL=""
DRY_RUN=0

while [ $# -gt 0 ]; do
    case "$1" in
        --repository-url)
            REPOSITORY_URL="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            err "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

if [ ! -d "$PYTHON_SDK_ROOT" ]; then
    err "Python SDK root not found: $PYTHON_SDK_ROOT"
    exit 1
fi

if [ "${DRY_RUN}" -eq 0 ] && [ -z "${PYPI_API_TOKEN:-}" ]; then
    warn "PYPI_API_TOKEN is not set. Upload will likely fail."
fi

log "Using Python SDK root: $PYTHON_SDK_ROOT"

cd "$PYTHON_SDK_ROOT"

if ! command -v uv >/dev/null 2>&1; then
    err "uv is not installed or not on PATH. Install it first (e.g. 'pip install uv' or see https://github.com/astral-sh/uv)."
    exit 1
fi

log "Syncing dependencies with uv (including dev tools)..."
uv sync --group dev || uv sync

log "Building distribution artifacts..."
uv run python -m build

if [ "$DRY_RUN" -eq 1 ]; then
    log "Dry run enabled; skipping upload."
    ls -1 dist || true
    exit 0
fi

log "Uploading to PyPI via twine..."
TWINE_ARGS=()
if [ -n "$REPOSITORY_URL" ]; then
    TWINE_ARGS+=(--repository-url "$REPOSITORY_URL")
fi

PYPI_PASSWORD="${PYPI_API_TOKEN:-}"
if [ -z "$PYPI_PASSWORD" ]; then
    warn "PYPI_API_TOKEN empty; twine will prompt for credentials."
fi

PYPI_API_TOKEN="$PYPI_PASSWORD" uv run twine upload "${TWINE_ARGS[@]}" dist/*

log "Publish completed."
