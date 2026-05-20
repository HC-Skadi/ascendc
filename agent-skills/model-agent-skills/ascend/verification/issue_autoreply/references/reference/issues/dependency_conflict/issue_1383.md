# Issue #1383: [Bug]: [v0.9.1rc1] Use 310P3 Not Start. [Log] Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.

## 基本信息

- **编号**: #1383
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1383
- **创建时间**: 2025-06-24T01:20:48Z
- **关闭时间**: 2025-06-24T07:50:03Z
- **更新时间**: 2025-06-24T07:50:03Z
- **提交者**: @LwengGitHub
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

Use 310P3 Not Start.

[Log] 
Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.[tbe-custom]:op type TransData is not found in this op store.[Dynamic shape check]: The format and dtype is not precisely equivalent to format and dtype in op information library[Static shape check]:The format and dtype is not precisely equivalent to format and dtype in op information library.


### 🐛 Describe the bug

LogInfo:
[root@74dae9b20914 workspace]# export VLLM_USE_MODELSCOPE=true
[root@74dae9b20914 workspace]# vllm serve Qwen/Qwen2.5-0.5B-Instruct &
[1] 332
[root@74dae9b20914 workspace]# INFO 06-23 10:49:40 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 10:49:40 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 10:49:42 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 10:49:42 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 10:49:42 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 10:49:43 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 10:49:46 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 06-23 10:49:51 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-23 10:49:51 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-23 10:49:51 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-23 10:49:51 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-23 10:49:51 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-23 10:49:51 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-23 10:49:53 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:49:54 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:49:55 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:49:57 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:49:57 [api_server.py:1287] vLLM API server version 0.9.1
INFO 06-23 10:49:59 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:49:59 [cli_args.py:309] non-default args: {'model': 'Qwen/Qwen2.5-0.5B-Instruct'}
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:50:00,000 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:50:00,560 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 06-23 10:50:17 [config.py:823] This model supports multiple tasks: {'embed', 'classify', 'reward', 'generate', 'score'}. Defaulting to 'generate'.
INFO 06-23 10:50:27 [arg_utils.py:1653] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
INFO 06-23 10:50:27 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 10:50:27 [platform.py:164] Compilation disabled, using eager mode by default
INFO 06-23 10:50:27 [api_server.py:265] Started engine process with PID 603
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:50:28,515 - modelscope - INFO - Target directory already exists, skipping creation.
WARNING 06-23 10:50:32 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-23 10:50:33 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 10:50:33 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 10:50:35 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 10:50:35 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 10:50:35 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 10:50:35 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 10:50:39 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 06-23 10:50:43 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-23 10:50:43 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-23 10:50:43 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-23 10:50:43 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-23 10:50:43 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-23 10:50:43 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-23 10:50:43 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":256,"local_cache_dir":null}, use_cached_outputs=True, 
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:50:43,691 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:50:44,795 - modelscope - INFO - Target directory already exists, skipping creation.
WARNING 06-23 10:50:44 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd607e5180>
WARNING 06-23 10:50:52 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-23 10:50:54 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 10:50:54 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 10:50:56 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 10:50:56 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 10:50:56 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 10:50:56 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 10:50:59 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 06-23 10:51:03 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 06-23 10:51:03 [model_runner.py:995] Starting to load model Qwen/Qwen2.5-0.5B-Instruct...
..Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-06-23 10:51:40,443 - modelscope - INFO - Target directory already exists, skipping creation.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.73it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  5.72it/s]

