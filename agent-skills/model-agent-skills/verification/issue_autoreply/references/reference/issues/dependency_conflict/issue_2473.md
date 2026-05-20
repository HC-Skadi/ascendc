# Issue #2473: [Bug]: Qwen3-30B-A3B-W8A8 on v0.10.0rc1 report AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027

## 基本信息

- **编号**: #2473
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2473
- **创建时间**: 2025-08-21T08:41:06Z
- **关闭时间**: 2025-12-03T07:07:38Z
- **更新时间**: 2025-12-03T07:07:38Z
- **提交者**: @e1e1t7t7
- **评论数**: 3

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-153.56.0.134.oe2203sp2.aarch64-aarch64-with-glibc2.35

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
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.53.3
[conda] Could not collect
vLLM Version: 0.10.0
vLLM Ascend Version: 0.10.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:False
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ASCEND_LAUNCH_BLOCKING=0
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 90.5        34                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2841 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 83.4        32                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2837 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 82.8        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2837 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 81.9        33                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2838 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 82.7        39                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2838 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 94.6        37                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2837 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 88.3        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2837 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 90.7        38                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2837 / 32768         |
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
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux

```

</details>


### 🐛 Describe the bug


(VllmWorker rank=5 pid=36860) INFO 08-21 08:25:46 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_5_0/backbone for vLLM's torch.compile
(VllmWorker rank=5 pid=36860) INFO 08-21 08:25:46 [backends.py:541] Dynamo bytecode transform time: 17.38 s
(VllmWorker rank=2 pid=36130) INFO 08-21 08:25:46 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_2_0/backbone for vLLM's torch.compile
(VllmWorker rank=2 pid=36130) INFO 08-21 08:25:46 [backends.py:541] Dynamo bytecode transform time: 17.67 s
(VllmWorker rank=3 pid=36368) INFO 08-21 08:25:47 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_3_0/backbone for vLLM's torch.compile
(VllmWorker rank=3 pid=36368) INFO 08-21 08:25:47 [backends.py:541] Dynamo bytecode transform time: 17.70 s
(VllmWorker rank=0 pid=36105) INFO 08-21 08:25:47 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_0_0/backbone for vLLM's torch.compile
(VllmWorker rank=0 pid=36105) INFO 08-21 08:25:47 [backends.py:541] Dynamo bytecode transform time: 17.96 s
(VllmWorker rank=7 pid=37352) INFO 08-21 08:25:47 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_7_0/backbone for vLLM's torch.compile
(VllmWorker rank=7 pid=37352) INFO 08-21 08:25:47 [backends.py:541] Dynamo bytecode transform time: 17.66 s
(VllmWorker rank=4 pid=36614) INFO 08-21 08:25:48 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_4_0/backbone for vLLM's torch.compile
(VllmWorker rank=4 pid=36614) INFO 08-21 08:25:48 [backends.py:541] Dynamo bytecode transform time: 17.97 s
(VllmWorker rank=1 pid=36111) INFO 08-21 08:25:48 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_1_0/backbone for vLLM's torch.compile
(VllmWorker rank=1 pid=36111) INFO 08-21 08:25:48 [backends.py:541] Dynamo bytecode transform time: 18.03 s
(VllmWorker rank=6 pid=37106) INFO 08-21 08:25:48 [backends.py:530] Using cache directory: /root/.cache/vllm/torch_compile_cache/8a812ea728/rank_6_0/backbone for vLLM's torch.compile
(VllmWorker rank=6 pid=37106) INFO 08-21 08:25:48 [backends.py:541] Dynamo bytecode transform time: 17.23 s
(VllmWorker rank=5 pid=36860) INFO 08-21 08:25:51 [backends.py:215] Compiling a graph for dynamic shape takes 3.61 s
(VllmWorker rank=2 pid=36130) INFO 08-21 08:25:51 [backends.py:215] Compiling a graph for dynamic shape takes 3.44 s
(VllmWorker rank=3 pid=36368) INFO 08-21 08:25:51 [backends.py:215] Compiling a graph for dynamic shape takes 3.51 s
(VllmWorker rank=0 pid=36105) INFO 08-21 08:25:52 [backends.py:215] Compiling a graph for dynamic shape takes 3.44 s
(VllmWorker rank=7 pid=37352) INFO 08-21 08:25:52 [backends.py:215] Compiling a graph for dynamic shape takes 3.46 s
(VllmWorker rank=1 pid=36111) INFO 08-21 08:25:53 [backends.py:215] Compiling a graph for dynamic shape takes 3.52 s
(VllmWorker rank=6 pid=37106) INFO 08-21 08:25:53 [backends.py:215] Compiling a graph for dynamic shape takes 3.54 s
(VllmWorker rank=4 pid=36614) INFO 08-21 08:25:53 [backends.py:215] Compiling a graph for dynamic shape takes 3.64 s
[rank2]:[W821 08:26:12.487618185 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank6]:[W821 08:26:12.509318232 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank0]:[W821 08:26:12.542800067 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank5]:[W821 08:26:13.909029063 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank1]:[W821 08:26:13.932323998 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank3]:[W821 08:26:13.000065453 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank4]:[W821 08:26:13.042186539 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank7]:[W821 08:26:13.353314943 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
(VllmWorker rank=0 pid=36105) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.40 s in total
(VllmWorker rank=3 pid=36368) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.21 s in total
(VllmWorker rank=2 pid=36130) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.11 s in total
(VllmWorker rank=1 pid=36111) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.55 s in total
(VllmWorker rank=5 pid=36860) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 20.99 s in total
(VllmWorker rank=4 pid=36614) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.60 s in total
(VllmWorker rank=7 pid=37352) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 21.11 s in total
(VllmWorker rank=6 pid=37106) INFO 08-21 08:26:15 [monitor.py:34] torch.compile takes 20.77 s in total
(VllmWorker rank=2 pid=36130) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 20467668582, total memory: 31662800896
(VllmWorker rank=4 pid=36614) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 19637687910, total memory: 31662800896
(VllmWorker rank=1 pid=36111) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 20320957030, total memory: 31662800896
(VllmWorker rank=0 pid=36105) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 19443365990, total memory: 31662800896
(VllmWorker rank=3 pid=36368) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 20133888614, total memory: 31662800896
(VllmWorker rank=6 pid=37106) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 19795793510, total memory: 31662800896
(VllmWorker rank=5 pid=36860) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 20058244710, total memory: 31662800896
(VllmWorker rank=7 pid=37352) INFO 08-21 08:26:19 [worker_v1.py:186] Available memory: 20467316326, total memory: 31662800896
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 791,040 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 193.12x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 826,752 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 201.84x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 832,768 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 203.31x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 819,200 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 200.00x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 798,976 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 195.06x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 816,128 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 199.25x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 805,376 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 196.62x
INFO 08-21 08:26:19 [kv_cache_utils.py:833] GPU KV cache size: 832,768 tokens
INFO 08-21 08:26:19 [kv_cache_utils.py:837] Maximum concurrency for 4,096 tokens per request: 203.31x
[rank4]:[W821 08:26:20.536421538 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank1]:[W821 08:26:20.548242047 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W821 08:26:20.555928992 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546] WorkerProc hit an exception.
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 261, in compile_or_warm_up_model
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self.model_runner.capture_model()
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2430, in capture_model
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self._dummy_run(num_tokens)
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1975, in _dummy_run
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=0 pid=36105) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File 
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     quantized_tokens, expanded_row_idx, global_expert_tokens, token_scales = init_routing_quant(
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in init_routing_quant
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                                                                              ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     global_expert_tokens = torch.bincount(expanded_expert_idx,
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in init_routing_quant
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "<eval_with_key>.98", line 882, in forward
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     global_expert_tokens = torch.bincount(expanded_expert_idx,
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     submod_2 = self.submod_2(getitem_3, s0, ...
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546] [ERROR] 2025-08-21-08:26:21 (PID:36130, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 194, in __call__
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546] EE9999: Inner Error!
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546] [ERROR] 2025-08-21-08:26:21 (PID:36368, Device:3, RankID:-1) ERR00100 PTA call acl api failed.
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = entry.runnable(*args)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546] WorkerProc hit an exception.
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546] EE9999: [PID: 36130] 2025-08-21-08:26:21.385.272 Not allow to synchronize captured-stream, stream_id=9.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546] EE9999: Inner Error!
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]         TraceBack (most recent call last):
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546] EE9999: [PID: 36368] 2025-08-21-08:26:21.384.697 Not allow to synchronize captured-stream, stream_id=9.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]         TraceBack (most recent call last):
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 261, in compile_or_warm_up_model
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     raise e
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self.model_runner.capture_model()
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2430, in capture_model
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self._dummy_run(num_tokens)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 261, in compile_or_warm_up_model
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 261, in compile_or_warm_up_model
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self.model_runner.capture_model()
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self.model_runner.capture_model()
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2430, in capture_model
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2430, in capture_model
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1975, in _dummy_run
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self._dummy_run(num_tokens)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self._dummy_run(num_tokens)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "<eval_with_key>.3", line 21, in forward
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     moe_forward = torch.ops.vllm.moe_forward(view_2, linear, 'model.layers.0.mlp.experts');  view_2 = linear = None
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1975, in _dummy_run
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1975, in _dummy_run
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._op(*args, **(kwargs or {}))
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1579, in moe_forward
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 386, in forward
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self.forward_impl(hidden_states, router_logits)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1489, in forward_impl
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 279, in __call__
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     final_hidden_states = self.quant_method.apply(
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 386, in forward
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 386, in forward
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 330, in apply
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 279, in forward
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self.quant_method.apply(
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     def forward(
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 279, in __call__
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 279, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 1001, in apply
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return fused_experts_with_all2all(
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 279, in forward
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 279, in forward
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 433, in fused_experts_with_all2all
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     def forward(
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     def forward(
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     quantized_tokens, expanded_row_idx, global_expert_tokens, token_scales = init_routing_quant(

(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     raise e
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]         TraceBack (most recent call last):
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546] WorkerProc hit an exception.
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=1 pid=36111) ERROR 08-21 08:26:21 [multiproc_executor.py:546]
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     raise e
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546] Traceback (most recent call last):
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     raise e
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 541, in worker_busy_loop
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = func(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 261, in compile_or_warm_up_model
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self.model_runner.capture_model()
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "<eval_with_key>.98", line 882, in forward
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2430, in capture_model
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     submod_2 = self.submod_2(getitem_3, s0, ...
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     self._dummy_run(num_tokens)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
ERROR 08-21 08:26:21 [core.py:632] EngineCore failed to start.
ERROR 08-21 08:26:21 [core.py:632] Traceback (most recent call last):
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 623, in run_engine_core
ERROR 08-21 08:26:21 [core.py:632]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 08-21 08:26:21 [core.py:632]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 441, in __init__
ERROR 08-21 08:26:21 [core.py:632]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 86, in __init__
ERROR 08-21 08:26:21 [core.py:632]     self._initialize_kv_caches(vllm_config)
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
ERROR 08-21 08:26:21 [core.py:632]     self.model_executor.initialize_from_config(kv_cache_configs)
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 66, in initialize_from_config
ERROR 08-21 08:26:21 [core.py:632]     self.collective_rpc("compile_or_warm_up_model")
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 237, in collective_rpc
ERROR 08-21 08:26:21 [core.py:632]     result = get_response(w, dequeue_timeout)
ERROR 08-21 08:26:21 [core.py:632]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 08-21 08:26:21 [core.py:632]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 224, in get_response
ERROR 08-21 08:26:21 [core.py:632]     raise RuntimeError(
ERROR 08-21 08:26:21 [core.py:632] RuntimeError: Worker failed with error 'operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
ERROR 08-21 08:26:21 [core.py:632] [ERROR] 2025-08-21-08:26:21 (PID:36105, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 08-21 08:26:21 [core.py:632] EE9999: Inner Error!
ERROR 08-21 08:26:21 [core.py:632] EE9999: [PID: 36105] 2025-08-21-08:26:21.384.027 Not allow to synchronize captured-stream, stream_id=37.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
ERROR 08-21 08:26:21 [core.py:632]         TraceBack (most recent call last):
ERROR 08-21 08:26:21 [core.py:632]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
ERROR 08-21 08:26:21 [core.py:632]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 08-21 08:26:21 [core.py:632] ', please check the stack trace above for the root cause
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return forward_call(*args, **kwargs)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 194, in __call__
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = entry.runnable(*args)
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "<eval_with_key>.98", line 882, in forward
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "<eval_with_key>.98", line 882, in forward
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     submod_2 = self.submod_2(getitem_3, s0, ...
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1975, in _dummy_run
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     submod_2 = self.submod_2(getitem_3, s0, ...
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     hidden_states = model(
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 194, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     output = entry.runnable(*args)
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker rank=4 pid=36614) ERROR 08-21 08:26:21 [multiproc_executor.py:546]     raise e
(VllmWorker rank=2 pid=36130) ERROR 08-21 08:26:21 [multiproc_executor.py:546]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 194, in __call__
(VllmWorker rank=7 pid=37352) ERROR 08-21 08:26:21 [multiproc_executor.py:546]                     ^^^^^^
(VllmWorker rank=3 pid=36368) ERROR 08-21 08:26:21 [multiproc_executor.py:546]              ^^^^^^^^^^^^^^^^^^^^^
ERROR 08-21 08:26:33 [multiproc_executor.py:140] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 636, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 623, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 441, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 86, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
    self.model_executor.initialize_from_config(kv_cache_configs)
  File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 66, in initialize_from_config
    self.collective_rpc("compile_or_warm_up_model")
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 237, in collective_rpc
    result = get_response(w, dequeue_timeout)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 224, in get_response
    raise RuntimeError(
RuntimeError: Worker failed with error 'operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
[ERROR] 2025-08-21-08:26:21 (PID:36105, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
EE9999: Inner Error!
EE9999: [PID: 36105] 2025-08-21-08:26:21.384.027 Not allow to synchronize captured-stream, stream_id=37.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
        TraceBack (most recent call last):
       rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 52, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
    return runner.run(wrapper())
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1791, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1811, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 163, in from_vllm_config
    return cls(
           ^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 117, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 98, in make_async_mp_client
    return AsyncMPClient(*client_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 677, in __init__
    super().__init__(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 408, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 697, in launch_core_engines
    wait_for_engine_startup(
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 750, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-08-21-08:26:35 (PID:35698, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

