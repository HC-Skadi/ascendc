# Issue #1315: [release] 0.9.1rc1 release checklist

## 基本信息

- **编号**: #1315
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1315
- **创建时间**: 2025-06-20T08:46:59Z
- **关闭时间**: 2025-06-26T07:02:04Z
- **更新时间**: 2025-06-30T04:57:49Z
- **提交者**: @Yikun
- **评论数**: 8

## 标签

new model

## 问题描述

## Prepare v0.9.1rc1

### 1. model support

- [x] Download models 2025.06.20
   - [x] A2 4 cards to Ascend02 @shen-shanshan 
   - [x] 310P 8 cards to 310P @leo-pony

- [x] Altlas A2 series  2025.06.21
  - [x] PR validation:  @shen-shanshan 
  - [x] Run passed on with CANN 8.1rc1 @shen-shanshan 
  - [x] Docker image e2e test @shen-shanshan 
  - [x] Run accuracy: gsm8k @shen-shanshan 
  - [ ] Doc Turtorial: `Multi-NPU (XXXX 72B)` @shen-shanshan

- [x] Altlas 300I DUO series  2025.06.21
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1333
    - [x]  Dockerfile 310P and github action workflow @wangxiyuan  https://github.com/vllm-project/vllm-ascend/pull/1318
        - TAG(ubuntu): `main-310p`, `v0.9.1rc1-310p` 
    - [x] 310 support: https://github.com/vllm-project/vllm-ascend/pull/914
    - [x] 310 moe support: https://github.com/vllm-project/vllm-ascend/pull/1327
    - [x]  Run passed with CANN 8.1rc1 on 300I DUO @leo-pony
  - [ ] Doc Turtorial: `Multi-NPU (300I DUO)` @leo-pony https://github.com/vllm-project/vllm-ascend/pull/1341
  - [ ] (Before 0627) Add CI infra for 310p

### 2. PR to be merged

0.9.1-dev: 
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1277
- [x] https://github.com/vllm-project/vllm-ascend/pull/1311
- [x] https://github.com/vllm-project/vllm-ascend/pull/1320

main：
- [ ] release note
- [x] https://github.com/vllm-project/vllm-ascend/pull/1032
- [x] https://github.com/vllm-project/vllm-ascend/pull/1333
    - [x] https://github.com/vllm-project/vllm-ascend/pull/914
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1318
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1327

DNM:
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1284
- [ ] https://github.com/vllm-project/vllm-ascend/pull/950
- [ ] https://github.com/vllm-project/vllm-ascend/pull/1273
