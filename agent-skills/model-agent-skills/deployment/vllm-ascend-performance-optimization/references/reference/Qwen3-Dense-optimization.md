# Qwen3-32B Dense Model Optimization Guide

## Baseline Configuration
- Model: Qwen3-32B
- Hardware: 8x Ascend 910 NPU
- Parallel: TP=4
- Quantization: w8a8

## Measured Performance Results

### Baseline (No Optimizations)
- Throughput: 239.36 tok/s
- TPOT: 115.09 ms
- Benchmark Duration: 106.95s

### Optimized Configuration
- Throughput: 383.23 tok/s (+60.1%)
- TPOT: 55.21 ms (-52%)
- Benchmark Duration: 66.80s (-37.5%)

## Key Optimizations Applied

### 1. Async Scheduling
**Flag:** `--async-scheduling`

**Impact:** Reduces scheduling overhead by ~15-20%

**Applicable:** All scenarios, especially high concurrency

**Why:** Allows overlapped scheduling and execution, hiding the scheduler overhead behind computation

### 2. Graph Compilation (Decode Only)
**Flag:** `--compilation-config FULL_DECODE_ONLY`

**Impact:** Reduces TorchDynamo guard overhead by ~3ms per iteration

**Applicable:** Decode-heavy workloads where input shapes are fixed

**Why:** Skips dynamo guard checks by using cached compiled graphs for fixed batch sizes

### 3. Block Size Tuning
**Flag:** `--block-size 16`

**Impact:** Improves KV cache allocation efficiency

**Applicable:** Variable length inputs

**Why:** Smaller blocks reduce padding waste for short sequences

### 4. Max Num Batched Tokens
**Flag:** `--max-num-batched-tokens 8192`

**Impact:** Enables larger batch sizes for throughput

**Applicable:** Throughput-focused scenarios

**Why:** Increases batching granularity to maximize GPU utilization

## Additional Optimizations for Dense Models

### Attention Mask Compression
For sequences >16k, enable norm-compress mask:
```bash
--ascend-use-norm-compress-mask
```
**Savings:** ~2GB VRAM for 32k sequence (2*seq^2 B formula)

### Long Sequence Support
For 32k+ inputs:
```bash
--max-seq-len-to-capture 32768
--gpu-memory-utilization 0.85
```

## Performance Scaling by Hardware

| Hardware | TP | Throughput (tok/s) | TPOT (ms) |
|---------|-----|-------------------|-----------|
| 8x Ascend 910 | 4 | 383.23 | 55.21 |
| 4x Ascend 910 | 4 | ~190 | ~110 |
| 16x Ascend 910 | 8 | ~750 | ~28 |

## Common Issues and Fixes

### Issue: Low Throughput Despite Good TPOT
**Cause:** Scheduling overhead dominates
**Fix:** Enable async scheduling and increase concurrency

### Issue: OOM on Long Sequences  
**Cause:** KV cache too small
**Fix:** Reduce `gpu-memory-utilization` or enable attention mask compression

### Issue: High TTFT but Low TPOT
**Cause:** Prefill is bottleneck
**Fix:** Enable chunked prefill to overlap prefills
