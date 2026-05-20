# Issue #198: [Bug]: TBE Subprocess Task Distribute Failure When TP>1

## 基本信息

- **编号**: #198
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/198
- **创建时间**: 2025-02-27T17:32:08Z
- **关闭时间**: 2025-04-10T09:17:26Z
- **更新时间**: 2025-06-20T01:42:43Z
- **提交者**: @XuyaoWang
- **评论数**: 7

## 标签

question

## 问题描述

### Your current environment

<details>
<summary>The output of `npu-smi info`</summary>

```text
root@1c518a2e9ee2:/workspace# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.7                   Version: 23.0.7                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 102.8       55                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3338 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 97.6        54                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3337 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 96.5        56                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 108.7       57                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 103.9       58                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 99.3        56                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 107.7       58                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 105.1       59                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3338 / 65536         |
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
```
</details>


<details>
<summary>The output of `cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info`</summary>

```text
root@1c518a2e9ee2:/workspace# cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```
</details>


<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@1c518a2e9ee2:/workspace# python collect_env.py
INFO 02-27 17:19:50 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-27 17:19:50 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-27 17:19:50 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-27 17:19:50 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-27 17:19:50 __init__.py:42] plugin ascend loaded.
INFO 02-27 17:19:51 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-27 17:19:51 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-27 17:19:51 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-27 17:19:51 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-27 17:19:51 __init__.py:42] plugin ascend loaded.
INFO 02-27 17:19:51 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-27 17:19:51 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-27 17:19:51 __init__.py:174] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.139.0.166.oe2203.aarch64-aarch64-with-glibc2.35
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250218
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.1
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```

</details>


### 🐛 Describe the bug

When the tensor parallelism size is greater than 1, that is, when the parameter `tensor_parallel_size` is set to a value greater than 1, the error "TBE Subprocess[task_distribute] raise error[], main process disappeared!" is reported.

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    tensor_parallel_size=2
)
```

```
root@1c518a2e9ee2:/workspace/scripts# python test_qwen_tp.py 
INFO 02-27 17:30:21 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-27 17:30:21 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-27 17:30:21 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-27 17:30:21 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-27 17:30:21 __init__.py:42] plugin ascend loaded.
INFO 02-27 17:30:21 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-27 17:30:21 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-27 17:30:21 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-27 17:30:21 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-27 17:30:21 __init__.py:42] plugin ascend loaded.
INFO 02-27 17:30:21 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-27 17:30:21 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-27 17:30:21 __init__.py:174] Platform plugin ascend is activated
INFO 02-27 17:30:33 config.py:526] This model supports multiple tasks: {'generate', 'reward', 'embed', 'classify', 'score'}. Defaulting to 'generate'.
INFO 02-27 17:30:33 config.py:1383] Defaulting to use mp for distributed inference
INFO 02-27 17:30:33 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 02-27 17:30:33 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='/workspace/models/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='/workspace/models/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/workspace/models/Qwen2.5-0.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
WARNING 02-27 17:30:33 multiproc_worker_utils.py:298] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(VllmWorkerProcess pid=2259) INFO 02-27 17:30:33 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
INFO 02-27 17:30:40 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_f5abf76b'), local_subscribe_port=35617, remote_subscribe_port=None)
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.75it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.74it/s]

/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py:112: UserWarning: HCCL doesn't support gather at the moment. Implemented with allgather instead.
  warnings.warn("HCCL doesn't support gather at the moment. Implemented with allgather instead.")
INFO 02-27 17:30:51 executor_base.py:108] # CPU blocks: 564790, # CPU blocks: 43690
INFO 02-27 17:30:51 executor_base.py:113] Maximum concurrency for 32768 tokens per request: 275.78x
INFO 02-27 17:30:53 llm_engine.py:429] init engine (profile, create kv cache, warmup model) took 11.57 seconds
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
/usr/local/python3.10/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
Exception ignored in: <function LLMEngine.__del__ at 0xfffda85337f0>
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 501, in __del__
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 132, in shutdown
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 139, in close
AttributeError: 'NoneType' object has no attribute 'info'
/usr/local/python3.10/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
