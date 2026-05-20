# vLLM-Ascend 性能优化技能

## 概述

`vllm-ascend-performance-optimization` 是一个交互式技能，用于分析用户在昇腾硬件上的 vLLM 部署配置，并基于实际案例研究提供定制化优化建议。

**技能位置：** `/root/.config/opencode/skills/vllm-ascend-performance-optimization/`

---

## 如何使用此技能

### 触发条件

当您说以下内容时，技能会自动触发：

- "优化 Ascend 上的 vLLM"
- "提升 NPU 上的推理性能"
- "优化 vLLM-Ascend 吞吐量"
- "降低 Ascend 硬件上的 TPOT 延迟"
- 或者分享您的 vLLM 启动脚本并请求优化建议

### 使用流程

#### 第一步：回答问题

技能会通过交互式问卷收集以下信息：

1. **模型信息**
   - 模型名称和参数量（如 Qwen3-32B、DeepSeek-V3、GLM-5）
   - 量化格式（w8a8、w4a16、fp16）
   - MoE 还是 Dense 架构

2. **硬件配置**
   - Ascend 910/NPU 设备数量
   - Tensor Parallel (TP) 策略
   - Expert Parallel (EP) 如果是 MoE
   - Data Parallel (DP) 如果使用

3. **性能场景**
   - 主要目标：吞吐量 (QPS) 还是延迟 (TPOT/TTFT)
   - 输入/输出长度特性（最大序列长度）
   - 并发需求

4. **当前脚本**
   - 请分享您当前的 vLLM 启动脚本或命令行
   - 技能会提取现有优化参数

#### 第二步：分析与匹配

技能会分析您的脚本，并与参考文档库进行匹配：
- `Qwen3-Dense-optimization.md` - Dense 模型优化
- `DeepSeek-MoE-optimization.md` - MoE 特定优化
- `PD-separation-optimization.md` - Prefill-Decode 分离调优
- `communication-optimization.md` - HCCL、FlashComm、EP 优化
- `memory-optimization.md` - KV cache、注意力掩码压缩
- `scheduling-optimization.md` - 分块 prefill、异步调度

#### 第三步：生成优化报告

技能会生成结构化报告，包含：
- 当前配置分析
- 按优先级排序的优化建议（含具体数据）
- 修改后的完整启动命令
- 验证步骤

---

## 优化参数快速参考

### 高优先级优化（优先启用）

| 类别 | 参数 | 适用场景 |
|-----|------|---------|
| 异步调度 | `--async-scheduling` | 所有场景，降低调度开销 |
| 图编译 | `--compilation-config FULL_DECODE_ONLY` | Decode 密集型工作负载 |
| FlashComm1 | `VLLM_ASCEND_ENABLE_FLASHCOMM1=1` | EP 并行配置 |
| 分块 Prefill | `--enable-chunked-prefill` | 长输入序列 |
| MoE 多流 | `VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1` | MoE 模型 |
| MLA 多流 | `VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1` | DeepSeek MLA 注意力 |

### 中优先级优化

| 类别 | 参数 | 适用场景 |
|-----|------|---------|
| 动态量化 | MoE gate 移至 allgather 前 | EP 并行 |
| 权重预取 | 上下文权重加载 | 内存带宽受限 |
| 注意力掩码压缩 | `--ascend-use-norm-compress-mask` | 长序列 |
| HCCL Buffer 调优 | 动态 HCCL_BUFFERSIZE 计算 | 多节点部署 |

---

## Qwen3-32B Dense 模型优化案例

### 实测性能数据

**基线配置（无优化）：**
- 吞吐量：239.36 tok/s
- TPOT：115.09 ms
- 基准测试时长：106.95s

**优化配置：**
- 吞吐量：383.23 tok/s（+60.1%）
- TPOT：55.21 ms（-52%）
- 基准测试时长：66.80s（-37.5%）

**硬件：** 8x Ascend 910 NPU，TP=4，w8a8 量化

### 关键优化项

