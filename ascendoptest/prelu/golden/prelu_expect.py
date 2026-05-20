import numpy as np
import torch
from ml_dtypes import bfloat16


def _numpy_to_torch(arr):
    if arr.dtype == bfloat16:
        return torch.from_numpy(arr.astype(np.float32))
    if arr.dtype == np.float16:
        return torch.from_numpy(arr.astype(np.float32))
    return torch.from_numpy(arr.astype(np.float32, copy=False))


def _cast_like(arr_fp32, ref):
    if ref.dtype == bfloat16:
        return arr_fp32.astype(np.float32).astype(bfloat16)
    return arr_fp32.astype(ref.dtype)


def _prelu_core(x, weight):
    x_t = _numpy_to_torch(x)
    w_t = _numpy_to_torch(weight)
    result = torch.nn.functional.prelu(x_t, w_t)
    return [_cast_like(result.cpu().numpy(), x)]


def prelu_custom_expect(x, weight):
    return _prelu_core(x, weight)


def prelu_builtin_expect(x, weight):
    return _prelu_core(x, weight)
