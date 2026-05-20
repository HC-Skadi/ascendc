# 昇腾模型适配验证工具

## 目录

- [概述](#概述)
- [功能特性](#功能特性)
- [系统要求](#系统要求)
- [快速开始](#快速开始)
- [详细使用指南](#详细使用指南)
- [脚本说明](#脚本说明)
- [参数配置](#参数配置)
- [输出报告](#输出报告)
- [常见问题](#常见问题)

---

## 概述

昇腾模型适配验证工具（Ascend Model Verification）是一款基于 vLLM-Ascend 后端的自动化验证流水线，专为华为昇腾 NPU 设备设计。该工具能够自动完成模型在昇腾硬件上的部署验证、精度测试和性能评估，并生成结构化的验证报告。

### 适用场景

- 在 Atlas 800 A2/A3 等昇腾设备上部署大语言模型
- 验证模型部署后的推理功能是否正常
- 在 GSM8K、C-Eval、MMLU 等数据集上评估模型精度
- 对模型服务进行在线吞吐、延迟、离线吞吐等性能基准测试
- 生成标准化的模型适配验证报告

---

## 功能特性

| 功能 | 说明 |
|------|------|
| **环境预检** | 自动检查 NPU 驱动、vLLM 安装状态、昇腾设备可用性 |
| **模型部署** | 一键启动 vLLM API 服务器，支持量化、TP、编译配置 |
| **功能验证** | 通过 curl 调用验证模型推理是否正常工作 |
| **精度评估** | 集成 AISBench，支持 GSM8K、C-Eval、MMLU 等数据集 |
| **性能测试** | 支持 serve/latency/throughput 三种基准测试模式 |
| **资源清理** | 验证完成后自动停止服务进程 |
| **报告生成** | 输出 JSON 格式的结构化验证报告 |

---

## 系统要求

### 硬件要求

| 组件 | 要求 |
|------|------|
| NPU 设备 | Atlas 800 A2 (64G×8) 或 Atlas 800 A3 (64G×16) |
| 内存 | 建议 64GB 以上 |
| 存储 | 建议 100GB 以上可用空间 |

### 软件要求

| 软件 | 版本/说明 |
|------|----------|
| Python | 3.8+ |
| vLLM-Ascend | v0.17.0rc1+ |
| AISBench | 用于精度评估（可选） |
| npu-smi | 昇腾设备管理工具 |

---

## 快速开始

### 方式一：使用 Python 验证编排器（推荐）

```bash
# 安装依赖
pip install vllm-ascend

# 运行验证
python validator.py \
  --model-path Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --model-name qwen3.5 \
  --quantized \
  --port 8000 \
  --tp-size 2
```

### 方式二：分步执行脚本

```bash
# 1. 启动服务
./serve_qwen3.5-27B.sh

# 2. 功能验证
./verify_qwen3.5-27B.sh

# 3. 精度评估
DATASET=gsm8k ./eval_qwen3.5-27B_accuracy.sh

# 4. 性能测试
BENCH_MODE=serve ./eval_qwen3.5-27B_perf.sh
```

---

## 详细使用指南

### 第一步：环境预检

运行验证前，请确保环境满足以下条件：

```bash
# 检查 NPU 设备
npu-smi info

# 检查 vLLM 安装
pip list | grep vllm
```

预期输出：
- `npu-smi info` 应显示昇腾设备信息
- `pip list` 应包含 `vllm` 或 `vllm-ascend`

### 第二步：模型服务部署

#### 使用量化模型（推荐）

```bash
export VLLM_USE_MODELSCOPE=true
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_BUFFSIZE=512

vllm serve Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 2 \
  --quantization ascend \
  --max-model-len 133000 \
  --gpu-memory-utilization 0.90 \
  --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
  --async-scheduling
```

#### 使用 BF16 模型（无量化）

```bash
vllm serve Qwen/Qwen3.5-27B \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 2 \
  --max-model-len 133000 \
  --gpu-memory-utilization 0.90
```

### 第三步：功能验证

服务启动后，可通过以下命令验证功能：

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

正常响应应包含 `choices` 字段和生成的文本。

### 第四步：精度评估

#### 安装 AISBench

```bash
git clone https://gitee.com/aisbench/benchmark.git /tmp/aisbench
cd /tmp/aisbench
pip install -e ./
pip install -r requirements/api.txt
pip install -r requirements/extra.txt
```

#### 下载数据集

```bash
# GSM8K 数据集
cd /tmp/aisbench/datasets
wget http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/gsm8k.zip
unzip gsm8k.zip && rm gsm8k.zip
```

#### 运行评估

```bash
ais_bench \
  --models /path/to/vllm_api_config.py \
  --datasets demo_gsm8k.py \
  --mode all \
  --dump-eval-details \
  --merge-ds
```

### 第五步：性能基准测试

#### serve 模式（在线吞吐）

测试在线服务吞吐量，包括 QPS、TTFT（首 Token 时间）、TPOT（Token 输出时间）。

```bash
vllm bench serve \
  --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --dataset-name random \
  --random-input 200 \
  --num-prompts 200 \
  --request-rate 1 \
  --save-result \
  --result-dir ./perf_results
```

#### latency 模式（延迟）

测试单批请求的延迟指标，包括 P50、P90、P99。

```bash
vllm bench latency \
  --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --input-len 200 \
  --output-len 200 \
  --num-iterations 10
```

#### throughput 模式（离线吞吐）

测试离线推理吞吐量。

```bash
vllm bench throughput \
  --model Eco-Tech/Qwen3.5-27B-w8a8-mtp \
  --input-len 200 \
  --output-len 200 \
  --num-batches 16
```

---

## 脚本说明

| 脚本 | 功能 | 适用场景 |
|------|------|----------|
| `validator.py` | Python 验证编排器，一键执行完整验证流程 | 快速验证，推荐使用 |
| `serve_qwen3.5-27B.sh` | Qwen3.5-27B 模型服务启动 | 单独部署服务 |
| `verify_qwen3.5-27B.sh` | 功能验证脚本 | 快速验证服务是否正常 |
| `eval_qwen3.5-27B_accuracy.sh` | AISBench 精度评估 | 评估模型精度 |
| `eval_qwen3.5-27B_perf.sh` | vllm bench 性能测试 | 评估模型性能 |

### validator.py 命令行参数

```bash
python validator.py \
  --model-path STRING              # 模型路径（必需）
  --model-name STRING             # 模型名称，默认 "Qwen3.5-27B"
  --hardware-type STRING          # 硬件类型，默认 "Atlas 800 A2"
  --quantized                     # 使用量化模型
  --port INT                      # 服务端口，默认 8000
  --tp-size INT                   # Tensor 并行大小，默认 2
  --max-model-len INT             # 最大上下文长度，默认 133000
  --gpu-mem-util FLOAT           # GPU 内存利用率，默认 0.90
  --run-accuracy                  # 执行精度测试，默认 True
  --perf-tests [serve latency throughput]  # 性能测试类型
  --report-path STRING            # 报告输出路径，默认 "./validation_report.json"
```

---

## 参数配置

### vLLM 服务参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--tensor-parallel-size` | 2 | Tensor 并行大小，A2 建议 2，A3 可选 4/8 |
| `--data-parallel-size` | 1 | Data 并行大小 |
| `--max-model-len` | 133000 | 最大上下文长度（128k） |
| `--max-num-seqs` | 32 | 每 DP 组最大并发请求数 |
| `--max-num-batched-tokens` | 8096 | 单步最大处理 tokens 数 |
| `--gpu-memory-utilization` | 0.90 | HBM 利用率，建议 0.85-0.90 |
| `--quantization` | ascend | 量化方式，启用量化时使用 |
| `--compilation-config` | FULL_DECODE_ONLY | 图编译模式，推荐 FULL_DECODE_ONLY |

### 性能测试参数

| 参数 | serve 模式 | latency 模式 | throughput 模式 |
|------|-----------|--------------|-----------------|
| `--random-input` | 200 | - | - |
| `--num-prompts` | 200 | - | - |
| `--request-rate` | 1 | - | - |
| `--input-len` | - | 200 | 200 |
| `--output-len` | - | 200 | 200 |
| `--num-iterations` | - | 10 | - |
| `--num-batches` | - | - | 16 |

---

## 输出报告

验证完成后，工具会在指定路径生成 JSON 格式的验证报告：

```json
{
  "success": true,
  "summary": "验证完成，耗时 320.5 秒",
  "detailed_report": {
    "environment_check": {
      "npu_smi": true,
      "vllm_installed": true,
      "vllm_version": "v0.17.0rc1",
      "npu_devices": 8
    },
    "accuracy_evaluation": {
      "dataset": "gsm8k",
      "accuracy": 96.74,
      "status": "passed"
    },
    "performance_benchmarks": {
      "serve": {
        "qps": 45.2,
        "ttft_ms": 120,
        "tpot_ms": 35,
        "status": "passed"
      },
      "latency": {
        "p50_ms": 85,
        "p90_ms": 150,
        "p99_ms": 220,
        "status": "passed"
      },
      "throughput": {
        "tokens_per_sec": 1250,
        "status": "passed"
      }
    },
    "functionality_test": {
      "passed": 3,
      "failed": 0,
      "status": "passed"
    },
    "logs": [
      "[2026-03-30 12:00:00] [INFO] Step 1: 环境预检",
      "[2026-03-30 12:00:05] [INFO] ✅ npu-smi 正常可用, 检测到 8 个 NPU 设备",
      "[2026-03-30 12:00:10] [INFO] ✅ vLLM 已安装: vllm-ascend v0.17.0rc1"
    ]
  },
  "report_path": "./validation_report.json",
  "metadata": {
    "model_name": "Qwen3.5-27B-w8a8",
    "hardware_type": "Atlas 800 A2",
    "is_quantized": true,
    "duration_seconds": 320.5,
    "timestamp": "2026-03-30T12:00:00"
  }
}
```

### 报告字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `success` | boolean | 整体验证是否成功 |
| `summary` | string | 人类可读的摘要信息 |
| `detailed_report` | object | 详细报告内容 |
| `detailed_report.environment_check` | object | 环境检查结果 |
| `detailed_report.accuracy_evaluation` | object | 精度评估结果 |
| `detailed_report.performance_benchmarks` | object | 性能测试结果 |
| `detailed_report.functionality_test` | object | 功能测试结果 |
| `detailed_report.logs` | array | 执行日志 |
| `report_path` | string | 报告文件路径 |
| `metadata` | object | 附加元数据 |

---

## 常见问题

### Q1: 服务启动超时怎么办？

**可能原因：**
- 模型下载时间过长（建议提前下载到本地）
- NPU 资源被占用
- 图编译首次运行需要 warmup

**解决方案：**
1. 提前下载模型到本地目录
2. 检查 NPU 使用情况：`npu-smi info`
3. 增加启动超时时间
4. 首次运行建议使用 `--enforce-eager` 禁用图编译

### Q2: 精度评估结果低于预期怎么办？

**可能原因：**
- 温度参数设置不当
- 数据集版本不一致
- 模型权重损坏

**解决方案：**
1. 检查 AISBench 配置中的 temperature、top_p 等参数
2. 确保使用正确的数据集版本
3. 验证模型权重完整性

### Q3: 性能测试 QPS 较低怎么优化？

**可优化方向：**
1. 调整 `--tensor-parallel-size`（增加并行度）
2. 调整 `--gpu-memory-utilization`（提高内存利用率）
3. 启用 `--async-scheduling`
4. 使用 `--compilation-config FULL_DECODE_ONLY`
5. 启用量化（`--quantization ascend`）

### Q4: 如何在多节点环境中运行？

**步骤：**
1. 在每个节点安装 vLLM-Ascend
2. 配置多节点通信（参考[官方文档](https://docs.vllm.ai/projects/ascend/en/latest/installation.html#verify-multi-node-communication)）
3. 修改启动命令中的 `--tensor-parallel-size` 和 `--data-parallel-size`

### Q5: 报告生成失败怎么办？

**检查：**
1. 确保输出目录有写入权限
2. 检查磁盘空间是否充足
3. 查看日志中的具体错误信息

---

## 参考文档

- [Qwen3.5-27B 部署教程](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3.5-27B.html)
- [AISBench 精度评估指南](https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/evaluation/using_ais_bench.html)
- [vLLM Benchmark 文档](https://docs.vllm.ai/en/latest/contributing/benchmarks.html)
- [vLLM-Ascend GitHub](https://github.com/vllm-project/vllm-ascend)

---

## 版本信息

- **工具版本**: 1.0.0
- **更新日期**: 2026-03-30
- **支持 vLLM-Ascend**: v0.17.0rc1+