# Issue #616: [Bug]: DP Attention in V1 error: cannot set moe all to all group due to repeated initializations

## 基本信息

- **编号**: #616
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/616
- **创建时间**: 2025-04-22T09:29:59Z
- **关闭时间**: 2025-04-22T09:42:01Z
- **更新时间**: 2025-04-22T09:42:01Z
- **提交者**: @HanlinDu
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
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
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.16.0
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.dev107+g4c41278b7 (git sha: 4c41278b7)
vLLM Ascend Version: 0.8.4rc2.dev4+g5442b46 (git sha: 5442b46)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
VLLM_WORKER_MULTIPROC_METHOD=spawn
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/mnt/deepseek/sunbaosong/setup_0410_8.2/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/mnt/deepseek/sunbaosong/setup_0410_8.2/nnal/atb/latest/atb/cxx_abi_0/lib:/mnt/deepseek/sunbaosong/setup_0410_8.2/nnal/atb/latest/atb/cxx_abi_0/examples:/mnt/deepseek/sunbaosong/setup_0410_8.2/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/tools/aml/lib64:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/tools/aml/lib64/plugin:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/lib64:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/lib64/plugin/opskernel:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/lib64/plugin/nnengine:/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/lib/python3.11/site-packages/mindie_turbo:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/mnt/deepseek/sunbaosong/setup_0410_8.2/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
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
| 0     910B2C              | OK            | 94.3        40                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 100.3       43                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3366 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 95.1        43                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3367 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 92.7        40                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3365 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 90.1        41                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3364 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 96.9        43                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3366 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 91.0        43                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3366 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 101.1       44                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3365 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 92.8        40                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3360 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 95.8        41                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3365 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 91.3        40                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3364 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 92.8        41                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3363 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 93.7        43                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3366 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 100.1       43                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3364 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 88.1        41                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3364 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 96.5        42                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3363 / 65536         |
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
innerversion=V100R001C21B081
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

When running DP attention in V1, I found that HCCL error occurred. As DP attn relies on multiple LLM Engine instances, and Ascend decided to apply MoE all to all communication in MC2 ver, the all to all group need to be established after attn stage. However, bugs occurred during all 2 all initialization. Multiple instances will initialize comm group repeatedly, on which HCCL does not support. Thus, a solution to the all 2 all group is needed via either rank adjustment or HCCL support.

- running script
```shell
# The running script is below vllm: [github.com/vllm](https://github.com/vllm-project/vllm/tree/main/examples/offline_inference/data_parallel.py)
export TASK_QUEUE_ENABLE=2
export VLLM_USE_V1=1
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export VLLM_ENABLE_MC2=1

python examples/offline_inference/data_parallel.py  --model="/mnt/deepseek/DeepSeek-V2-Lite" --dp-size=2 --tp-size=8
```

