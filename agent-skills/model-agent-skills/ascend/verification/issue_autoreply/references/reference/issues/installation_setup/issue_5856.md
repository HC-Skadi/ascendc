# Issue #5856: [CI] Nightly image build sync with main image build

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
It is a little strange that nightly image build is unschedule https://github.com/vllm-project/vllm-ascend/actions/workflows/schedule_nightly_image_build.yaml; to avoid it ,we should make it snyc with the main image build
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5856
- **作者**: Potabk
- **创建时间**: 2026-01-13T09:42:12Z
- **关闭时间**: 2026-01-13T12:04:02Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5856)
