# Issue #2146: [Bug]: v0.9.2rc2, Qwen3-235B-A22B-Thinking-2507, with mindie_turbo, deploy failed

## 基本信息

- **编号**: #2146
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2146
- **创建时间**: 2025-07-31T12:06:24Z
- **关闭时间**: 2025-10-15T02:31:22Z
- **更新时间**: 2025-10-15T02:31:22Z
- **提交者**: @15626471095
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

command:
```
vllm serve /share/model/Qwen/Qwen3-235B-A22B-Thinking-2507 --served-model-name Qwen3-235B-A22B-Thinking-2507 \
-tp 16 --trust-remote-code --host 0.0.0.0 --port 8086 --gpu-memory-utilization 0.95 \
--max-model-len 32768 --max-num-seqs 256 --block-size 128 \
--distributed_executor_backend "ray" --enforce-eager \
--enable-auto-tool-choice --tool-call-parser hermes' --reasoning-parser deepseek_r1
```

### 🐛 Describe the bug

INFO 07-31 19:34:26 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-31 19:34:26 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-31 19:34:26 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-31 19:34:26 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-31 19:34:27 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-31 19:34:31 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-31 19:34:31 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-31 19:34:33 [api_server.py:1395] vLLM API server version 0.9.2
INFO 07-31 19:34:33 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'port': 8086, 'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'model': '/share/model/Qwen/Qwen3-235B-A22B-Thinking-2507', 'trust_remote_code': True, 'max_model_len': 32768, 'enforce_eager': True, 'served_model_name': ['Qwen3-235B-A22B-Thinking-2507'], 'distributed_executor_backend': 'ray', 'tensor_parallel_size': 16, 'block_size': 128, 'gpu_memory_utilization': 0.95, 'max_num_seqs': 256}
INFO 07-31 19:34:46 [config.py:841] This model supports multiple tasks: {'reward', 'classify', 'generate', 'embed'}. Defaulting to 'generate'.
INFO 07-31 19:34:46 [config.py:1472] Using max model len 32768
INFO 07-31 19:34:46 [config.py:2285] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 07-31 19:34:46 [platform.py:161] Compilation disabled, using eager mode by default
INFO 07-31 19:34:54 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-31 19:34:54 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-31 19:34:54 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-31 19:34:54 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-31 19:34:55 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-31 19:34:58 [core.py:526] Waiting for init message from front-end.
INFO 07-31 19:34:59 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-31 19:35:00 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-31 19:35:00 [core.py:69] Initializing a V1 LLM engine (v0.9.2) with config: model='/share/model/Qwen/Qwen3-235B-A22B-Thinking-2507', speculative_config=None, tokenizer='/share/model/Qwen/Qwen3-235B-A22B-Thinking-2507', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen3-235B-A22B-Thinking-2507, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}
2025-07-31 19:35:00,009	INFO worker.py:1723 -- Connecting to existing Ray cluster at address: 7.242.101.23:6379...
2025-07-31 19:35:00,021	INFO worker.py:1917 -- Connected to Ray cluster.
INFO 07-31 19:35:06 [ray_utils.py:334] No current placement group found. Creating a new placement group.
WARNING 07-31 19:35:06 [ray_utils.py:198] tensor_parallel_size=16 is bigger than a reserved number of NPUs (8 NPUs) in a node 7d4e6ff56db338157a016797ed548e0741af70426fa64317f56ba8cb. Tensor parallel workers can be spread out to 2+ nodes which can degrade the performance unless you have fast interconnect across nodes, like Infiniband. To resolve this issue, make sure you have more than 16 GPUs available at each node.
WARNING 07-31 19:35:06 [ray_utils.py:198] tensor_parallel_size=16 is bigger than a reserved number of NPUs (8 NPUs) in a node 1f8c93cafea1fe875631e2de8f3ebfc6d61aa11d468a4533a92c051f. Tensor parallel workers can be spread out to 2+ nodes which can degrade the performance unless you have fast interconnect across nodes, like Infiniband. To resolve this issue, make sure you have more than 16 GPUs available at each node.
INFO 07-31 19:35:06 [ray_distributed_executor.py:177] use_ray_spmd_worker: True
(pid=13210) INFO 07-31 19:35:13 [__init__.py:39] Available plugins for group vllm.platform_plugins:
(pid=13210) INFO 07-31 19:35:13 [__init__.py:41] - ascend -> vllm_ascend:register
(pid=13210) INFO 07-31 19:35:13 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
(pid=13210) INFO 07-31 19:35:14 [__init__.py:235] Platform plugin ascend is activated
(pid=13210) WARNING 07-31 19:35:15 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-31 19:35:17 [ray_distributed_executor.py:353] non_carry_over_env_vars from config: set()
INFO 07-31 19:35:17 [ray_distributed_executor.py:355] Copying the following environment variables to workers: ['LD_LIBRARY_PATH', 'VLLM_USE_RAY_SPMD_WORKER', 'VLLM_USE_RAY_COMPILED_DAG', 'VLLM_WORKER_MULTIPROC_METHOD', 'VLLM_USE_V1']
INFO 07-31 19:35:17 [ray_distributed_executor.py:358] If certain env vars should NOT be copied to workers, add them to /root/.config/vllm/ray_non_carry_over_env_vars.json file
(RayWorkerWrapper pid=13210) INFO 07-31 19:35:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(pid=776, ip=7.242.96.68) INFO 07-31 19:35:15 [__init__.py:39] Available plugins for group vllm.platform_plugins: [repeated 15x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=776, ip=7.242.96.68) INFO 07-31 19:35:15 [__init__.py:41] - ascend -> vllm_ascend:register [repeated 15x across cluster]
(pid=776, ip=7.242.96.68) INFO 07-31 19:35:15 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. [repeated 15x across cluster]
(pid=776, ip=7.242.96.68) INFO 07-31 19:35:15 [__init__.py:235] Platform plugin ascend is activated [repeated 15x across cluster]
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(RayWorkerWrapper pid=13210) WARNING 07-31 19:35:19 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(RayWorkerWrapper pid=13210) INFO 07-31 19:35:21 [utils.py:212] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
(pid=776, ip=7.242.96.68) WARNING 07-31 19:35:17 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") [repeated 15x across cluster]
(RayWorkerWrapper pid=13210) INFO 07-31 19:35:31 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_c68f5af8'), local_subscribe_addr='ipc:///tmp/6ea66a59-708a-49fe-bfe0-38a84a9b1ce7', remote_subscribe_addr='tcp://7.242.101.23:60229', remote_addr_ipv6=False)
(RayWorkerWrapper pid=13214) INFO 07-31 19:35:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 15x across cluster]
(RayWorkerWrapper pid=13214) WARNING 07-31 19:35:20 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP. [repeated 15x across cluster]
(RayWorkerWrapper pid=13214) WARNING 07-31 19:35:20 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM. [repeated 75x across cluster]
(RayWorkerWrapper pid=776, ip=7.242.96.68) INFO 07-31 19:35:22 [utils.py:212] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo. [repeated 15x across cluster]
(RayWorkerWrapper pid=13210) INFO 07-31 19:35:31 [parallel_state.py:1076] rank 0 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(RayWorkerWrapper pid=769, ip=7.242.96.68) INFO 07-31 19:35:33 [model_runner_v1.py:1745] Starting to load model /share/model/Qwen/Qwen3-235B-A22B-Thinking-2507...
ERROR 07-31 19:35:35 [core.py:586] EngineCore failed to start.
ERROR 07-31 19:35:35 [core.py:586] Traceback (most recent call last):
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 07-31 19:35:35 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
ERROR 07-31 19:35:35 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 75, in __init__
ERROR 07-31 19:35:35 [core.py:586]     self.model_executor = executor_class(vllm_config)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 287, in __init__
ERROR 07-31 19:35:35 [core.py:586]     super().__init__(*args, **kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
ERROR 07-31 19:35:35 [core.py:586]     self._init_executor()
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
ERROR 07-31 19:35:35 [core.py:586]     self._init_workers_ray(placement_group)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
ERROR 07-31 19:35:35 [core.py:586]     self._run_workers("load_model",
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 522, in _run_workers
ERROR 07-31 19:35:35 [core.py:586]     ray_worker_outputs = ray.get(ray_worker_outputs)
ERROR 07-31 19:35:35 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
ERROR 07-31 19:35:35 [core.py:586]     return fn(*args, **kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
ERROR 07-31 19:35:35 [core.py:586]     return func(*args, **kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
ERROR 07-31 19:35:35 [core.py:586]     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
ERROR 07-31 19:35:35 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
ERROR 07-31 19:35:35 [core.py:586]     raise value.as_instanceof_cause()
ERROR 07-31 19:35:35 [core.py:586] ray.exceptions.RayTaskError(TypeError): ray::RayWorkerWrapper.execute_method() (pid=13215, ip=7.242.101.23, actor_id=02a815d7708e6d7233293c3f01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xffcfc468d5a0>)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 623, in execute_method
ERROR 07-31 19:35:35 [core.py:586]     raise e
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 614, in execute_method
ERROR 07-31 19:35:35 [core.py:586]     return run_method(self, method, args, kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method
ERROR 07-31 19:35:35 [core.py:586]     return func(*args, **kwargs)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 240, in load_model
ERROR 07-31 19:35:35 [core.py:586]     self.model_runner.load_model()
ERROR 07-31 19:35:35 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
ERROR 07-31 19:35:35 [core.py:586]     func(self)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1748, in load_model
ERROR 07-31 19:35:35 [core.py:586]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
ERROR 07-31 19:35:35 [core.py:586]     return loader.load_model(vllm_config=vllm_config,
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 41, in load_model
ERROR 07-31 19:35:35 [core.py:586]     self.load_weights(model, model_config)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 269, in load_weights
ERROR 07-31 19:35:35 [core.py:586]     loaded_weights = model.load_weights(
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 541, in load_weights
ERROR 07-31 19:35:35 [core.py:586]     return loader.load_weights(weights)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 291, in load_weights
ERROR 07-31 19:35:35 [core.py:586]     autoloaded_weights = set(self._load_module("", self.module, weights))
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 240, in _load_module
ERROR 07-31 19:35:35 [core.py:586]     for child_prefix, child_weights in self._groupby_prefix(weights):
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 129, in _groupby_prefix
ERROR 07-31 19:35:35 [core.py:586]     for prefix, group in itertools.groupby(weights_by_parts,
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 126, in <genexpr>
ERROR 07-31 19:35:35 [core.py:586]     weights_by_parts = ((weight_name.split(".", 1), weight_data)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 288, in <genexpr>
ERROR 07-31 19:35:35 [core.py:586]     weights = ((name, weight) for name, weight in weights
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 251, in get_all_weights
ERROR 07-31 19:35:35 [core.py:586]     yield from self._get_weights_iterator(primary_weights)
ERROR 07-31 19:35:35 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 198, in _get_weights_iterator
ERROR 07-31 19:35:35 [core.py:586]     weights_iterator = safetensors_weights_iterator(
ERROR 07-31 19:35:35 [core.py:586] TypeError: wrapper_weights_iterator.<locals>._safetensors_weights_iterator() takes 1 positional argument but 2 were given
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 590, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 75, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 287, in __init__
    super().__init__(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
    self._init_workers_ray(placement_group)
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
    self._run_workers("load_model",
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 522, in _run_workers
    ray_worker_outputs = ray.get(ray_worker_outputs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
    values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(TypeError): ray::RayWorkerWrapper.execute_method() (pid=13215, ip=7.242.101.23, actor_id=02a815d7708e6d7233293c3f01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xffcfc468d5a0>)
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 623, in execute_method
    raise e
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 614, in execute_method
    return run_method(self, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 240, in load_model
    self.model_runner.load_model()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
    func(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1748, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
    return loader.load_model(vllm_config=vllm_config,
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 41, in load_model
    self.load_weights(model, model_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 269, in load_weights
    loaded_weights = model.load_weights(
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 541, in load_weights
    return loader.load_weights(weights)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 291, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 240, in _load_module
    for child_prefix, child_weights in self._groupby_prefix(weights):
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 129, in _groupby_prefix
    for prefix, group in itertools.groupby(weights_by_parts,
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 126, in <genexpr>
    weights_by_parts = ((weight_name.split(".", 1), weight_data)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 288, in <genexpr>
    weights = ((name, weight) for name, weight in weights
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 251, in get_all_weights
    yield from self._get_weights_iterator(primary_weights)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 198, in _get_weights_iterator
    weights_iterator = safetensors_weights_iterator(
TypeError: wrapper_weights_iterator.<locals>._safetensors_weights_iterator() takes 1 positional argument but 2 were given
INFO 07-31 19:35:35 [ray_distributed_executor.py:128] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
2025-07-31 19:35:35,770	ERROR worker.py:423 -- Unhandled error (suppress with 'RAY_IGNORE_UNHANDLED_ERRORS=1'): ray::RayWorkerWrapper.execute_method() (pid=13214, ip=7.242.101.23, actor_id=11573371cb1364127fd3f12c01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xffcff00f55a0>)
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 623, in execute_method
    raise e
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 614, in execute_method
    return run_method(self, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 240, in load_model
    self.model_runner.load_model()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
    func(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1748, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
    return loader.load_model(vllm_config=vllm_config,
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 41, in load_model
    self.load_weights(model, model_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 269, in load_weights
    loaded_weights = model.load_weights(
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 541, in load_weights
    return loader.load_weights(weights)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 291, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 240, in _load_module
    for child_prefix, child_weights in self._groupby_prefix(weights):
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 129, in _groupby_prefix
    for prefix, group in itertools.groupby(weights_by_parts,
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 126, in <genexpr>
    weights_by_parts = ((weight_name.split(".", 1), weight_data)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 288, in <genexpr>
    weights = ((name, weight) for name, weight in weights
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 251, in get_all_weights
    yield from self._get_weights_iterator(primary_weights)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 198, in _get_weights_iterator
    weights_iterator = safetensors_weights_iterator(
TypeError: wrapper_weights_iterator.<locals>._safetensors_weights_iterator() takes 1 positional argument but 2 were given
