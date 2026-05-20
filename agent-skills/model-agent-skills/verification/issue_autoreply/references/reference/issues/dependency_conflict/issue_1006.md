# Issue #1006: [Bug]: vllm0.8.4+vllm_ascend0.8.4rc2（驱动24.1rc2，cann8.1rc1（cann8.0也试过），torch_npu2.5.1），离线能够跑起来，并发运行在线推理服务，算子库链接不到aclnnNonzeroV2

## 基本信息

- **编号**: #1006
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1006
- **创建时间**: 2025-05-29T04:52:09Z
- **关闭时间**: 2025-07-13T09:35:56Z
- **更新时间**: 2025-07-13T09:36:30Z
- **提交者**: @towy98
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm0.8.4+vllm_ascend0.8.4rc2（驱动24.1rc2，cann8.1rc1(cann8.0也试过)，torch_npu2.5.1）
```

</details>


### 🐛 Describe the bug

离线可以运行，在线服务并发测试时找不到对应算子库
call aclnnNonzeroV2 failed, detail:E39999: Inner Error!
E39999: [PID: 85141] 2025-05-29-12:09:01.468.164 The error from device(chipId:0, dieId:0), serial number is 3, an exception occurred during AICPU execution, stream_id:6, task_id:2895, errcode:11002, msg:open so failed.[FUNC:ProcessStarsAicpuErrorInfo][FILE:device_error_proc.cc][LINE:1479]
        TraceBack (most recent call last):
       Kernel task happen error, retCode=0x2a, [aicpu exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1356]
       AICPU Kernel task happen error, retCode=0x2a.[FUNC:GetError][FILE:stream.cc][LINE:1124]
       Aicpu kernel execute failed, device_id=0, stream_id=6, task_id=2895, errorCode=2a.[FUNC:PrintAicpuErrorInfo][FILE:davinci_kernel_task.cc][LINE:1120]
       Aicpu kernel execute failed, device_id=0, stream_id=6, task_id=2895, fault op_name=[FUNC:GetError][FILE:stream.cc][LINE:1124]
       rtStreamSynchronize execute failed, reason=[aicpu exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       rtStreamSynchronize failed. stream: 0x5062fad0
       Kernel Run failed. opType: 51, NonZero
       launch failed for NonZero, errno:507018.

RuntimeError('The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnNonzeroV2.\nSince the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.\nNote: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.\n[ERROR] 2025-05-29-12:09:01 (PID:85141, Device:0, RankID:-1) ERR00100 PTA call acl api failed.\n')

