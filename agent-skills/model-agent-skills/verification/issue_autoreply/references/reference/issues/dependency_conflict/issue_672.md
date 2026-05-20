# Issue #672: [Bug]: DP+EP混合并行报错 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 15

## 基本信息

- **编号**: #672
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/672
- **创建时间**: 2025-04-27T03:20:37Z
- **关闭时间**: 2025-05-06T07:07:58Z
- **更新时间**: 2025-05-06T07:07:58Z
- **提交者**: @gao12312
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment


The output of `python /vllm-ascend-main/examples/dp_offline/data_parallel.py.py`  
使用DeepSeek-V2-Lite-Chat-w8a8和DeepSeek-V2-Lite-Chat报错


### 🐛 Describe the bug

```text
 bash run_dp.sh 
W0427 03:08:57.144000 540525 site-packages/torch/distributed/run.py:793] 
W0427 03:08:57.144000 540525 site-packages/torch/distributed/run.py:793] *****************************************
W0427 03:08:57.144000 540525 site-packages/torch/distributed/run.py:793] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
W0427 03:08:57.144000 540525 site-packages/torch/distributed/run.py:793] *****************************************
INFO 04-27 03:09:33 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-27 03:09:33 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-27 03:09:33 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-27 03:09:33 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-27 03:09:33 [__init__.py:44] plugin ascend loaded.
INFO 04-27 03:09:33 [__init__.py:230] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 04-27 03:09:33 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-27 03:09:33 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-27 03:09:33 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-27 03:09:33 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-27 03:09:33 [__init__.py:44] plugin ascend loaded.
INFO 04-27 03:09:33 [__init__.py:230] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
DP rank 1 needs to process 8 prompts
INFO 04-27 03:09:36 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-27 03:09:36 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-27 03:09:36 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-27 03:09:36 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-27 03:09:36 [__init__.py:44] plugin ascend_enhanced_model loaded.
INFO 04-27 03:09:36 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
DP rank 0 needs to process 8 prompts
WARNING 04-27 03:09:36 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 04-27 03:09:36 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-27 03:09:36 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-27 03:09:36 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-27 03:09:36 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-27 03:09:36 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-27 03:09:36 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 04-27 03:09:36 [config.py:209] Replacing legacy 'type' key with 'rope_type'
WARNING 04-27 03:09:36 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-27 03:09:36 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-27 03:09:36 [config.py:209] Replacing legacy 'type' key with 'rope_type'
INFO 04-27 03:09:47 [config.py:689] This model supports multiple tasks: {'embed', 'reward', 'generate', 'classify', 'score'}. Defaulting to 'generate'.
WARNING 04-27 03:09:47 [config.py:768] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
WARNING 04-27 03:09:47 [arg_utils.py:1731] --additional-config is not supported by the V1 Engine. Falling back to V0. 
INFO 04-27 03:09:47 [config.py:1747] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 04-27 03:09:47 [config.py:3763] MLA is enabled on a non-GPU platform; forcing chunked prefill and prefix caching to be disabled.
WARNING 04-27 03:09:47 [platform.py:129] NPU compilation support pending. Will be available in future CANN and torch_npu releases. Using default: enforce_eager=True
INFO 04-27 03:09:47 [platform.py:134] Compilation disabled, using eager mode by default
INFO 04-27 03:09:47 [llm_engine.py:243] Initializing a V0 LLM engine (v0.8.4) with config: model='/root/models/DeepSeek-V2-Lite-Chat-w8a8', speculative_config=None, tokenizer='/root/models/DeepSeek-V2-Lite-Chat-w8a8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/root/models/DeepSeek-V2-Lite-Chat-w8a8, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[8,4,2,1],"max_capture_size":8}, use_cached_outputs=False, 
INFO 04-27 03:09:48 [config.py:689] This model supports multiple tasks: {'generate', 'classify', 'reward', 'score', 'embed'}. Defaulting to 'generate'.
WARNING 04-27 03:09:48 [config.py:768] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
WARNING 04-27 03:09:48 [arg_utils.py:1731] --additional-config is not supported by the V1 Engine. Falling back to V0. 
INFO 04-27 03:09:48 [config.py:1747] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 04-27 03:09:48 [config.py:3763] MLA is enabled on a non-GPU platform; forcing chunked prefill and prefix caching to be disabled.
WARNING 04-27 03:09:48 [platform.py:129] NPU compilation support pending. Will be available in future CANN and torch_npu releases. Using default: enforce_eager=True
INFO 04-27 03:09:48 [platform.py:134] Compilation disabled, using eager mode by default
INFO 04-27 03:09:48 [llm_engine.py:243] Initializing a V0 LLM engine (v0.8.4) with config: model='/root/models/DeepSeek-V2-Lite-Chat-w8a8', speculative_config=None, tokenizer='/root/models/DeepSeek-V2-Lite-Chat-w8a8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/root/models/DeepSeek-V2-Lite-Chat-w8a8, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[8,4,2,1],"max_capture_size":8}, use_cached_outputs=False, 
ERROR 04-27 03:09:48 [camem.py:69] Failed to import vllm_ascend_C:libvllm_ascend_kernels.so: cannot open shared object file: No such file or directory
ERROR 04-27 03:09:48 [camem.py:69] Failed to import vllm_ascend_C:libvllm_ascend_kernels.so: cannot open shared object file: No such file or directory
WARNING 04-27 03:09:49 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff855c0a60>
WARNING 04-27 03:09:49 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff5467cc10>
INFO 04-27 03:09:55 [parallel_state.py:838] Adjusting world_size=2 rank=0 distributed_init_method=tcp://127.0.0.1:12345 for DP
INFO 04-27 03:09:55 [parallel_state.py:838] Adjusting world_size=2 rank=1 distributed_init_method=tcp://127.0.0.1:12345 for DP
[rank0]:[W427 03:10:15.652192062 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank1]:[W427 03:10:15.764108557 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
INFO 04-27 03:10:45 [parallel_state.py:959] rank 1 in world size 2 is assigned as DP rank 1, PP rank 0, TP rank 0
INFO 04-27 03:10:45 [parallel_state.py:959] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0
INFO 04-27 03:11:05 [model_runner.py:944] Starting to load model /root/models/DeepSeek-V2-Lite-Chat-w8a8...
INFO 04-27 03:11:05 [model_runner.py:944] Starting to load model /root/models/DeepSeek-V2-Lite-Chat-w8a8...
INFO 04-27 03:11:05 [quantizer.py:88] Using the vLLM Ascend Quantizer version now!
INFO 04-27 03:11:05 [quantizer.py:88] Using the vLLM Ascend Quantizer version now!
[rank0]: Traceback (most recent call last):
[rank0]:   File "/workspace/vllm-ascend-main-0425/examples/dp_offline/data_parallel.py", line 84, in <module>
[rank0]:     main()
[rank0]:   File "/workspace/vllm-ascend-main-0425/examples/dp_offline/data_parallel.py", line 59, in main
[rank0]:     llm = LLM(model="/root/models/DeepSeek-V2-Lite-Chat-w8a8",
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1099, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 248, in __init__
[rank0]:     self.llm_engine = LLMEngine.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 522, in from_engine_args
[rank0]:     return engine_cls.from_vllm_config(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 498, in from_vllm_config
[rank0]:     return cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 282, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
[rank0]:     self.collective_rpc("load_model")
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/worker/worker.py", line 209, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/worker/model_runner.py", line 946, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
[rank0]:     model = _initialize_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 555, in __init__
[rank0]:     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 481, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 483, in <lambda>
[rank0]:     lambda prefix: CustomDeepseekV2DecoderLayer(
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 389, in __init__
[rank0]:     self.mlp = CustomDeepseekV2MoE(
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 104, in __init__
[rank0]:     self.experts = AscendFusedMoE(
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/ops/fused_moe.py", line 593, in __init__
[rank0]:     self.quant_method = quant_config.get_quant_method(self, prefix)
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quant_config.py", line 101, in get_quant_method
[rank0]:     return AscendFusedMoEMethod(self, prefix,
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quant_config.py", line 276, in __init__
[rank0]:     self.quant_method = self.quantizer.build_moe_method()
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quantizer.py", line 281, in build_moe_method
[rank0]:     return AscendW8A8DynamicFusedMoEMethod()
[rank0]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in __init__
[rank0]:     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(
[rank0]: RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:102 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 15
[rank0]: [ERROR] 2025-04-27-03:11:08 (PID:540988, Device:0, RankID:0) ERR02200 DIST call hccl api failed.
[rank0]: EE9999: Inner Error!
[rank0]: EE9999: [PID: 540988] 2025-04-27-03:11:08.089.335 get error: phyid:1 realDeviceId:1 is err:0x7010003[FUNC:GetDeviceIndexByPhyId][FILE:api_error.cc][LINE:1918]
[rank0]:         TraceBack (most recent call last):
[rank0]:        rtGetDeviceIndexByPhyId execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]

[rank1]: Traceback (most recent call last):
[rank1]:   File "/workspace/vllm-ascend-main-0425/examples/dp_offline/data_parallel.py", line 84, in <module>
[rank1]:     main()
[rank1]:   File "/workspace/vllm-ascend-main-0425/examples/dp_offline/data_parallel.py", line 59, in main
[rank1]:     llm = LLM(model="/root/models/DeepSeek-V2-Lite-Chat-w8a8",
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1099, in inner
[rank1]:     return fn(*args, **kwargs)
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 248, in __init__
[rank1]:     self.llm_engine = LLMEngine.from_engine_args(
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 522, in from_engine_args
[rank1]:     return engine_cls.from_vllm_config(
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 498, in from_vllm_config
[rank1]:     return cls(
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 282, in __init__
[rank1]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank1]:     self._init_executor()
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
[rank1]:     self.collective_rpc("load_model")
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank1]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/worker/worker.py", line 209, in load_model
[rank1]:     self.model_runner.load_model()
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/worker/model_runner.py", line 946, in load_model
[rank1]:     self.model = get_model(vllm_config=self.vllm_config)
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank1]:     return loader.load_model(vllm_config=vllm_config)
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
[rank1]:     model = _initialize_model(vllm_config=vllm_config)
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
[rank1]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 555, in __init__
[rank1]:     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 481, in __init__
[rank1]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
[rank1]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank1]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
[rank1]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 483, in <lambda>
[rank1]:     lambda prefix: CustomDeepseekV2DecoderLayer(
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 389, in __init__
[rank1]:     self.mlp = CustomDeepseekV2MoE(
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/models/deepseek_v2.py", line 104, in __init__
[rank1]:     self.experts = AscendFusedMoE(
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/ops/fused_moe.py", line 593, in __init__
[rank1]:     self.quant_method = quant_config.get_quant_method(self, prefix)
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quant_config.py", line 101, in get_quant_method
[rank1]:     return AscendFusedMoEMethod(self, prefix,
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quant_config.py", line 276, in __init__
[rank1]:     self.quant_method = self.quantizer.build_moe_method()
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/quantizer.py", line 281, in build_moe_method
[rank1]:     return AscendW8A8DynamicFusedMoEMethod()
[rank1]:   File "/workspace/vllm-ascend-main-0425/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in __init__
[rank1]:     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(
[rank1]: RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:102 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 15
[rank1]: [ERROR] 2025-04-27-03:11:08 (PID:540989, Device:0, RankID:1) ERR02200 DIST call hccl api failed.
[rank1]: EE9999: Inner Error!
[rank1]: EE9999: [PID: 540989] 2025-04-27-03:11:08.269.791 get error: phyid:0 realDeviceId:0 is err:0x7010003[FUNC:GetDeviceIndexByPhyId][FILE:api_error.cc][LINE:1918]
[rank1]:         TraceBack (most recent call last):
[rank1]:        rtGetDeviceIndexByPhyId execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
```

