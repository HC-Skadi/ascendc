# Memory Optimization Guide for vLLM-Ascend

## Memory Components in vLLM

1. **Model Weights**: Proportional to model size and precision
2. **KV Cache**: Proportional to batch size × sequence length × heads
3. **Activation Memory**: Proportional to batch size × sequence length × hidden
4. **Workspace**: Temporary buffers for computation

## Attention Mask Compression

### Problem
Standard flash attention uses full attention mask:
- Shape: [seq_len, seq_len] (triangular)
- For 32k sequence: 32k × 32k = 1G elements
- At fp16: ~2GB memory!

### Solution: Norm-Compress Mask
Uses `MASK_TYPE_NORM_COMPRESS` instead of full mask:
- Shape: [128, 128] fixed size
- Works with any sequence length
- Memory: negligible

### Configuration
```bash
--ascend-use-norm-compress-mask
```

### Memory Savings

| Sequence Length | Original Mask | Compressed Mask | Savings |
|-----------------|---------------|-----------------|---------|
| 8k | 512MB | negligible | ~512MB |
| 16k | 2GB | negligible | ~2GB |
| 32k | 8GB | negligible | ~8GB |

### When to Use
- Sequence length > 8k
- Memory-constrained deployments
- Batch size needs to be increased

## Router Expert Sequence Chunking

### Problem
During MoE routing, workspace memory spikes:
- Input shape: [num_tokens × topK, hidden_size]
- Output shape: [num_tokens × topK, expert_hidden]
- Example (32k context, DP2): 
  - num_tokens = 32k × 2 = 65536
  - Peak: 512 + 3584 = 4096MB!

### Solution: Chunked Routing
Split expert computation into chunks:
```bash
# Process 8k tokens at a time instead of 32k
# Chunk 1: [8k × topK, 2048] → compute → partial output
# Chunk 2: [8k × topK, 2048] → compute → partial output  
# Concat all chunks
```

### Memory Savings

| Context | Original Peak | Chunked (8k) | Savings |
|---------|---------------|--------------|---------|
| 32k, DP2 | 4096MB | 1360MB | 2736MB (67%) |

### Performance Trade-off
- Additional concat operation
- 8k chunk concat: ~740us
- < 0.1% overhead

## KV Cache Optimization

### Dynamic KV Cache Allocation
```bash
--gpu-memory-utilization 0.85
```

**Rule:** Higher utilization = more memory for KV cache = larger batches

**Trade-off:**
- Higher utilization → more batching → higher throughput
- Too high → OOM risk on long sequences
- Recommended: 0.85 for balanced, 0.95 for throughput-focused

### KV Cache Chunking
```bash
--enable-chunked-prefill
```

**Benefit:**
- Splits long sequences into manageable chunks
- Reduces peak memory during prefill
- Better memory reuse across requests

## HCCL Buffer Size Optimization

### Problem
Fixed HCCL buffers waste memory:
- 6 communication channels × 2 directions × 80MB = 960MB per node
- AIV mode: buffer overflow → coredump

### Solution: Dynamic Calculation
```bash
export HCCL_BUFFSIZE=CEIL(2 × (BS × epWorldSize × min(local_expert_num/epWorldSize, K) 
                    × H × sizeof(uint16) / (1024×1024) + 2))
```

### Memory Savings
For TP8 DP2 EP16 configuration:
- Static 80MB: 6 × 2 × 80 = 960MB waste
- Dynamic: ~20MB per buffer
- **Total savings: ~6GB per 16-card node**

## Flash Attention Memory

### Standard Flash Attention
```bash
# Default behavior
# Allocates: [batch × heads × seq_len × head_dim]
```

### Optimized Flash Attention
```bash
--ascend-flash-attention-mode unified
```

**Benefit:** Better memory layout for Ascend hardware

## Weight Prefetch

### What It Does
During compute of current layer:
- Prefetch weights for next layer
- Overlaps weight loading with computation

### Memory Impact
- Slightly higher peak (extra weight copy)
- But better compute utilization
- Net: positive for throughput

### Configuration
```bash
--enable-weight-prefetch
```

## Memory Summary by Optimization

| Optimization | Memory Savings | Performance Impact |
|--------------|---------------|-------------------|
| Norm-compress mask | 2-8GB | None |
| Router chunking | 2-4GB | <0.1% overhead |
| Dynamic HCCL buff | 6GB/node | None |
| KV cache tuning | N/A | +20-50% throughput |
| Weight prefetch | Slight increase | +5-10% TPOT |

## Memory-Efficient Configurations

### High Throughput (Memory Constrained)
```bash
--gpu-memory-utilization 0.95
--ascend-use-norm-compress-mask
--block-size 16
--enable-chunked-prefill
```

### Long Sequences (Memory Constrained)
```bash
--gpu-memory-utilization 0.85
--ascend-use-norm-compress-mask
--max-seq-len-to-capture 32768
--enable-chunked-prefill
```

### Balanced
```bash
--gpu-memory-utilization 0.90
--block-size 32
```

## OOM Troubleshooting

### Symptoms
- OOM during startup
- OOM during inference with long sequences
- OOM with high concurrency

### Quick Fixes
1. Reduce `--gpu-memory-utilization` by 0.05
2. Enable `--ascend-use-norm-compress-mask`
3. Enable `--enable-chunked-prefill`
4. Reduce `--max-num-batched-tokens`

### Advanced Fixes
1. Enable router chunking (if MoE model)
2. Reduce TP (fewer model copies)
3. Use higher quantization (w4a16 instead of w8a8)
4. Enable KV cache compression (OmniAttn)

## Quick Reference

```bash
# Memory optimizations
--ascend-use-norm-compress-mask      # Compressed attention mask
--enable-chunked-prefill             # Split long prefill
--gpu-memory-utilization 0.90        # KV cache allocation
--block-size 16                      # Smaller allocation units

# MoE specific
export HCCL_BUFFSIZE=<calculated>    # Dynamic buffer sizing
--enable-weight-prefetch            # Overlap weight loading
```
