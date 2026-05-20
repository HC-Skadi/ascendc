# Issue #2494: [Doc]: 910B3 v0.10.0rc1   Qwen3-30B使用PD分离双机部署，进行ais_bench进行测试出现卡停现象，同时P、D服务都没有出现报错提示

## 基本信息

- **编号**: #2494
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2494
- **创建时间**: 2025-08-22T09:36:07Z
- **关闭时间**: 2025-10-15T03:31:35Z
- **更新时间**: 2025-10-15T03:31:35Z
- **提交者**: @0moyi0-2024
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

P节点拉起服务命令:
export VLLM_LOG_LEVEL=ERROR
export VLLM_LOG_TO_STDOUT=0
export VLLM_CONFIGURE_LOGGING=0
export export ASCEND_RT_VISIBLE_DEVICES=6,7
export HCCL_IF_IP=7.150.11.32
export GLOO_SOCKET_IFNAME="enp67s0f5"
export TP_SOCKET_IFNAME="enp67s0f5"
export HCCL_SOCKET_IFNAME="enp67s0f5"
export DISAGGREGATED_PREFILL_RANK_TABLE_PATH=/vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1/ranktable.json
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
vllm serve /disk1/liangliang/qwen3-30b-a3b \
  --host 0.0.0.0 \
  --port 13701 \
  --tensor-parallel-size 2 \
  --no-enable-prefix-caching \
  --seed 1024 \
  --served-model-name qwen-moe \
  --max-model-len 6144  \
  --max-num-batched-tokens 6144  \
  --trust-remote-code \
  --enable-expert-parallel \
  --gpu-memory-utilization 0.9  \
  --kv-transfer-config  \
  '{"kv_connector": "LLMDataDistCMgrConnector",
  "kv_buffer_device": "npu",
  "kv_role": "kv_producer",
  "kv_parallel_size": 2,
  "kv_port": "20001",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.llmdatadist_c_mgr_connector"
  }'  \
  --additional-config \
  '{"torchair_graph_config": {"enabled":false, "enable_multistream_shared_expert":false}, "expert_tensor_parallel_size": 2,  "ascend_scheduler_config":{"enabled":true, "enable_chunked_prefill":false}}'
D节点拉起服务命令：
export VLLM_LOG_LEVEL=ERROR
export VLLM_LOG_TO_STDOUT=0
export VLLM_CONFIGURE_LOGGING=0
export export ASCEND_RT_VISIBLE_DEVICES=3,4
export GLOO_SOCKET_IFNAME="enp67s0f5"
export TP_SOCKET_IFNAME="enp67s0f5"
export HCCL_SOCKET_IFNAME="enp67s0f5"
export HCCL_IF_IP=7.150.14.181
export DISAGGREGATED_PREFILL_RANK_TABLE_PATH=/vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1/ranktable.json
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export VLLM_USE_V1=1
vllm serve /disk1/liangliang/qwen3-30b-a3b  \
  --host 0.0.0.0 \
  --port 13701 \
  --tensor-parallel-size 2 \
  --no-enable-prefix-caching \
  --seed 1024 \
  --served-model-name qwen-moe \
  --max-model-len 6144  \
  --max-num-batched-tokens 6144  \
  --trust-remote-code \
  --enable-expert-parallel \
  --gpu-memory-utilization 0.9  \
  --kv-transfer-config  \
  '{"kv_connector": "LLMDataDistCMgrConnector",
  "kv_buffer_device": "npu",
  "kv_role": "kv_consumer",
  "kv_parallel_size": 2,
  "kv_port": "20001",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.llmdatadist_c_mgr_connector"
  }'  \
  --additional-config \
  '{"torchair_graph_config": {"enabled":false, "enable_multistream_shared_expert":false}, "expert_tensor_parallel_size": 2, "ascend_scheduler_config":{"enabled":true, "enable_chunked_prefill":false}}'
proxy执行命令：
cd /vllm-workspace/vllm-ascend/examples/disaggregated_prefill_v1
python load_balance_proxy_server_example.py --host 7.150.11.32 --port 2026 --prefiller-hosts 7.150.11.32 --prefiller-port 13701 --decoder-hosts 7.150.14.181 --decoder-ports 13701

### Suggest a potential alternative/fix

_No response_

这个初步定位是因为P节点KVcache使用完没有释放导致后续的请求无法响应卡住的情况

