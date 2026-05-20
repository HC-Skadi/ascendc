# Prefill-Decode Separation Optimization Guide

## When to Use PD Separation

PD separation is beneficial when:
- TTFT (Time To First Token) is critical
- High concurrency with mixed input lengths
- Throughput goal: >1.5 qps per node

## Architecture Overview

```
PD Separation Architecture:
┌─────────────┐     ┌─────────────┐
│   Prefill   │────▶│   Decode    │
│   Nodes     │     │   Nodes     │
│  (P nodes)  │     │  (D nodes)  │
└─────────────┘     └─────────────┘
    Handles:           Handles:
    - Tokenization     - KV cache lookup
    - Attention        - Token generation
    - MoE routing      - Sampling
```

## Target Performance

| Scenario | P Nodes | D Nodes | Target QPS | TTFT | TPOT |
|----------|---------|---------|------------|------|------|
| 4k in, 1.5k out | 1P1D | 16c P, 32c D | 2.25 qps | <2s | <100ms |
| 7P1D (DeepSeek-R1) | 7 | 1 | 608 QPM | <2s | <50ms |

## Prefill Optimizations

### 1. FlashComm1 for Prefill
**Same as MoE optimization:**
```bash
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
```
**Benefit:** Reduces single layer latency from 8ms → 7ms

### 2. Micro-Batch Pipeline
**Purpose:** Overlap computation and communication

**Implementation:**
- Split input into 2 micro-batches
- Create dual pipeline for Attention and MoE streams
-分核 strategy (long vs short sequences)

**For Long Sequences (16k+):**
```bash
# Attn uses 16:32 (AIC:AIV) core ratio
# MoE uses 8:16 (AIC:AIV) core ratio
```

**For Short Sequences:**
```bash
# Reduce attn cores, balance attn and MoE compute time
```

**Benefit:** Hides communication behind computation, ~10-20% latency reduction

### 3. InitRouting V2 (EP Optimization)
**Instead of:** `npu_moe_init_routing`
**Use:** `npu_moe_init_routing_v2`

**Why:** 
- Supports input scale for quantized communication
- Reduces DynamicQuant computation by 8x (topK factor)

**Performance Comparison:**

| Implementation | Total MoE Time |
|----------------|----------------|
| npu_moe_init_routing + TP | 3647us |
| npu_moe_init_routing_v2 + EP | 1747us (-52%) |

### 4. FA Operator Optimization (MLA)
**Issue:** vLLM-Ascend adds unnecessary padding to QKV
**Fix:** Use `UnpadFlashAttentionMlaBF16NdKernel` instead of padded version

**Benefit:** 
- Model latency: 574ms → 538ms (-36ms)
- P node throughput: 1.75 qps → 2.0 qps (+14%)

## Decode Optimizations

### 1. GroupedMatmulSwigluQuant Fusion
**Purpose:** Filter dirty data from expert dispatch

**Impact:** TPOT reduction 4-5ms @ DP32 EP32, 24batch

### 2. Multi-Stream + Weight Prefetch
**Impact:** 
- Multi-stream alone: ~6ms TPOT reduction
- + Weight prefetch: additional ~1ms

### 3. Dynamic Batch Overlap (DBO)
**Purpose:** Overlap prefill and decode in mixed workloads

**Benefit:** Improves system utilization during prefetch/decode transitions

## PD Balance Tuning

### Core Relationship
```
Throughput ∝ 1/TTFT (for prefill) × 1/TPOT (for decode) × concurrency
```

### Determining P:D Ratio

**Rule of Thumb:**
- Short inputs (4k), high QPS: Use more D capacity
- Long inputs (16k+): Use more P capacity
- Target TTFT <2s, TPOT <100ms

**Scaling Formula:**
```
QPM = (P_cards × prefill_qps) × (D_cards × decode_qps) / (P_cards + D_cards)
```

### Typical Configurations

| Model | P Config | D Config | QPS Target |
|-------|----------|----------|------------|
| DeepSeek-R1 | TP16+EP16 | TP2+DP32 | 7.2 qps (4 nodes) |
| DeepSeek-V3 | TP16+EP16 | TP2+DP32 | 7.2 qps (4 nodes) |
| Qwen3-32B | TP8 | DP16 | 4 qps (1 node) |

## SuperKernel for Decode

**What:** Fuses 58/61 layers into single kernel for DeepSeek-R1

**Benefit:** 10-20% throughput improvement

**Usage:** Automatic when using torchair compilation

```bash
# Enable graph compilation for SuperKernel fusion
--compilation-config FULL_DECODE_ONLY
--torch-profile
```

## Chunked Prefill

**Purpose:** Split long prefills into chunks for:
1. Better memory management
2. Latency hiding
3. Reduced peak memory

**Configuration:**
```bash
--enable-chunked-prefill
--max-num-batched-tokens 8192
```

**Benefit:** Enables longer sequences without OOM, improves TTFT variance

## Environment Variables Quick Reference

```bash
# Prefill optimizations
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export HCCL_OP_EXPANSION_MODE=AIV

# Decode optimizations  
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_WEIGHT_PREFETCH=1

# Memory
export HCCL_BUFFSIZE=<dynamic calculation>
```

## Troubleshooting PD Issues

### Issue: TTFT Too High
**Solutions:**
1. Add more P nodes
2. Increase P node concurrency
3. Enable chunked prefill
4. Check P:D ratio balance

### Issue: TPOT Degradation After Scaling
**Solutions:**
1. Ensure D node TPOT <50ms target
2. Use weight prefetch
3. Optimize D node batch size

### Issue: Low Overall QPS
**Solutions:**
1. Verify P:D ratio matches workload
2. Check for prefill/decode imbalance
3. Profile with MindStudio tools
