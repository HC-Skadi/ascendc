# Issue #1369: [Bug]: UnboundLocalError: local variable 'decode_hs_or_q_c' referenced before assignment

## 基本信息

- **编号**: #1369
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1369
- **创建时间**: 2025-06-23T08:41:33Z
- **关闭时间**: 2025-06-25T09:02:56Z
- **更新时间**: 2025-07-31T12:10:16Z
- **提交者**: @tt545571022
- **评论数**: 11

## 标签

bug

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

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.108.0.188.u167.fos23.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
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
| 0     910B3               | OK            | 100.4       42                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 95.3        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3386 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 98.4        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3387 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 103.6       40                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 102.8       47                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          61917/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 100.8       47                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          61932/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 96.2        46                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          61916/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 103.5       46                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          61916/ 65536         |
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
| 4       0                 | 1933166       |                          | 58579                   |
+===========================+===============+====================================================+
| 5       0                 | 1933167       |                          | 58579                   |
+===========================+===============+====================================================+
| 6       0                 | 1933168       |                          | 58579                   |
+===========================+===============+====================================================+
| 7       0                 | 1933169       |                          | 58579                   |
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

当我使用官方pull的0.9.1rc1的镜像，使用USE_VLLM_V1=1推理DeepSeek-R1-W8A8的torchair图模式，使用了2卡，将网络层数改为5层，在eager模式下可以正常推理，在torchair图模式下报如下错误：
`UnboundLocalError: local variable 'decode_hs_or_q_c' referenced before assignment`
详细报错如下：
```
(VllmWorker rank=0 pid=114263) INFO 06-23 16:26:53 [quantizer.py:88] Using the vLLM Ascend Quantizer version now!
Loading safetensors checkpoint shards:   0% Completed | 0/8 [00:00<?, ?it/s]
(VllmWorker rank=1 pid=114447) INFO 06-23 16:26:54 [quantizer.py:88] Using the vLLM Ascend Quantizer version now!
[rank1]:[W623 16:26:54.863418440 compiler_depend.ts:2156] Warning: The indexFromRank 0is not equal indexFromCurDevice 1 , which might be normal if the number of devices on your collective communication server is inconsistent.Otherwise, you need to check if the current device is correct when calling the interface.If it's incorrect, it might have introduced an error. (function operator())
Loading safetensors checkpoint shards:  25% Completed | 2/8 [00:00<00:00, 12.76it/s]
Loading safetensors checkpoint shards:  50% Completed | 4/8 [00:02<00:03,  1.29it/s]
Loading safetensors checkpoint shards:  62% Completed | 5/8 [00:02<00:01,  1.69it/s]
Loading safetensors checkpoint shards:  88% Completed | 7/8 [00:03<00:00,  2.01it/s]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:04<00:00,  1.76it/s]
Loading safetensors checkpoint shards: 100% Completed | 8/8 [00:04<00:00,  1.82it/s]
(VllmWorker rank=0 pid=114263) 
(VllmWorker rank=0 pid=114263) INFO 06-23 16:26:58 [default_loader.py:272] Loading weights took 4.43 seconds
(VllmWorker rank=1 pid=114447) INFO 06-23 16:26:58 [default_loader.py:272] Loading weights took 4.22 seconds
(VllmWorker rank=0 pid=114263) INFO 06-23 16:26:59 [model_runner_v1.py:1848] Loading model weights took 8.1004 GB
(VllmWorker rank=1 pid=114447) INFO 06-23 16:26:59 [model_runner_v1.py:1848] Loading model weights took 8.1004 GB
[rank1]:[W623 16:27:05.639043890 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank0]:[W623 16:27:05.720933950 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
INFO 06-23 16:27:05 [kv_cache_utils.py:715] GPU KV cache size: 9,874,688 tokens
INFO 06-23 16:27:05 [kv_cache_utils.py:719] Maximum concurrency for 16 tokens per request: 77146.00x
INFO 06-23 16:27:05 [kv_cache_utils.py:715] GPU KV cache size: 9,876,352 tokens
INFO 06-23 16:27:05 [kv_cache_utils.py:719] Maximum concurrency for 16 tokens per request: 77159.00x
(VllmWorker rank=0 pid=114263) INFO 06-23 16:27:05 [model_runner_v1.py:2045] Capturing torchair graph, this usually takes 0.5~1.5 mins.
(VllmWorker rank=1 pid=114447) INFO 06-23 16:27:05 [model_runner_v1.py:2045] Capturing torchair graph, this usually takes 0.5~1.5 mins.
(VllmWorker rank=0 pid=114263) /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:992: UserWarning: When enable frozen_parameter, Parameters will be considered frozen.Please make sure that the Parameters data address remain the same throughout the program runtime.
(VllmWorker rank=0 pid=114263)   warnings.warn(f'When enable frozen_parameter, Parameters will be considered frozen.'
(VllmWorker rank=1 pid=114447) /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:992: UserWarning: When enable frozen_parameter, Parameters will be considered frozen.Please make sure that the Parameters data address remain the same throughout the program runtime.
(VllmWorker rank=1 pid=114447)   warnings.warn(f'When enable frozen_parameter, Parameters will be considered frozen.'
....(VllmWorker rank=1 pid=114447) INFO 06-23 16:27:27 [model_runner_v1.py:2061] Batchsize 256 is compiled successfully: 1/1.
(VllmWorker rank=0 pid=114263) INFO 06-23 16:27:27 [model_runner_v1.py:2061] Batchsize 256 is compiled successfully: 1/1.
(VllmWorker rank=1 pid=114447) INFO 06-23 16:27:27 [model_runner_v1.py:2081] Graph capturing finished in 21 secs, took 0.02 GiB
(VllmWorker rank=0 pid=114263) INFO 06-23 16:27:27 [model_runner_v1.py:2081] Graph capturing finished in 21 secs, took 0.02 GiB
INFO 06-23 16:27:27 [core.py:171] init engine (profile, create kv cache, warmup model) took 27.48 seconds
Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 292.83it/s]
Processed prompts:   0%|                                                                                           | 0/4 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s](VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527] WorkerProc hit an exception.
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527] Traceback (most recent call last):
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 178, in execute_model
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1472, in execute_model
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     aux_hidden_states) = (self._process_reqs(scheduler_output,
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1164, in _process_reqs
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.model(
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 753, in forward
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.model(input_ids, positions, kv_caches,
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 700, in forward
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states, residual = layer(
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 593, in forward
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.self_attn(
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 489, in forward
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = self.mla_attn.impl.forward(self.mla_attn,
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/mla_v1.py", line 1099, in forward
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     self._q_proj_and_k_up_proj(decode_hs_or_q_c)
(VllmWorker rank=1 pid=114447) ERROR 06-23 16:27:28 [multiproc_executor.py:527] UnboundLocalError: local variable 'decode_hs_or_q_c' referenced before assignment
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527] WorkerProc hit an exception.
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527] Traceback (most recent call last):
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 178, in execute_model
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1472, in execute_model
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     aux_hidden_states) = (self._process_reqs(scheduler_output,
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1164, in _process_reqs
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.model(
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 753, in forward
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.model(input_ids, positions, kv_caches,
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 700, in forward
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states, residual = layer(
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 593, in forward
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     hidden_states = self.self_attn(
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     return forward_call(*args, **kwargs)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 489, in forward
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     output = self.mla_attn.impl.forward(self.mla_attn,
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/mla_v1.py", line 1099, in forward
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527]     self._q_proj_and_k_up_proj(decode_hs_or_q_c)
(VllmWorker rank=0 pid=114263) ERROR 06-23 16:27:28 [multiproc_executor.py:527] UnboundLocalError: local variable 'decode_hs_or_q_c' referenced before assignment
ERROR 06-23 16:27:28 [dump_input.py:69] Dumping input data
```
推理脚本如下：
```
import os

from vllm import LLM, SamplingParams

os.environ["VLLM_USE_V1"] = "1"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

if __name__ == "__main__":
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=16, temperature=0.0)
    # Create an LLM.
    llm = LLM(model="/home/models/DeepSeek-R1-W8A8-lite/",
              tensor_parallel_size=2,
            #   enforce_eager=True,
              trust_remote_code=True,
              max_model_len=16,
              quantization="ascend",
              additional_config={
                "torchair_graph_config": {"enabled": True},
                # "asacend_scheduler_config": {"enabled": True,},
              },
              )

    # Generate texts from the prompts.
    for i in range(10):
        outputs = llm.generate(prompts, sampling_params)

```

