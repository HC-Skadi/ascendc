# Issue #556: [Usage]: How to use vllm.sleep mode in recent v0.7.3-dev branch?

## 基本信息

- **编号**: #556
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/556
- **创建时间**: 2025-04-17T10:24:31Z
- **关闭时间**: 2025-05-14T03:59:24Z
- **更新时间**: 2025-05-14T04:13:55Z
- **提交者**: @Switchsyj
- **评论数**: 3

## 标签

无

## 问题描述

### Your current environment

My env:
```
(env-3.10.14) [root@vllm-ascend]# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.2               Version: 24.1.rc2.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 92.6        39                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3360 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 93.8        42                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3355 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 95.2        41                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 91.6        41                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 88.9        40                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 91.3        40                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 92.9        39                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3355 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 88.8        39                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 89.4        40                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3359 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 98.5        40                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 93.3        40                0    / 0             |
| 0                         | 0000:48:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 94.6        42                0    / 0             |
| 0                         | 0000:38:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 89.3        40                0    / 0             |
| 0                         | 0000:D9:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 96.6        41                0    / 0             |
| 0                         | 0000:98:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 91.6        39                0    / 0             |
| 0                         | 0000:B9:00.0  | 0           0    / 0          3354 / 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 97.5        41                0    / 0             |
| 0                         | 0000:C9:00.0  | 0           0    / 0          3353 / 65536         |
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
```
```      
(env-3.10.14) [root@vllm-ascend]# cat /usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.1.T6
innerversion=V100R001C21B058
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.T6/x86_64-linux
(env-3.10.14) [root@vllm-ascend]# python collect_env.py 
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: TencentOS Server 4.0 (x86_64)
GCC version: (GCC) 12.2.0 20220819 (TencentOS 12.2.0-5)
Clang version: 14.0.5 (TencentOS 14.0.5-1.tl4)
CMake version: version 4.0.0
Libc version: glibc-2.38

Python version: 3.10.14 (main, May  6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.4.241-1-tlinux4-0017.7-x86_64-with-glibc2.38
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8476C
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
[pip3] mindietorch==1.0rc2+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] pynvml==11.5.3
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torch_npu_acc==1.0.7
[pip3] transformers==4.51.3
[pip3] transformers-stream-generator==0.0.5
[conda] mindietorch               1.0rc2+torch2.1.0.abi0          pypi_0    pypi
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pynvml                    11.5.3                   pypi_0    pypi
[conda] pyzmq                     26.4.0                   pypi_0    pypi
[conda] torch                     2.5.1+cpu                pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250320          pypi_0    pypi
[conda] torch-npu-acc             1.0.7                    pypi_0    pypi
[conda] transformers              4.51.3                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.5                    pypi_0    pypi
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages:/usr/local/Ascend/ascend-toolkit/latest/x86_64-linux/lib64:/data/miniconda3/envs/env-3.10.14/lib/python3.10/site-packages/torch/lib/:/data/miniconda3/envs/env-3.10.14/lib:/usr/local/Ascend/driver/lib64/driver:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```


### How would you like to use vllm on ascend

Hi, I notice that recent updates in v0.7.3-dev enables sleep and wake up mode for vllm-ascend to save memory while the inference is not activate. And I am now trying to initialize QwQ-32B to inference on my machine:
```python
self.llm = LLM(
            model=self.model.name_or_path,
            device=self.vllm_device,
            gpu_memory_utilization=self.args.vllm_gpu_memory_utilization,
            dtype=self.args.vllm_dtype,
            enable_prefix_caching=self.args.vllm_enable_prefix_caching,
            max_model_len=self.args.vllm_max_model_len,
            tensor_parallel_size=args.vllm_colocation_tp,
            distributed_executor_backend="external_launcher",
            max_num_seqs=self.args.per_device_train_batch_size * self.args.vllm_colocation_tp,
            enable_sleep_mode=True,
)
```
but It shows an error for all ranks:
```
[rank12]:     assert camem_available, "camem allocator is not available"
```
And I find that in `setup.py`, envs.COMPILE_CUSTOM_KERNELS = None, so that `vllm_ascend.vllm_ascend_C` would not be modularized in this case. 

Are there any suggestions for this issue?

