#!/usr/bin/env bash

# Submodule 变更检测脚本
# 功能: 检测 tidas-tools submodule 的 commit 是否变更
# 输出: JSON 格式的变更信息

set -euo pipefail

# 默认参数
REF_BEFORE="${1:-HEAD^}"
REF_AFTER="${2:-HEAD}"
SUBMODULE_PATH="${3:-tidas-tools}"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${GREEN}[INFO]${NC} $*" >&2
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $*" >&2
}

# 检查 submodule 是否存在
if [ ! -d "$SUBMODULE_PATH" ]; then
    log_error "Submodule path '$SUBMODULE_PATH' does not exist"
    exit 2
fi

# 检查是否在 git 仓库中
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    log_error "Not in a git repository"
    exit 2
fi

# 获取 submodule 在不同 commit 的 SHA
log_info "Detecting changes in submodule '$SUBMODULE_PATH'"
log_info "Comparing $REF_BEFORE...$REF_AFTER"

# 获取 REF_BEFORE 的 submodule commit
OLD_COMMIT=$(git ls-tree "$REF_BEFORE" "$SUBMODULE_PATH" 2>/dev/null | awk '{print $3}')
if [ -z "$OLD_COMMIT" ]; then
    log_warn "Could not find submodule commit at $REF_BEFORE, assuming initial state"
    OLD_COMMIT="<none>"
fi

# 获取 REF_AFTER 的 submodule commit
NEW_COMMIT=$(git ls-tree "$REF_AFTER" "$SUBMODULE_PATH" 2>/dev/null | awk '{print $3}')
if [ -z "$NEW_COMMIT" ]; then
    log_error "Could not find submodule commit at $REF_AFTER"
    exit 2
fi

# 比较 commits
CHANGED=false
if [ "$OLD_COMMIT" != "$NEW_COMMIT" ]; then
    CHANGED=true
    log_info "Submodule changed: $OLD_COMMIT → $NEW_COMMIT"
else
    log_info "No submodule changes detected"
fi

# 输出 JSON
cat <<EOF
{
  "changed": $CHANGED,
  "old_commit": "$OLD_COMMIT",
  "new_commit": "$NEW_COMMIT",
  "submodule_path": "$SUBMODULE_PATH"
}
EOF

# 退出码: 0 表示有变更，1 表示无变更
if [ "$CHANGED" = "true" ]; then
    exit 0
else
    exit 1
fi
