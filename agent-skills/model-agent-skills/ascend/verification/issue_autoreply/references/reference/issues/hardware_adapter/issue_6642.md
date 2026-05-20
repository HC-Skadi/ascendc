# Issue #6642: [Model] GLM5 adaptation

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
GLM5 adaptation
1. use torch_npu.npu_lightning_indexer for GLM5
2. forbid eagle proposer when fullgraph mode is enabled because of bugs
3. add quatization config for GLM5
### Does this PR introduce _any_ user-facing change?
N/A
### How was this patch tested?
by ci
- vLLM main: https://github.com/vllm-project/vllm/commit/978a37c82387ce4a40aaadddcdbaf4a06fc4d590


## 基本信息
- **编号**: #6642
- **作者**: yydyzr
- **创建时间**: 2026-02-09T12:42:48Z
- **关闭时间**: 2026-02-11T14:22:23Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6642)
