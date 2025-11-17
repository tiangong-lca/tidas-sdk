#!/usr/bin/env bash

# Python SDK generation script
# Rebuilds the auto-generated Pydantic models from the JSON Schemas bundled in
# the tidas-tools submodule.

set -euo pipefail

TIDAS_TOOLS_PATH="${TIDAS_TOOLS_PATH:-./tidas-tools}"
PYTHON_SDK_ROOT="${PYTHON_SDK_ROOT:-./sdks/python}"
OUTPUT_DIR="${OUTPUT_DIR:-$PYTHON_SDK_ROOT/src/tidas_sdk/generated}"
GENERATOR="${GENERATOR:-$PYTHON_SDK_ROOT/scripts/generate_sdk.py}"

SCHEMAS_DIR="$TIDAS_TOOLS_PATH/src/tidas_tools/tidas/schemas"

GREEN="$(tput setaf 2)"
RED="$(tput setaf 1)"
YELLOW="$(tput setaf 3)"
BLUE="$(tput setaf 4)"
NC="$(tput sgr0)"

log() { printf "%b[INFO]%b %s\n" "$GREEN" "$NC" "$*" >&2; }
warn() { printf "%b[WARN]%b %s\n" "$YELLOW" "$NC" "$*" >&2; }
err() { printf "%b[ERR ]%b %s\n" "$RED" "$NC" "$*" >&2; }
step() { printf "%b[STEP]%b %s\n" "$BLUE" "$NC" "$*" >&2; }

handle_error() {
    err "Failure on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

validate_inputs() {
    step "Validating inputs..."
    if [ ! -d "$TIDAS_TOOLS_PATH" ] || [ -z "$(ls -A "$TIDAS_TOOLS_PATH" 2>/dev/null)" ]; then
        warn "tidas-tools appears empty. Did you run: git submodule update --init --recursive ?"
    fi
    if [ ! -d "$SCHEMAS_DIR" ]; then
        err "Schema directory not found: $SCHEMAS_DIR"
        exit 1
    fi
    if [ ! -f "$GENERATOR" ]; then
        err "Generator not found: $GENERATOR"
        exit 1
    fi
    mkdir -p "$OUTPUT_DIR"
    log "Schemas: $SCHEMAS_DIR"
    log "Output:  $OUTPUT_DIR"
}

check_dependencies() {
    step "Checking dependencies..."
    if ! command -v python3 >/dev/null 2>&1; then
        err "python3 not found in PATH"
        exit 1
    fi
    python3 --version
}

generate_models() {
    step "Generating Python models..."
    python3 "$GENERATOR" \
        --schemas "$SCHEMAS_DIR" \
        --output "$OUTPUT_DIR"
}

verify_generation() {
    step "Running basic verification..."
    python3 -m compileall "$PYTHON_SDK_ROOT/src/tidas_sdk" >/dev/null
    python3 - <<'PY'
from tidas_sdk import create_process

entity = create_process({})
entity.to_json()
PY
}

summarize() {
    step "Generation summary"
    local file_count
    file_count=$(find "$OUTPUT_DIR" -maxdepth 1 -name "*.py" | wc -l | tr -d ' ')
    cat <<EOF

================================================================
Python SDK generation completed
================================================================
Schemas directory : $SCHEMAS_DIR
Output directory  : $OUTPUT_DIR
Generated modules : $file_count
Timestamp         : $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Next steps        :
  1. Inspect generated modules under $OUTPUT_DIR
  2. Run ruff/mypy/pytest inside $PYTHON_SDK_ROOT
  3. Commit the refreshed artifacts
================================================================

EOF
}

main() {
    log "Starting Python SDK generation..."
    validate_inputs
    check_dependencies
    generate_models
    verify_generation
    summarize
    log "Done."
}

main "$@"
