#!/bin/bash
#
# 阶段1：昇腾环境基础验证脚本
# 验证驱动目录、npu-smi命令、容器环境等信息
#

set -e

ASCEND_PATH="${ASCEND_PATH:-/usr/local/Ascend}"
LOG_FILE="${LOG_FILE:-stage_1_env.log}"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1" | tee -a "$LOG_FILE"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

check_result() {
    if [ $? -eq 0 ]; then
        log_info "$1"
        return 0
    else
        log_error "$2"
        return 1
    fi
}

log_info "=== 昇腾环境基础验证 ==="
log_info "驱动路径: $ASCEND_PATH"
log_info "日志文件: $LOG_FILE"

ERRORS=0

# 1. 检查驱动目录
log_info "检查1: 验证 Ascend 驱动目录..."
if [ -d "$ASCEND_PATH/driver" ]; then
    log_info "✓ Ascend驱动目录存在: $ASCEND_PATH/driver"
else
    log_error "✗ Ascend驱动目录不存在: $ASCEND_PATH/driver"
    ERRORS=$((ERRORS + 1))
fi

# 2. 检查 npu-smi 命令
log_info "检查2: 验证 npu-smi 命令..."
if command -v npu-smi &> /dev/null; then
    log_info "✓ npu-smi 命令可用"
    if npu-smi info &> /dev/null; then
        log_info "✓ npu-smi 可正常获取设备信息"
        npu-smi info | tee -a "$LOG_FILE"
    else
        log_warn "⚠ npu-smi 无法获取设备信息（可能无NPU）"
    fi
else
    log_error "✗ npu-smi 命令不可用"
    ERRORS=$((ERRORS + 1))
fi

# 3. 检查容器环境文件
log_info "检查3: 验证 Ascend 安装信息文件..."
if [ -f "/etc/ascend_install.info" ]; then
    log_info "✓ Ascend安装信息文件存在"
    cat /etc/ascend_install.info | tee -a "$LOG_FILE"
else
    log_warn "⚠ Ascend安装信息文件不存在（非容器环境？）"
fi

# 4. 检查 ASCEND_VISIBLE_DEVICES 环境变量
log_info "检查4: 验证 ASCEND_VISIBLE_DEVICES 环境变量..."
if [ -n "$ASCEND_VISIBLE_DEVICES" ]; then
    log_info "✓ ASCEND_VISIBLE_DEVICES 已设置: $ASCEND_VISIBLE_DEVICES"
else
    log_warn "⚠ ASCEND_VISIBLE_DEVICES 未设置（将使用默认值0）"
    export ASCEND_VISIBLE_DEVICES=0
    log_info "  已临时设置 ASCEND_VISIBLE_DEVICES=0"
fi

# 5. 检查 Ascend 组件目录
log_info "检查5: 验证 Ascend 组件目录..."
for component in "driver" "fw" "tools"; do
    if [ -d "$ASCEND_PATH/$component" ]; then
        log_info "✓ $ASCEND_PATH/$component 存在"
    else
        log_warn "⚠ $ASCEND_PATH/$component 不存在"
    fi
done

# 6. 检查 NPU 设备状态
log_info "检查6: 检查 NPU 设备状态..."
if command -v npu-smi &> /dev/null; then
    if npu-smi info -l &> /dev/null; then
        DEVICE_COUNT=$(npu-smi info -l | grep -c "NPU")
        log_info "✓ 检测到 $DEVICE_COUNT 个 NPU 设备"
    fi
fi

# 7. 检查 CANN 版本（如果可用）
log_info "检查7: 检查 CANN 版本..."
if [ -f "$ASCEND_PATH/Ascend/AscendCANN/latest/version.txt" ]; then
    CANN_VERSION=$(cat "$ASCEND_PATH/Ascend/AscendCANN/latest/version.txt" 2>/dev/null || echo "未知")
    log_info "✓ CANN 版本: $CANN_VERSION"
elif [ -d "$ASCEND_PATH/Ascend/AscendCANN" ]; then
    log_info "✓ AscendCANN 已安装"
else
    log_warn "⚠ CANN 版本信息不可用"
fi

# 总结
log_info ""
log_info "=== 验证总结 ==="
if [ $ERRORS -eq 0 ]; then
    log_info "✓ 所有检查通过！环境基础验证成功。"
    exit 0
else
    log_error "✗ 发现 $ERRORS 个错误，请检查上述日志。"
    exit 1
fi