INFO 06-23 10:51:40 [default_loader.py:272] Loading weights took 0.21 seconds
INFO 06-23 10:51:41 [model_runner.py:1000] Loading model weights took 0.9278 GB
..ERROR 06-23 10:51:59 [engine.py:458] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Identity.
ERROR 06-23 10:51:59 [engine.py:458] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-23 10:51:59 [engine.py:458] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 06-23 10:51:59 [engine.py:458] [ERROR] 2025-06-23-10:51:59 (PID:603, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 06-23 10:51:59 [engine.py:458] EZ3002: [PID: 603] 2025-06-23-10:51:59.636.525 Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.[tbe-custom]:op type TransData is not found in this op store.[Dynamic shape check]: The format and dtype is not precisely equivalent to format and dtype in op information library[Static shape check]:The format and dtype is not precisely equivalent to format and dtype in op information library.
ERROR 06-23 10:51:59 [engine.py:458]         Possible Cause: The operator type is unsupported in the operator information library due to specification mismatch.
ERROR 06-23 10:51:59 [engine.py:458]         Solution: Submit an issue to request for support at https://gitee.com/ascend, or remove this type of operators from your model.
ERROR 06-23 10:51:59 [engine.py:458]         TraceBack (most recent call last):
ERROR 06-23 10:51:59 [engine.py:458]         Optype [TransData] of Ops kernel [aicpu_ascend_kernel] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
ERROR 06-23 10:51:59 [engine.py:458]         No supported Ops kernel and engine are found for [trans_TransData_6], optype [TransData].
ERROR 06-23 10:51:59 [engine.py:458]         Assert ((SelectEngine(node_ptr, exclude_engines, is_check_support_success, op_info)) == ge::SUCCESS) failed[FUNC:operator()][FILE:engine_place.cc][LINE:148]
ERROR 06-23 10:51:59 [engine.py:458]         RunAllSubgraphs failed, graph=online.[FUNC:RunAllSubgraphs][FILE:engine_place.cc][LINE:122]
ERROR 06-23 10:51:59 [engine.py:458]         build graph failed, graph id:15, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1623]
ERROR 06-23 10:51:59 [engine.py:458]         [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 06-23 10:51:59 [engine.py:458]         [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 06-23 10:51:59 [engine.py:458]         build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 06-23 10:51:59 [engine.py:458] Traceback (most recent call last):
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine
ERROR 06-23 10:51:59 [engine.py:458]     engine = MQLLMEngine.from_vllm_config(
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config
ERROR 06-23 10:51:59 [engine.py:458]     return cls(
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__
ERROR 06-23 10:51:59 [engine.py:458]     self.engine = LLMEngine(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 268, in __init__
ERROR 06-23 10:51:59 [engine.py:458]     self._initialize_kv_caches()
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 413, in _initialize_kv_caches
ERROR 06-23 10:51:59 [engine.py:458]     self.model_executor.determine_num_available_blocks())
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 104, in determine_num_available_blocks
ERROR 06-23 10:51:59 [engine.py:458]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 06-23 10:51:59 [engine.py:458]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
ERROR 06-23 10:51:59 [engine.py:458]     return func(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-23 10:51:59 [engine.py:458]     return func(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 288, in determine_num_available_blocks
ERROR 06-23 10:51:59 [engine.py:458]     self.model_runner.profile_run()
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-23 10:51:59 [engine.py:458]     return func(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1205, in profile_run
ERROR 06-23 10:51:59 [engine.py:458]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-23 10:51:59 [engine.py:458]     return func(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1441, in execute_model
ERROR 06-23 10:51:59 [engine.py:458]     hidden_or_intermediate_states = model_executable(
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return self._call_impl(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return forward_call(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 477, in forward
ERROR 06-23 10:51:59 [engine.py:458]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 173, in __call__
ERROR 06-23 10:51:59 [engine.py:458]     return self.forward(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 354, in forward
ERROR 06-23 10:51:59 [engine.py:458]     hidden_states, residual = layer(
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return self._call_impl(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return forward_call(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 253, in forward
ERROR 06-23 10:51:59 [engine.py:458]     hidden_states = self.self_attn(
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return self._call_impl(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return forward_call(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 182, in forward
ERROR 06-23 10:51:59 [engine.py:458]     q, k = self.rotary_emb(positions, q, k)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return self._call_impl(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-23 10:51:59 [engine.py:458]     return forward_call(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 24, in forward
ERROR 06-23 10:51:59 [engine.py:458]     return self._forward_method(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 69, in rope_forward_oot
ERROR 06-23 10:51:59 [engine.py:458]     torch_npu._npu_rotary_embedding(
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 72, in wrapper
ERROR 06-23 10:51:59 [engine.py:458]     return api_func(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 80, in generated_function
ERROR 06-23 10:51:59 [engine.py:458]     return getattr(torch.ops.atb, api_name)(*args, **kwargs)
ERROR 06-23 10:51:59 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 06-23 10:51:59 [engine.py:458]     return self._op(*args, **(kwargs or {}))
ERROR 06-23 10:51:59 [engine.py:458] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Identity.
ERROR 06-23 10:51:59 [engine.py:458] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-23 10:51:59 [engine.py:458] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 06-23 10:51:59 [engine.py:458] [ERROR] 2025-06-23-10:51:59 (PID:603, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 06-23 10:51:59 [engine.py:458] EZ3002: [PID: 603] 2025-06-23-10:51:59.636.525 Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.[tbe-custom]:op type TransData is not found in this op store.[Dynamic shape check]: The format and dtype is not precisely equivalent to format and dtype in op information library[Static shape check]:The format and dtype is not precisely equivalent to format and dtype in op information library.
ERROR 06-23 10:51:59 [engine.py:458]         Possible Cause: The operator type is unsupported in the operator information library due to specification mismatch.
ERROR 06-23 10:51:59 [engine.py:458]         Solution: Submit an issue to request for support at https://gitee.com/ascend, or remove this type of operators from your model.
ERROR 06-23 10:51:59 [engine.py:458]         TraceBack (most recent call last):
ERROR 06-23 10:51:59 [engine.py:458]         Optype [TransData] of Ops kernel [aicpu_ascend_kernel] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
ERROR 06-23 10:51:59 [engine.py:458]         No supported Ops kernel and engine are found for [trans_TransData_6], optype [TransData].
ERROR 06-23 10:51:59 [engine.py:458]         Assert ((SelectEngine(node_ptr, exclude_engines, is_check_support_success, op_info)) == ge::SUCCESS) failed[FUNC:operator()][FILE:engine_place.cc][LINE:148]
ERROR 06-23 10:51:59 [engine.py:458]         RunAllSubgraphs failed, graph=online.[FUNC:RunAllSubgraphs][FILE:engine_place.cc][LINE:122]
ERROR 06-23 10:51:59 [engine.py:458]         build graph failed, graph id:15, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1623]
ERROR 06-23 10:51:59 [engine.py:458]         [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 06-23 10:51:59 [engine.py:458]         [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 06-23 10:51:59 [engine.py:458]         build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 06-23 10:51:59 [engine.py:458] 
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 460, in run_mp_engine
    raise e from None
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 268, in __init__
    self._initialize_kv_caches()
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 413, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 104, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 288, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1205, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1441, in execute_model
    hidden_or_intermediate_states = model_executable(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 477, in forward
    hidden_states = self.model(input_ids, positions, intermediate_tensors,
  File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 173, in __call__
    return self.forward(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 354, in forward
    hidden_states, residual = layer(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 253, in forward
    hidden_states = self.self_attn(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 182, in forward
    q, k = self.rotary_emb(positions, q, k)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 24, in forward
    return self._forward_method(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 69, in rope_forward_oot
    torch_npu._npu_rotary_embedding(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 72, in wrapper
    return api_func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 80, in generated_function
    return getattr(torch.ops.atb, api_name)(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Identity.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2025-06-23-10:51:59 (PID:603, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
EZ3002: [PID: 603] 2025-06-23-10:51:59.636.525 Optype [TransData] of Ops kernel [AIcoreEngine] is unsupported. Reason: [tbe-custom]:op type TransData is not found in this op store.[tbe-custom]:op type TransData is not found in this op store.[Dynamic shape check]: The format and dtype is not precisely equivalent to format and dtype in op information library[Static shape check]:The format and dtype is not precisely equivalent to format and dtype in op information library.
        Possible Cause: The operator type is unsupported in the operator information library due to specification mismatch.
        Solution: Submit an issue to request for support at https://gitee.com/ascend, or remove this type of operators from your model.
        TraceBack (most recent call last):
        Optype [TransData] of Ops kernel [aicpu_ascend_kernel] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
        No supported Ops kernel and engine are found for [trans_TransData_6], optype [TransData].
        Assert ((SelectEngine(node_ptr, exclude_engines, is_check_support_success, op_info)) == ge::SUCCESS) failed[FUNC:operator()][FILE:engine_place.cc][LINE:148]
        RunAllSubgraphs failed, graph=online.[FUNC:RunAllSubgraphs][FILE:engine_place.cc][LINE:122]
        build graph failed, graph id:15, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1623]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 59, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 58, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1323, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1343, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 155, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 288, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-06-23-10:52:09 (PID:332, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

