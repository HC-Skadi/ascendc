# Issue #4229: [Bug]: AttributeError: '_OpNamespace' '_C' object has no attribute

## 基本信息

- **编号**: #4229
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4229
- **创建时间**: 2025-11-17T09:53:42Z
- **关闭时间**: 2025-12-29T11:08:09Z
- **更新时间**: 2025-12-29T11:08:09Z
- **提交者**: @leo-pony
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov  2 2025, 08:46:33) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h2056.eulerosv2r10.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc8.dev1+g1246b19b4.d20251117 (git sha: 1246b19b4, date: 20251117)
vLLM Ascend Version: 0.1.dev1373+gd1497b421.d20251117 (git sha: d1497b421, date: 20251117)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
VLLM_WORKER_MULTIPROC_METHOD=spawn
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:254
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
| 0     910B4               | OK            | 89.3        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2861 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 85.0        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2854 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 84.9        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2852 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 88.2        40                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2852 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 87.6        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2840 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 86.8        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2839 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 87.1        36                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2655 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 86.0        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2837 / 32768         |
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

Reproduce scripts:
```python
pytest -sv tests/e2e/singlecard/test_completion_with_prompt_embeds.py::test_single_prompt_embeds_inference[Qwen/Qwen2.5-0.5B-Instruct]
```

Error information:
```
(EngineCore_DP0 pid=3977) Process EngineCore_DP0:
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854] EngineCore failed to start.
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854] Traceback (most recent call last):
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 845, in run_engine_core
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) Traceback (most recent call last):
(EngineCore_DP0 pid=3977)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=3977)     self.run()
(EngineCore_DP0 pid=3977)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=3977)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 858, in run_engine_core
(EngineCore_DP0 pid=3977)     raise e
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 845, in run_engine_core
(EngineCore_DP0 pid=3977)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3977)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 613, in __init__
(EngineCore_DP0 pid=3977)     super().__init__(
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 101, in __init__
(EngineCore_DP0 pid=3977)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3977)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=3977)     self._init_executor()
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=3977)     self.driver_worker.load_model()
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 339, in load_model
(EngineCore_DP0 pid=3977)     self.model_runner.load_model()
(EngineCore_DP0 pid=3977)   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3666, in load_model
(EngineCore_DP0 pid=3977)     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=3977)                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 613, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     super().__init__(
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 101, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self._init_executor()
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/uniproc_executor.py", line 48, in _init_executor
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self.driver_worker.load_model()
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 339, in load_model
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self.model_runner.load_model()
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3666, in load_model
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 130, in get_model
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     return loader.load_model(vllm_config=vllm_config, model_config=model_config)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 49, in load_model
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     model = initialize_model(
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]             ^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/utils.py", line 55, in initialize_model
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     return model_class(vllm_config=vllm_config, prefix=prefix)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2.py", line 486, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     self.model = Qwen2Model(
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]                  ^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 293, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     TorchCompileWrapperWithCustomDispatcher.__init__(
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/wrapper.py", line 42, in __init__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     backend = vllm_config.compilation_config.init_backend(vllm_config)
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/config/compilation.py", line 696, in init_backend
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     from vllm.compilation.backends import VllmBackend
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/backends.py", line 40, in <module>
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     from .pass_manager import PostGradPassManager
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/pass_manager.py", line 28, in <module>
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     from .sequence_parallelism import SequenceParallelismPass
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/sequence_parallelism.py", line 21, in <module>
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     from .matcher_utils import MatcherFusedAddRMSNorm, MatcherQuantFP8, MatcherRMSNorm
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/matcher_utils.py", line 24, in <module>
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     RMS_OP = torch.ops._C.rms_norm.default
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1267, in __getattr__
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854]     raise AttributeError(
(EngineCore_DP0 pid=3977) ERROR 11-17 01:32:30 [core.py:854] AttributeError: '_OpNamespace' '_C' object has no attribute 'rms_norm'
```
