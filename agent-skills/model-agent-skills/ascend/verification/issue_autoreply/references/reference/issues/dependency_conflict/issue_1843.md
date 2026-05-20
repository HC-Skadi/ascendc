# Issue #1843: [Bug]: Randomized replying of `actor.generate.remote` when RLHF

## 基本信息

- **编号**: #1843
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1843
- **创建时间**: 2025-07-17T03:41:06Z
- **关闭时间**: 2025-07-17T06:12:59Z
- **更新时间**: 2025-07-17T06:13:43Z
- **提交者**: @janelu9
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

vllm-0.9.2.rc1

### 🐛 Describe the bug
Got a randomized replying if request a response by ray.
```
ray.get(vllm_actor.generate.remote(prompts=[TokensPrompt(prompt_token_ids=r) for r in prompt_ids],sampling_params=sampling_params))
```
