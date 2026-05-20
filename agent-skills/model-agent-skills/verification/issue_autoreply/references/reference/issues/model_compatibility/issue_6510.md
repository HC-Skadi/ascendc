# Issue #6510: [Main2Main] Upgrade to newest vLLM 0204

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

[Main2Main] Upgrade to newest vLLM 0128
1. Fix the problem caused by` 'tuple' object has no attribute 'job_id'` due to https://github.com/vllm-project/vllm/pull/27492
2. Fix the problem  that all_moe_layers is not equal to vllm.moe_forward, vllm.moe_forward_shared due to https://github.com/vllm-project/vllm/pull/33184
3. Fix the problem "got multiple values for keyword argument 'add_special_tokens'" due to https://github.com/vllm-project/vllm/pull/32863
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/v0.15.0


## 基本信息
- **编号**: #6510
- **作者**: zhangxinyuehfad
- **创建时间**: 2026-02-03T11:39:27Z
- **关闭时间**: 2026-03-02T12:04:27Z
- **标签**: documentation, ci/build, module:tests, module:ops, module:quantization, merge-conflicts

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6510)
