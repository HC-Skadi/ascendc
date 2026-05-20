# Issue #1249: [Bug]: export VLLM_USE_V1=1  后启动报错

## 基本信息

- **编号**: #1249
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1249
- **创建时间**: 2025-06-17T01:16:43Z
- **关闭时间**: 2025-10-27T06:50:10Z
- **更新时间**: 2025-12-15T03:38:11Z
- **提交者**: @BZFF
- **评论数**: 15

## 标签

bug

## 问题描述

### Your current environment

<details>

<summary>The output of `python collect_env.py`</summary>


Your output of above commands here
```text
INFO 06-17 01:14:48 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-17 01:14:48 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-17 01:14:49 [__init__.py:31] Available plugins for group vllm.platform_plugins:
INFO 06-17 01:14:49 [__init__.py:33] - ascend -> vllm_ascend:register
INFO 06-17 01:14:49 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-17 01:14:49 [__init__.py:234] Platform plugin ascend is activated
WARNING:root:Failed to import 'vllm_ascend.vllm_ascend_C': /lib/aarch64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by /vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so). All custom ops will be disabled. 
WARNING 06-17 01:14:51 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/vllm-ascend-env/lib/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 20.04.6 LTS (aarch64)
GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.31

Python version: 3.11.11 (main, Dec  4 2024, 08:55:08) [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.31

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
Vendor ID:                       0x48
Model:                           0
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
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.7.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.9.0
vLLM Ascend Version: 0.9.0rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc1                 Version: 24.1.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 88.2        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2787 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 90.1        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2785 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 88.4        39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2785 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 94.7        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2785 / 32768         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

```


</details>

### 🐛 Describe the bug
export VLLM_USE_V1=1 启动后报错

启动命令
vllm serve /models/Qwen3-32B-20250429/ --enable-auto-tool-choice --tool-call-parser hermes --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 6090 --uvicorn-log-level info --served-model-name Qwen3-32B

