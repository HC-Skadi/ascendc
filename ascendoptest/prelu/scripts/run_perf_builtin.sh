#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SUITE_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
ASCENDOPTEST_DIR=$(cd "${SUITE_DIR}/.." && pwd)
VENDORS_DIR="/usr/local/Ascend/cann-9.0.0-beta.2/opp/vendors"
CUSTOMIZE_DIR="${VENDORS_DIR}/prelu_custom"
CUSTOMIZE_BACKUP_DIR="${VENDORS_DIR}/prelu_nn.__builtin_perf_backup__"

case_args=()
if [[ "${1:-}" == "-n" ]]; then
    case_args=("-n" "${2:?error: -n requires a case name argument}")
fi

restore_customize_dir() {
  if [[ -d "${CUSTOMIZE_BACKUP_DIR}" && ! -e "${CUSTOMIZE_DIR}" ]]; then
    mv "${CUSTOMIZE_BACKUP_DIR}" "${CUSTOMIZE_DIR}"
  fi
}

trap restore_customize_dir EXIT

if [[ -e "${CUSTOMIZE_BACKUP_DIR}" ]]; then
  echo "Found stale builtin perf backup: ${CUSTOMIZE_BACKUP_DIR}" >&2
  exit 1
fi

if [[ -d "${CUSTOMIZE_DIR}" ]]; then
  echo "Temporarily hiding deployed custom OPP to force builtin TBE baseline..."
  mv "${CUSTOMIZE_DIR}" "${CUSTOMIZE_BACKUP_DIR}"
fi

python3 "${ASCENDOPTEST_DIR}/run_test.py" \
  -i "${SUITE_DIR}/prototypes/prelu_builtin.json" \
  -c "${SUITE_DIR}/cases/prelu_builtin_cases.json" \
  -a "${SUITE_DIR}/aclnn_builtin_perf" \
  --op-type builtin \
  --msprof \
  --op \
  -d "${SUITE_DIR}/prof/builtin" \
  --build \
  -k PRelu \
  "${case_args[@]+"${case_args[@]}"}"
