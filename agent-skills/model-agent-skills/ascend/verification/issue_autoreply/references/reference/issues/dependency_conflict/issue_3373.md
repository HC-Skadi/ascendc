# Issue #3373: [Bug]: 按照文档执行 qwen3-next 启动失败，在 arm 910c 上面

## 基本信息

- **编号**: #3373
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3373
- **创建时间**: 2025-10-10T14:16:20Z
- **关闭时间**: 2025-11-11T03:56:18Z
- **更新时间**: 2025-11-26T05:48:32Z
- **提交者**: @yingxudeng
- **评论数**: 4

## 标签

bug; qwen3-next

## 问题描述

### Your current environment

文档中环境：https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_npu_qwen3_next.html

### 🐛 Describe the bug

按照文档执行 qwen3-next 启动失败，在 arm 910c 上面，报错如下：
`root@51e83cfa55ab:/workspace# vllm serve /export/home/models/Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 4 --max-model-len 4096 --gpu-memory-utilization 0.7 --enforce-eager
INFO 10-10 14:03:18 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:18 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:18 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:18 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-10 14:03:21 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-10 14:03:21 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(APIServer pid=3100) INFO 10-10 14:03:22 [api_server.py:1839] vLLM API server version 0.11.0rc3
(APIServer pid=3100) INFO 10-10 14:03:22 [utils.py:233] non-default args: {'model_tag': '/export/home/models/Qwen3-Next-80B-A3B-Instruct', 'model': '/export/home/models/Qwen3-Next-80B-A3B-Instruct', 'max_model_len': 4096, 'enforce_eager': True, 'tensor_parallel_size': 4, 'gpu_memory_utilization': 0.7}
(APIServer pid=3100) INFO 10-10 14:03:22 [model.py:547] Resolved architecture: Qwen3NextForCausalLM
(APIServer pid=3100) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=3100) INFO 10-10 14:03:22 [model.py:1510] Using max model len 4096
(APIServer pid=3100) INFO 10-10 14:03:22 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=3100) INFO 10-10 14:03:22 [config.py:297] Hybrid or mamba-based model detected: disabling prefix caching since it is not yet supported.
(APIServer pid=3100) INFO 10-10 14:03:22 [config.py:308] Hybrid or mamba-based model detected: setting cudagraph mode to FULL_AND_PIECEWISE in order to optimize performance.
(APIServer pid=3100) INFO 10-10 14:03:22 [__init__.py:381] Cudagraph is disabled under eager mode
(APIServer pid=3100) INFO 10-10 14:03:22 [platform.py:141] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
(APIServer pid=3100) INFO 10-10 14:03:22 [platform.py:179] Compilation disabled, using eager mode by default
INFO 10-10 14:03:27 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:27 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:27 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:27 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-10 14:03:30 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(EngineCore_DP0 pid=3372) INFO 10-10 14:03:30 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(EngineCore_DP0 pid=3372) INFO 10-10 14:03:30 [core.py:77] Initializing a V1 LLM engine (v0.11.0rc3) with config: model='/export/home/models/Qwen3-Next-80B-A3B-Instruct', speculative_config=None, tokenizer='/export/home/models/Qwen3-Next-80B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/export/home/models/Qwen3-Next-80B-A3B-Instruct, enable_prefix_caching=False, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
(EngineCore_DP0 pid=3372) WARNING 10-10 14:03:30 [multiproc_executor.py:720] Reducing Torch parallelism from 640 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(EngineCore_DP0 pid=3372) INFO 10-10 14:03:30 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1, 2, 3], buffer_handle=(4, 16777216, 10, 'psm_e0d73146'), local_subscribe_addr='ipc:///tmp/82c06d02-287b-46e4-9278-4c86c39e7d83', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:35 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:35 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:35 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:35 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:35 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:35 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:35 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:35 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:35 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:35 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:35 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:35 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:35 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:35 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:35 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:35 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-10 14:03:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-10 14:03:38 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
INFO 10-10 14:03:46 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:46 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:46 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:46 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:46 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:46 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:46 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:46 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:46 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:46 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:46 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:46 [__init__.py:207] Platform plugin ascend is activated
INFO 10-10 14:03:46 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-10 14:03:46 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-10 14:03:46 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-10 14:03:46 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-10 14:03:49 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:49 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:49 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-10 14:03:49 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 10-10 14:03:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_39c57c38'), local_subscribe_addr='ipc:///tmp/0cc5b443-0fcd-49fe-8fca-54c70d122c3c', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_92970db9'), local_subscribe_addr='ipc:///tmp/6af22cba-06e1-4d4b-bda0-8011189e6f2c', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6cc39a6a'), local_subscribe_addr='ipc:///tmp/82b6d478-5ca9-4f55-b840-2887f51a35e6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_aa9dbd98'), local_subscribe_addr='ipc:///tmp/1158b9df-1fe8-4859-8d9a-83849cccd7d5', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:52 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_565575ae'), local_subscribe_addr='ipc:///tmp/bd570eb8-df6c-4d20-bc7e-1c49a71bad4d', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-10 14:03:52 [parallel_state.py:1208] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 10-10 14:03:52 [parallel_state.py:1208] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 10-10 14:03:52 [parallel_state.py:1208] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 10-10 14:03:52 [parallel_state.py:1208] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
ERROR 10-10 14:03:52 [multiproc_executor.py:597] WorkerProc failed to start.
ERROR 10-10 14:03:52 [multiproc_executor.py:597] Traceback (most recent call last):
ERROR 10-10 14:03:52 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
ERROR 10-10 14:03:52 [multiproc_executor.py:597]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 10-10 14:03:52 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 430, in __init__
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     self.worker.init_device()
ERROR 10-10 14:03:52 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 259, in init_device
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     self.worker.init_device()  # type: ignore
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     ^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 10-10 14:03:52 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 195, in init_device
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     self.model_runner = NPUModelRunner(self.vllm_config, device)
ERROR 10-10 14:03:52 [multiproc_executor.py:597]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 10-10 14:03:52 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 357, in __init__
ERROR 10-10 14:03:52 [multiproc_executor.py:597]     self.input_ids = torch.zeros(self.max_num_tokens,
ERROR 10-10 14:03:52 [multiproc_executor.py:597]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 10-10 14:03:52 [multiproc_executor.py:597] RuntimeError: zero_:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:26 NPU function error: call aclnnInplaceZero failed, error code is 561103
ERROR 10-10 14:03:52 [multiproc_executor.py:597] [ERROR] 2025-10-10-14:03:52 (PID:3513, Device:3, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 10-10 14:03:52 [multiproc_executor.py:597] EZ9999: Inner Error!
ERROR 10-10 14:03:52 [multiproc_executor.py:597] EZ9999: [PID: 3513] 2025-10-10-14:03:52.302.004 Parse dynamic kernel config fail.
ERROR 10-10 14:03:52 [multiproc_executor.py:597]         TraceBack (most recent call last):
ERROR 10-10 14:03:52 [multiproc_executor.py:597]        AclOpKernelInit failed opType
ERROR 10-10 14:03:52 [multiproc_executor.py:597]        ZerosLike ADD_TO_LAUNCHER_LIST_AICORE failed.
ERROR 10-10 14:03:52 [multiproc_executor.py:597] 
INFO 10-10 14:03:52 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-10 14:03:52 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-10 14:03:52 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-10 14:03:52 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708]     raise e from None
(EngineCore_DP0 pid=3372) ERROR 10-10 14:03:56 [core.py:708] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP0 pid=3372) Process EngineCore_DP0:
(EngineCore_DP0 pid=3372) Traceback (most recent call last):
(EngineCore_DP0 pid=3372)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=3372)     self.run()
(EngineCore_DP0 pid=3372)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=3372)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=3372)     raise e
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3372)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3372)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3372)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=3372)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3372)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=3372)     self._init_executor()
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=3372)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=3372)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3372)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=3372)     raise e from None
(EngineCore_DP0 pid=3372) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(APIServer pid=3100) Traceback (most recent call last):
(APIServer pid=3100)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=3100)     sys.exit(main())
(APIServer pid=3100)              ^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=3100)     args.dispatch_function(args)
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=3100)     uvloop.run(run_server(args))
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=3100)     return runner.run(wrapper())
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=3100)     return self._loop.run_until_complete(task)
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=3100)     return await main
(APIServer pid=3100)            ^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=3100)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=3100)     async with build_async_engine_client(
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=3100)     return await anext(self.gen)
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=3100)     async with build_async_engine_client_from_engine_args(
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=3100)     return await anext(self.gen)
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=3100)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=3100)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=3100)     return fn(*args, **kwargs)
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=3100)     return cls(
(APIServer pid=3100)            ^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=3100)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=3100)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=3100)     return AsyncMPClient(*client_args)
(APIServer pid=3100)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=3100)     super().__init__(
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=3100)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=3100)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=3100)     next(self.gen)
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=3100)     wait_for_engine_startup(
(APIServer pid=3100)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=3100)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=3100) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=3100) [ERROR] 2025-10-10-14:03:58 (PID:3100, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception`
