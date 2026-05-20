#!/usr/bin/env bash
set -euo pipefail

# ============================================================================
#  run_perf_tail_shapes.sh
#  Batch performance test for 15 tail-shaped PReLU cases
#  (5 shapes × 3 dtypes, per-channel weight)
#
#  Usage:
#    bash run_perf_tail_shapes.sh                # full run (generate + perf + report)
#    bash run_perf_tail_shapes.sh --skip-build   # skip compilation/deployment
#    bash run_perf_tail_shapes.sh --skip-deploy  # skip only deployment
#    bash run_perf_tail_shapes.sh --custom-only  # only run custom perf (no builtin)
#    bash run_perf_tail_shapes.sh --builtin-only # only run builtin perf (no custom)
#    bash run_perf_tail_shapes.sh --report-only  # only regenerate report from cached data
# ============================================================================

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
SUITE_DIR=$(cd "${SCRIPT_DIR}/.." && pwd)
OPS_NN_DIR=/root/hc/ops-prelu/codex/ops-nn

# --- Parse flags ---
SKIP_BUILD=false
SKIP_DEPLOY=false
CUSTOM_ONLY=false
BUILTIN_ONLY=false
REPORT_ONLY=false

for arg in "$@"; do
    case "$arg" in
        --skip-build)  SKIP_BUILD=true ;;
        --skip-deploy) SKIP_DEPLOY=true ;;
        --custom-only) CUSTOM_ONLY=true ;;
        --builtin-only) BUILTIN_ONLY=true ;;
        --report-only) REPORT_ONLY=true ;;
        *) echo "Unknown option: $arg"; exit 1 ;;
    esac
done

# # ============================================================================
# #  Step 0: Build & Deploy (unless skipped)
# # ============================================================================
# if [[ "$REPORT_ONLY" == false && "$SKIP_BUILD" == false ]]; then
#     echo ""
#     echo "========================================================================"
#     echo "  Step 0: Compile PReLU operator"
#     echo "========================================================================"
#     cd "${OPS_NN_DIR}"
#     bash build.sh --pkg --soc=ascend910b --ops=prelu --experimental --vendor_name=prelu -j16
# fi

# if [[ "$REPORT_ONLY" == false && "$SKIP_DEPLOY" == false ]]; then
#     echo ""
#     echo "========================================================================"
#     echo "  Step 0: Deploy operator"
#     echo "========================================================================"
#     cd "${OPS_NN_DIR}"
#     ls build_out/cann-ops-nn-custom_linux-aarch64.run 2>/dev/null && \
#         ./build_out/cann-ops-nn-custom_linux-aarch64.run
# fi

if [[ "$REPORT_ONLY" == true ]]; then
    echo ""
    echo "========================================================================"
    echo "  Step 0: Skip build/deploy (--report-only), regenerating report..."
    echo "========================================================================"
fi

# ============================================================================
#  Step 1: Generate the 15 test cases (custom + builtin JSON)
# ============================================================================
if [[ "$REPORT_ONLY" == false ]]; then
    echo ""
    echo "========================================================================"
    echo "  Step 1: Generate 15 tail-shape test cases"
    echo "========================================================================"
    cd "${SUITE_DIR}"
    python3 "${SCRIPT_DIR}/gen_tail_perf_cases.py"
fi

# ============================================================================
#  Step 2: Run custom perf
# ============================================================================
if [[ "$REPORT_ONLY" == false && "$BUILTIN_ONLY" == false ]]; then
    echo ""
    echo "========================================================================"
    echo "  Step 2: Custom operator performance test (15 cases)"
    echo "========================================================================"
    cd "${SUITE_DIR}"
    bash "${SCRIPT_DIR}/run_perf_custom.sh"
fi

# ============================================================================
#  Step 3: Run builtin perf (hides custom OPP temporarily)
# ============================================================================
if [[ "$REPORT_ONLY" == false && "$CUSTOM_ONLY" == false ]]; then
    echo ""
    echo "========================================================================"
    echo "  Step 3: Builtin operator baseline performance test (15 cases)"
    echo "========================================================================"
    cd "${SUITE_DIR}"
    bash "${SCRIPT_DIR}/run_perf_builtin.sh"
fi

# ============================================================================
#  Step 4: Generate comparison report
# ============================================================================
echo ""
echo "========================================================================"
echo "  Step 4: Generate performance comparison report"
echo "========================================================================"
cd "${SUITE_DIR}"
bash "${SCRIPT_DIR}/report_perf.sh"

echo ""
echo "========================================================================"
echo "  Done! Report: ${SUITE_DIR}/prof/report/all_prof.csv"
echo "========================================================================"
