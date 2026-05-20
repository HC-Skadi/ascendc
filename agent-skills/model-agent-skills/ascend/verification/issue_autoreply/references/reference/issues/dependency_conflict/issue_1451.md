# Issue #1451: [Bug]: The allowed number of queries per kv when enabling both MLA and Graph mode only support {32, 64, 128}, Thus this is not supported for DeepSeek-V2-Lite, as it only has 16 attention heads

## 基本信息

- **编号**: #1451
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1451
- **创建时间**: 2025-06-26T08:22:57Z
- **关闭时间**: 2025-12-29T12:46:55Z
- **更新时间**: 2025-12-29T12:46:55Z
- **提交者**: @xxzhang0927
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35

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
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250528
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc1

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
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 91.4        49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3387 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.3        50                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 94.2        49                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 91.6        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 92.1        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 93.8        48                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 89.0        50                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 93.7        49                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3381 / 65536         |
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

</details>


### 🐛 Describe the bug

启动命令：vllm serve /models/DeepSeek-V3 --served-model-name "deepseek-v3" --max-model-len 32000  --trust-remote-code --tensor-parallel-size 8 --pipeline-parallel-size 4 --distributed_executor_backend "ray" --additional-config='{"torchair_graph_config": {"enabled": true},"ascend_scheduler_config": {"enabled": true}}' 

错误信息：
ERROR 06-26 08:18:55 [core.py:515] EngineCore failed to start.
ERROR 06-26 08:18:55 [core.py:515] Traceback (most recent call last):
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 506, in run_engine_core
ERROR 06-26 08:18:55 [core.py:515]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
ERROR 06-26 08:18:55 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.model_executor = executor_class(vllm_config)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 287, in __init__
ERROR 06-26 08:18:55 [core.py:515]     super().__init__(*args, **kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self._init_executor()
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
ERROR 06-26 08:18:55 [core.py:515]     self._init_workers_ray(placement_group)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
ERROR 06-26 08:18:55 [core.py:515]     self._run_workers("load_model",
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 522, in _run_workers
ERROR 06-26 08:18:55 [core.py:515]     ray_worker_outputs = ray.get(ray_worker_outputs)
ERROR 06-26 08:18:55 [core.py:515]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
ERROR 06-26 08:18:55 [core.py:515]     return fn(*args, **kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
ERROR 06-26 08:18:55 [core.py:515]     return func(*args, **kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
ERROR 06-26 08:18:55 [core.py:515]     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
ERROR 06-26 08:18:55 [core.py:515]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
ERROR 06-26 08:18:55 [core.py:515]     raise value.as_instanceof_cause()
ERROR 06-26 08:18:55 [core.py:515] ray.exceptions.RayTaskError(AssertionError): ray::RayWorkerWrapper.execute_method() (pid=1355, ip=10.246.250.20, actor_id=ebfc50cd17be309a3e771cfd02000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfffc2ec46350>)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 623, in execute_method
ERROR 06-26 08:18:55 [core.py:515]     raise e
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 614, in execute_method
ERROR 06-26 08:18:55 [core.py:515]     return run_method(self, method, args, kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
ERROR 06-26 08:18:55 [core.py:515]     return func(*args, **kwargs)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 192, in load_model
ERROR 06-26 08:18:55 [core.py:515]     self.model_runner.load_model()
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1832, in load_model
ERROR 06-26 08:18:55 [core.py:515]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
ERROR 06-26 08:18:55 [core.py:515]     return loader.load_model(vllm_config=vllm_config,
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
ERROR 06-26 08:18:55 [core.py:515]     model = initialize_model(vllm_config=vllm_config,
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
ERROR 06-26 08:18:55 [core.py:515]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 730, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 656, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 626, in make_layers
ERROR 06-26 08:18:55 [core.py:515]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 627, in <listcomp>
ERROR 06-26 08:18:55 [core.py:515]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 658, in <lambda>
ERROR 06-26 08:18:55 [core.py:515]     lambda prefix: CustomDeepseekV2DecoderLayer(
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 532, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.self_attn = attn_cls(
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 430, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.mla_attn = Attention(
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm/vllm/attention/layer.py", line 137, in __init__
ERROR 06-26 08:18:55 [core.py:515]     self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads,
ERROR 06-26 08:18:55 [core.py:515]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/mla_v1.py", line 575, in __init__
ERROR 06-26 08:18:55 [core.py:515]     assert self.num_queries_per_kv in _ALLOWED_NUM_QUERIES_PER_KV, \
ERROR 06-26 08:18:55 [core.py:515] AssertionError: The allowed number of queries per kv when enabling both MLA and Graph mode only support {32, 64, 128}, Thus this is not supported for DeepSeek-V2-Lite, as it only has 16 attention heads. And if you're using DeepSeek-V3 or DeepSeek-R1, please make sure after the tensor parallel split, num_heads / num_kv_heads in {32, 64, 128}.
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 519, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 506, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 287, in __init__
    super().__init__(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
    self._init_workers_ray(placement_group)
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
    self._run_workers("load_model",
  File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 522, in _run_workers
    ray_worker_outputs = ray.get(ray_worker_outputs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
    values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(AssertionError): ray::RayWorkerWrapper.execute_method() (pid=1355, ip=10.246.250.20, actor_id=ebfc50cd17be309a3e771cfd02000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfffc2ec46350>)
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 623, in execute_method
    raise e
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 614, in execute_method
    return run_method(self, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 192, in load_model
    self.model_runner.load_model()
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1832, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
    return loader.load_model(vllm_config=vllm_config,
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
    model = initialize_model(vllm_config=vllm_config,
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
    return model_class(vllm_config=vllm_config, prefix=prefix)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 730, in __init__
    self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
  File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 656, in __init__
    self.start_layer, self.end_layer, self.layers = make_layers(
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 626, in make_layers
    [PPMissingLayer() for _ in range(start_layer)] + [
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 627, in <listcomp>
    maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
  File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 658, in <lambda>
    lambda prefix: CustomDeepseekV2DecoderLayer(
  File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 532, in __init__
    self.self_attn = attn_cls(
  File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 430, in __init__
    self.mla_attn = Attention(
  File "/vllm-workspace/vllm/vllm/attention/layer.py", line 137, in __init__
    self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads,
  File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/mla_v1.py", line 575, in __init__
    assert self.num_queries_per_kv in _ALLOWED_NUM_QUERIES_PER_KV, \
AssertionError: The allowed number of queries per kv when enabling both MLA and Graph mode only support {32, 64, 128}, Thus this is not supported for DeepSeek-V2-Lite, as it only has 16 attention heads. And if you're using DeepSeek-V3 or DeepSeek-R1, please make sure after the tensor parallel split, num_heads / num_kv_heads in {32, 64, 128}.
INFO 06-26 08:18:55 [ray_distributed_executor.py:128] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
