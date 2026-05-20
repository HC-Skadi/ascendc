# Scheduling Optimization Guide for vLLM-Ascend

## Async Scheduling

### What It Does
Enables asynchronous request scheduling:
- Scheduler runs in parallel with inference
- Hides scheduling overhead (~10-15% of total time)

### Configuration
```bash
--async-scheduling
```

### Expected Impact
- Latency reduction: 10-15%
- Throughput increase: 15-20%
- No trade-offs

### When to Use
- All scenarios
- Especially beneficial with high concurrency

## Chunked Prefill

### What It Does
Splits long prefill sequences into chunks:
```
Original: [Prefill 8192 tokens]
Chunked: [Chunk 2048] → [Chunk 2048] → [Chunk 2048] → [Chunk 2048]
```

### Benefits
1. **Reduced peak memory:** Don't hold all activations for 8k+ tokens
2. **Better latency hiding:** First token earlier for streaming
3. **More consistent TTFT:** Less variance from memory allocation
4. **Higher throughput:** Better GPU utilization

### Configuration
```bash
--enable-chunked-prefill
--max-num-batched-tokens 8192
```

### Trade-offs
- Small overhead from chunking
- Slightly higher TTFT for short sequences
- Better for long sequence scenarios

### When to Use
- Input sequences > 4k
- Memory constrained environments
- Streaming applications
- Mixed batch with varying lengths

## Dynamic Batch Overlap (DBO)

### What It Does
Overlaps prefill and decode in mixed workloads:
- While some requests are decoding
- Others can start prefill
- Maximum GPU utilization

### Configuration
```bash
--enable-dynamic-batch-overlap
```

### Expected Impact
- System utilization: +20-30%
- Throughput: +15-25% in mixed workloads

## Scheduling Parameters

### Max Num Batched Tokens
```bash
--max-num-batched-tokens 8192
```

**Purpose:** Maximum tokens processed in single batch

**Trade-offs:**
| Value | Throughput | Latency | Memory |
|-------|------------|---------|--------|
| 2048 | Lower | More consistent | Less |
| 8192 | Higher | More variable | More |
| 16384 | Highest | Most variable | Highest |

**Recommendation:** Start with 8192, tune based on workload

### Max Num Seq
```bash
--max-num-seqs 256
```

**Purpose:** Maximum concurrent sequences

**Recommendation:** Match your concurrency requirements

### Block Size
```bash
--block-size 16
```

**Purpose:** KV cache allocation granularity

**Trade-offs:**
| Block Size | Memory Efficiency | Fragmentation |
|------------|------------------|----------------|
| 16 | Better for short seqs | More blocks |
| 32 | Balanced | Balanced |
| 64 | Better for long seqs | Less blocks |

**Recommendation:** 16 for diverse lengths, 32 for mostly long

## Multi-Stream Parallelism

### What It Does
Runs Attention and MoE on separate streams:
```
Stream 1: [Attn] → [MoE Wait] → [MoE]
Stream 2: (Idle)  → [Attn Compute] → (Idle)
                    ↑ Overlapped
```

### MLA Multi-Stream
```bash
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1
```

**Expected Impact:** TPOT reduction ~3-4ms

### MoE Multi-Stream
```bash
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
```

**Expected Impact:** TPOT reduction ~3ms

### Combined Multi-Stream
**Expected Impact:** ~6ms TPOT reduction

### When to Use
- MoE models (DeepSeek, Qwen3-MoE)
- Decode-heavy workloads
- When TPOT is the bottleneck

## Weight Prefetch

### What It Does
Prefetches weights for next layer during current layer compute:
```
Current: Layer N compute (weights loaded)
        ↓
Prefetch: Layer N+1 weights loaded in background
        ↓
Next: Layer N+1 compute (weights already in memory)
```

### Expected Impact
- Additional ~1ms TPOT reduction on top of multi-stream
- Better compute/load overlap

### When to Use
- Memory bandwidth limited
- When multi-stream alone doesn't meet TPOT target

## Prefill-Decode Scheduling

### Scheduling Strategy
```bash
--scheduling-policy prefill_decode_mixed
```

**Purpose:** Allows prefill and decode in same batch

**Benefit:** Better utilization when workload is mixed

### Separate P and D Scheduling
For PD separation mode:
- P nodes: Schedule only prefills
- D nodes: Schedule only decodes
- External scheduler coordinates

## Latency vs Throughput Trade-offs

### Low Latency (Streaming)
```bash
--max-num-batched-tokens 2048
--block-size 16
--enable-chunked-prefill
--async-scheduling
```

**Result:** Lower TTFT, lower TPOT, lower throughput

### High Throughput (Batch Processing)
```bash
--max-num-batched-tokens 16384
--block-size 32
--gpu-memory-utilization 0.95
```

**Result:** Higher throughput, higher latency per request

### Balanced
```bash
--max-num-batched-tokens 8192
--block-size 32
--gpu-memory-utilization 0.90
--enable-chunked-prefill
--async-scheduling
```

## Profiling and Tuning

### Enable Profiling
```bash
--enable-profiling
--profile-output-dir ./profile_logs
```

### Key Metrics to Watch
1. **Scheduler overhead:** Should be <5% of total time
2. **Queue time:** Indicator of scheduling efficiency
3. **TTFT vs TPOT ratio:** For latency budget allocation

### Tuning Loop
1. Start with baseline
2. Enable async scheduling
3. Tune batch size for target latency/QPS
4. Add chunked prefill if memory constrained
5. Enable multi-stream for MoE models
6. Profile and iterate

## Quick Reference

```bash
# Core scheduling
--async-scheduling                           # Always enable
--enable-chunked-prefill                     # For long sequences
--scheduling-policy prefill_decode_mixed    # Mixed workloads

# Batching
--max-num-batched-tokens 8192              # Tune for workload
--max-num-seqs 256                          # Match concurrency

# Multi-stream (MoE only)
export VLLM_ASCEND_ENABLE_MULTISTREAM_MOE=1
export VLLM_ASCEND_ENABLE_MULTISTREAM_MLA=1

# Weight prefetch
--enable-weight-prefetch
```

## Troubleshooting Scheduling Issues

### High Scheduler Overhead
**Symptoms:** Scheduling takes >10% of time
**Fix:** Enable async scheduling

### Inconsistent Latency
**Symptoms:** High variance in TTFT/TPOT
**Fix:** Enable chunked prefill, reduce batch size

### Low GPU Utilization
**Symptoms:** GPU usage <80%
**Fix:** 
1. Increase batch size
2. Enable chunked prefill
3. Check for CPU bottlenecks

### Memory Pressure
**Symptoms:** OOM with reasonable batch sizes
**Fix:**
1. Reduce batch size
2. Enable chunked prefill
3. Use compressed attention mask
