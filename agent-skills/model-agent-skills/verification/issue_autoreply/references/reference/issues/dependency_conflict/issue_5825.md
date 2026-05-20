# Issue #5825: [Bug]: `eagle3` with `sp` will cause an accuracy problem in drafter model

## 基本信息

- **编号**: #5825
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5825
- **创建时间**: 2026-01-12T14:15:27Z
- **关闭时间**: 2026-01-14T01:08:36Z
- **更新时间**: 2026-01-14T01:09:03Z
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
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.39

Python version: 3.11.10 (main, Dec 10 2025, 14:18:36) [GCC 13.3.0] (64-bit runtime)
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
[pip3] torch==2.8.0
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2.dev154+gff4c1a47b (git sha: ff4c1a47b)

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
| 0     Ascend910           | OK            | 164.0       29                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3142 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           30                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2887 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 164.0       29                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3107 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           28                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2872 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 164.6       29                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          62308/ 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           29                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          61795/ 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 160.4       28                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          62073/ 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           29                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          61793/ 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 159.9       29                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          56095/ 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           29                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          55523/ 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 156.8       30                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          55841/ 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           29                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          55504/ 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 161.0       28                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3139 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           27                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2891 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 152.0       29                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3134 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           28                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| 2       0                 | 2268928       |                          | 126                     |
| 2       0                 | 2268921       |                          | 58959                   |
| 2       0                 | 2268924       |                          | 126                     |
| 2       0                 | 2268925       |                          | 126                     |
| 2       1                 | 2268924       |                          | 58953                   |
+===========================+===============+====================================================+
| 3       0                 | 2268925       |                          | 58953                   |
| 3       1                 | 2268928       |                          | 58953                   |
+===========================+===============+====================================================+
| 4       0                 | 2906560       |                          | 126                     |
| 4       0                 | 2905025       |                          | 52747                   |
| 4       0                 | 2907938       |                          | 126                     |
| 4       0                 | 2909355       |                          | 126                     |
| 4       1                 | 2906560       |                          | 52680                   |
+===========================+===============+====================================================+
| 5       0                 | 2907938       |                          | 52721                   |
| 5       1                 | 2909355       |                          | 52660                   |
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

When running `eagle3` with `sp`, it will get a low acceptance rate. It is an accuracy problem of drafter model.

For simpilicity, we modified codes in `vllm-ascend/vllm_ascend/ascend_forward_context.py`.

Delete the condition `and num_tokens > 1000` to judge whether `sp_enabled` is `True` or not.

After deleting the condition, `sp` is always enabled.

Then, we run the codes below:

