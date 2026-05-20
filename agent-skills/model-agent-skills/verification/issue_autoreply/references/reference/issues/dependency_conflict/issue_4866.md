# Issue #4866: [Bug]: disaggregated_prefill_decode Mooncake transfer failed for request cmpl in decode

## 基本信息

- **编号**: #4866
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4866
- **创建时间**: 2025-12-10T03:30:03Z
- **关闭时间**: 2025-12-12T08:31:49Z
- **更新时间**: 2025-12-12T08:31:49Z
- **提交者**: @ZRJ026
- **评论数**: 9

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
Python platform: Linux-5.10.0-136.12.0.88.4.ctl3.aarch64-aarch64-with-glibc2.35

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
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
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
ASCEND_MF_STORE_URL=tcp://inference-deepseek-w8a8-pd-prefill-0.inference-deepseek-w8a8-pd-prefill:22222
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
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
| 0     910B2               | OK            | 97.8        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          60126/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 94.9        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          60235/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 98.0        36                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          60234/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 96.0        36                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          60234/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 94.6        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          60235/ 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 97.6        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          60232/ 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 96.3        36                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          60233/ 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 93.1        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          60231/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 2759218       | VLLMWorker_DP            | 56293                   |
+===========================+===============+====================================================+
| 1       0                 | 2759615       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 2       0                 | 2760054       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 3       0                 | 2760301       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 4       0                 | 2760849       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 5       0                 | 2762399       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 6       0                 | 2762902       | VLLMWorker_DP            | 56415                   |
+===========================+===============+====================================================+
| 7       0                 | 2763344       | VLLMWorker_DP            | 56415                   |
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

I followed the reference document
https://github.com/vllm-project/vllm-ascend/blob/main/examples/disaggregated_prefill_v1/mooncake_connector_deployment_guide.md

to run PD disaggregation in a 1P1D setup using the model:
https://modelscope.cn/models/vllm-ascend/DeepSeek-R1-0528-W8A8
.
Both the Prefill (P) and Decode (D) sides use 2 pods each, with 8× 910B GPUs per pod.
The base image used is m.daocloud.io/quay.io/ascend/vllm-ascend:v0.11.0rc2, and MoonCake has been installed.

Below are the startup commands for the four pods.
```python
# Prefill0-Pod0
HCCL_EXEC_TIMEOUT=204 HCCL_CONNECT_TIMEOUT=120 HCCL_IF_IP=$(hostname -i) GLOO_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME=eth0 HCCL_SOCKET_IFNAME=eth0  vllm serve /data/models --served-model-name inference-deepseek-w8a8-pd --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1024 --max-model-len 2000  --max-num-batched-tokens 2000  --trust-remote-code  --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-address ${HCCL_IF_IP}   --data-parallel-rpc-port 9100  --quantization ascend --kv-transfer-config '{"kv_connector":"MooncakeConnectorV1","kv_buffer_device":"npu","kv_role":"kv_producer","kv_parallel_size":1,"kv_port":"20001","engine_id":"0","kv_rank":0,"kv_connector_module_path":"vllm_ascend.distributed.mooncake_connector","kv_connector_extra_config":{"prefill":{"dp_size":2,"tp_size":8},"decode":{"dp_size":2,"tp_size":8}}}'
```
```python
# Prefill0-Pod1
HCCL_EXEC_TIMEOUT=204 HCCL_CONNECT_TIMEOUT=120 HCCL_IF_IP=$(hostname -i) GLOO_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME=eth0 HCCL_SOCKET_IFNAME=eth0  vllm serve /data/models --served-model-name inference-deepseek-w8a8-pd --headless --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1024 --max-model-len 2000  --max-num-batched-tokens 2000  --trust-remote-code  --data-parallel-size 2 --data-parallel-size-local 1  --data-parallel-start-rank $LWS_WORKER_INDEX --data-parallel-address ${Preill0_POD0_IP}   --data-parallel-rpc-port 9100  --quantization ascend --kv-transfer-config '{"kv_connector":"MooncakeConnectorV1","kv_buffer_device":"npu","kv_role":"kv_producer","kv_parallel_size":1,"kv_port":"20001","engine_id":"0","kv_rank":0,"kv_connector_module_path":"vllm_ascend.distributed.mooncake_connector","kv_connector_extra_config":{"prefill":{"dp_size":2,"tp_size":8},"decode":{"dp_size":2,"tp_size":8}}}'
```
```python
# Decode0-Pod0
HCCL_EXEC_TIMEOUT=204 HCCL_CONNECT_TIMEOUT=120 HCCL_IF_IP=$(hostname -i) GLOO_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME=eth0 HCCL_SOCKET_IFNAME=eth0  vllm serve /data/models --served-model-name inference-deepseek-w8a8-pd --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1024 --max-model-len 2000  --max-num-batched-tokens 2000  --trust-remote-code  --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-address ${HCCL_IF_IP}   --data-parallel-rpc-port 9100  --quantization ascend --kv-transfer-config '{"kv_connector":"MooncakeConnectorV1","kv_buffer_device":"npu","kv_role":"kv_consumer","kv_parallel_size":1,"kv_port":"20001","engine_id":"1","kv_rank":1,"kv_connector_module_path":"vllm_ascend.distributed.mooncake_connector","kv_connector_extra_config":{"prefill":{"dp_size":2,"tp_size":8},"decode":{"dp_size":2,"tp_size":8}}}'
```
```python
# Decode0-Pod1
HCCL_EXEC_TIMEOUT=204 HCCL_CONNECT_TIMEOUT=120 HCCL_IF_IP=$(hostname -i) GLOO_SOCKET_IFNAME=eth0 TP_SOCKET_IFNAME=eth0 HCCL_SOCKET_IFNAME=eth0  vllm serve /data/models --served-model-name inference-deepseek-w8a8-pd --headless --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1024 --max-model-len 2000  --max-num-batched-tokens 2000  --trust-remote-code  --data-parallel-size 2 --data-parallel-size-local 1  --data-parallel-start-rank $LWS_WORKER_INDEX --data-parallel-address ${Decode0_POD0_IP}   --data-parallel-rpc-port 9100  --quantization ascend --kv-transfer-config '{"kv_connector":"MooncakeConnectorV1","kv_buffer_device":"npu","kv_role":"kv_consumer","kv_parallel_size":1,"kv_port":"20001","engine_id":"1","kv_rank":1,"kv_connector_module_path":"vllm_ascend.distributed.mooncake_connector","kv_connector_extra_config":{"prefill":{"dp_size":2,"tp_size":8},"decode":{"dp_size":2,"tp_size":8}}}'
```

