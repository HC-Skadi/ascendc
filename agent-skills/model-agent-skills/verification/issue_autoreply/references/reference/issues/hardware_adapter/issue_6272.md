# Issue #6272: [Lint] Fix mypy issue to make CI happy

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
The variables `self.prefiller_heap` `self.decoder_heap` are used as `List[tuple[float, int, ServerState]]` but defined as  `List[tuple[int, int, ServerState]]`, which leads to the failed of mypy, see https://github.com/vllm-project/vllm-ascend/actions/runs/21351411010/job/61448739554?pr=6265
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6272
- **作者**: Potabk
- **创建时间**: 2026-01-26T09:20:39Z
- **关闭时间**: 2026-01-26T09:54:00Z
- **标签**: 无

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6272)
