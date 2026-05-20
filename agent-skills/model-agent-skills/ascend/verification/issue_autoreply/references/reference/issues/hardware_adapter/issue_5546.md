# Issue #5546: [Main2Main] Upgrade vllm commit to 0102

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Upgrade vllm commit to 0102

1. Remove `maybe_padded_num_tokens` arg in `model_runner_v1.py` due to https://github.com/vllm-project/vllm/pull/31517
2. Remove `Qwen/Qwen3-0.6B` in `tests/e2e/multicard/test_aclgraph_capture_replay.py` because that [ Offline data parallel mode will be not supported/useful for dense models](https://github.com/vllm-project/vllm/commit/bd877162ebd7a2eb36961a8e49824422dd35bcdc#diff-c1550d0a38469d039370567d8981969530cbfffc7302cd1778e7c2c8a9322deaL548)
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5546
- **作者**: wjunLu
- **创建时间**: 2025-12-31T02:45:30Z
- **关闭时间**: 2026-01-04T03:51:10Z
- **标签**: documentation, ci/build, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5546)
