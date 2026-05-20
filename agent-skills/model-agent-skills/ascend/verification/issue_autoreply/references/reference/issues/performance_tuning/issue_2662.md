# Issue #2662: [Feature]: Expose Componentized GPU Memory Metrics

## 基本信息

- **编号**: #2662
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2662
- **创建时间**: 2025-08-31T05:25:23Z
- **关闭时间**: 2025-09-01T03:54:37Z
- **更新时间**: 2025-09-01T03:54:37Z
- **提交者**: @BugVanquisher
- **评论数**: 0

## 标签

feature request

## 问题描述

Description:

vLLM currently provides useful observability via the /metrics endpoint, including request counts, queue sizes, and end-to-end latency histograms. While this is helpful, several production-critical observability gaps remain:

I only see high-level GPU cache usage (vllm:gpu_cache_usage_perc).
It would be nice also to add:
	•	Model weights memory
	•	KV cache memory (allocated vs. used vs. evicted)
	•	Framework overhead memory

### Alternatives

_No response_

### Additional context

_No response_
