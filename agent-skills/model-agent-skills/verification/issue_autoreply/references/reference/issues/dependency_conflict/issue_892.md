# Issue #892: [Bug]: v0.7.3 model outputs a chain of numbers

## 基本信息

- **编号**: #892
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/892
- **创建时间**: 2025-05-19T00:44:52Z
- **关闭时间**: 2025-07-13T09:24:02Z
- **更新时间**: 2025-07-13T09:24:02Z
- **提交者**: @xyyyzzz
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: EulerOS 2.0 (SP10) (aarch64)
GCC version: (GCC) 7.3.0
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.28

Python version: 3.9.20 (main, Oct  3 2024, 07:31:44)  [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1960.eulerosv2r10.aarch64-aarch64-with-glibc2.28

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
NUMA node(s):                       8
Vendor ID:                          HiSilicon
Model:                              0
Model name:                         Kunpeng-920
Stepping:                           0x1
BogoMIPS:                           200.00
L1d cache:                          12 MiB
L1i cache:                          12 MiB
L2 cache:                           96 MiB
L3 cache:                           192 MiB
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
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs

Versions of relevant libraries:
[pip3] mypy==1.11.1
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.25.0
[pip3] pyzmq==26.2.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torch-tb-profiler-ascend==0.4.0.11
[pip3] torchvision==0.20.1
[pip3] transformers==4.50.2
[pip3] transformers-stream-generator==0.0.4
[conda] numpy                     1.25.0                   pypi_0    pypi
[conda] pyzmq                     26.2.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1                    pypi_0    pypi
[conda] torch-tb-profiler-ascend  0.4.0.11                 pypi_0    pypi
[conda] torchvision               0.20.1                   pypi_0    pypi
[conda] transformers              4.50.2                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.4                    pypi_0    pypi
vLLM Version: 0.7.4.dev0+ged6e907.d20250516 (git sha: ed6e907, date: 20250516)
vLLM Ascend Version: 0.7.4.dev0+g779eebb.d20250516 (git sha: 779eebb, date: 20250516)


CANN:
package_name=Ascend-cann-toolkit
version=8.0.T60
innerversion=V100R001C20B029
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.T60/aarch64-linux
```

</details>


### 🐛 Describe the bug

When prompt is "The future of AI is" and the model is DeepSeek-R1-Distill-Qwen-7B, I get a chain of numbers for the generated text. This error starts occurring from vllm-ascend v0.7.3.

![Image](https://github.com/user-attachments/assets/5d2a0c49-6a2c-4ab0-872e-cb6f6dc6d855)

Offline inference example:
```python
from vllm import LLM, SamplingParams
prompts = [
    "The future of AI is ",
]

# Create a sampling params object.
sampling_params = SamplingParams(max_tokens=100, temperature=0.0)
# Create an LLM.
llm = LLM(model="/disknpu/llm/model/DeepSeek-R1-Distill-Qwen-7B", enable_chunked_prefill=True, max_num_batched_tokens=2048, gpu_memory_utilization=0.5, block_size=16)

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Generated text: {generated_text}")
```
