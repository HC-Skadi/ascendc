# Issue #4725: [Bug]: MoonCake disaggregate prefill fail to start when p and d on same machine due to port conflict

## 基本信息

- **编号**: #4725
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4725
- **创建时间**: 2025-12-04T14:50:40Z
- **关闭时间**: 2025-12-05T11:08:10Z
- **更新时间**: 2025-12-05T11:08:10Z
- **提交者**: @mitseng
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:57:00) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.152.bsk.business.7-rc2-arm64-64k-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
BIOS Model name:                    Kunpeng 920 7285Z
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU max MHz:                        3000.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng bti ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       4
NUMA node0 CPU(s):                  0-159
NUMA node1 CPU(s):                  160-319
NUMA node2 CPU(s):                  320-479
NUMA node3 CPU(s):                  480-639
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
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc3

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
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
| npu-smi 25.3.rc1.2               Version: 25.3.rc1.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 157.4       32                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          59196/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           31                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          59183/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 154.7       33                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          59208/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           30                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          59210/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 158.2       31                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          59208/ 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           30                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          59171/ 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 160.9       32                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          59197/ 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           30                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          59182/ 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 157.9       32                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3148 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           30                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2878 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 158.9       31                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3135 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           30                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 161.8       31                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3147 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           30                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2878 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 161.2       29                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3136 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           31                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 166929        |                          | 56087                   |
| 0       1                 | 166925        |                          | 56327                   |
+===========================+===============+====================================================+
| 1       0                 | 166922        |                          | 56087                   |
| 1       1                 | 166923        |                          | 56367                   |
+===========================+===============+====================================================+
| 2       0                 | 166928        |                          | 56087                   |
| 2       1                 | 166927        |                          | 56327                   |
+===========================+===============+====================================================+
| 3       0                 | 166926        |                          | 56087                   |
| 3       1                 | 166924        |                          | 56327                   |
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

start P and D instance on an A3 machine, scripts:

```bash
# decode
export VLLM_VERSION="0.11.0"
export VLLM_RPC_TIMEOUT=3600000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120
export HCCL_ENTRY_LOG_ENABLE=1
nic_name="enx00e04c6800bf"  # 根据实际情况改写
local_ip="100.102.180.194"  # 根据实际情况改写
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
# export LD_PRELOAD=/mnt/nfs/s00899273/libjemalloc.so
export HCCL_BUFFSIZE=256
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_MLAPO=1
#export VLLM_TORCH_PROFILER_DIR="./vllm_profile"
export VLLM_TORCH_PROFILER_WITH_STACK=0
export VLLM_USE_V1=1
export ASCEND_RT_VISIBLE_DEVICES=$1
export ASCEND_BUFFER_POOL=4:8
#export ASCEND_AGGREGATE_ENABLE=1
#export ASCEND_TRANSPORT_PRINT=0
#export ASCEND_A3_ENABLE=1
#export ACL_OP_INIT_MODE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
export HCCL_OP_EXPANSION_MODE="AIV"

vllm serve /data/Qwen3-235B-A22B-Instruct-2507-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port $2 \
  --data-parallel-size $3 \
  --data-parallel-rank $4 \
  --data-parallel-address $5 \
  --data-parallel-rpc-port $6 \
  --tensor-parallel-size $7 \
  --enable-expert-parallel \
  --seed 1024 \
  --served-model-name qwen \
  --max-model-len 6000 \
  --max-num-batched-tokens 16384 \
  --max-num-seqs 16 \
  --enforce-eager \
  --trust-remote-code \
  --gpu-memory-utilization 0.9  \
  --quantization ascend \
  --no-enable-prefix-caching \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_producer",
  "kv_port": "30000",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "use_ascend_direct": true,
            "prefill": {
                    "dp_size": 2,
                    "tp_size": 4
             },
             "decode": {
                    "dp_size": 8,
                    "tp_size": 1
             }
      }
  }' \
  --additional-config '{"ascend_scheduler_config":{"enabled":true,"enable_chunked_prefill":true}}'
```

```bash
# decode
export VLLM_VERSION="0.11.0"
export VLLM_RPC_TIMEOUT=3600000
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export HCCL_EXEC_TIMEOUT=204
export HCCL_CONNECT_TIMEOUT=120
export HCCL_ENTRY_LOG_ENABLE=1
export EXPERT_MAP_RECORD="true"
export DYNAMIC_EPLB="true"
nic_name="enx00e04c6800bf"  # 根据实际情况改写
local_ip="100.102.180.194"  # 根据实际情况改写
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
#export LD_PRELOAD=/mnt/nfs/s00899273/libjemalloc.so
export HCCL_BUFFSIZE=1024
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_MLAPO=1
#export VLLM_TORCH_PROFILER_DIR="./vllm_profile"
export VLLM_TORCH_PROFILER_WITH_STACK=0
export VLLM_USE_V1=1
export ASCEND_RT_VISIBLE_DEVICES=$1
export ASCEND_BUFFER_POOL=4:8
#export ASCEND_AGGREGATE_ENABLE=1
#export ASCEND_TRANSPORT_PRINT=0
#export ASCEND_A3_ENABLE=1
#export ACL_OP_INIT_MODE=1
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
export HCCL_OP_EXPANSION_MODE="AIV"

vllm serve /data/Qwen3-235B-A22B-Instruct-2507-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port $2 \
  --data-parallel-size $3 \
  --data-parallel-rank $4 \
  --data-parallel-address $5 \
  --data-parallel-rpc-port $6 \
  --tensor-parallel-size $7 \
  --enable-expert-parallel \
  --seed 1024 \
  --served-model-name qwen \
  --max-model-len 6000 \
  --max-num-batched-tokens 4096 \
  --max-num-seqs 15 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9  \
  --quantization ascend \
  --no-enable-prefix-caching \
  --async-scheduling \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY","cudagraph_capture_sizes":[5,10,15]}' \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_consumer",
  "kv_port": "30100",
  "engine_id": "1",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "use_ascend_direct": true,
            "prefill": {
                    "dp_size": 2,
                    "tp_size": 4
             },
             "decode": {
                    "dp_size": 8,
                    "tp_size": 1
             }
      }
  }' \
  --additional-config '{"lm_head_tensor_parallel_size":8}'
```

