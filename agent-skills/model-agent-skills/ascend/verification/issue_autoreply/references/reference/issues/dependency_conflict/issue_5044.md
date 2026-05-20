# Issue #5044: [Bug]: decode fail to get kv cache from mooncake store when directly use V1 mooncake store connector

## 基本信息

- **编号**: #5044
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5044
- **创建时间**: 2025-12-15T12:00:45Z
- **关闭时间**: 2025-12-16T07:01:03Z
- **更新时间**: 2025-12-16T07:01:03Z
- **提交者**: @Shichang-Zhang
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc3

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| 4     910B4               | OK            | 94.1        43                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2854 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux

```

</details>


### 🐛 Describe the bug

I deployed 1P1D with only Mooncake Store Connector, but failed when decode trying to get the KV cache with the adxl engine.
The Prefill (P) and Decode (D) are deployed with use 1 pods each on the same machine, with 1× 910B NPUs per pod.
The base image used is quay.io/ascend/vllm-ascend:v0.11.0rc3, has been installed.

**Prefill Node Start Command:**
```
export MOONCAKE_CONFIG_PATH=/workspace/mooncake_config.json
          echo "{
              \"local_hostname\": \"$POD_IP\",
              \"metadata_server\": \"redis://redis-service:6379\",
              \"master_server_address\": \"mooncake-master-service:30089\",
              \"protocol\": \"ascend\",
              \"device_name\": \"\",
              \"global_segment_size\": 42949672960,
              \"use_ascend_direct\": \"true\"
          }" > ${MOONCAKE_CONFIG_PATH}
VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen3-8B \
    --port 8100 \
    --trust-remote-code \
    --enforce-eager \
    --no_enable_prefix_caching \
    --tensor-parallel-size 1 \
    --data-parallel-size 1 \
    --max-model-len 10000 \
    --block-size 128 \
    --max-num-batched-tokens 4096 \
    --kv-transfer-config \
    '{
	"kv_connector": "MooncakeConnectorStoreV1",
	"kv_role": "kv_producer",
        "mooncake_rpc_port":"0",
        "kv_buffer_device":"npu",
	"kv_connector_extra_config": {
		"use_layerwise": false,
		"prefill": {
						"dp_size": 1,
						"tp_size": 1
					},
					"decode": {
						"dp_size": 1,
						"tp_size": 1
					}
	}
}'
```
**Decode Node Start Command:**
```
export MOONCAKE_CONFIG_PATH=/workspace/mooncake_config.json
          echo "{
              \"local_hostname\": \"$POD_IP\",
              \"metadata_server\": \"redis://redis-service:6379\",
              \"master_server_address\": \"mooncake-master-service:30089\",
              \"protocol\": \"ascend\",
              \"device_name\": \"\",
              \"global_segment_size\": 42949672960,
              \"use_ascend_direct\": \"true\"
          }" > ${MOONCAKE_CONFIG_PATH}
python3 -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen3-8B \
    --port 8200 \
    --trust-remote-code \
    --enforce-eager \
    --no_enable_prefix_caching \
    --tensor-parallel-size 1 \
    --data-parallel-size 1 \
    --max-model-len 10000 \
    --block-size 128 \
    --max-num-batched-tokens 4096 \
    --kv-transfer-config \
    '{
	"kv_connector": "MooncakeConnectorStoreV1",
	"kv_role": "kv_consumer",
        "mooncake_rpc_port":"1",
        "kv_buffer_device":"npu",
	"kv_connector_extra_config": {
		"use_layerwise": false,
                "consumer_is_to_load": true,
		"prefill": {
						"dp_size": 1,
						"tp_size": 1
					},
					"decode": {
						"dp_size": 1,
						"tp_size": 1
					}
	}
    }'
