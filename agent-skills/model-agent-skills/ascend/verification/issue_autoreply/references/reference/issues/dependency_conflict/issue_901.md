# Issue #901: [Bug]: VLLM_V1 failed when using ray  distributed_executor_backend in deepseek-R1 W8A8

## 基本信息

- **编号**: #901
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/901
- **创建时间**: 2025-05-19T11:19:55Z
- **关闭时间**: 2025-06-05T09:08:26Z
- **更新时间**: 2025-06-05T09:08:26Z
- **提交者**: @gao12312
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

**update ray package from to 2.45 to  2.46.0 , it seems that  ray  uses  cuda device other than NPU device**  :


The output of `python collect_env.py`

```
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.post1
vLLM Ascend Version: 0.8.5rc2.dev14+g5305a2c (git sha: 5305a2c)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.3                   Version: 23.0.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 96.9        40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 96.3        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 90.3        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.9        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 96.4        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3335 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 94.0        44                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3335 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.4        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3335 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 90.3        43                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3336 / 65536         |
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
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```
command:
```text
 VLLM_USE_V1=1 python -m vllm.entrypoints.openai.api_server --model="/root/models/deepseek_r1_w8a8" --trust-remote-code --enforce-eager --distributed_executor_backend "ray" --tensor-parallel-size 8 --pipeline-parallel-size 2  --max-model-len 4096 --gpu_memory_utilization 0.95 --port 8002 --served-model-name "dpsk-w8a8"
```



### 🐛 Describe the bug




