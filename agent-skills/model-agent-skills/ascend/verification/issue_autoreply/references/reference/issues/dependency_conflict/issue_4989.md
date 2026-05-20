# Issue #4989: [Bug]: DeepSeek-OCR loop output

## 基本信息

- **编号**: #4989
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4989
- **创建时间**: 2025-12-13T11:23:20Z
- **关闭时间**: 2025-12-16T06:53:36Z
- **更新时间**: 2025-12-17T01:19:49Z
- **提交者**: @Potabk
- **评论数**: 3

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

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:57:00) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
Model:                                0
Thread(s) per core:                   1
Core(s) per cluster:                  80
Socket(s):                            -
Cluster(s):                           4
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
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.2.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.1
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.12.0
vLLM Ascend Version: 0.11.0rc1.dev626+g358194625 (git sha: 358194625)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=3,6,14,7,10,12,0,5,9,13,1,15,8,2,4,11
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=true
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
| npu-smi 25.2.1                   Version: 25.2.1                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 165.3       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3143 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2887 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 163.6       35                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3141 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           35                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2882 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 161.5       34                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3133 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           34                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 165.0       34                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3139 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           34                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 167.1       34                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3143 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           35                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 165.7       34                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3140 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           37                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2881 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 162.5       36                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3143 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           36                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2876 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 158.6       35                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3145 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           36                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2876 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

Using vllm v0.12.0 and vllm-ascend latest main, run `DeepSeek-OCR` failed

```python
# /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-OCR

from vllm import LLM, SamplingParams
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
from PIL import Image

# Create model instance
llm = LLM(
    model="deepseek-ai/DeepSeek-OCR",
    enable_prefix_caching=False,
    mm_processor_cache_gb=0,
    logits_processors=[NGramPerReqLogitsProcessor]
)

# Prepare batched input with your image file
image_1 = Image.open("/root/.cache/vllm/assets/vllm_public_assets/cherry_blossom.jpg").convert("RGB")
image_2 = Image.open("/root/.cache/vllm/assets/vllm_public_assets/stop_sign.jpg").convert("RGB")
prompt = "<image>\nFree OCR."

model_input = [
    {
        "prompt": prompt,
        "multi_modal_data": {"image": image_1}
    },
    {
        "prompt": prompt,
        "multi_modal_data": {"image": image_2}
    }
]

sampling_param = SamplingParams(
            temperature=0.0,
            max_tokens=8192,
            # ngram logit processor args
            extra_args=dict(
                ngram_size=30,
                window_size=90,
                whitelist_token_ids={128821, 128822},  # whitelist: <td>, </td>
            ),
            skip_special_tokens=False,
        )
# Generate output
model_outputs = llm.generate(model_input, sampling_param)

# Print output
for output in model_outputs:
    print(output.outputs[0].text)

```

error logs

```bash
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海世博城
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博局
上海世博城
上海
ERROR 12-13 11:19:54 [core_client.py:600] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.
```