**P and D can start normally, and calling the /v1/completions API on both P and D via curl returns results correctly.**
Next, in new pod, I use the script
https://github.com/vllm-project/vllm-ascend/blob/main/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py

with the following startup command:
```python
TORCH_DEVICE_BACKEND_AUTOLOAD=0 python3 load_balance_proxy_server_example.py \
  --port 8000 \
  --prefiller-hosts ${Prefill0_POD0_IP} 8000 \
  --decoder-hosts ${Decode0_POD0_IP} \
  --decoder-ports 8000
```

In the proxy pod, I run the following command:
```python
curl -X POST http://127.0.0.1:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{ "model": "inference-deepseek-w8a8-pd","prompt": "The future of AI is","max_tokens": 24 }'
```
and it returns a normal response.

The logs from prefill0-pod0 are as follows:
```yaml
(EngineCore_DP0 pid=2757272) INFO 12-10 03:24:54 [mooncake_connector.py:834] Delaying free of 1 blocks for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(APIServer pid=2756696) INFO:     172.16.100.98:46662 - "POST /v1/completions HTTP/1.1" 200 OK
(APIServer pid=2756696) INFO:     172.16.95.192:36616 - "GET /metrics HTTP/1.1" 200 OK
(APIServer pid=2756696) INFO 12-10 03:24:57 [loggers.py:127] Engine 000: Avg prompt throughput: 0.6 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%

```

However, the logs from **decode0-pod0 show the following error:**
172.16.100.99 is the IP address of Prefill0-pod0.
```yaml
E1210 03:24:54.778028 2548307 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:25389, status: 103900
E1210 03:24:54.778062 2548307 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:16381
E1210 03:24:54.778272 2548209 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:20874, status: 103900
E1210 03:24:54.778306 2548209 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:16604
E1210 03:24:54.778358 2548322 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:26671, status: 103900
E1210 03:24:54.778391 2548322 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:15863
(Worker_DP0_TP5 pid=2543213) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP5 pid=2543213) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
E1210 03:24:54.778759 2548207 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:22468, status: 103900
E1210 03:24:54.778759 2548208 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:23888, status: 103900
(Worker_DP0_TP0 pid=2536715) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
E1210 03:24:54.778793 2548208 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:16398
E1210 03:24:54.778795 2548207 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:16732
E1210 03:24:54.778812 2548310 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:27460, status: 103900
E1210 03:24:54.778836 2548310 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:15766
(Worker_DP0_TP6 pid=2544327) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP6 pid=2544327) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(Worker_DP0_TP0 pid=2536715) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(Worker_DP0_TP7 pid=2546570) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP7 pid=2546570) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
E1210 03:24:54.779412 2548311 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:24545, status: 103900
E1210 03:24:54.779441 2548311 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:16935
E1210 03:24:54.779620 2548210 ascend_direct_transport.cpp:820] Failed to connect to target: 172.16.100.99:21174, status: 103900
E1210 03:24:54.779678 2548210 ascend_direct_transport.cpp:581] Failed to connect to segment: 172.16.100.99:15798
(Worker_DP0_TP3 pid=2540966) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP1 pid=2537825) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP3 pid=2540966) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(Worker_DP0_TP2 pid=2538728) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP1 pid=2537825) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(Worker_DP0_TP2 pid=2538728) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(Worker_DP0_TP4 pid=2542110) ERROR 12-10 03:24:54 [mooncake_connector.py:410] Mooncake transfer failed for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0
(Worker_DP0_TP4 pid=2542110) ERROR 12-10 03:24:54 [mooncake_connector.py:329] Failed to transfer KV cache for request cmpl-09be0283-e039-40ce-aefa-da0f36c8cd46-0: Mooncake transfer failed, ret: -1
(APIServer pid=2531394) INFO:     172.16.100.98:57438 - "POST /v1/completions HTTP/1.1" 200 OK
(APIServer pid=2531394) INFO 12-10 03:24:58 [loggers.py:127] Engine 000: Avg prompt throughput: 0.6 tokens/s, Avg generation throughput: 2.4 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=2531394) INFO 12-10 03:25:08 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
```
