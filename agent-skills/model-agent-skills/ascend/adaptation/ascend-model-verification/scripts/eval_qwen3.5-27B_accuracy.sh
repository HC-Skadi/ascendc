#!/bin/bash
set -e

MODEL_PATH="${MODEL_PATH:-Eco-Tech/Qwen3.5-27B-w8a8-mtp}"
MODEL_NAME="${MODEL_NAME:-qwen3.5}"
HOST="${HOST:-localhost}"
PORT="${PORT:-8000}"
DATASET="${DATASET:-gsm8k}"
AISBENCH_DIR="${AISBENCH_DIR:-/tmp/aisbench}"
DATASET_DIR="${AISBENCH_DIR}/datasets"

echo "=========================================="
echo "  Qwen3.5-27B 精度评估 (AISBench)"
echo "=========================================="
echo "数据集:     ${DATASET}"
echo "模型:       ${MODEL_NAME}"
echo "服务地址:   ${HOST}:${PORT}"
echo ""

echo "[1/4] 检查服务..."
if ! curl -sf http://${HOST}:${PORT}/v1/models > /dev/null 2>&1; then
    echo "❌ 服务未就绪"
    exit 1
fi
echo "✅ 服务就绪"

echo ""
echo "[2/4] 安装 AISBench..."
if [ ! -d "${AISBENCH_DIR}" ]; then
    git clone https://gitee.com/aisbench/benchmark.git ${AISBENCH_DIR}
    cd ${AISBENCH_DIR}
    pip install -e ./ --use-pep517
    pip install -r requirements/api.txt
    pip install -r requirements/extra.txt
fi

echo ""
echo "[3/4] 准备数据集..."
mkdir -p ${DATASET_DIR}

case "${DATASET}" in
    gsm8k)
        cd ${DATASET_DIR}
        [ ! -d "gsm8k" ] && wget -q http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/gsm8k.zip && unzip -q gsm8k.zip && rm gsm8k.zip
        DATASET_CONFIG="demo_gsm8k.py"
        ;;
    ceval)
        cd ${DATASET_DIR}/ceval/formal_ceval
        [ ! -f "ceval-exam.zip" ] && wget -q https://www.modelscope.cn/datasets/opencompass/ceval-exam/resolve/master/ceval-exam.zip && unzip -q ceval-exam.zip && rm ceval-exam.zip
        DATASET_CONFIG="ceval_gen_0_shot_cot_chat_prompt.py"
        ;;
    mmlu)
        cd ${DATASET_DIR}
        [ ! -d "mmlu" ] && wget -q http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/mmlu.zip && unzip -q mmlu.zip && rm mmlu.zip
        DATASET_CONFIG="mmlu_gen_0_shot_cot_chat_prompt.py"
        ;;
    *)
        echo "❌ 不支持的数据集: ${DATASET}"
        exit 1
        ;;
esac
echo "✅ 数据集已准备"

echo ""
echo "[4/4] 运行评估..."
CONFIG_FILE="/tmp/vllm_qwen35_eval_config.py"
cat > ${CONFIG_FILE} << EOF
from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.model_postprocessors import extract_non_reasoning_content

models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr='vllm-api-qwen35',
        path="${MODEL_PATH}",
        model="${MODEL_NAME}",
        request_rate=0,
        retry=2,
        host_ip="${HOST}",
        host_port=${PORT},
        max_out_len=1024,
        batch_size=1,
        trust_remote_code=False,
        generation_kwargs=dict(
            temperature=0.6,
            top_k=10,
            top_p=0.95,
            seed=None,
            repetition_penalty=1.03,
        ),
        pred_postprocessor=dict(type=extract_non_reasoning_content)
    )
]
EOF

cd ${AISBENCH_DIR}
ais_bench --models ${CONFIG_FILE} --datasets ${DATASET_CONFIG} --mode all --dump-eval-details --merge-ds

echo ""
echo "=========================================="
echo "  评估完成"
echo "=========================================="
echo "结果目录: ${AISBENCH_DIR}/outputs/"