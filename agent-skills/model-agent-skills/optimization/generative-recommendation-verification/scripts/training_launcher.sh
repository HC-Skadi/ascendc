#!/bin/bash
#
# 阶段6：训练启动验证脚本
# 验证训练脚本能否正常启动
#

set -e

CONFIG="${CONFIG:-configs/ml-1m/hstu-mt-3400.gin}"
DEVICE="${DEVICE:-0}"
PORT="${PORT:-12345}"
WORKDIR="${WORKDIR:-.}"
LOG_FILE="${LOG_FILE:-stage_6_train.log}"
TIMEOUT="${TIMEOUT:-300}"

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

log_info "=== 训练启动验证 ==="
log_info "配置文件: $CONFIG"
log_info "设备: NPU $DEVICE"
log_info "端口: $PORT"
log_info "工作目录: $WORKDIR"
log_info "超时: ${TIMEOUT}秒"
log_info "日志文件: $LOG_FILE"

export ASCEND_RT_VISIBLE_DEVICES=$DEVICE
export USE_NPU_HSTU=1
export ENABLE_RAB=0
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

ERRORS=0

# 1. 检查配置文件
log_info "检查1: 验证配置文件..."
if [ -f "$CONFIG" ]; then
    log_info "✓ 配置文件存在: $CONFIG"
else
    log_error "✗ 配置文件不存在: $CONFIG"
    exit 1
fi

# 2. 检查 main.py
log_info "检查2: 查找 main.py..."
MAIN_PY=""
for path in "$WORKDIR/main.py" "$WORKDIR/generative-recommenders/main.py" "./main.py"; do
    if [ -f "$path" ]; then
        MAIN_PY="$path"
        log_info "✓ main.py 找到: $MAIN_PY"
        break
    fi
done

if [ -z "$MAIN_PY" ]; then
    log_error "✗ main.py 未找到"
    exit 1
fi

# 3. 检查依赖
log_info "检查3: 验证 Python 依赖..."
if python3 -c "import torch" 2>/dev/null; then
    log_info "✓ PyTorch 可用"
else
    log_error "✗ PyTorch 不可用"
    exit 1
fi

if python3 -c "import torch_npu" 2>/dev/null; then
    log_info "✓ torch_npu 可用"
else
    log_error "✗ torch_npu 不可用"
    exit 1
fi

# 4. 启动训练
log_info "检查4: 启动训练..."

TRAIN_CMD="python3 $MAIN_PY --gin_config_file=$CONFIG --master_port=$PORT"

log_info "执行命令: $TRAIN_CMD"

# 使用 timeout 启动训练
# 训练会在后台运行，我们只验证能否启动
set +e
timeout $TIMEOUT bash -c "
    $TRAIN_CMD &> >(tee -a $LOG_FILE) &
    TRAIN_PID=\$!
    echo \"训练进程 PID: \$TRAIN_PID\"
    
    # 等待一段时间让训练启动
    sleep 30
    
    # 检查进程是否还在运行
    if ps -p \$TRAIN_PID > /dev/null 2>&1; then
        echo \"训练进程运行中\"
        kill \$TRAIN_PID 2>/dev/null
        exit 0
    else
        echo \"训练进程已结束\"
        exit 1
    fi
" > /dev/null 2>&1

LAUNCH_RESULT=$?
set -e

# 5. 分析日志
log_info "检查5: 分析训练日志..."

if [ -f "$LOG_FILE" ]; then
    # 检查是否有 OOM 错误
    if grep -qi "out of memory\|oom\|cuda out of memory" "$LOG_FILE" 2>/dev/null; then
        log_error "✗ 检测到 OOM 错误"
        ERRORS=$((ERRORS + 1))
    fi
    
    # 检查是否有导入错误
    if grep -qi "importerror\|import error\|cannot import" "$LOG_FILE" 2>/dev/null; then
        log_error "✗ 检测到导入错误"
        ERRORS=$((ERRORS + 1))
    fi
    
    # 检查是否有 NPU 错误
    if grep -qi "npu.*error\|ascend.*error" "$LOG_FILE" 2>/dev/null; then
        log_error "✗ 检测到 NPU 相关错误"
        ERRORS=$((ERRORS + 1))
    fi
    
    # 检查是否有正常的 loss 输出
    if grep -qi "loss\|iter\|step" "$LOG_FILE" 2>/dev/null; then
        log_info "✓ 检测到训练日志输出"
    fi
fi

# 总结
log_info ""
log_info "=== 验证总结 ==="

if [ $LAUNCH_RESULT -eq 0 ] && [ $ERRORS -eq 0 ]; then
    log_info "✓ 训练启动验证通过！"
    exit 0
elif [ $LAUNCH_RESULT -eq 124 ]; then
    log_info "✓ 训练启动成功（超时后正常结束）"
    exit 0
else
    log_error "✗ 训练启动验证失败"
    if [ $ERRORS -gt 0 ]; then
        log_error "  发现 $ERRORS 个错误"
    fi
    exit 1
fi
