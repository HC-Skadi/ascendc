# Issue #237: [Bug]: RuntimeError: call aclnnSwiGlu failed, detail:EZ1001: [PID: 72153] 2025-03-04-15:41:40.695.851 Get path and read binary_info_config.json failed, please check if the opp_kernel package is installed!

## 基本信息

- **编号**: #237
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/237
- **创建时间**: 2025-03-04T07:54:54Z
- **关闭时间**: 2025-04-10T09:20:00Z
- **更新时间**: 2025-04-10T09:20:00Z
- **提交者**: @YuanEZhou
- **评论数**: 11

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 03-04 15:46:27 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-04 15:46:27 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-04 15:46:27 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-04 15:46:27 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-04 15:46:27 __init__.py:42] plugin ascend loaded.
INFO 03-04 15:46:28 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-04 15:46:28 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-04 15:46:28 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-04 15:46:28 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-04 15:46:28 __init__.py:42] plugin ascend loaded.
INFO 03-04 15:46:28 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-04 15:46:28 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-04 15:46:28 __init__.py:174] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.14.0-115.el7a.0.1.aarch64-aarch64-with-glibc2.35
Is XNNPACK available: True

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
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    1
NUMA node0 CPU(s):               0-191
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Spec store bypass: Not affected
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250218
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.1
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+-------------------------------------------------------------------------------------------+
| npu-smi 23.0.rc1                 Version: 23.0.rc1                                        |
+----------------------+---------------+----------------------------------------------------+
| NPU   Name           | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                 | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+======================+===============+====================================================+
| 2     910ProB        | OK            | 81.1        39                0    / 0             |
| 0                    | 0000:41:00.0  | 0           2322 / 15137      1    / 32768         |
+======================+===============+====================================================+
+----------------------+---------------+----------------------------------------------------+
| NPU     Chip         | Process id    | Process name             | Process memory(MB)      |
+======================+===============+====================================================+
| No running processes found in NPU 2                                                       |
+======================+===============+====================================================+

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

### **Sample**
```
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
llm = LLM(model="./Qwen2.5-0.5B-Instruct")
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")`
```
### 
**Error**
‘’‘
```
root@vllm-ascend-8535-task1-0:/workspace/project/example# python example.py     
INFO 03-04 11:50:55 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-04 11:50:55 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-04 11:50:55 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-04 11:50:55 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-04 11:50:55 __init__.py:42] plugin ascend loaded.
INFO 03-04 11:50:55 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-04 11:50:55 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-04 11:50:55 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-04 11:50:55 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-04 11:50:55 __init__.py:42] plugin ascend loaded.
INFO 03-04 11:50:55 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-04 11:50:55 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-04 11:50:55 __init__.py:174] Platform plugin ascend is activated
INFO 03-04 11:51:09 config.py:526] This model supports multiple tasks: {'reward', 'embed', 'generate', 'classify', 'score'}. Defaulting to 'generate'.
INFO 03-04 11:51:09 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 03-04 11:51:09 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='./Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='./Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=./Qwen2.5-0.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  7.23it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  7.20it/s]

mki_log log dir:/root/atb/log exist
[rank0]:[E304 11:51:28.519999228 compiler_depend.ts:426] setup failed!
Exception raised from OperationSetup at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:111 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0xb8 (0xffff96e6c908 in /usr/local/python3.10/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, char const*) + 0x70 (0xffff96e1b4e0 in /usr/local/python3.10/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x13652b4 (0xfffde3a652b4 in /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x1479524 (0xfffde3b79524 in /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x6c1824 (0xfffde2dc1824 in /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x6c1f90 (0xfffde2dc1f90 in /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x6bf15c (0xfffde2dbf15c in /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x4c9e4c (0xffff96ea9e4c in /usr/local/python3.10/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #8: <unknown function> + 0x7d5b8 (0xffffa186d5b8 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe5edc (0xffffa18d5edc in /lib/aarch64-linux-gnu/libc.so.6)

[rank0]:[W304 11:51:28.655246468 compiler_depend.ts:432] Warning:  (function ExecFuncOpApi)
[rank0]: Traceback (most recent call last):
[rank0]:   File "/workspace/project/example/example.py", line 13, in <module>
[rank0]:     llm = LLM(model="./Qwen2.5-0.5B-Instruct")
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1039, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 240, in __init__
[rank0]:     self.llm_engine = self.engine_class.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 482, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 274, in __init__
[rank0]:     self._initialize_kv_caches()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 414, in _initialize_kv_caches
[rank0]:     self.model_executor.determine_num_available_blocks())
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 99, in determine_num_available_blocks
[rank0]:     results = self.collective_rpc("determine_num_available_blocks")
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 226, in determine_num_available_blocks
[rank0]:     self.model_runner.profile_run()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1357, in profile_run
[rank0]:     self.execute_model(model_input, kv_caches, intermediate_tensors)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 484, in forward
[rank0]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 170, in __call__
[rank0]:     return self.forward(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 346, in forward
[rank0]:     hidden_states, residual = layer(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 255, in forward
[rank0]:     hidden_states = self.mlp(hidden_states)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 94, in forward
[rank0]:     x = self.act_fn(gate_up)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 23, in forward
[rank0]:     return self._forward_method(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/ops/activation.py", line 25, in silu_and_mul_forward_oot
[rank0]:     out = torch_npu.npu_swiglu(x)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
[rank0]:     return self._op(*args, **(kwargs or {}))
[rank0]: RuntimeError: call aclnnSwiGlu failed, detail:EZ1001: [PID: 24244] 2025-03-04-11:51:28.837.824 Get path and read binary_info_config.json failed, please check if the opp_kernel package is installed!
[rank0]:         TraceBack (most recent call last):
[rank0]:         Check NnopbaseCollecterWork(binCollecter.get()) failed
[rank0]:         Assert ((NnopbaseInit()) == 0) failed
[rank0]:         Check NnopbaseCreateExecutorSpace(&executorSpace) failed

[rank0]: [ERROR] 2025-03-04-11:51:28 (PID:24244, Device:0, RankID:-1) ERR01100 OPS call acl api failed
root@vllm-ascend-8535-task1-0:/workspace/project/example# 
’‘’
```


