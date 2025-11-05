#!/usr/bin/env bash

# Python SDK 生成脚本
# 功能: 从 tidas-tools submodule 重新生成 Python SDK
# 输出: 生成的文件列表和摘要

set -euo pipefail

# 默认参数
TIDAS_TOOLS_PATH="${TIDAS_TOOLS_PATH:-./tidas-tools}"
OUTPUT_DIR="${OUTPUT_DIR:-./sdks/python/src/tidas_sdk}"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

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

log_step() {
    echo -e "${BLUE}[STEP]${NC} $*" >&2
}

# 错误处理
handle_error() {
    local line_no=$1
    log_error "Script failed at line $line_no"
    log_error "Command: $BASH_COMMAND"
    exit 1
}

trap 'handle_error $LINENO' ERR

# 验证输入
validate_inputs() {
    log_step "Validating inputs..."

    if [ ! -d "$TIDAS_TOOLS_PATH" ]; then
        log_error "tidas-tools path not found: $TIDAS_TOOLS_PATH"
        exit 1
    fi

    if [ ! -d "$OUTPUT_DIR" ]; then
        log_warn "Output directory not found, creating: $OUTPUT_DIR"
        mkdir -p "$OUTPUT_DIR"
    fi

    log_info "✓ tidas-tools path: $TIDAS_TOOLS_PATH"
    log_info "✓ Output directory: $OUTPUT_DIR"
}

# 检查依赖
check_dependencies() {
    log_step "Checking dependencies..."

    # 检查 Python
    if ! command -v python3 &> /dev/null; then
        log_error "python3 not found. Please install Python 3.12+"
        exit 1
    fi

    local python_version=$(python3 --version | cut -d' ' -f2)
    log_info "✓ Python version: $python_version"

    # 检查是否有 tidas-tools 内容
    if [ ! -f "$TIDAS_TOOLS_PATH/README.md" ]; then
        log_warn "tidas-tools appears to be empty or not initialized"
        log_warn "Run: git submodule update --init --recursive"
    fi
}

# 生成 SDK
generate_sdk() {
    log_step "Generating Python SDK..."

    # 定位 schema 目录
    local schema_dir="$TIDAS_TOOLS_PATH/src/tidas_tools/tidas/schemas"

    if [ ! -d "$schema_dir" ]; then
        log_error "Schema directory not found: $schema_dir"
        log_error "Expected path: tidas-tools/src/tidas_tools/tidas/schemas"
        exit 1
    fi

    log_info "Schema directory found: $schema_dir"

    # 统计 schema 文件
    local schema_count=$(find "$schema_dir" -name "tidas_*.json" | wc -l | tr -d ' ')
    log_info "Found $schema_count TIDAS schema files"

    # 切换到 Python SDK 目录
    local sdk_dir="./sdks/python"
    if [ ! -d "$sdk_dir" ]; then
        log_error "Python SDK directory not found: $sdk_dir"
        exit 1
    fi

    cd "$sdk_dir" || exit 1
    log_info "Working directory: $(pwd)"

    # 确保虚拟环境已激活或使用 uv
    if [ -f ".venv/bin/activate" ]; then
        log_info "Activating virtual environment..."
        source .venv/bin/activate
    elif command -v uv &> /dev/null; then
        log_info "Using uv for dependency management..."
    else
        log_error "Neither .venv nor uv found. Please set up Python environment."
        exit 1
    fi

    # 检查生成脚本是否存在
    local gen_script="scripts/generate_types.py"
    if [ ! -f "$gen_script" ]; then
        log_error "Generation script not found: $gen_script"
        exit 1
    fi

    log_info "Using generation script: $gen_script"

    # 运行生成脚本
    log_info "Running Python SDK generation..."

    if command -v uv &> /dev/null; then
        # 使用 uv run
        if uv run python "$gen_script" --schema-dir "../../$schema_dir" --force --verbose; then
            log_info "✓ Python SDK generation completed successfully"
        else
            log_error "Python SDK generation failed"
            cd - > /dev/null
            exit 1
        fi
    else
        # 使用标准 python
        if python "$gen_script" --schema-dir "../../$schema_dir" --force --verbose; then
            log_info "✓ Python SDK generation completed successfully"
        else
            log_error "Python SDK generation failed"
            cd - > /dev/null
            exit 1
        fi
    fi

    # 返回原始目录
    cd - > /dev/null

    # 验证生成结果
    local types_dir="$OUTPUT_DIR/types"
    if [ -d "$types_dir" ]; then
        local generated_count=$(find "$types_dir" -name "*.py" -type f | wc -l | tr -d ' ')
        log_info "✓ Generated $generated_count Python files in $types_dir"
    else
        log_warn "Types directory not found: $types_dir"
    fi

    log_info "✓ Python SDK generated successfully"
}

# 生成摘要
generate_summary() {
    log_step "Generating summary..."

    local types_dir="$OUTPUT_DIR/types"
    local wrappers_dir="$OUTPUT_DIR/wrappers"
    local generated_files=$(find "$OUTPUT_DIR" -name "*.py" -type f 2>/dev/null | wc -l | tr -d ' ')
    local types_count=0
    local wrappers_count=0

    if [ -d "$types_dir" ]; then
        types_count=$(find "$types_dir" -name "*.py" -type f 2>/dev/null | wc -l | tr -d ' ')
    fi

    if [ -d "$wrappers_dir" ]; then
        wrappers_count=$(find "$wrappers_dir" -name "*.py" -type f 2>/dev/null | wc -l | tr -d ' ')
    fi

    cat <<EOF

================================================================================
Python SDK Generation Summary
================================================================================
Timestamp:        $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Source:           $TIDAS_TOOLS_PATH
Output:           $OUTPUT_DIR
Generated files:  $generated_files Python files total
  - Types:        $types_count files ($types_dir)
  - Wrappers:     $wrappers_count files ($wrappers_dir)
Status:           SUCCESS
================================================================================

Generation includes:
  ✅ Pydantic types from TIDAS schemas (using datamodel-code-generator)
  ✅ Clean category files (using generate_category_types.py)
  ✅ Typed field hint wrappers (using generate_wrappers.py)

Next steps:
1. Run validation: cd sdks/python && uv run ruff check . && uv run mypy src
2. Run tests: cd sdks/python && uv run pytest
3. Verify generated code quality

EOF
}

# 主函数
main() {
    log_info "Starting Python SDK generation..."
    log_info "================================================"

    validate_inputs
    check_dependencies
    generate_sdk
    generate_summary

    log_info "✓ Python SDK generation completed"
    exit 0
}

# 执行主函数
main "$@"
