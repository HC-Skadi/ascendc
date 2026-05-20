# Issue #6675: [CI]fix nightly multi node test error for wait for pod ready

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Fixes the issue where nightly multi-node tests hang during the "wait for pod ready" stage due to strict shell mode.

issue: https://github.com/vllm-project/vllm-ascend/actions/runs/21874130621/job/63137883914

bug:
<img width="1170" height="381" alt="截屏2026-02-11 11 16 44_副本" src="https://github.com/user-attachments/assets/714cc93c-0239-46f5-ab8e-30281e050ae2" />

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/13397841ab469cecf1ed425c3f52a9ffc38139b5


## 基本信息
- **编号**: #6675
- **作者**: MrZ20
- **创建时间**: 2026-02-11T03:19:42Z
- **关闭时间**: 2026-02-11T10:11:01Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6675)
