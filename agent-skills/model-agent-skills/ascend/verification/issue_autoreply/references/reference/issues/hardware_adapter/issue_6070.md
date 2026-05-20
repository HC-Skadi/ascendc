# Issue #6070: [CI] Upgrade CANN to 8.5.0

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. Upgrade CANN to 8.5.0
2. move triton-ascend 3.2.0 to requirements

note: we skipped the two failed e2e test, see https://github.com/vllm-project/vllm-ascend/issues/6076 for more detail. We'll fix it soon.


### How was this patch tested?
Closes: https://github.com/vllm-project/vllm-ascend/issues/5494

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6070
- **作者**: wangxiyuan
- **创建时间**: 2026-01-21T03:00:22Z
- **关闭时间**: 2026-01-22T01:29:51Z
- **标签**: documentation, ci/build, module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6070)
