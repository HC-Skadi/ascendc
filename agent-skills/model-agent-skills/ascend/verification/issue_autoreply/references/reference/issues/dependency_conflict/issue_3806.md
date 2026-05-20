# Issue #3806: [Bug]: Qwen3-VL-30B-A3B-Instruct输出全是感叹号!!!!!

## 基本信息

- **编号**: #3806
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3806
- **创建时间**: 2025-10-28T00:57:15Z
- **关闭时间**: 2025-10-28T02:07:08Z
- **更新时间**: 2025-12-25T09:21:47Z
- **提交者**: @csw7777
- **评论数**: 2

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

A2服务器
quay.io/ascend/vllm-ascend:v0.11.0rc0镜像
驱动固件版本为最新
启动命令：
```
export LD_PRELOAD="/home/data/libjemalloc.so:$LD_PRELOAD"
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export OMP_NUM_THREADS=10
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
export HCCL_OP_EXPANSION_MODE="AIV"
unset http_proxy
unset https_proxy
taskset -c 0-31 vllm serve /opt/data2/Qwen/Qwen3-VL-30B-A3B-Instruct \
--max-num-seqs=128 \
--max_model_len=150000 \
--tensor-parallel-size=4 \
--block-size=128 \
--host=0.0.0.0 \
--port=60201 \
--gpu-memory-utilization=0.85 \
--trust-remote-code \
--served-model-name "qwen3" \
--no-enable-prefix-caching \
--allowed-local-media-path "/" \
--compilation-config '{"cudagraph_capture_sizes": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]}'
```

### 🐛 Describe the bug

```
curl -X POST "http://0.0.0.0:60201/v1/chat/completions" \
> -H "Content-Type: application/json" \
> -d '{
>   "model": "qwen3",
>   "messages": [
>     {
>       "role": "system",
>       "content": "You are a helpful assistant."
>     },
>     {
>       "role": "user",
>       "content": [
>         {
>           "type": "text",
>           "text": "请用表格总结一下视频中的商品特点"
>         },
>         {
>           "type": "video_url",
>           "video_url": {
>             "url": "https://duguang-labelling.oss-cn-shanghai.aliyuncs.com/qiansun/video_ocr/videos/50221078283.mp4"
>           }
>         }
>       ]
>     }
>   ],
>   "max_tokens": 300
> }'
{"id":"chatcmpl-db3143b8c28b4d4e93b72d115a0f8e6e","object":"chat.completion","created":1761612582,"model":"qwen3","choices":[{"index":0,"message":{"role":"assistant","content":"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":11686,"total_tokens":11986,"completion_tokens":300,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
```
