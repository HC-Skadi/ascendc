# Issue #3865: [Bug]: Qwen3-Next-80B-A3B-Instruct vllm-ascend0.11.0cr1图模式加载失败

## 基本信息

- **编号**: #3865
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3865
- **创建时间**: 2025-10-29T08:38:03Z
- **关闭时间**: 2025-10-29T08:42:24Z
- **更新时间**: 2025-10-29T08:42:24Z
- **提交者**: @alex7092
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
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
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchaudio==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1.dev167+gcd58a643c (git sha: cd58a643c)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.6        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          37705/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.7        36                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          39053/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 88.1        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          39072/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.8        37                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          39072/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.3        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          39053/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 89.8        40                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          39053/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 92.6        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          39073/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 90.9        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          39053/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 3104272       |                          | 116                     |
| 0       0                 | 3104266       |                          | 33895                   |
| 0       0                 | 3104283       |                          | 115                     |
| 0       0                 | 3104267       |                          | 115                     |
| 0       0                 | 3104268       |                          | 115                     |
| 0       0                 | 3104269       |                          | 115                     |
| 0       0                 | 3104270       |                          | 115                     |
| 0       0                 | 3104271       |                          | 115                     |
+===========================+===============+====================================================+
| 1       0                 | 3104267       |                          | 35695                   |
+===========================+===============+====================================================+
| 2       0                 | 3104268       |                          | 35715                   |
+===========================+===============+====================================================+
| 3       0                 | 3104269       |                          | 35715                   |
+===========================+===============+====================================================+
| 4       0                 | 3104270       |                          | 35695                   |
+===========================+===============+====================================================+
| 5       0                 | 3104271       |                          | 35695                   |
+===========================+===============+====================================================+
| 6       0                 | 3104272       |                          | 35715                   |
+===========================+===============+====================================================+
| 7       0                 | 3104283       |                          | 35696                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux


</details>


### 🐛 Describe the bug

启动命令：
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh
source /usr/local/Ascend/8.3.RC1/bisheng_toolkit/set_env.sh

# export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
# export VLLM_USE_V1=1
# export HCCL_DETERMINISTIC=true
#export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1  

# Debug
#export ASDOPS_LOG_TO_FILE=1
#export ASDOPS_LOG_LEVEL=INFO
#export ASCEND_GLOBAL_LOG_LEVEL=1
#export ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=1

#export ASCEND_LAUNCH_BLOCKING=1
export VLLM_USE_MODELSCOPE=true
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
#export TRITON_ALL_BLOCKS_PARALLEL=1
MODEL_DIR="/root/.cache/Qwen3-Next-80B-A3B-Instruct"
MODEL_NAME="qwen3_next"
LOGFILE=/workspace/log/qwen3_next_infer.log


VLLM_CMD="vllm serve $MODEL_DIR --served-model-name $MODEL_NAME --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.7 --enforce-eager 2>&1 &"
echo -e "\nStarting vLLM with command: \n\t $VLLM_CMD \n"

vllm serve $MODEL_DIR --served-model-name $MODEL_NAME --tensor-parallel-size 8 --max-model-len 32768 --gpu-memory-utilization 0.5 --additional-config='{"torchair_graph_config": {"enabled": true},"ascend_scheduler_config": {"enabled": true}}' > $LOGFILE 2>&1 &

exec "$@"
报错信息：
y:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] WorkerProc hit an exception.
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_worker.py", line 34, in determine_available_memory
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     available_kv_cache_memory = super().determine_available_memory()
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in determine_available_memory
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self.model_runner.profile_run()
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2557, in profile_run
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self._dummy_run(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2521, in _dummy_run
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 185, in _generate_dummy_run_hidden_states
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = super()._generate_dummy_run_hidden_states(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2342, in _generate_dummy_run_hidden_states
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 225, in __call__
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states, residual = layer(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                               ^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 823, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self.linear_attn(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 387, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return torch.ops.vllm.gdn_attention(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1198, in gdn_attention
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self._forward(hidden_states=hidden_states, output=output)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 197, in _forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     assert isinstance(attn_metadata, dict)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] AssertionError
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_worker.py", line 34, in determine_available_memory
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     available_kv_cache_memory = super().determine_available_memory()
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in determine_available_memory
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self.model_runner.profile_run()
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2557, in profile_run
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self._dummy_run(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2521, in _dummy_run
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 185, in _generate_dummy_run_hidden_states
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = super()._generate_dummy_run_hidden_states(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2342, in _generate_dummy_run_hidden_states
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1144, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 225, in __call__
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 928, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     hidden_states, residual = layer(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]                               ^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 823, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self.linear_attn(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 387, in forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return torch.ops.vllm.gdn_attention(
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1198, in gdn_attention
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     self._forward(hidden_states=hidden_states, output=output)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_next.py", line 197, in _forward
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]     assert isinstance(attn_metadata, dict)
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] AssertionError
(Worker_TP0 pid=137462) ERROR 10-29 08:32:26 [multiproc_executor.py:671] 
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     self.model_executor.determine_available_memory())
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708]     raise RuntimeError(
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:26 [core.py:708] RuntimeError: Worker failed with error '', please check the stack trace above for the root cause
(EngineCore_DP0 pid=137324) ERROR 10-29 08:32:36 [multiproc_executor.py:154] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=137324) Process EngineCore_DP0:
(EngineCore_DP0 pid=137324) Traceback (most recent call last):
(EngineCore_DP0 pid=137324)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=137324)     self.run()
(EngineCore_DP0 pid=137324)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=137324)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=137324)     raise e
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=137324)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=137324)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=137324)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(EngineCore_DP0 pid=137324)     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
(EngineCore_DP0 pid=137324)     self.model_executor.determine_available_memory())
(EngineCore_DP0 pid=137324)     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
(EngineCore_DP0 pid=137324)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=137324)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=137324)     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=137324)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=137324)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=137324)     raise RuntimeError(
(EngineCore_DP0 pid=137324) RuntimeError: Worker failed with error '', please check the stack trace above for the root cause
(APIServer pid=137051) Traceback (most recent call last):
(APIServer pid=137051)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=137051)     sys.exit(main())
(APIServer pid=137051)              ^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=137051)     args.dispatch_function(args)
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=137051)     uvloop.run(run_server(args))
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=137051)     return runner.run(wrapper())
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=137051)     return self._loop.run_until_complete(task)
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=137051)     return await main
(APIServer pid=137051)            ^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=137051)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=137051)     async with build_async_engine_client(
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=137051)     return await anext(self.gen)
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=137051)     async with build_async_engine_client_from_engine_args(
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=137051)     return await anext(self.gen)
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=137051)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=137051)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1572, in inner
(APIServer pid=137051)     return fn(*args, **kwargs)
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=137051)     return cls(
(APIServer pid=137051)            ^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=137051)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=137051)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=137051)     return AsyncMPClient(*client_args)
(APIServer pid=137051)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=137051)     super().__init__(
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=137051)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=137051)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=137051)     next(self.gen)
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=137051)     wait_for_engine_startup(
(APIServer pid=137051)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=137051)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=137051) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=137051) [ERROR] 2025-10-29-08:32:40 (PID:137051, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