```python
INFO:     Started server process [597187]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO 05-19 09:49:00 [chat_utils.py:397] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
INFO 05-19 09:49:00 [logger.py:39] Received request chatcmpl-d0450f669c6444898daa975997a72078: prompt: '<｜begin▁of▁sentence｜><｜User｜>hello!<｜Assistant｜>', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=1.0, repetition_penalty=1.0, temperature=0.3, top_p=0.95, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=50, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 05-19 09:49:00 [async_llm.py:252] Added request chatcmpl-d0450f669c6444898daa975997a72078.
INFO 05-19 09:49:00 [ray_distributed_executor.py:561] VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE = auto
INFO 05-19 09:49:00 [ray_distributed_executor.py:563] VLLM_USE_RAY_COMPILED_DAG_OVERLAP_COMM = False
INFO 05-19 09:49:00 [ray_distributed_executor.py:578] RAY_CGRAPH_get_timeout is set to 1000
ERROR 05-19 09:49:02 [core.py:398] EngineCore encountered a fatal error.
ERROR 05-19 09:49:02 [core.py:398] Traceback (most recent call last):
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 389, in run_engine_core
ERROR 05-19 09:49:02 [core.py:398]     engine_core.run_busy_loop()
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 413, in run_busy_loop
ERROR 05-19 09:49:02 [core.py:398]     self._process_engine_step()
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 438, in _process_engine_step
ERROR 05-19 09:49:02 [core.py:398]     outputs = self.step_fn()
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 203, in step
ERROR 05-19 09:49:02 [core.py:398]     output = self.model_executor.execute_model(scheduler_output)
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/v1/executor/ray_distributed_executor.py", line 57, in execute_model
ERROR 05-19 09:49:02 [core.py:398]     return refs[0].get()
ERROR 05-19 09:49:02 [core.py:398]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 150, in get
ERROR 05-19 09:49:02 [core.py:398]     return _process_return_vals(return_vals, True)
ERROR 05-19 09:49:02 [core.py:398]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 27, in _process_return_vals
ERROR 05-19 09:49:02 [core.py:398]     raise val.as_instanceof_cause()
ERROR 05-19 09:49:02 [core.py:398] ray.exceptions.RayTaskError(ValueError): ray::RayWorkerWrapper.__ray_call__() (pid=597873, ip=192.168.1.10)
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 130, in execute_model_ray
ERROR 05-19 09:49:02 [core.py:398]     self.setup_device_if_necessary()
ERROR 05-19 09:49:02 [core.py:398]   File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 117, in setup_device_if_necessary
ERROR 05-19 09:49:02 [core.py:398]     torch.cuda.set_device(self.worker.device)
ERROR 05-19 09:49:02 [core.py:398]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/cuda/__init__.py", line 476, in set_device
ERROR 05-19 09:49:02 [core.py:398]     device = _get_device_index(device)
ERROR 05-19 09:49:02 [core.py:398]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/cuda/_utils.py", line 34, in _get_device_index
ERROR 05-19 09:49:02 [core.py:398]     raise ValueError(f"Expected a cuda device, but got: {device}")
ERROR 05-19 09:49:02 [core.py:398] ValueError: Expected a cuda device, but got: npu:0
INFO 05-19 09:49:02 [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
2025-05-19 09:49:02,006 INFO compiled_dag_node.py:2173 -- Tearing down compiled DAG
ERROR 05-19 09:49:02 [async_llm.py:399] AsyncLLM output_handler failed.
ERROR 05-19 09:49:02 [async_llm.py:399] Traceback (most recent call last):
ERROR 05-19 09:49:02 [async_llm.py:399]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 357, in output_handler
ERROR 05-19 09:49:02 [async_llm.py:399]     outputs = await engine_core.get_output_async()
ERROR 05-19 09:49:02 [async_llm.py:399]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 716, in get_output_async
ERROR 05-19 09:49:02 [async_llm.py:399]     raise self._format_exception(outputs) from None
ERROR 05-19 09:49:02 [async_llm.py:399] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
INFO 05-19 09:49:02 [async_llm.py:324] Request chatcmpl-d0450f669c6444898daa975997a72078 failed (engine dead).
INFO:     127.0.0.1:41478 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
2025-05-19 09:49:02,018 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, a76e06f2d7f0bc48de40876101000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 2f6ac9a4a355a2c8be707cd601000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, ecac126f949186ede63dbe9f01000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 5f7f2ea14ae7738a5654864901000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, a4143a4c78567314e582794101000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, d10fbfa00712caf42c844e3401000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 6aefa6693fd44bdb3cdfa71c01000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, f0551ae5d6394550fc9ceb5d01000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, e93de1ab938804e79306f09101000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, f1879b8e576e4db50baa046c01000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, f62679921ab2feef4b1d6bde01000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 970659aa8dbb4d99f233c0d501000000)
2025-05-19 09:49:02,019 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, df364531132a1c69d21c1ffe01000000)
2025-05-19 09:49:02,020 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, fe78b546f5a5c54547ab076e01000000)
2025-05-19 09:49:02,020 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 9e82c9c3d3bd647a9879965b01000000)
2025-05-19 09:49:02,020 INFO compiled_dag_node.py:2178 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, f2bed996c340fd18268a9b9401000000)
2025-05-19 09:49:02,063 INFO compiled_dag_node.py:2200 -- Waiting for worker tasks to exit
2025-05-19 09:49:02,065 INFO compiled_dag_node.py:2203 -- Teardown complete
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 400, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 389, in run_engine_core
    engine_core.run_busy_loop()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 413, in run_busy_loop
    self._process_engine_step()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 438, in _process_engine_step
    outputs = self.step_fn()
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 203, in step
    output = self.model_executor.execute_model(scheduler_output)
  File "/vllm-workspace/vllm/vllm/v1/executor/ray_distributed_executor.py", line 57, in execute_model
    return refs[0].get()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 150, in get
    return _process_return_vals(return_vals, True)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 27, in _process_return_vals
    raise val.as_instanceof_cause()
ray.exceptions.RayTaskError(ValueError): ray::RayWorkerWrapper.__ray_call__() (pid=597873, ip=192.168.1.10)
  File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 130, in execute_model_ray
    self.setup_device_if_necessary()
  File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 117, in setup_device_if_necessary
    torch.cuda.set_device(self.worker.device)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/cuda/__init__.py", line 476, in set_device
    device = _get_device_index(device)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/cuda/_utils.py", line 34, in _get_device_index
    raise ValueError(f"Expected a cuda device, but got: {device}")
ValueError: Expected a cuda device, but got: npu:0
INFO:     Shutting down
(RayWorkerWrapper pid=597889) Exception in thread Thread-1:
(RayWorkerWrapper pid=597889) Traceback (most recent call last):
(RayWorkerWrapper pid=597889)   File "/usr/local/python3.10.17/lib/python3.10/threading.py", line 1016, in _bootstrap_inner
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889)     self.run()
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 91, in run
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889) [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(RayWorkerWrapper pid=597889)     key, func, args, kwargs = self.task_q.get(timeout=TIMEOUT)
(RayWorkerWrapper pid=597889)   File "<string>", line 2, in get
(RayWorkerWrapper pid=597889)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
(RayWorkerWrapper pid=597889)     kind, result = conn.recv()
(RayWorkerWrapper pid=597889)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/connection.py", line 250, in recv
(RayWorkerWrapper pid=597889)     buf = self._recv_bytes()
(RayWorkerWrapper pid=597889)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
(RayWorkerWrapper pid=597889)     buf = self._recv(4)
(RayWorkerWrapper pid=597889)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
(RayWorkerWrapper pid=597889)     raise EOFError
(RayWorkerWrapper pid=597889) EOFError
(RayWorkerWrapper pid=4120, ip=10.151.18.104) [rank10]:[W519 09:48:20.222650460 compiler_depend.ts:26] Warning: Warning: kernel [ArgSort] can not support dtype int32 or int64 on AiCore, Now this kernel is running on AiCpu.If you are more concerned about high-performance execution,please cast dtype to float32. (function operator()) [repeated 15x across cluster]
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [597187]
*** SIGTERM received at time=1747648142 on cpu 3 ***
(raylet) [2025-05-19 09:49:02,102 C 594234 594234] (raylet) experimental_mutable_object_provider.cc:153:  Check failed: object_manager_->WriteAcquire(info.local_object_id, total_data_size, nullptr, total_metadata_size, info.num_readers, object_backing_store) Status not OK: ChannelError: Channel closed. 
(raylet) *** StackTrace Information ***
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0xd1b178) [0xaaaaeafbb178] ray::operator<<()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0xd1daa8) [0xaaaaeafbdaa8] ray::RayLog::~RayLog()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x458a48) [0xaaaaea6f8a48] ray::core::experimental::MutableObjectProvider::HandlePushMutableObject()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x241f00) [0xaaaaea4e1f00] ray::raylet::NodeManager::HandlePushMutableObject()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x2a5530) [0xaaaaea545530] ray::rpc::ServerCallImpl<>::HandleRequestImpl()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x6daa0c) [0xaaaaea97aa0c] EventTracker::RecordExecution()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x6d6140) [0xaaaaea976140] std::_Function_handler<>::_M_invoke()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x6d65d0) [0xaaaaea9765d0] boost::asio::detail::completion_handler<>::do_complete()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0xcf78f0) [0xaaaaeaf978f0] boost::asio::detail::scheduler::do_run_one()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0xcf9b84) [0xaaaaeaf99b84] boost::asio::detail::scheduler::run()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0xcfa188) [0xaaaaeaf9a188] boost::asio::io_context::run()
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x1acec4) [0xaaaaea44cec4] main
(raylet) /lib/aarch64-linux-gnu/libc.so.6(+0x273fc) [0xffff8a9873fc]
(raylet) /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98) [0xffff8a9874cc] __libc_start_main
(raylet) /usr/local/python3.10.17/lib/python3.10/site-packages/ray/core/src/ray/raylet/raylet(+0x1ff62c) [0xaaaaea49f62c]
(raylet) 
PC: @     0xffffb64bea9c  (unknown)  select
    @     0xfffde935b4d8        464  absl::lts_20230802::AbslFailureSignalHandler()
    @     0xffffb69957c0  (unknown)  (unknown)
    @     0xffffb67ed194        128  time_sleep
    @     0xffffb6699d1c        112  cfunction_vectorcall_O
    @     0xffffb65fe64c         48  _PyEval_EvalFrameDefault
    @     0xffffb673df34        448  _PyEval_Vector
    @     0xffffb65f9f58         48  _PyEval_EvalFrameDefault
    @     0xffffb673df34        448  _PyEval_Vector
    @     0xffffb67e870c         48  atexit_callfuncs
    @     0xffffb677dc2c         64  Py_FinalizeEx
    @     0xffffb677ea54         80  Py_Exit
    @     0xffffb6783418         32  _PyErr_PrintEx
    @     0xffffb678409c        144  PyRun_SimpleStringFlags
    @     0xffffb67a333c         32  Py_RunMain
    @     0xffffb67a3d4c        224  Py_BytesMain
    @     0xffffb64073fc        192  (unknown)
    @     0xffffb64074cc        272  __libc_start_main
[2025-05-19 09:49:02,188 E 597629 597629] logging.cc:496: *** SIGTERM received at time=1747648142 on cpu 3 ***
[2025-05-19 09:49:02,188 E 597629 597629] logging.cc:496: PC: @     0xffffb64bea9c  (unknown)  select
[2025-05-19 09:49:02,193 E 597629 597629] logging.cc:496:     @     0xfffde935b500        464  absl::lts_20230802::AbslFailureSignalHandler()
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb69957c0  (unknown)  (unknown)
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb67ed194        128  time_sleep
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb6699d1c        112  cfunction_vectorcall_O
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb65fe64c         48  _PyEval_EvalFrameDefault
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb673df34        448  _PyEval_Vector
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb65f9f58         48  _PyEval_EvalFrameDefault
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb673df34        448  _PyEval_Vector
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb67e870c         48  atexit_callfuncs
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb677dc2c         64  Py_FinalizeEx
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb677ea54         80  Py_Exit
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb6783418         32  _PyErr_PrintEx
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb678409c        144  PyRun_SimpleStringFlags
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb67a333c         32  Py_RunMain
[2025-05-19 09:49:02,196 E 597629 597629] logging.cc:496:     @     0xffffb67a3d4c        224  Py_BytesMain
[2025-05-19 09:49:02,198 E 597629 597629] logging.cc:496:     @     0xffffb64073fc        192  (unknown)
[2025-05-19 09:49:02,198 E 597629 597629] logging.cc:496:     @     0xffffb64074cc        272  __libc_start_main
Exception ignored in atexit callback: <function shutdown at 0xfffde773b250>
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 1957, in shutdown
    time.sleep(0.5)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 1539, in sigterm_handler
    sys.exit(signum)
SystemExit: 15
