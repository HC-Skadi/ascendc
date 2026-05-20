---
name: vllm-ascend-performance-optimization
description: vLLM-Ascend performance tuning advisor for optimizing inference throughput and latency on Huawei Ascend hardware. Use when users want to optimize vLLM deployment on Ascend NPUs, improve model inference performance, reduce token latency, or maximize throughput on Ascend hardware. Triggers for queries like "optimize vLLM on Ascend", "improve inference performance on NPU", "tune vLLM-Ascend for better throughput", "reduce TPOT latency on Ascend hardware", or when users share vLLM startup scripts and want optimization recommendations.
---

# vLLM-Ascend Performance Optimization Advisor

An interactive skill that analyzes your vLLM deployment configuration on Ascend hardware and provides customized optimization recommendations based on proven case studies.

## Workflow

### Phase 1: Collect User Configuration

Use the `question` tool to gather deployment information:

**Must-ask questions:**

1. **Model Information**
   - Model name and size (e.g., Qwen3-32B, DeepSeek-V3, GLM-5)
   - Quantization format (w8a8, w4a16, fp16)
   - MoE vs Dense architecture

2. **Hardware Configuration**
   - Number of Ascend 910/NPU devices
   - Tensor Parallel (TP) strategy
   - Expert Parallel (EP) if MoE
   - Data Parallel (DP) if used

3. **Performance Scenario**
   - Primary goal: throughput (QPS) or latency (TPOT/TTFT)
   - Input/output length characteristics (max seq length)
   - Concurrency requirements

4. **Current Script**
   - Ask user to share their current vLLM startup script or command line
   - Extract existing optimization flags and parameters

### Phase 2: Analyze Script and Match Cases

Read reference documents from `./reference/` to find relevant optimization patterns:

- `Qwen3-Dense-optimization.md` - Dense model optimizations
- `DeepSeek-MoE-optimization.md` - MoE-specific optimizations  
- `PD-separation-optimization.md` - Prefill-Decode separation tuning
- `communication-optimization.md` - HCCL, FlashComm, EP optimizations
- `memory-optimization.md` - KV cache, attention mask compression
- `scheduling-optimization.md` - Chunked prefill, async scheduling

For each optimization found in user's script:
1. Check if already applied → note as "implemented"
2. Check if applicable but missing → add to recommendations
3. Note any potentially problematic settings

### Phase 3: Generate Optimization Report

Produce a structured report with:

```
## Current Configuration Analysis

### Detected Parameters
[Extract all vLLM flags from user's script]

### Performance Profile
- Model: {model}
- Hardware: {n} x Ascend {chip}
- Parallel Strategy: TP={tp}, EP={ep}, DP={dp}

## Optimization Recommendations

### 1. [Category] - [Impact: High/Medium]
**Current:** [what user has]
**Recommended:** [what to change]
**Expected Gain:** [quantified improvement from case studies]
**Reference:** [case study source with specific numbers]

### 2. ... (prioritized by impact)

## Modified Startup Command

[Full vLLM command with optimizations applied]

## Verification Steps

1. [Step to verify each optimization]
2. ...
```

### Phase 4: Explain Each Recommendation

For each recommendation:
- Explain WHY it helps (communication/computation/memory reason)
- Show specific numbers from case studies
- Provide the exact flag/command to add
- Warn about any prerequisites or trade-offs

## Optimization Categories Reference

### High-Impact Optimizations (Try First)

| Category | Flags | Applicable When |
|---------|-------|----------------|
| Async Scheduling | `--async-scheduling` | All scenarios, reduces scheduling overhead |
| Graph Compilation | `--compilation-config FULL_DECODE_ONLY` | Decode-heavy workloads |
| FlashComm1 | `VLLM_ASCEND_ENABLE_FLASHCOMM1=1` | EP parallel configurations |
| Chunked Prefill | `--enable-chunked-prefill` | Long input sequences |
| Multi-Stream MoE | `VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1` | MoE models |
| MLA Multi-Stream | `VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1` | DeepSeek MLA attention |

### Medium-Impact Optimizations

| Category | Flags | Applicable When |
|---------|-------|----------------|
| Dynamic Quantization | MoE gate before allgather | EP parallel |
| Weight Prefetch | Contextual weight loading | Memory bandwidth limited |
| Attention Mask Compression | `--ascend-use-norm-compress-mask` | Long sequence lengths |
| HCCL Buffer Tuning | Dynamic HCCL_BUFFERSIZE formula | Multi-node deployments |

### Model-Specific Optimizations

**For MoE Models (DeepSeek, Qwen3-30B-A3B):**
- Enable EP + FlashComm1 for communication optimization
- Use `npu_grouped_matmul_swiglu_quant` fusion operator
- Enable multi-stream parallelism for both MLA and MoE

**For Dense Models (Qwen3-32B, GLM-5):**
- Focus on TP optimization and memory bandwidth
- Enable chunked prefill for long sequences
- Use attention mask compression for 32k+ sequences

## Output Format

Always present:
1. **Executive Summary** - Top 3 optimizations by impact
2. **Detailed Recommendations** - All applicable optimizations
3. **Modified Script** - Complete working command
4. **Expected Performance Range** - Based on case study benchmarks
5. **Risk Notes** - Any trade-offs or注意事项

Use Chinese for the report when user query is in Chinese, English otherwise.
