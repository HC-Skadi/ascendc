# Issue #3534: [Bug]: DeepSeek-V3-0324  KeyError: 'model.embed_tokens.weight'  is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"

## 基本信息

- **编号**: #3534
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3534
- **创建时间**: 2025-10-18T13:19:11Z
- **关闭时间**: 2025-10-22T01:33:54Z
- **更新时间**: 2025-10-22T01:33:54Z
- **提交者**: @ZRJ026
- **评论数**: 6

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
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.88.4.ctl3.aarch64-aarch64-with-glibc2.35

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
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.2
[conda] Could not collect
vLLM Version: 0.11.0rc3
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
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
VLLM_USE_V1=1
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
| 0     910B2               | OK            | 95.8        41                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 96.7        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 94.9        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.8        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 103.0       40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 104.1       42                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.7        41                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 95.1        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
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

Run DeepSeek in data parallel (DP) mode on four machines with a total of 32 NPUs.
Docker images: m.daocloud.io/quay.io/ascend/vllm-ascend:v0.11.0rc0
Model: https://modelscope.cn/models/deepseek-ai/DeepSeek-V3-0324

```python
# node0 
vllm serve /data/models --host 0.0.0.0 --port 8004 --data-parallel-size 8 --data-parallel-size-local 2 --data-parallel-address ${HCCL_IF_IP} --data-parallel-rpc-port 13389 --tensor-parallel-size 4 --seed 1024 --served-model-name deepseek_v3  --max-num-seqs  8 --max-model-len 2048 --max-num-batched-tokens 2048 --trust-remote-code --enable-expert-parallel --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

# node1
vllm serve /data/models --host 0.0.0.0 --port 8004 --headless --data-parallel-size 8 --data-parallel-size-local 2 --data-parallel-start-rank 2 --data-parallel-address 172.16.125.137 --data-parallel-rpc-port 13389 --tensor-parallel-size 4 --seed 1024 --served-model-name deepseek_v3 --max-num-seqs 8 --max-model-len 2048 --max-num-batched-tokens 2048 --trust-remote-code --enable-expert-parallel --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

# node2
vllm serve /data/models --host 0.0.0.0 --port 8004 --headless --data-parallel-size 8 --data-parallel-size-local 2 --data-parallel-start-rank 4 --data-parallel-address 172.16.125.137 --data-parallel-rpc-port 13389 --tensor-parallel-size 4 --seed 1024 --served-model-name deepseek_v3 --max-num-seqs 8 --max-model-len 2048 --max-num-batched-tokens 2048 --trust-remote-code --enable-expert-parallel --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

# node3
vllm serve /data/models --host 0.0.0.0 --port 8004 --headless --data-parallel-size 8 --data-parallel-size-local 2 --data-parallel-start-rank 6 --data-parallel-address 172.16.125.137 --data-parallel-rpc-port 13389 --tensor-parallel-size 4 --seed 1024 --served-model-name deepseek_v3 --max-num-seqs 8 --max-model-len 2048 --max-num-batched-tokens 2048 --trust-remote-code --enable-expert-parallel --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

```

