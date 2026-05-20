# Issue #5620: Improve the performance of Mooncake as a backend.

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Call the `batch_put_from_multi_buffers` interface and set `prefer_alloc_in_same_node` to true to prioritize storing kvcache on the same node.

Performance comparison：
| Scenario| Sequence Length | TTFT （s）|
| --- | --- | --- |
| `prefer_alloc_in_same_node` is False | 35450 | 1.199 |
| `prefer_alloc_in_same_node` is True| 35450 | 0.634 |

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/8be6432bdaf6275664d857b1e5e9bf8ed1ce299e


## 基本信息
- **编号**: #5620
- **作者**: heijian123
- **创建时间**: 2026-01-06T01:36:42Z
- **关闭时间**: 2026-01-06T05:55:49Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5620)
