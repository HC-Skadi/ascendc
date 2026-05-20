# Issue #629: [Bug]: deepseek-r1-w8a8 无法在vllm==v0.8.4下启动图模式

## 基本信息

- **编号**: #629
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/629
- **创建时间**: 2025-04-23T07:08:23Z
- **关闭时间**: 2025-05-14T06:04:24Z
- **更新时间**: 2025-05-14T06:04:24Z
- **提交者**: @NeverRaR
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

INFO 04-23 15:06:44 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-23 15:06:44 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-23 15:06:44 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-23 15:06:44 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-23 15:06:44 [__init__.py:44] plugin ascend loaded.
INFO 04-23 15:06:44 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.38

Python version: 3.11.6 (main, Feb 19 2025, 17:40:52) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
BIOS Vendor ID:                  Intel(R) Corporation
Model name:                      Intel(R) Xeon(R) Platinum 8468
BIOS Model name:                 Intel(R) Xeon(R) Platinum 8468  CPU @ 2.1GHz
BIOS CPU family:                 179
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
BogoMIPS:                        4200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        210 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250409
[pip3] torchaudio==2.6.0
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.4
vLLM Ascend Version: 0.8.4rc2.dev19+gab4c72a (git sha: ab4c72a)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/lib/python3.11/site-packages/mindie_turbo:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=3
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 93.1        55                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3418 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 95.0        54                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 93.4        55                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 96.6        56                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 92.9        57                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 107.0       56                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 99.9        55                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 98.9        56                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 95.4        54                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 94.4        55                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 98.7        55                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 96.6        57                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 95.0        57                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 97.5        57                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 99.2        52                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 96.2        55                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3392 / 65536         |
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
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 10                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 11                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 12                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 13                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 14                                                           |
+===========================+===============+====================================================+
| No running processes found in NPU 15                                                           |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B212
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux


### 🐛 Describe the bug

相关版本:
runtime_running_version=[7.7.T20.0.B210:8.1.RC1]
compiler_running_version=[7.7.T20.0.B210:8.1.RC1]
hccl_running_version=[7.7.T20.0.B210:8.1.RC1]
opp_running_version=[7.7.T20.0.B210:8.1.RC1]
toolkit_running_version=[7.7.T20.0.B210:8.1.RC1]
aoe_running_version=[7.7.T20.0.B210:8.1.RC1]
ncs_running_version=[7.7.T20.0.B210:8.1.RC1]
opp_kernel_running_version=[7.7.T20.0.B210:8.1.RC1]
opp_kernel_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
runtime_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
compiler_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
hccl_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
opp_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
toolkit_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
aoe_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
ncs_upgrade_version=[7.7.T20.0.B210:8.1.RC1]
runtime_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
compiler_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
hccl_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
opp_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
toolkit_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
aoe_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
ncs_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T20.0.B210:8.1.RC1]
opp_kernel_installed_version=[7.7.T9.0.B057:8.1.T6][7.7.T12.0.B078:8.1.RC1][7.7.T20.0.B210:8.1.RC1]

启动参数:
```
export TASK_QUEUE_ENABLE=2
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_USE_V1=0
export VLLM_ENABLE_GRAPH_MODE=1
python -m vllm.entrypoints.openai.api_server --model=/mnt/deepseek/DeepSeek-R1-W8A8-VLLM \
	 --trust-remote-code \
	 --distributed-executor-backend=mp \
         --max-num-seqs 8 \
	 -tp=16 \
	 --port 8006 \
	 --max-model-len 16384 \
	 --block-size 128 \
	 --compilation_config 1\
	 --additional-config '{"enable_graph_mode":true}'\
	 --gpu-memory-utilization 0.99
```

在首次请求后报错:

```
RuntimeError: Unsupported torch op npu.npu_moe_gating_top_k.default by ge
```

尝试手动添加npu_moe_gating_top_k的converter之后, 首次请求之后依旧报错

```
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
ERROR 04-23 17:13:13 [client.py:305] RuntimeError('Engine process (pid 402494) died.')
ERROR 04-23 17:13:13 [client.py:305] NoneType: None
ERROR 04-23 17:13:23 [serving_chat.py:885] Error in chat completion stream generator.
ERROR 04-23 17:13:23 [serving_chat.py:885] Traceback (most recent call last):
ERROR 04-23 17:13:23 [serving_chat.py:885]   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/serving_chat.py", line 487, in chat_completion_stream_generator
ERROR 04-23 17:13:23 [serving_chat.py:885]     async for res in result_generator:
ERROR 04-23 17:13:23 [serving_chat.py:885]   File "/usr/local/lib64/python3.11/site-packages/vllm/engine/multiprocessing/client.py", line 664, in _process_request
ERROR 04-23 17:13:23 [serving_chat.py:885]     raise request_output
ERROR 04-23 17:13:23 [serving_chat.py:885] vllm.engine.multiprocessing.MQEngineDeadError: Engine loop is not running. Inspect the stacktrace to find the original error: RuntimeError('Engine process (pid 402494) died.').
^C[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!

```

