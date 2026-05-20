# Issue #397: [Bug]: RuntimeError: create:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:89 HCCL function error: HcclCommInitRootInfo(numRanks, &rootInfo, rank, &(comm->hcclComm_))

## 基本信息

- **编号**: #397
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/397
- **创建时间**: 2025-03-26T04:21:40Z
- **关闭时间**: 2025-05-14T02:53:13Z
- **更新时间**: 2025-05-14T02:53:14Z
- **提交者**: @qratosone
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.10.16 (main, Dec 11 2024, 16:18:56) [GCC 11.2.0] (64-bit runtime)
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
[pip3] onnxruntime==1.21.0
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.50.0.dev0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250308          pypi_0    pypi
[conda] transformers              4.50.0.dev0              pypi_0    pypi
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_LOG_TO_STDOUT=0
ATB_LOG_TO_FILE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=1,2
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_LOG_TO_FILE_FLUSH=0
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_GLOBAL_EVENT_ENABLE=0
ATB_OPERATION_EXECUTE_ASYNC=1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_GLOBAL_LOG_LEVEL=3
ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/aie_ascendc:/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/customize:
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/mindie/latest/mindie-llm/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-llm/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-torch/lib:/usr/local/Ascend/mindie/latest/mindie-rt/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_LOG_LEVEL=ERROR
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
| 1     910B2               | OK            | 95.0        45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 105.4       44                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3370 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux</summary>




</details>


### 🐛 Describe the bug


I‘m running open-r1 with deepspeed on a machine with 2 NPUs, using the command mentioned in https://github.com/huggingface/open-r1/pull/303


got the following error:
```text
2025-03-26 11:48:53 - INFO - vllm_ascend.worker.model_runner - Loading model weights took 5.7560 GB
INFO 03-26 11:49:00 executor_base.py:111] # npu blocks: 3915, # CPU blocks: 910
INFO 03-26 11:49:00 executor_base.py:116] Maximum concurrency for 32768 tokens per request: 15.29x
INFO 03-26 11:49:01 llm_engine.py:436] init engine (profile, create kv cache, warmup model) took 7.91 seconds
[2025-03-26 11:49:01,311] [INFO] [logging.py:128:log_dist] [Rank 0] DeepSpeed info: version=0.15.4, git-hash=unknown, git-branch=unknown
[2025-03-26 11:49:01,311] [INFO] [config.py:733:__init__] Config mesh_device None world_size = 1
[rank0]:[W326 11:49:12.331714626 compiler_depend.ts:133] Warning: Warning: Device do not support double dtype now, dtype cast repalce with float. (function operator())
[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/autodl-tmp/open-r1/src/open_r1/grpo.py", line 263, in <module>
[rank0]:     main(script_args, training_args, model_args)
[rank0]:   File "/root/autodl-tmp/open-r1/src/open_r1/grpo.py", line 198, in main
[rank0]:     trainer = GRPOTrainer(
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/trl/trainer/grpo_trainer.py", line 568, in __init__
[rank0]:     self.ref_model = prepare_deepspeed(self.ref_model, self.accelerator)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/trl/models/utils.py", line 254, in prepare_deepspeed
[rank0]:     model, *_ = deepspeed.initialize(model=model, config=config_kwargs)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/__init__.py", line 193, in initialize
[rank0]:     engine = DeepSpeedEngine(args=args,
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/runtime/engine.py", line 269, in __init__
[rank0]:     self._configure_distributed_model(model)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/runtime/engine.py", line 1201, in _configure_distributed_model
[rank0]:     self._broadcast_model()
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/runtime/engine.py", line 1120, in _broadcast_model
[rank0]:     dist.broadcast(p.data, groups._get_broadcast_src_rank(), group=self.seq_data_parallel_group)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/comm/comm.py", line 117, in log_wrapper
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/comm/comm.py", line 224, in broadcast
[rank0]:     return cdb.broadcast(tensor=tensor, src=src, group=group, async_op=async_op)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/deepspeed/comm/torch.py", line 200, in broadcast
[rank0]:     return torch.distributed.broadcast(tensor=tensor, src=src, group=group, async_op=async_op)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/autodl-tmp/vllm_073/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2421, in broadcast
[rank0]:     work = group.broadcast([tensor], opts)
[rank0]: RuntimeError: create:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:89 HCCL function error: HcclCommInitRootInfo(numRanks, &rootInfo, rank, &(comm->hcclComm_)), error code is 2
[rank0]: [ERROR] 2025-03-26-11:49:12 (PID:3674, Device:0, RankID:0) ERR02200 DIST call hccl api failed.
```


