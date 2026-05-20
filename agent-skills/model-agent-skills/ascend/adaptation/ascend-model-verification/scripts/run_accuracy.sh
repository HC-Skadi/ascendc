#!/bin/bash
set -e

DATASET="${DATASET:-gsm8k}"
MODEL_PATH="${MODEL_PATH:-Eco-Tech/Qwen3.5-27B-w8a8-mtp}"
MODEL_NAME="${MODEL_NAME:-qwen3.5}"
HOST="${HOST:-localhost}"
PORT="${PORT:-8000}"
AISBENCH_DIR="${AISBENCH_DIR:-/tmp/aisbench}"

echo "=========================================="
echo "  精度评估 (AISBench)"
echo "=========================================="
echo "数据集:     ${DATASET}"
echo "模型:       ${MODEL_NAME}"
echo "服务地址:   ${HOST}:${PORT}"

if ! curl -sf http://${HOST}:${PORT}/v1/models > /dev/null 2>&1; then
    echo "❌ 服务未就绪，请先启动 vLLM 服务"
    exit 1
fi
echo "✅ 服务就绪"

if [ ! -d "${AISBENCH_DIR}" ]; then
    echo "安装 AISBench..."
    git clone https://gitee.com/aisbench/benchmark.git ${AISBENCH_DIR}
    cd ${AISBENCH_DIR}
    pip install -e ./ --use-pep517
    pip install -r requirements/api.txt
    pip install -r requirements/extra.txt
fi

DATASET_DIR="${AISBENCH_DIR}/datasets"
mkdir -p ${DATASET_DIR}

case "${DATASET}" in
    gsm8k)
        cd ${DATASET_DIR}
        if [ ! -d "gsm8k" ]; then
            wget -q http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/gsm8k.zip
            unzip -q gsm8k.zip
            rm gsm8k.zip
        fi
        DATASET_CONFIG="demo_gsm8k.py"
        ;;
    ceval)
        cd ${DATASET_DIR}/ceval/formal_ceval
        if [ ! -f "ceval-exam.zip" ]; then
            wget -q https://www.modelscope.cn/datasets/opencompass/ceval-exam/resolve/master/ceval-exam.zip
            unzip -q ceval-exam.zip
            rm ceval-exam.zip
        fi
        DATASET_CONFIG="ceval_gen_0_shot_cot_chat_prompt.py"
        ;;
    mmlu)
        cd ${DATASET_DIR}
        if [ ! -d "mmlu" ]; then
            wget -q http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/mmlu.zip
            unzip -q mmlu.zip
            rm mmlu.zip
        fi
        DATASET_CONFIG="mmlu_gen_0_shot_cot_chat_prompt.py"
        ;;
    *)
        echo "❌ 不支持的数据集: ${DATASET}"
        exit 1
        ;;
esac

CONFIG_FILE="/tmp/vllm_api_eval_config.py"
cat > ${CONFIG_FILE} << EOF
from ais_bench.benchmark.models import VLLMCustomAPIChat
from ais_bench.benchmark.utils.model_postprocessors import extract_non_reasoning_content

models = [
    dict(
        attr="service",
        type=VLLMCustomAPIChat,
        abbr='vllm-api-eval',
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

echo "运行精度评估..."
ais_bench \
    --models ${CONFIG_FILE} \
    --datasets ${DATASET_CONFIG} \
    --mode all \
    --dump-eval-details \
    --merge-ds

echo ""
echo "=========================================="
echo "  评估完成"
echo "=========================================="
echo "结果目录: ${AISBENCH_DIR}/outputs/"