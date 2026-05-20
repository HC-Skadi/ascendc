# Issue #5490: [Refactor]7/N Extract common code to common_cp

**类型**: Pull Request

## 问题背景
RFC: https://github.com/vllm-project/vllm-ascend/issues/4629
Reason：
Eliminate duplicate code for two file(mla_cp.py attention_cp.py) to common_cp.py.

vLLM version: 0.13.0rc3
vLLM main: https://github.com/vllm-project/vllm/commit/ad32e3e19ccf0526cb6744a5fed09a138a5fb2f9

vLLM version: release/v0.13.0
vLLM main: https://github.com/vllm-project/vllm/commit/5fbfa8d9ef15948599631baeb91e8220b2ee9bcc

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/5326c89803566a131c928f7fdd2100b75c981a42


## 基本信息
- **编号**: #5490
- **作者**: wujinyuan1
- **创建时间**: 2025-12-29T13:12:34Z
- **关闭时间**: 2026-01-05T09:41:12Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: 0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5490)
