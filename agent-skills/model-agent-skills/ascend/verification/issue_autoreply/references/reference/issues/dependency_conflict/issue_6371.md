# Issue #6371: [Bug]: Performance regression issue of version 0.13.0rc1 compared with version 0.11.0

## 基本信息

- **编号**: #6371
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6371
- **创建时间**: 2026-01-28T17:29:06Z
- **关闭时间**: 2026-01-28T17:46:51Z
- **更新时间**: 2026-01-28T17:46:51Z
- **提交者**: @qiudepei
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

Image: 0.11.0 and 0.13.RC1
Hardware: A2 and A3
Model: Qwen2.5-VL-72B

### 🐛 Describe the bug

1、Environment variables and configurations are as follows:
export HCCL_CONNECT_TIMEOUT=7200
#export GLOBAL_ASCEND_RT_VISIBLE_DEVICES=12,13,14,15
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=0
export CPU_AFFINITY_CONF=2
export VLLM_USE_V1=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0
export VLLM_DP_POLLING_LOAD_BALANCE_ENABLE=1
vllm serve /home/weight/Qwen2.5-VL-72B-Instruct/ \
    --served-model-name qwen2.5-vl-72b \
    --trust-remote-code \
    -tp 4 \
    --port 7777 \
    --compilation-config "{\"cudagraph_mode\": \"FULL_DECODE_ONLY\", \"cudagraph_capture_sizes\": [1,2,4,8,16]}" \
    --gpu-memory-utilization 0.85 \
    --max-num-seqs 128 \
    --max-model-len 65536 \
    --max-num-batched-tokens 65536 \
    --allowed-local-media-path /home/l60056053 \
    --mm-processor-cache-type "shm" \
    --mm-processor-cache-gb 0 \
    --additional-config '{
        "enable_cpu_binding": true,
        "ascend_scheduler_config": {
            "enabled": false,
            "enable_chunked_prefill": true,
            "chunked_prefill_enabled": true
        }
    }'

2、The key difference is that version 0.11.0 does not support FULL_DECODE_ONLY; instead, it uses PIECEWISE, which has a theoretically poorer performance.

3、In the same test case (A3, plain text input), TPOT yielded 56ms (version 0.13.0RC1) and 50ms (version 0.11.0) respectively, showing a significant performance degradation.
