# Issue #4930: [Bug]: NPU and GPU have redundant outputs when running Qwen3-Next-MTP.

## 基本信息

- **编号**: #4930
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4930
- **创建时间**: 2025-12-11T14:01:23Z
- **关闭时间**: 2025-12-16T09:41:27Z
- **更新时间**: 2025-12-16T09:41:27Z
- **提交者**: @drslark
- **评论数**: 1

## 标签

bug; qwen3-next

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.39

Python version: 3.11.10 (main, Nov 23 2025, 16:33:07) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.39

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS Model name:                    Kunpeng 920 7280Z To be filled by O.E.M. CPU @ 2.9GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2900.0000
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
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.2.dev634+ge83b7e379 (git sha: e83b7e379)
vLLM Ascend Version: 0.11.0rc1.dev589+gbb76f7962 (git sha: bb76f7962)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib
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
| npu-smi 25.2.3                   Version: 25.2.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 232.5       52                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 17          0    / 0          53444/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           51                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 17          0    / 0          52948/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 226.9       51                0    / 0             |
| 0     2                   | 0000:99:00.0  | 17          0    / 0          53200/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           52                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 17          0    / 0          52940/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 175.3       52                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3128 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           52                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2888 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 170.6       51                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3122 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           51                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2888 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 167.2       51                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3136 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           49                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2895 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 174.5       51                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3130 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           50                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2895 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 243.3       53                0    / 0             |
| 0     12                  | 0000:85:00.0  | 17          0    / 0          50719/ 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           50                0    / 0             |
| 1     13                  | 0000:87:00.0  | 17          0    / 0          50242/ 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 248.0       52                0    / 0             |
| 0     14                  | 0000:81:00.0  | 17          0    / 0          50494/ 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           52                0    / 0             |
| 1     15                  | 0000:83:00.0  | 17          0    / 0          50242/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 3325989       |                          | 50128                   |
| 0       0                 | 3330598       |                          | 132                     |
| 0       0                 | 3328327       |                          | 133                     |
| 0       0                 | 3333165       |                          | 132                     |
| 0       1                 | 3328327       |                          | 50119                   |
+===========================+===============+====================================================+
| 1       0                 | 3330598       |                          | 50117                   |
| 1       1                 | 3333165       |                          | 50119                   |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| 6       0                 | 3085960       |                          | 47426                   |
| 6       0                 | 3085961       |                          | 122                     |
| 6       0                 | 3085962       |                          | 122                     |
| 6       0                 | 3085964       |                          | 122                     |
| 6       1                 | 3085961       |                          | 47416                   |
+===========================+===============+====================================================+
| 7       0                 | 3085962       |                          | 47416                   |
| 7       1                 | 3085964       |                          | 47416                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.5.0
innerversion=V100R001C25B048
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.5.0/aarch64-linux


</details>


### 🐛 Describe the bug

When we run:

```python
    prompts = [
        "Hello, my name is", 
        "The president of the United States is",
        "The capital of France is", 
        "The future of AI is"
    ]

    sampling_params = SamplingParams(temperature=0.0, top_p=0.95, top_k=40, max_tokens=20)
    llm = LLM(model="/home/model/Qwen3-Next-80B-A3B-Instruct",
              tensor_parallel_size=4,
              enforce_eager=True,
              distributed_executor_backend="mp",
              gpu_memory_utilization=0.7,
              speculative_config={
                  "method": "qwen3_next_mtp",
                  "num_speculative_tokens": 1,
              },
              max_model_len=4096, 
              enable_prefix_caching=False)

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

The outputs of gpu are:

```text
Prompt: 'Hello, my name is', Generated text: ' [Your Name], and I am a 20-year-old student from [Your Country]. I'
Prompt: 'The president of the United States is', Generated text: ' 2024 is the president of the United States of America. The president of the United'
Prompt: 'The capital of France is', Generated text: ' the of capital isThe the of capital isThe the of capital isThe the of capital of capital'
Prompt: 'The future of AI is', Generated text: ' the future of the world is in the hands of the people of the world. The future of the'
```

The outputs of npu are:

```text
Prompt: 'Hello, my name is', Generated text: ' [Your Name], and I am a 20-year-old student from [Your Country]. I'
Prompt: 'The president of the United States is', Generated text: ' 2025, and the world is in chaos. The AI has become self-aware and'
Prompt: 'The capital of France is', Generated text: ' the most important of the three. The capital of the United States is Washington, D.C., which'
Prompt: 'The future of AI is', Generated text: ' a of the of the of the of the of the of the of the of the of the of'
```

They all have redundant outputs.
