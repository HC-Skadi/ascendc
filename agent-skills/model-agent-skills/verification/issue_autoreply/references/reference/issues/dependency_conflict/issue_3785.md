# Issue #3785: [Bug]: kimi-k2 start bug, weight load ERROR

## 基本信息

- **编号**: #3785
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3785
- **创建时间**: 2025-10-27T03:51:04Z
- **关闭时间**: 2025-12-30T11:00:16Z
- **更新时间**: 2025-12-30T11:00:16Z
- **提交者**: @Levi-JQ
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Init 115487 task_queue_enable = 1
Collecting environment information...
PyTorch version: 2.7.1+cu126
Is debug build: False

OS: Alibaba Group Enterprise Linux Server 7.2 (Paladin) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.38

Python version: 3.11.6 (main, Sep 23 2025, 18:31:41) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
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
[pip3] flake8==7.3.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1+git36de3a5
[pip3] transformers==4.55.2
[conda] Could not collect
vLLM Version: 0.10.1.dev2047+g4d95b2b19.d20251024 (git sha: 4d95b2b19, date: 20251024)
vLLM Ascend Version: 0.1.dev1109+g1e2ffe61d.d20251024 (git sha: 1e2ffe61d, date: 20251024)

ENV Variables:
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ATB_LLM_COMM_BACKEND=hccl
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_LLM_HCCL_ENABLE=1
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/mpich-3.2.1/lib::/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=3
VLLM_LOGGING_CONFIG_PATH=/home/admin/vllm/logging_config.json
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 94.2        43                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3455 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 99.0        45                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 89.3        43                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 90.5        43                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3437 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 90.1        43                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3435 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 92.2        45                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 92.7        43                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 91.0        44                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 92.2        42                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3448 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 95.9        44                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 90.0        43                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 92.5        44                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 94.3        44                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 92.1        44                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 90.5        43                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 92.1        45                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3434 / 65536         |
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
version=8.3.RC1
innerversion=V100R001C23SPC001B224
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

When start vllm with kimi-k2-w8a8, the weight load module will report ERROR as following:

```shell
Traceback (most recent call last):
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/v1/executor/multiproc_executor.py", line 437, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.worker.load_model()
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 361, in load_model
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.model_runner.load_model()
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2654, in load_model
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.model = get_model(vllm_config=self.vllm_config)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     return loader.load_model(vllm_config=vllm_config,
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     model = initialize_model(vllm_config=vllm_config,
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     return model_class(vllm_config=vllm_config, prefix=prefix)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 644, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.model = AscendDeepseekV2Model(vllm_config=vllm_config,
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/compilation/decorators.py", line 201, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 107, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.start_layer, self.end_layer, self.layers = make_layers(
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                                                     ^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/models/utils.py", line 629, in make_layers
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     [PPMissingLayer() for _ in range(start_layer)] + [
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                                                      ^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/models/utils.py", line 630, in <listcomp>
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 109, in <lambda>
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     lambda prefix: DeepseekV2DecoderLayer(vllm_config, prefix,
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 596, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.mlp = DeepseekV2MoE(
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                ^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/models/deepseek_v2.py", line 220, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     self.experts = SharedFusedMoE(
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 500, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     AscendFusedMoE.__init__(self, **kwargs)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 159, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     super().__init__(*args, **kwargs)
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1104, in __init__
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     else quant_config.get_quant_method(self, prefix))
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 115, in get_quant_method
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     if self.is_layer_skipped_ascend(prefix,
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]   File "/mnt/deepseek/cloudide/yujinqi/issue/kimi-k2/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 153, in is_layer_skipped_ascend
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597]                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP8_EP8 pid=844) ERROR 2025-10-25 15:32:13.272 [multiproc_executor.py:597] KeyError: 'model.layers.1.mlp.experts.weight'
```
