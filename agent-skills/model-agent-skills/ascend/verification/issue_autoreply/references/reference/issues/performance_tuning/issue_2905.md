# Issue #2905: [RFC]: Performance optimation of decode in DeepSeek Large EP situation.

## 基本信息

- **编号**: #2905
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2905
- **创建时间**: 2025-09-13T04:05:10Z
- **关闭时间**: 2026-01-29T10:07:55Z
- **更新时间**: 2026-01-29T10:07:55Z
- **提交者**: @whx-sjtu
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

In Large EP situation, the performance of decoding is key to several important SLOs including TPOT and TPS. Here we list several main optimation methods concerning decoding phase of deepseek.

### MoE Multi-stream
In A2/A3, the cube core and vector core are separated, thus kernels running in cube core and kernels running in vector core can run in parallel to improve performance. We call this optimization CV-Parallel. Combined with calculation-communication parallel, we can almost completely hide the processing time of shared experts utilizing multi-stream.

<img width="2032" height="761" alt="Image" src="https://github.com/user-attachments/assets/dc25bfd6-80a6-4176-91fd-614ae76bbd13" />

### MLA Multi-stream
Same reason, we can utilize multi-stream to overlap the calculation of cube kernels and vector kernels in MLA.

<img width="1127" height="966" alt="Image" src="https://github.com/user-attachments/assets/60e3b1dc-2ffc-49ab-8ed0-a6272129ae5b" />

### LLM-Head TP
The calculation of matmul in LLM-Head is very long in Large EP situation, usually longer than 2ms. This is because in large EP situation we don't use TP in main model, and the parallel strategy of LLM-Head is aligned with main model. To optimize this we can apply unique TP to LLM-Head. Below is an example of performing TP2 to LLM-Head.

<img width="1214" height="350" alt="Image" src="https://github.com/user-attachments/assets/96f30ee0-009c-4054-9468-4e4225dc2f89" />

### External-DP Load Balance

<img width="830" height="627" alt="Image" src="https://github.com/user-attachments/assets/c160903b-60bc-4944-8dae-ab76ae045feb" />

### Proposed Change.

This RFC is ued to track the test process of the above features. Relevant codes are already merged into main branch.

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
