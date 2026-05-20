# Issue #6288: [Misc] Drop deepseek patch

**类型**: Pull Request

## 问题背景
We patched deepseek before since we notice asserterror raised by transformers. Now due to transformers upgrade, the patch looks useless now. Let's remove it.

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6288
- **作者**: wangxiyuan
- **创建时间**: 2026-01-27T01:21:44Z
- **关闭时间**: 2026-01-29T06:45:51Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6288)
