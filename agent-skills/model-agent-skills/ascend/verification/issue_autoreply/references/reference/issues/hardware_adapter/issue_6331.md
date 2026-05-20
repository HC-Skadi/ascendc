# Issue #6331: [Fix] Adds CUDA graph stats to execution state

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Adds a CUDA graph profiling stats field to the execution state and updates the NPU model runner to set, unpack, and forward those stats during execution. This preserves CUDA graph metrics across state transitions, improving observability for later use and diagnostics.

### Does this PR introduce _any_ user-facing change?
Enable this by set
```python
    llm = LLM(
        ...
        disable_log_stats=False,
        cudagraph_metrics=True,
        ...
    )
```
or `--cudagraph-metrics` and make sure do not disable log stats.

After this, you should be able to see something like this, which is really helpful for some light debugging:
```
[loggers.py:257] Engine 000: Avg prompt throughput: 32.3 tokens/s, Avg generation throughput: 114.4 tokens/s, Running: 4 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%
[cuda_graph.py:117] **CUDAGraph Config Settings:**
[cuda_graph.py:117] 
[cuda_graph.py:117] - Mod

## 基本信息
- **编号**: #6331
- **作者**: yiz-liu
- **创建时间**: 2026-01-28T01:45:57Z
- **关闭时间**: 2026-01-28T08:34:20Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6331)
