# Issue #4293: [Bug]: qwen3-vl-235b-w8a8 load weight ERROR when start service

## 基本信息

- **编号**: #4293
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4293
- **创建时间**: 2025-11-20T03:11:54Z
- **关闭时间**: 2025-12-22T11:09:09Z
- **更新时间**: 2025-12-22T11:09:09Z
- **提交者**: @Levi-JQ
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
```shell
Collecting environment information...
PyTorch version: 2.7.1+cu126
Is debug build: False

OS: openEuler 24.03 (LTS) (x86_64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403)
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.38

Python version: 3.11.6 (main, Oct 29 2025, 18:39:28) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime)
Python platform: Linux-5.10.112-100.alios7.x86_64-x86_64-with-glibc2.38

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8468
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
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.0
[conda] Could not collect
vLLM Version: 0.11.1.dev20+gb23904a04 (git sha: b23904a04)
vLLM Ascend Version: 0.11.0rc1.dev219+gecc210626.d20251119 (git sha: ecc210626, date: 20251119)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_LAYER_INTERNAL_TENSOR_REUSE=1
ASCEND_VISIBLE_DEVICES=4,12,5,13,7,15,6,14,3,11,1,9,2,10,0,8
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ATB_LLM_COMM_BACKEND=hccl
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ATB_LLM_HCCL_ENABLE=1
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/lib64/:/usr/local/lib:/usr/local/lib64/:/home/admin/inference/triton_default/lib:/home/admin/inference/triton_default/lib64:/usr/local/lib64/python3.11/site-packages/vllm_ascend:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_LOGGING_CONFIG_PATH=/home/admin/vllm/logging_config.json
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
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
| 0     910B2C              | OK            | 95.0        43                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          56188/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 101.2       45                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          56180/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 96.1        45                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          56180/ 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 92.9        43                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          56179/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 90.2        44                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          56181/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 97.8        47                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          56179/ 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 91.2        45                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          56180/ 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 102.3       46                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          56179/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 93.4        43                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          56108/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 96.0        44                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 91.6        43                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 92.7        44                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 94.3        45                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          56099/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 101.3       45                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 88.6        45                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 97.0        45                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          56097/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 29705         | VLLMWorker_DP            | 52775                   |
+===========================+===============+====================================================+
| 1       0                 | 29726         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 2       0                 | 29771         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 3       0                 | 29820         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 4       0                 | 29872         | VLLMWorker_DP            | 52796                   |
+===========================+===============+====================================================+
| 5       0                 | 29921         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 6       0                 | 29972         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 7       0                 | 30020         | VLLMWorker_DP            | 52795                   |
+===========================+===============+====================================================+
| 8       0                 | 29704         | VLLMWorker_DP            | 52713                   |
+===========================+===============+====================================================+
| 9       0                 | 29727         | VLLMWorker_DP            | 52714                   |
+===========================+===============+====================================================+
| 10      0                 | 29774         | VLLMWorker_DP            | 52713                   |
+===========================+===============+====================================================+
| 11      0                 | 29825         | VLLMWorker_DP            | 52714                   |
+===========================+===============+====================================================+
| 12      0                 | 29873         | VLLMWorker_DP            | 52714                   |
+===========================+===============+====================================================+
| 13      0                 | 29922         | VLLMWorker_DP            | 52713                   |
+===========================+===============+====================================================+
| 14      0                 | 29971         | VLLMWorker_DP            | 52714                   |
+===========================+===============+====================================================+
| 15      0                 | 30021         | VLLMWorker_DP            | 52713                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/x86_64-linux
```
```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

When start vllm with qwen3-vl-235b-w8a8, the weight load module will report ERROR as following:
```shell
File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/quantization/quant_config-py", line 153, in is_layer_skipped_ascendis_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
KeyError: 'visual.merger.linear_fc1.weight'
```
