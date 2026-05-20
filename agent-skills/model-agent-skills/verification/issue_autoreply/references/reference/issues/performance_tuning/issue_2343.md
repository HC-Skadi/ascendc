# Issue #2343: [Usage]: How to deploy DeepSeek-R1-0528-BF16 on 910B 64G × 32 using DP

## 基本信息

- **编号**: #2343
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2343
- **创建时间**: 2025-08-12T15:17:11Z
- **关闭时间**: 2025-08-12T15:36:20Z
- **更新时间**: 2025-08-12T15:36:20Z
- **提交者**: @miaomiaoguaiOvO
- **评论数**: 0

## 标签

无

## 问题描述

### Your current environment

```text
(910B1 64G × 8 )× 4
npu-driver 24.1.0.3
vllm-ascend v0.10.0rc1
```


### How would you like to use vllm on ascend

##### node0
vllm serve /data0/models/DeepSeek-R1-0528-BF16 \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 8 \
--data-parallel-size-local 2 \
--data-parallel-address 172.16.134.121 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--seed 1024 \
--served-model-name DeepSeek-R1-0528-BF16 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.96 \
--additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

##### node1-3 --data-parallel-start-rank 2 --data-parallel-start-rank 4 --data-parallel-start-rank 6 
vllm serve /data0/models/DeepSeek-R1-0528-BF16 \
--host 0.0.0.0 \
--port 8000 \
--headless \
--data-parallel-size 8 \
--data-parallel-size-local 2 \
--data-parallel-start-rank 2 \
--data-parallel-address 172.16.134.121 \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--seed 1024 \
--served-model-name DeepSeek-R1-0528-BF16 \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--enable-expert-parallel \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.96 \
--additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'



