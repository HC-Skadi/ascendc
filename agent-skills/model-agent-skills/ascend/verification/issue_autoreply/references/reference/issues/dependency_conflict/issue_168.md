# Issue #168: [Usage]: Error running on multiple nodes

## 基本信息

- **编号**: #168
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/168
- **创建时间**: 2025-02-26T02:58:28Z
- **关闭时间**: 2025-02-26T11:23:31Z
- **更新时间**: 2025-02-26T13:34:43Z
- **提交者**: @ApsarasX
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

```txt
npu-smi 24.1.0                   Version: 24.1.0
```
```txt
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/x86_64-linux
```
```txt
torch==2.5.1+cpu
torch-npu==2.5.1.dev20250218
transformers==4.49.0
ray==2.42.1
```

### How would you like to use vllm on ascend

I am attempting to run the bf16 version of DeepSeek-V3 using 2 machines, with each node equipped with 16 910B NPUs, totaling 32 NPUs across all nodes.

The followings are my operational steps(from https://vllm-ascend.readthedocs.io/en/latest/tutorials.html#online-serving-on-multi-machine):
1. on the head node 
```sh
export VLLM_HOST_IP=$POD_IP
export HCCL_IF_IP=$POD_IP
export HCCL_CONNECT_TIMEOUT=120
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ray start --head --num-gpus=16 --port=6379
```
2. on the worker node
```sh
export VLLM_HOST_IP=$POD_IP
export HCCL_IF_IP=$POD_IP
export HCCL_CONNECT_TIMEOUT=120
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1 
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ray start --address=$HEAD_NODE_IP:6379 --num-gpus=16 --node-ip-address=$POD_IP
```
3. on each node
```sh
vllm serve /root/DeepSeek-V3 \
    --served_model_name DeepSeek-V3 \
    -tp 16 -pp 2 \
    --distributed_executor_backend "ray" \
    --max-model-len 1024 \
    --trust-remote-code
```

Then, I encountered the following error
```txt
(RayWorkerWrapper pid=120290) WARNING 02-26 15:54:01 utils.py:549] Overwriting environment variable ASCEND_RT_VISIBLE_DEVICES from '4' to '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15'
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] Error executing method 'init_device'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] Traceback (most recent call last):
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]   File "/root/vllm/vllm/worker/worker_base.py", line 566, in execute_method
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]     return run_method(target, method, args, kwargs)
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]   File "/root/vllm/vllm/utils.py", line 2220, in run_method
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]     return func(*args, **kwargs)
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]   File "/root/vllm-ascend/vllm_ascend/worker.py", line 173, in init_device
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]     current_platform.set_device(self.device)
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]   File "/root/vllm-ascend/vllm_ascend/platform.py", line 83, in set_device
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]     torch.npu.set_device(device)
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]   File "/opt/conda/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 58, in set_device
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]     torch_npu._C._npu_setDevice(device_id)
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] RuntimeError: Initialize:torch_npu/csrc/core/npu/sys_ctrl/npu_sys_ctrl.cpp:226 NPU function error: c10_npu::SetDevice(device_id_), error code is 107001
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] [ERROR] 2025-02-26-15:54:06 (PID:120292, Device:0, RankID:0) ERR00100 PTA call acl api failed
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] [Error]: Invalid device ID.
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         Check whether the device ID is valid.
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] EE1001: [PID: 120292] 2025-02-26-15:54:03.062.588 The argument is invalid.Reason: Set visible device failed, invalid device=3, input visible devices:3
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         TraceBack (most recent call last):
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         rtSetDevice execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         open device 3 failed, runtime result = 107001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5372]
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(RayWorkerWrapper pid=120292) ERROR 02-26 15:54:06 worker_base.py:574] 
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:30] Available plugins for group vllm.platform_plugins: [repeated 31x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:32] name=ascend, value=vllm_ascend:register [repeated 31x across cluster]
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. [repeated 31x across cluster]
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. [repeated 31x across cluster]
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:44] plugin ascend loaded. [repeated 31x across cluster]
(pid=80888, ip=...) INFO 02-26 15:54:01 __init__.py:181] Platform plugin ascend is activated [repeated 31x across cluster]
(RayWorkerWrapper pid=120276) WARNING 02-26 15:54:01 utils.py:549] Overwriting environment variable ASCEND_RT_VISIBLE_DEVICES from '13' to '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15' [repeated 14x across cluster]
```

It seems that vllm-ascend did not recognize the other machine
