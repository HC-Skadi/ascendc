#!/bin/bash
set -e

MODEL_PATH="${MODEL_PATH:-Eco-Tech/Qwen3.5-27B-w8a8-mtp}"
MODEL_NAME="${MODEL_NAME:-qwen3.5}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
TP_SIZE="${TP_SIZE:-2}"
DP_SIZE="${DP_SIZE:-1}"
MAX_MODEL_LEN="${MAX_MODEL_LEN:-133000}"
MAX_NUM_SEQS="${MAX_NUM_SEQS:-32}"
GPU_MEM_UTIL="${GPU_MEM_UTIL:-0.90}"
QUANTIZATION="${QUANTIZATION:-ascend}"

export VLLM_USE_MODELSCOPE=true
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_BUFFSIZE=512
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1

CMD="vllm serve ${MODEL_PATH}"
CMD="${CMD} --host ${HOST}"
CMD="${CMD} --port ${PORT}"
CMD="${CMD} --data-parallel-size ${DP_SIZE}"
CMD="${CMD} --tensor-parallel-size ${TP_SIZE}"
CMD="${CMD} --seed 1024"
CMD="${CMD} --served-model-name ${MODEL_NAME}"
CMD="${CMD} --max-num-seqs ${MAX_NUM_SEQS}"
CMD="${CMD} --max-model-len ${MAX_MODEL_LEN}"
CMD="${CMD} --trust-remote-code"
CMD="${CMD} --gpu-memory-utilization ${GPU_MEM_UTIL}"
CMD="${CMD} --no-enable-prefix-caching"
CMD="${CMD} --compilation-config '{\"cudagraph_mode\":\"FULL_DECODE_ONLY\"}'"
CMD="${CMD} --additional-config '{\"enable_cpu_binding\":true}'"
CMD="${CMD} --async-scheduling"

if [ "${QUANTIZATION}" = "ascend" ]; then
    CMD="${CMD} --quantization ascend"
fi

echo "=========================================="
echo "  vLLM-Ascend 模型服务启动"
echo "=========================================="
echo "模型路径:     ${MODEL_PATH}"
echo "服务地址:     ${HOST}:${PORT}"
echo "TP size:     ${TP_SIZE}"
echo "DP size:     ${DP_SIZE}"
echo "最大上下文:   ${MAX_MODEL_LEN}"
echo "量化方式:     ${QUANTIZATION}"
echo "=========================================="

echo "启动服务中..."
eval ${CMD} &
SERVER_PID=$!

echo "服务 PID: ${SERVER_PID}"
echo "等待服务就绪..."

MAX_WAIT=300
WAIT_COUNT=0
while [ $WAIT_COUNT -lt $MAX_WAIT ]; do
    if curl -sf http://${HOST}:${PORT}/v1/models > /dev/null 2>&1; then
        echo "服务已就绪!"
        exit 0
    fi
    sleep 2
    WAIT_COUNT=$((WAIT_COUNT + 2))
    echo "等待中... (${WAIT_COUNT}s)"
done

echo "服务启动超时!"
kill ${SERVER_PID} 2>/dev/null || true
exit 1