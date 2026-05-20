# Issue #1813: [Bug]: Cannot support Qwen3-30b-a3b on Altas 300I Duo(310p)

## 基本信息

- **编号**: #1813
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1813
- **创建时间**: 2025-07-15T09:09:04Z
- **关闭时间**: 2025-11-11T06:31:49Z
- **更新时间**: 2026-01-16T17:09:38Z
- **提交者**: @AlphaINF
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

I using a device with 4*300I duo, machine with Docker.


### 🐛 Describe the bug

I using the following command to start vllm-ascend, to deploy a qwen3-30b-a3b model:
```
# 设置镜像版本
export IMAGE=quay.io/ascend/vllm-ascend:v0.9.2rc1-310p

# 启动容器并在后台运行vLLM服务
docker run --rm \
        --name qwen3-30b \
        --device /dev/davinci2 \
        --device /dev/davinci3 \
        --device /dev/davinci4 \
        --device /dev/davinci5 \
        --device /dev/davinci_manager \
        --device /dev/devmm_svm \
        --device /dev/hisi_hdc \
        -v /usr/local/dcmi:/usr/local/dcmi \
        -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
        -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
        -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
        -v /etc/ascend_install.info:/etc/ascend_install.info \
        -v /root/.cache:/root/.cache \
        -v /home/HwHiAiUser/models:/models \
        -e OMP_NUM_THREADS=48 \
        -e VLLM_USE_V1=1 \
        -p 8001:8001 \
        $IMAGE \
        vllm serve --model="/models/Qwen3-30B-A3B" \
            --host 0.0.0.0 \
            --port 8001 \
            --max-num-seqs 32 \
            --max-seq-len-to-capture 32768 \
            --max-model-len 32768 \
            --served-model-name "qwen30b" \
            --enforce-eager \
            --dtype float16 \
            --tensor-parallel-size 4 \
            --enable-expert-parallel
```

