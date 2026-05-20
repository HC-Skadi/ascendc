# DeepSeek MoE Model Optimization Guide

## Target Models
- DeepSeek-V3
- DeepSeek-R1
- Qwen3-30B-A3B

## Key Architectural Differences from Dense

MoE models have:
- Multiple "expert" FFN layers
- Routing network to select top-K experts per token
- Expert Parallel (EP) for distributing experts across devices

## Critical Optimizations

### 1. FlashComm1 Communication Optimization
**Environment Variable:** `VLLM_ASCEND_ENABLE_FLASHCOMM1=1`

**What it does:**
Replaces AllReduce with ReduceScatter + AllGather pattern in MoE layers

**Expected Impact:**
- Single layer latency: 8.0ms → 7.0ms (12.5% reduction)
-整网 latency reduction: ~2.5ms

**Applicable:** All MoE models with EP > 1

**Why it works:**
- ReduceScatter reduces communication data size (1/TP factor)
- AllGather after computation hides communication behind compute

### 2. Gate DP (Quantization Before Allgather)
**Environment Variable:** `VLLM_ASCEND_ENABLE_GATEDP=1`

**What it does:**
Moves gate computation before hidden_states allgather, enables quantization before communication

**Expected Impact:**
- Reduces communication volume by ~50% for hidden_states
- Gate computation: 674us → optimized (exact depends on batch size)

**Applicable:** EP parallel configurations with DeepSeek models

### 3. GroupedMatmulSwigluQuant Fusion
**Purpose:** Fuses GroupedMatmul + Swiglu + DynamicQuant into single operator

**Expected Impact:**
- TPOT reduction: 4-5ms in DP32 EP32 @ 24batch
- Eliminates "dirty data" handling overhead

**Why:** Filters out invalid tokens in dispatched routing results

### 4. Multi-Stream Parallelism

#### MLA Multi-Stream (for DeepSeek)
**Environment Variable:** `VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1`

**Expected Impact:** TPOT reduction ~3-4ms

#### MoE Multi-Stream
**Environment Variable:** `VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1`

**Expected Impact:** TPOT reduction ~3ms

**Combined Impact:** ~6ms TPOT reduction when both enabled

### 5. Weight Prefetch (MLA + MoE)
**What it does:** Prefetches qkv down-projection and o_proj weights during Quant computation

**Expected Impact:** Additional ~1ms TPOT reduction on top of multi-stream

## Communication Optimizations for MoE

### Allreduce → ReduceScatter (Pure TP Mode)
When MoE uses pure TP (no EP):
```bash
# MoE layer: AllReduce replaced by ReduceScatter + AllGather
# Performance gain: 30us per AllReduce → 1.7ms total latency reduction
```

### EP Mode with Dispatch/Combine
For EP32 configurations:
```bash
# Use HCCL_OP_EXPANSION_MODE for hierarchical communication
HCCL_OP_EXPANSION_MODE=AIV
```
**Benefit:** Reduces cross-node communication by using plane-level HCCS

### Multi-DP EP Communication
**Issue:** DP broadcast via RoCE is 8x slower than HCCS
**Solution:** Merge TP Allgather + DP broadcast into EP Allgather (Pipeline algorithm)
**Result:** ~10% throughput improvement for DP>1 configurations

## HCCL Buffer Size Dynamic Calculation

**Formula:**
```bash
export HCCL_BUFFSIZE=CEIL(2 * (BS * epWorldSize * min(local_expert_num/epWorldSize, K) * H * sizeof(uint16) / (1024*1024.0) + 2))
```

**Parameters:**
- BS: Batch size per card
- epWorldSize: EP communication domain size
- local_expert_num: Number of local experts
- K: Top-K experts selected
- H: Hidden size

**Benefits:**
- Dynamic sizing avoids memory waste
- Prevents coredump from buffer overflow in AIV mode
- ~6GB memory savings per 16-card node

## Measured Performance (DeepSeek-V3/R1)

| Configuration | Throughput | TPOT | TTFT |
|--------------|-----------|------|------|
| TP8 DP2 EP16 (baseline) | 0.73 qps/node | - | - |
| TP8 DP2 EP16 + FlashComm1 | 0.85 qps/node | - | - |
| + GateDP + Fusion | 1.2 qps/node | - | - |
| + Multi-stream | 1.5 qps/node | - | - |
| Full optimized (PD 4P1D) | 1.8 qps/node | - | - |

## Environment Variable Quick Reference

```bash
# Core MoE optimizations
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_GATEDP=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1

# Communication
export HCCL_OP_EXPANSION_MODE=AIV

# Memory
export HCCL_BUFFSIZE=<calculated value>
```

## Troubleshooting

### Issue: MoE experts have uneven load
**Solution:** Enable OmniPlacement (expert redundancy + load balancing)

### Issue: Long TTFT on long sequences
**Solution:** 
1. Increase P nodes (Prefill capacity)
2. Enable chunked prefill
3. Use Micro-Batch pipeline for computation/communication overlap

### Issue: TPOT increases with higher concurrency
**Solution:** Enable multi-stream parallelism and weight prefetch
