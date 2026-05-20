# PReLU 用例设计文档

## 1. 算子标杆

PyTorch 参考实现：

```python
import torch


def prelu_reference(self: torch.Tensor, weight: torch.Tensor) -> torch.Tensor:
    return torch.prelu(self, weight)


def prelu_formula_reference(self: torch.Tensor, weight: torch.Tensor) -> torch.Tensor:
    if weight.numel() == 1:
        alpha = weight.reshape(())
        weight_view = alpha
    else:
        view_shape = [1] * self.dim()
        view_shape[1] = weight.numel()
        weight_view = weight.reshape(view_shape)
    return torch.where(self > 0, self, self * weight_view)
```

---

## 2. 用例说明

### 2.1 测试配置

```python
SUPPORTED_DTYPES = [torch.float16, torch.bfloat16, torch.float32]

TEST_SHAPES = [
    ("scalar_weight_1d", "1D vector, scalar weight", (128,), "scalar"),
    ("scalar_weight_1d_large", "1D 8192 elements, scalar weight", (8192,), "scalar"),
    ("channel_weight_2d", "2D N x C, channel weight", (32, 512), "channel"),
    ("channel_weight_2d_large_c", "2D large C, channel weight", (64, 768), "channel"),
    ("channel_weight_3d", "3D N x C x L, channel weight", (8, 16, 64), "channel"),
    ("channel_weight_3d_large_inner", "3D large inner, channel weight", (4, 128, 256), "channel"),
    ("channel_weight_4d_nchw", "4D NCHW, channel weight", (4, 8, 32, 16), "channel"),
    ("channel_weight_4d_c64", "4D C=64, channel weight", (2, 64, 32, 32), "channel"),
]

GENERAL_SHAPES = [
    ("small_scalar_single", "single element scalar weight", (1,), "scalar"),
    ("small_scalar_unaligned3", "unaligned 1D length 3", (3,), "scalar"),
    ("small_scalar_unaligned7", "unaligned 1D length 7", (7,), "scalar"),
    ("small_channel_2d", "small 2D channel weight", (2, 2), "channel"),
    ("small_channel_inner1", "innerSize=1 channel path", (5, 7), "channel"),
    ("small_channel_3d", "small 3D channel weight", (2, 3, 5), "channel"),
    ("large_scalar_bert_ffn", "BERT FFN vector scalar weight", (4096,), "scalar"),
    ("large_channel_bert", "BERT-like 512x768 channel weight", (512, 768), "channel"),
    ("large_channel_gpt", "GPT-like 1024x1024 channel weight", (1024, 1024), "channel"),
    ("large_channel_vit", "ViT-like 8x197x768 channel weight", (8, 197, 768), "channel"),
]

BOUNDARY_VALUES = [
    ("all_zero", "all elements are zero"),
    ("all_positive", "all elements are positive"),
    ("all_negative", "all elements are negative"),
    ("mixed_sign", "positive, negative and zero mixed"),
    ("tiny_values", "values around zero: +/-1e-3"),
    ("large_values", "values around +/-100"),
]
```

### 2.2 用例覆盖统计

| 类别 | Shape数量 | 边界值数量 | dtype数量 | 总用例数 |
|------|----------|-----------|----------|---------|
| 常规形状 | 8 | - | 3 | 24 |
| 泛化形状 | 10 | - | 3 | 30 |
| 边界值 | 2 个代表 shape | 6 | 3 | 36 |
| **总计** | **18** | **6** | **3** | **90** |

---

## 3. 使用说明

### 生成测试数据示例

```python
def make_weight(shape, mode, dtype, device):
    if mode == "scalar":
        return torch.tensor([0.25], dtype=dtype, device=device)
    return torch.linspace(-0.5, 0.5, shape[1], dtype=torch.float32, device=device).to(dtype)


def make_input(shape, boundary, dtype, device):
    if boundary == "all_zero":
        data = torch.zeros(shape, dtype=torch.float32, device=device)
    elif boundary == "all_positive":
        data = torch.rand(shape, dtype=torch.float32, device=device) * 10 + 1e-3
    elif boundary == "all_negative":
        data = -(torch.rand(shape, dtype=torch.float32, device=device) * 10 + 1e-3)
    elif boundary == "tiny_values":
        data = (torch.rand(shape, dtype=torch.float32, device=device) - 0.5) * 2e-3
    elif boundary == "large_values":
        data = (torch.rand(shape, dtype=torch.float32, device=device) - 0.5) * 200
    else:
        data = torch.randn(shape, dtype=torch.float32, device=device)
    return data.to(dtype)
```

### 注意事项

1. `weight` dtype 必须与 `self` 一致，device 必须一致。
2. `weight.numel() == 1` 覆盖标量斜率路径。
3. `weight.numel() == self.size(1)` 覆盖按通道广播路径，要求 `self.dim() >= 2`。
4. 当前 AscendC 实现默认要求输入可 contiguous；非 contiguous 输入由 Host 端转 contiguous 后计算。
