# Issue #5813: [Bug]: 部署Qwen3-8B-W8A8  layers.0.mlp.gate_up_proj.deq_scale

## 基本信息

- **编号**: #5813
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5813
- **创建时间**: 2026-01-12T10:02:36Z
- **关闭时间**: 2026-01-15T07:54:21Z
- **更新时间**: 2026-01-15T07:54:21Z
- **提交者**: @impptg
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[root@DS-01 0.13.0]# docker exec -it c8a bash -c "python -m vllm.collect_env"
Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.2.1
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.8.0+cpu
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

==============================
       CUDA / GPU Info
==============================
Is CUDA available            : False
CUDA runtime version         : No CUDA
CUDA_MODULE_LOADING set to   : N/A
GPU models and configuration : No CUDA
Nvidia driver version        : No CUDA
cuDNN version                : No CUDA
HIP runtime version          : N/A
MIOpen runtime version       : N/A
Is XNNPACK available         : True

==============================
          CPU Info
==============================
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
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

==============================
Versions of relevant libraries
==============================
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
vLLM Version                 : 0.13.0
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled
GPU Topology:
  Could not collect

==============================
     Environment Variables
==============================
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
OMP_NUM_THREADS=1
VLLM_PORT=8000
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
```

</details>


### 🐛 Describe the bug

模型地址（官方docs给的）：https://www.modelscope.cn/models/vllm-ascend/Qwen3-8B-W8A8
vllm-ascend版本：0.13.0rc1、0.11.0（都失败，错误一样）
docker-compose.yaml:
```yaml
services:
  vllm-ascend:
    image: quay.io/ascend/vllm-ascend:v0.13.0rc1
    container_name: vllm-ascend-openai
    shm_size: '1g'
    network_mode: host
    # 只映射你想要的两个NPU设备（例如davinci0和davinci1）
    devices:
      - "/dev/davinci0"        # 第一个NPU
      - "/dev/davinci1"
      - "/dev/davinci2"
      - "/dev/davinci3"
      - "/dev/davinci_manager" # 管理设备（必须）
      - "/dev/devmm_svm"       # 内存管理设备（必须）
      - "/dev/hisi_hdc"        # 高速数据传输设备（必须）
    volumes:
      - "/usr/local/dcmi:/usr/local/dcmi"
      - "/usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool"
      - "/usr/local/bin/npu-smi:/usr/local/bin/npu-smi"
      - "/usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/"
      - "/usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info"
      - "/etc/ascend_install.info:/etc/ascend_install.info"
      - "../models/Qwen3-8B-W8A8:/app/model"
      - "./cache:/root/.cache"
    environment:
      - MODEL_PATH=/app/model
      - VLLM_HOST=0.0.0.0
      - VLLM_PORT=8000
      - ASCEND_VISIBLE_DEVICES=0,1,2,3  # 只显示设备0和1
    command: >
      bash -c "
      python -m vllm.entrypoints.api_server 
      --model /app/model 
      --host 0.0.0.0 
      --port 8001
      --served-model-name Qwen3-0.6B
      --tensor-parallel-size 1   # 使用x个NPU
      --device ascend  # 指定使用昇腾设备
      --dtype auto
      --trust-remote-code
      --enable-chunked-prefill
      --disable-log-stats
      --quantization ascenId
      "
    restart:
            unless-stopped
```

异常日志：
```text
(EngineCore_DP0 pid=29) INFO 01-12 09:26:16 [parallel_state.py:1411] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0

[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0

(EngineCore_DP0 pid=29) INFO 01-12 09:26:16 [model_runner_v1.py:2227] Starting to load model /app/model...

(EngineCore_DP0 pid=29) INFO 01-12 09:26:17 [compilation.py:862] Using OOT custom backend for compilation.

(EngineCore_DP0 pid=29) INFO 01-12 09:26:17 [compilation.py:862] Using OOT custom backend for compilation.

Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s]

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] EngineCore failed to start.

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] Traceback (most recent call last):

(EngineCore_DP0 pid=29) Process EngineCore_DP0:

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 857, in run_engine_core

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] engine_core = EngineCoreProc(*args, **kwargs)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] super().__init__(

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 102, in __init__

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self.model_executor = executor_class(vllm_config)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 101, in __init__

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self._init_executor()

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/v1/executor/uniproc_executor.py", line 48, in _init_executor

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self.driver_worker.load_model()

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 355, in load_model

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self.model_runner.load_model()

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2230, in load_model

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self.model = get_model(vllm_config=self.vllm_config)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 132, in get_model

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] return loader.load_model(vllm_config=vllm_config, model_config=model_config)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] self.load_weights(model, model_config)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 305, in load_weights

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] loaded_weights = model.load_weights(self.get_all_weights(model_config, model))

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3.py", line 331, in load_weights

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] return loader.load_weights(weights)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/model_loader/online_quantization.py", line 173, in patched_model_load_weights

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] return original_load_weights(auto_weight_loader, weights, mapper=mapper)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 335, in load_weights

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] autoloaded_weights = set(self._load_module("", self.module, weights))

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 288, in _load_module

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] yield from self._load_module(

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in _load_module

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] loaded_params = module_load_weights(weights)

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 496, in load_weights

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] param = params_dict[name]

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] ~~~~~~~~~~~^^^^^^

