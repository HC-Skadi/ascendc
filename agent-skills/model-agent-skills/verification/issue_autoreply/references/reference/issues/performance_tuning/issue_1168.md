# Issue #1168: vLLM Ascend Roadmap Q3 2025

## 基本信息

- **编号**: #1168
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1168
- **创建时间**: 2025-06-11T06:50:39Z
- **关闭时间**: 2025-11-07T11:22:32Z
- **更新时间**: 2025-11-07T11:22:32Z
- **提交者**: @wangxiyuan
- **评论数**: 12

## 标签

无

## 问题描述

This is a living document! We are eager to know what do you want for vLLM Ascend in Q3 2025. Any feedback is welcome.

Welcome to join [vLLM Ascend Weekly Meeting](https://tinyurl.com/vllm-ascend-meeting).

---

## Release plan
Next release v0.10.3 (v0.10.3rc1) (about 2025.09.23): https://github.com/vllm-project/vllm-ascend/milestone/4

---

As a vital component of vLLM, the vLLM Ascend project is dedicated to providing an easy, fast, and cheap LLM serving for everyone on Ascend NPU, and to actively contribute to the enrichment of vLLM.

In 2025 Q2, we have focused on 4 themes: vLLM Ascend for Production, Performance Optimization, Key Features, Ecosystem Connect. In 2025 Q3, we will focus on: ***Default V1 Engine、Quality and Production ready、User / Developer Experience、Competitive for Key Workflow***.

## 1. Default V1 Engine
- [ ] Stable plugin architecture for hardware platforms https://github.com/vllm-project/vllm/issues/22082
- [x] V1 Engine fully supports and cleanup V0 code path: https://github.com/vllm-project/vllm-ascend/issues/1620
- [x] Enable CustomOP register: https://github.com/vllm-project/vllm-ascend/pull/1647
- [ ] V1 feature support enhancement
  - [ ] Enc-Dec models
  - [x] V1 PP supports https://github.com/vllm-project/vllm-ascend/pull/1800
  - [x] xPyD #950
  - [ ] V1 scheduler

## 2. Quality and Production ready
- [x] Unit test coverage enhancement: https://github.com/vllm-project/vllm-ascend/issues/1298
    - [x] Coverage report: https://app.codecov.io/gh/vllm-project/vllm-ascend
- [x] E2e Test coverage
- [x] Model Support https://github.com/vllm-project/vllm-ascend/issues/1608
- [x] Benchmark Test
- [x] Accuracy Test 
- [x] Module refactor
  - [ ] model arch
  - [x] ops
  - [x] attention
  - [x] torchair
  - [x] quantization

## 3. User / Developer Experience
- [ ] Users doc: https://github.com/vllm-project/vllm-ascend/issues/1248
- [ ] Developer Design doc: https://github.com/vllm-project/vllm-ascend/issues/1248
- [ ] Distributions
- [ ] Perf Dashboard and Accuracy report
- [ ] Developer Experience
  - [x] vLLM commit hash recording: https://github.com/vllm-project/vllm-ascend/pull/1623

## 4. Competitive for Key Workflow

- Large Scale Serving
  - EPLB
      - [x] Dynamic EPLB: https://github.com/vllm-project/vllm/issues/22246
      - [x] static EPLB: https://github.com/vllm-project/vllm-ascend/pull/1116
  - Qwen series (Qwen3 / Qwen3 MoE) optimization https://github.com/vllm-project/vllm-ascend/pull/1245
  - Qwen series (Qwen3 MoE) optimization: https://github.com/vllm-project/vllm-ascend/pull/1381
  - Disaggregated Prefilling
    - [x] LLMDataDist: https://github.com/vllm-project/vllm-ascend/pull/950
    - [x] Mooncake: https://github.com/vllm-project/vllm-ascend/pull/1568
  - [ ] CP/SP https://github.com/vllm-project/vllm/issues/22693
  - [ ] AF Disaggregated https://github.com/vllm-project/vllm/issues/22799
  - 
- RLHF
    - [ ] Performance improvements
    - [ ] Parallel support
- Graph mode
    - [x] Support Full Graph with multiple attention kernels: https://github.com/vllm-project/vllm-ascend/issues/1649
    - [ ] Automatic Kernel Fusion via torch.fx.graph and graph rewriter for vLLM-Ascend: https://github.com/vllm-project/vllm-ascend/issues/2386
- Model
    - [x] Qwen/DeepSeek/Qwen VL series
    - [ ] Gemma3
    - [x] K2
    - [ ] New model support https://github.com/vllm-project/vllm-ascend/issues/1608
          - New trending models like: minimax / hunyuan / ERNIE
    - [x] Quantization support: w4a16/w4a8 for Dense model
    - [x] Quantization support: w4a16/w4a8 for MoE model
    - [ ] Model format support: awq, gguf

- Others
  - [ ] Atlas 300I series experimental support and perf enhancement: https://github.com/vllm-project/vllm-ascend/pull/1591
  - [x] LoRA performance enhancement. https://github.com/vllm-project/vllm-ascend/pull/1884


---

If any of the items you wanted is not on the roadmap, your suggestion and contribution is strongly welcomed! Please feel free to comment in this thread, open feature request, or create an RFC.

Historical Roadmap:
- https://github.com/vllm-project/vllm-ascend/issues/448
- https://github.com/vllm-project/vllm-ascend/issues/71 


