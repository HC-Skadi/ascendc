# Issue #5701: [Perf] Supports compute-communication overlap in the forward of sfa_v1 in the Sharded-CP feature.

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
> Extracted from PR #5513
Based on the Sharded-CP feature PR:#4702; RFC:https://github.com/vllm-project/vllm/issues/30055

### All-gather KV Cache for Communication Overlap:
- This PR adjusts the calculation order in the SFA.
- split `index_select` into `indexer_select_pre_process` and `indexer_select_post_process`.
- Combine `nope`, `rope` and `index-k` into a tensor to perform asynchronous all-gather.

### benchmark:
input=40k && num_batch_token=20k
- before:
```
Mean TTFT (ms):                          2614.52
Median TTFT (ms):                        3148.03
P50 TTFT (ms):                           3148.03
P90 TTFT (ms):                           3163.48
P99 TTFT (ms):                           3170.20
```

- after:
```
Mean TTFT (ms):                          2529.92
Median TTFT (ms):                        3051.69
P50 TTFT (ms):                           3051.69
P90 TTFT (ms):                           3067.31
P99 T

## 基本信息
- **编号**: #5701
- **作者**: zzhx1
- **创建时间**: 2026-01-07T15:14:07Z
- **关闭时间**: 2026-01-11T01:47:28Z
- **标签**: documentation, module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5701)
