# Quantization Guide — vLLM-Ascend

## Overview

Model quantization reduces model size and computational overhead by lowering numerical precision. vLLM-Ascend supports multiple quantization algorithms through the ModelSlim integration.

## Supported Quantization Algorithms

| Algorithm | Weight | Activation | Weight Granularity | Activation Granularity | Type | Description |
|-----------|--------|------------|-------------------|----------------------|------|-------------|
| W4A16 | INT4 | FP16/BF16 | Per-Group | Per-Tensor | Static | 4-bit weight, 16-bit activation. For MoE expert layers, supports int32 packing |
| W8A16 | INT8 | FP16/BF16 | Per-Channel | Per-Tensor | Static | 8-bit weight, 16-bit activation. Balanced accuracy/performance |
| W8A8 | INT8 | INT8 | Per-Channel | Per-Tensor | Static | Static activation quantization |
| W8A8_DYNAMIC | INT8 | INT8 | Per-Channel | Per-Token | Dynamic | Dynamic activation with per-token scaling |
| W4A8_DYNAMIC | INT4 | INT8 | Per-Group | Per-Token | Dynamic | Two-step quantization (channel→group) |
| W4A4_FLATQUANT_DYNAMIC | INT4 | INT4 | Per-Channel | Per-Token | Dynamic | FlatQuant for activation smoothing |
| W8A8_MIX | INT8 | INT8 | Per-Channel | Per-Tensor/Token | Mixed | PD scenarios: dynamic for P node, static for D node |

## Static vs Dynamic Quantization

- **Static**: Pre-computed scaling factors. Better performance, lower precision.
- **Dynamic**: Compute scaling factors on-the-fly. Higher precision, slightly lower performance.

## Weight Granularity

- **Per-Tensor**: Single scale for entire weight matrix
- **Per-Channel**: One scale per output channel
- **Per-Group**: One scale per group of channels (e.g., 256 elements)

## Quantization Configuration

### Enable Quantization in vLLM

```bash
vllm serve <model_path> \
  --quantization ascend \
  --dtype bfloat16
```

### Quantization Method Selection

The `--quantization ascend` flag enables ascend quantization method. The specific algorithm (W8A8, W4A16, etc.) is determined by the model's quantization configuration file (`quant_model_description.json`).

## ModelSlim Quantization Tools

### Installation

```bash
# Clone msit repository (verified branch)
git clone -b br_release_MindStudio_8.1.RC2_TR5_20260624 https://gitcode.com/Ascend/msit

cd msit/msmodelslim
bash install.sh
pip install accelerate
```

### Quantize Qwen3-8B to W4A8

```bash
export ASCEND_RT_VISIBLE_DEVICES=0
export MODEL_PATH=/path/to/Qwen3-8B
export SAVE_PATH=/path/to/Qwen3-8B-W4A8

python quant_qwen.py \
  --model_path $MODEL_PATH \
  --save_directory $SAVE_PATH \
  --device_type npu \
  --model_type qwen3 \
  --w_bit 4 \
  --a_bit 8 \
  --is_lowbit True \
  --group_size 256 \
  --is_dynamic True \
  --trust_remote_code True \
  --w_method HQQ
```

### Quantize Qwen3-MoE to W8A8

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export MODEL_PATH=/path/to/Qwen3-MoE
export SAVE_PATH=/path/to/Qwen3-MoE-W8A8

python3 quant_qwen_moe_w8a8.py \
  --model_path $MODEL_PATH \
  --save_path $SAVE_PATH \
  --anti_dataset ../common/qwen3-moe_anti_prompt_50.json \
  --calib_dataset ../common/qwen3-moe_calib_prompt_50.json \
  --trust_remote_code True
