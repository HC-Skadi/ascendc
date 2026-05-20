# Issue #6778: [Nightly] Increase VLLM_ENGINE_READY_TIMEOUT_S to avoid nightly failure

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
After some observation, I found some cases failed for timeout, just like https://github.com/vllm-project/vllm-ascend/actions/runs/22280996034/job/64487867977#step:9:921 and  https://github.com/vllm-project/vllm-ascend/actions/runs/22315540111/job/64574590762#step:9:1809, this may caused by the excessively long model loading time (currently we are still loading weights from network storage), it is necessary to adjust the timeout seconds 600s -> 1800s
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/9562912cead1f11e8540fb91306c5cbda66f0007


## 基本信息
- **编号**: #6778
- **作者**: Potabk
- **创建时间**: 2026-02-24T02:03:17Z
- **关闭时间**: 2026-02-25T02:14:51Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6778)