```

**Proxy server:**
I used a proxy server modified from the example: https://github.com/vllm-project/vllm-ascend/blob/main/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py, which just adding k8s auto service discover for prefill and decode pods.

The curl request to the proxy server. 
```
curl -X POST http://xxxx:8000/v1/chat/completions \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer fake-key" \
     -d '{
           "model": "Qwen/Qwen3-8B",
           "messages": [
             {
               "role": "user",
               "content": "Reflect on daily growth and life choices: How do morning routines—like meditation, exercise, or planning—shape productivity and mental state throughout the day, and what tips help stick to these habits amid busy schedules? Discuss the value of traveling locally—why exploring nearby parks, towns, or cultural spots can be as rewarding as long trips, and how it fosters deeper connection with one’s community. Explore the impact of digital detoxes: what benefits do short breaks from phones and social media bring to focus, relationships, and mental well-being, and how to practice them without feeling disconnected? Please answer me as soon as possible. Thank you!"
             }
           ],
           "stream": false
         }'
```

I saw the inference response from the proxy server, but also found there are error logs in the decode pod. **The log shows successfully connect to the segment, but then transfer failed with error code `103901`. `10.250.40.157` is the IP address of Prefill0-pod0.**

**Prefill Node log:**
```
INFO 12-15 11:44:45 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-15 11:44:45 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-15 11:44:45 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-15 11:44:45 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
WARNING 12-15 11:44:51 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-15 11:44:51 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 12-15 11:44:51 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(APIServer pid=161) INFO 12-15 11:44:52 [api_server.py:1839] vLLM API server version 0.11.0
(APIServer pid=161) INFO 12-15 11:44:52 [utils.py:233] non-default args: {'port': 8100, 'model': 'Qwen/Qwen3-8B', 'trust_remote_code': True, 'max_model_len': 10000, 'enforce_eager': True, 'block_size': 128, 'enable_prefix_caching': False, 'max_num_batched_tokens': 4096, 'kv_transfer_config': KVTransferConfig(kv_connector='MooncakeConnectorStoreV1', engine_id='3029508e-1e54-42ec-921d-b052f06f3c19', kv_buffer_device='npu', kv_buffer_size=1000000000.0, kv_role='kv_producer', kv_rank=None, kv_parallel_size=1, kv_ip='127.0.0.1', kv_port=14579, kv_connector_extra_config={'use_layerwise': False, 'prefill': {'dp_size': 1, 'tp_size': 1}, 'decode': {'dp_size': 1, 'tp_size': 1}}, kv_connector_module_path=None)}
(APIServer pid=161) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=161) INFO 12-15 11:44:54 [model.py:547] Resolved architecture: Qwen3ForCausalLM
(APIServer pid=161) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=161) INFO 12-15 11:44:54 [model.py:1510] Using max model len 10000
(APIServer pid=161) INFO 12-15 11:44:54 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=4096.
(APIServer pid=161) INFO 12-15 11:44:54 [__init__.py:381] Cudagraph is disabled under eager mode
(APIServer pid=161) INFO 12-15 11:44:54 [platform.py:152] Compilation disabled, using eager mode by default
(APIServer pid=161) WARNING 12-15 11:44:54 [platform.py:275] If chunked prefill or prefix caching is enabled, block size must be set to 128.
INFO 12-15 11:45:04 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-15 11:45:04 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-15 11:45:04 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-15 11:45:04 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-15 11:45:09 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(EngineCore_DP0 pid=299) INFO 12-15 11:45:09 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:09 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(EngineCore_DP0 pid=299) INFO 12-15 11:45:09 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='Qwen/Qwen3-8B', speculative_config=None, tokenizer='Qwen/Qwen3-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-8B, enable_prefix_caching=False, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
(EngineCore_DP0 pid=299) INFO 12-15 11:45:09 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_DP0 pid=299) INFO 12-15 11:45:11 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=299) INFO 12-15 11:45:12 [factory.py:51] Creating v1 connector with name: MooncakeConnectorV1 and engine_id: 3029508e-1e54-42ec-921d-b052f06f3c19
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:12 [base.py:86] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
WARNING: Logging before InitGoogleLogging() is written to STDERR
I1215 11:45:12.058995   299 transfer_engine.cpp:486] Metrics reporting is disabled (set MC_TE_METRIC=1 to enable)
I1215 11:45:12.059032   299 transfer_engine.cpp:91] Transfer Engine parseHostNameWithPort. server_name: 10.250.40.157 port: 12001
I1215 11:45:12.059199   299 transfer_engine.cpp:146] Transfer Engine RPC using P2P handshake, listening on 10.250.40.157:15308
I1215 11:45:12.059301   299 ascend_direct_transport.cpp:86] install AscendDirectTransport for: 10.250.40.157:15308
I1215 11:45:12.059332   299 ascend_direct_transport.cpp:477] Find available between 20000 and 21000
I1215 11:45:12.059391   299 ascend_direct_transport.cpp:442] AscendDirectTransport set segment desc: host_ip=10.250.40.157, host_port=20266, deviceLogicId=0
I1215 11:45:12.067461   299 ascend_direct_transport.cpp:177] Success to initialize adxl engine:10.250.40.157:20266 with device_id:0
I1215 11:45:12.072492   498 ascend_direct_transport.cpp:512] AscendDirectTransport worker thread started
I1215 11:45:12.072546   299 client_metric.cpp:76] Client metrics enabled (default enabled)
I1215 11:45:12.073642   299 ha_helper.cpp:20] Master view key: mooncake-store/mooncake/master_view
I1215 11:45:12.073658   299 client.cpp:45] client_id=7227224038138927126-8099509819820419468
I1215 11:45:12.073665   299 client.cpp:53] Client metrics enabled but reporting disabled (interval=0)
I1215 11:45:12.077270   299 client.cpp:380] Storage root directory is not set. persisting data is disabled.
I1215 11:45:12.077286   299 client.cpp:403] Use exist transfer engine instance
I1215 11:45:12.091323   299 ascend_direct_transport.cpp:341] AscendDirectTransport register mem addr:0x12c180000000, length:1073741824, location:*, mem type:1
I1215 11:45:12.091395   299 pybind_client.cpp:218] Mounting segment: 42949672960 bytes, 42949672960 of 42949672960
I1215 11:45:12.322327   299 ascend_direct_transport.cpp:341] AscendDirectTransport register mem addr:0x12c1c0000000, length:42949672960, location:*, mem type:1
(EngineCore_DP0 pid=299) INFO 12-15 11:45:12 [model_runner_v1.py:2679] Starting to load model Qwen/Qwen3-8B...
(EngineCore_DP0 pid=299) INFO 12-15 11:45:14 [weight_utils.py:392] Using model weights format ['*.safetensors']
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:01,  2.65it/s]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:00<00:01,  2.39it/s]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:01<00:00,  2.27it/s]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:01<00:00,  2.19it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:02<00:00,  2.66it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:02<00:00,  2.49it/s]
(EngineCore_DP0 pid=299)
(EngineCore_DP0 pid=299) INFO 12-15 11:45:16 [default_loader.py:267] Loading weights took 2.07 seconds
(EngineCore_DP0 pid=299) INFO 12-15 11:45:17 [model_runner_v1.py:2705] Loading model weights took 15.2684 GB
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:18 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [worker_v1.py:256] Available memory: 10701063270, total memory: 31662800896
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [kv_cache_utils.py:1087] GPU KV cache size: 72,448 tokens
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [kv_cache_utils.py:1091] Maximum concurrency for 10,000 tokens per request: 7.16x
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [mooncake_engine.py:102] num_blocks: 566, block_shape: torch.Size([128, 8, 128])
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [mooncake_engine.py:105] Registering KV_Caches. use_mla: False, shape torch.Size([566, 128, 8, 128])
(EngineCore_DP0 pid=299) INFO 12-15 11:45:19 [core.py:210] init engine (profile, create kv cache, warmup model) took 1.96 seconds
(EngineCore_DP0 pid=299) INFO 12-15 11:45:21 [factory.py:51] Creating v1 connector with name: MooncakeConnectorV1 and engine_id: 3029508e-1e54-42ec-921d-b052f06f3c19
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:21 [base.py:86] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
(EngineCore_DP0 pid=299) INFO 12-15 11:45:21 [__init__.py:381] Cudagraph is disabled under eager mode
(EngineCore_DP0 pid=299) INFO 12-15 11:45:21 [platform.py:152] Compilation disabled, using eager mode by default
(EngineCore_DP0 pid=299) WARNING 12-15 11:45:21 [platform.py:275] If chunked prefill or prefix caching is enabled, block size must be set to 128.
(APIServer pid=161) INFO 12-15 11:45:21 [loggers.py:147] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 566
(APIServer pid=161) INFO 12-15 11:45:21 [api_server.py:1634] Supported_tasks: ['generate']
(APIServer pid=161) WARNING 12-15 11:45:21 [model.py:1389] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
(APIServer pid=161) INFO 12-15 11:45:21 [serving_responses.py:137] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=161) INFO 12-15 11:45:22 [serving_chat.py:139] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=161) INFO 12-15 11:45:22 [serving_completion.py:76] Using default completion sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=161) INFO 12-15 11:45:22 [api_server.py:1912] Starting vLLM API server 0 on http://0.0.0.0:8100
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:34] Available routes are:
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /openapi.json, Methods: HEAD, GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /docs, Methods: HEAD, GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /docs/oauth2-redirect, Methods: HEAD, GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /redoc, Methods: HEAD, GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /health, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /load, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /ping, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /ping, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /tokenize, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /detokenize, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/models, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /version, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/responses, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/chat/completions, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/completions, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/embeddings, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /pooling, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /classify, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /score, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/score, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/audio/translations, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /rerank, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v1/rerank, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /v2/rerank, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /invocations, Methods: POST
(APIServer pid=161) INFO 12-15 11:45:22 [launcher.py:42] Route: /metrics, Methods: GET
(APIServer pid=161) INFO:     Started server process [161]
(APIServer pid=161) INFO:     Waiting for application startup.
(APIServer pid=161) INFO:     Application startup complete.
(APIServer pid=161) INFO 12-15 11:46:21 [chat_utils.py:560] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
(EngineCore_DP0 pid=299) INFO 12-15 11:46:21 [mooncake_store_connector_v1.py:217] Reqid: chatcmpl-57f1d4e7-f1f2-4986-877e-e56c901e056f, Total tokens 136, mooncake hit tokens: 0, need to load: 0
(EngineCore_DP0 pid=299) INFO 12-15 11:46:21 [mooncake_engine.py:338] Storing KV cache for 128 out of 128 tokens (skip_leading_tokens=0) for request chatcmpl-57f1d4e7-f1f2-4986-877e-e56c901e056f
I1215 11:46:21.793583   918 pybind_client.cpp:1218] batch_put_from_multi_buffers: 1923us
(EngineCore_DP0 pid=299) INFO 12-15 11:46:21 [mooncake_store_connector_v1.py:428] Delaying free of 2 blocks for request chatcmpl-57f1d4e7-f1f2-4986-877e-e56c901e056f
(APIServer pid=161) INFO:     10.250.40.154:34334 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=161) INFO 12-15 11:46:22 [loggers.py:127] Engine 000: Avg prompt throughput: 13.6 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=161) INFO 12-15 11:46:32 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%

