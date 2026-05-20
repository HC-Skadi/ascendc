# Issue #2900: [Bug]: Qwen 235B Multi-Node + 1P1D + 2DP + 16TP + EP failed

## 基本信息

- **编号**: #2900
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2900
- **创建时间**: 2025-09-12T12:06:51Z
- **关闭时间**: 2025-12-23T12:44:12Z
- **更新时间**: 2025-12-23T12:44:12Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/issues/2859#issuecomment-3283568276

### 🐛 Describe the bug

# ❌ Qwen 235B Multi-Node + 1P1D + 2DP + 16TP + EP 

## command

```bash
bash gen_ranktable.sh --ips 172.22.0.188 172.22.0.212  \
  --npus-per-node 16 --network-card-name enp23s0f3 --prefill-device-cnt 16 --decode-device-cnt 16
```
### node0:
```bash
#!/bin/sh

# this obtained through ifconfig
# nic_name is the network interface name corresponding to local_ip
nic_name="enp23s0f3"
local_ip="172.22.0.188"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1280
export DISAGGREGATED_PREFILL_RANK_TABLE_PATH=/vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1/ranktable.json
export PYTORCH_NPU_ALLOC_CONF="max_split_size_mb:256"

vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-235B-A22B \
--host 0.0.0.0 \
--port 8004 \
--data-parallel-size 2 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--seed 1024 \
--enforce-eager \
--no-enable-prefix-caching \
--enable-expert-parallel \
--max-num-seqs 8 \
--max-model-len 8192 \
--trust-remote-code \
--served-model-name qwen_235 \
--gpu-memory-utilization 0.8 \
--kv-transfer-config  \
  '{"kv_connector": "LLMDataDistCMgrConnector",
    "kv_buffer_device": "npu",
    "kv_role": "kv_producer",
    "kv_parallel_size": 1,
    "kv_port": "20001",
    "engine_id": "0",
    "kv_connector_module_path": "vllm_ascend.distributed.llmdatadist_c_mgr_connector"
  }'  &

```
### node1:
```bash
#!/bin/sh

nic_name="enp23s0f3"
local_ip="172.22.0.212"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1280
export PYTORCH_NPU_MAX_SPLIT_SIZE_MB=128
export DISAGGREGATED_PREFILL_RANK_TABLE_PATH=/vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1/ranktable.json
export ASCEND_LAUNCH_BLOCKING=1
export PYTORCH_NPU_ALLOC_CONF="max_split_size_mb:256"


vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-235B-A22B \
--host 0.0.0.0 \
--port 8004 \
--data-parallel-size 2 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 8 \
--seed 1024 \
--enforce-eager \
--served-model-name qwen_235 \
--max-num-seqs 8 \
--max-model-len 8192 \
--enable-expert-parallel \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9 \
--kv-transfer-config  \
  '{"kv_connector": "LLMDataDistCMgrConnector",
  "kv_buffer_device": "npu",
  "kv_role": "kv_consumer",
  "kv_parallel_size": 1,
  "kv_port": "20001",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.llmdatadist_c_mgr_connector"
  }'  &

```
### proxy:
```python
python load_balance_proxy_server_example.py --host 0.0.0.0  --port 1025 --prefiller-hosts 172.22.0.188 --prefiller-port 8004 --decoder-hosts 172.22.0.212 --decoder-ports 8004\

```
## error log：
### node0:
```
(EngineCore_DP0 pid=851637) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:276] Delaying free of 1 blocks for request cmpl-0ed7171a-19e2-4f99-85b2-3e9fea46deb7-0
(APIServer pid=851368) INFO:     172.22.0.188:46216 - "POST /v1/completions HTTP/1.1" 200 OK
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 20
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.196_192.45.3.196
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '3', 'device_ip': '192.23.3.196', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '3', 'device_ip': '192.45.3.196', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.196_192.45.3.196
(Worker_DP0_TP3_EP3 pid=852060) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {4: 0, 20: 1}
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 19
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 23
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.197_192.45.2.197
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '2', 'device_ip': '192.23.2.197', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '2', 'device_ip': '192.45.2.197', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.193_192.45.2.193
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.197_192.45.2.197
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '6', 'device_ip': '192.23.2.193', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '6', 'device_ip': '192.45.2.193', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP2_EP2 pid=852052) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {3: 0, 19: 1}
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.193_192.45.2.193
(Worker_DP0_TP6_EP6 pid=852063) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {7: 0, 23: 1}
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 21
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 22
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 24
(Worker_DP0_TP2_EP2 pid=852052) Exception in thread metadata_agent_listener:
(Worker_DP0_TP3_EP3 pid=852060) Exception in thread metadata_agent_listener:
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.195_192.45.2.195
(Worker_DP0_TP2_EP2 pid=852052) Traceback (most recent call last):
(Worker_DP0_TP2_EP2 pid=852052)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.194_192.45.3.194
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '4', 'device_ip': '192.23.2.195', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '4', 'device_ip': '192.45.2.195', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP3_EP3 pid=852060) Traceback (most recent call last):
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=852060)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '5', 'device_ip': '192.23.3.194', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '5', 'device_ip': '192.45.3.194', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.192_192.45.3.192
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.195_192.45.2.195
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.194_192.45.3.194
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 17
(Worker_DP0_TP4_EP4 pid=852061) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {5: 0, 21: 1}
(Worker_DP0_TP5_EP5 pid=852062) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {6: 0, 22: 1}
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '7', 'device_ip': '192.23.3.192', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '7', 'device_ip': '192.45.3.192', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.192_192.45.3.192
(Worker_DP0_TP7_EP7 pid=852064) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {8: 0, 24: 1}
(Worker_DP0_TP2_EP2 pid=852052)     self.run()
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:367] LLMDataDistCMgrConnectorWorker: Receive message from cluster 18
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.199_192.45.2.199
(Worker_DP0_TP6_EP6 pid=852063) Exception in thread metadata_agent_listener:
(Worker_DP0_TP2_EP2 pid=852052)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP6_EP6 pid=852063) Traceback (most recent call last):
(Worker_DP0_TP6_EP6 pid=852063)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=852060)     self.run()
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '0', 'device_ip': '192.23.2.199', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '0', 'device_ip': '192.45.2.199', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP3_EP3 pid=852060)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.199_192.45.2.199
(Worker_DP0_TP0_EP0 pid=852049) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {1: 0, 17: 1}
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.198_192.45.3.198
(Worker_DP0_TP2_EP2 pid=852052)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP2_EP2 pid=852052)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP3_EP3 pid=852060)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=852060)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP2_EP2 pid=852052)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP6_EP6 pid=852063)     self.run()
(Worker_DP0_TP2_EP2 pid=852052)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '1', 'device_ip': '192.23.3.198', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '1', 'device_ip': '192.45.3.198', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.198_192.45.3.198
(Worker_DP0_TP6_EP6 pid=852063)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP3_EP3 pid=852060)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP1_EP1 pid=852051) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {2: 0, 18: 1}
(Worker_DP0_TP3_EP3 pid=852060)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP2_EP2 pid=852052)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP2_EP2 pid=852052)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=852063)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP2_EP2 pid=852052)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP6_EP6 pid=852063)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP3_EP3 pid=852060)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP3_EP3 pid=852060)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP3_EP3 pid=852060)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP2_EP2 pid=852052)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP6_EP6 pid=852063)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP2_EP2 pid=852052)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP2_EP2 pid=852052)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP2_EP2 pid=852052) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {3: 0, 19: 1}.
(Worker_DP0_TP3_EP3 pid=852060)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP3_EP3 pid=852060)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP6_EP6 pid=852063)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP3_EP3 pid=852060)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP3_EP3 pid=852060) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {4: 0, 20: 1}.
(Worker_DP0_TP6_EP6 pid=852063)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP6_EP6 pid=852063)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=852063)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP5_EP5 pid=852062) Exception in thread metadata_agent_listener:
(Worker_DP0_TP5_EP5 pid=852062) Traceback (most recent call last):
(Worker_DP0_TP5_EP5 pid=852062)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP4_EP4 pid=852061) Exception in thread metadata_agent_listener:
(Worker_DP0_TP4_EP4 pid=852061) Traceback (most recent call last):
(Worker_DP0_TP4_EP4 pid=852061)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP6_EP6 pid=852063)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP6_EP6 pid=852063)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP6_EP6 pid=852063)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP6_EP6 pid=852063) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {7: 0, 23: 1}.
(Worker_DP0_TP7_EP7 pid=852064) Exception in thread metadata_agent_listener:
(Worker_DP0_TP7_EP7 pid=852064) Traceback (most recent call last):
(Worker_DP0_TP4_EP4 pid=852061)     self.run()
(Worker_DP0_TP5_EP5 pid=852062)     self.run()
(Worker_DP0_TP7_EP7 pid=852064)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP5_EP5 pid=852062)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP4_EP4 pid=852061)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP4_EP4 pid=852061)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP4_EP4 pid=852061)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP5_EP5 pid=852062)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP0_EP0 pid=852049) Exception in thread metadata_agent_listener:
(Worker_DP0_TP7_EP7 pid=852064)     self.run()
(Worker_DP0_TP4_EP4 pid=852061)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP5_EP5 pid=852062)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP0_EP0 pid=852049) Traceback (most recent call last):
(Worker_DP0_TP4_EP4 pid=852061)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP0_EP0 pid=852049)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP7_EP7 pid=852064)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP5_EP5 pid=852062)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP4_EP4 pid=852061)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP4_EP4 pid=852061)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP4_EP4 pid=852061)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP7_EP7 pid=852064)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP5_EP5 pid=852062)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP7_EP7 pid=852064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP1_EP1 pid=852051) Exception in thread metadata_agent_listener:
(Worker_DP0_TP1_EP1 pid=852051) Traceback (most recent call last):
(Worker_DP0_TP1_EP1 pid=852051)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
(Worker_DP0_TP7_EP7 pid=852064)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP4_EP4 pid=852061)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP7_EP7 pid=852064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP4_EP4 pid=852061)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP0_EP0 pid=852049)     self.run()
(Worker_DP0_TP5_EP5 pid=852062)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP4_EP4 pid=852061)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP0_EP0 pid=852049)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP4_EP4 pid=852061) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {5: 0, 21: 1}.
(Worker_DP0_TP5_EP5 pid=852062)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP7_EP7 pid=852064)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP5_EP5 pid=852062)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP7_EP7 pid=852064)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP7_EP7 pid=852064)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP7_EP7 pid=852064)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP5_EP5 pid=852062)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP7_EP7 pid=852064)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP5_EP5 pid=852062)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP0_EP0 pid=852049)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP0_EP0 pid=852049)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP1_EP1 pid=852051)     self.run()
(Worker_DP0_TP7_EP7 pid=852064)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP7_EP7 pid=852064) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {8: 0, 24: 1}.
(Worker_DP0_TP1_EP1 pid=852051)   File "/usr/local/python3.11.13/lib/python3.11/threading.py", line 982, in run
(Worker_DP0_TP5_EP5 pid=852062)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP5_EP5 pid=852062) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {6: 0, 22: 1}.
(Worker_DP0_TP0_EP0 pid=852049)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP1_EP1 pid=852051)     self._target(*self._args, **self._kwargs)
(Worker_DP0_TP1_EP1 pid=852051)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 371, in listen_for_agent_metadata_req
(Worker_DP0_TP0_EP0 pid=852049)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP1_EP1 pid=852051)     self.add_remote_agent(decode_msg)
(Worker_DP0_TP1_EP1 pid=852051)   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/llmdatadist_c_mgr_connector.py", line 691, in add_remote_agent
(Worker_DP0_TP0_EP0 pid=852049)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP0_EP0 pid=852049)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP1_EP1 pid=852051)     comm_id = self.llm_datadist.link(comm_name, cluster_rank_info,
(Worker_DP0_TP0_EP0 pid=852049)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP1_EP1 pid=852051)               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP1_EP1 pid=852051)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/v2/llm_datadist.py", line 334, in link
(Worker_DP0_TP1_EP1 pid=852051)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP1_EP1 pid=852051)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP0_EP0 pid=852049)     handle_llm_status(ret, '[link]', cluster_rank_info)
(Worker_DP0_TP0_EP0 pid=852049)   File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/llm_datadist/status.py", line 125, in handle_llm_status
(Worker_DP0_TP1_EP1 pid=852051)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP1_EP1 pid=852051) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {2: 0, 18: 1}.
(Worker_DP0_TP0_EP0 pid=852049)     raise LLMException(f"{func_name} failed, error code is {code_2_status(status)}, {other_info}.",
(Worker_DP0_TP0_EP0 pid=852049) llm_datadist.status.LLMException: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {1: 0, 17: 1}.
(APIServer pid=851368) INFO 09-12 03:40:07 [loggers.py:123] Engine 000: Avg prompt throughput: 0.4 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%
(APIServer pid=851368) INFO 09-12 03:40:17 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%
(APIServer pid=851368) Task was destroyed but it is pending!
(APIServer pid=851368) task: <Task pending name='Task-17' coro=<AsyncMicrobatchTokenizer._batch_encode_loop() done, defined at /vllm-workspace/vllm/vllm/utils/__init__.py:580> wait_for=<Future cancelled>>

```
#### node1:
```
(APIServer pid=139846) INFO:     Started server process [139846]
(APIServer pid=139846) INFO:     Waiting for application startup.
(APIServer pid=139846) INFO:     Application startup complete.
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='3', device_ip='192.23.3.196', super_device_id='98369551', cluster_id=4)
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.196_192.45.3.196
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:737] Try request remote metadata from socket......
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '3', 'device_ip': '192.23.3.196', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '3', 'device_ip': '192.45.3.196', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.196_192.45.3.196
(Worker_DP0_TP3_EP3 pid=140538) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {4: 0, 20: 1}
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='2', device_ip='192.23.2.197', super_device_id='98369551', cluster_id=3)
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.197_192.45.2.197
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='6', device_ip='192.23.2.193', super_device_id='98369551', cluster_id=7)
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '2', 'device_ip': '192.23.2.197', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '2', 'device_ip': '192.45.2.197', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.197_192.45.2.197
(Worker_DP0_TP2_EP2 pid=140529) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {3: 0, 19: 1}
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.193_192.45.2.193
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '6', 'device_ip': '192.23.2.193', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '6', 'device_ip': '192.45.2.193', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.193_192.45.2.193
(Worker_DP0_TP6_EP6 pid=140541) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {7: 0, 23: 1}
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='4', device_ip='192.23.2.195', super_device_id='98369551', cluster_id=5)
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='5', device_ip='192.23.3.194', super_device_id='98369551', cluster_id=6)
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.195_192.45.2.195
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='7', device_ip='192.23.3.192', super_device_id='98369551', cluster_id=8)
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '4', 'device_ip': '192.23.2.195', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '4', 'device_ip': '192.45.2.195', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.194_192.45.3.194
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.195_192.45.2.195
(Worker_DP0_TP4_EP4 pid=140539) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {5: 0, 21: 1}
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.192_192.45.3.192
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '5', 'device_ip': '192.23.3.194', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '5', 'device_ip': '192.45.3.194', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.194_192.45.3.194
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '7', 'device_ip': '192.23.3.192', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '7', 'device_ip': '192.45.3.192', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP5_EP5 pid=140540) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {6: 0, 22: 1}
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.192_192.45.3.192
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='0', device_ip='192.23.2.199', super_device_id='98369551', cluster_id=1)
(Worker_DP0_TP7_EP7 pid=140542) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {8: 0, 24: 1}
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.2.199_192.45.2.199
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '0', 'device_ip': '192.23.2.199', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '0', 'device_ip': '192.45.2.199', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.2.199_192.45.2.199
(Worker_DP0_TP0_EP0 pid=140527) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {1: 0, 17: 1}
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:743] recving metadata: LLMDataDistCMgrAgentMetadata(super_pod_id='11', server_id='172.22.0.188', device_id='1', device_ip='192.23.3.198', super_device_id='98369551', cluster_id=2)
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:685] LLMDataDistCMgrConnectorWorker: try link with remote, comm id: pd_comm_192.23.3.198_192.45.3.198
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] rank table
(Worker_DP0_TP3_EP3 pid=140538) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {4: 0, 20: 1}.
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:688] {'version': '1.2', 'server_count': '2', 'status': 'completed', 'server_list': [{'device': [{'device_id': '1', 'device_ip': '192.23.3.198', 'super_device_id': '98369551', 'rank_id': '0'}], 'server_id': '172.22.0.188'}, {'device': [{'device_id': '1', 'device_ip': '192.45.3.198', 'super_device_id': '190644239', 'rank_id': '1'}], 'server_id': '172.22.0.212'}], 'super_pod_list': [{'super_pod_id': '11', 'server_list': [{'server_id': '172.22.0.188'}, {'server_id': '172.22.0.212'}]}]}
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:689] comm name: pd_comm_192.23.3.198_192.45.3.198
(Worker_DP0_TP1_EP1 pid=140528) INFO 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:690] cluster rank info: {2: 0, 18: 1}
(Worker_DP0_TP2_EP2 pid=140529) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {3: 0, 19: 1}.
(Worker_DP0_TP4_EP4 pid=140539) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {5: 0, 21: 1}.
(Worker_DP0_TP6_EP6 pid=140541) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {7: 0, 23: 1}.
(Worker_DP0_TP7_EP7 pid=140542) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {8: 0, 24: 1}.
(Worker_DP0_TP5_EP5 pid=140540) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {6: 0, 22: 1}.
(Worker_DP0_TP0_EP0 pid=140527) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {1: 0, 17: 1}.
(Worker_DP0_TP1_EP1 pid=140528) ERROR 09-12 03:40:02 [llmdatadist_c_mgr_connector.py:581] KV transfer task failed: [link] failed, error code is LLMStatusCode.LLM_LINK_FAILED, {2: 0, 18: 1}.

```
