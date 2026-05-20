# Issue #1563: [Bug]: Inference on 310P device is extremely slow

## 基本信息

- **编号**: #1563
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1563
- **创建时间**: 2025-07-01T10:39:30Z
- **关闭时间**: 2025-07-02T07:46:27Z
- **更新时间**: 2025-07-02T07:54:54Z
- **提交者**: @SorryMaker2022
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May 27 2025, 01:34:13) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-6.8.0-60-generic-x86_64-with-glibc2.35

CPU:
Architecture:                         x86_64
CPU op-mode(s):                       32-bit, 64-bit
Address sizes:                        46 bits physical, 48 bits virtual
Byte Order:                           Little Endian
CPU(s):                               20
On-line CPU(s) list:                  0-19
Vendor ID:                            GenuineIntel
Model name:                           Intel(R) Core(TM) i5-14500
CPU family:                           6
Model:                                191
Thread(s) per core:                   2
Core(s) per socket:                   14
Socket(s):                            1
Stepping:                             2
CPU max MHz:                          5000.0000
CPU min MHz:                          800.0000
BogoMIPS:                             5222.40
Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq tme rdpid movdiri movdir64b fsrm md_clear serialize pconfig arch_lbr ibt flush_l1d arch_capabilities
Virtualization:                       VT-x
L1d cache:                            544 KiB (14 instances)
L1i cache:                            704 KiB (14 instances)
L2 cache:                             11.5 MiB (8 instances)
L3 cache:                             24 MiB (1 instance)
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-19
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Mitigation; Clear Register File
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW sequence; BHI BHI_DIS_S
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc2.dev45+gb308a7a (git sha: b308a7a)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1                               Version: 25.0.rc1.1                                   |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 8       310P3                 | OK              | NA           47                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1475 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 8       310P3                 | OK              | NA           45                0     / 0             |
| 1       1                     | 0000:01:00.0    | 0            1462 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 8                                                                    |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux
```

</details>


### 🐛 Describe the bug

Hi authors,

I am currently working on vLLM on 310P NPUs. I really appreciate your great work introducing vllm-ascend to ascend 310P. However, when I deploy mistral-7B on Atlas 300I Duo (but only use one NPU) with 
```
export ASCEND_RT_VISIBLE_DEVICES=0 && vllm serve --trust-remote-code /path/to/Mistral-7B
```
and test it with 
```
python3 vllm/benchmarks/benchmark_serving.py \
    --backend vllm --host 127.0.0.1 --port 8000 \
    --dataset-name random --random-input-len 1 --random-output-len 256 \
    --max-concurrency 1 --num-prompts 16 \
    --ignore-eos \
    --model /path/to/Mistral-7B
```
(The settings are intended to test single-request speed)

I found that the inference speed is 2.9Tokens/s, which is abnormally lower than the hardware spec bandwidth (204GBps per NPU, which means theoretically the inference speed is at most 14.6Tokens/s).

```
# NPU-SMI at the moment (only chip 0)
Pwr(W)      Temp(C)     AI Core(%)  AI Cpu(%)   Ctrl Cpu(%) Memory(%)   Memory BW(%)
NA          57          95          0           2           62          70
```

With profiling mode I found that the `transData` operator took up 61% of the total time, with most of its time used to convert weights from ND format to NZ format:

![Image](https://github.com/user-attachments/assets/e7b0089b-c73b-4abd-bee8-15fd646d3481)

![Image](https://github.com/user-attachments/assets/c854fbcc-524b-4f5d-9ded-3dfa2c47a4cb)

This also happens when I'm running a GEMV NPU bandwidth microbenchmark (the transData time is up to 70%):

![Image](https://github.com/user-attachments/assets/df1d9100-fd60-489c-8188-1f545f86bef1)

My bandwidth test got only 44GBps per NPU, but the Matmul operator can reach 155GBps per NPU (76% of the NPU spec, a reasonable result), which indicates the operator itself may be efficient enough, but the transData operator severely degrades the performance.

```
# Bandwidth test code
import torch
import torch_npu
import time

device1 = 'npu:0'
device2 = 'npu:1'

device_prop = torch.npu.get_device_properties(device1)
print(f"{device_prop}") # _NPUDeviceProperties(name='Ascend310P3', total_memory=44280.3MB)
# device_prop = torch.npu.get_device_properties(device2)
# print(f"{device_prop}") # _NPUDeviceProperties(name='Ascend310P3', total_memory=44280.3MB)

num_iterations = 100000
gemv_ic = 4096
gemv_oc = 14336
dtype = torch.float16

a1 = torch.rand((gemv_oc,gemv_ic), dtype=dtype, device=device1)
b1 = torch.rand((gemv_ic,1), dtype=dtype, device=device1)
# a2 = torch.rand((gemv_oc,gemv_ic), dtype=dtype, device=device2)
# b2 = torch.rand((gemv_ic,1), dtype=dtype, device=device2)
torch.npu.synchronize()

start_time = time.time()

for _ in range(num_iterations):
    c1 = torch.mm(a1, b1)
    # c2 = torch.mm(a2, b2)

torch.npu.synchronize()
end_time = time.time()

elapsed_time_sec = end_time - start_time
# bytes_transferred = num_iterations * gemv_oc * gemv_ic * 2 * 2
bytes_transferred = num_iterations * gemv_oc * gemv_ic * 2
bandwidth = bytes_transferred / elapsed_time_sec / (1024 ** 3)  # GB/s

print(f"Elapsed Time: {elapsed_time_sec:.4f} s")
print(f"Estimated Aggregated Memory Bandwidth: {bandwidth:.2f} GB/s")
```

Given that ascend 310P's matrix hardware can only handle NZ format weights and activations, can we solve this by transforming all the weights to NZ format at the model loading phase and bypass the auto insertion of transData operators in the low-level ATB engine? Is there any ready-to-go implementations or configs that I may have missed?

This optimization may speed up inference on ascend my 310P by up to 200%. I'd appreciate it if you can give me some advice on the optimization.

Thanks!