node0 output
```shell
INFO 10-18 13:08:44 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-18 13:08:44 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-18 13:08:44 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-18 13:08:44 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-18 13:08:48 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 10-18 13:08:48 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 10-18 13:08:48 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-18 13:08:48 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-18 13:08:48 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-18 13:08:48 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
......
(APIServer pid=9681) INFO 10-18 13:08:49 [api_server.py:1839] vLLM API server version 0.11.0rc3
(APIServer pid=9681) INFO 10-18 13:08:49 [utils.py:233] non-default args: {'model_tag': '/data/models', 'host': '0.0.0.0', 'port': 8004, 'model': '/data/models', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 2048, 'served_model_name': ['deepseek_v3'], 'tensor_parallel_size': 4, 'data_parallel_size': 8, 'data_parallel_size_local': 2, 'data_parallel_address': '172.16.125.137', 'data_parallel_rpc_port': 13389, 'enable_expert_parallel': True, 'gpu_memory_utilization': 0.95, 'enable_prefix_caching': False, 'max_num_batched_tokens': 2048, 'max_num_seqs': 8, 'additional_config': {'ascend_scheduler_config': {'enabled': True}, 'torchair_graph_config': {'enabled': True}}}
(APIServer pid=9681) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
(APIServer pid=9681) INFO 10-18 13:08:49 [config.py:386] Replacing legacy 'type' key with 'rope_type'
(APIServer pid=9681) INFO 10-18 13:08:49 [model.py:547] Resolved architecture: DeepseekV3ForCausalLM
(APIServer pid=9681) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=9681) INFO 10-18 13:08:49 [model.py:1510] Using max model len 2048
(APIServer pid=9681) INFO 10-18 13:08:49 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=9681) INFO 10-18 13:08:49 [platform.py:194] Torchair compilation enabled on NPU. Setting CUDAGraphMode to NONE
(APIServer pid=9681) INFO 10-18 13:08:50 [config.py:386] Replacing legacy 'type' key with 'rope_type'
(APIServer pid=9681) INFO 10-18 13:08:50 [utils.py:651] Started DP Coordinator process (PID: 9817)
INFO 10-18 13:08:58 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-18 13:08:58 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-18 13:08:58 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
......
WARNING 10-18 13:09:03 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-18 13:09:03 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 10-18 13:09:04 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 10-18 13:09:04 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 10-18 13:09:04 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_DP0 pid=9820) INFO 10-18 13:09:04 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP1 pid=9821) INFO 10-18 13:09:04 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP1 pid=9821) WARNING 10-18 13:09:16 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP1 pid=9821) WARNING 10-18 13:09:16 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
(EngineCore_DP1 pid=9821) WARNING 10-18 13:09:16 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
(EngineCore_DP1 pid=9821) WARNING 10-18 13:09:16 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP1 pid=9821) WARNING 10-18 13:09:16 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
......
(EngineCore_DP1 pid=9821) INFO 10-18 13:09:16 [core.py:77] Initializing a V1 LLM engine (v0.11.0rc3) with config: model='/data/models', speculative_config=None, tokenizer='/data/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=8, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=deepseek_v3, enable_prefix_caching=False, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":16,"local_cache_dir":null}
(EngineCore_DP0 pid=9820) WARNING 10-18 13:09:16 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
......
(EngineCore_DP1 pid=9821) INFO 10-18 13:09:16 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1, 2, 3], buffer_handle=(4, 16777216, 10, 'psm_4afd92be'), local_subscribe_addr='ipc:///tmp/868e9679-d722-42ab-8992-ad6e4be34970', remote_subscribe_addr=None, remote_addr_ipv6=False)
(EngineCore_DP0 pid=9820) INFO 10-18 13:09:16 [core.py:77] Initializing a V1 LLM engine (v0.11.0rc3) with config: model='/data/models', speculative_config=None, tokenizer='/data/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=8, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=deepseek_v3, enable_prefix_caching=False, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":16,"local_cache_dir":null}
(EngineCore_DP0 pid=9820) INFO 10-18 13:09:16 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1, 2, 3], buffer_handle=(4, 16777216, 10, 'psm_e042c2b5'), local_subscribe_addr='ipc:///tmp/3929e032-f76a-4d12-9a18-667358201828', remote_subscribe_addr=None, remote_addr_ipv6=False)
......
INFO 10-18 13:09:49 [parallel_state.py:1047] Adjusting world_size=32 rank=1 distributed_init_method=tcp://172.16.125.137:54127 for DP
INFO 10-18 13:09:49 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6ad377e8'), local_subscribe_addr='ipc:///tmp/866ca674-ec8c-4f7d-bab1-34647fc5abf6', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-18 13:09:50 [parallel_state.py:1047] Adjusting world_size=32 rank=3 distributed_init_method=tcp://172.16.125.137:54127 for DP
INFO 10-18 13:09:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_387c8af4'), local_subscribe_addr='ipc:///tmp/10d28665-4b38-4a43-ae55-d7c1e7264075', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-18 13:09:50 [parallel_state.py:1047] Adjusting world_size=32 rank=0 distributed_init_method=tcp://172.16.125.137:54127 for DP
INFO 10-18 13:09:50 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_b907f7bd'), local_subscribe_addr='ipc:///tmp/4586f23f-5ea7-4214-8794-3f5c180c038b', remote_subscribe_addr=None, remote_addr_ipv6=False)
......
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 2 in world size 32 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 4 in world size 32 is assigned as DP rank 1, PP rank 0, TP rank 0, EP rank 4
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 3 in world size 32 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 1 in world size 32 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 5 in world size 32 is assigned as DP rank 1, PP rank 0, TP rank 1, EP rank 5
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 6 in world size 32 is assigned as DP rank 1, PP rank 0, TP rank 2, EP rank 6
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 7 in world size 32 is assigned as DP rank 1, PP rank 0, TP rank 3, EP rank 7
INFO 10-18 13:09:53 [parallel_state.py:1208] rank 0 in world size 32 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
......
(Worker_DP0_TP0_EP0 pid=10242) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP1_TP0_EP4 pid=10236) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
WARNING 10-18 13:09:54 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.torchair.models.torchair_deepseek_mtp:TorchairDeepSeekMTP.
WARNING 10-18 13:09:54 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.torchair.models.torchair_deepseek_v2:TorchairDeepseekV2ForCausalLM.
......
(Worker_DP0_TP3_EP3 pid=10245) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP1_TP3_EP7 pid=10239) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP0_TP2_EP2 pid=10244) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP1_TP2_EP6 pid=10238) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP0_TP1_EP1 pid=10243) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP1_TP1_EP5 pid=10237) INFO 10-18 13:09:54 [model_runner_v1.py:2627] Starting to load model /data/models...
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597] WorkerProc failed to start.
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597] Traceback (most recent call last):
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 437, in __init__
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     self.worker.load_model()
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 291, in load_model
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     self.model_runner.load_model()
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2630, in load_model
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     self.model = get_model(vllm_config=self.vllm_config)
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     return loader.load_model(vllm_config=vllm_config,
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     model = initialize_model(vllm_config=vllm_config,
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     return model_class(vllm_config=vllm_config, prefix=prefix)
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1167, in __init__
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     self.model = TorchairDeepseekV2Model(vllm_config=vllm_config,
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1078, in __init__
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     self.embed_tokens = VocabParallelEmbedding(
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]                         ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py", line 81, in __init__
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     quant_method = quant_config.get_quant_method(self, prefix=prefix)
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 120, in get_quant_method
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     if self.is_layer_skipped_ascend(prefix,
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 152, in is_layer_skipped_ascend
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597]                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=10242) ERROR 10-18 13:09:55 [multiproc_executor.py:597] KeyError: 'model.embed_tokens.weight'
(Worker_DP0_TP0_EP0 pid=10242) INFO 10-18 13:09:55 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP1_EP1 pid=10243) INFO 10-18 13:09:55 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP2_EP2 pid=10244) INFO 10-18 13:09:55 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP1_TP2_EP6 pid=10238) ERROR 10-18 13:09:55 [multiproc_executor.py:597] WorkerProc failed to start.
(Worker_DP1_TP2_EP6 pid=10238) ERROR 10-18 13:09:55 [multiproc_executor.py:597] Traceback (most recent call last):
(Worker_DP1_TP2_EP6 pid=10238) ERROR 10-18 13:09:55 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
```
