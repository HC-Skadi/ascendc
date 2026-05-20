# Issue #3316: [Bug]: v0.11.0rc0不支持Altlas 300I

## 基本信息

- **编号**: #3316
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3316
- **创建时间**: 2025-10-09T02:21:31Z
- **关闭时间**: 2025-12-23T11:20:00Z
- **更新时间**: 2025-12-23T11:20:00Z
- **提交者**: @3892633
- **评论数**: 12

## 标签

bug; 310p

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
python3 collect_env.py
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.3 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.11 (main, Dec 11 2024, 16:19:35) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.15.0-78-generic-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          96
On-line CPU(s) list:             0-95
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       2
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
L1d cache:                       6 MiB (96 instances)
L1i cache:                       6 MiB (96 instances)
L2 cache:                        48 MiB (96 instances)
L3 cache:                        96 MiB (4 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Not affected
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] gpytorch==1.14
[pip3] ktransformers==0.2.1+torch23
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0
[pip3] torch_atb==0.0.1
[pip3] torch_npu==2.8.0rc1
[pip3] torchaudio==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.56.2
[conda] gpytorch                  1.14                     pypi_0    pypi
[conda] ktransformers             0.2.1+torch23            pypi_0    pypi
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     27.1.0                   pypi_0    pypi
[conda] torch                     2.8.0                    pypi_0    pypi
[conda] torch-atb                 0.0.1                    pypi_0    pypi
[conda] torch-npu                 2.8.0rc1                 pypi_0    pypi
[conda] torchaudio                2.8.0                    pypi_0    pypi
[conda] torchvision               0.23.0                   pypi_0    pypi
[conda] transformers              4.56.2                   pypi_0    pypi
vLLM Version: 0.10.2
vLLM Ascend Version: 0.10.2rc2.dev0+g048bfd555.d20250926 (git sha: 048bfd555, date: 20250926)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/nnal/atb/latest/atb/cxx_abi_1/lib:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/nnal/atb/latest/atb/cxx_abi_1/examples:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/tools/aml/lib64:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/lib64:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/lib64/plugin/opskernel:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/lib64/plugin/nnengine:/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/home/h00643489/cann/Ascend_8.3.RC1.alpha002/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.b033                            Version: 25.0.rc1.b033                                |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 1       310P3                 | OK              | NA           52                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1607 / 47304                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 1       310P3                 | OK              | NA           50                0     / 0             |
| 1       1                     | 0000:01:00.0    | 0            1379 / 46717                            |
+===============================+=================+======================================================+
| 2       310P3                 | OK              | NA           58                0     / 0             |
| 0       2                     | 0000:02:00.0    | 0            1866 / 47304                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 2       310P3                 | OK              | NA           51                0     / 0             |
| 1       3                     | 0000:02:00.0    | 0            1116 / 46717                            |
+===============================+=================+======================================================+
| 4       310P3                 | Critical        | NA           56                0     / 0             |
| 0       4                     | 0000:81:00.0    | 0            1793 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 4       310P3                 | OK              | NA           54                0     / 0             |
| 1       5                     | 0000:81:00.0    | 0            1162 / 43693                            |
+===============================+=================+======================================================+
| 5       310P3                 | OK              | NA           56                0     / 0             |
| 0       6                     | 0000:82:00.0    | 0            1665 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 5       310P3                 | OK              | NA           56                0     / 0             |
| 1       7                     | 0000:82:00.0    | 0            1292 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 1                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 2                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 4                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 5                                                                    |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21B054
compatible_version=[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

```text
Your output of above commands here
```

</details>



### 🐛 Describe the bug

vllm serve /home/h00643489/data/Qwen2.5-0.5B-Instruct     --tensor-parallel-size 1     --enforce-eager     --dtype float16     --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
INFO 10-09 01:29:57 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-09 01:29:57 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-09 01:29:57 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-09 01:29:57 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-09 01:30:00 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory')
WARNING 10-09 01:30:01 [registry.py:483] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
WARNING 10-09 01:30:01 [registry.py:483] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:Qwen3NextForCausalLM.
INFO 10-09 01:30:01 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(APIServer pid=6624) INFO 10-09 01:30:01 [api_server.py:1896] vLLM API server version 0.10.2
(APIServer pid=6624) INFO 10-09 01:30:01 [utils.py:328] non-default args: {'model_tag': '/home/h00643489/data/Qwen2.5-0.5B-Instruct', 'model': '/home/h00643489/data/Qwen2.5-0.5B-Instruct', 'dtype': 'float16', 'enforce_eager': True, 'compilation_config': {"level":null,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["none","+rms_norm","+rotary_embedding"],"splitting_ops":null,"use_inductor":true,"compile_sizes":null,"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":null,"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":null,"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":null,"local_cache_dir":null}}
(APIServer pid=6624) INFO 10-09 01:30:17 [__init__.py:742] Resolved architecture: Qwen2ForCausalLM
(APIServer pid=6624) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=6624) INFO 10-09 01:30:17 [__init__.py:1815] Using max model len 32768
(APIServer pid=6624) INFO 10-09 01:30:18 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=6624) INFO 10-09 01:30:18 [platform.py:137] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
(APIServer pid=6624) INFO 10-09 01:30:18 [platform.py:175] Compilation disabled, using eager mode by default
(APIServer pid=6624) WARNING 10-09 01:30:18 [platform.py:193] compilation_config.level = CompilationLevel.NO_COMPILATION is set, Setting CUDAGraphMode to NONE
INFO 10-09 01:30:30 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-09 01:30:30 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-09 01:30:30 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-09 01:30:30 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-09 01:30:33 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory')
(EngineCore_DP0 pid=6903) INFO 10-09 01:30:33 [core.py:654] Waiting for init message from front-end.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
(EngineCore_DP0 pid=6903) WARNING 10-09 01:30:33 [registry.py:483] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:Qwen3NextForCausalLM.
(EngineCore_DP0 pid=6903) INFO 10-09 01:30:33 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='/home/h00643489/data/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='/home/h00643489/data/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/h00643489/data/Qwen2.5-0.5B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["none","+rms_norm","+rotary_embedding"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
(EngineCore_DP0 pid=6903) INFO 10-09 01:30:34 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 10-09 01:30:56 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-09 01:30:56 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-09 01:30:56 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-09 01:30:56 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-09 01:30:59 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory')
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:02 [parallel_state.py:1165] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:05 [model_runner_v1.py:2345] Starting to load model /home/h00643489/data/Qwen2.5-0.5B-Instruct...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.67s/it]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.67s/it]
(EngineCore_DP0 pid=6903)
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:07 [default_loader.py:268] Loading weights took 1.72 seconds
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:09 [model_runner_v1.py:2373] Loading model weights took 0.9299 GB
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:14 [worker_v1.py:198] Available memory: 40178937036, total memory: 49602220032
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:14 [kv_cache_utils.py:864] GPU KV cache size: 3,269,760 tokens
(EngineCore_DP0 pid=6903) INFO 10-09 01:31:14 [kv_cache_utils.py:868] Maximum concurrency for 32,768 tokens per request: 99.79x
[rank0]:[W1009 01:31:14.941463170 compiler_depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operator())
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] EngineCore failed to start.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] Traceback (most recent call last):
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 91, in __init__
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 215, in _initialize_kv_caches
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 72, in initialize_from_config
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     self.collective_rpc("initialize_from_config",
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     return func(*args, **kwargs)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 606, in initialize_from_config
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/home/h00643489/codes/vllm-ascend_v0.10.2rc1/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     self.model_runner.initialize_kv_cache(kv_cache_config)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/home/h00643489/codes/vllm-ascend_v0.10.2rc1/vllm_ascend/worker/model_runner_v1.py", line 2396, in initialize_kv_cache
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/home/h00643489/codes/vllm-ascend_v0.10.2rc1/vllm_ascend/worker/model_runner_v1.py", line 2579, in initialize_kv_cache_tensors
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     kv_cache = self._convert_torch_format(kv_cache)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/home/h00643489/codes/vllm-ascend_v0.10.2rc1/vllm_ascend/worker/model_runner_v1.py", line 2377, in _convert_torch_format
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     tensor = torch_npu.npu_format_cast(tensor, ACL_FORMAT)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   File "/root/anaconda3/envs/hwd_t280/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     return self._op(*args, **kwargs)
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] [ERROR] 2025-10-09-01:31:16 (PID:6903, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] [Error]: System Direct Memory Access (DMA) hardware execution error.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         Rectify the fault based on the error information in the ascend log.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] EL0004: [PID: 6903] 2025-10-09-01:31:15.131.349 Failed to allocate memory.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         Possible Cause: Available memory is insufficient.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         Solution: Close applications not in use.
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         TraceBack (most recent call last):
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         The error from device(0), serial number is 1. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         Memory async copy failed, device_id=0, stream_id=2, task_id=2114, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=3348234240[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] DEVICE[0] PID[6903]:
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] SYSTEM ERROR:
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   Exception info:
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]   Message info[0]:
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718]     Other info[0]:time=, function=, line=0, error code=0
(EngineCore_DP0 pid=6903) ERROR 10-09 01:31:16 [core.py:718] SYSTEM ERROR:


