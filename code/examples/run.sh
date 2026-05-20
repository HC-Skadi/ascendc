#!/bin/bash
# prelu 算子调用示例执行脚本

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/build"

echo "========================================"
echo "prelu 算子调用示例"
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

SET_ENV_FILE="${ASCEND_HOME_PATH}/set_env.sh"
if [ -f "${SET_ENV_FILE}" ]; then
    # shellcheck disable=SC1090
    source "${SET_ENV_FILE}"
else
    echo "WARN: ${SET_ENV_FILE} not found, continue with current environment."
fi

CUSTOM_VENDOR_PATH="${ASCEND_HOME_PATH}/opp/vendors/prelu_custom"
if [ ! -d "${CUSTOM_VENDOR_PATH}" ] && [ -d "/usr/local/Ascend/opp/vendors/prelu_custom" ]; then
    CUSTOM_VENDOR_PATH="/usr/local/Ascend/opp/vendors/prelu_custom"
fi

export ASCEND_OPP_PATH="${ASCEND_HOME_PATH}/opp:${ASCEND_OPP_PATH:-}"
if [ -d "${CUSTOM_VENDOR_PATH}" ]; then
    export ASCEND_OPP_PATH="$(dirname "$(dirname "${CUSTOM_VENDOR_PATH}")"):${ASCEND_OPP_PATH}"
    export LD_LIBRARY_PATH="${CUSTOM_VENDOR_PATH}/op_api/lib:${ASCEND_HOME_PATH}/lib64:${LD_LIBRARY_PATH:-}"
else
    echo "WARN: custom OPP vendor path not found: ${CUSTOM_VENDOR_PATH}"
    echo "      Please install the generated prelu_custom*.run package before running the example."
    export LD_LIBRARY_PATH="${ASCEND_HOME_PATH}/lib64:${LD_LIBRARY_PATH:-}"
fi

export ASCEND_SLOG_PRINT_TO_STDOUT="${ASCEND_SLOG_PRINT_TO_STDOUT:-1}"

if command -v nproc >/dev/null 2>&1; then
    JOBS="$(nproc)"
else
    JOBS="$(sysctl -n hw.ncpu 2>/dev/null || echo 4)"
fi

echo "ASCEND_HOME_PATH=${ASCEND_HOME_PATH}"
echo "ASCEND_OPP_PATH=${ASCEND_OPP_PATH}"
echo "CUSTOM_VENDOR_PATH=${CUSTOM_VENDOR_PATH}"

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"
cmake ..
make -j"${JOBS}"

echo "执行调用示例..."
cd bin
./test_aclnn_prelu

echo "========================================"
echo "执行完成"
echo "========================================"
