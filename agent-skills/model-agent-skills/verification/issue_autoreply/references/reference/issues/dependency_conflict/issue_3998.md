# Issue #3998: [Bug]: vllm加载模型报错：AssertionError: camem allocator is not available

## 基本信息

- **编号**: #3998
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3998
- **创建时间**: 2025-11-05T06:10:49Z
- **关闭时间**: 2025-11-06T02:54:38Z
- **更新时间**: 2025-11-06T02:54:38Z
- **提交者**: @snowlts
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@k8s-node1:/home/ltaishuang/Gcore# python collect_env.py
INFO 11-05 14:00:28 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 11-05 14:00:28 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
/usr/local/python3.11.13/lib/python3.11/site-packages/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: ''If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source?
  warn(
INFO 11-05 14:00:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 11-05 14:00:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 11-05 14:00:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-05 14:00:29 [__init__.py:235] Platform plugin ascend is activated
/usr/local/python3.11.13/lib/python3.11/site-packages/torchvision/datapoints/__init__.py:12: UserWarning: The torchvision.datapoints and torchvision.transforms.v2 namespaces are still Beta. While we do not expect major breaking changes, some APIs may still change according to user feedback. Please submit any feedback you may have in this issue: https://github.com/pytorch/vision/issues/6753, and you can also check out https://github.com/pytorch/vision/issues/7319 to learn more about the APIs that we suspect might involve future changes. You can silence this warning by calling torchvision.disable_beta_transforms_warning().
  warnings.warn(_BETA_TRANSFORMS_WARNING)
/usr/local/python3.11.13/lib/python3.11/site-packages/torchvision/transforms/v2/__init__.py:54: UserWarning: The torchvision.datapoints and torchvision.transforms.v2 namespaces are still Beta. While we do not expect major breaking changes, some APIs may still change according to user feedback. Please submit any feedback you may have in this issue: https://github.com/pytorch/vision/issues/6753, and you can also check out https://github.com/pytorch/vision/issues/7319 to learn more about the APIs that we suspect might involve future changes. You can silence this warning by calling torchvision.disable_beta_transforms_warning().
  warnings.warn(_BETA_TRANSFORMS_WARNING)
Collecting environment information...
PyTorch version: 2.6.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 3.31.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 7265
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              64
Socket(s):                       4
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     3000.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       16 MiB (256 instances)
L1i cache:                       16 MiB (256 instances)
L2 cache:                        128 MiB (256 instances)
L3 cache:                        256 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
NUMA node4 CPU(s):               128-159
NUMA node5 CPU(s):               160-191
NUMA node6 CPU(s):               192-223
NUMA node7 CPU(s):               224-255
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.0
[pip3] pytorch-lightning==2.5.0.post0
[pip3] pyzmq==26.4.0
[pip3] rotary-embedding-torch==0.8.6
[pip3] torch==2.6.0+cpu
[pip3] torch_npu==2.6.0.post3
[pip3] torchmetrics==1.6.1
[pip3] torchvision==0.15.0
[pip3] transformers==4.52.3
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.2.dev0+g0740d1021.d20251105 (git sha: 0740d1021, date: 20251105)

ENV Variables:
VLLM_ALLOW_INSECURE_SERIALIZATION=1
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
VLLM_WORKER_MULTIPROC_METHOD=spawn
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
TORCHINDUCTOR_CACHE_DIR=/tmp/torchinductor_root


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.3        53                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          4487 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 100.1       53                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          4483 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 101.2       52                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          4482 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 100.4       54                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          4481 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 97.2        55                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          4481 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 98.3        54                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          4481 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 98.3        54                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          4481 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 91.5        54                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          4482 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 2698909       |                          | 600                     |
| 0       0                 | 2701550       |                          | 538                     |
+===========================+===============+====================================================+
| 1       0                 | 2698910       |                          | 600                     |
| 1       0                 | 2701551       |                          | 538                     |
+===========================+===============+====================================================+
| 2       0                 | 2701552       |                          | 538                     |
| 2       0                 | 2698911       |                          | 600                     |
+===========================+===============+====================================================+
| 3       0                 | 2698912       |                          | 600                     |
| 3       0                 | 2701553       |                          | 538                     |
+===========================+===============+====================================================+
| 4       0                 | 2698913       |                          | 600                     |
| 4       0                 | 2701554       |                          | 538                     |
+===========================+===============+====================================================+
| 5       0                 | 2698914       |                          | 600                     |
| 5       0                 | 2701555       |                          | 538                     |
+===========================+===============+====================================================+
| 6       0                 | 2698915       |                          | 600                     |
| 6       0                 | 2701556       |                          | 538                     |
+===========================+===============+====================================================+
| 7       0                 | 2701557       |                          | 538                     |
| 7       0                 | 2698917       |                          | 600                     |
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

vllm加载模型报错 
(RayWorkerWrapper pid=527478) WARNING 11-05 13:27:54 [camem.py:63] Failed to import vllm_ascend_C:/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so: undefined symbol: _ZN2fe13PlatFormInfos16GetCoreNumByTypeERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE. Sleep mode will be disabled.
(RayWorkerWrapper pid=527487) WARNING 11-05 13:27:54 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xffcfae5899d0>
(RayWorkerWrapper pid=527464) WARNING 11-05 13:27:54 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xffcfd83ee350>
(RayWorkerWrapper pid=527480) WARNING 11-05 13:27:54 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xffcfbe7f2590>
(RayWorkerWrapper pid=527428) INFO 11-05 13:27:54 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_6d742a00'), local_subscribe_addr='ipc:///tmp/ff03a7d3-0bdc-4d4e-8277-a89b61d00e37', remote_subscribe_addr=None, remote_addr_ipv6=False)
(RayWorkerWrapper pid=527428) INFO 11-05 13:27:55 [parallel_state.py:1065] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(RayWorkerWrapper pid=527432) INFO 11-05 13:27:55 [parallel_state.py:1065] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
(RayWorkerWrapper pid=527467) INFO 11-05 13:27:55 [parallel_state.py:1065] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
(RayWorkerWrapper pid=527474) INFO 11-05 13:27:55 [parallel_state.py:1065] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
/usr/local/python3.11.13/lib/python3.11/contextlib.py:191: ResourceWarning: Unclosed context <zmq.Context() at 0xffff1cb0ff50>
  exc.__traceback__ = traceback
ERROR 11-05 13:27:55 [core.py:515] EngineCore failed to start.
ERROR 11-05 13:27:55 [core.py:515] Traceback (most recent call last):
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core
ERROR 11-05 13:27:55 [core.py:515]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 11-05 13:27:55 [core.py:515]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 390, in __init__
ERROR 11-05 13:27:55 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 76, in __init__
ERROR 11-05 13:27:55 [core.py:515]     self.model_executor = executor_class(vllm_config)
ERROR 11-05 13:27:55 [core.py:515]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 287, in __init__
ERROR 11-05 13:27:55 [core.py:515]     super().__init__(*args, **kwargs)
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 53, in __init__
ERROR 11-05 13:27:55 [core.py:515]     self._init_executor()
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
ERROR 11-05 13:27:55 [core.py:515]     self._init_workers_ray(placement_group)
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
ERROR 11-05 13:27:55 [core.py:515]     self._run_workers("load_model",
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 522, in _run_workers
ERROR 11-05 13:27:55 [core.py:515]     ray_worker_outputs = ray.get(ray_worker_outputs)
ERROR 11-05 13:27:55 [core.py:515]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/auto_init_hook.py", line 21, in auto_init_wrapper
ERROR 11-05 13:27:55 [core.py:515]     return fn(*args, **kwargs)
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
ERROR 11-05 13:27:55 [core.py:515]     return func(*args, **kwargs)
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 2822, in get
ERROR 11-05 13:27:55 [core.py:515]     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
ERROR 11-05 13:27:55 [core.py:515]                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/ray/_private/worker.py", line 930, in get_objects
ERROR 11-05 13:27:55 [core.py:515]     raise value.as_instanceof_cause()
ERROR 11-05 13:27:55 [core.py:515] ray.exceptions.RayTaskError(AssertionError): ray::RayWorkerWrapper.execute_method() (pid=527432, ip=175.73.9.2, actor_id=3c9c27c5de0bdaa25836f5a302000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xffcfcd809b90>)
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 623, in execute_method
ERROR 11-05 13:27:55 [core.py:515]     raise e
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 614, in execute_method
ERROR 11-05 13:27:55 [core.py:515]     return run_method(self, method, args, kwargs)
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/utils.py", line 2671, in run_method
ERROR 11-05 13:27:55 [core.py:515]     return func(*args, **kwargs)
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 229, in load_model
ERROR 11-05 13:27:55 [core.py:515]     allocator = CaMemAllocator.get_instance()
ERROR 11-05 13:27:55 [core.py:515]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/device_allocator/camem.py", line 141, in get_instance
ERROR 11-05 13:27:55 [core.py:515]     assert camem_available, "camem allocator is not available"
ERROR 11-05 13:27:55 [core.py:515]            ^^^^^^^^^^^^^^^
ERROR 11-05 13:27:55 [core.py:515] AssertionError: camem allocator is not available


查看代码/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/device_allocator/camem.py
134     @staticmethod
135     def get_instance() -> "CaMemAllocator":
136         """
137         CaMemAllocator is a singleton class.
138         We cannot call the constructor directly.
139         Call this method to get the instance.
140         """
141         assert camem_available, "camem allocator is not available"
142         if CaMemAllocator.instance is None:
143             CaMemAllocator.instance = CaMemAllocator()
144         return CaMemAllocator.instance

 56 camem_available = False
 57 try:
 58     from vllm_ascend.vllm_ascend_C import (  # type: ignore # noqa: F401
 59         init_module, python_create_and_map, python_unmap_and_release)
 60     lib_name = find_loaded_library("vllm_ascend_C")
 61     camem_available = True
 62 except ImportError as e:
 63     logger.warning(
 64         "Failed to import vllm_ascend_C:%s. Sleep mode will be disabled. ", e)
 65     init_module = None
 66     python_create_and_map = None
 67     python_unmap_and_release = None
 68     lib_name = None
 69     libcudart = None

尝试在python交互界面import module，失败
>>> import torch
/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/__init__.py:312: UserWarning: On the interactive interface, the value of TASK_QUEUE_ENABLE is set to 0 by default.                      Do not set it to 1 to prevent some unknown errors
  warnings.warn("On the interactive interface, the value of TASK_QUEUE_ENABLE is set to 0 by default. \
>>> import vllm_ascend.vllm_ascend_C
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: /home/ltaishuang/Gcore/pips/vllm-ascend-0.9.1/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so: undefined symbol: _ZN5torch7LibraryC1ENS0_4KindESsSt8optionalIN3c1011DispatchKeyEEPKcj
