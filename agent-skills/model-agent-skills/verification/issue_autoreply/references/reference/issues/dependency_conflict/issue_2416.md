# Issue #2416: [Bug]: [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start.

## 基本信息

- **编号**: #2416
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2416
- **创建时间**: 2025-08-18T07:42:57Z
- **关闭时间**: 2025-08-21T06:49:11Z
- **更新时间**: 2025-10-05T15:23:58Z
- **提交者**: @yangzishy
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `collect_env.py`</summary>

```text
Your output of above commands here
```
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 22.03 (LTS-SP4) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.34

Python version: 3.11.13 (main, Jun  5 2025, 13:03:00) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             128
On-line CPU(s) list:                0-127
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 7260
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 64
Socket(s):                          2
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
L1d cache:                          8 MiB (128 instances)
L1i cache:                          8 MiB (128 instances)
L2 cache:                           64 MiB (128 instances)
L3 cache:                           128 MiB (4 instances)
NUMA node(s):                       4
NUMA node0 CPU(s):                  0-31
NUMA node1 CPU(s):                  32-63
NUMA node2 CPU(s):                  64-95
NUMA node3 CPU(s):                  96-127
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1rc1
[pip3] torchvision==0.22.1
[pip3] transformers==4.53.3
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     27.0.1                   pypi_0    pypi
[conda] torch                     2.7.1                    pypi_0    pypi
[conda] torch-npu                 2.7.1rc1                 pypi_0    pypi
[conda] torchvision               0.22.1                   pypi_0    pypi
[conda] transformers              4.53.3                   pypi_0    pypi
vLLM Version: 0.10.0
vLLM Ascend Version: 0.10.0rc2.dev0+g4604882a3.d20250818 (git sha: 4604882a3, date: 20250818)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=true
ATB_USE_TILING_CACHE=0
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
VLLM_LOGGING_LEVEL=DEBUG
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_ASYNC=0
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.2.0                                   Version: 25.2.0                                       |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 2       310P3                 | OK              | NA           70                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1417 / 44216                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 2       310P3                 | OK              | NA           69                0     / 0             |
| 1       1                     | 0000:01:00.0    | 0            1516 / 43757                            |
+===============================+=================+======================================================+
| 3       310P3                 | OK              | NA           69                0     / 0             |
| 0       2                     | 0000:03:00.0    | 0            1666 / 44216                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 3       310P3                 | OK              | NA           67                0     / 0             |
| 1       3                     | 0000:03:00.0    | 0            1260 / 43757                            |
+===============================+=================+======================================================+
| 5       310P3                 | OK              | NA           72                16    / 16            |
| 0       4                     | 0000:81:00.0    | 0            1691 / 44216                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 5       310P3                 | OK              | NA           69                8     / 8             |
| 1       5                     | 0000:81:00.0    | 0            1381 / 43757                            |
+===============================+=================+======================================================+
| 6       310P3                 | OK              | NA           73                0     / 0             |
| 0       6                     | 0000:84:00.0    | 0            1196 / 44216                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 6       310P3                 | OK              | NA           68                0     / 0             |
| 1       7                     | 0000:84:00.0    | 0            1758 / 43757                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 2                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 3                                                                    |
+===============================+=================+======================================================+
| 5       0                     | 904545          | python3                  | 101                       |
| 5       0                     | 917047          | mindie_llm_back          | 101                       |
| 5       1                     | 904546          | python3                  | 100                       |
+===============================+=================+======================================================+
| No running processes found in NPU 6                                                                    |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux


</details>


### 🐛 Describe the bug

vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B --port 8900 --host 192.168.7.136 --tensor-parallel-size 1 --enforce-eager --dtype float16 --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'

