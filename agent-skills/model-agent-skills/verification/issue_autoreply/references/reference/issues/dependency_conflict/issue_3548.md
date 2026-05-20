# Issue #3548: [Bug]: Qwen3-Next has a runtime bug in layer_norm_fwd_kernel which has invalid CoreDim

## 基本信息

- **编号**: #3548
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3548
- **创建时间**: 2025-10-20T06:26:02Z
- **关闭时间**: 2025-10-22T01:02:07Z
- **更新时间**: 2025-10-22T01:02:08Z
- **提交者**: @drslark
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

**docker image:** quay.io/ascend/vllm-ascend:v0.10.2rc1

**model**: Qwen3-Next

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
BIOS Model name:                    Kunpeng 920 7270Z
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU max MHz:                        3100.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-79
NUMA node1 CPU(s):                  80-159
NUMA node2 CPU(s):                  160-239
NUMA node3 CPU(s):                  240-319
NUMA node4 CPU(s):                  320-399
NUMA node5 CPU(s):                  400-479
NUMA node6 CPU(s):                  480-559
NUMA node7 CPU(s):                  560-639
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.11.1.dev0+gb8b302cde.d20251020 (git sha: b8b302cde, date: 20251020)
vLLM Ascend Version: 0.11.0rc1.dev103+gdaa4dd0a5.d20251020 (git sha: daa4dd0a5, date: 20251020)

ENV Variables:
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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 199.1       32                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 8           0    / 0          51166/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           30                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 7           0    / 0          52518/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 200.3       30                0    / 0             |
| 0     2                   | 0000:99:00.0  | 8           0    / 0          51780/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           33                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 8           0    / 0          52526/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 165.4       33                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3145 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           31                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2891 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 164.6       31                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3145 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           31                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 162.8       29                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3156 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           29                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2896 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 159.6       29                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3153 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           30                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2895 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 161.7       30                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3156 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           30                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 161.4       31                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3156 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           29                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 4071417       |                          | 47881                   |
| 0       0                 | 4071418       |                          | 112                     |
| 0       0                 | 4071419       |                          | 112                     |
| 0       0                 | 4071420       |                          | 112                     |
| 0       1                 | 4071418       |                          | 49681                   |
+===========================+===============+====================================================+
| 1       0                 | 4071419       |                          | 48681                   |
| 1       1                 | 4071420       |                          | 49701                   |
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

**The bug description:** 

The bug occurs when we start a vllm server like:
```shell
vllm serve /home/model/Qwen3-Next-80B-A3B-Instruct   --port 22   --host 0.0.0.0   --served-model-name qwen3_next_mtp_0   --tensor-parallel-size 4   --max-model-len 32000   --gpu-memory-utilization 0.7   --enforce-eager
```

The, we start an aisbench clinet like:
```shell
ais_bench --models vllm_api_general_chat --datasets ceval_gen_0_shot_cot_chat_prompt --dump-eval-details
```

Whose config is:
```python
    # a big batch_size and a large max_out_len
    dict(
        abbr='vllm-api-general-chat',
        attr='service',
        batch_size=512,
        generation_kwargs=dict(temperature=0.7, top_k=20, top_p=0.8),
        host_ip='xxx.xxx.xxx.xxx',
        host_port=8881,
        max_out_len=30000,
        model='qwen3_next_mtp_0',
        path='',
        pred_postprocessor=dict(
            type=
            'ais_bench.benchmark.utils.model_postprocessors.extract_non_reasoning_content'
        ),
        request_rate=0,
        retry=2,
        trust_remote_code=False,
        type='ais_bench.benchmark.models.VLLMCustomAPIChat'),
```

Every time when we sent a bunch of requests and the **KV cache usage reaches 100.0%**.
We get a **coreDim=xxx can't be greater than UINT16_MAX.** Exception.

```text
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:15:53 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 71.4 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 94.1%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:03 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 70.7 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 97.1%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:13 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 71.4 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 97.1%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:23 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 71.4 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 97.1%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:33 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 72.8 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 99.6%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:43 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 71.4 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 0.0%
[1;36m(APIServer pid=597826)[0;0m INFO 10-21 01:16:53 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 73.5 tokens/s, Running: 7 reqs, Waiting: 1 reqs, GPU KV cache usage: 100.0%, Prefix cache hit rate: 0.0%
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 258, in execute_model
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1958, in execute_model
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     hidden_states = self._generate_process_reqs_hidden_states(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1564, in _generate_process_reqs_hidden_states
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     hidden_states = self.model(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                     ^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 225, in __call__
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     hidden_states, residual = layer(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                               ^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 848, in forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     hidden_states = self.mlp(hidden_states)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 163, in forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     final_hidden_states = self.experts(hidden_states=hidden_states,
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 44, in forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._forward_method(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self.forward_native(*args, **kwargs)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1827, in forward_native
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     fused_output = torch.ops.vllm.moe_forward(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2144, in moe_forward
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self.forward_impl(hidden_states, router_logits)
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 311, in forward_impl
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     final_hidden_states = self.quant_method.apply(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                           ^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 137, in apply
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return moe_comm_method.fused_experts(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/moe/moe_comm_method.py", line 137, in fused_experts
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     mlp_output = unified_apply_mlp(hidden_states=permuted_hidden_states,
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/moe/moe_mlp.py", line 252, in unified_apply_mlp
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return unquant_apply_mlp(hidden_states=hidden_states,
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/moe/moe_mlp.py", line 195, in unquant_apply_mlp
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     gate_up_out = torch_npu.npu_grouped_matmul(
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is layer_norm_fwd_kernel.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] [ERROR] 2025-10-21-01:17:01 (PID:598143, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671] EE1001: [PID: 598143] 2025-10-21-01:17:01.546.291 The argument is invalid.Reason: coreDim=66976 can't be greater than UINT16_MAX.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]         TraceBack (most recent call last):
[1;36m(Worker_TP2 pid=598143)[0;0m ERROR 10-21 01:17:01 [multiproc_executor.py:671]         The argument is invalid.Reason: rtKernelLaunch execute failed, reason=[invalid value]
```

It seems like triton kernel **layer_norm_fwd_kernel** has a **coreDim** bug.
