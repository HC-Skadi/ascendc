# Issue #5493: [Bug]: Atlas A2 start qwen3-235B-A22B in 2 node mode failed, error: launch failed for Slice, errno:361001

## 基本信息

- **编号**: #5493
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5493
- **创建时间**: 2025-12-29T13:39:57Z
- **关闭时间**: 2026-01-29T06:10:34Z
- **更新时间**: 2026-01-29T06:10:34Z
- **提交者**: @leo-pony
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.35

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
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.2.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2.dev5+g3e67e8276 (git sha: 3e67e8276)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=6,7,0,1,2,3,4,5
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:254
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 97.1        35                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 93.7        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3430 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 92.4        35                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3431 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 95.5        36                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 93.7        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3433 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 94.1        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3430 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 95.2        34                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3430 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 96.2        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3436 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

Failed test cases:
```
test_name: "test Qwen3-235B-A22B multi-dp on A2"
model: "Qwen/Qwen3-235B-A22B"
num_nodes: 2
npu_per_node: 8
env_common:
  VLLM_USE_MODELSCOPE: true
  OMP_PROC_BIND: false
  OMP_NUM_THREADS: 1
  HCCL_BUFFSIZE: 1024
  SERVER_PORT: 8080
  NUMEXPR_MAX_THREADS: 128
  TASK_QUEUE_ENABLE: 1
  PYTORCH_NPU_ALLOC_CONF: expandable_segments:True

deployment:
  -
    server_cmd: >
        vllm serve "Qwen/Qwen3-235B-A22B"
        --host 0.0.0.0
        --port $SERVER_PORT
        --data-parallel-size 2
        --data-parallel-size-local 1
        --data-parallel-address $LOCAL_IP
        --data-parallel-rpc-port 13389
        --tensor-parallel-size 8
        --seed 1024
        --enable-expert-parallel
        --max-num-seqs 128
        --max-model-len 40960
        --max-num-batched-tokens 256
        --trust-remote-code
        --gpu-memory-utilization 0.9
        --async-scheduling
  -
    server_cmd: >
        vllm serve "Qwen/Qwen3-235B-A22B"
        --headless
        --data-parallel-size 2
        --data-parallel-size-local 1
        --data-parallel-start-rank 1
        --data-parallel-address $MASTER_IP
        --data-parallel-rpc-port 13389
        --tensor-parallel-size 8
        --seed 1024
        --max-num-seqs 128
        --max-model-len 40960
        --max-num-batched-tokens 256
        --enable-expert-parallel
        --trust-remote-code
        --gpu-memory-utilization 0.9
        --async-scheduling
benchmarks:
  perf:
    case_type: performance
    dataset_path: vllm-ascend/GSM8K-in3500-bs2800
    request_conf: vllm_api_stream_chat
    dataset_conf: gsm8k/gsm8k_gen_0_shot_cot_str_perf
    num_prompts: 2800
    max_out_len: 1500
    batch_size: 256
    request_rate: 4.8
    baseline: 1
    threshold: 0.97
  acc:
    case_type: accuracy
    dataset_path: vllm-ascend/gsm8k-lite
    request_conf: vllm_api_general_chat
    dataset_conf: gsm8k/gsm8k_gen_0_shot_cot_chat_prompt
    max_out_len: 7680
    batch_size: 256
    baseline: 96
    threshold: 5

```

