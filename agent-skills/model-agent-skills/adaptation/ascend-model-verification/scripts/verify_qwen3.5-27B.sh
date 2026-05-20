#!/bin/bash
set -e

HOST="${HOST:-localhost}"
PORT="${PORT:-8000}"
MODEL_NAME="${MODEL_NAME:-qwen3.5}"
TIMEOUT="${TIMEOUT:-60}"

API_URL="http://${HOST}:${PORT}/v1/completions"

declare -a TEST_PROMPTS=(
    "The future of AI is"
    "What is machine learning?"
    "Hello, how are you?"
)

echo "=========================================="
echo "  Qwen3.5-27B 功能验证"
echo "=========================================="
echo "服务地址: ${API_URL}"
echo ""

echo "[1/3] 检查服务状态..."
if curl -sf http://${HOST}:${PORT}/v1/models > /dev/null 2>&1; then
    echo "✅ 服务就绪"
else
    echo "❌ 服务未就绪，请先启动 vLLM 服务"
    exit 1
fi

echo ""
echo "[2/3] 获取模型信息..."
MODELS=$(curl -sf http://${HOST}:${PORT}/v1/models 2>&1)
echo "可用模型: ${MODELS}"

echo ""
echo "[3/3] 执行功能测试..."
PASSED=0
TOTAL=${#TEST_PROMPTS[@]}

for PROMPT in "${TEST_PROMPTS[@]}"; do
    echo "----------------------------------------"
    echo "测试: '${PROMPT}'"
    
    RESPONSE=$(curl -sf -X POST "${API_URL}" \
        -H "Content-Type: application/json" \
        -d "{\"model\":\"${MODEL_NAME}\",\"prompt\":\"${PROMPT}\",\"max_completion_tokens\":50,\"temperature\":0}" \
        --max-time ${TIMEOUT} 2>&1)
    
    if [ $? -eq 0 ] && echo "${RESPONSE}" | grep -q '"choices"'; then
        echo "✅ 通过"
        PASSED=$((PASSED + 1))
    else
        echo "❌ 失败"
    fi
done

echo ""
echo "=========================================="
echo "  验证结果: ${PASSED}/${TOTAL} 通过"
echo "=========================================="

[ ${PASSED} -eq ${TOTAL} ] && exit 0 || exit 1