# Issue #3109: [Bug]: RuntimeError: start (0) + length (6144) exceeds dimension size (3072) when running w4a8_dynamic quantized qwen3 dense model

## 基本信息

- **编号**: #3109
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3109
- **创建时间**: 2025-09-22T16:07:53Z
- **关闭时间**: 2025-09-22T16:08:22Z
- **更新时间**: 2025-12-25T01:15:53Z
- **提交者**: @Anionex
- **评论数**: 3

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
GCC version: (conda-forge gcc 15.1.0-5) 15.1.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.9.23 (main, Jun  5 2025, 13:23:59)  [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.0.3
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.0.3                   pypi_0    pypi
[conda] torch                     2.7.1                    pypi_0    pypi
[conda] torch-npu                 2.7.1.dev20250724          pypi_0    pypi
[conda] torchvision               0.22.1                   pypi_0    pypi
[conda] transformers              4.55.0.dev0              pypi_0    pypi
vLLM Version: 0.10.2rc3.dev321+g65a5910ce (git sha: 65a5910ce)
vLLM Ascend Version: 0.10.2rc2.dev38+g7996325 (git sha: 7996325)

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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64::/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 104.4       48                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
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

when running w4a8_dynamic quantized qwen3 dense model, there will be RuntimeError: start (0) + length (6144) exceeds dimension size (3072) error

```
(EngineCore_DP0 pid=158158) INFO 09-22 23:59:04 [core.py:77] Initializing a V1 LLM engine (v0.10.2rc3.dev321+g65a5910ce) with config: model='./models/Qwen3-1.7B-quantized', speculative_config=None, tokenizer='./models/Qwen3-1.7B-quantized', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=./models/Qwen3-1.7B-quantized, enable_prefix_caching=True, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified_ascend_attention_with_output","vllm.mla_forward"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[168,160,152,144,136,120,112,104,96,88,80,64,56,48,40,32,24,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":168,"local_cache_dir":null}
(EngineCore_DP0 pid=158158) INFO 09-22 23:59:04 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 09-22 23:59:17 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-22 23:59:17 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-22 23:59:17 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-22 23:59:17 [__init__.py:207] Platform plugin ascend is activated
/root/miniconda3/envs/infer/lib/python3.9/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
WARNING 09-22 23:59:20 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(EngineCore_DP0 pid=158158) INFO 09-22 23:59:23 [parallel_state.py:1206] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=158158) INFO 09-22 23:59:23 [model_runner_v1.py:2593] Starting to load model ./models/Qwen3-1.7B-quantized...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/executor/uniproc_executor.py", line 55, in _init_executor
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self.collective_rpc("load_model")
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/utils/__init__.py", line 3010, in run_method
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     return func(*args, **kwargs)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 268, in load_model
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self.model_runner.load_model()
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2596, in load_model
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/base_loader.py", line 50, in load_model
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     self.load_weights(model, model_config)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/default_loader.py", line 264, in load_weights
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     loaded_weights = model.load_weights(
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/models/qwen3.py", line 341, in load_weights
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     return loader.load_weights(weights)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 291, in load_weights
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     autoloaded_weights = set(self._load_module("", self.module, weights))
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 249, in _load_module
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     yield from self._load_module(prefix,
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 222, in _load_module
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     loaded_params = module_load_weights(weights)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/models/qwen2.py", line 428, in load_weights
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     weight_loader(param, loaded_weight, shard_id)
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]   File "/root/autodl-tmp/vllm/vllm/model_executor/layers/linear.py", line 738, in weight_loader
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708]     loaded_weight = loaded_weight.narrow(output_dim, start_idx,
(EngineCore_DP0 pid=158158) ERROR 09-22 23:59:24 [core.py:708] RuntimeError: start (0) + length (6144) exceeds dimension size (3072).
(EngineCore_DP0 pid=158158) Process EngineCore_DP0:
(EngineCore_DP0 pid=158158) Traceback (most recent call last):
(EngineCore_DP0 pid=158158)   File "/root/miniconda3/envs/infer/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
(EngineCore_DP0 pid=158158)     self.run()
(EngineCore_DP0 pid=158158)   File "/root/miniconda3/envs/infer/lib/python3.9/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=158158)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=158158)     raise e
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=158158)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=158158)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=158158)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=158158)     self._init_executor()
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/executor/uniproc_executor.py", line 55, in _init_executor
(EngineCore_DP0 pid=158158)     self.collective_rpc("load_model")
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=158158)     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/utils/__init__.py", line 3010, in run_method
(EngineCore_DP0 pid=158158)     return func(*args, **kwargs)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 268, in load_model
(EngineCore_DP0 pid=158158)     self.model_runner.load_model()
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2596, in load_model
(EngineCore_DP0 pid=158158)     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(EngineCore_DP0 pid=158158)     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/base_loader.py", line 50, in load_model
(EngineCore_DP0 pid=158158)     self.load_weights(model, model_config)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/model_loader/default_loader.py", line 264, in load_weights
(EngineCore_DP0 pid=158158)     loaded_weights = model.load_weights(
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/models/qwen3.py", line 341, in load_weights
(EngineCore_DP0 pid=158158)     return loader.load_weights(weights)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 291, in load_weights
(EngineCore_DP0 pid=158158)     autoloaded_weights = set(self._load_module("", self.module, weights))
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 249, in _load_module
(EngineCore_DP0 pid=158158)     yield from self._load_module(prefix,
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/models/utils.py", line 222, in _load_module
(EngineCore_DP0 pid=158158)     loaded_params = module_load_weights(weights)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/models/qwen2.py", line 428, in load_weights
(EngineCore_DP0 pid=158158)     weight_loader(param, loaded_weight, shard_id)
(EngineCore_DP0 pid=158158)   File "/root/autodl-tmp/vllm/vllm/model_executor/layers/linear.py", line 738, in weight_loader
(EngineCore_DP0 pid=158158)     loaded_weight = loaded_weight.narrow(output_dim, start_idx,
(EngineCore_DP0 pid=158158) RuntimeError: start (0) + length (6144) exceeds dimension size (3072).
```
