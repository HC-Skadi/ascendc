#!/bin/bash
set -e

export BASE_PATH=$(
  cd "$(dirname $0)"
  pwd
)
export BUILD_PATH="${BASE_PATH}/build"
export BUILD_OUT_PATH="${BASE_PATH}/build_out"

if [ -z "${ASCEND_HOME_PATH:-}" ]; then
  if [ -d "/usr/local/Ascend/cann-9.0.0-beta.2" ]; then
    export ASCEND_HOME_PATH="/usr/local/Ascend/cann-9.0.0-beta.2"
  else
    export ASCEND_HOME_PATH="/usr/local/Ascend/cann"
  fi
fi

if [ ! -d "${ASCEND_HOME_PATH}" ]; then
  echo "[ERROR] ASCEND_HOME_PATH does not exist: ${ASCEND_HOME_PATH}"
  echo "[ERROR] Please set ASCEND_HOME_PATH, for example:"
  echo "        export ASCEND_HOME_PATH=/usr/local/Ascend/cann-9.0.0-beta.2"
  exit 1
fi

if [ -f "${ASCEND_HOME_PATH}/set_env.sh" ]; then
  # shellcheck disable=SC1090
  source "${ASCEND_HOME_PATH}/set_env.sh"
else
  echo "[WARN] ${ASCEND_HOME_PATH}/set_env.sh not found, continue with current environment."
fi

if command -v nproc >/dev/null 2>&1; then
  CORE_NUMS=$(nproc)
elif command -v sysctl >/dev/null 2>&1; then
  CORE_NUMS=$(sysctl -n hw.ncpu 2>/dev/null || echo 8)
else
  CORE_NUMS=8
fi
if [ ${CORE_NUMS} -gt 8 ]; then
  CORE_NUMS=8
fi

usage() {
  echo "Build script for prelu operator"
  echo "Usage: bash build.sh [OPTIONS]"
  echo ""
  echo "Options:"
  echo "  -h, --help              Print this help message"
  echo "  -j[n]                   Compile thread nums, default is ${CORE_NUMS}, eg: -j8"
  echo "  --make_clean            Clean build artifacts"
  echo "  -u, --ut                Run UT (Unit Tests)"
  echo "  -e, --example           Run examples (requires NPU)"
  echo ""
  echo "Examples:"
  echo "  bash build.sh           # Build with default soc (ascend910b)"
  echo "  bash build.sh -j8       # Build with 8 threads"
  echo "  bash build.sh --make_clean"
  echo "  bash build.sh -u        # Run UT tests"
  echo "  bash build.sh -e        # Run aclnn example (requires NPU)"
}

clean_build() {
  if [ -d "${BUILD_PATH}" ]; then
    echo "Cleaning build directory..."
    rm -rf ${BUILD_PATH}/*
  fi
}

clean_build_out() {
  if [ -d "${BUILD_OUT_PATH}" ]; then
    echo "Cleaning build_out directory..."
    rm -rf ${BUILD_OUT_PATH}/*
  fi
}

THREAD_NUM=${CORE_NUMS}
COMPUTE_UNIT="ascend910b"
ENABLE_CLEAN=FALSE
RUN_UT=FALSE
RUN_EXAMPLE=FALSE

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    -j*)
      THREAD_NUM="${1:2}"
      if [ -z "$THREAD_NUM" ]; then
        THREAD_NUM=${CORE_NUMS}
      fi
      shift
      ;;
    -u|--ut)
      RUN_UT=true
      shift
      ;;
    -e|--example)
      RUN_EXAMPLE=true
      shift
      ;;
    --make_clean)
      ENABLE_CLEAN=TRUE
      shift
      ;;
    -*)
      echo "[ERROR] Invalid option: $1"
      usage
      exit 1
      ;;
    *)
      echo "[ERROR] Unexpected argument: $1"
      usage
      exit 1
      ;;
  esac
done

if [ "$ENABLE_CLEAN" = "TRUE" ]; then
  clean_build
  clean_build_out
  exit 0
fi

if [ "$RUN_UT" = true ]; then
  echo "[INFO] Running UT tests..."
  cd "${BASE_PATH}/tests/ut"
  ./run.sh
  UT_RESULT=$?
  if [ $UT_RESULT -ne 0 ]; then
    echo "[ERROR] UT tests failed"
    exit 1
  fi
  echo "[INFO] UT tests passed!"
  exit 0
fi

CMAKE_ARGS="-DASCEND_COMPUTE_UNIT=$COMPUTE_UNIT"

if [ ! -d "${BUILD_PATH}" ]; then
  mkdir -p "${BUILD_PATH}"
fi

[ -f "${BUILD_PATH}/CMakeCache.txt" ] && rm -f ${BUILD_PATH}/CMakeCache.txt

echo "----------------------------------------------------------------"
echo "[INFO] Configuring project..."
echo "[INFO] CMAKE_ARGS: ${CMAKE_ARGS}"
echo "[INFO] ASCEND_HOME_PATH: ${ASCEND_HOME_PATH}"
cd "${BUILD_PATH}" && cmake ${CMAKE_ARGS} ..

echo "----------------------------------------------------------------"
echo "[INFO] Building project with ${THREAD_NUM} threads..."
cmake --build . --target all binary package -- -j ${THREAD_NUM}

KERNEL_O=$(find ${BUILD_PATH}/op_kernel/ascendc_kernels/binary/${COMPUTE_UNIT} -name "*.o" 2>/dev/null | head -1)
if [ -z "$KERNEL_O" ]; then
    echo "[ERROR] Kernel binary not found"
    exit 1
fi

PKG_PATH=$(ls "${BUILD_PATH}"/custom_opp_*.run 2>/dev/null | head -n 1)
if [ -z "$PKG_PATH" ] || [ ! -f "$PKG_PATH" ] || [ ! -s "$PKG_PATH" ]; then
    echo "[ERROR] Package not found or empty"
    exit 1
fi

echo "----------------------------------------------------------------"
echo "[INFO] Build completed successfully!"
echo "[INFO] Kernel binary: ${KERNEL_O}"
echo "[INFO] Package: ${PKG_PATH}"

if [ "$RUN_EXAMPLE" = true ]; then
  echo "----------------------------------------------------------------"
  echo "[INFO] Running examples..."
  cd "${BASE_PATH}/examples"
  ./run.sh
  EXAMPLE_RESULT=$?
  cd - > /dev/null
  if [ $EXAMPLE_RESULT -ne 0 ]; then
    echo "[ERROR] Example execution failed"
    exit 1
  fi
  echo "[INFO] Example completed successfully!"
fi
