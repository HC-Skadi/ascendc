# Issue #924: [Bug]: TP8DP2下RuntimeError: Engine core initialization failed. See root cause above.

## 基本信息

- **编号**: #924
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/924
- **创建时间**: 2025-05-22T03:53:49Z
- **关闭时间**: 2026-03-03T00:15:27Z
- **更新时间**: 2026-03-03T00:15:27Z
- **提交者**: @Yanguan619
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
# python collect_env.py
INFO 05-22 11:36:11 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-22 11:36:11 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-22 11:36:11 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-22 11:36:11 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-22 11:36:11 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-22 11:36:11 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-22 11:36:11 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-22 11:36:11 [__init__.py:44] plugin ascend loaded.
INFO 05-22 11:36:11 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-22 11:36:12 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib64/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: openEuler 24.03 (LTS) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.38

Python version: 3.11.6 (main, Feb 19 2025, 18:13:39) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS Model name:                    Kunpeng 920 7285Z To be filled by O.E.M. CPU @ 3.0GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        3000.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-79
NUMA node1 CPU(s):                  80-159
NUMA node2 CPU(s):                  160-239
NUMA node3 CPU(s):                  240-319
NUMA node4 CPU(s):                  320-399
NUMA node5 CPU(s):                  400-479
NUMA node6 CPU(s):                  480-559
NUMA node7 CPU(s):                  560-639
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] mindietorch==2.0rc1+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] onnx==1.17.0
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.6.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.2
[conda] Could not collect
vLLM Version: 0.8.5
vLLM Ascend Version: 0.8.5rc2.dev38+gb4d6672 (git sha: b4d6672)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_LOG_TO_STDOUT=0
ATB_LOG_TO_FILE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=16
ATB_LOG_TO_FILE_FLUSH=0
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_GLOBAL_EVENT_ENABLE=0
ATB_CONTEXT_HOSTTILING_RING=1
ATB_OPERATION_EXECUTE_ASYNC=1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_CONTEXT_HOSTTILING_SIZE=102400
ASCEND_GLOBAL_LOG_LEVEL=3
ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/aie_ascendc:/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/customize:
ASCEND_DOCKER_RUNTIME=True
PYTORCH_INSTALL_PATH=/usr/local/lib64/python3.11/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/local/lib64/python3.11/site-packages/torch_npu
ATB_SPEED_HOME_PATH=/usr/local/Ascend/atb-models
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/lib64:/lib:/lib:/usr/local/Ascend/atb-models/lib:/usr/local/Ascend/mindie/latest/mindie-llm/lib:/usr/local/Ascend/mindie/latest/mindie-llm/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-service/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-torch/lib:/usr/local/Ascend/mindie/latest/mindie-rt/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_USE_TILING_COPY_STREAM=0
ATB_LOG_LEVEL=ERROR
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1                 Version: 25.0.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 160.7       45                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3103 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           45                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 167.2       44                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3089 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           45                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 162.0       48                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3092 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           49                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 179.1       48                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3101 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           48                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 160.4       45                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3097 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           44                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2892 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 160.4       45                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3098 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           45                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2892 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 172.9       49                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3104 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           48                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 169.7       47                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3107 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           48                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2883 / 65536         |
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
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export USING_LCCL_COM=1
export VLLM_USE_V1=1

python -m vllm.entrypoints.openai.api_server \
    --served-model-name DeepSeek-R1-Distill-Qwen-32B \
    --model /home/weights/DeepSeek-R1-Distill-Qwen-32B/ \
    --trust-remote-code \
    --block-size 128 \
    --max-num-seqs 128 \
    --max-model-len 8192 \
    --gpu-memory-utilization=0.9 \
    --tensor-parallel-size 8 \
    --port 1025 \
    -dp 2 \
    --additional-config '{"ascend_scheduler_config": {}, "enable_graph_mode": true}'
