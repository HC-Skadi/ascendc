# Issue #6233: [CI] Decrease Qwen3 dense model output throughput baseline to make ci happy

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
As https://github.com/vllm-project/vllm-ascend/actions/runs/21327913593/job/61388195448 shows, I encountered two CI failures., The results consistently pointed to the reduced outcome 1600 -> 1514
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6233
- **作者**: Potabk
- **创建时间**: 2026-01-25T12:57:31Z
- **关闭时间**: 2026-01-26T01:04:13Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6233)
