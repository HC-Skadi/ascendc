# Issue #674: [Bug]: Missing attn_metadata in profile_run causes underestimated activation memory peak measurement, leading to KVCache overallocation and OOM risks

## 基本信息

- **编号**: #674
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/674
- **创建时间**: 2025-04-27T07:46:14Z
- **关闭时间**: 2025-04-29T09:06:21Z
- **更新时间**: 2025-04-29T09:06:21Z
- **提交者**: @ApsarasX
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

vllm: v0.8.4(**force enable chunked prefill**)
vllm-ascend: 3879d9cad95c14e3cce8fc053540e369a39cd341

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/blob/fa4a5d980e8845a88b9162cf169f0a5ab230f8a5/vllm_ascend/attention/mla_v1.py#L490-L492

https://github.com/vllm-project/vllm-ascend/blob/fa4a5d980e8845a88b9162cf169f0a5ab230f8a5/vllm_ascend/models/deepseek_v2.py#L143-L147

During profile_run, we execute the forward function of the prefill phase to estimate the peak activation memory consumption. However, the measured peak activation memory is significantly lower than the actual value due to the absence of attn_metadata during profiling.

This will lead to KVCache overallocation and OOM risks.

vllm server launch command
```
export VLLM_USE_V1=1
python -m vllm.entrypoints.openai.api_server --model=<...>/DeepSeek-R1-W8A8-VLLM \
    --trust-remote-code \
    --distributed-executor-backend=mp \
    --port 8006 \
    -tp=16 \
    --max-model-len 32768 \
    --block-size 128 \
    --gpu-memory-utilization 0.97 &> run.log &
disown
```
client launch command:
```sh
python benchmark_serving.py --backend vllm --dataset-name random \
        --random-input-len 31500 \
        --random-output-len 2 \
        --num-prompts 1 \
        --model <...>/DeepSeek-R1-W8A8-VLLM \
        --port 8006 \
        --metric-percentiles "50,90,99"
```
