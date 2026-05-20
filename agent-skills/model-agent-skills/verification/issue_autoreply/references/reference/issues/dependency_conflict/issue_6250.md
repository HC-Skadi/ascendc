# Issue #6250: [Bug]: The model of qwen-next didn't work in the version of 0.13.rc2 and the error as below

## 基本信息

- **编号**: #6250
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6250
- **创建时间**: 2026-01-26T03:49:17Z
- **关闭时间**: 2026-01-26T11:26:13Z
- **更新时间**: 2026-01-26T11:26:13Z
- **提交者**: @perrypeng-peng
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

# The env is 
** hardware:**
800I A2
**os**
openeuler2203
**the mode is**
Qwen3-Next-80B-A3B-Instruct


# The error output of command
<details>
<summary> `vllm serve /opt/data/Qwen3-Next-80B-A3B-Instruct  --host 0.0.0.0 --port 1035   --tensor-parallel-size 4   --max-model-len 32768  --served-model-name qwen3-next-80b --gpu-memory-utilization 0.8 --max-num-batched-tokens 4096` </summary>

```text
INFO 01-26 02:10:47 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:10:47 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:10:47 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:10:47 [__init__.py:217] Platform plugin ascend is activated
INFO 01-26 02:10:53 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [api_server.py:1351] vLLM API server version 0.13.0
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [utils.py:253] non-default args: {'model_tag': '/opt/data/Qwen3-Next-80B-A3B-Instruct', 'host': '0.0.0.0', 'port': 1035, 'model': '/opt/data/Qwen3-Next-80B-A3B-Instruct', 'max_model_len': 32768, 'served_model_name': ['qwen3-next-80b'], 'tensor_parallel_size': 4, 'gpu_memory_utilization': 0.8, 'max_num_batched_tokens': 4096, 'compilation_config': {'level': None, 'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'vllm_ascend.compilation.compiler_interface.AscendCompiler', 'custom_ops': [], 'splitting_ops': None, 'compile_mm_encoder': False, 'compile_sizes': None, 'compile_ranges_split_points': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': None, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False}, 'local_cache_dir': None}}
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [model.py:514] Resolved architecture: Qwen3NextForCausalLM
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [model.py:1661] Using max model len 32768
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [scheduler.py:230] Chunked prefill is enabled with max_num_batched_tokens=4096.
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [config.py:312] Disabling cascade attention since it is not supported for hybrid models.
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:463] Parameter '--disable-cascade-attn' is a GPU-specific feature. Resetting to False for Ascend.
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [ascend_config.py:55] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
[0;36m(APIServer pid=1105)[0;0m INFO 01-26 02:10:54 [platform.py:279] FULL_DECODE_ONLY compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296] [91m
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             **********************************************************************************
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * WARNING: You have enabled the *full graph* feature.
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * This is an early experimental stage and may involve various unknown issues.
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * A known problem is that capturing too many batch sizes can lead to OOM
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * (Out of Memory) errors or inference hangs. If you encounter such issues,
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * consider reducing `gpu_memory_utilization` or manually specifying a smaller
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * batch size for graph capture.
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * For more details, please refer to:
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             * https://docs.vllm.ai/en/stable/configuration/conserving_memory.html#reduce-cuda-graphs
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             **********************************************************************************[0m
[0;36m(APIServer pid=1105)[0;0m WARNING 01-26 02:10:54 [platform.py:296]             
INFO 01-26 02:11:01 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:11:01 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:11:01 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:11:01 [__init__.py:217] Platform plugin ascend is activated
[0;36m(EngineCore_DP0 pid=1189)[0;0m INFO 01-26 02:11:07 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
[0;36m(EngineCore_DP0 pid=1189)[0;0m INFO 01-26 02:11:07 [core.py:93] Initializing a V1 LLM engine (v0.13.0) with config: model='/opt/data/Qwen3-Next-80B-A3B-Instruct', speculative_config=None, tokenizer='/opt/data/Qwen3-Next-80B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False), seed=0, served_model_name=qwen3-next-80b, enable_prefix_caching=False, enable_chunked_prefill=True, pooler_config=None, compilation_config={'level': None, 'mode': <CompilationMode.VLLM_COMPILE: 3>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'vllm_ascend.compilation.compiler_interface.AscendCompiler', 'custom_ops': ['all'], 'splitting_ops': [], 'compile_mm_encoder': False, 'compile_sizes': [], 'compile_ranges_split_points': [4096], 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': True, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'eliminate_noops': True, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_cudagraph_capture_size': 256, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False}, 'local_cache_dir': None}
INFO 01-26 02:11:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:11:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:11:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:11:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:11:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:11:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:11:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:11:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:11:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:11:14 [__init__.py:217] Platform plugin ascend is activated
INFO 01-26 02:11:14 [__init__.py:217] Platform plugin ascend is activated
INFO 01-26 02:11:14 [__init__.py:217] Platform plugin ascend is activated
INFO 01-26 02:11:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 01-26 02:11:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 01-26 02:11:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 01-26 02:11:14 [__init__.py:217] Platform plugin ascend is activated
INFO 01-26 02:11:21 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 01-26 02:11:21 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 01-26 02:11:21 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 01-26 02:11:21 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 01-26 02:11:24 [ascend_config.py:55] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
INFO 01-26 02:11:24 [parallel_state.py:1203] world_size=4 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:38195 backend=hccl
INFO 01-26 02:11:24 [ascend_config.py:55] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
INFO 01-26 02:11:24 [ascend_config.py:55] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
INFO 01-26 02:11:24 [ascend_config.py:55] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
INFO 01-26 02:11:24 [parallel_state.py:1203] world_size=4 rank=2 local_rank=2 distributed_init_method=tcp://127.0.0.1:38195 backend=hccl
INFO 01-26 02:11:24 [parallel_state.py:1203] world_size=4 rank=1 local_rank=1 distributed_init_method=tcp://127.0.0.1:38195 backend=hccl
INFO 01-26 02:11:24 [parallel_state.py:1203] world_size=4 rank=3 local_rank=3 distributed_init_method=tcp://127.0.0.1:38195 backend=hccl

[log_err.log](https://github.com/user-attachments/files/24852405/log_err.log)

[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 2 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 1 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 0 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 3 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
INFO 01-26 02:11:25 [parallel_state.py:1411] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 1, EP rank 1
INFO 01-26 02:11:25 [parallel_state.py:1411] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 2, EP rank 2
INFO 01-26 02:11:25 [parallel_state.py:1411] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0
INFO 01-26 02:11:25 [parallel_state.py:1411] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 3, EP rank 3
[Gloo] Rank 0 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 1 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 3 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[Gloo] Rank 2 is connected to 3 peer ranks. Expected number of connected peer ranks is : 3
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:11:25 [model_runner_v1.py:2369] Starting to load model /opt/data/Qwen3-Next-80B-A3B-Instruct...
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:11:25 [model_runner_v1.py:2369] Starting to load model /opt/data/Qwen3-Next-80B-A3B-Instruct...
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:11:25 [model_runner_v1.py:2369] Starting to load model /opt/data/Qwen3-Next-80B-A3B-Instruct...
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:11:25 [model_runner_v1.py:2369] Starting to load model /opt/data/Qwen3-Next-80B-A3B-Instruct...
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:11:25 [layer.py:365] Disabling MoE shared_experts cuda stream
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:11:25 [layer.py:365] Disabling MoE shared_experts cuda stream
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:11:25 [layer.py:365] Disabling MoE shared_experts cuda stream
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:11:25 [layer.py:365] Disabling MoE shared_experts cuda stream
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:11:26 [compilation.py:862] Using OOT custom backend for compilation.
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:11:26 [compilation.py:862] Using OOT custom backend for compilation.
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:11:26 [compilation.py:862] Using OOT custom backend for compilation.
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:11:26 [compilation.py:862] Using OOT custom backend for compilation.
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:12:15 [fused_moe.py:499] SharedFusedMoE shared experts split computation matches the integrated computation.
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:12:15 [default_loader.py:308] Loading weights took 48.58 seconds
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:12:16 [model_runner_v1.py:2386] Loading model weights took 37.3242 GB
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:12:16 [fused_moe.py:499] SharedFusedMoE shared experts split computation matches the integrated computation.
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:12:16 [fused_moe.py:499] SharedFusedMoE shared experts split computation matches the integrated computation.
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:12:16 [model_runner_v1.py:2386] Loading model weights took 37.3242 GB
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:12:17 [model_runner_v1.py:2386] Loading model weights took 37.3242 GB
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:12:18 [fused_moe.py:499] SharedFusedMoE shared experts split computation matches the integrated computation.
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:12:18 [model_runner_v1.py:2386] Loading model weights took 37.3242 GB
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:12:32 [backends.py:643] Using cache directory: /root/.cache/vllm/torch_compile_cache/7ec8cb36c9/rank_0_0/backbone for vLLM's torch.compile
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:12:32 [backends.py:703] Dynamo bytecode transform time: 13.08 s
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:13:07 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 28.42 s
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:13:07 [monitor.py:34] torch.compile takes 41.50 s in total
[0;36m(Worker_TP0 pid=1284)[0;0m INFO 01-26 02:13:10 [worker.py:302] Available memory: 9786143744, total memory: 65452113920
[0;36m(Worker_TP1 pid=1285)[0;0m INFO 01-26 02:13:10 [worker.py:302] Available memory: 10023158784, total memory: 65452113920
[0;36m(Worker_TP3 pid=1287)[0;0m INFO 01-26 02:13:10 [worker.py:302] Available memory: 10022433792, total memory: 65452113920
[0;36m(Worker_TP2 pid=1286)[0;0m INFO 01-26 02:13:10 [worker.py:302] Available memory: 10023117824, total memory: 65452113920
[0;36m(EngineCore_DP0 pid=1189)[0;0m INFO 01-26 02:13:10 [kv_cache_utils.py:1291] GPU KV cache size: 198,912 tokens
[0;36m(EngineCore_DP0 pid=1189)[0;0m INFO 01-26 02:13:10 [kv_cache_utils.py:1296] Maximum concurrency for 32,768 tokens per request: 23.29x
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824] WorkerProc hit an exception.
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824] Traceback (most recent call last):
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3105, in _torch_cuda_wrapper
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     yield
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3051, in capture_model
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     GPUModelRunner.capture_model(self)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4563, in capture_model
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     self._capture_cudagraphs(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4641, in _capture_cudagraphs
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     self._dummy_run(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2293, in _dummy_run
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     hidden_states = self._generate_dummy_run_hidden_states(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2061, in _generate_dummy_run_hidden_states
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     hidden_states = self.model(input_ids=input_ids,
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 113, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self.runnable(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1231, in forward
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     hidden_states = self.model(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]                     ^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 439, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 223, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self._call_with_optional_nvtx_range(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 109, in _call_with_optional_nvtx_range
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return callable_fn(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 997, in forward
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     def forward(
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return fn(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/caching.py", line 54, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self.optimized_call(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     raise e
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]   File "<eval_with_key>.10", line 346, in forward
[0;36m(Worker_TP3 pid=1287)[0;0m ERROR 01-26 02:13:22 [multiproc_executor.py:824]     submod_0 = self.submod_0(l_input_ids_, s72, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_linear_attn_modules_in_proj_qkvz_parameters_weight_, l_self_modules_layers_modules_0_modules_linear_attn_modules_in_proj_ba_parameters_weight_, l_self_modules_layers_modules_0_modules_linear_attn_modules_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_linear_attn_modules_out_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, 


.......



```

</details>

## log detail as attachment

[log_err.log](https://github.com/user-attachments/files/24852443/log_err.log)

### 🐛 Describe the bug

```
 vllm serve /opt/data/Qwen3-Next-80B-A3B-Instruct  --host 0.0.0.0 --port 1035   --tensor-parallel-size 4   --max-model-len 32768  --served-model-name qwen3-next-80b --gpu-memory-utilization 0.8 --max-num-batched-tokens 4096
```



