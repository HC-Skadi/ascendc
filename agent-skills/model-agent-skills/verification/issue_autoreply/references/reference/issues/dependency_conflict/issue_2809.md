# Issue #2809: [Bug]: 310p vllm 0.9.1 demo测试失败

## 基本信息

- **编号**: #2809
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2809
- **创建时间**: 2025-09-08T08:06:04Z
- **关闭时间**: 2025-12-23T12:04:47Z
- **更新时间**: 2025-12-23T12:04:54Z
- **提交者**: @zhaohaixu
- **评论数**: 3

## 标签

bug; 310p

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
(ascend_vllm) hxzhao@user:~/code$ python collect_env.py
INFO 09-08 07:55:56 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 09-08 07:55:56 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 09-08 07:55:57 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 09-08 07:55:57 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 09-08 07:55:57 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-08 07:55:57 [__init__.py:235] Platform plugin ascend is activated
WARNING 09-08 07:56:01 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 20.04.6 LTS (aarch64)
GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.31

Python version: 3.10.18 (main, Jun  5 2025, 13:08:10) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.4.0-216-generic-aarch64-with-glibc2.31

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             128
On-line CPU(s) list:                0-127
Thread(s) per core:                 1
Core(s) per socket:                 64
Socket(s):                          2
NUMA node(s):                       4
Vendor ID:                          0x48
Model:                              0
Stepping:                           0x1
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
L1d cache:                          8 MiB
L1i cache:                          8 MiB
L2 cache:                           64 MiB
L3 cache:                           128 MiB
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
Vulnerability Spec store bypass:    Vulnerable
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.2
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1
[pip3] torchaudio==2.7.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] numpy                                       1.26.4           pypi_0           pypi
[conda] pyzmq                                       27.0.2           pypi_0           pypi
[conda] torch                                       2.5.1            pypi_0           pypi
[conda] torch-npu                                   2.5.1.post1      pypi_0           pypi
[conda] torchaudio                                  2.7.0            pypi_0           pypi
[conda] torchvision                                 0.20.1           pypi_0           pypi
[conda] transformers                                4.52.4           pypi_0           pypi
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_TOOLKIT_HOME=/home/hxzhao/Ascend/ascend-toolkit/latest
ASCEND_PROCESS_LOG_PATH=/home/hxzhao/ascend
ASCEND_GLOBAL_LOG_LEVEL=1
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/home/hxzhao/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/hxzhao/.local/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/home/hxzhao/.local/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/hxzhao/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/nnal/asdsip/latest//lib:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/lib64:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/hxzhao/miniconda3/envs/ascend_vllm/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/home/hxzhao/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/home/hxzhao/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.1                                 Version: 24.1.0.1                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           56                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1844 / 21527                            |
+===============================+=================+======================================================+
| 32      310P3                 | OK              | NA           58                0     / 0             |
| 0       1                     | 0000:02:00.0    | 0            1846 / 21527                            |
+===============================+=================+======================================================+
| 96      310P3                 | OK              | NA           60                0     / 0             |
| 0       2                     | 0000:04:00.0    | 0            1845 / 21527                            |
+===============================+=================+======================================================+
| 32768   310P3                 | OK              | NA           56                0     / 0             |
| 0       3                     | 0000:81:00.0    | 0            1846 / 21527                            |
+===============================+=================+======================================================+
| 32800   310P3                 | OK              | NA           59                0     / 0             |
| 0       4                     | 0000:82:00.0    | 0            1844 / 21527                            |
+===============================+=================+======================================================+
| 32832   310P3                 | OK              | NA           60                0     / 0             |
| 0       5                     | 0000:83:00.0    | 0            1843 / 21527                            |
+===============================+=================+======================================================+
| 32864   310P3                 | OK              | NA           60                0     / 0             |
| 0       6                     | 0000:84:00.0    | 0            1844 / 21527                            |
+===============================+=================+======================================================+
| 32896   310P3                 | OK              | NA           61                0     / 0             |
| 0       7                     | 0000:85:00.0    | 0            1846 / 21527                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 0                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 32                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 96                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 32768                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32800                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32832                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32864                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32896                                                                |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1.alpha001
innerversion=V100R001C22B041
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1.alpha001/aarch64-linux
```

</details>


### 🐛 Describe the bug

我在310p上在自己的路径下安装了cann 8.1rc1（而不是系统下的8.2rc1），并通过pip安装了
vllm & vllm-ascend，使用example测试时有如下报错，似乎是torch版本的问题？
```
import os
os.environ["VLLM_USE_V1"] = "1"

