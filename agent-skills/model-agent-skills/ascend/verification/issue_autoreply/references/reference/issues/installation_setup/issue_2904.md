# Issue #2904: Triton Verification process

## 基本信息

- **编号**: #2904
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2904
- **创建时间**: 2025-09-12T17:19:29Z
- **关闭时间**: 2025-12-29T12:05:29Z
- **更新时间**: 2025-12-29T12:05:29Z
- **提交者**: @fffrog
- **评论数**: 5

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

- get latest images of main branch: `docker pull quay.io/ascend/vllm-ascend:main`
- start the container with the image mentioned above
- get and install necessary packages:
  - bisheng compiler: https://modelers.cn/models/SGLangAscend/Qwen3-Next-80B-A3B-Instruct/blob/main/README.md
  - triton ascend: https://modelers.cn/models/SGLangAscend/Qwen3-Next-80B-A3B-Instruct/blob/main/README.md
- Add bisheng compiler path to environment PATH variable
- install test suite: `pip3 install pytest`
- test the pytest scripts below with the command: `pytest -v a.py`
```Python
from typing import Optional

import pytest
import torch
import torch.nn.functional as F

from einops import rearrange
from vllm.platforms import current_platform
from vllm.model_executor.layers.mamba.ops.causal_conv1d import causal_conv1d_update

def causal_conv1d_update_ref(x,
                             conv_state,
                             weight,
                             bias=None,
                             activation=None,
                             cache_seqlens=None):
    """
    x: (batch, dim) or (batch, dim, seqlen)
    conv_state: (batch, dim, state_len), where state_len >= width - 1
    weight: (dim, width)
    bias: (dim,)
    cache_seqlens: (batch,), dtype int32.
        If not None, the conv_state is treated as a circular buffer.
        The conv_state will be updated by copying x to the
        conv_state starting at the index
        @cache_seqlens % state_len before performing the convolution.

    out: (batch, dim) or (batch, dim, seqlen)
    """
    if activation not in [None, "silu", "swish"]:
        raise NotImplementedError("activation must be None, silu, or swish")
    dtype_in = x.dtype
    unsqueeze = x.dim() == 2
    if unsqueeze:
        x = x.unsqueeze(-1)
    batch, dim, seqlen = x.shape
    width = weight.shape[1]
    state_len = conv_state.shape[-1]
    assert conv_state.shape == (batch, dim, state_len)
    assert weight.shape == (dim, width)
    if cache_seqlens is None:
        x_new = torch.cat([conv_state, x], dim=-1).to(
            weight.dtype)  # (batch, dim, state_len + seqlen)
        conv_state.copy_(x_new[:, :, -state_len:])
    else:
        width_idx = torch.arange(
            -(width - 1), 0, dtype=torch.long,
            device=x.device).unsqueeze(0) + cache_seqlens.unsqueeze(1)
        width_idx = torch.remainder(width_idx, state_len).unsqueeze(1).expand(
            -1, dim, -1)
        x_new = torch.cat([conv_state.gather(2, width_idx), x],
                          dim=-1).to(weight.dtype)
        copy_idx = torch.arange(
            seqlen, dtype=torch.long,
            device=x.device).unsqueeze(0) + cache_seqlens.unsqueeze(1)
        copy_idx = torch.remainder(copy_idx,
                                   state_len).unsqueeze(1).expand(-1, dim, -1)
        conv_state.scatter_(2, copy_idx, x)
    out = F.conv1d(x_new, weight.unsqueeze(1), bias, padding=0,
                   groups=dim)[:, :, -seqlen:]
    if unsqueeze:
        out = out.squeeze(-1)
    return (out if activation is None else F.silu(out)).to(dtype=dtype_in)


@pytest.mark.parametrize("itype", [torch.bfloat16])
@pytest.mark.parametrize("silu_activation", [False])
@pytest.mark.parametrize("has_bias", [False])
@pytest.mark.parametrize("seqlen", [1])
@pytest.mark.parametrize("width", [4])
@pytest.mark.parametrize("dim", [4096])
def test_causal_conv1d_update(dim, width, seqlen, has_bias, silu_activation,
                              itype):
    device = "npu"
    rtol, atol = (3e-4, 1e-3) if itype == torch.float32 else (3e-3, 5e-3)
    if itype == torch.bfloat16:
        rtol, atol = 1e-2, 5e-2
    # set seed
    current_platform.seed_everything(0)
    batch = 2
    x = torch.randn(batch, dim, seqlen, device=device, dtype=itype)
    x_ref = x.clone()
    conv_state = torch.randn(batch, dim, width - 1, device=device, dtype=itype)

    weight = torch.randn(dim, width, device=device, dtype=itype)
    bias = torch.randn(dim, device=device, dtype=itype) if has_bias else None
    conv_state_ref = conv_state.detach().clone()
    activation = None if not silu_activation else "silu"

    out_ref = causal_conv1d_update_ref(x_ref,
                                       conv_state_ref,
                                       weight,
                                       bias,
                                       activation=activation)
    print(out_ref)

    out = causal_conv1d_update(x,
                               conv_state,
                               weight,
                               bias,
                               activation=activation)
    print(out)

    assert torch.equal(conv_state, conv_state_ref)
    assert torch.allclose(out, out_ref, rtol=rtol, atol=atol)
```
