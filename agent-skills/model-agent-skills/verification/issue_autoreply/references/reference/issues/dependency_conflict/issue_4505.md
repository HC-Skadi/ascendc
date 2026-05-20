# Issue #4505: [Bug]: ascend不支持prompt_embeds作为输入

## 基本信息

- **编号**: #4505
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4505
- **创建时间**: 2025-11-27T10:51:56Z
- **关闭时间**: 2025-12-09T08:25:42Z
- **更新时间**: 2025-12-09T08:25:42Z
- **提交者**: @Dog-Boss
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Sep 23 2025, 11:59:46) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.4.241-1-tlinux4-0017.7-x86_64-with-glibc2.35

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
BIOS Vendor ID:                  Intel(R) Corporation
Model name:                      Intel(R) Xeon(R) Platinum 8476C
BIOS Model name:                 Intel(R) Xeon(R) Platinum 8476C
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        8
Frequency boost:                 enabled
CPU max MHz:                     2601.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq la57 rdpid cldemote movdiri movdir64b fsrm md_clear pconfig flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       4.5 MiB (96 instances)
L1i cache:                       3 MiB (96 instances)
L2 cache:                        192 MiB (96 instances)
L3 cache:                        195 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47,96-143
NUMA node1 CPU(s):               48-95,144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable: eIBRS with unprivileged eBPF
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pytorch-wpe==0.0.1
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch-complex==0.4.4
[pip3] torch_npu==2.7.1
[pip3] torchaudio==2.8.0+cpu
[pip3] torchvision==0.22.1+cpu
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 89.1        37                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          65489/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 89.1        39                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          63501/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 92.1        37                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          63497/ 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 88.6        36                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          63501/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 89.4        36                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          63522/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 98.8        39                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          63500/ 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 88.8        38                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          63497/ 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 91.3        38                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          63500/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 85.3        39                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          63501/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 90.8        37                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          63500/ 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 92.8        38                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          63499/ 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 91.1        39                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          63499/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 88.6        39                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          63497/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 90.5        37                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          63500/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 85.0        36                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          63501/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 89.6        39                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          63501/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 472232        |                          | 6313                    |
| 0       0                 | 495142        |                          | 55751                   |
+===========================+===============+====================================================+
| 1       0                 | 495146        |                          | 60179                   |
+===========================+===============+====================================================+
| 2       0                 | 495154        |                          | 60179                   |
+===========================+===============+====================================================+
| 3       0                 | 495160        |                          | 60179                   |
+===========================+===============+====================================================+
| 4       0                 | 495167        |                          | 60179                   |
+===========================+===============+====================================================+
| 5       0                 | 495174        |                          | 60179                   |
+===========================+===============+====================================================+
| 6       0                 | 495176        |                          | 60179                   |
+===========================+===============+====================================================+
| 7       0                 | 495188        |                          | 60179                   |
+===========================+===============+====================================================+
| 8       0                 | 495195        |                          | 60179                   |
+===========================+===============+====================================================+
| 9       0                 | 495202        |                          | 60179                   |
+===========================+===============+====================================================+
| 10      0                 | 495209        |                          | 60179                   |
+===========================+===============+====================================================+
| 11      0                 | 495216        |                          | 60179                   |
+===========================+===============+====================================================+
| 12      0                 | 495227        |                          | 60179                   |
+===========================+===============+====================================================+
| 13      0                 | 495230        |                          | 60179                   |
+===========================+===============+====================================================+
| 14      0                 | 495242        |                          | 60179                   |
+===========================+===============+====================================================+
| 15      0                 | 495264        |                          | 60179                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC2
innerversion=V100R001C22SPC002B220
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC2/x86_64-linux
```

</details>


### 🐛 Describe the bug

当前遇到的报错是
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
(EngineCore_DP0 pid=47940) Process EngineCore_DP0:
(EngineCore_DP0 pid=47940) Traceback (most recent call last):
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=47940)     self.run()
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=47940)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=47940)     raise e
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 701, in run_engine_core
(EngineCore_DP0 pid=47940)     engine_core.run_busy_loop()
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 728, in run_busy_loop
(EngineCore_DP0 pid=47940)     self._process_engine_step()
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 754, in _process_engine_step
(EngineCore_DP0 pid=47940)     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=47940)                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 284, in step
(EngineCore_DP0 pid=47940)     model_output = self.execute_model_with_error_logging(
(EngineCore_DP0 pid=47940)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
(EngineCore_DP0 pid=47940)     raise err
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
(EngineCore_DP0 pid=47940)     return model_fn(scheduler_output)
(EngineCore_DP0 pid=47940)            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 103, in execute_model
(EngineCore_DP0 pid=47940)     output = self.collective_rpc("execute_model",
(EngineCore_DP0 pid=47940)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=47940)     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=47940)             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/utils/__init__.py", line 3122, in run_method
(EngineCore_DP0 pid=47940)     return func(*args, **kwargs)
(EngineCore_DP0 pid=47940)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 276, in execute_model
(EngineCore_DP0 pid=47940)     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=47940)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=47940)     return func(*args, **kwargs)
(EngineCore_DP0 pid=47940)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1898, in execute_model
(EngineCore_DP0 pid=47940)     self._update_states(scheduler_output)
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 650, in _update_states
(EngineCore_DP0 pid=47940)     self.requests[req_id] = CachedRequestState(
(EngineCore_DP0 pid=47940)                             ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940)   File "<string>", line 18, in __init__
(EngineCore_DP0 pid=47940)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/npu_input_batch.py", line 70, in __post_init__
(EngineCore_DP0 pid=47940)     self.num_prompt_tokens = len(self.prompt_token_ids)
(EngineCore_DP0 pid=47940)                              ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=47940) TypeError: object of type 'NoneType' has no len()

我的输入方式使用的prompt_embeds

<img width="1485" height="690" alt="Image" src="https://github.com/user-attachments/assets/e341185d-cf64-444a-b382-3e0e57653050" />
