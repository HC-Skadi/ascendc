# Issue #1048: [Bug][V1]:  Failed to start openai  api_server with exception "Parameter block_size has unsupported type list[int]"

## 基本信息

- **编号**: #1048
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1048
- **创建时间**: 2025-06-03T07:32:34Z
- **关闭时间**: 2025-06-10T07:11:29Z
- **更新时间**: 2025-06-10T08:55:25Z
- **提交者**: @farawayboat
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.34

Python version: 3.11.5 (main, Sep 11 2023, 13:14:08) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.r865_35.hce2.aarch64-aarch64-with-glibc2.34

CPU:
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
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[pip3] transformers-stream-generator==0.0.5
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1                    pypi_0    pypi
[conda] torchaudio                2.5.1                    pypi_0    pypi
[conda] torchvision               0.20.1                   pypi_0    pypi
[conda] transformers              4.51.3                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.5                    pypi_0    pypi
vLLM Version: 0.1.dev6389+g246e3e0.empty (git sha: 246e3e0, date: mpty)
vLLM Ascend Version: main

ENV Variables:
TORCH_PLUGIN_PKG=/usr/local/Ascend/latest/tools/ms_fmk_transplt/torch_npu_bridge
ASCEND_OPP_PATH=/usr/local/Ascend/latest/opp
LD_LIBRARY_PATH=:/usr/local/Ascend/latest/lib64/plugin/nnengine:/usr/local/Ascend/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/latest/lib64:/usr/local/Ascend/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/compat:/usr/local/cuda/lib64/:/opt/huawei/miniconda3/lib/python3.11/site-packages/torch/lib:/opt/huawei/miniconda3/lib/python3.11/site-packages/torch_npu/lib
ASCEND_AICPU_PATH=/usr/local/Ascend/latest
ASCEND_HOME_PATH=/usr/local/Ascend/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 88.2        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2825 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 84.8        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2825 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 86.6        36                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2829 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 86.6        35                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2840 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 88.8        34                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          31859/ 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 85.0        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2824 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 86.2        35                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2840 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 86.3        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2830 / 32768         |
+===========================+===============+====================================================+


CANN:
package_name=Ascend-cann-toolkit
version=8.1.T18
innerversion=V100R001C21SPC001B229
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.T18/aarch64-linux

```

</details>


### 🐛 Describe the bug

使用 vllm-ascend main 分支代码启动 openai api_server:

```shell
[ -e /usr/local/Ascend/ascend-toolkit/set_env.sh ] &&  source /usr/local/Ascend/ascend-toolkit/set_env.sh
[ -e /usr/local/Ascend/mindie/set_env.sh ] &&  source /usr/local/Ascend/mindie/set_env.sh
[ -e /usr/local/Ascend/nnal/atb/set_env.sh ] &&  source /usr/local/Ascend/nnal/atb/set_env.sh
[ -e /usr/local/atb-models/set_env.sh ] &&  source /usr/local/atb-models/set_env.sh
export ASCEND_RT_VISIBLE_DEVICES=7
export NPU_VISIBLE_DEVICES=$ASCEND_RT_VISIBLE_DEVICES
export ASCEND_LAUNCH_BLOCKING=1
export VLLM_PLUGINS=ascend
export VLLM_USE_V1=1
export LD_LIBRARY_PATH="/opt/huawei/miniconda3/envs/vllm/lib:$LD_LIBRARY_PATH"


