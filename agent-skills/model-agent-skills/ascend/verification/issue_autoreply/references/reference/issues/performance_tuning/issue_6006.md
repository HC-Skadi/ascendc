# Issue #6006: [Graph][Fusion] Add MatmulAllReduceAddRMSNorm graph fusion for npugraph_ex.

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR builds upon PR https://github.com/vllm-project/vllm-ascend/pull/5011 and aims to further enhance the npu_graph_ex_passes module. Based on prior work, we have added graph optimization support for the add_rms_quant fused operator in scenarios where a bias term is present—ensuring the fusion pattern is correctly registered and matched into the computation graph.

This time, we performed the operator fusion of MatmulAllReduceAddRMSNorm and added corresponding ST test cases for regression monitoring.
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #6006
- **作者**: ForBetterCodeNine
- **创建时间**: 2026-01-19T08:49:21Z
- **关闭时间**: 2026-01-27T08:41:48Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6006)
