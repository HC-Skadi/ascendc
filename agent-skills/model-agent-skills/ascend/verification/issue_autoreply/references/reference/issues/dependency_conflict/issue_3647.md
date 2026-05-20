# Issue #3647: [Bug]: NPU Context Initialization Failed when Loading Model Weights

## 基本信息

- **编号**: #3647
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3647
- **创建时间**: 2025-10-23T02:26:49Z
- **关闭时间**: 2025-10-28T07:35:57Z
- **更新时间**: 2025-10-28T07:35:57Z
- **提交者**: @tinylk
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

npu-smi info
```
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 93.3        49                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          53665/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 95.0        51                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          53653/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 93.8        50                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 98.4        51                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          53651/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 96.1        49                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 97.6        50                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 92.9        50                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 101.2       51                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          53652/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 99.7        50                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          53416/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 99.4        51                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 100.9       49                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 93.0        51                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          53417/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 93.8        49                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 99.3        50                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3394 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 93.7        49                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 99.8        51                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3399 / 65536         |
+===========================+===============+====================================================+
```
vLLM Version: vllm v0.10.2
Base Image: vllm-ascend v0.10.2rc1
NPU Driver: Ascend CANN Toolkit
PyTorch: torch==2.7.1+cpu torch-npu==2.7.1.dev20250724 torchvision==0.22.1+cpu 
Model: Qwen2.5-7B-Instruct

### 🐛 Describe the bug

When deploying model inference service using a custom-built Docker image, the service fails during model weight loading with NPU context initialization errors. The same deployment works fine with the official vllm-ascend:v0.10.2rc1 image. Important Note: The main components in the custom image (torch-npu, vllm-ascend, vllm, transformers versions) are consistent with the official image, but the NPU context initialization still fails.
Error Log
```
Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00<? it/s]
2025-10-15 11:11:50.834 ERROR vllm.model_executor.model_loader.pallas_loader
File ['/mnt/pvc/model/Qwen2.5/Qwen2.5-7B-Instruct/model-00002-of-00004.safetensors'] generated an exception: copy_between_host_and_device_opapi

torch_npu/csrc/aten/ops/op_api/CopyKernelOpApi.cpp:54 NPU function error: aclrtMemcpy, error code is 107002

[ERROR] 2025-10-15-11:11:50 (PID:407, Device:0, RankID:-1) ERROR100 PTA call acl api failed
[Error]: The context is empty.
E:161] Check whether acl.rt.set_context or acl.rt.set_device is called.

ctx is NULL! [FUNC: StreamSynchronize] [FILE:api_impl.cc] [LINE: 1507]
The argument is invalid.Reason: rtStreamSynchronize execute failed, reason=[context pointer null]
```

The custom Dockerfile:

> Uses multi-stage build from official vllm-ascend image
> Copies Ascend driver and toolkit from the official image
> Installs torch-npu and vllm-ascend packages
> Sets up environment variables and library paths
