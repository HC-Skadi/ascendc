# vLLM Ascend 量化指南

> 本文档介绍如何使用 ModelSlim 和 LLM-Compressor 进行模型量化
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 量化概述

量化是通过降低模型权重和激活的精度来减少内存占用和提高推理速度的技术。vLLM Ascend 支持多种量化方法。

## 支持的量化类型

| 类型 | 权重精度 | 激活精度 | 内存节省 |
|------|---------|---------|---------|
| W4A8 | 4-bit | 8-bit | ~75% |
| W8A8 | 8-bit | 8-bit | ~50% |
| W4A4 | 4-bit | 4-bit | ~85% |

## 量化工具

vLLM Ascend 支持以下量化工具:

1. **ModelSlim**: 华为官方量化工具
2. **LLM-Compressor**: 开源量化工具

## 使用 ModelSlim 量化

### 安装 ModelSlim

```bash
# 克隆msit仓库
git clone -b br_release_MindStudio_8.1.RC2_TR5_20260624 https://gitcode.com/Ascend/msit

cd msit/msmodelslim

# 安装
bash install.sh
pip install accelerate
```

### 量化 Qwen3-8B 为 W4A8

```bash
cd example/Qwen

# 设置路径
MODEL_PATH=/home/models/Qwen3-8B
SAVE_PATH=/home/models/Qwen3-8B-w4a8

# 设置NPU设备
export ASCEND_RT_VISIBLE_DEVICES=0

# 运行量化
python quant_qwen.py \
    --model_path $MODEL_PATH \
    --save_directory $SAVE_PATH \
    --device_type npu \
    --model_type qwen3 \
    --calib_file None \
    --anti_method m6 \
    --anti_calib_file ./calib_data/mix_dataset.json \
    --w_bit 4 \
    --a_bit 8 \
    --is_lowbit True \
    --open_outlier False \
    --group_size 256 \
    --is_dynamic True \
    --trust_remote_code True \
    --w_method HQQ
```

### 量化参数说明

| 参数 | 说明 | 常用值 |
|------|------|--------|
| w_bit | 权重位宽 | 4, 8 |
| a_bit | 激活位宽 | 4, 8 |
| group_size | 量化组大小 | 128, 256 |
| w_method | 权重量化方法 | HQQ, AWQ |
| is_dynamic | 是否动态量化 | True, False |

### 量化 Qwen3-MoE 为 W8A8

```bash
cd example/Qwen3-MOE

# 设置多卡量化
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:False

# 设置路径
export MODEL_PATH="/path/to/your/model"
export SAVE_PATH="/path/to/your/quantized_model"

# 运行量化
python3 quant_qwen_moe_w8a8.py \
    --model_path $MODEL_PATH \
    --save_path $SAVE_PATH \
    --anti_dataset ../common/qwen3-moe_anti_prompt_50.json \
    --calib_dataset ../common/qwen3-moe_calib_prompt_50.json \
    --trust_remote_code True
```

## 使用量化模型

### Python 代码

```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The future of AI is",
]

sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=40)

# 使用量化模型
llm = LLM(
    model="/path/to/your/quantized_model",
    max_model_len=4096,
    trust_remote_code=True,
    tensor_parallel_size=2,
    data_parallel_size=1,
    quantization="ascend"
)

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(f"Generated: {output.outputs[0].text}")
```

### 命令行服务

```bash
vllm serve /path/to/your/quantized_model \
    --quantization ascend \
    --trust-remote-code \
    --tensor-parallel-size 2 \
    --max-model-len 4096
```

## 量化精度对比

### W4A8 量化

- 内存占用: 原始的 ~25%
- 精度损失: 通常 <2%
- 适用场景: 大模型、多卡部署

### W8A8 量化

- 内存占用: 原始的 ~50%
- 精度损失: 通常 <1%
- 适用场景: 中等模型、延迟敏感场景

## 动态量化 vs 静态量化

### 静态量化

- 离线量化,权重在推理前确定
- 优点: 推理速度快
- 缺点: 需要校准数据集

```bash
python quant_qwen.py \
    --is_dynamic False \
    --calib_file ./calib_data.json
```

### 动态量化

- 推理时动态量化权重
- 优点: 无需校准数据
- 缺点: 推理速度略慢

```bash
python quant_qwen.py \
    --is_dynamic True
```

## 量化最佳实践

### 1. 选择合适的量化位数

- 大模型 (>70B): 建议 W4A8
- 中等模型 (7B-70B): 建议 W8A8
- 小模型 (<7B): 可以使用全精度

### 2. 调整 group_size

- 较大的 group_size: 精度更高,内存更少
- 较小的 group_size: 精度略低,内存略多
- 推荐: 128 或 256

### 3. 验证量化模型

```python
from vllm import LLM, SamplingParams

# 加载量化模型
llm = LLM(
    model="/path/to/quantized/model",
    quantization="ascend"
)

# 测试推理
test_prompt = "Explain quantum computing in simple terms."
output = llm.generate(test_prompt, SamplingParams(max_tokens=200))

print(output.outputs[0].text)
```

### 4. 性能基准测试

```bash
# 使用vLLM benchmark
vllm bench throughput \
    --model /path/to/quantized/model \
    --dataset /path/to/dataset.json \
    --quantization ascend
```

## 常见问题

### 量化后模型无法加载

- 确认使用了正确的量化方法 (ascend)
- 检查模型路径是否正确
- 验证 trust_remote_code=True

### 量化精度损失过大

- 尝试更大的 group_size
- 使用更小的 w_bit
- 检查校准数据集质量

### 内存仍然不足

- 进一步减小 max_model_len
- 增加 tensor_parallel_size
- 使用更激进的量化 (W4A4)

## 相关资源

- [ModelSlim 文档](https://gitcode.com/Ascend/msit)
- [LLM-Compressor](https://github.com/vllm-project/llm-compressor)

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
