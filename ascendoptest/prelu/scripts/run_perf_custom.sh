#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SUITE_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
ASCENDOPTEST_DIR=$(cd "${SUITE_DIR}/.." && pwd)

export ASCEND_CUSTOM_OPP_PATH="/usr/local/Ascend/cann-9.0.0-beta.2/opp/vendors/prelu_custom"
export LD_LIBRARY_PATH="${ASCEND_CUSTOM_OPP_PATH}/op_api/lib:${LD_LIBRARY_PATH:-}"

case_args=()
if [[ "${1:-}" == "-n" ]]; then
    case_args=("-n" "${2:?error: -n requires a case name argument}")
fi

python3 "${ASCENDOPTEST_DIR}/run_test.py" \
  -i "${SUITE_DIR}/prototypes/prelu_custom.json" \
  -c "${SUITE_DIR}/cases/prelu_custom_cases.json" \
  -a "${SUITE_DIR}/aclnn_custom_perf" \
  --op-path "${ASCEND_CUSTOM_OPP_PATH}/op_api" \
  --op-type custom \
  --msprof \
  --op \
  -d "${SUITE_DIR}/prof/custom" \
  --build \
  # "${case_args[@]+"${case_args[@]}"}"
