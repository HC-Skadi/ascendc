#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SUITE_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
ASCENDOPTEST_DIR=$(cd "${SUITE_DIR}/.." && pwd)

REPORT_DIR="${SUITE_DIR}/prof/report"
CUSTOM_DIR="${SUITE_DIR}/prof/custom"
BUILTIN_DIR="${SUITE_DIR}/prof/builtin"

CASES_FILE="${SUITE_DIR}/cases/prelu_custom_cases.json"
if [[ "${1:-}" == "-f" ]]; then
    CASES_FILE="${2:?error: -f requires a cases file path}"
fi

python3 "${ASCENDOPTEST_DIR}/scripts/get_prof.py" \
  -c "${CUSTOM_DIR}" \
  -b "${BUILTIN_DIR}" \
  -f "${CASES_FILE}" \
  -d "${REPORT_DIR}"

python3 "${SUITE_DIR}/scripts/check_perf_vs_builtin.py" \
  --csv "${REPORT_DIR}/all_prof.csv"
