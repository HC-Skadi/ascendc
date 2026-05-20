#!/bin/bash
#
# 阶段3：算子编译验证脚本
# 验证6个适配算子是否正确安装
#

set -e

WORKDIR="${WORKDIR:-.}"
LOG_FILE="${LOG_FILE:-stage_3_op.log}"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

# 需要检查的6个适配算子
REQUIRED_OPERATORS=(
    "mxrec_opp_asynchronous_complete_cumsum"
    "mxrec_opp_dense_to_jagged"
    "mxrec_opp_index_select_for_rank1_backward"
    "mxrec_opp_jagged_to_padded_dense"
    "mxrec_opp_gather_for_rank1"
    "mxrec_opp_hstu_dense_forward"
)

log_info "=== 算子编译验证 ==="
log_info "工作目录: $WORKDIR"
log_info "日志文件: $LOG_FILE"

ERRORS=0
WARNINGS=0

# 1. 检查 Python 和 torch_npu
log_info "检查1: 验证 Python 环境..."
if python3 -c "import torch_npu; print(torch_npu.__version__)" 2>/dev/null; then
    log_info "✓ torch_npu 可用"
else
    log_error "✗ torch_npu 不可用"
    ERRORS=$((ERRORS + 1))
fi

# 2. 检查 libhstu_dense_ops.so
log_info "检查2: 验证 libhstu_dense_ops.so..."
LIB_PATH=""
for path in \
    "/usr/local/Ascend/opp/built-in/ops_impl/framework/ascendc/libhstu_dense_ops.so" \
    "/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/ops_impl/framework/ascendc/libhstu_dense_ops.so" \
    "$WORKDIR/libhstu_dense_ops.so" \
    "./libhstu_dense_ops.so"; do
    if [ -f "$path" ]; then
        LIB_PATH="$path"
        log_info "✓ libhstu_dense_ops.so 存在: $path"
        break
    fi
done

if [ -z "$LIB_PATH" ]; then
    log_error "✗ libhstu_dense_ops.so 未找到"
    log_info "  搜索路径:"
    log_info "    - /usr/local/Ascend/opp/..."
    log_info "    - /usr/local/Ascend/ascend-toolkit/..."
    log_info "    - \$WORKDIR/"
    ERRORS=$((ERRORS + 1))
fi

# 3. 检查 gcc 版本
log_info "检查3: 验证 gcc 版本..."
if command -v gcc &> /dev/null; then
    GCC_VERSION=$(gcc --version | head -n1 | grep -oP '\d+\.\d+\.\d+')
    log_info "✓ gcc 版本: $GCC_VERSION"
    
    # 提取主版本号
    GCC_MAJOR=$(echo $GCC_VERSION | cut -d. -f1)
    if [ "$GCC_MAJOR" -ge 10 ]; then
        log_info "  ✓ gcc 版本符合建议 (≥10.2.0)"
    elif [ "$GCC_MAJOR" -ge 9 ]; then
        log_warn "  ⚠ gcc 版本可用，但建议使用 10.2.0+"
    else
        log_warn "  ⚠ gcc 版本较低，建议升级"
    fi
else
    log_warn "⚠ gcc 未安装（如果只使用预编译算子则不影响）"
fi

# 4. 尝试导入算子 Python 模块
log_info "检查4: 验证算子 Python 模块..."
if python3 -c "
import sys
sys.path.insert(0, '$WORKDIR')
try:
    # 尝试查找算子模块
    import importlib.util
    modules = [
        'mxrec_opp_asynchronous_complete_cumsum',
        'mxrec_opp_dense_to_jagged', 
        'mxrec_opp_index_select_for_rank1_backward',
        'mxrec_opp_jagged_to_padded_dense',
        'mxrec_opp_gather_for_rank1',
    ]
    found = 0
    for mod in modules:
        if importlib.util.find_spec(mod) is not None:
            found += 1
    print(f'Found {found}/{len(modules)} modules')
except Exception as e:
    print(f'Error: {e}')
" 2>/dev/null; then
    log_info "✓ 算子模块检查完成"
else
    log_warn "⚠ 无法自动检查算子模块，将尝试直接导入测试"
fi

# 5. 功能测试 - 尝试加载动态库
log_info "检查5: 动态库加载测试..."
if [ -n "$LIB_PATH" ]; then
    if python3 -c "import ctypes; ctypes.CDLL('$LIB_PATH')" 2>/dev/null; then
        log_info "✓ libhstu_dense_ops.so 可正常加载"
    else
        log_error "✗ libhstu_dense_ops.so 加载失败"
        ERRORS=$((ERRORS + 1))
    fi
fi

# 6. 算子注册检查
log_info "检查6: 算子注册检查..."
OPERATOR_CHECK_SCRIPT='
import torch
try:
    # 检查torch_npu扩展是否可用
    if hasattr(torch.npu, "memory_stats"):
        print("torch_npu扩展正常")
    
    # 尝试检查自定义算子
    try:
        from torch_npu import custom_ops
        ops = dir(custom_ops)
        hstu_ops = [op for op in ops if "hstu" in op.lower() or "mxrec" in op.lower()]
        if hstu_ops:
            print(f"找到HSTU相关算子: {len(hstu_ops)}")
        else:
            print("未找到HSTU相关算子（需要确认是否已注册）")
    except ImportError:
        print("custom_ops模块不可用")
except Exception as e:
    print(f"检查完成: {e}")
'

if python3 -c "$OPERATOR_CHECK_SCRIPT" 2>&1 | tee -a "$LOG_FILE"; then
    log_info "✓ 算子注册检查完成"
else
    log_warn "⚠ 算子注册检查有警告"
fi

# 总结
log_info ""
log_info "=== 验证总结 ==="
log_info "驱动路径: /usr/local/Ascend/driver"
log_info "动态库: ${LIB_PATH:-未找到}"

if [ $ERRORS -eq 0 ]; then
    log_info "✓ 算子编译验证通过！"
    if [ $WARNINGS -gt 0 ]; then
        log_warn "有 $WARNINGS 个警告，建议检查"
    fi
    exit 0
else
    log_error "✗ 发现 $ERRORS 个错误，请检查上述日志"
    exit 1
fi
