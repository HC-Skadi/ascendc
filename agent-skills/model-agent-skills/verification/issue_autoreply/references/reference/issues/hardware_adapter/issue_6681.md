# Issue #6681: Add Worker Interface:check_health

**类型**: Pull Request

## 问题背景
This pull request introduces a new capability to monitor the health of NPU cards directly from the Worker class. This enhancement allows for proactive detection of NPU issues by executing the npu-smi command, improving system reliability and operational visibility within the vllm_ascend worker environment.
more details see https://github.com/vllm-project/vllm-ascend/issues/4112
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/13397841ab469cecf1ed425c3f52a9ffc38139b5


## 基本信息
- **编号**: #6681
- **作者**: luomin2005
- **创建时间**: 2026-02-11T06:09:08Z
- **关闭时间**: 2026-02-11T07:24:48Z
- **标签**: 无

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6681)
