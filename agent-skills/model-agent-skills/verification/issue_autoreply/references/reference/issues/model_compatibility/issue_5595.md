# Issue #5595: [Main2Main] Upgrade vllm commit to 0105

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Upgrade vllm commit to 0105 (8be6432bdaf6275664d857b1e5e9bf8ed1ce299e)

1. Remove `maybe_padded_num_tokens` arg in `model_runner_v1.py` since https://github.com/vllm-project/vllm/pull/31517 deleted unused arg

2. Remove  dense `Qwen/Qwen3-0.6B` in `tests/e2e/multicard/test_aclgraph_capture_replay.py` and `tests/e2e/multicard/test_data_parallel.py` due to https://github.com/vllm-project/vllm/pull/30739
    where offline data parallel mode will not be supported/useful for dense models

3. Adapt `vllm_ascend/worker/worker.py` due to https://github.com/vllm-project/vllm/pull/31584

4. Adapt `self.block_size` calling due to https://github.com/vllm-project/vllm/pull/31540

5. Modify `test_mla_v1.py` due to https://github.com/vllm-project/vllm/pull/28454 , which refactorred `get_head_size()` 

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com

## 基本信息
- **编号**: #5595
- **作者**: wjunLu
- **创建时间**: 2026-01-05T03:17:24Z
- **关闭时间**: 2026-01-06T00:44:29Z
- **标签**: documentation, ci/build, module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5595)
