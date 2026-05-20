#!/bin/bash
set -e

MODEL_PATH="${MODEL_PATH:-Eco-Tech/Qwen3.5-27B-w8a8-mtp}"
BENCH_MODE="${BENCH_MODE:-serve}"
INPUT_LEN="${INPUT_LEN:-200}"
NUM_PROMPTS="${NUM_PROMPTS:-200}"
REQUEST_RATE="${REQUEST_RATE:-1}"
NUM_ITERATIONS="${NUM_ITERATIONS:-10}"
NUM_BATCHES="${NUM_BATCHES:-16}"
OUTPUT_LEN="${OUTPUT_LEN:-200}"
RESULT_DIR="${RESULT_DIR:-./perf_results}"

export VLLM_USE_MODELSCOPE=true

echo "=========================================="
echo "  性能基准测试"
echo "=========================================="
echo "模型:       ${MODEL_PATH}"
echo "模式:       ${BENCH_MODE}"

if ! command -v vllm &> /dev/null; then
    echo "❌ vllm 不可用"
    exit 1
fi

mkdir -p ${RESULT_DIR}

case "${BENCH_MODE}" in
    serve)
        CMD="vllm bench serve ${MODEL_PATH}"
        CMD="${CMD} --dataset-name random"
        CMD="${CMD} --random-input ${INPUT_LEN}"
        CMD="${CMD} --num-prompts ${NUM_PROMPTS}"
        CMD="${CMD} --request-rate ${REQUEST_RATE}"
        CMD="${CMD} --save-result"
        CMD="${CMD} --result-dir ${RESULT_DIR}"
        ;;
    latency)
        CMD="vllm bench latency ${MODEL_PATH}"
        CMD="${CMD} --input-len ${INPUT_LEN}"
        CMD="${CMD} --output-len ${OUTPUT_LEN}"
        CMD="${CMD} --num-iterations ${NUM_ITERATIONS}"
        ;;
    throughput)
        CMD="vllm bench throughput ${MODEL_PATH}"
        CMD="${CMD} --input-len ${INPUT_LEN}"
        CMD="${CMD} --output-len ${OUTPUT_LEN}"
        CMD="${CMD} --num-batches ${NUM_BATCHES}"
        ;;
    *)
        echo "❌ 不支持的模式: ${BENCH_MODE}"
        echo "支持的模式: serve, latency, throughput"
        exit 1
        ;;
esac

echo "执行命令: ${CMD}"
echo ""

eval ${CMD}

echo ""
echo "=========================================="
echo "  测试完成"
echo "=========================================="
echo "结果目录: ${RESULT_DIR}"