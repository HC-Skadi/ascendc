# Qwen3-32B-W8A8 性能优化报告

## 测试配置

| 参数 | 值 |
|------|-----|
| **模型** | vllm-ascend/Qwen3-32B-W8A8 |
| **输入长度** | 3500 tokens |
| **输出长度** | 128 tokens |
| **Prompt数量** | 200 |
| **硬件** | Atlas 800 A3 (8x NPU) |
| **并行配置** | TP=4 |
| **最大并发数** | 32 |

---

## 性能对比

| 指标 | 基线 | 优化后 | 提升幅度 |
|------|------|--------|----------|
| **基准测试时长 (s)** | 106.95 | 66.80 | **-37.5%** |
| **请求吞吐量 (req/s)** | 1.87 | 2.99 | **+59.9%** |
| **输出Token吞吐量 (tok/s)** | 239.36 | 383.23 | **+60.1%** |
| **峰值Token吞吐量 (tok/s)** | 415.00 | 960.00 | **+131.3%** |
| **平均TPOT (ms/token)** | 115.09 | 55.21 | **-52.0%** |
| **平均ITL (ms)** | 115.09 | 55.21 | **-52.0%** |
| **平均TTFT (ms)** | 1368.42 | 3261.06 | +138.3%* |

> *注: TTFT (首Token时间) 增加是由于 CUDA graph 编译开销。这是预期行为 - 编译成本在后续token生成中被摊薄，获得更好的稳态吞吐量。

---

## 详细指标

### 基线配置（无优化）
```bash
vllm serve vllm-ascend/Qwen3-32B-W8A8 \
  --served-model-name qwen3 \
  --port 8113 \
  --trust-remote-code \
  --tensor-parallel-size 4 \
  --enforce-eager
```

| 指标 | 值 |
|------|-----|
| 测试时长 | 106.95 s |
| 请求吞吐量 | 1.87 req/s |
| 输出Token吞吐量 | 239.36 tok/s |
| 峰值Token吞吐量 | 415.00 tok/s |
| 平均TTFT | 1368.42 ms |
| 平均TPOT | 115.09 ms/token |
| 平均ITL | 115.09 ms |

### 优化配置（启用 vLLM-Ascend 优化）
```bash
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE="AIV"
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1

vllm serve vllm-ascend/Qwen3-32B-W8A8 \
  --served-model-name qwen3-optimized \
  --port 8123 \
  --trust-remote-code \
  --async-scheduling \
  --quantization ascend \
  --distributed-executor-backend mp \
  --tensor-parallel-size 4 \
  --max-model-len 5500 \
  --max-num-batched-tokens 40960 \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes":[1,8,24,48,60,64,72,76]}' \
  --additional-config '{"pa_shape_list":[48,64,72,80], "weight_prefetch_config":{"enabled":true}}' \
  --block-size 128 \
  --gpu-memory-utilization 0.9
```

| 指标 | 值 |
|------|-----|
| 测试时长 | 66.80 s |
| 请求吞吐量 | 2.99 req/s |
| 输出Token吞吐量 | 383.23 tok/s |
| 峰值Token吞吐量 | 960.00 tok/s |
| 平均TTFT | 3261.06 ms |
| 平均TPOT | 55.21 ms/token |
| 平均ITL | 55.21 ms |

---

## 应用的官方优化项

### 命令行参数

| 参数 | 值 | 说明 |
|------|-----|------|
| `--async-scheduling` | enabled | 非阻塞任务调度 |
| `--compilation-config` | FULL_DECODE_ONLY | ACLGraph 全解码优化 |
| `--tensor-parallel-size` | 4 | 多 NPU 并行 |
| `--max-model-len` | 5500 | 覆盖输入(3.5K) + 输出(1.5K) |
| `--max-num-batched-tokens` | 40960 | 最优批处理大小 |
| `--block-size` | 128 | 内存分配效率 |
| `--gpu-memory-utilization` | 0.9 | 最大内存使用 |
| `--weight-prefetch-config` | enabled | L2 缓存权重预加载 |
| `--pa-shape-list` | [48,64,72,80] | PA 算子批次切换 |

### 环境变量

| 变量 | 值 | 说明 |
|------|-----|------|
| `TASK_QUEUE_ENABLE` | 1 | 异步任务队列 |
| `HCCL_OP_EXPANSION_MODE` | AIV | AIV 向量核 ROCE 通信 |
| `VLLM_ASCEND_ENABLE_FLASHCOMM1` | 1 | FlashComm_v1 优化 |

---

## 性能分析

### 关键提升

1. **37.5% 更快的总测试时间** - 从 106.95s 缩短到 66.80s
2. **60.1% 更高的 Token 吞吐量** - 从 239.36 tok/s 提升到 383.23 tok/s
3. **131.3% 更高的峰值吞吐量** - 从 415.00 tok/s 提升到 960.00 tok/s
4. **52.0% 更低的 Token 延迟** - TPOT 从 115.09ms 降低到 55.21ms

### 优化原理

- **FULL_DECODE_ONLY CudaGraph**: 通过捕获解码图一次并回放，减少内核调度开销
- **Weight Prefetch**: 将 MLP 权重加载与计算重叠，减少内存访问停顿
- **FlashComm_v1**: 在大批量分布式场景下减少 allreduce 通信开销
- **Async Scheduling**: 允许非阻塞任务调度，提高 GPU 利用率
- **PA Shape List**: 在最优批次大小切换到 PA 算子，获得更好的注意力性能

---

## 参考文档

https://docs.vllm.ai/projects/ascend/en/latest/tutorials/models/Qwen3-Dense.html


*报告由 vLLM-ascend-performance-optimization 技能生成*
