# Issue #4009: [Bug]: Qwen/Qwen3-Omni-30B-A3B-Instruct 推理异常

## 基本信息

- **编号**: #4009
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4009
- **创建时间**: 2025-11-05T09:20:01Z
- **关闭时间**: 2025-11-08T01:45:39Z
- **更新时间**: 2025-11-11T10:11:08Z
- **提交者**: @sleepy-dev-bin
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
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov  2 2025, 08:46:33) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.35

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
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc4
vLLM Ascend Version: 0.1.dev1+g3ac76fdcc.d20251105 (git sha: 3ac76fdcc, date: 20251105)

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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| 0     910B4               | OK            | 85.6        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2857 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 87.5        39                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2854 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 85.3        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2854 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 85.6        38                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2854 / 32768         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

```PYTHON
from vllm import LLM, SamplingParams
import librosa
MODEL_PATH = "Qwen3-Omni-30B-A3B-Instruct"
llm = LLM(
        model=MODEL_PATH, trust_remote_code=True, gpu_memory_utilization=0.95,
        tensor_parallel_size=4,
        limit_mm_per_prompt={'image': 3, 'video': 3, 'audio': 3},
        max_num_seqs=8,
        max_model_len=4096,
        seed=1234,
)
SAMPLE_RATE=16000

audio_path = 'zh2en-08-sci_10.wav'
wave_data, sr = librosa.load(audio_path, sr=SAMPLE_RATE)

text = '<|im_start|>user\n<|audio_start|><|audio_pad|><|audio_end|>请将这段语音转换为纯文本。<|im_end|>\n<|im_start|>assistant\n'

inputs = {
    'prompt': text,
    'multi_modal_data': {
        'audio': [wave_data]
    },
    "mm_processor_kwargs": {
        "use_audio_in_video": True,
    },
}


sampling_params = SamplingParams(
    temperature=1e-2,
    top_p=0.1,
    top_k=1,
    max_tokens=int(wave_data.shape[0] * 1.0 / SAMPLE_RATE * 8),
)

outputs = llm.generate([inputs,], sampling_params=sampling_params)
```

