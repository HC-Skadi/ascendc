# Issue #5541: [Bug] FIA operator error during 64-concurrency test with Qwen3-235B W8A8 on Ascend (vLLM 0.13.0rc1)

## 基本信息

- **编号**: #5541
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5541
- **创建时间**: 2025-12-31T01:37:32Z
- **关闭时间**: 2026-01-06T07:26:47Z
- **更新时间**: 2026-01-06T07:28:58Z
- **提交者**: @triomino
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:03:05) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.36.0.112.4.oe2203sp1.x86_64-x86_64-with-glibc2.35

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   52 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          128
On-line CPU(s) list:             0-127
Vendor ID:                       GenuineIntel
BIOS Vendor ID:                  Intel(R) Corporation
Model name:                      Intel(R) Xeon(R) Gold 6430
BIOS Model name:                 Intel(R) Xeon(R) Gold 6430
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              32
Socket(s):                       2
Stepping:                        8
CPU max MHz:                     3400.0000
CPU min MHz:                     800.0000
BogoMIPS:                        4200.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm[89/1925]
all nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 moni
tor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm
3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept v
pid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_n
i avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves xfd cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dthe
rm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme
avx512_vpopcntdq la57 rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile
 amx_int8 flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       3 MiB (64 instances)
L1i cache:                       2 MiB (64 instances)
L2 cache:                        128 MiB (64 instances)
L3 cache:                        120 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-31,64-95
NUMA node1 CPU(s):               32-63,96-127
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and usercopy barriers only; no swapgs barriers
Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled, PBRSB-eIBRS: Vulnerable
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0+cpu
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/lates
t/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/
local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/
nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/
lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolki
t/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascen
d-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op
_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| 0     910B4-1             | OK            | 131.1       48                0    / 0             |
| 0                         | 0000:D8:00.0  | 27          0    / 0          57347/ 65536         |
+===========================+===============+====================================================+
| 1     910B4-1             | OK            | 127.6       46                0    / 0             |
| 0                         | 0000:D9:00.0  | 28          0    / 0          57347/ 65536         |
+===========================+===============+====================================================+
| 2     910B4-1             | OK            | 124.8       46                0    / 0             |
| 0                         | 0000:46:00.0  | 28          0    / 0          57346/ 65536         |
+===========================+===============+====================================================+
| 3     910B4-1             | OK            | 121.4       47                0    / 0             |
| 0                         | 0000:47:00.0  | 27          0    / 0          57345/ 65536         |
+===========================+===============+====================================================+
| 4     910B4-1             | OK            | 133.5       60                0    / 0             |
| 0                         | 0000:98:00.0  | 29          0    / 0          57346/ 65536         |
+===========================+===============+====================================================+
| 5     910B4-1             | OK            | 145.4       63                0    / 0             |
| 0                         | 0000:99:00.0  | 29          0    / 0          57346/ 65536         |
+===========================+===============+====================================================+
| 6     910B4-1             | OK            | 126.2       57                0    / 0             |
| 0                         | 0000:36:00.0  | 28          0    / 0          57345/ 65536         |
+===========================+===============+====================================================+
| 7     910B4-1             | OK            | 127.9       57                0    / 0             |
| 0                         | 0000:37:00.0  | 28          0    / 0          57347/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 1771333       |                          | 53997                   |
+===========================+===============+====================================================+
| 1       0                 | 1771356       |                          | 53997                   |
+===========================+===============+====================================================+
| 2       0                 | 1771377       |                          | 53997                   |
+===========================+===============+====================================================+
| 3       0                 | 1771399       |                          | 53996                   |
+===========================+===============+====================================================+
| 4       0                 | 1772488       |                          | 53997                   |
+===========================+===============+====================================================+
| 5       0                 | 1772525       |                          | 53997                   |
+===========================+===============+====================================================+
CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/x86_64-linux

```

</details>

### 🐛 Describe the bug

### Describe the bug
An execution error occurs in the **FIA (Fused Interrupted Attention)** operator when running a high-concurrency (64 concurrent requests) load test. The system crashes or throws an operator-related exception during inference.

### Environment
* **vLLM-Ascend Version:** 0.13.0rc1 (Official Docker Image)
* **Hardware:** x86 Host with 8x Huawei Ascend NPUs
* **Model:** Qwen3-235B-A22B (W8A8 Quantized)
* **Deployment Configuration:** 8-card TP (Tensor Parallelism = 8)
* **Test Case:** 64 Concurrency

### Steps to Reproduce
1. Use the official `vllm-ascend:0.13.0rc1` image.
2. Deploy the Qwen3-235B-A22B W8A8 quantized model across 8 NPUs.
```bash
export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_BUFFSIZE=1024
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1

TS=$(date +"%Y%m%d_%H%M%S")
LOG="logs/serve_${TS}.log"
ERR="logs/serve_${TS}.log"

model=/data/models/Qwen3-235B-A22B-W8A8
vllm serve $model \
--served-model-name "Qwen3-235B-A22B-W8A8"  \
--host 0.0.0.0 \
--port 1025 \
--async-scheduling \
--tensor-parallel-size 8 \
--data-parallel-size 1 \
--enable-expert-parallel \
--max-num-seqs 128 \
--max-model-len 8192 \
--max-num-batched-tokens 40960 \
--gpu-memory-utilization 0.9 \
--trust-remote-code \
--quantization ascend \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' 2>&1 | tee $LOG
```
3. Stress test the service with 64 concurrent requests.
```bash
model=Qwen3-235B-A22B-W8A8
port=1025
totl_req=6400
concurrency=64
tokenizer_path=/data/models/Qwen3-235B-A22B-W8A8
vllm bench serve --backend vllm --dataset-name random --random-input-len 4096 --random-output-len 1024 --num-prompts $totl_req --ignore-eos --model $model --tokenizer $tokenizer_path --seed 4441 --host 127.0.0.1 --port $port --endpoint /v1/completions --max-concurrency $concurrency --ready-check-timeout-sec 600
```
4. The FIA operator fails during decode phase.

### Logs & DiagnosticsThe full vLLM logs and NPU plog files are available here:
[Huawei Internal Cloud Drive Link](https://clouddrive.huawei.com/p/6c0f130d3f0f50dd7ada71fa05237a5d)

*(Note to maintainers: The link above is an internal Huawei drive.)*

### Expected Behavior
The model should handle 64-concurrency requests successfully without FIA operator errors, maintaining stable inference on the Ascend backend.

Besides, if `export VLLM_ASCEND_ENABLE_FLASHCOMM1=1` is set, above problem does not occur. However it will cause worse performance at low concurrency as mentioned in #5551 
