# Issue #5403: [User Story]: Deploy vLLM on Ascend NPU with GitCode Notebook 

## 基本信息

- **编号**: #5403
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5403
- **创建时间**: 2025-12-26T13:56:59Z
- **关闭时间**: 2025-12-27T13:53:07Z
- **更新时间**: 2025-12-27T13:53:07Z
- **提交者**: @wwjwisdom
- **评论数**: 3

## 标签

无

## 问题描述

### 📚 Title

Successful Zero-Day Deployment of DeepSeek-V2-Lite-Chat on Ascend NPU using vLLM-Ascend (Community Experience Sharing)

### About / Introduction

### Environment
- Hardware: Atlas 800T (Ascend 910B) via GitCode Notebook (1x NPU, 16 vCPU, 32GB RAM)
- Container Image: euler2.9-py38-torch2.1.0-cann8.0-openmind0.6-notebook
- vLLM version: v0.9.1 (cloned from Gitee mirror)
- vLLM-Ascend: Installed from main repository (no separate moe_support branch needed in my setup)
- Model: deepseek-ai/DeepSeek-V2-Lite-Chat (downloaded via hf-mirror.com)

### Deployment Summary
I successfully deployed and ran inference on **DeepSeek-V2-Lite-Chat** (a MoE model with MLA + MoE architecture) on a single Ascend NPU using vLLM-Ascend, achieving stable inference with bfloat16 precision, long context (32k), and reasonable concurrency.

Key configurations in the LLM initialization:

```python
llm = LLM(
    model=MODEL_PATH,
    device="npu",
    dtype="bfloat16",
    gpu_memory_utilization=0.75,
    max_model_len=32768,
    enable_prefix_caching=True,
    max_num_seqs=16,
    max_num_batched_tokens=4096,
    # MoE-related (single card)
    moe_expert_parallel_size=1,
)
```

### Bussiness Challenges

Additional env vars:
```
VLLM_USE_NPU=1
VLLM_NPU_GRAPH_MODE=0 (Eager mode was more stable for this MoE model)
```

### Solving challenges with vLLM Ascend and benefits

Model download worked smoothly with HF_ENDPOINT=https://hf-mirror.com.
Inference tests (Chinese/English prompts about DeepSeek-V2 innovations, MoE advantages, etc.) completed successfully with 100-500 tokens generated per request.
No OOM issues after setting gpu_memory_utilization=0.75.
Eager mode (VLLM_NPU_GRAPH_MODE=0) avoided potential graph-mode compatibility issues with DeepSeek-V2's MLA (as noted in FAQs for certain head counts).
This demonstrates excellent **zero-day / near-zero-day support** for DeepSeek-V2-Lite on Ascend NPUs — deployment was straightforward without custom patches.

### Extra Info

he project already has strong MoE support (including Expert Parallelism since v0.9.1 and ongoing DeepSeek-specific optimizations). It would be helpful to add **DeepSeek-V2-Lite-Chat** as an explicit example or tutorial in the documentation, similar to the existing DeepSeek-V3 multi-node guides. A single-NPU quick-start section would further lower the barrier for community users testing MoE models on Ascend.
Thanks to the maintainers and contributors for the great work on MoE optimization — this made rapid deployment possible!
