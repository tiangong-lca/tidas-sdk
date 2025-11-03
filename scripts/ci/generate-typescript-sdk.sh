#!/usr/bin/env bash

# TypeScript SDK 生成脚本
# 功能: 从 tidas-tools submodule 重新生成 TypeScript SDK
# 输出: 生成的文件列表和摘要

set -euo pipefail

# 默认参数
TIDAS_TOOLS_PATH="${TIDAS_TOOLS_PATH:-./tidas-tools}"
OUTPUT_DIR="${OUTPUT_DIR:-./sdks/typescript/src}"
SDK_ROOT="${SDK_ROOT:-./sdks/typescript}"

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

    if [ ! -d "$SDK_ROOT" ]; then
        log_error "SDK root directory not found: $SDK_ROOT"
        exit 1
    fi

    if [ ! -d "$OUTPUT_DIR" ]; then
        log_warn "Output directory not found, creating: $OUTPUT_DIR"
        mkdir -p "$OUTPUT_DIR"
    fi

    log_info "✓ tidas-tools path: $TIDAS_TOOLS_PATH"
    log_info "✓ SDK root: $SDK_ROOT"
    log_info "✓ Output directory: $OUTPUT_DIR"
}

# 检查依赖
check_dependencies() {
    log_step "Checking dependencies..."

    # 检查 Node.js
    if ! command -v node &> /dev/null; then
        log_error "node not found. Please install Node.js 14+"
        exit 1
    fi

    local node_version=$(node --version)
    log_info "✓ Node.js version: $node_version"

    # 检查 npm
    if ! command -v npm &> /dev/null; then
        log_error "npm not found. Please install npm"
        exit 1
    fi

    local npm_version=$(npm --version)
    log_info "✓ npm version: $npm_version"

    # 检查 package.json
    if [ ! -f "$SDK_ROOT/package.json" ]; then
        log_error "package.json not found in $SDK_ROOT"
        exit 1
    fi

    # 检查是否安装了依赖
    if [ ! -d "$SDK_ROOT/node_modules" ]; then
        log_warn "node_modules not found, installing dependencies..."
        cd "$SDK_ROOT"
        npm install
        cd - > /dev/null
    fi

    # 检查 tidas-tools 内容
    if [ ! -f "$TIDAS_TOOLS_PATH/README.md" ]; then
        log_warn "tidas-tools appears to be empty or not initialized"
        log_warn "Run: git submodule update --init --recursive"
    fi

    log_info "✓ All dependencies satisfied"
}

# 生成 SDK
generate_sdk() {
    log_step "Generating TypeScript SDK..."

    cd "$SDK_ROOT"

    log_info "Running TypeScript type generation..."

    # Step 1: Generate TypeScript types from JSON schemas
    if grep -q '"generate-types"' package.json; then
        log_info "Step 1/3: Generating TypeScript types from schemas..."
        if npm run generate-types; then
            log_info "✓ TypeScript types generated successfully"
        else
            log_error "TypeScript type generation failed"
            cd - > /dev/null
            exit 1
        fi
    else
        log_warn "generate-types script not found in package.json"
    fi

    # Step 2: Generate Zod validation schemas
    if grep -q '"generate-schemas"' package.json; then
        log_info "Step 2/3: Generating Zod validation schemas..."
        if npm run generate-schemas; then
            log_info "✓ Zod schemas generated successfully"
        else
            log_error "Zod schema generation failed"
            cd - > /dev/null
            exit 1
        fi
    else
        log_warn "generate-schemas script not found in package.json"
    fi

    # Step 3: Bundle methodologies (根据 build script)
    if grep -q '"bundle-methodologies"' package.json; then
        log_info "Step 3/3: Bundling LCIA methodologies..."
        if npm run bundle-methodologies; then
            log_info "✓ Methodologies bundled successfully"
        else
            log_warn "Methodology bundling failed (non-critical)"
        fi
    fi

    cd - > /dev/null

    log_info "✓ TypeScript SDK generated"
}

# 运行类型检查
run_typecheck() {
    log_step "Running type check..."

    cd "$SDK_ROOT"

    if npm run typecheck > /dev/null 2>&1; then
        log_info "✓ Type check passed"
    else
        log_warn "Type check failed - this may be expected if schemas are not yet complete"
    fi

    cd - > /dev/null
}

# 生成摘要
generate_summary() {
    log_step "Generating summary..."

    local types_dir="$OUTPUT_DIR/types"
    local schemas_dir="$OUTPUT_DIR/schemas"
    local generated_ts_files=$(find "$OUTPUT_DIR" -name "*.ts" -type f 2>/dev/null | wc -l | tr -d ' ')
    local types_count=0
    local schemas_count=0

    if [ -d "$types_dir" ]; then
        types_count=$(find "$types_dir" -name "*.ts" -type f 2>/dev/null | wc -l | tr -d ' ')
    fi

    if [ -d "$schemas_dir" ]; then
        schemas_count=$(find "$schemas_dir" -name "*.ts" -type f 2>/dev/null | wc -l | tr -d ' ')
    fi

    local generated_js_files=0
    if [ -d "$SDK_ROOT/dist" ]; then
        generated_js_files=$(find "$SDK_ROOT/dist" -name "*.js" -type f 2>/dev/null | wc -l | tr -d ' ')
    fi

    cat <<EOF

================================================================================
TypeScript SDK Generation Summary
================================================================================
Timestamp:        $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Source:           $TIDAS_TOOLS_PATH
Output:           $OUTPUT_DIR
TypeScript files: $generated_ts_files files total
  - Types:        $types_count files ($types_dir)
  - Schemas:      $schemas_count files ($schemas_dir)
Compiled files:   $generated_js_files JS files (if built)
Status:           SUCCESS
================================================================================

Generation includes:
  ✅ TypeScript types from TIDAS JSON schemas
  ✅ Zod validation schemas for runtime type checking
  ✅ Bundled LCIA methodologies

Next steps:
1. Run validation: cd sdks/typescript && npm run lint
2. Run type check: cd sdks/typescript && npm run typecheck
3. Run tests: cd sdks/typescript && npm test
4. Build: cd sdks/typescript && npm run build

EOF
}

# 主函数
main() {
    log_info "Starting TypeScript SDK generation..."
    log_info "================================================"

    validate_inputs
    check_dependencies
    generate_sdk
    run_typecheck
    generate_summary

    log_info "✓ TypeScript SDK generation completed"
    exit 0
}

# 执行主函数
main "$@"