however, it can't work, it shows that:
```
INFO 07-15 08:49:55 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:49:55 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:49:55 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:49:55 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-15 08:49:57 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-15 08:50:01 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:02 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-15 08:50:04 [api_server.py:1395] vLLM API server version 0.9.2
INFO 07-15 08:50:04 [cli_args.py:325] non-default args: {'host': '0.0.0.0', 'port': 8001, 'model': '/models/Qwen3-30B-A3B', 'dtype': 'float16', 'max_model_len': 32768, 'enforce_eager': True, 'max_seq_len_to_capture': 32768, 'served_model_name': ['qwen30b'], 'tensor_parallel_size': 4, 'enable_expert_parallel': True, 'max_num_seqs': 32}
INFO 07-15 08:50:16 [config.py:841] This model supports multiple tasks: {'reward', 'generate', 'classify', 'embed'}. Defaulting to 'generate'.
INFO 07-15 08:50:16 [config.py:1472] Using max model len 32768
INFO 07-15 08:50:17 [config.py:2285] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 07-15 08:50:17 [platform.py:161] Compilation disabled, using eager mode by default
INFO 07-15 08:50:25 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:25 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:25 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:25 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-15 08:50:26 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-15 08:50:28 [core.py:526] Waiting for init message from front-end.
INFO 07-15 08:50:30 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:30 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-15 08:50:30 [core.py:69] Initializing a V1 LLM engine (v0.9.2) with config: model='/models/Qwen3-30B-A3B', speculative_config=None, tokenizer='/models/Qwen3-30B-A3B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=qwen30b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}
INFO 07-15 08:50:30 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1, 2, 3], buffer_handle=(4, 16777216, 10, 'psm_f642643c'), local_subscribe_addr='ipc:///tmp/0b976716-eb37-48f7-b3be-fc6322de1c89', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 07-15 08:50:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:38 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:38 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:38 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:38 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-15 08:50:39 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:39 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:39 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:39 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-15 08:50:43 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 07-15 08:50:43 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 07-15 08:50:43 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-15 08:50:43 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-15 08:50:43 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(VllmWorker rank=1 pid=282) INFO 07-15 08:50:44 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6bccfe87'), local_subscribe_addr='ipc:///tmp/5cf31e34-8418-4525-9e3e-8b44e6817a76', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=2 pid=283) INFO 07-15 08:50:44 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_7837041b'), local_subscribe_addr='ipc:///tmp/b22798b1-d3a5-41a2-984e-af7d94c7dda2', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=0 pid=281) INFO 07-15 08:50:44 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_be7c04ba'), local_subscribe_addr='ipc:///tmp/3b4b4d1a-b0f4-4313-ba0d-37dc1fca8abd', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=3 pid=284) INFO 07-15 08:50:44 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6985db57'), local_subscribe_addr='ipc:///tmp/8ab9aff7-32cb-4987-b7cd-3da2e27d2b40', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 07-15 08:50:55 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:55 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:55 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:55 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:55 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:55 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:55 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:55 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:55 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:55 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:55 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:55 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-15 08:50:55 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-15 08:50:55 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-15 08:50:55 [__init__.py:235] Platform plugin ascend is activated
INFO 07-15 08:50:55 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-15 08:50:57 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:57 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:57 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-15 08:50:57 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorker rank=0 pid=281) INFO 07-15 08:51:03 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_8f9f5bb0'), local_subscribe_addr='ipc:///tmp/c225504e-1ba6-46a9-993a-06eb610e4e52', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=0 pid=281) INFO 07-15 08:51:03 [parallel_state.py:1076] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(VllmWorker rank=3 pid=284) INFO 07-15 08:51:03 [parallel_state.py:1076] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
(VllmWorker rank=1 pid=282) INFO 07-15 08:51:03 [parallel_state.py:1076] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
(VllmWorker rank=2 pid=283) INFO 07-15 08:51:03 [parallel_state.py:1076] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
(VllmWorker rank=1 pid=282) INFO 07-15 08:51:05 [model_runner_v1.py:1745] Starting to load model /models/Qwen3-30B-A3B...
(VllmWorker rank=0 pid=281) INFO 07-15 08:51:05 [model_runner_v1.py:1745] Starting to load model /models/Qwen3-30B-A3B...
(VllmWorker rank=3 pid=284) INFO 07-15 08:51:05 [model_runner_v1.py:1745] Starting to load model /models/Qwen3-30B-A3B...
(VllmWorker rank=2 pid=283) INFO 07-15 08:51:05 [model_runner_v1.py:1745] Starting to load model /models/Qwen3-30B-A3B...
Loading safetensors checkpoint shards:   0% Completed | 0/16 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   6% Completed | 1/16 [00:16<04:08, 16.59s/it]
Loading safetensors checkpoint shards:  12% Completed | 2/16 [00:29<03:25, 14.66s/it]
Loading safetensors checkpoint shards:  19% Completed | 3/16 [00:46<03:24, 15.71s/it]
Loading safetensors checkpoint shards:  25% Completed | 4/16 [01:04<03:16, 16.39s/it]
Loading safetensors checkpoint shards:  31% Completed | 5/16 [01:09<02:14, 12.19s/it]
Loading safetensors checkpoint shards:  38% Completed | 6/16 [01:24<02:14, 13.45s/it]
Loading safetensors checkpoint shards:  44% Completed | 7/16 [01:41<02:09, 14.42s/it]
Loading safetensors checkpoint shards:  50% Completed | 8/16 [01:51<01:45, 13.13s/it]
Loading safetensors checkpoint shards:  56% Completed | 9/16 [02:00<01:21, 11.66s/it]
Loading safetensors checkpoint shards:  62% Completed | 10/16 [02:11<01:08, 11.48s/it]
Loading safetensors checkpoint shards:  69% Completed | 11/16 [02:20<00:54, 10.81s/it]
Loading safetensors checkpoint shards:  75% Completed | 12/16 [02:33<00:46, 11.53s/it]
Loading safetensors checkpoint shards:  81% Completed | 13/16 [02:46<00:35, 11.98s/it]
Loading safetensors checkpoint shards:  88% Completed | 14/16 [03:00<00:25, 12.60s/it]
Loading safetensors checkpoint shards:  94% Completed | 15/16 [03:12<00:12, 12.23s/it]
Loading safetensors checkpoint shards: 100% Completed | 16/16 [03:23<00:00, 12.06s/it]
Loading safetensors checkpoint shards: 100% Completed | 16/16 [03:23<00:00, 12.74s/it]
(VllmWorker rank=0 pid=281) 
(VllmWorker rank=0 pid=281) INFO 07-15 08:54:29 [default_loader.py:272] Loading weights took 203.91 seconds
(VllmWorker rank=1 pid=282) INFO 07-15 08:54:30 [default_loader.py:272] Loading weights took 204.00 seconds
(VllmWorker rank=3 pid=284) INFO 07-15 08:54:30 [default_loader.py:272] Loading weights took 204.01 seconds
(VllmWorker rank=2 pid=283) INFO 07-15 08:54:30 [default_loader.py:272] Loading weights took 203.97 seconds
(VllmWorker rank=0 pid=281) INFO 07-15 08:54:30 [model_runner_v1.py:1777] Loading model weights took 14.2915 GB
(VllmWorker rank=1 pid=282) INFO 07-15 08:54:30 [model_runner_v1.py:1777] Loading model weights took 14.2915 GB
(VllmWorker rank=2 pid=283) INFO 07-15 08:54:30 [model_runner_v1.py:1777] Loading model weights took 14.2915 GB
(VllmWorker rank=3 pid=284) INFO 07-15 08:54:30 [model_runner_v1.py:1777] Loading model weights took 14.2915 GB
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 152, in determine_available_memory
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     self.model_runner.profile_run()
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1679, in profile_run
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     hidden_states = self._dummy_run(self.max_num_tokens)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1663, in _dummy_run
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 525, in forward
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 173, in __call__
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return self.forward(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 369, in forward
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     hidden_states, residual = layer(positions, hidden_states, residual)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 313, in forward
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     hidden_states = self.mlp(hidden_states)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 143, in forward
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522]     return final_hidden_states.view(orig_shape)
(VllmWorker rank=0 pid=281) ERROR 07-15 08:54:44 [multiproc_executor.py:522] RuntimeError: shape '[2048, 2048]' is invalid for input of size 16777216
ERROR 07-15 08:54:44 [core.py:586] EngineCore failed to start.
ERROR 07-15 08:54:44 [core.py:586] Traceback (most recent call last):
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 07-15 08:54:44 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
ERROR 07-15 08:54:44 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__
ERROR 07-15 08:54:44 [core.py:586]     self._initialize_kv_caches(vllm_config)
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 142, in _initialize_kv_caches
ERROR 07-15 08:54:44 [core.py:586]     available_gpu_memory = self.model_executor.determine_available_memory()
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
ERROR 07-15 08:54:44 [core.py:586]     output = self.collective_rpc("determine_available_memory")
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 215, in collective_rpc
ERROR 07-15 08:54:44 [core.py:586]     result = get_response(w, dequeue_timeout)
ERROR 07-15 08:54:44 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 202, in get_response
ERROR 07-15 08:54:44 [core.py:586]     raise RuntimeError(
ERROR 07-15 08:54:44 [core.py:586] RuntimeError: Worker failed with error 'shape '[2048, 2048]' is invalid for input of size 16777216', please check the stack trace above for the root cause
ERROR 07-15 08:54:54 [multiproc_executor.py:135] Worker proc VllmWorker-3 died unexpectedly, shutting down executor.
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
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 142, in _initialize_kv_caches
    available_gpu_memory = self.model_executor.determine_available_memory()
  File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
    output = self.collective_rpc("determine_available_memory")
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 215, in collective_rpc
    result = get_response(w, dequeue_timeout)
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 202, in get_response
    raise RuntimeError(
RuntimeError: Worker failed with error 'shape '[2048, 2048]' is invalid for input of size 16777216', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 65, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 55, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 162, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 124, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 96, in make_async_mp_client
    return AsyncMPClient(*client_args)
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 666, in __init__
    super().__init__(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 403, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 434, in launch_core_engines
    wait_for_engine_startup(
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 484, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-07-15-08:55:00 (PID:1, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

I want to know how can i run qwen3-30b-a3b on the machine?