Master node error log:
```
(Worker_DP0_TP5_EP5 pid=364) INFO 12-29 13:11:50 [model_runner_v1.py:2233] Loading model weights took 28.4835 GB
(Worker_DP0_TP0_EP0 pid=359) INFO 12-29 13:12:17 [backends.py:643] Using cache directory: /root/.cache/vllm/torch_compile_cache/9554a7af62/rank_0_0/backbone for vLLM's torch.compile
(Worker_DP0_TP0_EP0 pid=359) INFO 12-29 13:12:17 [backends.py:703] Dynamo bytecode transform time: 26.01 s
(EngineCore_DP0 pid=336) INFO 12-29 13:12:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(Worker_DP0_TP0_EP0 pid=359) INFO 12-29 13:13:14 [backends.py:278] Compiling a graph for compile range (1, 256) takes 53.67 s
(EngineCore_DP0 pid=336) INFO 12-29 13:13:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:14:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:15:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:16:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:17:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:18:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:19:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:20:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=336) INFO 12-29 13:21:50 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
[rank0]:[E1229 13:22:33.992084477 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 NPU function error: call aclnnRmsNorm failed, error code is 507014
[ERROR] 2025-12-29-13:22:33 (PID:359, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
[PID: 359] 2025-12-29-13:22:33.941.084 AclNN_Runtime_Error(EZ9903): rtKernelLaunchWithHandleV2 failed: 507014
        Solution: In this scenario, collect the plog when the fault occurs and locate the fault based on the plog.
        TraceBack (most recent call last):
        The error from device(chipId:0, dieId:0), serial number is 13, there is an exception of fftsplus aivector error, core id is 3, error code = 0, dump info: pc start: 0x12c0814211d0, current: 0x12c081423a3c, vec error info: 0x221e175130, mte error info: 0x7f398b6f4d, ifu error info: 0x2cd61292fec00, ccu error info: 0x1188a87d63609d9b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c140340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:333]
        The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x98b6f4d, fixp_error1 info: 0x7f, fsmId:0, tslot:4, thread:0, ctxid:0, blk:42, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:353]
        Kernel task happen error, retCode=0x25, [aicore timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1555]
        AICORE Kernel task happen error, retCode=0x25.[FUNC:GetError][FILE:stream.cc][LINE:1191]
        Failed to submit kernel task, retCode=0x7150025.[FUNC:LaunchKernelSubmit][FILE:context.cc][LINE:1164]
        kernel launch submit failed.[FUNC:LaunchKernelWithHandle][FILE:context.cc][LINE:1428]
        rtKernelLaunchWithHandleV2 execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        rtKernelLaunchWithHandleV2 failed: 507014
        #### KernelLaunch failed: /usr/local/Ascend/ascend-toolkit/8.3.RC2/opp/built-in/op_impl/ai_core/tbe//kernel/ascend910b/slice/Slice_ee29dafe4fe21e12bb8d56ae91626cba_high_performance.o
        Kernel Run failed. opType: 32, Slice
        launch failed for Slice, errno:361001.
        Check aclnnContiguous(inWorkspace, inContWorkspaceSize, aclInExecutor, stream) failed

Exception raised from operator() at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff892148c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff891bc140 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1b640c8 (0xffff761240c8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x29f0894 (0xffff76fb0894 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x9cc700 (0xffff74f8c700 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x9cd2dc (0xffff74f8d2dc in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9cb1f8 (0xffff74f8b1f8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xd29cc (0xffff96df29cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x80398 (0xffff96fd0398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe9e9c (0xffff97039e9c in /lib/aarch64-linux-gnu/libc.so.6)

(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2205, in profile_run
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     super().profile_run()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4484, in profile_run
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     self._sync_device()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 364, in _sync_device
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     torch.npu.synchronize()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 72, in synchronize
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     return torch_npu._C._npu_synchronize()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnRmsNorm.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] [ERROR] 2025-12-29-13:22:33 (PID:359, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2205, in profile_run
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     super().profile_run()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4484, in profile_run
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     self._sync_device()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 364, in _sync_device
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     torch.npu.synchronize()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 72, in synchronize
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]     return torch_npu._C._npu_synchronize()
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnRmsNorm.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824] [ERROR] 2025-12-29-13:22:33 (PID:359, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]
(Worker_DP0_TP0_EP0 pid=359) ERROR 12-29 13:22:33 [multiproc_executor.py:824]
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] EngineCore failed to start.
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] Traceback (most recent call last):
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 853, in run_engine_core
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     super().__init__(
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     super().__init__(
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 240, in _initialize_kv_caches
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     return aggregate(get_response())
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866]     raise RuntimeError(
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnRmsNorm.
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] [ERROR] 2025-12-29-13:22:33 (PID:359, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=336) ERROR 12-29 13:22:33 [core.py:866] ', please check the stack trace above for the root cause
[rank7]:[E1229 13:22:34.117361194 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 NPU function error: call aclnnRmsNorm failed, error code is 507014
[ERROR] 2025-12-29-13:22:34 (PID:366, Device:7, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
[PID: 366] 2025-12-29-13:22:34.070.507 AclNN_Runtime_Error(EZ9903): rtKernelLaunchWithHandleV2 failed: 507014
        Solution: In this scenario, collect the plog when the fault occurs and locate the fault based on the plog.
        TraceBack (most recent call last):
        The error from device(chipId:7, dieId:0), serial number is 12, there is an exception of fftsplus aivector error, core id is 1, error code = 0, dump info: pc start: 0x12c0814211d0, current: 0x12c081423a3c, vec error info: 0x6604a60208, mte error info: 0x720301c0ba, ifu error info: 0x7b13152ebcdc0, ccu error info: 0x889a01d7081a3ef, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c140340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:333]
        The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x301c0ba, fixp_error1 info: 0x72, fsmId:0, tslot:6, thread:0, ctxid:0, blk:18, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:353]
        Kernel task happen error, retCode=0x25, [aicore timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1555]
        AICORE Kernel task happen error, retCode=0x25.[FUNC:GetError][FILE:stream.cc][LINE:1191]
        Failed to submit kernel task, retCode=0x7150025.[FUNC:LaunchKernelSubmit][FILE:context.cc][LINE:1164]
        kernel launch submit failed.[FUNC:LaunchKernelWithHandle][FILE:context.cc][LINE:1428]
        rtKernelLaunchWithHandleV2 execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        rtKernelLaunchWithHandleV2 failed: 507014
        #### KernelLaunch failed: /usr/local/Ascend/ascend-toolkit/8.3.RC2/opp/built-in/op_impl/ai_core/tbe//kernel/ascend910b/slice/Slice_ee29dafe4fe21e12bb8d56ae91626cba_high_performance.o
        Kernel Run failed. opType: 32, Slice
        launch failed for Slice, errno:361001.
        Check aclnnContiguous(inWorkspace, inContWorkspaceSize, aclInExecutor, stream) failed

Exception raised from operator() at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff9e8348c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff9e7dc140 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1b640c8 (0xffff8b7440c8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x29f0894 (0xffff8c5d0894 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x9cc700 (0xffff8a5ac700 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x9cd2dc (0xffff8a5ad2dc in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9cb1f8 (0xffff8a5ab1f8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xd29cc (0xffffac4029cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x80398 (0xffffac5e0398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe9e9c (0xffffac649e9c in /lib/aarch64-linux-gnu/libc.so.6)

[366] [2025-12-29 13:22:34:096] torch.distributed: [ERROR] [546] Find exception when finishedNPUExecutionInternal, query:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 NPU function error: acl::AclQueryEventRecordedStatus(event_, &currStatus), error code is 507014
[ERROR] 2025-12-29-13:22:34 (PID:366, Device:7, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtEventQueryStatus execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999[PID: 366] 2025-12-29-13:22:34.092.455 (EH9999):  [Query][Status]query event recorded status failed, runtime result = 507014[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
        TraceBack (most recent call last):

Exception raised from query at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<c
[rank7]:[E1229 13:22:34.138773119 compiler_depend.ts:1675] [Rank 7] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:34 (PID:366, Device:7, RankID:-1) ERR02005 DIST internal error
terminate called after throwing an instance of 'std::runtime_error'
  what():  [Rank 7] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:34 (PID:366, Device:7, RankID:-1) ERR02005 DIST internal error
[359] [2025-12-29 13:22:34:129] torch.distributed: [ERROR] [547] Find exception when finishedNPUExecutionInternal, query:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 NPU function error: acl::AclQueryEventRecordedStatus(event_, &currStatus), error code is 507014
[ERROR] 2025-12-29-13:22:34 (PID:359, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtEventQueryStatus execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999[PID: 359] 2025-12-29-13:22:34.122.799 (EH9999):  [Query][Status]query event recorded status failed, runtime result = 507014[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
        TraceBack (most recent call last):

Exception raised from query at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<c
[rank0]:[E1229 13:22:34.172152229 compiler_depend.ts:1675] [Rank 0] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:34 (PID:359, Device:0, RankID:-1) ERR02005 DIST internal error
terminate called after throwing an instance of 'std::runtime_error'
  what():  [Rank 0] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:34 (PID:359, Device:0, RankID:-1) ERR02005 DIST internal error
[W1229 13:22:34.299774068 compiler_depend.ts:545] Warning: NPU warning, error code is 507014[Error]:
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
EZ9999: Inner Error!
EZ9999[PID: 359] 2025-12-29-13:22:34.252.439 (EZ9999):  [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1191]
        TraceBack (most recent call last):
       [AIC_INFO] after execute:mixCtx print end[FUNC:GetError][FILE:stream.cc][LINE:1191]
       Aicore kernel execute failed, device_id=0, stream_id=2, report_stream_id=2, task_id=45242, flip_num=0, fault kernel_name=MoeDistributeDispatchV2_ND_ND_BF16_BF16_high_performance_2000001000, fault kernel info ext=none, program id=59, hash=15758014642305588516.[FUNC:GetError][FILE:stream.cc][LINE:1191]
       rtDeviceSynchronizeWithTimeout execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       wait for compute device to finish failed, runtime result = 507014.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
 (function npuSynchronizeUsedDevices)
[W1229 13:22:34.303199836 compiler_depend.ts:527] Warning: NPU warning, error code is 507014[Error]:
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999[PID: 359] 2025-12-29-13:22:34.258.612 (EH9999):  wait for compute device to finish failed, runtime result = 507014.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[rank1]:[E1229 13:22:34.496173985 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 NPU function error: call aclnnRmsNorm failed, error code is 507014
[ERROR] 2025-12-29-13:22:34 (PID:360, Device:1, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
[PID: 360] 2025-12-29-13:22:34.447.110 AclNN_Runtime_Error(EZ9903): rtKernelLaunchWithHandleV2 failed: 507014
        Solution: In this scenario, collect the plog when the fault occurs and locate the fault based on the plog.
        TraceBack (most recent call last):
        The error from device(chipId:1, dieId:0), serial number is 9, there is an exception of fftsplus aivector error, core id is 0, error code = 0, dump info: pc start: 0x12c0814211d0, current: 0x12c081423a3c, vec error info: 0x5b1355e261, mte error info: 0xf9af19e078, ifu error info: 0x2c2e2b23ecc00, ccu error info: 0x3713d4237bbb0fe4, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c140340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:333]
        The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0xf19e078, fixp_error1 info: 0xf9, fsmId:0, tslot:5, thread:0, ctxid:0, blk:29, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:353]
        Kernel task happen error, retCode=0x25, [aicore timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1555]
        AICORE Kernel task happen error, retCode=0x25.[FUNC:GetError][FILE:stream.cc][LINE:1191]
        Failed to submit kernel task, retCode=0x7150025.[FUNC:LaunchKernelSubmit][FILE:context.cc][LINE:1164]
        kernel launch submit failed.[FUNC:LaunchKernelWithHandle][FILE:context.cc][LINE:1428]
        rtKernelLaunchWithHandleV2 execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        rtKernelLaunchWithHandleV2 failed: 507014
        #### KernelLaunch failed: /usr/local/Ascend/ascend-toolkit/8.3.RC2/opp/built-in/op_impl/ai_core/tbe//kernel/ascend910b/slice/Slice_ee29dafe4fe21e12bb8d56ae91626cba_high_performance.o
        Kernel Run failed. opType: 32, Slice
        launch failed for Slice, errno:361001.
        Check aclnnContiguous(inWorkspace, inContWorkspaceSize, aclInExecutor, stream) failed
```