```

## Quantized Model Description File

When loading quantized models, vLLM-Ascend reads `quant_model_description.json`:

```json
{
    "model.layers.0.linear_attn.dt_bias": "FLOAT",
    "model.layers.0.linear_attn.A_log": "FLOAT",
    "model.layers.0.linear_attn.conv1d.weight": "FLOAT",
    "model.layers.0.linear_attn.in_proj_qkvz.weight": "W8A8_DYNAMIC",
    "model.layers.0.linear_attn.in_proj_qkvz.weight_scale": "W8A8_DYNAMIC",
    "model.layers.0.linear_attn.in_proj_qkvz.weight_offset": "W8A8_DYNAMIC",
    "model.layers.0.linear_attn.in_proj_ba.weight": "FLOAT",
    "model.layers.0.linear_attn.norm.weight": "FLOAT",
    "model.layers.0.linear_attn.out_proj.weight": "FLOAT",
    "model.layers.0.mlp.gate.weight": "FLOAT",
    "model.layers.0.mlp.experts.0.gate_proj.weight": "W8A8_DYNAMIC",
    "model.layers.0.mlp.experts.0.gate_proj.weight_scale": "W8A8_DYNAMIC",
    "model.layers.0.mlp.experts.0.gate_proj.weight_offset": "W8A8_DYNAMIC"
}
```

## Fused Module Mapping

For quantized models, fused modules must be mapped correctly:

```python
packed_modules_model_mapping = {
    "qwen3_moe": {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
        "experts": [
            "experts.0.gate_proj",
            "experts.0.up_proj",
            "experts.0.down_proj",
        ],
    },
}
```

Location: `vllm_ascend/quantization/modelslim_config.py`

## Quantization Adaptation

### Adding New Quantized Model

Requirements:
1. Original model must be successfully adapted in vLLM-Ascend
2. Add `model_type` to `packed_modules_model_mapping` in `modelslim_config.py`
3. All quantization algorithms must be integrated into the quantization module

### Adding New Quantization Algorithm

**Step 1: Algorithm Design**
- Define algorithm ID (e.g., `W4A8_DYNAMIC`)
- Determine supported layers (linear, moe, attention)
- Design quantization scheme (static/dynamic, per-tensor/channel/group)

**Step 2: Registration**
```python
from vllm_ascend.quantization.methods import register_scheme, AscendLinearScheme

@register_scheme("W4A8_DYNAMIC", "linear")
class AscendW4A8DynamicLinearMethod(AscendLinearScheme):
    ...
```

**Step 3: Implementation**
- Create implementation file: `vllm_ascend/quantization/methods/w4a8.py`
- Implement `create_weights`, `process_weights_after_loading`, and `apply` methods

**Step 4: Testing**
- Generate quantization configurations
- Verify correctness and performance

## Serving Quantized Models

### Online Serving

```bash
export VLLM_USE_MODELSCOPE=true
export MODEL_PATH=vllm-ascend/Qwen3-8B-W4A8

vllm serve ${MODEL_PATH} \
  --served-model-name "qwen3-8b-w4a8" \
  --max-model-len 4096 \
  --quantization ascend
```

### Offline Inference

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="/model/Qwen3-32B-W8A8",
    tensor_parallel_size=4,
    trust_remote_code=True,
    quantization="ascend",
    compilation_config={"cudagraph_mode": "FULL_DECODE_ONLY"}
)

outputs = llm.generate(prompts, SamplingParams(temperature=0.6, top_p=0.95))
```

## Quantization Best Practices

1. **For Memory-Constrained Deployments**: Use W4A16 or W4A8_DYNAMIC
2. **For Accuracy-Critical Applications**: Use W8A16 or W8A8_DYNAMIC
3. **For Balanced Performance**: Use W8A8 (static)
4. **For MoE Models**: W4A16 is recommended for expert layers

## Troubleshooting

### fp8 Quantization Not Supported

**Error:** `fp8 quantization is currently not supported in npu`

**Solution:** Use ascend quantization instead, or dequantize fp8→bf16 at load time using `weight` + `weight_scale_inv` pairing.

### Shape Mismatch Under TP

**Issue:** KV-head replication not handled

**Solution:** Detect replicated KV heads; use local norm-shard path for distributed execution.

### Quant Model Description Missing

**Issue:** `quant_model_description.json` not found

**Solution:** Ensure the quantized model directory contains the quantization configuration file. If not, regenerate quantization with ModelSlim tools.
