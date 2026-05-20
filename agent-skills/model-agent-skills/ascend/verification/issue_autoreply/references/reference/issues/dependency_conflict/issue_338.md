# Issue #338: [Bug]: The inference of Qwen2/2.5-VL-7B is very slow.

## 基本信息

- **编号**: #338
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/338
- **创建时间**: 2025-03-15T07:24:07Z
- **关闭时间**: 2025-05-14T02:35:36Z
- **更新时间**: 2025-12-12T06:05:51Z
- **提交者**: @Ziang-Zack-Gao
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: EulerOS 2.0 (SP10) (aarch64)
GCC version: (GCC) 7.3.0
Clang version: Could not collect
CMake version: version 3.16.5
Libc version: glibc-2.28

Python version: 3.9.10 | packaged by conda-forge | (main, Feb  1 2022, 21:53:27)  [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.28
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
NUMA node(s):                    8
Vendor ID:                       HiSilicon
Model:                           0
Model name:                      Kunpeng-920
Stepping:                        0x1
BogoMIPS:                        200.00
L1d cache:                       12 MiB
L1i cache:                       12 MiB
L2 cache:                        96 MiB
L3 cache:                        192 MiB
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs

Versions of relevant libraries:
[pip3] modelarts-pytorch-model-server-arm==1.0.6
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.26.4
[pip3] onnx==1.16.1
[pip3] onnxconverter-common==1.14.0
[pip3] onnxruntime==1.15.1
[pip3] pyzmq==26.2.1
[pip3] skl2onnx==1.17.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[pip3] vector-quantize-pytorch==1.18.5
[conda] modelarts-pytorch-model-server-arm 1.0.6                     <pip>
[conda] numpy                     1.26.4                    <pip>
[conda] pyzmq                     26.2.1                    <pip>
[conda] torch                     2.5.1                     <pip>
[conda] torch-npu                 2.5.1.dev20250308           <pip>
[conda] torchaudio                2.5.1                     <pip>
[conda] torchvision               0.20.1                    <pip>
[conda] transformers              4.49.0                    <pip>
[conda] vector-quantize-pytorch   1.18.5                    <pip>
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/home/ma-user/work/dataset/multimodal_understand_llm/envs/cp39-pytorch251-vllm/lib/python3.9/site-packages/cv2/../../lib64:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/lib64:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/ma-user/work/dataset/multimodal_understand_llm/dependency/cann_8_0_0/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/third_party/dnnl
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```

</details>


### 🐛 Describe the bug

``` python

model = LLM(
    model=MODEL_PATH,
    limit_mm_per_prompt={"image": 1},
    tensor_parallel_size=2,
    max_model_len=16384,
    trust_remote_code=True,
    max_num_seqs=1
)

```

The inference of Qwen2/2.5-VL-7B is very slow. Only about 7 tokens/s when max_num_seqs=1, and 30 tokens/s (for Qwen2-VL-7B, also 7 tokens/s for Qwen2.5-VL-7B) when max_num_seqs=8. Please help me solve this issue. Thx!
