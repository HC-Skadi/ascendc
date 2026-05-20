# Issue #5527: [Bug]: A2 DeepSeek-V3.2 SingleNode  Start Error

## 基本信息

- **编号**: #5527
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5527
- **创建时间**: 2025-12-30T10:28:02Z
- **关闭时间**: 2026-01-07T15:33:47Z
- **更新时间**: 2026-01-07T15:33:47Z
- **提交者**: @flyrae
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands hereCollecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r2220_156.hce2.aarch64-aarch64-with-glibc2.35

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
Core(s) per cluster:                  48
Socket(s):                            -
Cluster(s):                           4
Stepping:                             0x1
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=3,4,5,6,7,0,1,2
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ASCEND_910_ENABLE=true
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
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.2        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3440 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 100.8       39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 95.0        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3440 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.7        36                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.1        42                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3440 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 96.2        42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 97.7        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 98.5        42                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3439 / 65536         |
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

vllm ascend:0.13.0rc1
deploy DeepSeek-V3.2  on single node （2 Altlas A2）with tp4 and dp4
**node 0  Error**: full log see attachment
<details>
<summary>node0 error log</summary>
``` log
le "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1995, in _dummy_run
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]     with_prefill) = self._sync_metadata_across_dp(num_tokens,
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]     return func(*args, **kwargs)
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824]     work.wait()
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [172.16.0.147]:5006
[0;36m(Worker_DP2_TP1_EP9 pid=329)[0;0m [0;36m(Worker_DP3_TP1_EP13 pid=332)[0;0m ERROR 12-30 02:53:10 [multiproc_executor.py:824] WorkerProc hit an exception.
```
</details>
**node 0  Error**: full log see attachment
<details>
<summary>node1 error log</summary>
``` log  
[0;36m(EngineCore_DP2 pid=215)[0;0m Traceback (most recent call last):
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_balance_schedule.py", line 657, in run_engine_core
[0;36m(EngineCore_DP2 pid=215)[0;0m     engine_core = BalanceDPEngineCoreProc(*args, **kwargs)
[0;36m(EngineCore_DP2 pid=215)[0;0m                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
[0;36m(EngineCore_DP2 pid=215)[0;0m     super().__init__(
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
[0;36m(EngineCore_DP2 pid=215)[0;0m     super().__init__(
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
[0;36m(EngineCore_DP2 pid=215)[0;0m     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
[0;36m(EngineCore_DP2 pid=215)[0;0m                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 240, in _initialize_kv_caches
[0;36m(EngineCore_DP2 pid=215)[0;0m     available_gpu_memory = self.model_executor.determine_available_memory()
[0;36m(EngineCore_DP2 pid=215)[0;0m                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
[0;36m(EngineCore_DP2 pid=215)[0;0m     return self.collective_rpc("determine_available_memory")
[0;36m(EngineCore_DP2 pid=215)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
[0;36m(EngineCore_DP2 pid=215)[0;0m     return aggregate(get_response())
[0;36m(EngineCore_DP2 pid=215)[0;0m                      ^^^^^^^^^^^^^^
[0;36m(EngineCore_DP2 pid=215)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
[0;36m(EngineCore_DP2 pid=215)[0;0m     raise RuntimeError(
[0;36m(EngineCore_DP2 pid=215)[0;0m RuntimeError: Worker failed with error '[/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [172.16.0.147]:10634', please check the stack trace above for the root cause
```

</details>

node0.sh
```  bash
#!/bin/sh

# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="eth0"
local_ip="172.16.0.171"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="172.16.0.171"

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is install on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0
export HCCL_OP_EXPANSION_MODE="AIV"
#export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
vllm serve /models \
    --host 0.0.0.0 \
    --port 8000 \
    --data-parallel-size 4 \
    --data-parallel-size-local 2 \
    --data-parallel-address $node0_ip \
    --data-parallel-rpc-port 13389 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --seed 1024 \
    --served-model-name DeepSeek-V3.2 \
    --enable-expert-parallel \
    --async-scheduling \
    --max-num-seqs 8 \
    --max-model-len 12288\
    --max-num-batched-tokens 4096 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.95 \
    --tokenizer-mode deepseek_v32 \
    --tool-call-parser deepseek_v32 \
    --enable-auto-tool-choice \
    --speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' \
    --compilation-config '{"cudagraph_capture_sizes":[4,16,32,48], "cudagraph_mode": "FULL_DECODE_ONLY"}'

```

node1.sh
``` bash
#!/bin/sh

# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip of the current node
nic_name="eth0"
local_ip="172.16.0.147"

# The value of node0_ip must be consistent with the value of local_ip set in node0 (master node)
node0_ip="172.16.0.171"

# [Optional] jemalloc
# jemalloc is for better performance, if `libjemalloc.so` is install on your machine, you can turn it on.
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0
export HCCL_OP_EXPANSION_MODE="AIV"
#export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
vllm serve /models \
    --host 0.0.0.0 \
    --port 8000 \
    --headless \
    --data-parallel-size 4 \
    --data-parallel-size-local 2 \
    --data-parallel-start-rank 2 \
    --data-parallel-address $node0_ip \
    --data-parallel-rpc-port 13389 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --seed 1024 \
    --served-model-name DeepSeek-V3.2 \
    --enable-expert-parallel \
    --async-scheduling \
    --max-num-seqs 16 \
    --max-model-len 12288 \
    --max-num-batched-tokens 4096 \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.95 \
    --tokenizer-mode deepseek_v32 \
    --tool-call-parser deepseek_v32 \
    --enable-auto-tool-choice \
    --speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' \
    --compilation-config '{"cudagraph_capture_sizes":[4,16,32,48], "cudagraph_mode": "FULL_DECODE_ONLY"}'

[node0.log](https://github.com/user-attachments/files/24380668/node0.log)
[node1.log](https://github.com/user-attachments/files/24380669/node1.log)
[run_node0.sh](https://github.com/user-attachments/files/24380671/run_node0.sh)
[run_node1.sh](https://github.com/user-attachments/files/24380670/run_node1.sh)

```
