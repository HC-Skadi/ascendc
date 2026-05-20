# Issue #592: [Bug]: 0.8.4rc1 version  Lora/MultiLora ERROR

## 基本信息

- **编号**: #592
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/592
- **创建时间**: 2025-04-21T06:55:45Z
- **关闭时间**: 2025-04-22T02:44:10Z
- **更新时间**: 2025-04-22T03:06:40Z
- **提交者**: @zhz292
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 04-21 06:52:40 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-21 06:52:40 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-21 06:52:40 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-21 06:52:40 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-21 06:52:40 [__init__.py:44] plugin ascend loaded.
INFO 04-21 06:52:40 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-119-generic-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
Model name:                           Kunpeng-920
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
Frequency boost:                      disabled
CPU max MHz:                          2600.0000
CPU min MHz:                          200.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                            12 MiB (192 instances)
L1i cache:                            12 MiB (192 instances)
L2 cache:                             96 MiB (192 instances)
L3 cache:                             192 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-23
NUMA node1 CPU(s):                    24-47
NUMA node2 CPU(s):                    48-71
NUMA node3 CPU(s):                    72-95
NUMA node4 CPU(s):                    96-119
NUMA node5 CPU(s):                    120-143
NUMA node6 CPU(s):                    144-167
NUMA node7 CPU(s):                    168-191
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.4
vLLM Ascend Version: 0.8.4rc1

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
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 99.6        42                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 95.9        39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 96.1        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          56631/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 96.6        41                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          56631/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 101.8       47                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          64750/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 100.5       44                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          64749/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 98.8        44                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          64750/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 94.1        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          64751/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| 2       0                 | 1036531       |                          | 53312                   |
+===========================+===============+====================================================+
| 3       0                 | 1036533       |                          | 53312                   |
+===========================+===============+====================================================+
| 4       0                 | 2729266       |                          | 61430                   |
+===========================+===============+====================================================+
| 5       0                 | 2729268       |                          | 61430                   |
+===========================+===============+====================================================+
| 6       0                 | 2729275       |                          | 61430                   |
+===========================+===============+====================================================+
| 7       0                 | 2729282       |                          | 61429                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
****
```

</details>


### 🐛 Describe the bug

## Serving LoRA Adapters

```
vllm serve /data/models/DeepSeek-R1-Distill-Qwen-32B/ --served-model-name DeepSeek-R1-Distill-Qwen-32B --trust-remote-code --tensor-parallel-size 2 --max-model-len 8000 --port 30000  --enable-lora --max-loras 3 --lora-modules '{"name": "nothink-lora", "path": "/data/models/loras/saves/deepseek-32b-nothink/lora/sft/", "base_model_name": "DeepSeek-R1-Distill-Qwen-32B"}'
```

## ERROR

```
(VllmWorkerProcess pid=4328) INFO 04-21 06:47:16 [model_runner.py:899] Starting to load model /data/models/DeepSeek-R1-Distill-Qwen-32B/...
Loading safetensors checkpoint shards:   0% Completed | 0/8 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  12% Completed | 1/8 [00:02<00:14,  2.03s/it]
Loading safetensors checkpoint shards:  25% Completed | 2/8 [00:04<00:13,  2.30s/it]
Loading safetensors checkpoint shards:  38% Completed | 3/8 [00:06<00:11,  2.32s/it]
Loading safetensors checkpoint shards:  50% Completed | 4/8 [00:09<00:09,  2.44s/it]
Loading safetensors checkpoint shards:  62% Completed | 5/8 [00:10<00:05,  1.99s/it]
Loading safetensors checkpoint shards:  75% Completed | 6/8 [00:13<00:04,  2.12s/it]
Loading safetensors checkpoint shards:  88% Completed | 7/8 [00:15<00:02,  2.26s/it]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:17<00:00,  2.26s/it]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:17<00:00,  2.23s/it]