```

**Decode Node log:**
```
INFO 12-15 11:44:44 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-15 11:44:44 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-15 11:44:44 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-15 11:44:44 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
WARNING 12-15 11:44:49 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 12-15 11:44:49 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 12-15 11:44:50 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(APIServer pid=160) INFO 12-15 11:44:50 [api_server.py:1839] vLLM API server version 0.11.0
(APIServer pid=160) INFO 12-15 11:44:50 [utils.py:233] non-default args: {'port': 8200, 'model': 'Qwen/Qwen3-8B', 'trust_remote_code': True, 'max_model_len': 10000, 'enforce_eager': True, 'block_size': 128, 'enable_prefix_caching': False, 'max_num_batched_tokens': 4096, 'kv_transfer_config': KVTransferConfig(kv_connector='MooncakeConnectorStoreV1', engine_id='789c06c9-5f99-48d4-b0a4-82afef5e687c', kv_buffer_device='npu', kv_buffer_size=1000000000.0, kv_role='kv_consumer', kv_rank=None, kv_parallel_size=1, kv_ip='127.0.0.1', kv_port=14579, kv_connector_extra_config={'use_layerwise': False, 'consumer_is_to_load': True, 'prefill': {'dp_size': 1, 'tp_size': 1}, 'decode': {'dp_size': 1, 'tp_size': 1}}, kv_connector_module_path=None)}
(APIServer pid=160) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=160) INFO 12-15 11:44:52 [model.py:547] Resolved architecture: Qwen3ForCausalLM
(APIServer pid=160) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=160) INFO 12-15 11:44:52 [model.py:1510] Using max model len 10000
(APIServer pid=160) INFO 12-15 11:44:52 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=4096.
(APIServer pid=160) INFO 12-15 11:44:52 [__init__.py:381] Cudagraph is disabled under eager mode
(APIServer pid=160) INFO 12-15 11:44:52 [platform.py:152] Compilation disabled, using eager mode by default
(APIServer pid=160) WARNING 12-15 11:44:52 [platform.py:275] If chunked prefill or prefix caching is enabled, block size must be set to 128.
INFO 12-15 11:45:02 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-15 11:45:02 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-15 11:45:02 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-15 11:45:02 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-15 11:45:07 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(EngineCore_DP0 pid=298) INFO 12-15 11:45:07 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:07 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(EngineCore_DP0 pid=298) INFO 12-15 11:45:07 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='Qwen/Qwen3-8B', speculative_config=None, tokenizer='Qwen/Qwen3-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=10000, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-8B, enable_prefix_caching=False, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
(EngineCore_DP0 pid=298) INFO 12-15 11:45:07 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_DP0 pid=298) INFO 12-15 11:45:10 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=298) INFO 12-15 11:45:10 [factory.py:51] Creating v1 connector with name: MooncakeConnectorV1 and engine_id: 789c06c9-5f99-48d4-b0a4-82afef5e687c
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:10 [base.py:86] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
WARNING: Logging before InitGoogleLogging() is written to STDERR
I1215 11:45:10.233269   298 transfer_engine.cpp:486] Metrics reporting is disabled (set MC_TE_METRIC=1 to enable)
I1215 11:45:10.233304   298 transfer_engine.cpp:91] Transfer Engine parseHostNameWithPort. server_name: 10.250.40.162 port: 12001
I1215 11:45:10.233525   298 transfer_engine.cpp:146] Transfer Engine RPC using P2P handshake, listening on 10.250.40.162:15019
I1215 11:45:10.233635   298 ascend_direct_transport.cpp:86] install AscendDirectTransport for: 10.250.40.162:15019
I1215 11:45:10.233672   298 ascend_direct_transport.cpp:477] Find available between 20000 and 21000
I1215 11:45:10.233743   298 ascend_direct_transport.cpp:442] AscendDirectTransport set segment desc: host_ip=10.250.40.162, host_port=20829, deviceLogicId=0
I1215 11:45:10.241544   298 ascend_direct_transport.cpp:177] Success to initialize adxl engine:10.250.40.162:20829 with device_id:0
I1215 11:45:10.245594   497 ascend_direct_transport.cpp:512] AscendDirectTransport worker thread started
I1215 11:45:10.245649   298 client_metric.cpp:76] Client metrics enabled (default enabled)
I1215 11:45:10.246730   298 ha_helper.cpp:20] Master view key: mooncake-store/mooncake/master_view
I1215 11:45:10.246747   298 client.cpp:45] client_id=1244058484768720439-7564156353943805575
I1215 11:45:10.246752   298 client.cpp:53] Client metrics enabled but reporting disabled (interval=0)
I1215 11:45:10.250041   298 client.cpp:380] Storage root directory is not set. persisting data is disabled.
I1215 11:45:10.250059   298 client.cpp:403] Use exist transfer engine instance
I1215 11:45:10.264995   298 ascend_direct_transport.cpp:341] AscendDirectTransport register mem addr:0x12c180000000, length:1073741824, location:*, mem type:1
I1215 11:45:10.265084   298 pybind_client.cpp:218] Mounting segment: 42949672960 bytes, 42949672960 of 42949672960
I1215 11:45:10.502547   298 ascend_direct_transport.cpp:341] AscendDirectTransport register mem addr:0x12c1c0000000, length:42949672960, location:*, mem type:1
(EngineCore_DP0 pid=298) INFO 12-15 11:45:11 [model_runner_v1.py:2679] Starting to load model Qwen/Qwen3-8B...
(EngineCore_DP0 pid=298) INFO 12-15 11:45:12 [weight_utils.py:392] Using model weights format ['*.safetensors']
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:01,  3.10it/s]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:00<00:01,  2.75it/s]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:01<00:00,  2.41it/s]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:01<00:00,  2.18it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:01<00:00,  2.60it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:01<00:00,  2.53it/s]
(EngineCore_DP0 pid=298)
(EngineCore_DP0 pid=298) INFO 12-15 11:45:14 [default_loader.py:267] Loading weights took 2.03 seconds
(EngineCore_DP0 pid=298) INFO 12-15 11:45:15 [model_runner_v1.py:2705] Loading model weights took 15.2684 GB
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:15 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [worker_v1.py:256] Available memory: 10700878950, total memory: 31662800896
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [kv_cache_utils.py:1087] GPU KV cache size: 72,448 tokens
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [kv_cache_utils.py:1091] Maximum concurrency for 10,000 tokens per request: 7.16x
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [mooncake_engine.py:102] num_blocks: 566, block_shape: torch.Size([128, 8, 128])
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [mooncake_engine.py:105] Registering KV_Caches. use_mla: False, shape torch.Size([566, 128, 8, 128])
(EngineCore_DP0 pid=298) INFO 12-15 11:45:17 [core.py:210] init engine (profile, create kv cache, warmup model) took 1.91 seconds
(EngineCore_DP0 pid=298) INFO 12-15 11:45:18 [factory.py:51] Creating v1 connector with name: MooncakeConnectorV1 and engine_id: 789c06c9-5f99-48d4-b0a4-82afef5e687c
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:18 [base.py:86] Initializing KVConnectorBase_V1. This API is experimental and subject to change in the future as we iterate the design.
(EngineCore_DP0 pid=298) INFO 12-15 11:45:18 [__init__.py:381] Cudagraph is disabled under eager mode
(EngineCore_DP0 pid=298) INFO 12-15 11:45:18 [platform.py:152] Compilation disabled, using eager mode by default
(EngineCore_DP0 pid=298) WARNING 12-15 11:45:18 [platform.py:275] If chunked prefill or prefix caching is enabled, block size must be set to 128.
(APIServer pid=160) INFO 12-15 11:45:19 [loggers.py:147] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 566
(APIServer pid=160) INFO 12-15 11:45:19 [api_server.py:1634] Supported_tasks: ['generate']
(APIServer pid=160) WARNING 12-15 11:45:19 [model.py:1389] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
(APIServer pid=160) INFO 12-15 11:45:19 [serving_responses.py:137] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=160) INFO 12-15 11:45:19 [serving_chat.py:139] Using default chat sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=160) INFO 12-15 11:45:20 [serving_completion.py:76] Using default completion sampling params from model: {'temperature': 0.6, 'top_k': 20, 'top_p': 0.95}
(APIServer pid=160) INFO 12-15 11:45:20 [api_server.py:1912] Starting vLLM API server 0 on http://0.0.0.0:8200
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:34] Available routes are:
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /openapi.json, Methods: GET, HEAD
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /docs, Methods: GET, HEAD
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /docs/oauth2-redirect, Methods: GET, HEAD
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /redoc, Methods: GET, HEAD
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /health, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /load, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /ping, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /ping, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /tokenize, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /detokenize, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/models, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /version, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/responses, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/chat/completions, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/completions, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/embeddings, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /pooling, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /classify, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /score, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/score, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/audio/translations, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /rerank, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v1/rerank, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /v2/rerank, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /invocations, Methods: POST
(APIServer pid=160) INFO 12-15 11:45:20 [launcher.py:42] Route: /metrics, Methods: GET
(APIServer pid=160) INFO:     Started server process [160]
(APIServer pid=160) INFO:     Waiting for application startup.
(APIServer pid=160) INFO:     Application startup complete.
(APIServer pid=160) INFO 12-15 11:46:24 [chat_utils.py:560] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
(EngineCore_DP0 pid=298) INFO 12-15 11:46:24 [mooncake_store_connector_v1.py:217] Reqid: chatcmpl-57f1d4e7-f1f2-4986-877e-e56c901e056f, Total tokens 136, mooncake hit tokens: 128, need to load: 128
I1215 11:46:25.724956   497 ascend_direct_transport.cpp:825] Connected to segment: 10.250.40.157:20266
E1215 11:46:28.725225   497 ascend_direct_transport.cpp:611] Transfer slice failed with status: 103901
E1215 11:46:28.725270   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 0 with status 6
E1215 11:46:28.725286   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 1 with status 6
E1215 11:46:28.725291   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 2 with status 6
E1215 11:46:28.725296   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 3 with status 6
E1215 11:46:28.725301   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 4 with status 6
E1215 11:46:28.725304   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 5 with status 6
E1215 11:46:28.725308   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 6 with status 6
E1215 11:46:28.725313   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 7 with status 6
E1215 11:46:28.725317   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 8 with status 6
E1215 11:46:28.725322   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 9 with status 6
E1215 11:46:28.725327   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 10 with status 6
E1215 11:46:28.725330   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 11 with status 6
E1215 11:46:28.725335   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 12 with status 6
E1215 11:46:28.725339   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 13 with status 6
E1215 11:46:28.725343   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 14 with status 6
E1215 11:46:28.725358   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 15 with status 6
E1215 11:46:28.725363   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 16 with status 6
E1215 11:46:28.725366   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 17 with status 6
E1215 11:46:28.725370   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 18 with status 6
E1215 11:46:28.725375   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 19 with status 6
E1215 11:46:28.725379   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 20 with status 6
E1215 11:46:28.725383   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 21 with status 6
E1215 11:46:28.725389   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 22 with status 6
E1215 11:46:28.725392   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 23 with status 6
E1215 11:46:28.725397   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 24 with status 6
E1215 11:46:28.725401   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 25 with status 6
E1215 11:46:28.725406   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 26 with status 6
E1215 11:46:28.725410   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 27 with status 6
E1215 11:46:28.725415   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 28 with status 6
E1215 11:46:28.725419   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 29 with status 6
E1215 11:46:28.725425   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 30 with status 6
E1215 11:46:28.725428   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 31 with status 6
E1215 11:46:28.725435   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 32 with status 6
E1215 11:46:28.725437   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 33 with status 6
E1215 11:46:28.725443   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 34 with status 6
E1215 11:46:28.725447   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 35 with status 6
E1215 11:46:28.725452   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 36 with status 6
E1215 11:46:28.725457   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 37 with status 6
E1215 11:46:28.725462   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 38 with status 6
E1215 11:46:28.725466   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 39 with status 6
E1215 11:46:28.725471   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 40 with status 6
E1215 11:46:28.725476   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 41 with status 6
E1215 11:46:28.725481   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 42 with status 6
E1215 11:46:28.725484   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 43 with status 6
E1215 11:46:28.725488   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 44 with status 6
E1215 11:46:28.725492   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 45 with status 6
E1215 11:46:28.725497   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 46 with status 6
E1215 11:46:28.725502   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 47 with status 6
E1215 11:46:28.725505   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 48 with status 6
E1215 11:46:28.725510   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 49 with status 6
E1215 11:46:28.725514   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 50 with status 6
E1215 11:46:28.725519   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 51 with status 6
E1215 11:46:28.725523   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 52 with status 6
E1215 11:46:28.725528   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 53 with status 6
E1215 11:46:28.725533   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 54 with status 6
E1215 11:46:28.725538   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 55 with status 6
E1215 11:46:28.725541   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 56 with status 6
E1215 11:46:28.725545   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 57 with status 6
E1215 11:46:28.725550   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 58 with status 6
E1215 11:46:28.725554   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 59 with status 6
E1215 11:46:28.725559   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 60 with status 6
E1215 11:46:28.725564   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 61 with status 6
E1215 11:46:28.725569   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 62 with status 6
E1215 11:46:28.725574   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 63 with status 6
E1215 11:46:28.725577   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 64 with status 6
E1215 11:46:28.725581   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 65 with status 6
E1215 11:46:28.725586   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 66 with status 6
E1215 11:46:28.725590   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 67 with status 6
E1215 11:46:28.725595   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 68 with status 6
E1215 11:46:28.725600   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 69 with status 6
E1215 11:46:28.725603   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 70 with status 6
E1215 11:46:28.725608   298 transfer_task.cpp:247] Transfer failed for batch 187651611544208 task 71 with status 6
E1215 11:46:28.725618   298 client.cpp:631] Failed to submit transfer operation for key: Qwen/Qwen3-8B@1@0@4984a94351eefc7e60fc58bdd17fbfb771b5923831216713a351f64ce5dc5746
E1215 11:46:28.725697   298 pybind_client.cpp:1405] BatchGet failed for key 'Qwen/Qwen3-8B@1@0@4984a94351eefc7e60fc58bdd17fbfb771b5923831216713a351f64ce5dc5746': TRANSFER_FAIL
I1215 11:46:28.725769   298 pybind_client.cpp:1276] batch_get_into_multi_buffers: 4178081us
(EngineCore_DP0 pid=298) ERROR 12-15 11:46:28 [mooncake_store.py:84] Failed to get key ['Qwen/Qwen3-8B@1@0@4984a94351eefc7e60fc58bdd17fbfb771b5923831216713a351f64ce5dc5746'],res:[-800]
(APIServer pid=160) INFO 12-15 11:46:30 [loggers.py:127] Engine 000: Avg prompt throughput: 13.6 tokens/s, Avg generation throughput: 3.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.4%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:46:40 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.5%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:46:50 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.6 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.9%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:00 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.1%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:10 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.1 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.2%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:20 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.4 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.6%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:30 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.8 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.8%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:40 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 17.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.9%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:47:50 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 18.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 2.3%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO:     10.250.40.154:34640 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=160) INFO 12-15 11:48:00 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 9.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=160) INFO 12-15 11:48:10 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%

```

I have found similar [issue 4866](https://github.com/vllm-project/vllm-ascend/issues/4866). However, I have already mounted hccn.conf and other ascend files. And the log shows the prefill segment is connectted. 
