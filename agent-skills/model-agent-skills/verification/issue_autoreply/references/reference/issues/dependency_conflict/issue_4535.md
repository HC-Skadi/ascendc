# Issue #4535: [Bug]: vllm-ascendv0.11.0rc1, Qwen3-VL-235B模型开启full_decode_only后，发送请求hang住

## 基本信息

- **编号**: #4535
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4535
- **创建时间**: 2025-11-28T08:04:56Z
- **关闭时间**: 2025-12-08T06:54:00Z
- **更新时间**: 2025-12-08T06:54:00Z
- **提交者**: @yifeililn
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

Qwen3-VL-235B，在开启图模式FULL_DECODE_ONLY后，再发送请求会出现hang住，然后collective_rpc超时。

版本：vllm-ascend v0.11.0rc1

复现的配置文件如下：

```text
export HCCL_CONNECT_TIMEOUT=7200
export GLOBAL_ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=0
export CPU_AFFINITY_CONF=2
export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:$LD_PRELOAD
export VLLM_USE_V1=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=1
export VLLM_VERSION=0.11.0

rm /dev/shm/VLLM_OBJECT_STORAGE_SHM_BUFFER -rf

vllm serve \
        --model="/mnt/huawei/weight/Qwen3-VL-235B-A22B-Instruct/" \
        --trust-remote-code \
        -tp 16 \
        --port 8003 \
        --gpu-memory-utilization 0.8 \
        --enable-prefix-caching \
        --no-enable-expert-parallel \
        --max-num-seqs 512 \
        --max-model-len 40960 \
        --max-num-batched-tokens 8192 \
        --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY", "cudagraph_capture_sizes": [512, 256, 192, 128, 64, 32, 16, 8, 1]}' \
        --served-model-name "qwen3vl" \
        --mm-processor-cache-type "shm" \
        --additional-config '{
            "enable_cpu_binding": true,
            "ascend_scheduler_config": {
                "enabled": true,
                "enable_chunked_prefill": true,
                "chunked_prefill_enabled": true
            }
        }' \
        --allowed-local-media-path /
```


### 🐛 Describe the bug

Qwen3-VL-235B，在开启图模式FULL_DECODE_ONLY后，再发送请求会出现hang住，然后collective_rpc超时。

版本：vllm-ascend v0.11.0rc1