INFO 04-21 06:47:34 [loader.py:458] Loading weights took 18.22 seconds
INFO 04-21 06:47:35 [model_runner.py:904] Loading model weights took 30.7295 GB
ERROR 04-21 06:47:35 [engine.py:448] No module named 'vllm_ascend.lora'
ERROR 04-21 06:47:35 [engine.py:448] Traceback (most recent call last):
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 04-21 06:47:35 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 04-21 06:47:35 [engine.py:448]     return cls(
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 282, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 286, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     super().__init__(*args, **kwargs)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     self._init_executor()
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
ERROR 04-21 06:47:35 [engine.py:448]     self._run_workers("load_model",
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
ERROR 04-21 06:47:35 [engine.py:448]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
ERROR 04-21 06:47:35 [engine.py:448]     return func(*args, **kwargs)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
ERROR 04-21 06:47:35 [engine.py:448]     self.model_runner.load_model()
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 931, in load_model
ERROR 04-21 06:47:35 [engine.py:448]     self.model = self.lora_manager.create_lora_manager(self.model)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/worker_manager.py", line 204, in create_lora_manager
ERROR 04-21 06:47:35 [engine.py:448]     lora_manager = create_lora_manager(
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 794, in create_lora_manager
ERROR 04-21 06:47:35 [engine.py:448]     lora_manager = lora_manager_cls(
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 717, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     super().__init__(model, max_num_seqs, max_num_batched_tokens,
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 335, in __init__
ERROR 04-21 06:47:35 [engine.py:448]     self.punica_wrapper = get_punica_wrapper(
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/punica_wrapper/punica_selector.py", line 14, in get_punica_wrapper
ERROR 04-21 06:47:35 [engine.py:448]     punica_wrapper_cls = resolve_obj_by_qualname(punica_wrapper_qualname)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2009, in resolve_obj_by_qualname
ERROR 04-21 06:47:35 [engine.py:448]     module = importlib.import_module(module_name)
ERROR 04-21 06:47:35 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/importlib/__init__.py", line 126, in import_module
ERROR 04-21 06:47:35 [engine.py:448]     return _bootstrap._gcd_import(name[level:], package, level)
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 04-21 06:47:35 [engine.py:448]   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ERROR 04-21 06:47:35 [engine.py:448] ModuleNotFoundError: No module named 'vllm_ascend.lora'
(VllmWorkerProcess pid=4328) INFO 04-21 06:47:35 [loader.py:458] Loading weights took 19.42 seconds
(VllmWorkerProcess pid=4328) INFO 04-21 06:47:36 [model_runner.py:904] Loading model weights took 30.7295 GB
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 931, in load_model
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     self.model = self.lora_manager.create_lora_manager(self.model)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/worker_manager.py", line 204, in create_lora_manager
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     lora_manager = create_lora_manager(
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 794, in create_lora_manager
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     lora_manager = lora_manager_cls(
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 717, in __init__
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     super().__init__(model, max_num_seqs, max_num_batched_tokens,
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 335, in __init__
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     self.punica_wrapper = get_punica_wrapper(
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/punica_wrapper/punica_selector.py", line 14, in get_punica_wrapper
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     punica_wrapper_cls = resolve_obj_by_qualname(punica_wrapper_qualname)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2009, in resolve_obj_by_qualname
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     module = importlib.import_module(module_name)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/importlib/__init__.py", line 126, in import_module
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]     return _bootstrap._gcd_import(name[level:], package, level)
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238]   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
(VllmWorkerProcess pid=4328) ERROR 04-21 06:47:36 [multiproc_worker_utils.py:238] ModuleNotFoundError: No module named 'vllm_ascend.lora'
ERROR 04-21 06:47:37 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 4328 died, exit code: -15
INFO 04-21 06:47:37 [multiproc_worker_utils.py:124] Killing local vLLM worker processes
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 450, in run_mp_engine
    raise e
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
    return cls(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 282, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config, )
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 286, in __init__
    super().__init__(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
    self._run_workers("load_model",
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
    driver_worker_output = run_method(self.driver_worker, sent_method,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
    self.model_runner.load_model()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 931, in load_model
    self.model = self.lora_manager.create_lora_manager(self.model)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/worker_manager.py", line 204, in create_lora_manager
    lora_manager = create_lora_manager(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 794, in create_lora_manager
    lora_manager = lora_manager_cls(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 717, in __init__
    super().__init__(model, max_num_seqs, max_num_batched_tokens,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/models.py", line 335, in __init__
    self.punica_wrapper = get_punica_wrapper(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/lora/punica_wrapper/punica_selector.py", line 14, in get_punica_wrapper
    punica_wrapper_cls = resolve_obj_by_qualname(punica_wrapper_qualname)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2009, in resolve_obj_by_qualname
    module = importlib.import_module(module_name)
  File "/usr/local/python3.10/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'vllm_ascend.lora'
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 51, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1069, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-04-21-06:47:42 (PID:4045, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@ascend:/workspace# /usr/local/python3.10/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 31 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

```
