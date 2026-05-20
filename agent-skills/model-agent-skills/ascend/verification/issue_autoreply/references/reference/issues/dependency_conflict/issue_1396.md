# Issue #1396: [Bug]: assert self.cpu_group is not None

## 基本信息

- **编号**: #1396
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1396
- **创建时间**: 2025-06-24T09:08:34Z
- **关闭时间**: 2025-07-21T01:08:05Z
- **更新时间**: 2025-12-25T23:11:57Z
- **提交者**: @iWasOmen
- **评论数**: 14

## 标签

bug; module:rl

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```INFO 06-24 08:53:28 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-24 08:53:28 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-24 08:53:31 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-24 08:53:31 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-24 08:53:31 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-24 08:53:31 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-24 08:53:35 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.35

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
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
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250528
[pip3] torchaudio==2.7.0
[pip3] torchdata==0.11.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 99.7        50                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          35879/ 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 96.7        49                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3390 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 97.3        49                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 98.3        50                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3390 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 106.1       49                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          56399/ 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 102.3       49                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          56401/ 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 93.2        48                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          61245/ 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 97.4        49                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          59966/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 1240128       |                          | 14734                   |
| 0       0                 | 1241418       |                          | 1586                    |
| 0       0                 | 1241419       |                          | 1626                    |
| 0       0                 | 1239115       |                          | 14788                   |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| 4       0                 | 931717        |                          | 53073                   |
+===========================+===============+====================================================+
| 5       0                 | 931861        |                          | 53073                   |
+===========================+===============+====================================================+
| 6       0                 | 819389        |                          | 57921                   |
+===========================+===============+====================================================+
| 7       0                 | 819930        |                          | 56641                   |
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

I am using vllm-ascend 0.9.1rc1(v1 mode)+verl
when run with verl (e.g. verl/examples/grpo_trainer/run_qwen2_5_7b_grpo_npu.sh)
if we set the actor_rollout_ref.rollout.tensor_model_parallel_size=$(the number of npu that the env can see), all is well and the training is ok. But if we set the actor_rollout_ref.rollout.tensor_model_parallel_size!=$(the number of npu that the env can see), there will be an assert self.cpu_group is not None error.

e.g. 
```
export ASCEND_RT_VISIBLE_DEVICES=0,1
python3 -m verl.trainer.main_ppo \
...
actor_rollout_ref.rollout.tensor_model_parallel_size=2
```
->ok
```
export ASCEND_RT_VISIBLE_DEVICES=0,1
python3 -m verl.trainer.main_ppo \
...
actor_rollout_ref.rollout.tensor_model_parallel_size=1
```
->error: assert self.cpu_group is not None

the bug detail is below:

![Image](https://github.com/user-attachments/assets/4c4e8466-f846-4f30-8cc6-75f266dfd1a5)
