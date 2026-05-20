# Issue #2498: [Bug][llmdatadist]: Checking query_register_mem_status again never stop

## 基本信息

- **编号**: #2498
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2498
- **创建时间**: 2025-08-22T10:28:16Z
- **关闭时间**: 2025-08-23T10:55:17Z
- **更新时间**: 2025-08-23T10:55:17Z
- **提交者**: @wzmayus
- **评论数**: 3

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
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.108.0.188.u167.fos23.aarch64-aarch64-with-glibc2.35

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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1
[pip3] torch-npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.53.3
[conda] Could not collect
vLLM Version: 0.10.0
vLLM Ascend Version: 0.10.0rc1

ENV Variables:
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
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 99.1        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          59784/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 6277          | python                   | 56485                   |
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

I tried 1P1D (one process per device) on two cards of a single machine, launching two containers with each container assigned to one card using container networking.

ranktable.json
```
{
    "version": "1.2",
    "server_count": "2",
    "prefill_device_list": [
        {
            "server_id": "172.17.0.6",
            "device_id": "0",
            "device_ip": "192.170.100.100",
            "cluster_id": "1"
        }
    ],
    "decode_device_list": [
        {
            "server_id": "172.17.0.7",
            "device_id": "1",
            "device_ip": "192.170.100.101",
            "cluster_id": "2"
        }
    ],
    "status": "completed"
}
```

cat /etc/hccn.conf
```
xsfp_reset_max_times_1=0
xsfp_reset_wait_times_1=7
xsfp_reset_max_times_3=0
xsfp_reset_wait_times_3=7
xsfp_reset_max_times_5=0
xsfp_reset_wait_times_5=7
xsfp_reset_max_times_6=0
xsfp_reset_wait_times_6=7
xsfp_reset_max_times_7=0
xsfp_reset_wait_times_7=7
xsfp_reset_max_times_4=0
xsfp_reset_wait_times_4=7
xsfp_reset_max_times_0=0
xsfp_reset_wait_times_0=7
xsfp_reset_max_times_2=0
xsfp_reset_wait_times_2=7
address_0=192.170.100.100
netmask_0=255.255.255.0
address_1=192.170.100.101
netmask_1=255.255.255.0
address_2=192.170.100.102
netmask_2=255.255.255.0
address_3=192.170.100.103
netmask_3=255.255.255.0
address_4=192.170.100.104
netmask_4=255.255.255.0
address_5=192.170.100.105
netmask_5=255.255.255.0
address_6=192.170.100.106
netmask_6=255.255.255.0
address_7=192.170.100.107
netmask_7=255.255.255.0
```

docker cli
```
docker run -d --shm-size=128g -u root --name ascend-1 --ulimit memlock=-1:-1 --ulimit nofile=65535:65535 --device=/dev/davinci_manager --device=/dev/hisi_hdc --device=/dev/devmm_svm --device=/dev/davinci0 -v /usr/local/dcmi:/usr/local/dcmi -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info -v /etc/ascend_install.info:/etc/ascend_install.info -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro -v /usr/local/sbin:/usr/local/sbin:ro -v /etc/hccn.conf:/etc/hccn.conf npu-aarch64:0.10.0 bash -c "tail -f /dev/null"

docker run -d --shm-size=128g -u root --name ascend-2 --ulimit memlock=-1:-1 --ulimit nofile=65535:65535 --device=/dev/davinci_manager --device=/dev/hisi_hdc --device=/dev/devmm_svm --device=/dev/davinci1 -v /usr/local/dcmi:/usr/local/dcmi -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info -v /etc/ascend_install.info:/etc/ascend_install.info -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro -v /usr/local/sbin:/usr/local/sbin:ro -v /etc/hccn.conf:/etc/hccn.conf npu-aarch64:0.10.0 bash -c "tail -f /dev/null"
```

serve cli
```
export GLOO_SOCKET_IFNAME="eth0"  
export TP_SOCKET_IFNAME="eth0"
export HCCL_SOCKET_IFNAME="eth0"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export LCCL_DETERMINISTIC=1
export HCCL_DETERMINISTIC=true
export CLOSE_MATMUL_K_SHIFT=1
export DISAGGREGATED_PREFILL_RANK_TABLE_PATH="./ranktable.json"

VLLM_LLMDD_RPC_PORT=5579 VLLM_LOGGING_LEVEL=DEBUG LMCACHE_LOG_LEVEL=DEBUG PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 vllm serve ./Qwen3-1.7B  --host 0.0.0.0 --port 8111 --served-model-name qwen3 --seed 1024 --enforce-eager --disable-log-requests --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --kv-transfer-config '{"kv_connector":"LLMDataDistCMgrConnector","kv_role":"kv_producer","kv_buffer_device":"npu","kv_parallel_size":"1","kv_port":"20001","engine_id":"0","kv_connector_module_path":"vllm_ascend.distributed.llmdatadist_c_mgr_connector"}'
```

error log:
```
DEBUG 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:207] LLMDataDistCMgrConnector get_num_new_matched_tokens: num_computed_tokens=0, kv_transfer_params={'do_remote_prefill': True, 'do_remote_decode': False, 'remote_block_ids': [5, 6, 7, 8], 'remote_engine_id': '0', 'remote_host': '172.17.0.6', 'remote_port': 5579, 'remote_tp_size': '1'}
DEBUG 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:224] LLMDataDistCMgrConnector update states num_externel_tokens: 418 kv_transfer_params: {'do_remote_prefill': True, 'do_remote_decode': False, 'remote_block_ids': [5, 6, 7, 8], 'remote_engine_id': '0', 'remote_host': '172.17.0.6', 'remote_port': 5579, 'remote_tp_size': '1'}
DEBUG 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:589] Start to transmit cmpl-6aaabd51-c40e-4c28-a621-693873731482-0
DEBUG 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:755] Querying metadata from url: tcp://172.17.0.6:5579
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:760] Try request remote metadata from socket......
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:766] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id=None, server_id='172.17.0.6', device_id='0', device_ip='192.170.100.100', super_device_id=None, cluster_id=1)
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:708] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.170.100.100_192.170.100.101
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:711] rank table 
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:711] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '0', 'device_ip': '192.170.100.100', 'rank_id': '0'}], 'server_id': '172.17.0.6'}, {'device': [{'device_id': '1', 'device_ip': '192.170.100.101', 'rank_id': '1'}], 'server_id': '172.17.0.7'}]}
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:712] comm name: pd_comm_192.170.100.100_192.170.100.101
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:44 [llmdatadist_c_mgr_connector.py:713] cluster rank info: {1: 0, 2: 1}
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
DEBUG 08-22 18:00:44 [scheduler.py:345] cmpl-6aaabd51-c40e-4c28-a621-693873731482-0 is still in WAITING_FOR_REMOTE_KVS state.
INFO 08-22 18:00:50 [llmdatadist_c_mgr_connector.py:728] Checking query_register_mem_status again
INFO 08-22 18:00:51 [llmdatadist_c_mgr_connector.py:728] Checking query_register_mem_status again
INFO 08-22 18:00:52 [llmdatadist_c_mgr_connector.py:728] Checking query_register_mem_status again
INFO 08-22 18:00:53 [llmdatadist_c_mgr_connector.py:728] Checking query_register_mem_status again
INFO 08-22 18:00:54 [llmdatadist_c_mgr_connector.py:728] Checking query_register_mem_status again
```


