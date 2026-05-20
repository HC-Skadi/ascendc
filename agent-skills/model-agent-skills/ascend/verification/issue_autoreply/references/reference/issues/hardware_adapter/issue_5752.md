# Issue #5752: [Main2Main] Upgrade vllm commit to 0109

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Upgrade vllm commit to 0109 (bde38c11df0ea066a740efe9b77fff5418be45df)

1. remove `init_cached_hf_modules ` due to https://github.com/vllm-project/vllm/pull/31786
2. fix spec_decode e2e test due to https://github.com/vllm-project/vllm/pull/29821 break 
3. fix `vllm.v1.attention.backends.utils` duo to https://github.com/vllm-project/vllm/pull/31891
4. fix `self.seq_lens - query_lens` on same device due to https://github.com/vllm-project/vllm/pull/31773 
5. skip model_runner_v2 e2e test due to `'_OpNamespace' '_C' object has no attribute 'get_cuda_view_from_cpu_tensor'`


### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5752
- **作者**: zhangxinyuehfad
- **创建时间**: 2026-01-09T03:48:10Z
- **关闭时间**: 2026-01-13T11:14:43Z
- **标签**: documentation, ci/build, module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5752)
