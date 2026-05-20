# Issue #6191: [Refactor] Separate `_prepare_inputs` to `_prepare_inputs` and `_preprocess`

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Align with upstream vLLM. This PR will help downstream vLLM-Omni reduce the cost for maintaining the _prepare_inputs. Besides, it helps vLLM-Ascend code more readable. In the future, we can follow closer to vLLM. The `preprocess` logic is same as GPUModelRunner. We don't need to maintain it anymore.

### Does this PR introduce _any_ user-facing change?

No

### How was this patch tested?

CI.

- vLLM version: v0.14.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6191
- **作者**: gcanlin
- **创建时间**: 2026-01-23T08:12:37Z
- **关闭时间**: 2026-01-26T06:05:23Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6191)
