# Issue #448: vLLM Ascend Roadmap Q2 2025

## 基本信息

- **编号**: #448
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/448
- **创建时间**: 2025-03-31T12:14:16Z
- **关闭时间**: 2025-07-12T17:17:12Z
- **更新时间**: 2025-08-26T13:28:25Z
- **提交者**: @Yikun
- **评论数**: 7

## 标签

无

## 问题描述

This is a living document! 

---

Our vision is to enable vLLM to run seamlessly on Ascend NPU. We are fully committed to **making vLLM one of the best engines for Ascend NPU**. In Q1 2025, we have provided initial support for vLLM on Ascend NPU.

In 2025 Q2, we will focus on 4 themes: ***vLLM Ascend for Production, Performance Optimization, Key Features, Ecosystem Connect***.

## 1. Performance Optimization
*We will focus on the performance optimization of dense models (Qwen/Llama/Qwen-VL) and MOE models (DeepSeek V3/R1), users of vLLM Ascend can trust its performance to be competitive for Ascend NPU.*
- [x] (P0) [V0] Support torch.compile (aka Graph mode): https://github.com/vllm-project/vllm-ascend/pull/426
- [x] (P0) (v0.7.3 only) MindIE-turbo integration `pip install vllm-ascend[mindie-turbo]` @MengqingCao 
- [x] (P0) vLLM V1 engine improvement  [RFC Llink](https://github.com/vllm-project/vllm-ascend/issues/414) @wangxiyuan 
- [x] (P1) Performance report for DeepSeek R1, Qwen3, Qwen2.5, Qwen2.5-VL: [Add official Performance Guide Doc](https://vllm-ascend.readthedocs.io/en/latest/developer_guide/performance/index.html)

## 2. vLLM Ascend for Production
*Align with vLLM, vLLM Ascend is designed for production, the first official version for vLLM 0.7.3 will be published, we will also actively promote the key features of vLLM v0.8.x/v1 to production availability*
- [ ] (P0) Stable Plugin Architecture for hardware platforms @wangxiyuan 
- [x] (P0) CI: Model/Feature coverage: https://github.com/vllm-project/vllm-ascend/issues/413 @MengqingCao 
- [x] (P0) Testing: Performance test @leo-pony @hfadzxy
- [x] (P0) Testing: Accuracy test @leo-pony @hfadzxy
- [x] (P0) Testing: Stress and longevity test (downstream)

## 3. Key Features
*We will focus on the integration and support of key lifecycle workflow of model training (SFT / RL) and inference (singe node / distributed).*

### 3.1 Workflows

**Cluster Scale Serving**
- [x] (P0) MLA enhancements: https://github.com/vllm-project/vllm-ascend/pull/1135 , https://github.com/vllm-project/vllm-ascend/pull/917
- [x] (P0) Distributed EP: EP + DP https://github.com/vllm-project/vllm-ascend/pull/121
- [x] (P0) Prefill Decode Disaggregation: 1P1D, xPyD: https://github.com/vllm-project/vllm-ascend/issues/841
- [x] (P0) EPLB: https://github.com/vllm-project/vllm-ascend/pull/1116

**Core feature support**
- [x] (P0) LoRA / MultiLora: https://github.com/vllm-project/vllm-ascend/issues/396 @ZhengJun9
- [x] (P1) Structured Output on V1: https://github.com/vllm-project/vllm-ascend/issues/177 @shen-shanshan 
- [ ] (Help wanted) Prompt adapter

**RLHF**
- [x] Sleep mode: https://github.com/vllm-project/vllm-ascend/pull/416 @celestialli

### 3.2 Models support
- [x] (P0) Quantization support: w8a8 (DeepSeek R1 with 2 nodes): https://github.com/vllm-project/vllm-ascend/pull/580
- [x] (P1) Upcoming Qwen3 / DeepSeek-R2 / Llama4/DeepSeek DRM series new models support
    - [x] https://github.com/vllm-project/vllm-ascend/issues/471
    - [x] https://github.com/vllm-project/vllm-ascend/issues/642
- [x] (P1) Qwen-Omini-thinker: https://github.com/vllm-project/vllm-ascend/pull/736
- [ ] (P1) Model format support: gguf
- [ ] (Help wanted) Quantization support: w4a16/w4a8 (DeepSeek R1 with 1 node)
- [ ] (Help wanted) Whisper
- [ ] (Help wanted) enc-dec
- [ ] (Help wanted) Gemma

### 3.3 User / Developer Experience

**Distributions**
- [x] (P0) Docker image (mirror)
  - https://github.com/DaoCloud/public-image-mirror/pull/41777
- [x] (P0) Python Wheel: https://github.com/vllm-project/vllm-ascend/pull/775

**Docs**
- [ ] Developer Design doc: https://github.com/vllm-project/vllm-ascend/issues/1248
- [x] Developer Evaluation doc: https://github.com/vllm-project/vllm-ascend/issues/367

**Dashboard**
- [ ] Perf Dashboard
- [x] Accuracy DashBoard: https://vllm-ascend.readthedocs.io/en/latest/developer_guide/evaluation/accuracy_report/index.html

### 3.4 Hardware support
- [x] 310 series supported: https://github.com/vllm-project/vllm-ascend/pull/1333


## 4. Ecosystem Connect
*It is key to seamlessly integrate key lifecycle components with vLLM Ascend, so we are also actively connecting with the ecosystem.*
- [x] (P1) [SFT] LLaMA-Factory: https://github.com/hiyouga/LLaMA-Factory/pull/7739
- [x] (P1) [RLHF] verl: https://github.com/volcengine/verl/discussions/900
- [ ] (P1) [RLHF] OpenRLHF: https://github.com/OpenRLHF/OpenRLHF/pull/605
- [x] (P1) [RLHF] MindSpeed-RL: https://github.com/Ascend/MindSpeed-RL
- [x] (P1) [RLHF] TRL: https://github.com/huggingface/trl/pull/3286
- [x] (P1) [Deploy] GPUStack https://github.com/gpustack/gpustack/issues/1495
---

If any of the items you wanted is not on the roadmap, your suggestion and contribution is strongly welcomed! Please feel free to comment in this thread, open feature request, or create an RFC.

Historical Roadmap: https://github.com/vllm-project/vllm-ascend/issues/71
