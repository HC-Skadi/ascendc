# Issue #5762: [CI] Avoid lint and ut for PR push

**类型**: Pull Request

## 问题背景
1. Don't run lint and ut again once the PR is merged to save CI resource
2. Update codecov every 4 hour
3. rename `model_downloader` to suitable name
4. update schedule job to better time.

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5762
- **作者**: wangxiyuan
- **创建时间**: 2026-01-09T06:58:14Z
- **关闭时间**: 2026-01-09T07:57:06Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5762)
