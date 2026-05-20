# Issue #1044: [Bug][V1]: Failed to start Qwen/Qwen2.5-VL-7B-Instruct accuracy serve

## 基本信息

- **编号**: #1044
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1044
- **创建时间**: 2025-06-03T02:01:15Z
- **关闭时间**: 2025-07-13T09:46:19Z
- **更新时间**: 2025-07-13T09:46:19Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

Failed to start Qwen/Qwen2.5-VL-7B-Instruct accuracy serve

[1] https://github.com/vllm-project/vllm-ascend/actions/runs/15397909461/job/43323198963?pr=1040
[2] https://github.com/vllm-project/vllm-ascend/actions/runs/15397909461?pr=1040


### 🐛 Describe the bug

```
(VllmWorker rank=0 pid=4482) INFO 06-02 16:56:09 [model_runner_v1.py:1048] Encoder cache will be initialized with a budget of 16384 tokens, and profiled with 1 image items of the maximum feature size.
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
(VllmWorker rank=3 pid=4488) Exception in thread Thread-1:
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
Error:  TBE Subprocess[task_distribute] raise error[], main process disappeared!
ERROR 06-02 17:15:31 [multiproc_executor.py:135] Worker proc VllmWorker-3 died unexpectedly, shutting down executor.
Error: Executing the custom container implementation failed. Please contact your self hosted runner administrator.
```
