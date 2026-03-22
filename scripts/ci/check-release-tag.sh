#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

usage() {
    cat <<EOF
Usage: $0 <typescript|python> [tag]

Validates that the provided tag matches the package version in the repository.
If [tag] is omitted, GITHUB_REF_NAME is used.
EOF
}

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    usage
    exit 1
fi

PACKAGE_KIND="$1"
TAG_NAME="${2:-${GITHUB_REF_NAME:-}}"

if [ -z "$TAG_NAME" ]; then
    echo "error: missing tag name and GITHUB_REF_NAME is not set" >&2
    exit 1
fi

cd "$REPO_ROOT"

case "$PACKAGE_KIND" in
    typescript)
        PACKAGE_NAME="$(node -p "require('./sdks/typescript/package.json').name")"
        PACKAGE_VERSION="$(node -p "require('./sdks/typescript/package.json').version")"
        EXPECTED_TAG="typescript-v${PACKAGE_VERSION}"
        ;;
    python)
        PACKAGE_NAME="tidas-sdk"
        PACKAGE_VERSION="$(
            python3 - <<'PY'
from pathlib import Path
import tomllib

with Path("sdks/python/pyproject.toml").open("rb") as fh:
    data = tomllib.load(fh)

print(data["project"]["version"])
PY
        )"
        EXPECTED_TAG="python-v${PACKAGE_VERSION}"
        ;;
    *)
        echo "error: unsupported package kind '$PACKAGE_KIND'" >&2
        usage
        exit 1
        ;;
esac

if [ "$TAG_NAME" != "$EXPECTED_TAG" ]; then
    echo "error: tag '$TAG_NAME' does not match ${PACKAGE_NAME} version ${PACKAGE_VERSION} (expected '$EXPECTED_TAG')" >&2
    exit 1
fi

echo "Validated ${PACKAGE_NAME} release tag: ${TAG_NAME}"
