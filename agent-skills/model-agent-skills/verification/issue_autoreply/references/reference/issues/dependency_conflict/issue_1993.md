# Issue #1993: [Bug]: 300I DUO OUT OF MEMORY

## 基本信息

- **编号**: #1993
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1993
- **创建时间**: 2025-07-24T09:46:17Z
- **关闭时间**: 2025-12-23T11:31:06Z
- **更新时间**: 2025-12-23T11:31:06Z
- **提交者**: @bouyeijiang
- **评论数**: 13

## 标签

bug; 310p

## 问题描述

### Your current environment

Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Kylin Linux Advanced Server V10 (Sword) (aarch64)
GCC version: (GCC) 7.3.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.28

Python version: 3.11.13 (main, Jul 17 2025, 10:24:39) [GCC 7.3.0] (64-bit runtime)
Python platform: Linux-4.19.90-25.48.v2101.ky10.aarch64-aarch64-with-glibc2.28

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             128
On-line CPU(s) list:                0-127
Thread(s) per core:                 1
Core(s) per socket:                 64
Socket(s):                          2
NUMA node(s):                       4
Vendor ID:                          HiSilicon
Model:                              0
Model name:                         Kunpeng-920
Stepping:                           0x1
BogoMIPS:                           200.00
L1d cache:                          8 MiB
L1i cache:                          8 MiB
L2 cache:                           64 MiB
L3 cache:                           128 MiB
NUMA node0 CPU(s):                  0-31
NUMA node1 CPU(s):                  32-63
NUMA node2 CPU(s):                  64-95
NUMA node3 CPU(s):                  96-127
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm

Versions of relevant libraries:
[pip3] mindietorch==2.0rc2+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.53.2
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3

ENV Variables:
VLLM_USE_MODELSCOPE=true
TORCH_DEVICE_BACKEND_AUTOLOAD=0
PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:40960
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/gcc-9.4/lib64:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1                               Version: 25.0.rc1.1                                   |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 6       310P3                 | OK              | NA           55                0     / 0             |
| 0       0                     | 0000:83:00.0    | 0            1175 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 6       310P3                 | OK              | NA           52                3262  / 3262          |
| 1       1                     | 0000:83:00.0    | 0            8322 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| 6       1                     | 293029          | python3.11               | 6612                      |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux


### 🐛 Describe the bug

import os
from vllm import LLM, SamplingParams
#import mindie_turbo

#os.environ["CUDA_VISIBLE_DEVICES"]="0,1"
#os.environ["PYTORCH_CUDA_ALLOC_CONF"]="max_split_size_mb:64"

prompts = [
     "Hello, my name is",
     "The president of the United States is",
     "The capital of France is",
     "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8,top_p=0.95)
 # Create an LLM.
llm = LLM(model="./models/qwen2.5-vl-3")

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