from vllm.entrypoints.llm import LLM
from vllm.sampling_params import SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="/home/hxzhao//model/Llama-2-7b-hf", dtype="float16")

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```
报错信息如下：
```
(ascend_vllm) hxzhao@user:~/code$ python example.py
INFO 09-08 07:48:14 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 09-08 07:48:14 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 09-08 07:48:16 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 09-08 07:48:16 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 09-08 07:48:16 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-08 07:48:16 [__init__.py:235] Platform plugin ascend is activated
WARNING 09-08 07:48:19 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 09-08 07:48:23 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture Qwen2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2:CustomQwen2ForCausalLM.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-08 07:48:23 [registry.py:401] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
INFO 09-08 07:48:40 [config.py:823] This model supports multiple tasks: {'classify', 'score', 'reward', 'generate', 'embed'}. Defaulting to 'generate'.
WARNING 09-08 07:48:40 [arg_utils.py:1647] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 09-08 07:48:40 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 09-08 07:48:40 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 09-08 07:48:40 [platform.py:135] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
WARNING 09-08 07:48:40 [ascend_config.py:242] ACL Graph is currently experimental. Please raise an issue on https://github.com/vllm-project/vllm-ascend/issues if you encourage any Error
INFO 09-08 07:48:40 [platform.py:235] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 09-08 07:48:40 [utils.py:221] Calculated maximum supported batch sizes for ACL graph: 58
INFO 09-08 07:48:40 [utils.py:236] Adjusted ACL graph batch sizes for LlamaForCausalLM model (layers: 32): 67 → 58 sizes
INFO 09-08 07:48:41 [core.py:455] Waiting for init message from front-end.
INFO 09-08 07:48:41 [platform.py:135] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
WARNING 09-08 07:48:41 [ascend_config.py:242] ACL Graph is currently experimental. Please raise an issue on https://github.com/vllm-project/vllm-ascend/issues if you encourage any Error
INFO 09-08 07:48:41 [platform.py:235] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 09-08 07:48:41 [utils.py:221] Calculated maximum supported batch sizes for ACL graph: 58
INFO 09-08 07:48:41 [utils.py:247] No adjustment needed for ACL graph batch sizes: LlamaForCausalLM model (layers: 32) with 58 sizes
INFO 09-08 07:48:41 [core.py:70] Initializing a V1 LLM engine (v0.9.1) with config: model='/home/hxzhao//model/Llama-2-7b-hf', speculative_config=None, tokenizer='/home/hxzhao//model/Llama-2-7b-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/hxzhao//model/Llama-2-7b-hf, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,472,464,456,448,440,432,416,408,400,392,384,376,360,352,344,336,328,320,312,296,288,280,272,264,256,240,232,224,216,208,200,184,176,168,160,152,144,136,120,112,104,96,88,80,64,56,48,40,32,24,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null}
WARNING 09-08 07:48:42 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xfffdbee16a10>
INFO 09-08 07:48:49 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 09-08 07:49:15 [model_runner_v1.py:1897] Starting to load model /home/hxzhao//model/Llama-2-7b-hf...
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:06<00:06,  6.66s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:09<00:00,  4.55s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:09<00:00,  4.87s/it]

