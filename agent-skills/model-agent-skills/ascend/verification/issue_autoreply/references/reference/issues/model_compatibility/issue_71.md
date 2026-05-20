# Issue #71: vLLM Ascend Roadmap Q1 2025

## 基本信息

- **编号**: #71
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/71
- **创建时间**: 2025-02-17T07:42:22Z
- **关闭时间**: 2025-04-09T16:39:53Z
- **更新时间**: 2025-04-09T16:39:54Z
- **提交者**: @Yikun
- **评论数**: 5

## 标签

无

## 问题描述

This is a living document!

Note that: vLLM Ascend 0.7.3 (match vLLM v0.7.3) is main release for 2025 Q1, see more in [link](https://vllm-ascend.readthedocs.io/en/main/developer_guide/versioning_policy.html#branch-state).

Supported models track: https://github.com/vllm-project/vllm-ascend/issues/260

## Hardware Plugin

- [x] https://github.com/vllm-project/vllm/issues/11162

## Basic support
Initial vLLM Ascend support will start to support with [basic hardware compatibility support](https://docs.vllm.ai/en/latest/features/compatibility_matrix.html#feature-x-hardware).
- [x] (P0) Chunked Prefill
- [x] (P1) Automatic Prefix Caching (Improve performance)
- [x] (P1) Speculative decoding
- [x] (P1) Guided Decoding: https://github.com/vllm-project/vllm-ascend/issues/177
- [x] (P1) Multi step scheduler: https://github.com/vllm-project/vllm-ascend/pull/222
- [ ] LoRA
- [ ] Prompt adapter


## Feature support
- [x] (P0) V1 engine support: https://github.com/vllm-project/vllm-ascend/issues/9
- [ ] (P1) EP support https://github.com/vllm-project/vllm/pull/12583
- [x] (P1) Custom op https://github.com/vllm-project/vllm-ascend/issues/156
- [x] (P1) MTP https://github.com/vllm-project/vllm-ascend/pull/236
- [ ] disaggregated prefill https://github.com/vllm-project/vllm/pull/12957
- [ ] Scheduler plugin https://github.com/vllm-project/vllm/pull/12544
- [ ] RLHF Post train support - verl: https://github.com/volcengine/verl/issues/338
- [ ] RLHF Post train suppor - OpenRLHF: https://github.com/OpenRLHF/OpenRLHF/pull/605


## Model support

- [x] (P0) DeepSeek V3 / DeepSeek R1: https://github.com/vllm-project/vllm-ascend/issues/72
- [x] (P0) Llama3
- [x] (P0) Qwen2.5
- [x] (P0) Qwen2-VL: https://github.com/vllm-project/vllm-ascend/issues/246
- [x] (P0) Qwen2.5-VL: https://github.com/vllm-project/vllm-ascend/issues/75
- [x] (P1) BAAI/bge-m3: https://github.com/vllm-project/vllm-ascend/issues/235
- [x] MiniCPM
- [ ] GLM4
- [ ] InternLM
- [ ] llava
- [ ] GLM4v
- [ ] InternVL

## Performance

- add vllm-ascend perf website like vLLM does https://perf.vllm.ai/
- focus on llama3, qwen2.5, qwen2-vl, deepseek v3/R1, improve the performance

## Quality

- [ ] Full UT coverage 
- [ ] Model e2e test
- [ ] Multi card/node e2e test

## Docs
- [x] README
- [x] vllm-ascend website: https://vllm-ascend.readthedocs.org/
- [x] Quick start / Installation / Turtorial
- [x] User guide: supported feature / models
- [x] Developer guide: Contributing / Versioning policy




## CI and Developer Productivity
- [x] vllm-ascend Docker image: https://github.com/vllm-project/vllm-ascend/pull/64
- [x] Ascend CI for main / dev branch: https://github.com/vllm-project/vllm-ascend/pull/3

