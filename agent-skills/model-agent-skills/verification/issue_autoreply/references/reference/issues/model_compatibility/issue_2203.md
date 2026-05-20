# Issue #2203: [Misc]: Torchair model runner refactor workflow

## 基本信息

- **编号**: #2203
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2203
- **创建时间**: 2025-08-05T01:49:45Z
- **关闭时间**: 2025-08-27T02:43:34Z
- **更新时间**: 2025-09-19T04:44:25Z
- **提交者**: @wangxiyuan
- **评论数**: 1

## 标签

无

## 问题描述

There is lot of torchair code in model runner leading the code hard for maintenance.  We'll create new torchair_model_runner to split torchair related logic. There are 5 function contain torchair code. I'll refactor the code in the following step
1. create torchair_model_runner https://github.com/vllm-project/vllm-ascend/pull/2205
1. move torchair code to common function, so that it can be override by torchair_model_runner
    - [x] _get_forward_metadata_across_dp https://github.com/vllm-project/vllm-ascend/pull/2204
    - [x] dummy_run https://github.com/vllm-project/vllm-ascend/pull/2207
    - [x] _process_reqs https://github.com/vllm-project/vllm-ascend/pull/2220
    - [x] initialize_kv_cache https://github.com/vllm-project/vllm-ascend/pull/2208
    - [x] capture_model https://github.com/vllm-project/vllm-ascend/pull/2216
    - [x] init https://github.com/vllm-project/vllm-ascend/pull/2221
    - [x] other common function
        - https://github.com/vllm-project/vllm-ascend/pull/2222