INFO 09-08 07:49:29 [default_loader.py:272] Loading weights took 9.99 seconds
INFO 09-08 07:49:30 [model_runner_v1.py:1912] Loading model weights took 12.5534 GB
.ERROR 09-08 07:49:31 [core.py:515] EngineCore failed to start.
ERROR 09-08 07:49:31 [core.py:515] Traceback (most recent call last):
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2013, in _dispatch_impl
ERROR 09-08 07:49:31 [core.py:515]     r = func(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 716, in __call__
ERROR 09-08 07:49:31 [core.py:515]     return self._op(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515] NotImplementedError: _C::rotary_embedding: attempted to run this operator with Meta tensors, but there was no fake impl or Meta kernel registered. You may have run into this message while using an operator with PT2 compilation APIs (torch.compile/torch.export); in order to use this operator with those APIs you'll need to add a fake impl. Please see the following for next steps:  https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] During handling of the above exception, another exception occurred:
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] Traceback (most recent call last):
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
ERROR 09-08 07:49:31 [core.py:515]     return node.target(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 09-08 07:49:31 [core.py:515]     return self._op(*args, **(kwargs or {}))
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return fn(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
ERROR 09-08 07:49:31 [core.py:515]     return self.dispatch(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
ERROR 09-08 07:49:31 [core.py:515]     return self._cached_dispatch_impl(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
ERROR 09-08 07:49:31 [core.py:515]     output = self._dispatch_impl(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
ERROR 09-08 07:49:31 [core.py:515]     return maybe_run_unsafe_fallback(not_implemented_error)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
ERROR 09-08 07:49:31 [core.py:515]     raise UnsupportedOperatorException(func)
ERROR 09-08 07:49:31 [core.py:515] torch._subclasses.fake_tensor.UnsupportedOperatorException: _C.rotary_embedding.default
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] The above exception was the direct cause of the following exception:
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] Traceback (most recent call last):
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2017, in get_fake_value
ERROR 09-08 07:49:31 [core.py:515]     ret_val = wrap_fake_exception(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1574, in wrap_fake_exception
ERROR 09-08 07:49:31 [core.py:515]     return fn()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2018, in <lambda>
ERROR 09-08 07:49:31 [core.py:515]     lambda: run_node(tx.output, node, args, kwargs, nnmodule)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2150, in run_node
ERROR 09-08 07:49:31 [core.py:515]     raise RuntimeError(make_error_message(e)).with_traceback(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
ERROR 09-08 07:49:31 [core.py:515]     return node.target(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 09-08 07:49:31 [core.py:515]     return self._op(*args, **(kwargs or {}))
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return fn(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
ERROR 09-08 07:49:31 [core.py:515]     return self.dispatch(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
ERROR 09-08 07:49:31 [core.py:515]     return self._cached_dispatch_impl(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
ERROR 09-08 07:49:31 [core.py:515]     output = self._dispatch_impl(func, types, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
ERROR 09-08 07:49:31 [core.py:515]     return maybe_run_unsafe_fallback(not_implemented_error)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
ERROR 09-08 07:49:31 [core.py:515]     raise UnsupportedOperatorException(func)
ERROR 09-08 07:49:31 [core.py:515] RuntimeError: Failed running call_function _C.rotary_embedding(*(FakeTensor(..., device='npu:0', size=(s1,), dtype=torch.int64), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), 128, FakeTensor(..., device='npu:0', size=(4096, 128), dtype=torch.float16), True), **{}):
ERROR 09-08 07:49:31 [core.py:515] _C.rotary_embedding.default
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] During handling of the above exception, another exception occurred:
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] Traceback (most recent call last):
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core
ERROR 09-08 07:49:31 [core.py:515]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 390, in __init__
ERROR 09-08 07:49:31 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 83, in __init__
ERROR 09-08 07:49:31 [core.py:515]     self._initialize_kv_caches(vllm_config)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 141, in _initialize_kv_caches
ERROR 09-08 07:49:31 [core.py:515]     available_gpu_memory = self.model_executor.determine_available_memory()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
ERROR 09-08 07:49:31 [core.py:515]     output = self.collective_rpc("determine_available_memory")
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 09-08 07:49:31 [core.py:515]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/utils.py", line 2671, in run_method
ERROR 09-08 07:49:31 [core.py:515]     return func(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 164, in determine_available_memory
ERROR 09-08 07:49:31 [core.py:515]     self.model_runner.profile_run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1874, in profile_run
ERROR 09-08 07:49:31 [core.py:515]     hidden_states = self._dummy_run(self.max_num_tokens,
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 09-08 07:49:31 [core.py:515]     return func(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1792, in _dummy_run
ERROR 09-08 07:49:31 [core.py:515]     hidden_states = model(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 09-08 07:49:31 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 09-08 07:49:31 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 581, in forward
ERROR 09-08 07:49:31 [core.py:515]     model_output = self.model(input_ids, positions, intermediate_tensors,
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 239, in __call__
ERROR 09-08 07:49:31 [core.py:515]     output = self.compiled_callable(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
ERROR 09-08 07:49:31 [core.py:515]     return fn(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 1269, in __call__
ERROR 09-08 07:49:31 [core.py:515]     return self._torchdynamo_orig_callable(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 526, in __call__
ERROR 09-08 07:49:31 [core.py:515]     return _compile(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 924, in _compile
ERROR 09-08 07:49:31 [core.py:515]     guarded_code = compile_inner(code, one_graph, hooks, transform)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 666, in compile_inner
ERROR 09-08 07:49:31 [core.py:515]     return _compile_inner(code, one_graph, hooks, transform)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_utils_internal.py", line 87, in wrapper_function
ERROR 09-08 07:49:31 [core.py:515]     return function(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 699, in _compile_inner
ERROR 09-08 07:49:31 [core.py:515]     out_code = transform_code_object(code, transform)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/bytecode_transformation.py", line 1322, in transform_code_object
ERROR 09-08 07:49:31 [core.py:515]     transformations(instructions, code_options)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 219, in _fn
ERROR 09-08 07:49:31 [core.py:515]     return fn(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 634, in transform
ERROR 09-08 07:49:31 [core.py:515]     tracer.run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2796, in run
ERROR 09-08 07:49:31 [core.py:515]     super().run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 09-08 07:49:31 [core.py:515]     while self.step():
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 09-08 07:49:31 [core.py:515]     self.dispatch_table[inst.opcode](self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return inner_fn(self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 09-08 07:49:31 [core.py:515]     self.call_function(fn, args, {})
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 09-08 07:49:31 [core.py:515]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return super().call_function(tx, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 09-08 07:49:31 [core.py:515]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 09-08 07:49:31 [core.py:515]     return inline_call(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 09-08 07:49:31 [core.py:515]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 09-08 07:49:31 [core.py:515]     tracer.run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 09-08 07:49:31 [core.py:515]     while self.step():
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 09-08 07:49:31 [core.py:515]     self.dispatch_table[inst.opcode](self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return inner_fn(self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1692, in CALL_FUNCTION_KW
ERROR 09-08 07:49:31 [core.py:515]     self.call_function(fn, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 09-08 07:49:31 [core.py:515]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
ERROR 09-08 07:49:31 [core.py:515]     return getattr(self.realize(), name)(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return super().call_function(tx, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 09-08 07:49:31 [core.py:515]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 09-08 07:49:31 [core.py:515]     return inline_call(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 09-08 07:49:31 [core.py:515]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 09-08 07:49:31 [core.py:515]     tracer.run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 09-08 07:49:31 [core.py:515]     while self.step():
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 09-08 07:49:31 [core.py:515]     self.dispatch_table[inst.opcode](self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return inner_fn(self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 09-08 07:49:31 [core.py:515]     self.call_function(fn, args, {})
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 09-08 07:49:31 [core.py:515]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
ERROR 09-08 07:49:31 [core.py:515]     return getattr(self.realize(), name)(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return super().call_function(tx, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 09-08 07:49:31 [core.py:515]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 09-08 07:49:31 [core.py:515]     return inline_call(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 09-08 07:49:31 [core.py:515]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 09-08 07:49:31 [core.py:515]     tracer.run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 09-08 07:49:31 [core.py:515]     while self.step():
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 09-08 07:49:31 [core.py:515]     self.dispatch_table[inst.opcode](self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return inner_fn(self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1680, in CALL_FUNCTION_EX
ERROR 09-08 07:49:31 [core.py:515]     self.call_function(fn, argsvars.items, kwargsvars)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 09-08 07:49:31 [core.py:515]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 385, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return super().call_function(tx, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return super().call_function(tx, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 09-08 07:49:31 [core.py:515]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 09-08 07:49:31 [core.py:515]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 09-08 07:49:31 [core.py:515]     return inline_call(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 09-08 07:49:31 [core.py:515]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 09-08 07:49:31 [core.py:515]     tracer.run()
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 09-08 07:49:31 [core.py:515]     while self.step():
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 09-08 07:49:31 [core.py:515]     self.dispatch_table[inst.opcode](self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 09-08 07:49:31 [core.py:515]     return inner_fn(self, inst)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 09-08 07:49:31 [core.py:515]     self.call_function(fn, args, {})
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 09-08 07:49:31 [core.py:515]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/torch.py", line 897, in call_function
ERROR 09-08 07:49:31 [core.py:515]     tensor_variable = wrap_fx_proxy(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2037, in wrap_fx_proxy
ERROR 09-08 07:49:31 [core.py:515]     return wrap_fx_proxy_cls(target_cls=TensorVariable, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2124, in wrap_fx_proxy_cls
ERROR 09-08 07:49:31 [core.py:515]     example_value = get_fake_value(proxy.node, tx, allow_non_graph_fake=True)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2064, in get_fake_value
ERROR 09-08 07:49:31 [core.py:515]     unimplemented(
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/exc.py", line 297, in unimplemented
ERROR 09-08 07:49:31 [core.py:515]     raise Unsupported(msg, case_name=case_name)
ERROR 09-08 07:49:31 [core.py:515] torch._dynamo.exc.Unsupported: unsupported operator: _C.rotary_embedding.default (see https://docs.google.com/document/d/1GgvOe7C8_NVOMLOCwDaYV1mXXyHMXY7ExoewHqooxrs/edit#heading=h.64r4npvq0w0 for how to fix)
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] from user code:
ERROR 09-08 07:49:31 [core.py:515]    File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 392, in forward
ERROR 09-08 07:49:31 [core.py:515]     hidden_states, residual = layer(positions, hidden_states, residual)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 305, in forward
ERROR 09-08 07:49:31 [core.py:515]     hidden_states = self.self_attn(positions=positions,
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 202, in forward
ERROR 09-08 07:49:31 [core.py:515]     q, k = self.rotary_emb(positions, q, k)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 24, in forward
ERROR 09-08 07:49:31 [core.py:515]     return self._forward_method(*args, **kwargs)
ERROR 09-08 07:49:31 [core.py:515]   File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/vllm_ascend/ops/rotary_embedding.py", line 54, in rope_forward_oot
ERROR 09-08 07:49:31 [core.py:515]     query, key = torch.ops._C.rotary_embedding(
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515]
ERROR 09-08 07:49:31 [core.py:515] You can suppress this exception and fall back to eager by setting:
ERROR 09-08 07:49:31 [core.py:515]     import torch._dynamo
ERROR 09-08 07:49:31 [core.py:515]     torch._dynamo.config.suppress_errors = True
ERROR 09-08 07:49:31 [core.py:515]
Process EngineCore_0:
Traceback (most recent call last):
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2013, in _dispatch_impl
    r = func(*args, **kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 716, in __call__
    return self._op(*args, **kwargs)
NotImplementedError: _C::rotary_embedding: attempted to run this operator with Meta tensors, but there was no fake impl or Meta kernel registered. You may have run into this message while using an operator with PT2 compilation APIs (torch.compile/torch.export); in order to use this operator with those APIs you'll need to add a fake impl. Please see the following for next steps:  https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
    return node.target(*args, **kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
    return fn(*args, **kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
    return self.dispatch(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
    return self._cached_dispatch_impl(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
    output = self._dispatch_impl(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
    return maybe_run_unsafe_fallback(not_implemented_error)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
    raise UnsupportedOperatorException(func)
torch._subclasses.fake_tensor.UnsupportedOperatorException: _C.rotary_embedding.default

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2017, in get_fake_value
    ret_val = wrap_fake_exception(
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1574, in wrap_fake_exception
    return fn()
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2018, in <lambda>
    lambda: run_node(tx.output, node, args, kwargs, nnmodule)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2150, in run_node
    raise RuntimeError(make_error_message(e)).with_traceback(
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
    return node.target(*args, **kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
    return fn(*args, **kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
    return self.dispatch(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
    return self._cached_dispatch_impl(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
    output = self._dispatch_impl(func, types, args, kwargs)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
    return maybe_run_unsafe_fallback(not_implemented_error)
  File "/home/hxzhao/miniconda3/envs/ascend_vllm/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
    raise UnsupportedOperatorException(func)
RuntimeError: Failed running call_function _C.rotary_embedding(*(FakeTensor(..., device='npu:0', size=(s1,), dtype=torch.int64), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), 128, FakeTensor(..., device='npu:0', size=(4096, 128), dtype=torch.float16), True), **{}):
_C.rotary_embedding.default
```