| 优化项 | 参数 | 效果 |
|-------|------|------|
| 异步调度 | `--async-scheduling` | 调度开销降低 15-20% |
| 图编译 | `--compilation-config FULL_DECODE_ONLY` | TorchDynamo guard 开销降低 ~3ms |
| Block Size | `--block-size 16` | KV cache 分配效率提升 |
| 批量 Token 数 | `--max-num-batched-tokens 8192` | 更大批量提升吞吐 |

### 推荐启动命令

```bash
python -m vllm.entrypoints.openai.api_server \
    --model Qwen3-32B \
    --tensor-parallel-size 4 \
    --quantization w8a8 \
    --async-scheduling \
    --compilation-config FULL_DECODE_ONLY \
    --block-size 16 \
    --max-num-batched-tokens 8192 \
    --device ascend \
    --dtype float16
```

---

## DeepSeek MoE 模型优化案例

### 目标模型
- DeepSeek-V3
- DeepSeek-R1
- Qwen3-30B-A3B

### 关键优化

#### 1. FlashComm1 通信优化
```bash
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
```
**效果：**
- 单层延迟：8.0ms → 7.0ms（降低 12.5%）
- 整网延迟降低：~2.5ms

#### 2. Gate DP（量化前置通信）
```bash
export VLLM_ASCEND_ENABLE_GATEDP=1
```
**效果：**
- hidden_states 通信量降低 50%
- Gate 计算从 674us 优化

#### 3. GroupedMatmulSwigluQuant 融合
**效果：**
- TPOT 降低 4-5ms（DP32 EP32，24batch）

#### 4. 多流并行
```bash
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1  # MLA
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1  # MoE
```
**效果：**
- TPOT 共降低 ~6ms

#### 5. 权重预取
**效果：** 额外 TPOT 降低 ~1ms

### 性能提升路径

| 配置 | 吞吐量 |
|------|--------|
| TP8 DP2 EP16（基线） | 0.73 qps/节点 |
| + FlashComm1 | 0.85 qps/节点 |
| + GateDP + 融合 | 1.2 qps/节点 |
| + 多流 | 1.5 qps/节点 |
| 完整优化（PD 4P1D） | 1.8 qps/节点 |

### 推荐环境变量

```bash
# 核心 MoE 优化
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_GATEDP=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1

# 通信优化
export HCCL_OP_EXPANSION_MODE=AIV

# 内存优化
export HCCL_BUFFSIZE=<计算值>
```

---

## Prefill-Decode 分离优化

### 何时使用 PD 分离

当以下情况时 PD 分离有益：
- TTFT（首 Token 时间）关键
- 高并发混合输入长度
- 吞吐量目标 >1.5 qps/节点

### 性能目标

| 场景 | P 节点 | D 节点 | 目标 QPS | TTFT | TPOT |
|------|--------|--------|---------|------|------|
| 4k 输入，1.5k 输出 | 1P1D | 16卡 P，32卡 D | 2.25 | <2s | <100ms |
| DeepSeek-R1 | 7P1D | - | 608 QPM | <2s | <50ms |

### Prefill 优化

1. **FlashComm1**：单层 8ms → 7ms
2. **Micro-Batch 流水线**：计算通信重叠
3. **InitRouting V2**：MoE 初始化优化，3647us → 1747us
4. **FA 算子优化**：延迟 574ms → 538ms

### Decode 优化

1. **GroupedMatmulSwigluQuant 融合**：TPOT 降低 4-5ms
2. **多流 + 权重预取**：TPOT 降低 ~7ms

---

## 通信优化指南

### FlashComm1

将 AllReduce 替换为 ReduceScatter + AllGather 模式：

```
原始：AllReduce（全量数据）
优化：ReduceScatter（1/TP 数据）→ 计算 → AllGather（1/TP 数据）
```

**效果：** 通信量降低 1/TP 倍

### HCCL Buffer 动态计算

```bash
HCCL_BUFFSIZE = CEIL(2 × (BS × epWorldSize × min(local_expert_num/epWorldSize, K) × H × sizeof(uint16) / (1024×1024) + 2))
```

**参数：**
- BS：每卡 batch size
- epWorldSize：EP 通信域大小
- local_expert_num：本地专家数
- K：Top-K 专家数
- H：隐藏层大小

**收益：**
- 避免内存浪费
- 防止 AIV 模式缓冲区溢出
- 每 16 卡节点节省 ~6GB

---

## 内存优化指南

### 注意力掩码压缩

**问题：** 32k 序列需要 ~2GB 存储掩码

**解决方案：**
```bash
--ascend-use-norm-compress-mask
```
**效果：** 32k 序列节省 ~2GB

### 路由专家序列分块

**问题：** MoE 路由时内存峰值高达 4096MB

**解决方案：** 分块处理（如每块 8k tokens）

**效果：** 4096MB → 1360MB（节省 67%）

### KV Cache 优化

```bash
--gpu-memory-utilization 0.85  # 推荐值：0.85-0.95
```

---

## 调度优化指南

### 异步调度
```bash
--async-scheduling
```
**效果：** 延迟降低 10-15%，吞吐提升 15-20%

### 分块 Prefill
```bash
--enable-chunked-prefill
--max-num-batched-tokens 8192
```
**效果：**
- 峰值内存降低
- TTFT 更一致
- 更好利用 GPU

### 关键调度参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| `--max-num-batched-tokens` | 8192 | 平衡吞吐和延迟 |
| `--max-num-seqs` | 256 | 匹配并发需求 |
| `--block-size` | 16 | 短序列效率更高 |

---

## 输出格式

技能始终提供：

1. **执行摘要** - 按影响力排序的前 3 个优化
2. **详细建议** - 所有适用优化
3. **修改后的脚本** - 完整的可运行命令
4. **预期性能范围** - 基于案例研究数据
5. **风险提示** - 任何权衡或注意事项

---

## 快速命令生成器

### Dense 模型（Qwen3-32B）
```bash
python -m vllm.entrypoints.openai.api_server \
    --model <模型路径> \
    --tensor-parallel-size 4 \
    --quantization w8a8 \
    --async-scheduling \
    --compilation-config FULL_DECODE_ONLY \
    --block-size 16 \
    --max-num-batched-tokens 8192 \
    --device ascend
```

### MoE 模型（DeepSeek-V3/R1）
```bash
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1
export HCCL_OP_EXPANSION_MODE=AIV

python -m vllm.entrypoints.openai.api_server \
    --model <模型路径> \
    --tensor-parallel-size 8 \
    --num-expert-parallel 16 \
    --quantization fp8 \
    --async-scheduling \
    --device ascend
```

### 长序列优化
```bash
--enable-chunked-prefill \
--ascend-use-norm-compress-mask \
--max-seq-len-to-capture 32768 \
--gpu-memory-utilization 0.85
```

---

## 文件结构

```
vllm-ascend-performance-optimization/
├── SKILL.md                          # 主技能文件
└── reference/
    ├── Qwen3-Dense-optimization.md   # Dense 模型基准数据
    ├── DeepSeek-MoE-optimization.md  # MoE 特定优化
    ├── PD-separation-optimization.md # PD 分离调优
    ├── communication-optimization.md # 通信优化
    ├── memory-optimization.md        # 内存优化
    └── scheduling-optimization.md    # 调度优化
```

---

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 吞吐低但 TPOT 好 | 调度开销大 | 启用异步调度 |
| 长序列 OOM | KV cache 太小 | 降低 gpu-memory-utilization 或启用掩码压缩 |
| TTFT 高但 TPOT 低 | Prefill 瓶颈 | 启用分块 prefill |
| MoE 专家负载不均 | 路由不均衡 | 启用 OmniPlacement |
| 多并发时 TPOT 上升 | 资源竞争 | 启用多流并行和权重预取 |

---

## 联系我们

如有问题，请提供：
1. 您的模型配置
2. 当前启动脚本
3. 性能测试结果
4. 遇到的具体问题

技能将基于实际案例数据为您提供定制化建议。
