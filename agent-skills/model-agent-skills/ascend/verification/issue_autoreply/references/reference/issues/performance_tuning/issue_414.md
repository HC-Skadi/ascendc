# Issue #414: [Guide] V1 Engine

## 基本信息

- **编号**: #414
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/414
- **创建时间**: 2025-03-27T13:15:07Z
- **关闭时间**: 2025-06-15T07:46:01Z
- **更新时间**: 2025-06-15T07:46:01Z
- **提交者**: @shen-shanshan
- **评论数**: 0

## 标签

guide

## 问题描述

## Overview

We added the basic V1 engine support in main and 0.7.3-dev branch. You can take a try now. Any feedback is welcome.

## How to use V1

### Installation

We can use `main` branch of vllm and vllm-ascend for a try:

```bash
# Install vLLM (latest)
git clone --depth 1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install . --extra-index https://download.pytorch.org/whl/cpu/

# Install vLLM Ascend (latest)
git clone --depth 1 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -e . --extra-index https://download.pytorch.org/whl/cpu/
```

Find more details [<u>here</u>](https://vllm-ascend.readthedocs.io/en/latest/installation.html).

### Usage

Before using V1, you need to set environment `VLLM_USE_V1=1` and `VLLM_WORKER_MULTIPROC_METHOD=spawn`.

If you are using vllm for offline inferencing, you need to add a `__main__` guard like as well:

```bash
if __name__ == '__main__':

    llm = vllm.LLM(...)
```

Find more details [<u>here</u>](https://docs.vllm.ai/en/latest/getting_started/troubleshooting.html#python-multiprocessing).

### Test

Currently, we enable the V1 engine E2E test on https://github.com/vllm-project/vllm-ascend/pull/389.

Run the command shown below to test V1 on vllm-ascend:

```bash
VLLM_USE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn pytest -sv tests
```
## RoadMap
We're now working on V1 Engine full support. Here is the detail info:

|Feature|vLLM Status| vllm-ascend Status| Next Step|
|--|--|--|--|
| Prefix Caching | 🚀 Optimized | No | Rely on CANN 8.1, need more test |
| Chunked Prefill | 🚀 Optimized | Don't supports MLA | Rely on V1 MLAAttention backend and V0 MLAAttention Chunked Prefill support |
| Logprobs Calculation | 🟢 Functional | 🟢 Functional |  |
| LoRA | 🟢 Functional | 🟢 Functional |  |
| Multimodal Models | 🟢 Functional | 🟢 Functional |  |
| FP8 KV Cache | 🟢 Functional on Hopper devices | Unrelated |  |
| Spec Decode | 🟢 Functional | 🟢 Functional |  |
| Prompt Logprobs with Prefix Caching | 🟢 Functional | No | Rely on Prefix Caching feature |
| Structured Output Alternative Backends | 🟡 Planned | No | https://github.com/vllm-project/vllm-ascend/issues/177 |
| Embedding Models | 🟡 Planned |  |  |
| Mamba Models | 🟡 Planned |  |  |
| Encoder-Decoder Models | 🟡 Planned |  |  |
| Async Output | 🟢 Functional | 🟢 Functional |  |
| Multi Step Scheduler | 🟢 Functional | 🟢 Functional |  |
| Beam Search | 🟢 Functional | 🟢 Functional |  |
| Guided Decoding | 🟢 Functional | 🟢 Functional | https://github.com/vllm-project/vllm-ascend/issues/177 |
| TP | 🟢 Functional | 🟢 Functional|  |
| PP | 🟢 Functional | 🟢 Functional |  |
| EP | 🟢 Functional | Need test | Need improve performance |
| DP | 🟢 Functional | No |  Need add DP support |
| MTP | 🟢 Functional | Need test |  Need more functional test |
| Model Support | 🟢 Functional | Only support Qwen-2/2.5 |  |
| Quantization | 🟢 Functional | No | working on w8a8 support |
| Ops | 🟢 Functional | 🟢 Functional |  |
| Request-level Structured Output Backend | 🔴 Deprecated |  |  |
| best_of | 🔴 Deprecated |  |  |
| Per-Request Logits Processors | 🔴 Deprecated |  |  |
| GPU <> CPU KV Cache Swapping | 🔴 Deprecated |  |  |
