# Issue #3479: [Bug]: vllm-ascend:v0.11.0rc0 310p拉起 Qwen3-4B失败

## 基本信息

- **编号**: #3479
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3479
- **创建时间**: 2025-10-15T08:44:59Z
- **关闭时间**: 2025-12-23T11:22:24Z
- **更新时间**: 2025-12-31T07:53:13Z
- **提交者**: @ZhuLeiguang1992
- **评论数**: 3

## 标签

bug; 310p

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
310p 
quay.io/ascend/vllm-ascend:v0.11.0rc0-310p-openeuler
Qwen3-4B
npu-smi 25.2.0                                   Version: 25.2.0    
```

</details>


### 🐛 Describe the bug

docker run --rm -it -d --privileged=true --shm-size 32g  -v --device=/dev/davinci_manager --device=/dev/devmm_svm --device=/dev/hisi_hdc -v /etc/hccn.conf:/etc/hccn.conf -v /etc/localtime:/etc/localtime -v /usr/local/Ascend/driver:/usr/local/Ascend/driver -v /var/log/npu/:/usr/slog -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /data/:/data/  --name xxx-vllm -v /home:/home quay.io/ascend/vllm-ascend:v0.11.0rc0-310p-openeuler /bin/bash

vllm serve /home/models/Qwen3/Qwen3-4B --served-model-name qwen2.5_7b --tensor-parallel-size 1 --max-model-len 4096 --gpu-memory-utilization 0.8 --enforce-eager --port 8080 --host 0.0.0.0


(EngineCore_DP0 pid=3132) INFO 10-15 16:32:10 [default_loader.py:267] Loading weights took 16.92 seconds
(EngineCore_DP0 pid=3132) INFO 10-15 16:32:11 [model_runner_v1.py:2661] Loading model weights took 7.5553 GB
(EngineCore_DP0 pid=3132) INFO 10-15 16:32:15 [worker_v1.py:234] Available memory: 26954181529, total memory: 46431260672
(EngineCore_DP0 pid=3132) INFO 10-15 16:32:15 [kv_cache_utils.py:1087] GPU KV cache size: 182,784 tokens
(EngineCore_DP0 pid=3132) INFO 10-15 16:32:15 [kv_cache_utils.py:1091] Maximum concurrency for 4,096 tokens per request: 44.62x
[rank0]:[W1015 16:32:16.549993460 compiler_depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operator())
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 73, in initialize_from_config
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     self.collective_rpc("initialize_from_config",
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3121, in run_method
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 254, in initialize_from_config
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 336, in initialize_from_config
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     self.model_runner.initialize_kv_cache(kv_cache_config)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2709, in initialize_kv_cache
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3043, in initialize_kv_cache_tensors
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     k_cache = self._convert_torch_format(k_cache)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2673, in _convert_torch_format
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     tensor = torch_npu.npu_format_cast(tensor, ACL_FORMAT)
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     return self._op(*args, **(kwargs or {}))
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] [ERROR] 2025-10-15-16:32:16 (PID:3132, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] [Error]: System Direct Memory Access (DMA) hardware execution error. 
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         Rectify the fault based on the error information in the ascend log.
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] EL0004: [PID: 3132] 2025-10-15-16:32:16.417.528 Failed to allocate memory.
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         Possible Cause: Available memory is insufficient.
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         Solution: Close applications not in use.
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         TraceBack (most recent call last):
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         The error from device(4), serial number is 2. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         Memory async copy failed, device_id=4, stream_id=7, task_id=1303, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=748683264[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] 
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] 
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] DEVICE[4] PID[3132]: 
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708] EXCEPTION STREAM:
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   Exception info:TGID=1933574, model id=65535, stream id=7, stream phase=3
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=11, stream_id=7
(EngineCore_DP0 pid=3132) ERROR 10-15 16:32:16 [core.py:708]     Other info[0]:time=2025-10-15-16:32:16.984.044, function=int_process_hwts_sdma_error, line=1381, error code=0x20b
(EngineCore_DP0 pid=3132) Process EngineCore_DP0:
(EngineCore_DP0 pid=3132) Traceback (most recent call last):
(EngineCore_DP0 pid=3132)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=3132)     self.run()
(EngineCore_DP0 pid=3132)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=3132)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=3132)     raise e
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3132)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3132)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3132)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=3132)     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
(EngineCore_DP0 pid=3132)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 73, in initialize_from_config
(EngineCore_DP0 pid=3132)     self.collective_rpc("initialize_from_config",
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=3132)     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=3132)             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3121, in run_method
(EngineCore_DP0 pid=3132)     return func(*args, **kwargs)
(EngineCore_DP0 pid=3132)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 254, in initialize_from_config
(EngineCore_DP0 pid=3132)     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(EngineCore_DP0 pid=3132)     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 336, in initialize_from_config
(EngineCore_DP0 pid=3132)     self.model_runner.initialize_kv_cache(kv_cache_config)
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2709, in initialize_kv_cache
(EngineCore_DP0 pid=3132)     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(EngineCore_DP0 pid=3132)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3043, in initialize_kv_cache_tensors
(EngineCore_DP0 pid=3132)     k_cache = self._convert_torch_format(k_cache)
(EngineCore_DP0 pid=3132)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2673, in _convert_torch_format
(EngineCore_DP0 pid=3132)     tensor = torch_npu.npu_format_cast(tensor, ACL_FORMAT)
(EngineCore_DP0 pid=3132)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(EngineCore_DP0 pid=3132)     return self._op(*args, **(kwargs or {}))
(EngineCore_DP0 pid=3132)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3132) RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
(EngineCore_DP0 pid=3132) [ERROR] 2025-10-15-16:32:16 (PID:3132, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(EngineCore_DP0 pid=3132) [Error]: System Direct Memory Access (DMA) hardware execution error. 
(EngineCore_DP0 pid=3132)         Rectify the fault based on the error information in the ascend log.
(EngineCore_DP0 pid=3132) EL0004: [PID: 3132] 2025-10-15-16:32:16.417.528 Failed to allocate memory.
(EngineCore_DP0 pid=3132)         Possible Cause: Available memory is insufficient.
(EngineCore_DP0 pid=3132)         Solution: Close applications not in use.
(EngineCore_DP0 pid=3132)         TraceBack (most recent call last):
(EngineCore_DP0 pid=3132)         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_DP0 pid=3132)         The error from device(4), serial number is 2. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
(EngineCore_DP0 pid=3132)         Memory async copy failed, device_id=4, stream_id=7, task_id=1303, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=748683264[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_DP0 pid=3132)         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_DP0 pid=3132)         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_DP0 pid=3132) 
(EngineCore_DP0 pid=3132) 
(EngineCore_DP0 pid=3132) DEVICE[4] PID[3132]: 
(EngineCore_DP0 pid=3132) EXCEPTION STREAM:
(EngineCore_DP0 pid=3132)   Exception info:TGID=1933574, model id=65535, stream id=7, stream phase=3
(EngineCore_DP0 pid=3132)   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=11, stream_id=7
(EngineCore_DP0 pid=3132)     Other info[0]:time=2025-10-15-16:32:16.984.044, function=int_process_hwts_sdma_error, line=1381, error code=0x20b
[rank0]:[W1015 16:32:18.560418550 compiler_depend.ts:528] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:18.234.552 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W1015 16:32:18.562668610 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:18.237.049 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1015 16:32:18.564206620 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:18.238.673 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1015 16:32:20.400254360 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.074.608 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1015 16:32:20.401777530 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.076.304 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1015 16:32:20.403205430 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.077.747 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1015 16:32:20.404655560 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.079.202 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1015 16:32:20.406086070 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.080.631 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1015 16:32:20.407525460 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 3132] 2025-10-15-16:32:20.082.081 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
(APIServer pid=2994) Traceback (most recent call last):
(APIServer pid=2994)   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
(APIServer pid=2994)     sys.exit(main())
(APIServer pid=2994)              ^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=2994)     args.dispatch_function(args)
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=2994)     uvloop.run(run_server(args))
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=2994)     return runner.run(wrapper())
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=2994)     return self._loop.run_until_complete(task)
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=2994)     return await main
(APIServer pid=2994)            ^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=2994)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=2994)     async with build_async_engine_client(
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=2994)     return await anext(self.gen)
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=2994)     async with build_async_engine_client_from_engine_args(
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=2994)     return await anext(self.gen)
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=2994)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=2994)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=2994)     return fn(*args, **kwargs)
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=2994)     return cls(
(APIServer pid=2994)            ^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=2994)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=2994)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=2994)     return AsyncMPClient(*client_args)
(APIServer pid=2994)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=2994)     super().__init__(
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=2994)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=2994)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=2994)     next(self.gen)
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=2994)     wait_for_engine_startup(
(APIServer pid=2994)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=2994)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=2994) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=2994) [ERROR] 2025-10-15-16:32:29 (PID:2994, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