INFO 08-18 15:31:33 [__init__.py:38] Available plugins for group vllm.platform_plugins:
INFO 08-18 15:31:33 [__init__.py:40] - ascend -> vllm_ascend:register
INFO 08-18 15:31:33 [__init__.py:43] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
DEBUG 08-18 15:31:33 [__init__.py:35] Checking if TPU platform is available.
DEBUG 08-18 15:31:33 [__init__.py:45] TPU platform is not available because: No module named 'libtpu'
DEBUG 08-18 15:31:33 [__init__.py:52] Checking if CUDA platform is available.
DEBUG 08-18 15:31:33 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found
DEBUG 08-18 15:31:33 [__init__.py:93] CUDA platform is not available because: NVML Shared Library Not Found
DEBUG 08-18 15:31:33 [__init__.py:100] Checking if ROCm platform is available.
DEBUG 08-18 15:31:33 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi'
DEBUG 08-18 15:31:33 [__init__.py:121] Checking if XPU platform is available.
DEBUG 08-18 15:31:33 [__init__.py:140] XPU platform is not available because: No module named 'intel_extension_for_pytorch'
DEBUG 08-18 15:31:33 [__init__.py:147] Checking if CPU platform is available.
DEBUG 08-18 15:31:33 [__init__.py:169] Checking if Neuron platform is available.
INFO 08-18 15:31:33 [__init__.py:226] Platform plugin ascend is activated
WARNING 08-18 15:31:35 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
DEBUG 08-18 15:31:36 [utils.py:164] Setting VLLM_WORKER_MULTIPROC_METHOD to 'spawn'
DEBUG 08-18 15:31:36 [__init__.py:38] Available plugins for group vllm.general_plugins:
DEBUG 08-18 15:31:36 [__init__.py:40] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver
DEBUG 08-18 15:31:36 [__init__.py:40] - ascend_enhanced_model -> vllm_ascend:register_model
DEBUG 08-18 15:31:36 [__init__.py:43] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 08-18 15:31:38 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
DEBUG 08-18 15:31:38 [decorators.py:139] Inferred dynamic dimensions for forward method of <class 'vllm.model_executor.models.deepseek_v2.DeepseekV2Model'>: ['input_ids', 'positions', 'intermediate_tensors', 'inputs_embeds']
/root/tools/anaconda3/envs/vllm/lib/python3.11/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
WARNING 08-18 15:31:38 [registry.py:430] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 08-18 15:31:38 [registry.py:430] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
DEBUG 08-18 15:31:40 [config.py:2212] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 08-18 15:31:40 [api_server.py:1755] vLLM API server version 0.10.0
INFO 08-18 15:31:40 [cli_args.py:261] non-default args: {'model_tag': '/root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B', 'host': '192.168.7.136', 'port': 8900, 'model': '/root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B', 'dtype': 'float16', 'enforce_eager': True, 'compilation_config': {"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["none","+rms_norm","+rotary_embedding"],"splitting_ops":[],"use_inductor":true,"compile_sizes":null,"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":null,"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":null,"local_cache_dir":null}}
DEBUG 08-18 15:31:53 [config.py:579] Tasks supported by runner type: {'generate': ['generate'], 'pooling': ['encode', 'embed'], 'draft': ['draft']}
DEBUG 08-18 15:31:53 [config.py:586] Selected runner type: generate
WARNING 08-18 15:31:53 [config.py:3443] Casting torch.bfloat16 to torch.float16.
INFO 08-18 15:31:53 [config.py:1604] Using max model len 40960
DEBUG 08-18 15:31:53 [arg_utils.py:1648] Setting max_num_batched_tokens to 2048 for OPENAI_API_SERVER usage context.
DEBUG 08-18 15:31:53 [arg_utils.py:1656] Setting max_num_seqs to 256 for OPENAI_API_SERVER usage context.
DEBUG 08-18 15:31:53 [config.py:2212] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 08-18 15:31:53 [config.py:2434] Chunked prefill is enabled with max_num_batched_tokens=2048.
DEBUG 08-18 15:31:53 [config.py:2212] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 08-18 15:31:53 [platform.py:144] Compilation disabled, using eager mode by default
INFO 08-18 15:32:02 [__init__.py:38] Available plugins for group vllm.platform_plugins:
INFO 08-18 15:32:02 [__init__.py:40] - ascend -> vllm_ascend:register
INFO 08-18 15:32:02 [__init__.py:43] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
DEBUG 08-18 15:32:02 [__init__.py:35] Checking if TPU platform is available.
DEBUG 08-18 15:32:02 [__init__.py:45] TPU platform is not available because: No module named 'libtpu'
DEBUG 08-18 15:32:02 [__init__.py:52] Checking if CUDA platform is available.
DEBUG 08-18 15:32:02 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found
DEBUG 08-18 15:32:02 [__init__.py:93] CUDA platform is not available because: NVML Shared Library Not Found
DEBUG 08-18 15:32:02 [__init__.py:100] Checking if ROCm platform is available.
DEBUG 08-18 15:32:02 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi'
DEBUG 08-18 15:32:02 [__init__.py:121] Checking if XPU platform is available.
DEBUG 08-18 15:32:02 [__init__.py:140] XPU platform is not available because: No module named 'intel_extension_for_pytorch'
DEBUG 08-18 15:32:02 [__init__.py:147] Checking if CPU platform is available.
DEBUG 08-18 15:32:02 [__init__.py:169] Checking if Neuron platform is available.
INFO 08-18 15:32:02 [__init__.py:226] Platform plugin ascend is activated
WARNING 08-18 15:32:04 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
DEBUG 08-18 15:32:04 [utils.py:737] Waiting for 1 local, 0 remote core engine proc(s) to connect.
INFO 08-18 15:32:04 [core.py:572] Waiting for init message from front-end.
DEBUG 08-18 15:32:04 [utils.py:822] HELLO from local core engine process 0.
DEBUG 08-18 15:32:04 [core.py:580] Received init message: EngineHandshakeMetadata(addresses=EngineZmqAddresses(inputs=['ipc:///tmp/1d7db4ad-f47b-46a3-98d2-d6196440a400'], outputs=['ipc:///tmp/b55ec280-d7f2-4132-be76-b42083383c09'], coordinator_input=None, coordinator_output=None, frontend_stats_publish_address=None), parallel_config={'data_parallel_master_ip': '127.0.0.1', 'data_parallel_master_port': 0, 'data_parallel_size': 1})
DEBUG 08-18 15:32:04 [__init__.py:38] Available plugins for group vllm.general_plugins:
DEBUG 08-18 15:32:04 [__init__.py:40] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver
DEBUG 08-18 15:32:04 [__init__.py:40] - ascend_enhanced_model -> vllm_ascend:register_model
DEBUG 08-18 15:32:04 [__init__.py:43] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 08-18 15:32:06 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
DEBUG 08-18 15:32:06 [decorators.py:139] Inferred dynamic dimensions for forward method of <class 'vllm.model_executor.models.deepseek_v2.DeepseekV2Model'>: ['input_ids', 'positions', 'intermediate_tensors', 'inputs_embeds']
/root/tools/anaconda3/envs/vllm/lib/python3.11/site-packages/torch_npu/dynamo/torchair/__init__.py:8: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
WARNING 08-18 15:32:07 [registry.py:430] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 08-18 15:32:07 [registry.py:430] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
INFO 08-18 15:32:07 [core.py:71] Initializing a V1 LLM engine (v0.10.0) with config: model='/root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B', speculative_config=None, tokenizer='/root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/root/.cache/modelscope/hub/models/Qwen/Qwen3-0___6B, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}
DEBUG 08-18 15:32:07 [decorators.py:139] Inferred dynamic dimensions for forward method of <class 'vllm.model_executor.models.llama.LlamaModel'>: ['input_ids', 'positions', 'intermediate_tensors', 'inputs_embeds']
DEBUG 08-18 15:32:07 [decorators.py:139] Inferred dynamic dimensions for forward method of <class 'vllm.model_executor.models.llama_eagle3.LlamaModel'>: ['input_ids', 'positions', 'hidden_states']
DEBUG 08-18 15:32:07 [decorators.py:139] Inferred dynamic dimensions for forward method of <class 'vllm.model_executor.models.minicpm.MiniCPMModel'>: ['input_ids', 'positions', 'intermediate_tensors', 'inputs_embeds']
DEBUG 08-18 15:32:14 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start.
DEBUG 08-18 15:32:24 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start.
DEBUG 08-18 15:32:34 [utils.py:741] Waiting for 1 local, 0 remote core engine proc(s) to start.
