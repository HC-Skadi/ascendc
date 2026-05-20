# Issue #4627: [Misc]: 使用最新镜像vllm-ascend-v0.11.0rc2.tar跑whisper模型报错，vLLM-Ascend 的 ModelRunner 中 get_kv_cache_spec() 根本没实现

## 基本信息

- **编号**: #4627
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4627
- **创建时间**: 2025-12-02T08:19:38Z
- **关闭时间**: 2025-12-03T06:39:30Z
- **更新时间**: 2025-12-03T06:39:30Z
- **提交者**: @helloworlder8
- **评论数**: 1

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

File ".../model_runner_v1.py", line 3347, in get_kv_cache_spec
    raise NotImplementedError
NotImplementedError
