# Issue #4266: [Bug]: Get random output in Qwen3-next

## 基本信息

- **编号**: #4266
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4266
- **创建时间**: 2025-11-19T03:28:32Z
- **关闭时间**: 2025-12-11T13:40:54Z
- **更新时间**: 2025-12-11T13:40:55Z
- **提交者**: @drslark
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

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.39

Python version: 3.11.10 (main, Nov 10 2025, 15:27:46) [GCC 13.3.0] (64-bit runtime)
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
BIOS Model name:                    Kunpeng 920 7285Z To be filled by O.E.M. CPU @ 3.0GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        3000.0000
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
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc5
vLLM Ascend Version: 0.11.0rc1.dev347+g67f2b3a03 (git sha: 67f2b3a03)

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
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 166.9       38                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          46536/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           37                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          46084/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 162.1       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          46528/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          46096/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 160.9       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3140 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 166.5       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3150 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           41                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2874 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 170.5       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3157 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           38                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2874 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 162.6       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3144 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           37                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 165.0       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3156 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           39                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2877 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 165.6       41                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3157 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           39                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2877 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 2173027       |                          | 43266                   |
| 0       1                 | 2173030       |                          | 43266                   |
+===========================+===============+====================================================+
| 1       0                 | 2173031       |                          | 43266                   |
| 1       1                 | 2173032       |                          | 43266                   |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

Codes to reproduce this bug:

```python
if __name__ == '__main__':
    prompts = [
        "Who are you?",
    ]

    sampling_params = SamplingParams(temperature=0.0, top_p=0.95, top_k=40, max_tokens=128)
    llm = LLM(model="/home/model/Qwen3-Next-80B-A3B-Instruct",
              tensor_parallel_size=4,
              enforce_eager=True,
              distributed_executor_backend="mp",
              gpu_memory_utilization=0.7,
              max_model_len=4096)

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(output.outputs[0].token_ids)
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

The output:

```text
[358, 139415, 120030, 1035, 198, 979, 198, 11917, 198, 135476, 26940, 11, 72776, 198, 93495, 198, 1008, 1940, 4102, 4102, 8, 3070, 198, 304, 27509, 220, 198, 198, 11, 11, 3070, 279, 11, 220, 334, 19095, 26889, 220, 71960, 111301, 7, 82, 279, 3059, 33358, 198, 1386, 3041, 8649, 1059, 198, 53180, 287, 11, 220, 11, 17486, 220, 353, 198, 198, 279, 279, 565, 198, 27773, 198, 17, 334, 23380, 328, 425, 1059, 1112, 279, 11, 334, 334, 68, 198, 198, 100530, 198, 198, 75061, 1035, 101708, 15204, 220, 6397, 198, 119268, 198, 3941, 3941, 99107, 11, 220, 220, 119142, 1359, 389, 30130, 11, 11, 220, 82, 24660, 8823, 113647, 109877, 198, 109492, 198, 25, 11995, 198, 220, 9856, 48415, 43687, 19191, 279, 220, 21887, 271, 101041, 6397]
Prompt: 'Who are you?', Generated text: ' Iビル荑 would\n when\npio\nビジ《, connexion\nOCR\n other…\xa0\xa0) **\n inrying \n\n,, ** the, **kn Castle /Z银行卡(s the results biology\nood far extract her\n oceansing, , crack  *\n\n the the##\n果\n2** swimming S B her... the,****e\n\n棋\n\n钟 would茅TA Target\n覃\n across across在线,  馍By on rim,, s polar meta跟她醒来\n古人\n: �\n  Germany_DECLAREVECTOR@@ the 理\n\n直接Target'
```

The output is random.
