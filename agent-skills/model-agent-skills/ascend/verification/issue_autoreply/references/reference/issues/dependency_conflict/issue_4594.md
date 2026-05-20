# Issue #4594: [Bug]: master分支aclgraph decode only测试qwen3 32B 3.5k输入长序列时，服务崩溃SelfAttentionOperation setup failed

## 基本信息

- **编号**: #4594
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4594
- **创建时间**: 2025-12-01T06:48:23Z
- **关闭时间**: 2025-12-01T09:13:34Z
- **更新时间**: 2025-12-01T09:13:34Z
- **提交者**: @changdawei1
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
export TASK_QUEUE_ENABLE=1
export VLLM_USE_V1=1
export OMP_PROC_BIND=false
export HCCL_OP_EXPANSION_MODE="AIV"
export VLLM_ASCEND_ENABLE_TOPK_OPTIMIZE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM=1
export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1
export VLLM_ASCEND_ENABLE_PREFETCH_MLP=1

ip=127.0.0.1
python -m vllm.entrypoints.openai.api_server \
	--model /mnt/nvme0n1/models/Qwen3-32B  \
	--tensor-parallel-size 8 \
	--gpu-memory-utilization 0.9 \
	--max-num-seqs=200 \
	--block-size 128 \
	--max-model-len 6656 \
	--trust-remote-code \
	--disable-log-requests \
	--served-model-name llama \
	--no-enable-prefix-caching \
	--distributed_executor_backend "mp" \
	--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
	--async-scheduling \
	--host ${ip} \
	--port ${port} > ${log} 2>&1 &
<summary>The output of `python collect_env.py`</summary>
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.h665.eulerosv2r11.aarch64-aarch64-with-glibc2.35

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.2
vLLM Ascend Version: 0.1.dev1424+gfb5538625.d20251129 (git sha: fb5538625, date: 20251129)

