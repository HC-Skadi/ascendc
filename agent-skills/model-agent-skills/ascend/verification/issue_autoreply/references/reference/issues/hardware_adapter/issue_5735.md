# Issue #5735: [Refactor] Provide a framework to accommodate operators for different hardware devices

**类型**: Pull Request

## 问题背景
come from: https://github.com/vllm-project/vllm-ascend/issues/5463

Reason:

During the iteration process of the hardware version, there may be a large number of iterations for the operators, which can lead to short-term compatibility differences. Therefore, an intermediate adaptation layer is provided to accommodate the short-term differences in operators.


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5735
- **作者**: weijinqian0
- **创建时间**: 2026-01-08T12:47:10Z
- **关闭时间**: 2026-01-13T01:53:27Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5735)
