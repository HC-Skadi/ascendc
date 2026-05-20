# Issue #361: [Bug]: ERROR 03-19 20:42:17 engine.py:400] Qwen2ForCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'

## 基本信息

- **编号**: #361
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/361
- **创建时间**: 2025-03-19T12:57:46Z
- **关闭时间**: 2025-04-09T16:35:26Z
- **更新时间**: 2025-06-08T13:15:22Z
- **提交者**: @jxc98728
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.11.11 (main, Mar 17 2025, 20:48:11) [GCC 6.3.0 20170516] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35
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
[pip3] transformers==4.49.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.2.1                   pypi_0    pypi
[conda] sentence-transformers     3.3.1                    pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] transformers              4.49.0                   pypi_0    pypi
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

LD_LIBRARY_PATH=/root/vllm-env/lib/python3.11/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/home/ma-user/work/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/ma-user/work/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/ma-user/work/Ascend/ascend-toolkit/latest/lib64:/home/ma-user/work/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/ma-user/work/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/ma-user/work/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_TOOLKIT_HOME=/home/ma-user/work/Ascend/ascend-toolkit/latest
ASCEND_AICPU_PATH=/home/ma-user/work/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/home/ma-user/work/Ascend/ascend-toolkit/latest/opp
ASCEND_HOME_PATH=/home/ma-user/work/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 93.7        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3389 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 88.2        30                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 86.8        30                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 90.9        30                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 90.8        34                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3376 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 88.3        34                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 91.3        33                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 87.2        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3377 / 65536         |
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
None
```

</details>


### 🐛 Describe the bug

```bash
vllm serve /data/model/DeepSeek-R1-Distill-Qwen-7B --max-model-len 16384
```

And the error output:

```bash

ERROR 03-19 20:42:17 engine.py:400] Qwen2ForCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'
ERROR 03-19 20:42:17 engine.py:400] Traceback (most recent call last):
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 03-19 20:42:17 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 03-19 20:42:17 engine.py:400]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 03-19 20:42:17 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 03-19 20:42:17 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
ERROR 03-19 20:42:17 engine.py:400]     self._initialize_kv_caches()
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
ERROR 03-19 20:42:17 engine.py:400]     self.model_executor.determine_num_available_blocks())
ERROR 03-19 20:42:17 engine.py:400]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 03-19 20:42:17 engine.py:400]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 03-19 20:42:17 engine.py:400]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 03-19 20:42:17 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 03-19 20:42:17 engine.py:400]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 03-19 20:42:17 engine.py:400]     return func(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-19 20:42:17 engine.py:400]     return func(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/worker.py", line 219, in determine_num_available_blocks
ERROR 03-19 20:42:17 engine.py:400]     self.model_runner.profile_run()
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-19 20:42:17 engine.py:400]     return func(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner.py", line 966, in profile_run
ERROR 03-19 20:42:17 engine.py:400]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-19 20:42:17 engine.py:400]     return func(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1132, in execute_model
ERROR 03-19 20:42:17 engine.py:400]     hidden_or_intermediate_states = model_executable(
ERROR 03-19 20:42:17 engine.py:400]                                     ^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-19 20:42:17 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400]   File "/root/vllm-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-19 20:42:17 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 03-19 20:42:17 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 03-19 20:42:17 engine.py:400] TypeError: Qwen2ForCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
    self._initialize_kv_caches()
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/worker.py", line 219, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner.py", line 966, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
  File "/root/vllm-env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1132, in execute_model
    hidden_or_intermediate_states = model_executable(
                                    ^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Qwen2ForCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'
Traceback (most recent call last):
  File "/root/vllm-env/bin/vllm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/root/vllm-env/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
    return runner.run(wrapper())
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/root/vllm-env/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/root/.local/share/uv/python/cpython-3.11.11-linux-aarch64-gnu/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/vllm-env/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-03-19-20:42:21 (PID:2571904, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