```

```log
INFO 05-22 11:41:52 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-22 11:41:53 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib64/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 05-22 11:41:53 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib64/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396] EngineCore failed to start.
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396] Traceback (most recent call last):
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 385, in run_engine_core
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 604, in __init__
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/config.py", line 1671, in stateless_init_dp_group
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     dp_group = stateless_init_torch_distributed_process_group(
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/distributed/utils.py", line 321, in stateless_init_torch_distributed_process_group
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     pg: ProcessGroup = ProcessGroup(
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]                        ^^^^^^^^^^^^^
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396] TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     1. torch._C._distributed_c10d.ProcessGroup(arg0: int, arg1: int)
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]     2. torch._C._distributed_c10d.ProcessGroup(arg0: torch._C._distributed_c10d.Store, arg1: int, arg2: int, arg3: c10d::ProcessGroup::Options)
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396]
(EngineCore_1 pid=382) ERROR 05-22 11:41:54 [core.py:396] Invoked with: <torch.distributed.distributed_c10d.PrefixStore object at 0xfffdffbd70b0>, 1, 2
(EngineCore_1 pid=382) Process EngineCore_1:
(EngineCore_1 pid=382) Traceback (most recent call last):
(EngineCore_1 pid=382)   File "/usr/lib64/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_1 pid=382)     self.run()
(EngineCore_1 pid=382)   File "/usr/lib64/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_1 pid=382)     self._target(*self._args, **self._kwargs)
(EngineCore_1 pid=382)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 400, in run_engine_core
(EngineCore_1 pid=382)     raise e
(EngineCore_1 pid=382)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 385, in run_engine_core
(EngineCore_1 pid=382)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_1 pid=382)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 604, in __init__
(EngineCore_1 pid=382)     self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()
(EngineCore_1 pid=382)                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382)   File "/usr/local/lib64/python3.11/site-packages/vllm/config.py", line 1671, in stateless_init_dp_group
(EngineCore_1 pid=382)     dp_group = stateless_init_torch_distributed_process_group(
(EngineCore_1 pid=382)                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=382)   File "/usr/local/lib64/python3.11/site-packages/vllm/distributed/utils.py", line 321, in stateless_init_torch_distributed_process_group
(EngineCore_1 pid=382)     pg: ProcessGroup = ProcessGroup(
(EngineCore_1 pid=382)                        ^^^^^^^^^^^^^
(EngineCore_1 pid=382) TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
(EngineCore_1 pid=382)     1. torch._C._distributed_c10d.ProcessGroup(arg0: int, arg1: int)
(EngineCore_1 pid=382)     2. torch._C._distributed_c10d.ProcessGroup(arg0: torch._C._distributed_c10d.Store, arg1: int, arg2: int, arg3: c10d::ProcessGroup::Options)
(EngineCore_1 pid=382)
(EngineCore_1 pid=382) Invoked with: <torch.distributed.distributed_c10d.PrefixStore object at 0xfffdffbd70b0>, 1, 2
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396] EngineCore failed to start.
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396] Traceback (most recent call last):
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 385, in run_engine_core
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 604, in __init__
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/config.py", line 1671, in stateless_init_dp_group
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     dp_group = stateless_init_torch_distributed_process_group(
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]   File "/usr/local/lib64/python3.11/site-packages/vllm/distributed/utils.py", line 321, in stateless_init_torch_distributed_process_group
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     pg: ProcessGroup = ProcessGroup(
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]                        ^^^^^^^^^^^^^
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396] TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     1. torch._C._distributed_c10d.ProcessGroup(arg0: int, arg1: int)
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]     2. torch._C._distributed_c10d.ProcessGroup(arg0: torch._C._distributed_c10d.Store, arg1: int, arg2: int, arg3: c10d::ProcessGroup::Options)
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396]
(EngineCore_0 pid=381) ERROR 05-22 11:41:54 [core.py:396] Invoked with: <torch.distributed.distributed_c10d.PrefixStore object at 0xfffe05d1b230>, 0, 2
(EngineCore_0 pid=381) Process EngineCore_0:
(EngineCore_0 pid=381) Traceback (most recent call last):
(EngineCore_0 pid=381)   File "/usr/lib64/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_0 pid=381)     self.run()
(EngineCore_0 pid=381)   File "/usr/lib64/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_0 pid=381)     self._target(*self._args, **self._kwargs)
(EngineCore_0 pid=381)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 400, in run_engine_core
(EngineCore_0 pid=381)     raise e
(EngineCore_0 pid=381)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 385, in run_engine_core
(EngineCore_0 pid=381)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=381)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381)   File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core.py", line 604, in __init__
(EngineCore_0 pid=381)     self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()
(EngineCore_0 pid=381)                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381)   File "/usr/local/lib64/python3.11/site-packages/vllm/config.py", line 1671, in stateless_init_dp_group
(EngineCore_0 pid=381)     dp_group = stateless_init_torch_distributed_process_group(
(EngineCore_0 pid=381)                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=381)   File "/usr/local/lib64/python3.11/site-packages/vllm/distributed/utils.py", line 321, in stateless_init_torch_distributed_process_group
(EngineCore_0 pid=381)     pg: ProcessGroup = ProcessGroup(
(EngineCore_0 pid=381)                        ^^^^^^^^^^^^^
(EngineCore_0 pid=381) TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
(EngineCore_0 pid=381)     1. torch._C._distributed_c10d.ProcessGroup(arg0: int, arg1: int)
(EngineCore_0 pid=381)     2. torch._C._distributed_c10d.ProcessGroup(arg0: torch._C._distributed_c10d.Store, arg1: int, arg2: int, arg3: c10d::ProcessGroup::Options)
(EngineCore_0 pid=381)
(EngineCore_0 pid=381) Invoked with: <torch.distributed.distributed_c10d.PrefixStore object at 0xfffe05d1b230>, 0, 2
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1130, in <module>
    uvloop.run(run_server(args))
  File "/usr/local/lib64/python3.11/site-packages/uvloop/__init__.py", line 105, in run
    return runner.run(wrapper())
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/lib64/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1078, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/lib64/python3.11/contextlib.py", line 204, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/lib64/python3.11/contextlib.py", line 204, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 178, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 150, in from_vllm_config
    return cls(
           ^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 118, in __init__
    self.engine_core = core_client_class(
                       ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core_client.py", line 837, in __init__
    super().__init__(vllm_config, executor_class, log_stats)
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core_client.py", line 642, in __init__
    super().__init__(
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core_client.py", line 398, in __init__
    self._wait_for_engine_startup()
  File "/usr/local/lib64/python3.11/site-packages/vllm/v1/engine/core_client.py", line 430, in _wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above.
[ERROR] 2025-05-22-11:41:56 (PID:239, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