python -m vllm.entrypoints.openai.api_server \
--model=/home/model/Qwen2.5-7B-Instruct \
--max-num-seqs=4 \
--max-model-len=4096 \
--tensor-parallel-size=1 \
--dtype="bfloat16" \
--disable-custom-all-reduce \
--trust-remote-code \
--host="127.0.0.1" \
--port=18080 \
--gpu-memory-utilization=0.8
```

报错如下：

```
INFO 06-03 15:25:43 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-03 15:25:43 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-03 15:25:46 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 06-03 15:25:46 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 06-03 15:25:46 [__init__.py:44] plugin ascend loaded.
INFO 06-03 15:25:46 [__init__.py:239] Platform plugin ascend is activated
WARNING 06-03 15:25:49 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 06-03 15:25:51 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 06-03 15:25:51 [__init__.py:32] name=lora_filesystem_resolver, value=vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver
INFO 06-03 15:25:51 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 06-03 15:25:53 [config.py:1903] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-03 15:25:55 [api_server.py:1289] vLLM API server version 0.1.dev6389+g246e3e0.empty
INFO 06-03 15:25:57 [config.py:1903] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-03 15:25:57 [cli_args.py:300] non-default args: {'host': '127.0.0.1', 'port': 18080, 'model': '/home/model/Qwen2.5-7B-Instruct', 'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 4096, 'disable_custom_all_reduce': True, 'gpu_memory_utilization': 0.8, 'max_num_seqs': 4}
INFO 06-03 15:26:14 [config.py:787] This model supports multiple tasks: {'classify', 'embed', 'generate', 'reward', 'score'}. Defaulting to 'generate'.
WARNING 06-03 15:26:14 [arg_utils.py:1595] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 06-03 15:26:14 [config.py:1903] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-03 15:26:14 [config.py:2112] Chunked prefill is enabled with max_num_batched_tokens=2048.
WARNING 06-03 15:26:14 [platform.py:142] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 06-03 15:26:14 [platform.py:150] Compilation disabled, using eager mode by default
INFO 06-03 15:26:21 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-03 15:26:21 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-03 15:26:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 06-03 15:26:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 06-03 15:26:24 [__init__.py:44] plugin ascend loaded.
INFO 06-03 15:26:24 [__init__.py:239] Platform plugin ascend is activated
WARNING 06-03 15:26:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 06-03 15:26:30 [core.py:427] Waiting for init message from front-end.
WARNING 06-03 15:26:30 [platform.py:142] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 06-03 15:26:30 [platform.py:150] Compilation disabled, using eager mode by default
INFO 06-03 15:26:30 [core.py:61] Initializing a V1 LLM engine (v0.1.dev6389+g246e3e0.empty) with config: model='/home/model/Qwen2.5-7B-Instruct', speculative_config=None, tokenizer='/home/model/Qwen2.5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/model/Qwen2.5-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"custom_ops": ["all"], "splitting_ops": ["vllm.unified_attention", "vllm.unified_attention_with_output"], "compile_sizes": [], "use_cudagraph": true, "cudagraph_num_of_warmups": 1, "cudagraph_capture_sizes": [512, 504, 496, 488, 480, 472, 464, 456, 448, 440, 432, 424, 416, 408, 400, 392, 384, 376, 368, 360, 352, 344, 336, 328, 320, 312, 304, 296, 288, 280, 272, 264, 256, 248, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 4, 2, 1], "max_capture_size": 512}
INFO 06-03 15:26:30 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 06-03 15:26:30 [__init__.py:32] name=lora_filesystem_resolver, value=vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver
INFO 06-03 15:26:30 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
ERROR 06-03 15:26:30 [core.py:489] EngineCore failed to start.
ERROR 06-03 15:26:30 [core.py:489] Traceback (most recent call last):
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 480, in run_engine_core
ERROR 06-03 15:26:30 [core.py:489]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-03 15:26:30 [core.py:489]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 379, in __init__
ERROR 06-03 15:26:30 [core.py:489]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 67, in __init__
ERROR 06-03 15:26:30 [core.py:489]     self.model_executor = executor_class(vllm_config)
ERROR 06-03 15:26:30 [core.py:489]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 06-03 15:26:30 [core.py:489]     self._init_executor()
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 45, in _init_executor
ERROR 06-03 15:26:30 [core.py:489]     self.collective_rpc("init_worker", args=([kwargs], ))
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-03 15:26:30 [core.py:489]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-03 15:26:30 [core.py:489]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/utils.py", line 2598, in run_method
ERROR 06-03 15:26:30 [core.py:489]     return func(*args, **kwargs)
ERROR 06-03 15:26:30 [core.py:489]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 558, in init_worker
ERROR 06-03 15:26:30 [core.py:489]     worker_class = resolve_obj_by_qualname(
ERROR 06-03 15:26:30 [core.py:489]                    ^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/utils.py", line 2184, in resolve_obj_by_qualname
ERROR 06-03 15:26:30 [core.py:489]     module = importlib.import_module(module_name)
ERROR 06-03 15:26:30 [core.py:489]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/importlib/__init__.py", line 126, in import_module
ERROR 06-03 15:26:30 [core.py:489]     return _bootstrap._gcd_import(name[level:], package, level)
ERROR 06-03 15:26:30 [core.py:489]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
ERROR 06-03 15:26:30 [core.py:489]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 46, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm_ascend.worker.model_runner_v1 import NPUModelRunner
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 39, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe import FusedMoE
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/__init__.py", line 6, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe.layer import (
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 51, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe.fused_moe import grouped_topk
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 14, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe.deep_gemm_moe import (
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/deep_gemm_moe.py", line 10, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe.moe_permute_unpermute import (
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py", line 9, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.fused_moe.utils import _fp8_perm
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/fused_moe/utils.py", line 8, in <module>
ERROR 06-03 15:26:30 [core.py:489]     from vllm.model_executor.layers.quantization.utils.fp8_utils import (
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 183, in <module>
ERROR 06-03 15:26:30 [core.py:489]     direct_register_custom_op(
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/vllm/utils.py", line 2166, in direct_register_custom_op
ERROR 06-03 15:26:30 [core.py:489]     schema_str = torch.library.infer_schema(op_func,
ERROR 06-03 15:26:30 [core.py:489]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/torch/_library/infer_schema.py", line 106, in infer_schema
ERROR 06-03 15:26:30 [core.py:489]     error_fn(
ERROR 06-03 15:26:30 [core.py:489]   File "/opt/huawei/miniconda3/lib/python3.11/site-packages/torch/_library/infer_schema.py", line 58, in error_fn
ERROR 06-03 15:26:30 [core.py:489]     raise ValueError(
ERROR 06-03 15:26:30 [core.py:489] ValueError: infer_schema(func): Parameter block_size has unsupported type list[int]. The valid types are: dict_keys([<class 'torch.Tensor'>, typing.Optional[torch.Tensor], typing.Sequence[torch.Tensor], typing.List[torch.Tensor], typing.Sequence[typing.Optional[torch.Tensor]], typing.List[typing.Optional[torch.Tensor]], <class 'int'>, typing.Optional[int], typing.Sequence[int], typing.List[int], typing.Optional[typing.Sequence[int]], typing.Optional[typing.List[int]], <class 'float'>, typing.Optional[float], typing.Sequence[float], typing.List[float], typing.Optional[typing.Sequence[float]], typing.Optional[typing.List[float]], <class 'bool'>, typing.Optional[bool], typing.Sequence[bool], typing.List[bool], typing.Optional[typing.Sequence[bool]], typing.Optional[typing.List[bool]], <class 'str'>, typing.Optional[str], typing.Union[int, float, bool], typing.Union[int, float, bool, NoneType], typing.Sequence[typing.Union[int, float, bool]], typing.List[typing.Union[int, float, bool]], <class 'torch.dtype'>, typing.Optional[torch.dtype], <class 'torch.device'>, typing.Optional[torch.device]]). Got func with signature (input: torch.Tensor, weight: torch.Tensor, block_size: list[int], weight_scale: torch.Tensor, input_scale: Optional[torch.Tensor] = None, bias: Optional[torch.Tensor] = None, cutlass_block_fp8_supported: bool = False, use_aiter_and_is_supported: bool = False) -> torch.Tensor)
[ERROR] 2025-06-03-15:26:33 (PID:1399, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

```

同样的环境， 能正常进行离线推理。