start p and d by(their paths are seperated):

```bash
# Prefill
python launch_online_dp.py --dp-size 2 --tp-size 4 --dp-size-local 2 --dp-rank-start 0 --dp-address 100.102.180.194 --dp-rpc-port 12345 --vllm-start-port 7100

# Decode
python launch_online_dp.py --dp-size 8 --tp-size 1 --dp-size-local 8 --dp-rank-start 0 --dp-address 100.102.180.194 --dp-rpc-port 12345 --vllm-start-port 7200
```

vllm error logs are:

```

(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     super().__init__(*args, **kwargs)
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1104, in __init__
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     else quant_config.get_quant_method(self, prefix))
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 126, in get_quant_method
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     return AscendFusedMoEMethod(self, prefix,
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 394, in __init__
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     self.quant_method = get_quant_method(quant_config.quant_description,
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/utils.py", line 81, in get_quant_method
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     return method_cls()
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]            ^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 137, in __init__
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597]                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:149 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 7
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597] [ERROR] 2025-12-04-14:46:07 (PID:60571, Device:0, RankID:-1) ERR02200 DIST call hccl api failed.
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597] [PID: 60571] 2025-12-04-14:46:07.669.968 Bind_Failed(EJ0003): Failed to bind the IP port. Reason: The IP address and port have been bound already.
(Worker_DP0_TP0_EP0 pid=60571) ERROR 12-04 14:46:08 [multiproc_executor.py:597] 
(Worker_DP0_TP0_EP0 pid=60571) INFO 12-04 14:46:08 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP1_EP1 pid=60615) INFO 12-04 14:46:08 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP3_EP3 pid=60777) INFO 12-04 14:46:08 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP2_EP2 pid=60695) INFO 12-04 14:46:08 [multiproc_executor.py:558] Parent process exited, terminating worker
```
the later instance will crash: start p first, d crash; start d first, p crash.
the plog shows this log(repeat 8 copies):

```
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.312 [hccl_socket.cc:106] [60570][HcclSocket][Listen] socket type[0], listen on ip[192.2.2.195] and specific port[16666] fail. Please check the port status and whether the port is being used by other process.
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.316 [hccl_socket_manager.cc:54] [60570][ServerInit]call trace: hcclRet -> 7
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.320 [hccl_communicator_host.cc:1208] [60570][InitRaResource]call trace: hcclRet -> 7
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.322 [hccl_communicator.cc:196] [60570][InitNetResource]call trace: hcclRet -> 7
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.323 [hccl_communicator_host.cc:274] [60570][Init]call trace: hcclRet -> 7
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.325 [hccl_comm.cc:115] [60570][HcclComm][Init]errNo[0x0000000005000007] hccl initialize failed
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.327 [op_base.cc:1097] [60570][InitCommRootInfo]errNo[0x0000000005000007] hcclComm init error
[ERROR] HCCP(60570,):2025-12-04-14:46:07.911.347 [rs_socket.c:2930]tid:60570,rs_peer_get_ifnum : param error, g_rs_cb is NULL
[ERROR] HCCP(60570,):2025-12-04-14:46:07.911.348 [ra_peer.c:879]tid:60570,ra_peer_get_ifnum : [get][ra_peer_ifnum]rs_peer_get_ifnum failed(-22)
[ERROR] HCCP(60570,):2025-12-04-14:46:07.911.354 [ra_host.c:1692]tid:60570,ra_get_ifnum : [get][ra_ifnum]ra_peer_get_ifnum failed, ret(-22)
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.356 [adapter_hccp.cc:1621] [60570][Get][IfNum]errNo[0x000000000500000b] ra get if num fail. ret[128303], num[0]
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.358 [adapter_hccp.cc:1493] [60570][hrtGetHostIf]call trace: hcclRet -> 11
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.360 [sal.cc:349] [60570][GetLocalHostIP]call trace: hcclRet -> 11
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.362 [op_base.cc:1166] [60570][InitCommRootInfo]Init failed, return[0x0000000005000007], rankNum[8], rank[4], rootInfo identifier[group_name_53], server[0.0.0.0], logicDevId[0]
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.379 [op_base.cc:2339] [60570][HcclCommDestroy] comm is not exist, comm=0xaaadf98aec10, group=group_name_53, deviceLogicId=0
[ERROR] HCCL(60570,):2025-12-04-14:46:07.911.556 [op_base.cc:1309] [60570][Init][CommRootInfoConfigInner]errNo[0x0000000005000007]HcclCommInitRootInfoConfigInner failed.
```


