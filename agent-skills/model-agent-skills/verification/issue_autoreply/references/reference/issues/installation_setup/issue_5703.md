# Issue #5703: [CI] fix image build tag

**类型**: Pull Request

## 问题背景
ref doesn't work with workflow_dispatch, let's change it to raw way

This PR also merge the pr_create job into one runner to save resource.
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5703
- **作者**: wangxiyuan
- **创建时间**: 2026-01-08T00:55:33Z
- **关闭时间**: 2026-01-08T01:27:46Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5703)
