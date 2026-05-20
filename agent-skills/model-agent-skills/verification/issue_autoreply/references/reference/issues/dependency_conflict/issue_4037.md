# Issue #4037: [Bug]: precision problem in ngram spec decoding

## 基本信息

- **编号**: #4037
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4037
- **创建时间**: 2025-11-06T11:17:56Z
- **关闭时间**: 2026-01-28T08:49:00Z
- **更新时间**: 2026-01-28T08:56:44Z
- **提交者**: @zhaomingyu13
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

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.125.0.152.oe2203.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.11.1rc3.dev0+gc9461e05a.d20251028 (git sha: c9461e05a, date: 20251028)
vLLM Ascend Version: 0.11.0rc1.dev209+g00aa0bf33.d20251028 (git sha: 00aa0bf33, date: 20251028)

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
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 100.4       50                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 100.1       52                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 98.0        49                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 99.1        49                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 101.7       48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 104.8       50                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 98.2        48                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 99.7        50                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3403 / 65536         |
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
import gc
import torch

from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)
import vllm_ascend
def clean_up():
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()

if __name__ == '__main__':
    prompts = [
        "123412"
        ]
    sampling_params = SamplingParams(temperature=0, top_p=0.95, top_k=40, max_tokens=12)
    llm = LLM(
              model="/home/model/Qwen3-1.7B/",
              tensor_parallel_size=1,
              enforce_eager=True,
              distributed_executor_backend="mp",
              gpu_memory_utilization=0.8,
              max_model_len=32,
              speculative_config={
                "method": "ngram",
                "prompt_lookup_max": 5,
                "prompt_lookup_min": 2,
                "num_speculative_tokens":2,
              },
    )

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

    del llm
    clean_up()
```

The precision problem is as follow:

> Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
> Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:00<00:00,  5.13it/s]
> Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:00<00:00,  5.13it/s]
> (EngineCore_DP0 pid=271251) (Worker pid=271261) 
> (EngineCore_DP0 pid=271251) (Worker pid=271261) INFO 11-06 09:33:05 [default_loader.py:314] Loading weights took 0.58 seconds
> (EngineCore_DP0 pid=271251) (Worker pid=271261) INFO 11-06 09:33:05 [model_runner_v1.py:2938] Loading drafter model...
> (EngineCore_DP0 pid=271251) (Worker pid=271261) INFO 11-06 09:33:06 [model_runner_v1.py:2947] Loading model weights took 3.2153 GB
> (EngineCore_DP0 pid=271251) (Worker pid=271261) INFO 11-06 09:33:08 [worker_v1.py:259] Available memory: 47612861952, total memory: 65452113920
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:08 [kv_cache_utils.py:1201] GPU KV cache size: 415,104 tokens
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:08 [kv_cache_utils.py:1206] Maximum concurrency for 64 tokens per request: 3243.00x
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:08 [core.py:241] init engine (profile, create kv cache, warmup model) took 1.97 seconds
> (EngineCore_DP0 pid=271251) WARNING 11-06 09:33:08 [core.py:135] Using configured V1 scheduler class vllm_ascend.core.scheduler.AscendScheduler. This scheduler interface is not public and compatibility may not be maintained.
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:09 [vllm.py:397] Cudagraph is disabled under eager mode
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:09 [platform.py:141] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:09 [platform.py:181] Compilation disabled, using eager mode by default
> (EngineCore_DP0 pid=271251) INFO 11-06 09:33:09 [gc_utils.py:40] GC Debug Config. enabled:False,top_objects:-1
> INFO 11-06 09:33:09 [llm.py:343] Supported tasks: ['generate']
> Adding requests: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 66.29it/s]
> Processed prompts: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:03<00:00,  3.95s/it, est. speed input: 1.52 toks/s, output: 10.13 toks/s]
> Prompt: '123412', Generated text: '34这条路的长度是1000米，每块砖的面积是10 forbidden, 123oud, 1AMENT, 1atos, 1itol,'