```
# There are 2 kinds of err msg randomly shown

# error msg 1:

^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238] Traceback (most recent call last):^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/utils.py", line 2362, in run_method^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]            ^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/worker/worker.py", line 177, in load_model^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.model_runner.load_model()^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/worker/model_runner.py", line 852, in load_model^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/model_executor/model_loader/loader.py", line 443, in load_model^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/model_executor/model_loader/loader.py", line 129, in _initialize_model^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/models/deepseek_v2.py", line 542, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/models/deepseek_v2.py", line 471, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                                                     ^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                                                      ^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/usr/local/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/models/deepseek_v2.py", line 473, in <lambda>^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     lambda prefix: CustomDeepseekV2DecoderLayer(^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/models/deepseek_v2.py", line 427, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.mlp = CustomDeepseekV2MoE(^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                ^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/models/deepseek_v2.py", line 108, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.experts = AscendFusedMoE(^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                    ^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/ops/fused_moe.py", line 705, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     AscendUnquantizedFusedMoEMethod())^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]   File "/root/dev/vllm-ascend-v1-huawei/vllm_ascend/ops/fused_moe.py", line 563, in __init__^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238]                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^M
^[[1;36m(VllmWorkerProcess pid=176029)^[[0;0m ERROR 04-17 15:30:42 [multiproc_worker_utils.py:238] RuntimeError: create:torch_npu/csrc/distributed/ProcessGroupHCCL.cpp:89 HCCL function error: HcclCommInitRootInfo(numRanks, &rootInfo, rank, &(comm->hcclComm_)), error code is 7^M

# error msg 2:

[rank3]:[W422 17:08:49.148465814 ProcessGroupHCCL.cpp:2100] Warning: The indexFromRank 0is not equal indexFromCurDevice 3 , which might be normal if the number of devices on your collective communication server is inconsistent.Otherwise, you need to check if the current device is correct when calling the interface.If it's incorrect, it might have introduced an error. (function operator())
[rank6]:[W422 17:08:49.245971515 ProcessGroupHCCL.cpp:2100] Warning: The indexFromRank 0is not equal indexFromCurDevice 6 , which might be normal if the number of devices on your collective communication server is inconsistent.Otherwise, you need to check if the current device is correct when calling the interface.If it's incorrect, it might have introduced an error. (function operator())
[rank2]:[W422 17:08:49.262101276 ProcessGroupHCCL.cpp:2100] Warning: The indexFromRank 0is not equal indexFromCurDevice 2 , which might be normal if the number of devices on your collective communication server is inconsistent.Otherwise, you need to check if the current device is correct when calling the interface.If it's incorrect, it might have introduced an error. (function operator())
[rank1]:[W422 17:08:49.266452303 ProcessGroupHCCL.cpp:2100] Warning: The indexFromRank 0is not equal indexFromCurDevice 1 , which might be normal if the number of devices on your collective communication server is inconsistent.Otherwise, you need to check if the current device is correct when calling the interface.If it's incorrect, it might have introduced an error. (function operator())
(EngineCore_1 pid=382867) CRITICAL 04-22 17:08:49 [multiproc_executor.py:49] MulitprocExecutor got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
CRITICAL 04-22 17:08:49 [core_client.py:359] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
(VllmWorker rank=6 pid=384550) Exception ignored in: <Finalize object, dead>
(VllmWorker rank=6 pid=384550) Traceback (most recent call last):
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/util.py", line 224, in __call__
(VllmWorker rank=6 pid=384550)     res = self._callback(*self._args, **self._kwargs)
(VllmWorker rank=6 pid=384550)           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/managers.py", line 874, in _decref
(VllmWorker rank=6 pid=384550)     conn = _Client(token.address, authkey=authkey)
(VllmWorker rank=6 pid=384550)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/connection.py", line 524, in Client
(VllmWorker rank=6 pid=384550)     answer_challenge(c, authkey)
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/connection.py", line 773, in answer_challenge
(VllmWorker rank=6 pid=384550)     response = connection.recv_bytes(256)        # reject large message
(VllmWorker rank=6 pid=384550)                ^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/connection.py", line 216, in recv_bytes
(VllmWorker rank=6 pid=384550)     buf = self._recv_bytes(maxlength)
(VllmWorker rank=6 pid=384550)           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/connection.py", line 437, in _recv_bytes
(VllmWorker rank=6 pid=384550)     return self._recv(size)
(VllmWorker rank=6 pid=384550)            ^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/lib64/python3.11/multiprocessing/connection.py", line 395, in _recv
(VllmWorker rank=6 pid=384550)     chunk = read(handle, remaining)
(VllmWorker rank=6 pid=384550)             ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=384550)   File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 308, in signal_handler
(VllmWorker rank=6 pid=384550)     raise SystemExit()
(VllmWorker rank=6 pid=384550) SystemExit:
(EngineCore_0 pid=382869) CRITICAL 04-22 17:08:50 [multiproc_executor.py:49] MulitprocExecutor got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
CRITICAL 04-22 17:08:50 [core_client.py:359] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
[root@99a03a2faf7e vllm]# python examples/offline_inference/data_parallel.py  --model="/mnt/deepseek/DeepSeek-V2-Lite" --dp-size=2 --tp-size=8Read from remote error: websocket: close 1006 (abnormal closure): unexpected EOF
```
