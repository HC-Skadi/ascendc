# Issue #4456: [Bug]: Ray start failed with multi-node case

## 基本信息

- **编号**: #4456
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4456
- **创建时间**: 2025-11-26T06:55:59Z
- **关闭时间**: 2025-12-15T06:22:03Z
- **更新时间**: 2025-12-15T06:22:03Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Versions of relevant libraries:
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.1.2
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.11.2
vLLM Ascend Version: 0.1.dev1433+gfcfb3a0e9 (git sha: fcfb3a0e9)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 89.4        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2862 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 85.2        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2862 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 85.0        38                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2855 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 88.2        40                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2855 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 87.6        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2840 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 86.8        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2839 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 87.2        37                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2655 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 86.1        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2838 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

Bug import PR:https://github.com/vllm-project/vllm-ascend/pull/4400

Reproduce script:
[Multi-Node-Ray](https://docs.vllm.ai/projects/ascend/en/latest/tutorials/multi_node_ray.html#)


Error information:
```
(EngineCore_DP0 pid=300679) (RayWorkerWrapper pid=300872) INFO 11-24 08:50:32 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
(EngineCore_DP0 pid=300679) (RayWorkerWrapper pid=300872) WARNING 11-24 08:50:33 [worker_base.py:301] Missing `shared_worker_lock` argument from executor. This argument is needed for mm_processor_cache_type='shm'.
(EngineCore_DP0 pid=300679) (RayWorkerWrapper pid=300872) INFO 11-24 08:50:33 [utils.py:973] FLASHCOMM2 not enable.
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842] EngineCore failed to start.
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842] Traceback (most recent call last):
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 833, in run_engine_core
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 606, in __init__
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     super().__init__(
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 102, in __init__
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self._init_executor()
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/ray_executor.py", line 97, in _init_executor
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self._init_workers_ray(placement_group)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/ray_executor.py", line 370, in _init_workers_ray
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self.collective_rpc("init_device")
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/ray_executor.py", line 493, in collective_rpc
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     return ray.get(ray_worker_outputs, timeout=timeout)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     return fn(*args, **kwargs)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     return func(*args, **kwargs)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 2858, in get
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 958, in get_objects
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     raise value.as_instanceof_cause()
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842] ray.exceptions.RayTaskError(AssertionError): ray::RayWorkerWrapper.execute_method() (pid=300878, ip=172.22.0.188, actor_id=ccad69f02f06cafa8981145201000000, repr=<vllm.v1.executor.ray_utils.RayWorkerWrapper object at 0xffcfbc328810>)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 343, in execute_method
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     raise e
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 332, in execute_method
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     return run_method(self, method, args, kwargs)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/serial_utils.py", line 479, in run_method
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     return func(*args, **kwargs)
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 324, in init_device
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self.worker.init_device()  # type: ignore
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 236, in init_device
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     self.device = self._init_device()
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]                   ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 220, in _init_device
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]     assert self.parallel_config.local_world_size <= visible_device_count, (
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=300679) ERROR 11-24 08:50:34 [core.py:842] AssertionError: local_world_size (32) must be less than or equal to the number of visible devices (16).

```
