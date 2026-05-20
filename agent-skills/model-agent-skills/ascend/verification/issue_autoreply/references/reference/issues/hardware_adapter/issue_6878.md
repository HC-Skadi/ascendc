# Issue #6878: [Feat][310p] 310P support w8a8s quantization and saving w8a8sc state

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This pull request introduces significant enhancements for 310P device support, primarily by enabling W8A8S quantization and facilitating the saving of models with W8A8SC state outputs. It provides an example script for saving sharded and compressed model states, implements the core W8A8S quantization method, and integrates metadata generation within the 310P worker to accurately describe the quantization types of saved parameters. These changes aim to improve efficiency and compatibility for quantized models on 310P hardware.
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?
W8A8S accuarcy test and W8A8SC states save.
<img width="886" height="184" alt="image" src="https://github.com/user-attachments/assets/e9bcac54-1f69-4d3a-a5b8-221a147ef99d" />

- vLLM version: v0.16.0
- vLLM main: https://github.com/vllm-project/vllm/commit/15d76f74e2fdb12a95ea00f0ca283acf6219a2b7


## 基本信息
- **编号**: #6878
- **作者**: pu-zhe
- **创建时间**: 2026-02-28T09:35:17Z
- **关闭时间**: 2026-03-02T12:09:16Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.16.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6878)