```ERROR
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] WorkerProc hit an exception.
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] WorkerProc hit an exception.
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703] WorkerProc hit an exception.
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP3 pid=7301) ERROR 11-05 09:18:38 [multiproc_executor.py:703] 
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP0 pid=7286) ERROR 11-05 09:18:38 [multiproc_executor.py:703] 
(EngineCore_DP0 pid=7279) (Worker_TP2 pid=7296) ERROR 11-05 09:18:38 [multiproc_executor.py:703]
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.11.1rc4) with config: model='/data/libin/models/Qwen3-Omni-30B-A3B-Instruct', speculative_config=None, tokenizer='/data/libin/models/Qwen3-Omni-30B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1234, served_model_name=/data/libin/models/Qwen3-Omni-30B-A3B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={'level': None, 'mode': 3, 'debug_dump_path': None, 'cache_dir': '', 'backend': 'eager', 'custom_ops': ['all'], 'splitting_ops': ['vllm::unified_attention', 'vllm::unified_attention_with_output', 'vllm::unified_mla_attention', 'vllm::unified_mla_attention_with_output', 'vllm::mamba_mixer2', 'vllm::mamba_mixer', 'vllm::short_conv', 'vllm::linear_attention', 'vllm::plamo2_mamba_mixer', 'vllm::gdn_attention', 'vllm::sparse_attn_indexer', 'vllm::mla_forward', 'vllm::mla_forward'], 'use_inductor': False, 'compile_sizes': [], 'inductor_compile_config': {'enable_auto_functionalized_v2': False}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.PIECEWISE: 1>, 'use_cudagraph': True, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16], 'cudagraph_copy_inputs': False, 'full_cuda_graph': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {}, 'max_cudagraph_capture_size': 16, 'local_cache_dir': None}, 
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] WorkerProc hit an exception.
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/worker/worker_base.py", line 351, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return func(*args, **kwargs)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2294, in execute_model
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1630, in _prepare_inputs
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1090, in _execute_mm_encoder
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1277, in get_multimodal_embeddings
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_embeddings = self._process_audio_input(multimodal_input)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1067, in _process_audio_input
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     audio_feature_lengths = flatten_bn(audio_feature_lengths, concat=True)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/model_executor/models/utils.py", line 390, in flatten_bn
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]     return x.flatten(0, 1)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703]            ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] IndexError: Dimension out of range (expected to be in range of [-1, 0], but got 1)
(EngineCore_DP0 pid=7279) (Worker_TP1 pid=7290) ERROR 11-05 09:18:38 [multiproc_executor.py:703] 
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids_len=225,mm_features=[MultiModalFeatureSpec(data={'input_audio_features': MultiModalFieldElem(modality='audio', key='input_audio_features', data=tensor([[-0.5430, -0.3730, -0.5820,  ..., -0.2432, -0.1152, -0.1094],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         [-0.4453, -0.2754, -0.4863,  ..., -0.1455, -0.0175, -0.0117],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         [-0.4551, -0.5391, -0.2852,  ..., -0.1084, -0.0212, -0.0859],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         ...,
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         [-0.6367, -0.6367, -0.6367,  ..., -0.6367, -0.6367, -0.6367],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         [-0.6367, -0.6367, -0.6367,  ..., -0.6367, -0.6367, -0.6367],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]         [-0.6367, -0.6367, -0.6367,  ..., -0.6367, -0.6367, -0.6367]],
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [dump_input.py:79]        dtype=torch.bfloat16), field=MultiModalFlatField(slices=[[slice(None, None, None), slice(0, 1395, None)]], dim=1)), 'audio_feature_lengths': MultiModalFieldElem(modality='audio', key='audio_feature_lengths', data=tensor(1395), field=MultiModalBatchedField()), 'feature_attention_mask': MultiModalFieldElem(modality='audio', key='feature_attention_mask', data=tensor([1., 1., 1.,  ..., 1., 1., 1.]), field=MultiModalBatchedField())}, modality='audio', identifier='44e68f039194baf98bbd0b7f1980da96e3cd1fb8ba8e3c986a6c000f40969953', mm_position=PlaceholderRange(offset=4, length=181, is_embed=None))],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.01, top_p=0.1, top_k=1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=111, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None),block_ids=([1, 2],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], resumed_req_token_ids=[], new_block_ids=[], num_computed_tokens=[], num_output_tokens=[]), num_scheduled_tokens={0: 225}, total_num_scheduled_tokens=225, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={0: [0]}, num_common_prefix_blocks=[2], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids=[], grammar_bitmask=null, kv_connector_metadata=null)
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781] Traceback (most recent call last):
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 772, in run_engine_core
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 799, in run_busy_loop
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     self._process_engine_step()
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 828, in _process_engine_step
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 318, in step
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     model_output = self.model_executor.execute_model(scheduler_output)
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 189, in execute_model
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     (output,) = self.collective_rpc(
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]                 ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 287, in collective_rpc
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     result = get_response(w, dequeue_timeout, self.shutdown_event)
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 268, in get_response
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781]     raise RuntimeError(
(EngineCore_DP0 pid=7279) ERROR 11-05 09:18:38 [core.py:781] RuntimeError: Worker failed with error 'Dimension out of range (expected to be in range of [-1, 0], but got 1)', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/data/libin/omni_demo.py", line 42, in <module>
    outputs = llm.generate([inputs,], sampling_params=sampling_params)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 441, in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 1723, in _run_engine
    step_outputs = self.llm_engine.step()
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/llm_engine.py", line 295, in step
    outputs = self.engine_core.get_output()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 708, in get_output
    raise self._format_exception(outputs) from None
vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
[ERROR] 2025-11-05-09:18:39 (PID:7142, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
```
