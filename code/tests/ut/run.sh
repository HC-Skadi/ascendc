#!/bin/bash
# prelu 算子 UT 测试执行脚本

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/build"
CLEAN_BUILD=true

echo "========================================"
echo "prelu 算子 UT 测试"
echo "========================================"

if [ -z "${ASCEND_HOME_PATH:-}" ]; then
    if [ -d "/usr/local/Ascend/cann-9.0.0-beta.2" ]; then
        export ASCEND_HOME_PATH=/usr/local/Ascend/cann-9.0.0-beta.2
    else
        export ASCEND_HOME_PATH=/usr/local/Ascend/cann
    fi
fi

if [ ! -d "${ASCEND_HOME_PATH}" ]; then
    echo "ERROR: ASCEND_HOME_PATH does not exist: ${ASCEND_HOME_PATH}"
    echo "Please set ASCEND_HOME_PATH, for example:"
    echo "  export ASCEND_HOME_PATH=/usr/local/Ascend/cann-9.0.0-beta.2"
    exit 1
fi

if [ -f "${ASCEND_HOME_PATH}/set_env.sh" ]; then
    # shellcheck disable=SC1090
    source "${ASCEND_HOME_PATH}/set_env.sh"
else
    echo "WARN: ${ASCEND_HOME_PATH}/set_env.sh not found, continue with current environment."
fi

export LD_LIBRARY_PATH=${ASCEND_HOME_PATH}/lib64:${LD_LIBRARY_PATH:-}

if command -v nproc >/dev/null 2>&1; then
    JOBS="$(nproc)"
else
    JOBS="$(sysctl -n hw.ncpu 2>/dev/null || echo 4)"
fi

if [ "$CLEAN_BUILD" = true ]; then
    rm -rf "${BUILD_DIR}"
fi

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"
cmake ..
make -j"${JOBS}"

echo "========================================"
echo "执行 UT 测试"
echo "========================================"

FAILED_TESTS=()
PASSED_TESTS=()

cd "${BUILD_DIR}/op_host"
if ./prelu_op_host_ut; then
    PASSED_TESTS+=("op_host")
else
    FAILED_TESTS+=("op_host")
fi

# 生成测试数据
echo "========================================"
echo "生成 Kernel UT 测试数据"
echo "========================================"
DATA_DIR="${SCRIPT_DIR}/op_kernel/prelu_data"
cd "${DATA_DIR}"
python3 gen_data.py

# 运行 Kernel UT
cd "${BUILD_DIR}/op_kernel"
if ./prelu_op_kernel_ut; then
    PASSED_TESTS+=("op_kernel")
else
    FAILED_TESTS+=("op_kernel")
fi

# 精度比对
echo "========================================"
echo "精度比对"
echo "========================================"
cd "${DATA_DIR}"
python3 compare_data.py
if [ $? -eq 0 ]; then
    echo "精度比对通过"
else
    FAILED_TESTS+=("precision_check")
fi

if [ -d "${BUILD_DIR}/../../../op_api" ]; then
    cd "${BUILD_DIR}/op_api"
    if ./prelu_op_api_ut; then
        PASSED_TESTS+=("op_api")
    else
        FAILED_TESTS+=("op_api")
    fi
fi

echo "========================================"
echo "测试结果汇总"
echo "========================================"

if [ ${#FAILED_TESTS[@]} -gt 0 ]; then
    echo "失败的测试: ${FAILED_TESTS[@]}"
    exit 1
else
    echo "所有测试通过"
    exit 0
fi