```text
Your output of above commands here
```
INFO 12-01 06:28:06 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:06 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:06 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:06 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:11 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:13 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
INFO 12-01 06:28:13 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:13 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048.
WARNING 12-01 06:28:13 [argparse_utils.py:79] argument '--disable-log-requests' is deprecated and replaced with '--enable-log-requests'. This will be removed in v0.12.0.
(APIServer pid=149035) INFO 12-01 06:28:13 [api_server.py:1977] vLLM API server version 0.11.2
(APIServer pid=149035) INFO 12-01 06:28:13 [utils.py:253] non-default args: {'host': '127.0.0.1', 'port': 8080, 'model': '/mnt/nvme0n1/models/Qwen3-32B', 'trust_remote_code': True, 'max_model_len': 6656, 'served_model_name': ['llama'], 'distributed_executor_backend': 'mp', 'tensor_parallel_size': 8, 'block_size': 128, 'enable_prefix_caching': False, 'max_num_seqs': 200, 'async_scheduling': True, 'compilation_config': {'level': None, 'mode': None, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'eager', 'custom_ops': [], 'splitting_ops': None, 'compile_mm_encoder': False, 'use_inductor': None, 'compile_sizes': None, 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 0, 'cudagraph_capture_sizes': None, 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': None, 'local_cache_dir': None}}
(APIServer pid=149035) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=149035) INFO 12-01 06:28:13 [model.py:631] Resolved architecture: Qwen3ForCausalLM
(APIServer pid=149035) INFO 12-01 06:28:13 [model.py:1745] Using max model len 6656
(APIServer pid=149035) INFO 12-01 06:28:13 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=149035) INFO 12-01 06:28:13 [utils.py:951] FLASHCOMM2 not enable.
(APIServer pid=149035) WARNING 12-01 06:28:13 [vllm.py:787] Batch sizes [1, 2, 4] are removed because they are not multiple of tp_size 8 when sequence parallelism is enabled
(APIServer pid=149035) INFO 12-01 06:28:13 [platform.py:222] FULL_DECODE_ONLY compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238] 
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             **********************************************************************************
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * WARNING: You have enabled the *full graph* feature.
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * This is an early experimental stage and may involve various unknown issues.
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * A known problem is that capturing too many batch sizes can lead to OOM
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * (Out of Memory) errors or inference hangs. If you encounter such issues,
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * consider reducing `gpu_memory_utilization` or manually specifying a smaller
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * batch size for graph capture.
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * For more details, please refer to:
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             * https://docs.vllm.ai/en/stable/configuration/conserving_memory.html#reduce-cuda-graphs
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             **********************************************************************************
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:238]             
(APIServer pid=149035) WARNING 12-01 06:28:13 [platform.py:272] If chunked prefill or prefix caching is enabled, block size must be set to 128.
INFO 12-01 06:28:21 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:21 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:21 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:21 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:26 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
(EngineCore_DP0 pid=149178) INFO 12-01 06:28:28 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
(EngineCore_DP0 pid=149178) INFO 12-01 06:28:28 [core.py:93] Initializing a V1 LLM engine (v0.11.2) with config: model='/mnt/nvme0n1/models/Qwen3-32B', speculative_config=None, tokenizer='/mnt/nvme0n1/models/Qwen3-32B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=6656, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=llama, enable_prefix_caching=False, enable_chunked_prefill=True, pooler_config=None, compilation_config={'level': None, 'mode': <CompilationMode.VLLM_COMPILE: 3>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'eager', 'custom_ops': ['all'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention_core', 'vllm::kda_attention', 'vllm::sparse_attn_indexer'], 'compile_mm_encoder': False, 'use_inductor': False, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 272, 288, 304, 320, 336, 352, 368, 384, 400], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 400, 'local_cache_dir': None}
(EngineCore_DP0 pid=149178) WARNING 12-01 06:28:28 [multiproc_executor.py:869] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:36 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:28:36 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:28:36 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:28:36 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:28:41 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:41 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:41 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:28:42 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:43 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
INFO 12-01 06:28:43 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
INFO 12-01 06:28:44 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:44 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:44 [utils.py:951] FLASHCOMM2 not enable.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-01 06:28:44 [registry.py:740] Model architecture Qwen3NextMTP is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next_mtp:CustomQwen3NextMTP.
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:44 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:44 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:44 [__init__.py:106] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
INFO 12-01 06:28:45 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:45 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:45 [utils.py:951] FLASHCOMM2 not enable.
INFO 12-01 06:28:45 [parallel_state.py:1208] world_size=8 rank=3 local_rank=3 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:45 [parallel_state.py:1208] world_size=8 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:45 [parallel_state.py:1208] world_size=8 rank=4 local_rank=4 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:46 [parallel_state.py:1208] world_size=8 rank=6 local_rank=6 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:46 [parallel_state.py:1208] world_size=8 rank=5 local_rank=5 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:46 [parallel_state.py:1208] world_size=8 rank=1 local_rank=1 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:46 [parallel_state.py:1208] world_size=8 rank=7 local_rank=7 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:46 [parallel_state.py:1208] world_size=8 rank=2 local_rank=2 distributed_init_method=tcp://127.0.0.1:40845 backend=hccl
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 0 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 1 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 2 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 4 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 4, EP rank 4
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 3 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 5 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 5, EP rank 5
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 6 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 6, EP rank 6
INFO 12-01 06:28:47 [parallel_state.py:1394] rank 7 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 7, EP rank 7
(Worker_TP5 pid=149322) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP1 pid=149318) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP3 pid=149320) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP4 pid=149321) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP7 pid=149324) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP2 pid=149319) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP6 pid=149323) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
(Worker_TP0 pid=149317) INFO 12-01 06:28:47 [model_runner_v1.py:3182] Starting to load model /mnt/nvme0n1/models/Qwen3-32B...
Loading safetensors checkpoint shards:   0% Completed | 0/17 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   6% Completed | 1/17 [00:00<00:03,  4.94it/s]
Loading safetensors checkpoint shards:  12% Completed | 2/17 [00:00<00:03,  4.43it/s]
Loading safetensors checkpoint shards:  18% Completed | 3/17 [00:00<00:03,  3.97it/s]
Loading safetensors checkpoint shards:  24% Completed | 4/17 [00:00<00:03,  3.90it/s]
Loading safetensors checkpoint shards:  29% Completed | 5/17 [00:01<00:03,  3.89it/s]
Loading safetensors checkpoint shards:  35% Completed | 6/17 [00:01<00:02,  4.12it/s]
Loading safetensors checkpoint shards:  41% Completed | 7/17 [00:01<00:02,  3.98it/s]
Loading safetensors checkpoint shards:  47% Completed | 8/17 [00:01<00:02,  3.93it/s]
Loading safetensors checkpoint shards:  53% Completed | 9/17 [00:02<00:02,  3.93it/s]
Loading safetensors checkpoint shards:  59% Completed | 10/17 [00:02<00:01,  3.92it/s]
Loading safetensors checkpoint shards:  65% Completed | 11/17 [00:02<00:01,  4.39it/s]
Loading safetensors checkpoint shards:  71% Completed | 12/17 [00:02<00:01,  4.31it/s]
Loading safetensors checkpoint shards:  76% Completed | 13/17 [00:03<00:00,  4.18it/s]
Loading safetensors checkpoint shards:  82% Completed | 14/17 [00:03<00:00,  4.11it/s]
Loading safetensors checkpoint shards:  88% Completed | 15/17 [00:03<00:00,  4.04it/s]
Loading safetensors checkpoint shards:  94% Completed | 16/17 [00:03<00:00,  4.02it/s]
Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:04<00:00,  4.00it/s]
Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:04<00:00,  4.06it/s]
(Worker_TP0 pid=149317) 
(Worker_TP0 pid=149317) INFO 12-01 06:28:52 [default_loader.py:314] Loading weights took 4.25 seconds
INFO 12-01 06:29:01 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:01 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:01 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:01 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:01 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:01 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:01 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:01 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:02 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:02 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:02 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:02 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:02 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:02 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:02 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:02 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:02 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:02 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:02 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:02 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:02 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:02 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:02 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:02 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:03 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:03 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:03 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:03 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:03 [__init__.py:40] Available plugins for group vllm.platform_plugins:
INFO 12-01 06:29:03 [__init__.py:42] - ascend -> vllm_ascend:register
INFO 12-01 06:29:03 [__init__.py:45] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-01 06:29:03 [__init__.py:217] Platform plugin ascend is activated
INFO 12-01 06:29:06 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:06 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:07 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:07 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:07 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:07 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:08 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 12-01 06:29:08 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
(Worker_TP4 pid=149321) INFO 12-01 06:29:12 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP3 pid=149320) INFO 12-01 06:29:13 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP1 pid=149318) INFO 12-01 06:29:13 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP5 pid=149322) INFO 12-01 06:29:14 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP0 pid=149317) INFO 12-01 06:29:14 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP6 pid=149323) INFO 12-01 06:29:16 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP2 pid=149319) INFO 12-01 06:29:16 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP7 pid=149324) INFO 12-01 06:29:18 [model_runner_v1.py:3208] Loading model weights took 7.6857 GB
(Worker_TP0 pid=149317) INFO 12-01 06:29:38 [backends.py:631] Using cache directory: /root/.cache/vllm/torch_compile_cache/a0ceb5f0fe/rank_0_0/backbone for vLLM's torch.compile
(Worker_TP0 pid=149317) INFO 12-01 06:29:38 [backends.py:647] Dynamo bytecode transform time: 20.27 s
(Worker_TP0 pid=149317) INFO 12-01 06:29:46 [backends.py:282] Compiling a graph for dynamic shape takes 5.93 s
(Worker_TP0 pid=149317) INFO 12-01 06:29:56 [monitor.py:34] torch.compile takes 26.20 s in total
(Worker_TP4 pid=149321) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49077283328, total memory: 65452113920
(Worker_TP3 pid=149320) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49076247040, total memory: 65452113920
(Worker_TP6 pid=149323) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49077930496, total memory: 65452113920
(Worker_TP0 pid=149317) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49075702272, total memory: 65452113920
(Worker_TP5 pid=149322) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49077107200, total memory: 65452113920
(Worker_TP1 pid=149318) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49076705792, total memory: 65452113920
(Worker_TP7 pid=149324) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49075792384, total memory: 65452113920
(Worker_TP2 pid=149319) INFO 12-01 06:30:00 [worker_v1.py:278] Available memory: 49076447744, total memory: 65452113920
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1229] GPU KV cache size: 1,497,600 tokens
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:00 [kv_cache_utils.py:1234] Maximum concurrency for 6,656 tokens per request: 225.00x
(Worker_TP0 pid=149317) INFO 12-01 06:30:01 [model_runner_v1.py:3938] Starting to capture ACL graphs for cases: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200], mode: FULL, uniform_decode: True
Capturing ACL graphs (decode, FULL):   0%|          | 0/25 [00:00<?, ?it/s][rank4]:[W1201 06:30:02.924750170 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank6]:[W1201 06:30:02.953718380 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank1]:[W1201 06:30:02.958914280 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank3]:[W1201 06:30:02.961741950 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank5]:[W1201 06:30:02.982037480 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W1201 06:30:02.999116960 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank7]:[W1201 06:30:02.076356040 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
Capturing ACL graphs (decode, FULL):  16%|█▌        | 4/25 [00:05<00:30,  1.44s/it][rank2]:[W1201 06:30:08.278954820 compiler_depend.ts:187] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
Capturing ACL graphs (decode, FULL):  96%|█████████▌| 24/25 [00:33<00:01,  1.33s/it](Worker_TP1 pid=149318) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.39 GiB
Capturing ACL graphs (decode, FULL): 100%|██████████| 25/25 [00:35<00:00,  1.42s/it]
(Worker_TP0 pid=149317) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.40 GiB
(Worker_TP4 pid=149321) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.39 GiB
(Worker_TP7 pid=149324) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.39 GiB
(Worker_TP5 pid=149322) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.39 GiB
(Worker_TP6 pid=149323) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.40 GiB
(Worker_TP3 pid=149320) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.39 GiB
(Worker_TP2 pid=149319) INFO 12-01 06:30:37 [model_runner_v1.py:4057] Graph capturing finished in 36 secs, took 0.40 GiB
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:37 [core.py:250] init engine (profile, create kv cache, warmup model) took 79.08 seconds
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:37 [core.py:180] Batch queue is enabled with size 2
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:38 [utils.py:951] FLASHCOMM2 not enable.
(EngineCore_DP0 pid=149178) INFO 12-01 06:30:38 [platform.py:222] FULL_DECODE_ONLY compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238] 
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             **********************************************************************************
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * WARNING: You have enabled the *full graph* feature.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * This is an early experimental stage and may involve various unknown issues.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * A known problem is that capturing too many batch sizes can lead to OOM
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * (Out of Memory) errors or inference hangs. If you encounter such issues,
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * consider reducing `gpu_memory_utilization` or manually specifying a smaller
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * batch size for graph capture.
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * For more details, please refer to:
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             * https://docs.vllm.ai/en/stable/configuration/conserving_memory.html#reduce-cuda-graphs
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             **********************************************************************************
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:238]             
(EngineCore_DP0 pid=149178) WARNING 12-01 06:30:38 [platform.py:272] If chunked prefill or prefix caching is enabled, block size must be set to 128.
(APIServer pid=149035) INFO 12-01 06:30:38 [api_server.py:1725] Supported tasks: ['generate']
(APIServer pid=149035) WARNING 12-01 06:30:38 [model.py:1568] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
(APIServer pid=149035) INFO 12-01 06:30:38 [serving_responses.py:154] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=149035) INFO 12-01 06:30:38 [serving_chat.py:131] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=149035) INFO 12-01 06:30:38 [serving_completion.py:73] Using default completion sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=149035) INFO 12-01 06:30:38 [serving_chat.py:131] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=149035) INFO 12-01 06:30:38 [api_server.py:2052] Starting vLLM API server 0 on http://127.0.0.1:8080
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:38] Available routes are:
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /openapi.json, Methods: GET, HEAD
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /docs, Methods: GET, HEAD
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /docs/oauth2-redirect, Methods: GET, HEAD
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /redoc, Methods: GET, HEAD
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /health, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /load, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /tokenize, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /detokenize, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/models, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /version, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/responses, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/messages, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/chat/completions, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/completions, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/embeddings, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /pooling, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /classify, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /score, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/score, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/audio/translations, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /rerank, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v1/rerank, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /v2/rerank, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /inference/v1/generate, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /ping, Methods: GET
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /ping, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /invocations, Methods: POST
(APIServer pid=149035) INFO 12-01 06:30:38 [launcher.py:46] Route: /metrics, Methods: GET
(APIServer pid=149035) INFO:     Started server process [149035]
(APIServer pid=149035) INFO:     Waiting for application startup.
(APIServer pid=149035) INFO:     Application startup complete.
(APIServer pid=149035) INFO 12-01 06:31:02 [chat_utils.py:557] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
(APIServer pid=149035) INFO:     127.0.0.1:36136 - "POST /v1/chat/completions HTTP/1.1" 200 OK
[rank1]:[E1201 06:31:02.635343200 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xd4 (0xffff82c23ea4 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xe4 (0xffff82bc3e44 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x254 (0xffff5f91c0e8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0x9ebec (0xffff5f91ebec in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x26e6c10 (0xffff75276c10 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x961a94 (0xffff734f1a94 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9644c0 (0xffff734f44c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x96072c (0xffff734f072c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd29cc (0xffff82a329cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #9: <unknown function> + 0x80398 (0xffff8ed20398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #10: <unknown function> + 0xe9e9c (0xffff8ed89e9c in /lib/aarch64-linux-gnu/libc.so.6)

[rank0]:[E1201 06:31:02.635822600 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xd4 (0xffff80553ea4 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xe4 (0xffff804f3e44 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x254 (0xffff6127c0e8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0x9ebec (0xffff6127ebec in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x26e6c10 (0xffff72ba6c10 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x961a94 (0xffff70e21a94 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9644c0 (0xffff70e244c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x96072c (0xffff70e2072c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd29cc (0xffff803629cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #9: <unknown function> + 0x80398 (0xffff8c650398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #10: <unknown function> + 0xe9e9c (0xffff8c6b9e9c in /lib/aarch64-linux-gnu/libc.so.6)

</details>


### 🐛 Describe the bug

[rank0]:[E1201 06:31:02.635822600 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xd4 (0xffff80553ea4 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0xe4 (0xffff804f3e44 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x254 (0xffff6127c0e8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0x9ebec (0xffff6127ebec in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x26e6c10 (0xffff72ba6c10 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x961a94 (0xffff70e21a94 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9644c0 (0xffff70e244c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x96072c (0xffff70e2072c in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd29cc (0xffff803629cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #9: <unknown function> + 0x80398 (0xffff8c650398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #10: <unknown function> + 0xe9e9c (0xffff8c6b9e9c in /lib/aarch64-linux-gnu/libc.so.6)
