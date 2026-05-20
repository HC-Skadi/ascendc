# Issue #5727: [Main2Main] Upgrade vllm commit to 0108

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Upgrade vllm commit to 0108 (eac3b96ec04d07a987823504671650a0bcad5a10)
1. remove `init_cached_hf_modules ` due to https://github.com/vllm-project/vllm/pull/31786
2. skip spec_decode e2e test due to https://github.com/vllm-project/vllm/pull/29821 break 
3. fix `vllm.v1.attention.backends.utils` duo to https://github.com/vllm-project/vllm/pull/31891
4. skip test_qwen3_next_distributed_mp_full_decode_only_tp4 due to https://github.com/vllm-project/vllm/pull/31773 (https://github.com/vllm-project/vllm/pull/31958 will fix)

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5727
- **作者**: zhangxinyuehfad
- **创建时间**: 2026-01-08T08:53:31Z
- **关闭时间**: 2026-01-12T11:45:14Z
- **标签**: documentation, ci/build, module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5727)