Slave node error log:
```
(Worker_DP1_TP0_EP8 pid=1264) INFO 12-29 13:13:15 [backends.py:278] Compiling a graph for compile range (1, 256) takes 54.05 s
(EngineCore_DP1 pid=1250) INFO 12-29 13:13:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:14:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:15:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:16:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:17:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:18:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:19:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:20:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:21:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP1 pid=1250) INFO 12-29 13:22:22 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
[1270] [2025-12-29 13:22:36:099] torch.distributed: [ERROR] [1449] Find exception when finishedNPUExecutionInternal, query:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 NPU function error: acl::AclQueryEventRecordedStatus(event_, &currStatus), error code is 507014
[ERROR] 2025-12-29-13:22:36 (PID:1270, Device:6, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtEventQueryStatus execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999[PID: 1270] 2025-12-29-13:22:36.090.922 (EH9999):  [Query][Status]query event recorded status failed, runtime result = 507014[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
        TraceBack (most recent call last):

Exception raised from query at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:59 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator
[rank14]:[E1229 13:22:36.548853401 compiler_depend.ts:1675] [Rank 6] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:36 (PID:1270, Device:6, RankID:-1) ERR02005 DIST internal error
terminate called after throwing an instance of 'std::runtime_error'
  what():  [Rank 6] HCCL watchdog thread terminated with exception:
[ERROR] 2025-12-29-13:22:36 (PID:1270, Device:6, RankID:-1) ERR02005 DIST internal error
[rank9]:[E1229 13:22:36.108824998 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 NPU function error: call aclnnRmsNorm failed, error code is 507014
[ERROR] 2025-12-29-13:22:36 (PID:1265, Device:1, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
[PID: 1265] 2025-12-29-13:22:36.650.724 AclNN_Runtime_Error(EZ9903): rtKernelLaunchWithHandleV2 failed: 507014
        Solution: In this scenario, collect the plog when the fault occurs and locate the fault based on the plog.
        TraceBack (most recent call last):
        The error from device(chipId:1, dieId:0), serial number is 18, there is an exception of fftsplus aivector error, core id is 1, error code = 0, dump info: pc start: 0x12c0814211d0, current: 0x12c081423a3c, vec error info: 0x6b1110230a, mte error info: 0x73491042d0, ifu error info: 0x7391f3ff0e380, ccu error info: 0x4b7f2d8e08630071, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c140340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:333]
        The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x91042d0, fixp_error1 info: 0x73, fsmId:0, tslot:4, thread:0, ctxid:0, blk:42, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:353]
        Kernel task happen error, retCode=0x25, [aicore timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1555]
        AICORE Kernel task happen error, retCode=0x25.[FUNC:GetError][FILE:stream.cc][LINE:1191]
        Failed to submit kernel task, retCode=0x7150025.[FUNC:LaunchKernelSubmit][FILE:context.cc][LINE:1164]
        kernel launch submit failed.[FUNC:LaunchKernelWithHandle][FILE:context.cc][LINE:1428]
        rtKernelLaunchWithHandleV2 execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        rtKernelLaunchWithHandleV2 failed: 507014
        #### KernelLaunch failed: /usr/local/Ascend/ascend-toolkit/8.3.RC2/opp/built-in/op_impl/ai_core/tbe//kernel/ascend910b/slice/Slice_ee29dafe4fe21e12bb8d56ae91626cba_high_performance.o
        Kernel Run failed. opType: 32, Slice
        launch failed for Slice, errno:361001.
        Check aclnnContiguous(inWorkspace, inContWorkspaceSize, aclInExecutor, stream) failed

Exception raised from operator() at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff8eb348c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff8eadc140 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x1b640c8 (0xffff7ba440c8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x29f0894 (0xffff7c8d0894 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x9cc700 (0xffff7a8ac700 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x9cd2dc (0xffff7a8ad2dc in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9cb1f8 (0xffff7a8ab1f8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xd29cc (0xffff9c7029cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x80398 (0xffff9c8e0398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe9e9c (0xffff9c949e9c in /lib/aarch64-linux-gnu/libc.so.6)

(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2205, in profile_run
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     super().profile_run()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4484, in profile_run
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     self._sync_device()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 364, in _sync_device
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     torch.npu.synchronize()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 72, in synchronize
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     return torch_npu._C._npu_synchronize()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnRmsNorm.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] [ERROR] 2025-12-29-13:22:36 (PID:1265, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2205, in profile_run
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     super().profile_run()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4484, in profile_run
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     self._sync_device()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 364, in _sync_device
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     torch.npu.synchronize()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 72, in synchronize
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]     return torch_npu._C._npu_synchronize()
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is aclnnRmsNorm.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824] [ERROR] 2025-12-29-13:22:36 (PID:1265, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]
(Worker_DP1_TP1_EP9 pid=1265) ERROR 12-29 13:22:36 [multiproc_executor.py:824]
[rank14]:[E1229 13:22:36.183034102 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:34 NPU function error: call aclnnRmsNorm failed, error code is 507014
[ERROR] 2025-12-29-13:22:36 (PID:1270, Device:6, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicore execution times out.
        Rectify the fault based on the error information in the ascend log.
[PID: 1270] 2025-12-29-13:22:36.717.430 AclNN_Runtime_Error(EZ9903): rtKernelLaunchWithHandleV2 failed: 507014
        Solution: In this scenario, collect the plog when the fault occurs and locate the fault based on the plog.
        TraceBack (most recent call last):
        The error from device(chipId:6, dieId:0), serial number is 12, there is an exception of fftsplus aivector error, core id is 1, error code = 0, dump info: pc start: 0x12c0814211d0, current: 0x12c081423838, vec error info: 0x411273dc10, mte error info: 0xf85fd8e628, ifu error info: 0x3d010197cc000, ccu error info: 0x5c3dfe8e70321280, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c140340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:333]
        The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0xfd8e628, fixp_error1 info: 0xf8, fsmId:0, tslot:2, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:353]
        Kernel task happen error, retCode=0x25, [aicore timeout].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1555]
        AICORE Kernel task happen error, retCode=0x25.[FUNC:GetError][FILE:stream.cc][LINE:1191]
        Failed to submit kernel task, retCode=0x7150025.[FUNC:LaunchKernelSubmit][FILE:context.cc][LINE:1164]
        kernel launch submit failed.[FUNC:LaunchKernelWithHandle][FILE:context.cc][LINE:1428]
        rtKernelLaunchWithHandleV2 execute failed, reason=[aicore timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        rtKernelLaunchWithHandleV2 failed: 507014
        #### KernelLaunch failed: /usr/local/Ascend/ascend-toolkit/8.3.RC2/opp/built-in/op_impl/ai_core/tbe//kernel/ascend910b/slice/Slice_ee29dafe4fe21e12bb8d56ae91626cba_high_performance.o
        Kernel Run failed. opType: 32, Slice
        launch failed for Slice, errno:361001.
        Check aclnnContiguous(inWorkspace, inContWorkspaceSize, aclInExecutor, stream) failed
```
