# Issue #5648: [Bug]: qwen3-235b开启eagle3投机解码在max-num-seqs>1时TPOT异常

## 基本信息

- **编号**: #5648
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5648
- **创建时间**: 2026-01-06T08:42:43Z
- **关闭时间**: 2026-01-23T09:28:56Z
- **更新时间**: 2026-01-23T09:28:56Z
- **提交者**: @gao12312
- **评论数**: 1

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
Python platform: Linux-4.19.90-2107.6.0.0251.43.oe1.bclinux.aarch64-aarch64-with-glibc2.35

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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2.dev84+g3cf059a72 (git sha: 3cf059a72)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=5,6,7,0,1,2,3,4
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 135.9       39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          33126/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 103.8       37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          32639/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 96.3        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          32640/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 93.8        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          32640/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 101.0       44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          32639/ 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 91.8        43                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          32639/ 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.2        41                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          32639/ 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 90.8        42                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          32638/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 314487        | VLLMWorker_TP            | 129                     |
| 0       0                 | 316405        | VLLMWorker_TP            | 129                     |
| 0       0                 | 315924        | VLLMWorker_TP            | 129                     |
| 0       0                 | 315419        | VLLMWorker_TP            | 129                     |
| 0       0                 | 317396        | VLLMWorker_TP            | 129                     |
| 0       0                 | 314183        | VLLMWorker_TP            | 29229                   |
| 0       0                 | 314935        | VLLMWorker_TP            | 129                     |
| 0       0                 | 316895        | VLLMWorker_TP            | 129                     |
+===========================+===============+====================================================+
| 1       0                 | 314487        | VLLMWorker_TP            | 29275                   |
+===========================+===============+====================================================+
| 2       0                 | 314935        | VLLMWorker_TP            | 29274                   |
+===========================+===============+====================================================+
| 3       0                 | 315419        | VLLMWorker_TP            | 29275                   |
+===========================+===============+====================================================+
| 4       0                 | 315924        | VLLMWorker_TP            | 29275                   |
+===========================+===============+====================================================+
| 5       0                 | 316405        | VLLMWorker_TP            | 29275                   |
+===========================+===============+====================================================+
| 6       0                 | 316895        | VLLMWorker_TP            | 29275                   |
+===========================+===============+====================================================+
| 7       0                 | 317396        | VLLMWorker_TP            | 29275                   |
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

PD分离双机910B2启动脚本如下：

P节点：
```python
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=512
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export CPU_AFFINITY_CONF=2
#export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ASCEND_ENABLE_FUSED_MC2=1  
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0
export VLLM_ASCEND_ENABLE_NZ=2


vllm serve /workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-W8A8 \
--tensor-parallel-size 8  \
--data-parallel-size 1 \
--prefill-context-parallel-size 1 \
--decode-context-parallel-size 1 \
--cp-kv-cache-interleave-size 128 \
--enable-expert-parallel  \
--enforce-eager \
--served-model-name "qwen" \
--max-model-len 10240  \
--quantization ascend  \
--max-num-batched-tokens 7168 \
--max-num-seqs 8 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9 \
--kv-transfer-config \
  '{"kv_connector":"MooncakeConnectorV1",
  "kv_role": "kv_producer",
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
  }' \
--speculative_config '{"model": "/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-speculator.eagle3", "num_speculative_tokens": 3, "method": "eagle3", "quantization": null}
```
D节点：
```python
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=512
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export CPU_AFFINITY_CONF=2
#export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
#export DISAGGREGATED_PREFILL_RANK_TABLE_PATH="/vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1/ranktable.json"
export VLLM_ASCEND_ENABLE_FUSED_MC2=1  
#export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0
export VLLM_ASCEND_ENABLE_NZ=2


vllm serve /workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-W8A8 \
--tensor-parallel-size 8  \
--data-parallel-size 1 \
--prefill-context-parallel-size 1 \
--decode-context-parallel-size 1 \
--cp-kv-cache-interleave-size 128 \
--enable-expert-parallel  \
--served-model-name "qwen" \
--max-model-len 10240  \
--quantization ascend  \
--max-num-batched-tokens 7168 \
--max-num-seqs 8 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9 \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[4, 8, 12, 24]}' \
--kv-transfer-config \
  '{"kv_connector": "MooncakeConnectorV1",
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
  }' \
--speculative_config '{"model": "/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-speculator.eagle3", "num_speculative_tokens": 3, "method": "eagle3", "quantization": null}'\
```
evalscope压测：
```python
evalscope perf   \
    --url "http://127.0.0.1:8001/v1/chat/completions"     \
    --parallel  8 \
    --number  8 \
    --model "qwen"   \
    --log-every-n-query 100   \
    --read-timeout=1200   \
    --max-tokens  180   \
    --min-tokens 180  \
    --dataset random   \
    --max-prompt-length 1546   \
    --min-prompt-length 1546   \
    --tokenizer-path /workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-W8A8   \
    --api openai \
    --extra-args '{"ignore_eos": true}' \
    --seed 1042 \
    --stream
```

性能损失异常大，开启eagle3后TPOT从0.04到0.16，但max-num-seqs=1时不会出现此问题

max-num-seqs>1 :

不开启eagle3解码：
<img width="1296" height="1108" alt="Image" src="https://github.com/user-attachments/assets/f57af52f-46c6-42f0-9b7d-8a41375c8716" />

开启eagle3解码：
<img width="1330" height="1064" alt="Image" src="https://github.com/user-attachments/assets/fa1bdf79-6b3e-4ba8-81cb-5dbf7505a1a2" />

max-num-seqs=1同时开启eagle3解码 :
<img width="1300" height="949" alt="Image" src="https://github.com/user-attachments/assets/cd49dc98-a54d-4223-82f3-cd1b1a462fb9" />


