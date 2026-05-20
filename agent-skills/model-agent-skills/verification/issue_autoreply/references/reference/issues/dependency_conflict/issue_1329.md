# Issue #1329: [Bug]: vllm-ascend 0.7.3.post1 does not support w8a8 quantization, but 0.9.0rc2 does.

## 基本信息

- **编号**: #1329
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1329
- **创建时间**: 2025-06-20T15:52:57Z
- **关闭时间**: 2025-11-11T07:56:31Z
- **更新时间**: 2025-11-11T07:56:31Z
- **提交者**: @crossxxd
- **评论数**: 3

## 标签

bug; module:mindie-turbo

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.8 (main, Nov 24 2022, 14:06:33) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35

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
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1                    pypi_0    pypi
[conda] torchaudio                2.5.1                    pypi_0    pypi
[conda] torchvision               0.20.1                   pypi_0    pypi
[conda] transformers              4.52.4                   pypi_0    pypi
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3.post1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=4
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
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
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 104.9       50                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
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

</details>


### 🐛 Describe the bug

I attempted to run w8a8 quantization of Qwen2.5 in vllm-ascend 0.7.3.post1 using the following multiple methods, but all failed:
Method 1:
download the official w8a8 model from modelscope [Qwen2.5-0.5B-Instruct-W8A8](https://www.modelscope.cn/models/vllm-ascend/Qwen2.5-0.5B-Instruct-W8A8) and start vllm engine with command：
```
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh
vllm serve vllm-ascend/Qwen2.5-0.5B-Instruct-W8A8
```
I can't start vllm with args ``--quantization ascend``  because vllm-ascend will raise the error like `` invalid choice: 'ascend'``

Method 2:
follow the latest vllm-ascend [document](https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_npu_quantization.html) , install modelslim(checkout modelslim-VLLM-8.1.RC1.b020_001 tag from source) and run the quant command like``python3 quant_qwen.py --model_path Qwen/Qwen2.5-7B-Instruct --save_directory Qwen/Qwen2.5-7B-Instruct-w8a8 --calib_file ../common/boolq.jsonl --w_bit 8 --a_bit 8 --device_type npu --anti_method m1 --trust_remote_code True``. But fail to start vllm with command ``vllm serve Qwen/Qwen2.5-7B-Instruct-w8a8`` and errors are like 
```
INFO 06-20 23:20:11 model_runner.py:902] Starting to load model /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct-w8a8...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
ERROR 06-20 23:20:13 engine.py:400] 'layers.0.mlp.gate_up_proj.deq_scale'
ERROR 06-20 23:20:13 engine.py:400] Traceback (most recent call last):
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 06-20 23:20:13 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 06-20 23:20:13 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 06-20 23:20:13 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
ERROR 06-20 23:20:13 engine.py:400]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 06-20 23:20:13 engine.py:400]     self._init_executor()
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 06-20 23:20:13 engine.py:400]     self.collective_rpc("load_model")
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-20 23:20:13 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 06-20 23:20:13 engine.py:400]     return func(*args, **kwargs)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 207, in load_model
ERROR 06-20 23:20:13 engine.py:400]     self.model_runner.load_model()
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
ERROR 06-20 23:20:13 engine.py:400]     func(self)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 904, in load_model
ERROR 06-20 23:20:13 engine.py:400]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 06-20 23:20:13 engine.py:400]     return loader.load_model(vllm_config=vllm_config)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 409, in load_model
ERROR 06-20 23:20:13 engine.py:400]     loaded_weights = model.load_weights(
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 515, in load_weights
ERROR 06-20 23:20:13 engine.py:400]     return loader.load_weights(weights)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 235, in load_weights
ERROR 06-20 23:20:13 engine.py:400]     autoloaded_weights = set(self._load_module("", self.module, weights))
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 196, in _load_module
ERROR 06-20 23:20:13 engine.py:400]     yield from self._load_module(prefix,
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 173, in _load_module
ERROR 06-20 23:20:13 engine.py:400]     loaded_params = module_load_weights(weights)
ERROR 06-20 23:20:13 engine.py:400]   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 398, in load_weights
ERROR 06-20 23:20:13 engine.py:400]     param = params_dict[name]
ERROR 06-20 23:20:13 engine.py:400] KeyError: 'layers.0.mlp.gate_up_proj.deq_scale'
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/root/miniconda3/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config, )
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
    self.collective_rpc("load_model")
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 207, in load_model
    self.model_runner.load_model()
  File "/root/miniconda3/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
    func(self)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 904, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
    return loader.load_model(vllm_config=vllm_config)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 409, in load_model
    loaded_weights = model.load_weights(
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 515, in load_weights
    return loader.load_weights(weights)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 235, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 196, in _load_module
    yield from self._load_module(prefix,
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 173, in _load_module
    loaded_params = module_load_weights(weights)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 398, in load_weights
    param = params_dict[name]
KeyError: 'layers.0.mlp.gate_up_proj.deq_scale'
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:02<?, ?it/s]

Traceback (most recent call last):
  File "/root/miniconda3/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/root/miniconda3/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/root/miniconda3/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/root/miniconda3/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/root/miniconda3/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-06-20-23:20:22 (PID:2037, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

Method 3:
checkout main branch from msit source, reinstall modelslim. follow [mindie-turbo document](https://www.hiascend.com/document/detail/zh/mindie/20RC1/AcceleratePlugin/turbodev/mindie-turbo-0015.html) and run the quant command like``python3 quant_qwen.py --model_path Qwen/Qwen2.5-7B-Instruct --save_directory Qwen/Qwen2.5-7B-Instruct-w8a8 --calib_file ../common/boolq.jsonl  --device_type npu --disable_level L5 --anti_method m3 --act_method 3``. But still fail to start vllm with command ``vllm serve Qwen/Qwen2.5-7B-Instruct-w8a8`` and errors are the same with Method 2.

Method 4:
checkout main branch from msit source, reinstall modelslim. follow mist official [Qwen example README](https://gitee.com/ascend/msit/tree/master/msmodelslim/example/Qwen) and run the quant command like``python3 quant_qwen.py --model_path Qwen/Qwen2.5-7B-Instruct --save_directory Qwen/Qwen2.5-7B-Instruct-w8a8 --calib_file ../common/boolq.jsonl --w_bit 8 --a_bit 8 --device_type npu --trust_remote_code True``. But still fail to start vllm with command ``vllm serve Qwen/Qwen2.5-7B-Instruct-w8a8`` and errors are the same with Method 2.

By the way, the quantized model generated in Method 2 can be loaded and inferenced normally in vllm-ascend 0.9.0rc2.



