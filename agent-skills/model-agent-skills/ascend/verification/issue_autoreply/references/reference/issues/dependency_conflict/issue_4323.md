# Issue #4323: [Bug]: vllm-ascend 0.11.x 版本qwen3-32b-eagle3乱码以及无法启动

## 基本信息

- **编号**: #4323
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4323
- **创建时间**: 2025-11-21T03:21:01Z
- **关闭时间**: 2025-12-18T02:46:27Z
- **更新时间**: 2025-12-18T02:46:27Z
- **提交者**: @sunchendd
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
 docker start vllm-ascend 0.11.0rc0镜像
启动服务
export ASCEND_RT_VISIBLE_DEVICES=4,5,6,7
export VLLM_USE_MODELSCOPE="True"
vllm serve /nfs/1_AscendPackage/05_weights_public/Qwen3-32B \
  --served-model-name Qwen3-32B \
  -tp 4 \
  --host "0.0.0.0" \
  --port "8000" \
  --trust-remote-code \
  --speculative-config '{"method":"eagle3","model":"/home/scd/qwen3_32b_eagle3/","num_speculative_tokens":4,"draft_tensor_parallel_size":1}' \
  --max-num-batched-tokens 4096 \
  --max-model-len 4096

调用返回乱码
curl -s http://127.0.0.1:8000/v1/completions     -H "Content-Type: application/json"     -d '{
        "model": "Qwen3-32B",
        "prompt": "Beijing is a",
        "max_tokens": 20,
        "temperature": 0.7
    }' | python3 -m json.tool
{
    "id": "cmpl-d5d8517207d5430189ded9a5367d6390",
    "object": "text_completion",
    "created": 1763694512,
    "model": "Qwen3-32B",
    "choices": [
        {
            "index": 0,
            "text": "tctctctctcctctcctc1llllllllll\");\nll",
            "logprobs": null,
            "finish_reason": "length",
            "stop_reason": null,
            "token_ids": null,
            "prompt_logprobs": null,
            "prompt_token_ids": null
        }
    ],
    "service_tier": null,
    "system_fingerprint": null,
    "usage": {
        "prompt_tokens": 4,
        "total_tokens": 24,
        "completion_tokens": 20,
        "prompt_tokens_details": null
    },
    "kv_transfer_params": null
}

 docker start vllm-ascend 0.11.0rc1镜像
启动服务如上
测试
 curl -s http://127.0.0.1:8000/v1/completions     -H "Content-Type: application/json"     -d '{
        "model": "Qwen3-32B",
        "prompt": "Beijing is a",
        "max_tokens": 20,
        "temperature": 0.7
    }' | python3 -m json.tool
{
    "error": {
        "message": "EngineCore encountered an issue. See stack trace (above) for the root cause.",
        "type": "Internal Server Error",
        "param": null,
        "code": 500
    }
}

服务报错日志

[logerror.txt](https://github.com/user-attachments/files/23667294/logerror.txt)

</details>


### 🐛 Describe the bug

草稿模型为[AngelSlim/Qwen3-32B_eagle3](https://modelscope.cn/models/AngelSlim/Qwen3-32B_eagle3
