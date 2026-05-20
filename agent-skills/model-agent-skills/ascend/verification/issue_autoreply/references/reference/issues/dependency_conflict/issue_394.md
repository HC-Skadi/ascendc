# Issue #394: [Bug]: TypeError: Qwen2ForCausalLM.forward() got an unexpected keyword argument 'kv_caches'

## 基本信息

- **编号**: #394
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/394
- **创建时间**: 2025-03-26T02:40:12Z
- **关闭时间**: 2025-03-26T04:23:43Z
- **更新时间**: 2025-03-26T05:20:14Z
- **提交者**: @mapinxue
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 03-26 02:34:58 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-26 02:34:58 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-26 02:34:58 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-26 02:34:58 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-26 02:34:58 [__init__.py:44] plugin ascend loaded.
INFO 03-26 02:34:58 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35

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
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.50.0
[conda] Could not collect
vLLM Version: 0.1.dev1+g4157f56 (git sha: 4157f56)
vLLM Ascend Version: 0.1.dev107+g3fb3b5c.d20250325 (git sha: 3fb3b5c, date: 20250325)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=true
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 92.4        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3577 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.4        36                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3566 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 89.2        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3568 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 95.0        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3565 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.9        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3567 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 94.5        42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3566 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 92.6        40                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3567 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 91.8        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3568 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 1       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 2       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 3       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 4       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 5       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 6       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+
| 7       0                 | 105974        |                          | 106                     |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```

</details>


### 🐛 Describe the bug

# code
```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

# error
```text
INFO 03-26 02:32:23 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-26 02:32:23 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-26 02:32:23 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-26 02:32:23 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-26 02:32:23 [__init__.py:44] plugin ascend loaded.
INFO 03-26 02:32:23 [__init__.py:230] Platform plugin ascend is activated
INFO 03-26 02:32:24 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-26 02:32:24 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-26 02:32:24 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-26 02:32:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-26 02:32:24 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-26 02:32:24 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-26 02:32:25 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-26 02:32:25 [registry.py:366] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-03-26 02:32:27,029 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-26 02:32:27,374 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-03-26 02:32:27,853 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-26 02:32:28,155 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 03-26 02:32:40 [config.py:585] This model supports multiple tasks: {'reward', 'embed', 'score', 'generate', 'classify'}. Defaulting to 'generate'.
WARNING 03-26 02:32:40 [arg_utils.py:1854] device type=npu is not supported by the V1 Engine. Falling back to V0. 
INFO 03-26 02:32:40 [llm_engine.py:241] Initializing a V0 LLM engine (v0.1.dev1+g4157f56) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-03-26 02:32:41,529 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-03-26 02:32:42,634 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-26 02:32:42,963 - modelscope - INFO - Target directory already exists, skipping creation.
/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
    *************************************************************************************************************
    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
    The backend in torch.distributed.init_process_group set to hccl now..
    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
    The device parameters have been replaced with npu in the function below:
    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
    *************************************************************************************************************
    
  warnings.warn(msg, ImportWarning)
/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
WARNING 03-26 02:32:43 [utils.py:2321] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd19e1f970>
INFO 03-26 02:32:52 [parallel_state.py:954] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-03-26 02:32:53,528 - modelscope - INFO - Target directory already exists, skipping creation.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  3.36it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  3.36it/s]

INFO 03-26 02:32:53 [loader.py:447] Loading weights took 0.40 seconds
[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/examples/example.py", line 13, in <module>
[rank0]:     llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1037, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 243, in __init__
[rank0]:     self.llm_engine = LLMEngine.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 520, in from_engine_args
[rank0]:     return engine_cls.from_vllm_config(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 496, in from_vllm_config
[rank0]:     return cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 283, in __init__
[rank0]:     self._initialize_kv_caches()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 432, in _initialize_kv_caches
[rank0]:     self.model_executor.determine_num_available_blocks())
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
[rank0]:     results = self.collective_rpc("determine_num_available_blocks")
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2255, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 227, in determine_num_available_blocks
[rank0]:     self.model_runner.profile_run()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1360, in profile_run
[rank0]:     self.execute_model(model_input, kv_caches, intermediate_tensors)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1140, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]: TypeError: Qwen2ForCausalLM.forward() got an unexpected keyword argument 'kv_caches'
[ERROR] 2025-03-26-02:32:55 (PID:3129, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