```

INFO 06-17 01:09:03 [kv_cache_utils.py:637] GPU KV cache size: 159,232 tokens
INFO 06-17 01:09:03 [kv_cache_utils.py:640] Maximum concurrency for 40,960 tokens per request: 3.89x
INFO 06-17 01:09:03 [kv_cache_utils.py:637] GPU KV cache size: 159,232 tokens
INFO 06-17 01:09:03 [kv_cache_utils.py:640] Maximum concurrency for 40,960 tokens per request: 3.89x
INFO 06-17 01:09:03 [kv_cache_utils.py:637] GPU KV cache size: 159,232 tokens
INFO 06-17 01:09:03 [kv_cache_utils.py:640] Maximum concurrency for 40,960 tokens per request: 3.89x
INFO 06-17 01:09:03 [kv_cache_utils.py:637] GPU KV cache size: 159,232 tokens
INFO 06-17 01:09:03 [kv_cache_utils.py:640] Maximum concurrency for 40,960 tokens per request: 3.89x
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 207, in compile_or_warm_up_model
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self.model_runner.capture_model()
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1781, in capture_model
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self._dummy_run(num_tokens)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen3.py", line 300, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 245, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 340, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise e
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "<eval_with_key>.130", line 522, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 207, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     entry.output = weak_ref_tensors(output)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in weak_ref_tensors
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in <genexpr>
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                  ^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1852, in weak_ref_tensor
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return torch.ops._C.weak_ref_tensor(tensor)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_ops.py", line 1225, in __getattr__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise AttributeError(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 207, in compile_or_warm_up_model
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self.model_runner.capture_model()
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1781, in capture_model
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self._dummy_run(num_tokens)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen3.py", line 300, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 245, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 340, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise e
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "<eval_with_key>.130", line 522, in forward
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 207, in __call__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     entry.output = weak_ref_tensors(output)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in weak_ref_tensors
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in <genexpr>
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                  ^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1852, in weak_ref_tensor
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return torch.ops._C.weak_ref_tensor(tensor)
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_ops.py", line 1225, in __getattr__
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise AttributeError(
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
(VllmWorker rank=1 pid=3742) ERROR 06-17 01:09:04 [multiproc_executor.py:522] 
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 207, in compile_or_warm_up_model
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self.model_runner.capture_model()
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1781, in capture_model
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self._dummy_run(num_tokens)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen3.py", line 300, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 245, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 340, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise e
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "<eval_with_key>.130", line 522, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 207, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     entry.output = weak_ref_tensors(output)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in weak_ref_tensors
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in <genexpr>
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                  ^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1852, in weak_ref_tensor
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return torch.ops._C.weak_ref_tensor(tensor)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_ops.py", line 1225, in __getattr__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise AttributeError(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 207, in compile_or_warm_up_model
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self.model_runner.capture_model()
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1781, in capture_model
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     self._dummy_run(num_tokens)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen3.py", line 300, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 245, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 340, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise e
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "<eval_with_key>.130", line 522, in forward
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 207, in __call__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     entry.output = weak_ref_tensors(output)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                    ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in weak_ref_tensors
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1869, in <genexpr>
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return tuple(weak_ref_tensor(t) for t in tensors)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]                  ^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/utils.py", line 1852, in weak_ref_tensor
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     return torch.ops._C.weak_ref_tensor(tensor)
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]   File "/vllm-ascend-env/lib/python3.11/site-packages/torch/_ops.py", line 1225, in __getattr__
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522]     raise AttributeError(
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
(VllmWorker rank=0 pid=3741) ERROR 06-17 01:09:04 [multiproc_executor.py:522] 
ERROR 06-17 01:09:04 [core.py:500] EngineCore failed to start.
ERROR 06-17 01:09:04 [core.py:500] Traceback (most recent call last):
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 491, in run_engine_core
ERROR 06-17 01:09:04 [core.py:500]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-17 01:09:04 [core.py:500]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 390, in __init__
ERROR 06-17 01:09:04 [core.py:500]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 78, in __init__
ERROR 06-17 01:09:04 [core.py:500]     self._initialize_kv_caches(vllm_config)
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 164, in _initialize_kv_caches
ERROR 06-17 01:09:04 [core.py:500]     self.model_executor.initialize_from_config(kv_cache_configs)
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 65, in initialize_from_config
ERROR 06-17 01:09:04 [core.py:500]     self.collective_rpc("compile_or_warm_up_model")
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 215, in collective_rpc
ERROR 06-17 01:09:04 [core.py:500]     result = get_response(w, dequeue_timeout)
ERROR 06-17 01:09:04 [core.py:500]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-17 01:09:04 [core.py:500]   File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 202, in get_response
ERROR 06-17 01:09:04 [core.py:500]     raise RuntimeError(
ERROR 06-17 01:09:04 [core.py:500] RuntimeError: Worker failed with error ''_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'', please check the stack trace above for the root cause
ERROR 06-17 01:09:12 [multiproc_executor.py:135] Worker proc VllmWorker-3 died unexpectedly, shutting down executor.
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 504, in run_engine_core
    raise e
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 491, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 78, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 164, in _initialize_kv_caches
    self.model_executor.initialize_from_config(kv_cache_configs)
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 65, in initialize_from_config
    self.collective_rpc("compile_or_warm_up_model")
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 215, in collective_rpc
    result = get_response(w, dequeue_timeout)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 202, in get_response
    raise RuntimeError(
RuntimeError: Worker failed with error ''_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/vllm-ascend-env/bin/vllm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 56, in main
    args.dispatch_function(args)
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 42, in cmd
    uvloop.run(run_server(args))
  File "/vllm-ascend-env/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
    return runner.run(wrapper())
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/vllm-ascend-env/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1324, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 153, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 185, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 157, in from_vllm_config
    return cls(
           ^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 123, in __init__
    self.engine_core = core_client_class(
                       ^^^^^^^^^^^^^^^^^^
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 734, in __init__
    super().__init__(
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 418, in __init__
    self._wait_for_engine_startup(output_address, parallel_config)
  File "/vllm-ascend-env/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 484, in _wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-06-17-01:09:15 (PID:3464, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
