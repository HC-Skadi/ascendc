# Issue #6587: [CI][Misc] Some improvement for github action

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

- This PR removes several self-hosted runner labels from the `actionlint.yaml` configuration file. These runners are likely no longer in use, so this change cleans up the configuration and ensures `actionlint` has an accurate list of available runners.
- Move all Action dockerfiles to one folder
- remove useless `runner` input for e2e test.
- update workflow option version

### Does this PR introduce _any_ user-facing change?

No.

### How was this patch tested?

This is a configuration change for the CI linter. The correctness will be verified by `actionlint` running in CI on subsequent pull requests.

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d7e17aaacd5ed1b4b4be6bcfef3a1b7cbc84fc9a


## 基本信息
- **编号**: #6587
- **作者**: wangxiyuan
- **创建时间**: 2026-02-06T03:00:54Z
- **关闭时间**: 2026-02-06T06:06:27Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6587)
