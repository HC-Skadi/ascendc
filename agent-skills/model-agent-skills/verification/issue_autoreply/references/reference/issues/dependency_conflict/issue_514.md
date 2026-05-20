# Issue #514: [Bug][V1]: Qwen2.5_vl not support on V1 engine

## 基本信息

- **编号**: #514
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/514
- **创建时间**: 2025-04-14T03:36:09Z
- **关闭时间**: 2025-06-07T08:53:21Z
- **更新时间**: 2025-06-07T08:53:21Z
- **提交者**: @Potabk
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
INFO 04-14 03:30:20 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-14 03:30:20 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-14 03:30:20 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-14 03:30:20 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-14 03:30:20 [__init__.py:44] plugin ascend loaded.
INFO 04-14 03:30:20 [__init__.py:230] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.10.16 (main, Dec 11 2024, 16:18:56) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1804.eulerosv2r10.aarch64-aarch64-with-glibc2.35
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
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
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
[pip3] mypy==1.15.0
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] sentence-transformers==3.4.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] transformers==4.49.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] sentence-transformers     3.4.1                    pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250320          pypi_0    pypi
[conda] transformers              4.49.0                   pypi_0    pypi
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.8.3.dev63+g08a6c748
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
</details>


### 🐛 Describe the bug

I'm using v1 engine serve `qwen2.5_vl_7b`, but got oom error,  But the same problem does not occur on v0
serving command:
```
VLLM_USE_V1=1 vllm serve Qwen/Qwen2.5-VL-7B-Instruct --trust-remote-code --max-model-len 8192
```
error trace:
```
ERROR 04-14 03:35:21 [core.py:386] EngineCore hit an exception: Traceback (most recent call last):
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/v1/engine/core.py", line 377, in run_engine_core
ERROR 04-14 03:35:21 [core.py:386]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/v1/engine/core.py", line 319, in __init__
ERROR 04-14 03:35:21 [core.py:386]     super().__init__(vllm_config, executor_class, log_stats)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/v1/engine/core.py", line 71, in __init__
ERROR 04-14 03:35:21 [core.py:386]     self._initialize_kv_caches(vllm_config)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/v1/engine/core.py", line 132, in _initialize_kv_caches
ERROR 04-14 03:35:21 [core.py:386]     available_gpu_memory = self.model_executor.determine_available_memory()
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/v1/executor/abstract.py", line 66, in determine_available_memory
ERROR 04-14 03:35:21 [core.py:386]     output = self.collective_rpc("determine_available_memory")
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-14 03:35:21 [core.py:386]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/utils.py", line 2363, in run_method
ERROR 04-14 03:35:21 [core.py:386]     return func(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 168, in determine_available_memory
ERROR 04-14 03:35:21 [core.py:386]     self.model_runner.profile_run()
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 698, in profile_run
ERROR 04-14 03:35:21 [core.py:386]     self._profile_multimodal()
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 645, in _profile_multimodal
ERROR 04-14 03:35:21 [core.py:386]     dummy_encoder_outputs = self.model.get_multimodal_embeddings(
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 989, in get_multimodal_embeddings
ERROR 04-14 03:35:21 [core.py:386]     vision_embeddings = self._process_image_input(image_input)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 926, in _process_image_input
ERROR 04-14 03:35:21 [core.py:386]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-14 03:35:21 [core.py:386]     return self._call_impl(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-14 03:35:21 [core.py:386]     return forward_call(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 674, in forward
ERROR 04-14 03:35:21 [core.py:386]     hidden_states = blk(
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-14 03:35:21 [core.py:386]     return self._call_impl(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-14 03:35:21 [core.py:386]     return forward_call(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 376, in forward
ERROR 04-14 03:35:21 [core.py:386]     x = x + self.attn(self.norm1(x),
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-14 03:35:21 [core.py:386]     return self._call_impl(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/miniconda3/envs/vllm_latest/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-14 03:35:21 [core.py:386]     return forward_call(*args, **kwargs)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 277, in forward
ERROR 04-14 03:35:21 [core.py:386]     q = apply_rotary_pos_emb_vision(q,
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_vl.py", line 242, in apply_rotary_pos_emb_vision
ERROR 04-14 03:35:21 [core.py:386]     output = apply_rotary_emb(t_, cos, sin).type_as(t)
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_vl.py", line 227, in apply_rotary_emb_torch
ERROR 04-14 03:35:21 [core.py:386]     rotate_half(x[..., :ro_dim], interleaved) * sin, x[..., ro_dim:]
ERROR 04-14 03:35:21 [core.py:386]   File "/root/wl/oldfiles/vllm-project/vllm/vllm/model_executor/models/qwen2_vl.py", line 200, in rotate_half
ERROR 04-14 03:35:21 [core.py:386]     return torch.cat((-x2, x1), dim=-1)
ERROR 04-14 03:35:21 [core.py:386] RuntimeError: NPU out of memory. Tried to allocate 322.00 MiB (NPU 0; 60.97 GiB total capacity; 57.51 GiB already allocated; 57.51 GiB current active; 20.12 MiB free; 59.53 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
ERROR 04-14 03:35:21 [core.py:386] 
CRITICAL 04-14 03:35:21 [core_client.py:359] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
Killed
```

