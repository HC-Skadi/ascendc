# Issue #5547: [Nightly] Trigger image build for nightly

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
We should also trigger image build when nightly test related files are changed to ensure the image is valid for nightly tests. Please note that this only applies to image with the tag `main*`(which means build triggered by PR).
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5547
- **作者**: Potabk
- **创建时间**: 2025-12-31T02:50:31Z
- **关闭时间**: 2026-01-04T00:50:58Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5547)
