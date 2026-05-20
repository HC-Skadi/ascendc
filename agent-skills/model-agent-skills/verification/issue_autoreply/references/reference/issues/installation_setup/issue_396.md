# Issue #396: [RFC]: Join the MultiLora and MultiLora Dynammic Serving feature develop

## 基本信息

- **编号**: #396
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/396
- **创建时间**: 2025-03-26T03:22:44Z
- **关闭时间**: 2025-05-20T11:21:40Z
- **更新时间**: 2025-05-20T11:21:41Z
- **提交者**: @ZhengJun9
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

We would like to join the MultiLora and MultiLora Dynammic Serving feature develop. 

### Proposed Change.

We want to implement the following：
1、The MultiLora usage should be the same as vllm, see https://docs.vllm.ai/en/latest/features/lora.html
2、What's more, for production environments use, the dynamically serving LoRA Adapters should be persistence. That means when the docker is restarted in some case, the load/unload lora adapters should not  roll back to the initial state.

### Feedback Period.

we plan to finnish this work in two weeks

### CC List.
[Yikun](https://github.com/Yikun)
[wangxiyuan](https://github.com/wangxiyuan)

### Any Other Things.

_No response_
