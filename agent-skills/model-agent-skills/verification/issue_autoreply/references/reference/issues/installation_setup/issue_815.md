# Issue #815: [Performance]: vllm-ascend + mindie-turbo Performance Optimization

## 基本信息

- **编号**: #815
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/815
- **创建时间**: 2025-05-12T07:22:42Z
- **关闭时间**: 2025-05-16T02:44:29Z
- **更新时间**: 2025-05-16T15:40:45Z
- **提交者**: @shen-shanshan
- **评论数**: 8

## 标签

documentation; RFC

## 问题描述

Doc: https://docs.google.com/document/d/1F4mnGa8XDmj37vCbNS6Zso6sg4TzXr4RTkihTbhjLYw/

## Motivation

To achieve ultimate performance on vllm-asend `v0.7.3` with mindie-turbo `2.0rc1`, we have make efforts to optimize our codes, configs, etc.

Performance test:
- Qwen 2.5 7B

## Separate single item optimizations

- v0.7.3 base image (vllm-ascend) + Ubuntu: m.daocloud.io/quay.io/ascend/vllm-ascend:v0.7.3
- Each improvement
- Performance test
    - Qwen2.5-7B-Instruct
- Doc

## Overall optimizations
- e2e

### 1. Compiler Optimization (@MaskerPRC)

- python
- pytorch
- torch-npu

Depends on specific model:
- [ ] tiny enhancement (LTO) 
- [ ] about 27% enhancement (PGO for specific model)
- [ ] (today) Step 1: Doc (must be ready)
- [ ] Step 2: Can be reproduce in dockerfile

### 2. OS Optimization (@celestialli)
- Mem allocator etc, performance
- [ ] (0514) Step 1: Doc (must be ready)
- [ ] Step 2: Can be reproduce in dockerfile (host / container)

### 3. torch-npu Optimization (@Potabk)

- Memory
- Scheduler

### 4. CANN Optimization (@Potabk)

- HCCL ENV
- mindie-turbo ENV

### 5. vllm-ascend Optimization (@shen-shanshan)

V1 Ascend Scheduler:

- Implementation: https://github.com/vllm-project/vllm-ascend/pull/512
- Usage: https://github.com/vllm-project/vllm-ascend/issues/788

Offline inference test using `Qwen2.5-7B-Instruct`:

- **V1 without Ascend Scheduler**: speed input: 8.05 toks/s, output: **146.39** toks/s
- **V1 with Ascend Scheduler**: speed input: 8.86 toks/s, output: **161.15** toks/s, but have **accuracy problem** need to be fixed.

### 6. Dockerfile (@MaskerPRC)

...
