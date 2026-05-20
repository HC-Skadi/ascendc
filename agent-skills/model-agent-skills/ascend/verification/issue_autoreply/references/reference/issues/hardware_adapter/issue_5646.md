# Issue #5646: [CI] Add workflow to cancel running workflows on PR close

**类型**: Pull Request

## 问题背景
Example: https://github.com/vllm-project/vllm-ascend/actions/runs/20735955959/job/59533181655 is still running after https://github.com/vllm-project/vllm-ascend/pull/5612 is closed.

And the action will be running for more than 2 hours, which needs to be cleanup.

It seems that the Github Aciton will not cancel it automatically, so I add this to cannel those PR related actions once it is closed.

Tested in https://github.com/pacoxu/pacoxu/actions/runs/20743173119.
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5646
- **作者**: pacoxu
- **创建时间**: 2026-01-06T08:25:27Z
- **关闭时间**: 2026-01-07T07:38:10Z
- **标签**: ci/build

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5646)
