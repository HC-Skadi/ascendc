# vLLM Ascend 模型部署示例

> 本文档提供各主流模型在昇腾NPU上的部署示例
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 支持的模型

vLLM Ascend 支持以下主流模型架构:

- **Qwen系列**: Qwen2.5, Qwen3, Qwen-VL
- **DeepSeek系列**: DeepSeek-V3, DeepSeek-R1
- **Llama系列**: Llama2, Llama3
- **其他**: 任何支持HuggingFace格式的模型

## Qwen 系列部署

### Qwen2.5-7B 单卡部署

```bash
#!/bin/sh

# 设置环境和模型路径
export ASCEND_RT_VISIBLE_DEVICES=0
export MODEL_PATH="Qwen/Qwen2.5-7B-Instruct"

# 启动服务
vllm serve ${MODEL_PATH} \
    --host 0.0.0.0 \
    --port 8000 \
    --served-model-name qwen-2.5-7b-instruct \
    --trust-remote-code \
    --max-model-len 32768
```

### Qwen3-32B 多卡部署

```bash
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1

vllm serve /model/Qwen3-32B-W8A8 \
    --served-model-name qwen3 \
    --trust-remote-code \
    --async-scheduling \
    --quantization ascend \
    --distributed-executor-backend mp \
    --tensor-parallel-size 4 \
    --max-model-len 5500 \
    --max-num-batched-tokens 40960 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --additional-config '{"pa_shape_list":[48,64,72,80], "weight_prefetch_config":{"enabled":true}}' \
    --port 8113 \
    --block-size 128 \
    --gpu-memory-utilization 0.9
```

### Qwen3-235B-A22B 大规模部署

```bash
vllm serve vllm-ascend/Qwen3-235B-A22B-w8a8 \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 8 \
    --data-parallel-size 8 \
    --data-parallel-size-local 4 \
    --data-parallel-start-rank 4 \
    --data-parallel-address decode_node_1_ip \
    --data-parallel-rpc-port decode_node_dp_port \
    --seed 1024 \
    --quantization ascend \
    --served-model-name qwen3 \
    --max-num-seqs 128 \
    --max-model-len 40960 \
    --max-num-batched-tokens 256 \
    --enable-expert-parallel \
    --trust-remote-code \
    --gpu-memory-utilization 0.9 \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
    --async-scheduling \
    --no-enable-prefix-caching \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
      "kv_role": "kv_consumer",
      "kv_port": "30100",
      "engine_id": "1",
      "kv_connector_extra_config": {
          "use_ascend_direct": true,
          "prefill": {"dp_size": 2, "tp_size": 8},
          "decode": {"dp_size": 8, "tp_size": 4}
      }}'
```

## DeepSeek 系列部署

### DeepSeek-V3.1 部署

```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

vllm serve /weights/DeepSeek-V3.1-w8a8-mtp-QuaRot \
    --host 0.0.0.0 \
    --port 8015 \
    --data-parallel-size 4 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --seed 1024 \
    --served-model-name deepseek_v3 \
    --enable-expert-parallel \
    --async-scheduling \
    --max-num-seqs 16 \
    --max-model-len 16384 \
    --max-num-batched-tokens 4096 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.92 \
    --speculative-config '{"num_speculative_tokens": 3, "method": "mtp"}' \
    --compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```

### DeepSeek-R1 部署

```bash
vllm serve vllm-ascend/DeepSeek-R1-W8A8 \
    --host 0.0.0.0 \
    --port 8006 \
    --tensor-parallel-size 8 \
    --enable-expert-parallel \
    --seed 1024 \
    --served-model-name deepseek_r1 \
    --max-model-len 17000 \
    --max-num-batched-tokens 16384 \
    --trust-remote-code \
    --max-num-seqs 4 \
    --gpu-memory-utilization 0.9 \
    --quantization ascend \
    --speculative-config '{"num_speculative_tokens": 1, "method":"deepseek_mtp"}' \
    --enforce-eager \
    --kv-transfer-config \
    '{"kv_connector": "MooncakeConnectorV1",
      "kv_buffer_device": "npu",
      "kv_role": "kv_producer",
      "kv_parallel_size": "1",
      "kv_port": "20001",
      "engine_id": "0"
    }' \
    --additional-config '{"enable_weight_nz_layout":true,"enable_prefill_optimizations":true}'
```

## 离线推理示例

### 基础离线推理

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=40)

llm = LLM(
    model="/model/Qwen3-32B-W8A8",
    tensor_parallel_size=4,
    trust_remote_code=True,
    max_model_len=5500,
    quantization="ascend"
)

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(f"Prompt: {output.prompt!r}")
    print(f"Generated: {output.outputs[0].text!r}")
```

### 量化模型推理

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="/path/to/your/quantized_model",
    max_model_len=4096,
    trust_remote_code=True,
    tensor_parallel_size=2,
    data_parallel_size=1,
    port=8000,
    served_model_name="quantized_model",
    quantization="ascend"
)

outputs = llm.generate(prompts, sampling_params)
```

## API服务部署

### 启动API Server

```bash
python -m vllm.entrypoints.api_server \
    --model /path/to/your/quantized_model \
    --max-model-len 4096 \
    --port 8000 \
    --tensor-parallel-size 2 \
    --data-parallel-size 1 \
    --served-model-name quantized_model \
    --trust-remote-code \
    --quantization ascend
```

### OpenAI兼容API

vLLM提供OpenAI兼容的API接口:

```bash
# 基础调用
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen-2.5-7b",
        "prompt": "Hello,",
        "max_tokens": 100
    }'

# 流式调用
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen-2.5-7b",
        "prompt": "Hello,",
        "max_tokens": 100,
        "stream": true
    }'
```

## 多模态模型部署

### Qwen2.5-VL 部署

```bash
vllm serve Qwen/Qwen2.5-VL-7B-Instruct \
    --host 0.0.0.0 \
    --port 13700 \
    --no-enable-prefix-caching \
    --tensor-parallel-size 1 \
    --seed 1024 \
    --served-model-name qwen25vl \
    --max-model-len 40000 \
    --max-num-batched-tokens 40000 \
    --trust-remote-code \
    --gpu-memory-utilization 0.9
```

## 性能调优参数

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| tensor_parallel_size | 张量并行度 | 根据卡数 |
| max_model_len | 最大序列长度 | 根据模型 |
| max_num_batched_tokens | 最大批处理token | 根据内存 |
| gpu_memory_utilization | GPU内存利用率 | 0.9 |
| quantization | 量化方法 | ascend |

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
