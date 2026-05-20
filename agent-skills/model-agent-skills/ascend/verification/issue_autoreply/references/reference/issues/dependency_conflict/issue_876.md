# Issue #876: [Bug]: Qwen2.5 7B W8A8 KeyError: 'model.layers.0.self_attn.q_proj.weight'

## 基本信息

- **编号**: #876
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/876
- **创建时间**: 2025-05-15T12:10:56Z
- **关闭时间**: 2025-07-13T09:10:29Z
- **更新时间**: 2025-07-13T09:10:29Z
- **提交者**: @Million-mo
- **评论数**: 3

## 标签

bug; module:quantization

## 问题描述

### Your current environment

<details>
<summary>ascen</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.r865_35.hce2.aarch64-aarch64-with-glibc2.35

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
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.post1
vLLM Ascend Version: 0.8.5rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 23.0.6                   Version: 23.0.6                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 85.2        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2802 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
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

ERROR 05-15 11:58:24 [engine.py:448] 'model.layers.0.self_attn.q_proj.weight'
ERROR 05-15 11:58:24 [engine.py:448] Traceback (most recent call last):
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 05-15 11:58:24 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 05-15 11:58:24 [engine.py:448]     return cls(
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self._init_executor()
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 05-15 11:58:24 [engine.py:448]     self.collective_rpc("load_model")
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-15 11:58:24 [engine.py:448]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-15 11:58:24 [engine.py:448]     return func(*args, **kwargs)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-15 11:58:24 [engine.py:448]     self.model_runner.load_model()
ERROR 05-15 11:58:24 [engine.py:448]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
ERROR 05-15 11:58:24 [engine.py:448]     func(self)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
ERROR 05-15 11:58:24 [engine.py:448]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-15 11:58:24 [engine.py:448]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
ERROR 05-15 11:58:24 [engine.py:448]     model = _initialize_model(vllm_config=vllm_config)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
ERROR 05-15 11:58:24 [engine.py:448]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 438, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.model = Qwen2Model(vllm_config=vllm_config,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 305, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
ERROR 05-15 11:58:24 [engine.py:448]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
ERROR 05-15 11:58:24 [engine.py:448]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 307, in <lambda>
ERROR 05-15 11:58:24 [engine.py:448]     lambda prefix: decoder_layer_type(config=config,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 205, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.self_attn = Qwen2Attention(
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 135, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.qkv_proj = QKVParallelLinear(
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 850, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     super().__init__(input_size=input_size,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 396, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     super().__init__(input_size,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 243, in __init__
ERROR 05-15 11:58:24 [engine.py:448]     self.quant_method = quant_config.get_quant_method(self,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 87, in get_quant_method
ERROR 05-15 11:58:24 [engine.py:448]     if self.is_layer_skipped_ascend(prefix,
ERROR 05-15 11:58:24 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 123, in is_layer_skipped_ascend
ERROR 05-15 11:58:24 [engine.py:448]     is_shard_skipped = self.quant_description[shard_prefix +
ERROR 05-15 11:58:24 [engine.py:448] KeyError: 'model.layers.0.self_attn.q_proj.weight'
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 53, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1078, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-05-15-11:58:25 (PID:6688, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@devserver-24ed-0:/vllm-workspace/vllm# /usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
