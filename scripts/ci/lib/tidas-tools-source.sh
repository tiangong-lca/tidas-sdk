#!/usr/bin/env bash

# shellcheck shell=bash

TIDAS_TOOLS_REPO_URL="${TIDAS_TOOLS_REPO_URL:-https://github.com/tiangong-lca/tidas-tools.git}"
TIDAS_TOOLS_REF="${TIDAS_TOOLS_REF:-main}"

RESOLVED_TIDAS_TOOLS_PATH=""
RESOLVED_TIDAS_TOOLS_IS_TEMP=0

is_tidas_tools_checkout() {
    local candidate="${1:-}"

    [ -n "$candidate" ] && [ -d "$candidate/src/tidas_tools/tidas" ]
}

resolve_tidas_tools_source() {
    local repo_root="${1:?repo_root is required}"
    local -a candidates=()

    if [ -n "${TIDAS_TOOLS_PATH:-}" ]; then
        candidates+=("$TIDAS_TOOLS_PATH")
    fi

    candidates+=(
        "$repo_root/tidas-tools"
        "$repo_root/../tidas-tools"
    )

    for candidate in "${candidates[@]}"; do
        if is_tidas_tools_checkout "$candidate"; then
            RESOLVED_TIDAS_TOOLS_PATH="$(cd "$candidate" && pwd)"
            RESOLVED_TIDAS_TOOLS_IS_TEMP=0
            return 0
        fi
    done

    RESOLVED_TIDAS_TOOLS_PATH="$(mktemp -d "${TMPDIR:-/tmp}/tidas-tools.XXXXXX")"
    RESOLVED_TIDAS_TOOLS_IS_TEMP=1

    >&2 echo "[STEP] Syncing tidas-tools into a temporary checkout..."
    git clone --depth 1 --branch "$TIDAS_TOOLS_REF" "$TIDAS_TOOLS_REPO_URL" "$RESOLVED_TIDAS_TOOLS_PATH" >&2
}

cleanup_tidas_tools_source() {
    if [ "${RESOLVED_TIDAS_TOOLS_IS_TEMP:-0}" -eq 1 ] && [ -n "${RESOLVED_TIDAS_TOOLS_PATH:-}" ]; then
        rm -rf "$RESOLVED_TIDAS_TOOLS_PATH"
    fi
}
