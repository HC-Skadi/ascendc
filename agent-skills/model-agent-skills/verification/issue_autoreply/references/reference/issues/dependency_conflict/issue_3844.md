# Issue #3844: [Bug]: Nightly test failed

## 基本信息

- **编号**: #3844
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3844
- **创建时间**: 2025-10-29T01:24:40Z
- **关闭时间**: 2026-01-07T00:53:10Z
- **更新时间**: 2026-01-07T00:53:10Z
- **提交者**: @wangxiyuan
- **评论数**: 2

## 标签

bug; nightly

## 问题描述

We notice that there are some function broken with nightly test. They should be fixed ASAP.

Test env: vLLM v0.11.0, vLLM Ascend main, torch-npu 0724, CANN 8.2rc1

1. qwen3-235b-a22b-w8a8-eplb @offline893 
    https://github.com/vllm-project/vllm-ascend/actions/runs/18848144365/job/53777583508 accuracy test failure 
2. deepseek-r1-w8a8-eplb  @offline893 
    https://github.com/vllm-project/vllm-ascend/actions/runs/18848144365/job/53777583497 function failure
3. deepseek-r1-0528-w8a8-prefix-cache performance
    https://github.com/vllm-project/vllm-ascend/actions/runs/18914892494/job/53995459351
