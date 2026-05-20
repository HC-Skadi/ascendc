---
name: ascend-model-verification
description: 昇腾模型适配验证 (Ascend Model Adaptation Verification) - 自动化验证华为昇腾设备上 vLLM-Ascend 模型部署、精度与性能的一站式工具。当用户提及在昇腾 NPU (Atlas 800 A2/A3) 上部署大语言模型、验证模型精度、运行性能基准测试、生成验证报告、或需要一键式模型适配验证时，使用此 Skill。它封装了完整验证流水线：环境检查、模型服务部署、精度测试、性能基准测试、资源清理与报告生成。适用于 Qwen3.5-27B、DeepSeek-V3 等 vLLM-Ascend 支持的模型。
---

# 昇腾模型适配验证 (Ascend Model Adaptation Verification)

基于 vLLM-Ascend 后端的自动化验证流水线，用于验证大语言模型在华为昇腾 NPU 设备上的部署、精度与性能表现。

## 核心流程

```
1. 环境预检 ──→ 2. 模型部署 ──→ 3. 执行验证 ──→ 4. 资源清理 ──→ 5. 生成报告
```

---

## 输入参数

Skill 接收以下 JSON 格式配置参数：

```json
{
  "model_path": "/models/Qwen3.5-27B-w8a8",
  "model_name": "Qwen3.5-27B-w8a8",
  "hardware_type": "Atlas 800 A2",
  "is_quantized": true,
  "vllm_server_config": {
    "host": "0.0.0.0",
    "port": 8000,
    "tensor_parallel_size": 2,
    "max_model_len": 133000,
    "gpu_memory_utilization": 0.90,
    "compilation_config": {"cudagraph_mode": "FULL_DECODE_ONLY"}
  },
  "benchmark_config": {
    "input_len": 200,
    "num_prompts": 200,
    "request_rate": 1
  },
  "run_accuracy_test": true,
  "run_performance_tests": ["serve", "latency", "throughput"]
}
```

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model_path` | string | ✅ | 模型权重路径 |
| `model_name` | string | ❌ | 模型标识，默认 "Qwen3.5-27B" |
| `hardware_type` | string | ❌ | 硬件类型，默认 "Atlas 800 A2" |
| `is_quantized` | boolean | ❌ | 是否量化，默认 true |
| `vllm_server_config` | object | ❌ | vLLM 服务器配置 |
| `benchmark_config` | object | ❌ | 性能测试配置 |
| `run_accuracy_test` | boolean | ❌ | 是否执行精度测试，默认 true |
| `run_performance_tests` | array | ❌ | 性能测试类型 ["serve", "latency", "throughput"] |

---

## 验证步骤

### Step 1: 环境预检

执行以下检查：

```bash
npu-smi info
pip list | grep vllm
```

检查项：
- NPU 驱动是否正常
- vLLM-Ascend 是否已安装
- 昇腾设备是否可用

### Step 2: 模型服务部署

根据配置启动临时 vLLM API 服务器：

```bash
vllm serve {model_path} \
  --host {host} \
  --port {port} \
  --tensor-parallel-size {tp_size} \
  --max-model-len {max_model_len} \
  --gpu-memory-utilization {gpu_mem_util} \
  --quantization ascend \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --async-scheduling
```

**量化配置：** 若 `is_quantized=true`，添加 `--quantization ascend` 参数。

### Step 3: 执行验证测试

#### 3.1 精度验证

使用 AISBench 在指定数据集（如 GSM8K）上运行推理：

```bash
ais_bench --models vllm_api_config.py --datasets gsm8k.py --mode all --dump-eval-details --merge-ds
```

输出指标：准确率 (accuracy)

#### 3.2 性能基准测试

使用 `vllm bench` 执行三种模式测试：

| 模式 | 说明 | 关键指标 |
|------|------|----------|
| `serve` | 在线吞吐测试 | QPS, TTFT, TPOT |
| `latency` | 单请求延迟测试 | P50/P90/P99 延迟 |
| `throughput` | 离线吞吐测试 | tokens/sec |

```bash
# serve 模式
vllm bench serve --model {model} --dataset-name random --random-input 200 --num-prompts 200 --request-rate 1 --save-result

# latency 模式
vllm bench latency --model {model} --input-len 200 --output-len 200 --num-iterations 10