(EngineCore_DP0 pid=29) ERROR 01-12 09:26:18 [core.py:866] KeyError: 'layers.0.mlp.gate_up_proj.deq_scale'

(EngineCore_DP0 pid=29) Traceback (most recent call last):

(EngineCore_DP0 pid=29) File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap

(EngineCore_DP0 pid=29) self.run()

(EngineCore_DP0 pid=29) File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run

(EngineCore_DP0 pid=29) self._target(*self._args, **self._kwargs)

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 870, in run_engine_core

(EngineCore_DP0 pid=29) raise e

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 857, in run_engine_core

(EngineCore_DP0 pid=29) engine_core = EngineCoreProc(*args, **kwargs)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__

(EngineCore_DP0 pid=29) super().__init__(

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 102, in __init__

(EngineCore_DP0 pid=29) self.model_executor = executor_class(vllm_config)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 101, in __init__

(EngineCore_DP0 pid=29) self._init_executor()

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/v1/executor/uniproc_executor.py", line 48, in _init_executor

(EngineCore_DP0 pid=29) self.driver_worker.load_model()

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 355, in load_model

(EngineCore_DP0 pid=29) self.model_runner.load_model()

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2230, in load_model

(EngineCore_DP0 pid=29) self.model = get_model(vllm_config=self.vllm_config)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 132, in get_model

(EngineCore_DP0 pid=29) return loader.load_model(vllm_config=vllm_config, model_config=model_config)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 55, in load_model

(EngineCore_DP0 pid=29) self.load_weights(model, model_config)

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/model_loader/default_loader.py", line 305, in load_weights

(EngineCore_DP0 pid=29) loaded_weights = model.load_weights(self.get_all_weights(model_config, model))

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3.py", line 331, in load_weights

(EngineCore_DP0 pid=29) return loader.load_weights(weights)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/model_loader/online_quantization.py", line 173, in patched_model_load_weights

(EngineCore_DP0 pid=29) return original_load_weights(auto_weight_loader, weights, mapper=mapper)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 335, in load_weights

(EngineCore_DP0 pid=29) autoloaded_weights = set(self._load_module("", self.module, weights))

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 288, in _load_module

(EngineCore_DP0 pid=29) yield from self._load_module(

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in _load_module

(EngineCore_DP0 pid=29) loaded_params = module_load_weights(weights)

(EngineCore_DP0 pid=29) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(EngineCore_DP0 pid=29) File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 496, in load_weights

(EngineCore_DP0 pid=29) param = params_dict[name]

(EngineCore_DP0 pid=29) ~~~~~~~~~~~^^^^^^

(EngineCore_DP0 pid=29) KeyError: 'layers.0.mlp.gate_up_proj.deq_scale'

Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:01<?, ?it/s]

(EngineCore_DP0 pid=29) 

Traceback (most recent call last):

File "<frozen runpy>", line 198, in _run_module_as_main

File "<frozen runpy>", line 88, in _run_code

File "/vllm-workspace/vllm/vllm/entrypoints/api_server.py", line 185, in <module>

asyncio.run(run_server(args))

File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 190, in run

return runner.run(main)

^^^^^^^^^^^^^^^^

File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run

return self._loop.run_until_complete(task)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/usr/local/python3.11.13/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete

return future.result()

^^^^^^^^^^^^^^^

File "/vllm-workspace/vllm/vllm/entrypoints/api_server.py", line 133, in run_server

app = await init_app(args, llm_engine)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/vllm-workspace/vllm/vllm/entrypoints/api_server.py", line 116, in init_app

else AsyncLLMEngine.from_engine_args(

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 244, in from_engine_args

return cls(

^^^^

File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__

self.engine_core = EngineCoreClient.make_async_mp_client(

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 121, in make_async_mp_client

return AsyncMPClient(*client_args)

^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 820, in __init__

super().__init__(

File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 477, in __init__

with launch_core_engines(vllm_config, executor_class, log_stats) as (

File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__

next(self.gen)

File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 903, in launch_core_engines

wait_for_engine_startup(

File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 960, in wait_for_engine_startup

raise RuntimeError(

RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_DP0': 1}
```
