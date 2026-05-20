# Communication Optimization Guide for vLLM-Ascend

## Overview

Communication optimization is critical for parallel configurations (TP/EP/DP) on Ascend hardware due to:
- HCCS ( intra-server): ~28 GB/s
- HCCS (inter-server plane): ~same bandwidth, but shared
- RDMA/RoCE (inter-server): ~25 GB/s (1/8 of HCCS)

## FlashComm1

### What It Does
Replaces AllReduce with ReduceScatter + AllGather pattern:
```
Original: AllReduce (full data)
Optimized: ReduceScatter (1/TP data) → Compute → AllGather (1/TP data)
```

### Why It Works
1. ReduceScatter sends 1/TP data per card
2. Local computation with smaller data
3. AllGather collects results (also 1/TP data)
4. **Net effect:** Communication volume reduced by 1/TP factor

### Performance Data

**Single Layer Measurement:**
| Mode | Latency |
|------|---------|
| Without FlashComm1 | 8.0ms |
| With FlashComm1 | 7.0ms |
| **Reduction** | **12.5%** |

**System Impact (DeepSeek-V3/R1):**
-整网 latency reduction: ~2.5ms
- Throughput improvement: ~16%

### Configuration
```bash
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
```

### When to Use
- EP parallel > 1
- MoE models (DeepSeek, Qwen3-MoE)
- Communication-bound workloads

## AllReduce → ReduceScatter for MoE

### Pure TP Mode (No EP)

**Before:**
```
AllGather (hidden_states) → Gate computation → AllReduce (shared+router experts)
```

**After:**
```
ReduceScatter (hidden_states) → Gate computation → AllGather (hidden_states)
→ [After expert computation]
ReduceScatter → AllGather
```

**Merged approach:**
```
ReduceScatter → Gate → AllGather → Expert Compute → ReduceScatter → AllGather
(Instead of two separate AllReduces)
```

**Benefit:** Single AllReduce instead of two → 30us saving, 1.7ms整网 latency reduction

### EP Mode with ReduceScatter

**Configuration:** TP8 DP2 EP16

**Original communication:**
- AllReduce: 25.5us

**With ReduceScatter:**
- ReduceScatter: 14us

**Benefit:** 45% communication reduction per operation

## Gate DP (Quantization Before Communication)

### Concept
Move gate computation before `hidden_states` allgather, enabling:
1. Quantization before communication (reduce data volume)
2. Local gate computation in DP domain

### Performance Impact
| Operation | Before | After |
|-----------|--------|-------|
| Hidden AllGather | bf16 full | int8 quantized (50% reduction) |
| Gate computation | After allgather | Before allgather |
| Gate AllGather | N/A | Small logits only |

### Code Pattern
In DeepSeek-V3 models:
```python
# Step 1: Quantize hidden_states locally
# Step 2: AllGather quantized data
# Step 3: Gate computation on local (quantized) data
# Step 4: AllGather logits for routing
```

## EP Communication Hierarchical Optimization

### Plane-Level Communication (AIV Mode)

**Problem:** Standard All2All sends data through all links

**Solution:** HCCL_OP_EXPANSION_MODE=AIV
- Each card communicates only with same-plane card on other servers
- HCCS broadcast within server plane
- **Result:** Only one inter-server link per card used

**Benefit:** 
- For EP32, 24batch: TPOT reduction ~20ms
- Dramatically reduces inter-server bandwidth pressure

### Configuration
```bash
export HCCL_OP_EXPANSION_MODE=AIV
```

## Multi-DP EP Communication (Pipeline Algorithm)

### Problem
When TP Allgather and DP Broadcast are separate:
- TP Allgather: uses HCCS (fast)
- DP Broadcast: uses RDMA/RoCE (slow, 1/8 HCCS bandwidth)
- DP Broadcast: 35ms vs TP Allgather: 5.5ms (6x slower!)

### Solution: Merge into EP Allgather
Combine:
- TP Allgather
- DP Broadcast

Into single EP Allgather using pipeline algorithm

**How it works:**
1. Fullmesh AllGather on HCCS within server (fast)
2. Simultaneously RDMA AllGather with same-plane cards (parallel)
3. Second fullmesh for non-plane data

**Result:** DP2 TP8 ~10% throughput improvement

### FlashComm1 + Multi-DP Combined
When both FlashComm1 and Multi-DP optimization are applied:
- Attention: TP16 → TP8 + DP2 with merged EP communication
- MoE: Similar merging
- **Result:** DP2 TP8 ≈ TP16 performance!

## HCCL Buffer Size Optimization

### Problem with Fixed Buffer Size
```bash
# If HCCL_BUFFERSIZE too small:
→ Coredump in AIV mode when traffic exceeds allocation

# If HCCL_BUFFERSIZE too large:
→ Memory waste per card
→ 80MB × 6 communications × 2 directions = 960MB waste
```

### Dynamic Calculation Formula
```bash
HCCL_BUFFSIZE = CEIL(2 × (BS × epWorldSize × min(local_expert_num/epWorldSize, K) × H × sizeof(uint16) / (1024×1024) + 2))
```

### Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| BS | Batch size per card | 24 |
| epWorldSize | EP size | 32 |
| local_expert_num | Local experts | 256/32 = 8 |
| K | Top-K | 8 |
| H | Hidden size | 2048 |

### Benefits
1. Eliminates coredump risk
2. ~6GB memory savings per 16-card node
3. Optimal for each deployment

## Communication-Compute Overlap

### Micro-Batch Pipeline

**Concept:** Split computation into 2 micro-batches
```
Timeline:
MB1: [Attn][────MoE Comm────][MoE][Residual]
MB2:      [Attn][────MoE Comm────][MoE][Residual]
         └────────────── Overlapped ───────────────┘
```

**Requirements:**
1.分核 (Core partitioning): Different streams use different AICore/AIV resources
2. Async communication: Dispatch/Combine as separate streams

###分核策略

**Long Sequences (Attn-heavy):**
```bash
Attn stream: 16 AIC + 32 AIV cores
MoE stream: 8 AIC + 16 AIV cores
```

**Short Sequences (MoE-heavy):**
```bash
Attn stream: 8 AIC + 16 AIV cores
MoE stream: 16 AIC + 32 AIV cores
```

**Goal:** Balance Attn and MoE compute time for optimal overlap

## Quick Reference

```bash
# FlashComm1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1

# Gate DP
export VLLM_ASCEND_ENABLE_GATEDP=1

# Hierarchical EP communication
export HCCL_OP_EXPANSION_MODE=AIV

# Dynamic HCCL buffer
export HCCL_BUFFSIZE=<calculated>

# Multi-stream for overlap
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1
```
