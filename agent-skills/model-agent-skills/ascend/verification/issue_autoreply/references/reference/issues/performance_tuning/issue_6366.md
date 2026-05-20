# Issue #6366: [Kernel] Add AscendC fused op transpose_kv_cache_by_block to speed up GQA transfer

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
As #2947 describe, we need to transpose kv cache layout after GQA kv transfer when prefill and decode tensor parallel size are heterogeneous, in the previous implementation, we use `npu_paged_cache_load ` + `tranpose` + `_npu_reshape_and_cache` to do this work.

But obviously, it is not an efficient plan, the ops above need to be called for each layer, which introduces 3 * layer_num kernel launch, and 6 * layer_num data movement between L1 Cache and HBM for one request on decode node. Usually, decode node uses graph mode, so these op kernels will be called between decode forward launched by an async thread in mooncacke connector, this kernels maybe last for several decode forward and TTFT will increase by 3~4 decode forward time.

 In this PR, we implement an AscendC fused op `transpose_kv_cache_by_block` to do this with only once kernel launch and move data between L1 Cache and HBM only once.

After using this fused op, the time cost in t

## 基本信息
- **编号**: #6366
- **作者**: lidenghui1110
- **创建时间**: 2026-01-28T13:21:51Z
- **关闭时间**: 2026-02-03T06:10:01Z
- **标签**: module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6366)
