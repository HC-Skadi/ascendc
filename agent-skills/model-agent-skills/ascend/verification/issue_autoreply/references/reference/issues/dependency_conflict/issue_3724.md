# Issue #3724: [Bug]: Mooncake PD Disaggregation Deploy Error: Mooncake transfer failed

## 基本信息

- **编号**: #3724
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3724
- **创建时间**: 2025-10-24T10:18:29Z
- **关闭时间**: 2025-11-13T08:14:30Z
- **更新时间**: 2025-11-13T08:14:30Z
- **提交者**: @paulyu12
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

[env.txt](https://github.com/user-attachments/files/23120983/env.txt)

### 🐛 Describe the bug

# Description

When I deloy a pd-disaggregation instance with Mooncake connector, the engine raise a exception while dealing with a request. The exception output occur on the prefill node, and the detail is in the attached file.

# Launch Command
 
- Prefill Node

```shell
export HCCL_IF_IP=172.39.0.88 # node ip
export GLOO_SOCKET_IFNAME="eth0"  # network card name
export TP_SOCKET_IFNAME="eth0"
export HCCL_SOCKET_IFNAME="eth0"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024
export ASCEND_AGGREGATE_ENABLE=1  # enable aggregated transmission
export ASCEND_TRANSPORT_PRINT=0  # print ascend transport logs
export ACL_OP_INIT_MODE=1  # acl op initialization mode to prevent device id acquisition failure
export ASCEND_A3_ENABLE=1  # enable hccs transmission for A3; set to 0 for A2
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
#export VLLM_LOGGING_LEVEL=DEBUG

vllm serve /model/Qwen3-30B-A3B  \
  --host 0.0.0.0 \
  --port 13700 \
  --no-enable-prefix-caching \
  --seed 1024 \
  --served-model-name qwen3-moe \
  --trust-remote-code \
  --gpu-memory-utilization 0.9  \
  --tensor-parallel-size 2 \
  --seed 1024 \
  --distributed-executor-backend mp \
  --served-model-name qwen3-moe \
  --max-model-len 32768 \
  --max-num-batched-tokens 32768 \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeLayerwiseConnector",
  "kv_role": "kv_producer",
  "kv_port": "30000",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_layerwise_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 2
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 2
             }
      }
  }'
```

- Decode Node

```shell
export HCCL_IF_IP=172.39.1.167 # node ip
export GLOO_SOCKET_IFNAME="eth0"  # network card name
export TP_SOCKET_IFNAME="eth0"
export HCCL_SOCKET_IFNAME="eth0"
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024
export ASCEND_AGGREGATE_ENABLE=1  # enable aggregated transmission
export ASCEND_TRANSPORT_PRINT=0  # print ascend transport logs
export ACL_OP_INIT_MODE=1  # acl op initialization mode to prevent device id acquisition failure
export ASCEND_A3_ENABLE=1  # enable hccs transmission for A3; set to 0 for A2
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
#export VLLM_LOGGING_LEVEL=DEBUG

export ASCEND_RT_VISIBLE_DEVICES=4,5

vllm serve /model/Qwen3-30B-A3B  \
  --host 0.0.0.0 \
  --port 13700 \
  --no-enable-prefix-caching \
  --seed 1024 \
  --served-model-name qwen3-moe \
  --trust-remote-code \
  --gpu-memory-utilization 0.9  \
  --tensor-parallel-size 2 \
  --seed 1024 \
  --distributed-executor-backend mp \
  --served-model-name qwen3-moe \
  --max-model-len 32768 \
  --max-num-batched-tokens 32768 \
  --compilation-config '{"cudagraph_capture_sizes":[16]}' \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeLayerwiseConnector",
  "kv_role": "kv_consumer",
  "kv_port": "30200",
  "engine_id": "1",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_layerwise_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 2
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 2
             }
      }
  }'
```

# Error Output & Env

[env.txt](https://github.com/user-attachments/files/23120990/env.txt)
[error_output.txt](https://github.com/user-attachments/files/23120989/error_output.txt)