# throughput 模式
vllm bench throughput --model {model} --input-len 200 --output-len 200 --num-batches 16
```

### Step 4: 资源清理

验证完成后自动停止服务进程：

```bash
pkill -f "vllm serve"
```

### Step 5: 生成验证报告

输出结构化 JSON 报告：

```json
{
  "success": true,
  "summary": "验证完成，耗时 320.5 秒",
  "detailed_report": {
    "environment_check": {
      "npu_smi": true,
      "vllm_installed": true,
      "version": "v0.17.0rc1"
    },
    "accuracy_evaluation": {
      "dataset": "gsm8k",
      "accuracy": 96.74,
      "status": "passed"
    },
    "performance_benchmarks": {
      "serve": {"qps": 45.2, "ttft_ms": 120, "tpot_ms": 35},
      "latency": {"p50_ms": 85, "p90_ms": 150, "p99_ms": 220},
      "throughput": {"tokens_per_sec": 1250}
    },
    "logs": ["步骤1完成", "服务启动成功", "精度测试通过"]
  },
  "report_path": "./validation_report.json"
}
```

---

## 输出格式

| 字段 | 类型 | 说明 |
|------|------|------|
| `success` | boolean | 整个流程是否成功 |
| `summary` | string | 人类可读的结果摘要 |
| `detailed_report` | object | 详细测试结果 |
| `detailed_report.environment_check` | object | 环境检查结果 |
| `detailed_report.accuracy_evaluation` | object | 精度测试结果 |
| `detailed_report.performance_benchmarks` | object | 性能测试结果 |
| `detailed_report.logs` | array | 关键步骤日志 |
| `report_path` | string | 报告文件路径 |

---

## 错误处理

- **环境检查失败**：记录错误信息，直接返回失败报告
- **服务启动失败**：捕获异常，尝试清理进程，报告失败原因
- **API 调用超时**：设置 60 秒超时，自动重试 2 次
- **测试执行失败**：记录失败环节，继续执行后续测试（可选）

---

## 参考脚本

| 脚本 | 功能 |
|------|------|
| `scripts/validator.py` | Python 验证编排器（推荐） |
| `scripts/start_server.sh` | vLLM 服务启动脚本 |
| `scripts/run_accuracy.sh` | 精度评估脚本 |
| `scripts/run_perf.sh` | 性能基准测试脚本 |

### 快速使用

```bash
python scripts/validator.py \
  --model-path Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --model-name qwen3.5 \
  --quantized \
  --port 8000 \
  --tp-size 2
```

---

## Qwen3.5-27B 参考实现

基于 [Qwen3.5-27B 官方部署教程](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.5-27B.html) 的参考脚本：

### Qwen3.5-27B 服务启动

```bash
# 环境变量
export VLLM_USE_MODELSCOPE=true
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_BUFFSIZE=512
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export TASK_QUEUE_ENABLE=1

# 启动命令
vllm serve Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --host 0.0.0.0 \
  --port 8000 \
  --data-parallel-size 1 \
  --tensor-parallel-size 2 \
  --seed 1024 \
  --quantization ascend \
  --served-model-name qwen3.5 \
  --max-num-seqs 32 \
  --max-model-len 133000 \
  --max-num-batched-tokens 8096 \
  --trust-remote-code \
  --gpu-memory-utilization 0.90 \
  --no-enable-prefix-caching \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --additional-config '{"enable_cpu_binding":true}' \
  --async-scheduling
```

### 关键参数说明

| 参数 | 值 | 说明 |
|------|-----|------|
| `--tensor-parallel-size` | 2 | Tensor 并行大小，A2 建议 2 |
| `--data-parallel-size` | 1 | Data 并行大小 |
| `--max-model-len` | 133000 | 最大上下文长度 (128k) |
| `--max-num-seqs` | 32 | 每 DP 组最大请求数 |
| `--max-num-batched-tokens` | 8096 | 单步最大处理 tokens |
| `--gpu-memory-utilization` | 0.90 | HBM 利用率 |
| `--quantization` | ascend | 启用 ascend 量化 |
| `--compilation-config` | FULL_DECODE_ONLY | 图编译模式 |

### 功能验证

```bash
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3.5",
        "prompt": "The future of AI is",
        "max_completion_tokens": 50,
        "temperature": 0
    }'
```

### 精度评估 (GSM8K 参考指标)

| 数据集 | 指标 | 参考值 |
|--------|------|--------|
| gsm8k | accuracy | 96.74 |

### 性能评估命令

```bash
# serve 模式 (在线吞吐)
vllm bench serve --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --dataset-name random \
  --random-input 200 \
  --num-prompts 200 \
  --request-rate 1 \
  --save-result \
  --result-dir ./

# latency 模式 (延迟)
vllm bench latency --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --input-len 200 \
  --output-len 200 \
  --num-iterations 10

# throughput 模式 (离线吞吐)
vllm bench throughput --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --input-len 200 \
  --output-len 200 \
  --num-batches 16
```

### Qwen3.5-27B 专用脚本

| 脚本 | 功能 |
|------|------|
| `scripts/serve_qwen3.5-27B.sh` | Qwen3.5-27B 服务启动 |
| `scripts/verify_qwen3.5-27B.sh` | Qwen3.5-27B 功能验证 |
| `scripts/eval_qwen3.5-27B_accuracy.sh` | Qwen3.5-27B 精度评估 |
| `scripts/eval_qwen3.5-27B_perf.sh` | Qwen3.5-27B 性能评估 |

---

## 参考文档

- [Qwen3.5-27B 部署教程](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.5-27B.html)
- [AISBench 精度评估](https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/evaluation/using_ais_bench.html)
- [vLLM Benchmark](https://docs.vllm.ai/en/latest/contributing/benchmarks.html)