```python
import os
import gc
import torch

from vllm.v1.metrics.reader import Counter, Vector
from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)

def clean_up():
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()

os.environ["VLLM_VERSION"]="0.13.0"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"]="spawn"
os.environ["VLLM_ASCEND_ENABLE_FLASHCOMM1"]="1"
os.environ["ASCEND_RT_VISIBLE_DEVICES"]="12,13,14,15"


if __name__ == '__main__':
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("/home/model/Qwen3-30B-A3B", trust_remote_code=True)

    prompts = [
        [
            {"role": "system", "content": ""},
            {"role": "user", "content": "\nRectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16,$ $AB=107,$ $FG=17,$ and $EF=184,$ what is the length of $CE$? [asy] import graph; unitsize(0.1cm);  pair A = (0,0);pair B = (70,0);pair C = (70,16);pair D = (0,16);pair E = (3,16);pair F = (90,16);pair G = (90,33);pair H = (3,33); dot(A^^B^^C^^D^^E^^F^^G^^H); label(\"$A$\", A, S);label(\"$B$\", B, S);label(\"$C$\", C, N);label(\"$D$\", D, N);label(\"$E$\", E, S);label(\"$F$\", F, S);label(\"$G$\", G, N);label(\"$H$\", H, N); draw(E--D--A--B--C--E--H--G--F--C); [/asy]\n\nPlease reason step by step, and put your final answer within \\boxed{}."}
        ]
    ]
    
    prompts = [tokenizer.apply_chat_template(
        prompt,
        tokenize=False,
        add_generation_prompt=True
    ) for prompt in prompts]

    sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=40, max_tokens=1000)

    num_spec_tokens = 32768
    llm = LLM(
            enforce_eager=True,
            model="/home/model/Qwen3-30B-A3B",
            enable_expert_parallel=True,
            tensor_parallel_size=2,
            distributed_executor_backend="mp",
            gpu_memory_utilization=0.8,
            max_num_seqs=1,
            max_model_len=32768,
            disable_log_stats=False,
            async_scheduling=False,

            speculative_config={
                "enforce_eager":True,
                "method": "eagle3",
                "model": "/home/model/Qwen3-30B-A3B-EAGLE3",
                "draft_tensor_parallel_size": 1,
                "num_speculative_tokens": 3
            },
    )

    outputs = llm.generate(prompts, sampling_params)

    total_num_output_tokens = sum(
        len(output.outputs[0].token_ids) for output in outputs
    )

    metrics = llm.get_metrics()
    num_drafts = 0
    num_draft_tokens = 0
    num_accepted_tokens = 0
    acceptance_counts = [0] * 6
    for metric in metrics:
        if metric.name == "vllm:spec_decode_num_drafts":
            assert isinstance(metric, Counter)
            num_drafts += metric.value
        elif metric.name == "vllm:spec_decode_num_draft_tokens":
            assert isinstance(metric, Counter)
            num_draft_tokens += metric.value
        elif metric.name == "vllm:spec_decode_num_accepted_tokens":
            assert isinstance(metric, Counter)
            num_accepted_tokens += metric.value
        elif metric.name == "vllm:spec_decode_num_accepted_tokens_per_pos":
            assert isinstance(metric, Vector)
            for pos in range(len(metric.values)):
                acceptance_counts[pos] += metric.values[pos]

    print("-" * 50)
    print(f"total_num_output_tokens: {total_num_output_tokens}")
    print(f"num_drafts: {num_drafts}")
    print(f"num_draft_tokens: {num_draft_tokens}")
    print(f"num_accepted_tokens: {num_accepted_tokens}")
    acceptance_length = 1 + (num_accepted_tokens / num_drafts) if num_drafts > 0 else 1
    print(f"mean acceptance length: {acceptance_length:.2f}")
    print("-" * 50)


    # print acceptance at each token position
    for i in range(len(acceptance_counts)):
        acceptance_rate = acceptance_counts[i] / num_drafts if num_drafts > 0 else 0
        print(f"acceptance at token {i}: {acceptance_rate:.2f}")

    del llm
    clean_up()

```

The output is:

```text
--------------------------------------------------
total_num_output_tokens: 1000
num_drafts: 597
num_draft_tokens: 1791
num_accepted_tokens: 402
mean acceptance length: 1.67
--------------------------------------------------
acceptance at token 0: 0.59
acceptance at token 1: 0.08
acceptance at token 2: 0.00
acceptance at token 3: 0.00
acceptance at token 4: 0.00
acceptance at token 5: 0.00
```

The acceptance rate of `token 0` and `token 1` are quite low.

And if we commented `os.environ["VLLM_ASCEND_ENABLE_FLASHCOMM1"]="1"` and `sp` is disabled.

The output is:

```text
--------------------------------------------------
total_num_output_tokens: 1000
num_drafts: 437
num_draft_tokens: 1311
num_accepted_tokens: 564
mean acceptance length: 2.29
--------------------------------------------------
acceptance at token 0: 0.62
acceptance at token 1: 0.40
acceptance at token 2: 0.27
acceptance at token 3: 0.00
acceptance at token 4: 0.00
acceptance at token 5: 0.00
```

We can see that the acceptance rate of `token 0` and `token 1` are normal when `sp` is disabled.

So, there is definitely an accuracy bug in drafter model with `sp`.
