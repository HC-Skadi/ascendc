# Issue #4497: [Bug]: Accuracy issue for Prefill-Decode Disaggregation on Qwen2.5VL in 0.11.0rc2

## 基本信息

- **编号**: #4497
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4497
- **创建时间**: 2025-11-27T07:50:07Z
- **关闭时间**: 2025-12-08T10:00:18Z
- **更新时间**: 2025-12-08T10:00:18Z
- **提交者**: @hhd52859
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

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35

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
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc2

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
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 87.7        48                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2907 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 86.5        46                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2899 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 84.8        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 90.5        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 92.7        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 87.4        49                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2898 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 89.9        46                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2899 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 90.4        48                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2899 / 32768         |
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

P:
```shell
export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:/usr/lib64/libtcmalloc.so.4:$LD_PRELOAD
export PYTORCH_NPU_ALLOC_CONF="max_split_size_mb:250"
export CPU_AFFINITY_CONF=2

export MALLOC_CONF='background_thread:true,metadata_thp:auto,dirty_decay_ms:30000,muzzy_decay_ms:30000,abort_conf:true,percpu_arena:phycpu'

export VLLM_RPC_TIMEOUT=120
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE=AIV

unset ftp_proxy
unset https_proxy
unset http_proxy
export HCCL_IF_IP=xxx.xxx.xxx.244
export GLOO_SOCKET_IFNAME="enpxxx"  # network card name
export TP_SOCKET_IFNAME="enpxxx"
export HCCL_SOCKET_IFNAME="enpxxx"
export HCCL_BUFFSIZE=2048
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH

MODEL_PATH=/path/to/Qwen2.5-VL-72B-Instruct

vllm serve $MODEL_PATH \
  --host 0.0.0.0 --mm_processor_cache_type shm \
  --port 8004 \
  --api-server-count 1 \
  --data-parallel-size 1 \
  --tensor-parallel-size 8 \
  --data-parallel-address xxx.xxx.xxx.244 \
  --data-parallel-size-local 1 \
  --data-parallel-rpc-port 13389 \
  --distributed-executor-backend mp \
  --served-model-name qwen-vl \
  --max-model-len 32768 \
  --max-num-batched-tokens 32768 \
  --max-num_seqs 16 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_producer",
  "kv_port": "30000",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 8
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 8
             }
      }
  }'
```
d:
```shell
export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:/usr/lib64/libtcmalloc.so.4:$LD_PRELOAD
export PYTORCH_NPU_ALLOC_CONF="max_split_size_mb:250"
export CPU_AFFINITY_CONF=2

export MALLOC_CONF='background_thread:true,metadata_thp:auto,dirty_decay_ms:30000,muzzy_decay_ms:30000,abort_conf:true,percpu_arena:phycpu'

export VLLM_RPC_TIMEOUT=120
export TASK_QUEUE_ENABLE=1

export HCCL_OP_EXPANSION_MODE=AIV

unset ftp_proxy
unset https_proxy
unset http_proxy
export HCCL_IF_IP=xxx.xxx.xxx.214
export GLOO_SOCKET_IFNAME="enpxxx"  
export TP_SOCKET_IFNAME="enpxxx"
export HCCL_SOCKET_IFNAME="enpxxx"
export HCCL_BUFFSIZE=2048
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH

MODEL_PATH=/path/to/Qwen2.5-VL-72B-Instruct

vllm serve $MODEL_PATH \
  --host 0.0.0.0 --mm_processor_cache_type shm \
  --port 8004  \
  --api-server-count 1 \
  --data-parallel-size 1 \
  --data-parallel-address xxx.xxx.xxx.214 \
  --data-parallel-size-local 1 \
  --data-parallel-rpc-port 5964 \
  --tensor-parallel-size 8 \
  --distributed-executor-backend mp \
  --served-model-name qwen-vl \
  --max-model-len 32768 \
  --max-num-batched-tokens 512 \
  --no-enable-prefix-caching \
  --max-num_seqs 16 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_consumer",
  "kv_port": "30100",
  "engine_id": "1",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 8
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 8
             }
      }
  }'
```
1P1D on Qwen2.5-VL-72B-Instruct/Qwen2.5-VL-72B-Instruct-w8a8 with mooncake backend. For some input cases, the model consistently output random chars like below: 
<img width="667" height="664" alt="Image" src="https://github.com/user-attachments/assets/7782d298-852b-40e3-ba52-88f27966dd84" />  
