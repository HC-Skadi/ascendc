# Issue #2971: [Bug]: Attention error in ngram spec decode

## 基本信息

- **编号**: #2971
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2971
- **创建时间**: 2025-09-17T03:01:13Z
- **关闭时间**: 2025-12-29T12:10:01Z
- **更新时间**: 2025-12-29T12:10:01Z
- **提交者**: @wxsIcey
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

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 09:30:19) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] sentence-transformers==5.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.0
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.2rc2.dev255+gcf96366.d20250830 (git sha: cf96366, date: 20250830)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 178.7       37                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3419 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3196 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 186.4       36                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3413 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3189 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 177.2       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3190 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 178.5       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3411 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           37                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3187 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 180.6       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3403 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           37                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3200 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 189.2       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3398 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3202 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 183.7       39                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3400 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3203 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 186.1       37                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3418 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3187 / 65536         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

```
import os

os.environ["VLLM_USE_MODELSCOPE"] = "True"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

from vllm import LLM, SamplingParams


def main():
    prompts = [
        "The quick brown fox jumps over the lazy dog.",
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    # Create an LLM.
    llm = LLM(
            model="Qwen/Qwen2.5-0.5B-Instruct",
            tensor_parallel_size=1,
            speculative_config={
                "method": "ngram",
                "num_speculative_tokens": 10, # 每次最多推测 10 个 token
                "prompt_lookup_max": 1, # 最多使用 1 个 n-gram 进行匹配
            },
            enforce_eager=True,
            gpu_memory_utilization=0.8,
            max_model_len=8192,
        )

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    print(f"Outputs: {outputs}")
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


if __name__ == "__main__":
    main()
```

The error is as follow:

<img width="1415" height="714" alt="Image" src="https://github.com/user-attachments/assets/8964e00b-266c-44b6-b8ac-ff1967b3989c" />

