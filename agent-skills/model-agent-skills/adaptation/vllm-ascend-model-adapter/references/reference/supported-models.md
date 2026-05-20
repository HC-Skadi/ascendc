# Supported Models — vLLM-Ascend

## Text-Only Language Models

### Generative Models

#### Core Supported Models

| Model | Support | Note | BF16 | Hardware | W8A8 | Chunked Prefill | APC | LoRA | Spec Dec | Async Sched | TP | PP | EP | DP | PD Disagg | Piecewise AclGraph | Fullgraph AclGraph | max-model-len | MLP Prefetch |
|-------|---------|------|------|----------|------|-----------------|-----|------|----------|-------------|----|----|----|----|-----------|-------------------|-------------------|---------------|--------------|
| DeepSeek V3/3.1 | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 240k | ✅ |
| DeepSeek V3.2 | 🔵 | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 160k | ✅ |
| DeepSeek R1 | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 128k | ✅ |
| Qwen3 | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 128k | ✅ | | | | | |
| Qwen3-Coder | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | | | | | | | |
| Qwen3-Moe | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 256k | ✅ | | |
| Qwen3-Next | 🔵 | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | 🔵 | ✅ | | | | | | | |
| Qwen2.5 | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | | | | | | | | |
| GLM-4.x | 🔵 | | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 198k | ✅ | | |
| Kimi-K2-Thinking | 🔵 | | A2/A3 | 🔵 | | | | | | | | | | | | | | |
| DeepseekOCR2 | ✅ | ✅ | A2/A3 | ✅ | ✅ | 🔵 | | | | | | | | | | | | |

**Legend:** ✅ = Supported | 🔵 = Experimental | ❌ = Not supported | 🟡 = Not tested

#### Extended Compatible Models

| Model | Support | Note | Hardware |
|-------|---------|------|----------|
| DeepSeek Distill (Qwen/Llama) | ✅ | A2/A3 | |
| Qwen3-based | ✅ | A2/A3 | |
| Qwen2 | ✅ | A2/A3 | |
| QwQ-32B | ✅ | A2/A3 | |
| Llama2/3/3.1/3.2 | ✅ | A2/A3 | |
| Internlm | 🔵 | A2/A3 | |
| Baichuan | 🔵 | A2/A3 | |
| Phi-4-mini | 🔵 | A2/A3 | |
| MiniCPM | 🔵 | A2/A3 | |
| Gemma-2 | 🔵 | A2/A3 | |
| Phi-3/4 | 🔵 | A2/A3 | |
| Mistral/Mistral-Instruct | 🔵 | A2/A3 | |

## Pooling Models

| Model | Support | Note | Hardware |
|-------|---------|------|----------|
| Qwen3-Embedding | 🔵 | A2/A3 | |
| Qwen3-VL-Embedding | 🔵 | A2/A3 | |
| Qwen3-Reranker | 🔵 | A2/A3 | |
| Qwen3-VL-Reranker | 🔵 | A2/A3 | |
| Molmo | 🔵 | A2/A3 | |
| XLM-RoBERTa-based | 🔵 | A2/A3 | |
| Bert | 🔵 | A2/A3 | |

## Multimodal Language Models

### Generative Models

#### Core Supported Models

| Model | Support | Note | BF16 | Hardware | W8A8 | Chunked Prefill | APC | LoRA | Spec Dec | Async Sched | TP | PP | EP | Data Parallel | PD Disagg | max-model-len |
|-------|---------|------|------|----------|------|-----------------|-----|------|----------|-------------|----|----|----|---------------|-----------|---------------|
| Qwen2.5-VL | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 30k | | | | |
| Qwen3-VL | ✅ | | A2/A3 | ✅ | ✅ | ✅ | | | | | | | | | | |
| Qwen3-VL-MOE | ✅ | ✅ | A2/A3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 256k | ✅ | |

#### Extended Compatible Models

| Model | Support | Note | Hardware |
|-------|---------|------|----------|
| Qwen2-VL | ✅ | A2/A3 | |
| Qwen3-Omni | 🔵 | A2/A3 | |
| QVQ | 🔵 | A2/A3 | |
| Aria | 🔵 | A2/A3 | |
| LLaVA-Next | 🔵 | A2/A3 | |
| MiniCPM-V | 🔵 | A2/A3 | |
| Mistral3 | 🔵 | A2/A3 | |
| Gemma3 | 🔵 | A2/A3 | |
| Llama3.2 | 🔵 | A2/A3 | |

### Not Supported Models

| Model | Issue |
|-------|-------|
| Llama4 | Issue #1972 |
| Keye-VL-8B-Preview | Issue #1963 |
| Florence-2 | Issue #2259 |
| GLM-4V | Issue #2260 |
| InternVL2.0/2.5/3.0 | Issue #2064 |
| Whisper | Issue #2262 |

## Hardware Requirements

- **Atlas 800 A2**: Mainstream support
- **Atlas 800 A3**: Mainstream support
- **Atlas 900 A2/A3 SuperPoD**: Extended scenarios

## Feature Support Matrix

### Attention Types

| Attention Type | Support | Notes |
|---------------|---------|-------|
| Multi-Head Attention (MHA) | ✅ | Standard models |
| Multi-Query Attention (MQA) | ✅ | Some models |
| Grouped-Query Attention (GQA) | ✅ | Most models |
| Multi-Latent Attention (MLA) | ✅ | DeepSeek models |
| Sliding Window Attention | ✅ | Some models |

### Parallel Strategies

| Strategy | Support | Notes |
|---------|---------|-------|
| Tensor Parallel (TP) | ✅ | All core models |
| Pipeline Parallel (PP) | ✅ | MoE models |
| Expert Parallel (EP) | ✅ | MoE models |
| Data Parallel (DP) | ✅ | All models |
| PD Disaggregation | ✅ | DeepSeek models |

## Quick Reference Commands

### Check Model Support

To verify if a model is supported:
1. Check the tables above
2. Look for the model in vLLM-Ascend GitHub issues (#1608 for latest info)
3. Try loading with `--load-format dummy` first

### Model Type Detection

```python
from vllm import LLM

# For text models
llm = LLM(model="<model_path>", task="generate")

# For embedding models
llm = LLM(model="<model_path>", task="embed")

# For reranker models
llm = LLM(model="<model_path>", task="score")
```

## Contributing New Models

If a model is not listed:
1. Check GitHub issues for planned support
2. Use this skill to analyze compatibility
3. Follow the 10-step playbook in SKILL.md
4. Submit a PR to vllm-ascend project
