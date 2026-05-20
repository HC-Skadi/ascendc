# Issue #2235: [Bug]: vllm 拉 DeepSeek-R1-Distill-Llama-70B  报错

## 基本信息

- **编号**: #2235
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2235
- **创建时间**: 2025-08-06T03:11:11Z
- **关闭时间**: 2025-08-07T03:20:02Z
- **更新时间**: 2025-08-07T03:20:02Z
- **提交者**: @luckfu
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
python collect_env.py
Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.0.3
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.7.1+cpu
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.35

==============================
       CUDA / GPU Info
==============================
Is CUDA available            : False
CUDA runtime version         : No CUDA
CUDA_MODULE_LOADING set to   : N/A
GPU models and configuration : No CUDA
Nvidia driver version        : No CUDA
cuDNN version                : No CUDA
HIP runtime version          : N/A
MIOpen runtime version       : N/A
Is XNNPACK available         : True

==============================
          CPU Info
==============================
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

==============================
Versions of relevant libraries
==============================
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.53.3
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
Neuron SDK Version           : N/A
vLLM Version                 : 0.10.0
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
  Could not collect

==============================
     Environment Variables
==============================
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
```

</details>


### 🐛 Describe the bug

 python3 -m vllm.entrypoints.openai.api_server \
> --model /models/DeepSeek-R1-Distill-Llama-70B \
> --served-model-name DeepSeek70B \
> --max-model-len=32767 \
> -tp=8 \
> --host=0.0.0.0 \
> --port=8008 \
> --gpu-memory-utilization=0.9 \
> --trust-remote-code

```text
......
(VllmWorker rank=7 pid=1568) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.04 seconds
(VllmWorker rank=3 pid=1564) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.13 seconds
(VllmWorker rank=4 pid=1565) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.14 seconds
(VllmWorker rank=0 pid=1561) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.01 seconds
(VllmWorker rank=5 pid=1566) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.08 seconds
(VllmWorker rank=2 pid=1563) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.13 seconds
(VllmWorker rank=1 pid=1562) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.14 seconds
(VllmWorker rank=6 pid=1567) INFO 08-06 10:40:26 [default_loader.py:262] Loading weights took 35.11 seconds
(VllmWorker rank=3 pid=1564) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=4 pid=1565) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=5 pid=1566) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=1 pid=1562) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=0 pid=1561) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=2 pid=1563) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=6 pid=1567) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=7 pid=1568) INFO 08-06 10:40:27 [model_runner_v1.py:2070] Loading model weights took 16.4610 GB
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] WorkerProc hit an exception.
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 155, in determine_available_memory
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     self.model_runner.profile_run()
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1965, in profile_run
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states = self._dummy_run(self.max_num_tokens,
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1940, in _dummy_run
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 584, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     model_output = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 272, in __call__
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     output = self.compiled_callable(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 659, in _fn
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     raise e.with_traceback(None) from None
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] torch._dynamo.exc.Unsupported: Operator does not support running with fake tensors
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   Explanation:
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   Hint: see https://docs.google.com/document/d/1GgvOe7C8_NVOMLOCwDaYV1mXXyHMXY7ExoewHqooxrs/edit#heading=h.64r4npvq0w0 for how to fix
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   Developer debug context: unsupported operator: _C.rotary_embedding.default
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] from user code:
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]    File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 392, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states, residual = layer(positions, hidden_states, residual)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 305, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states = self.self_attn(positions=positions,
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 202, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     q, k = self.rotary_emb(positions, q, k)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 44, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return self._forward_method(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 62, in rope_forward_oot
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     query, key = torch.ops._C.rotary_embedding(
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 155, in determine_available_memory
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     self.model_runner.profile_run()
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1965, in profile_run
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states = self._dummy_run(self.max_num_tokens,
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1940, in _dummy_run
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 584, in forward
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     model_output = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 272, in __call__
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     output = self.compiled_callable(*args, **kwargs)
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 659, in _fn
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]     raise e.with_traceback(None) from None
(VllmWorker rank=3 pid=1564) ERROR 08-06 10:40:29 [multiproc_executor.py:546]
......
```

[报错日志(1).txt](https://github.com/user-attachments/files/21610209/1.txt)
