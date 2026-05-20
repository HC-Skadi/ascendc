#!/usr/bin/env python3
"""Unit tests for prelu NPU operator."""

import glob
import os

import pytest
import torch

try:
    import torch_npu  # noqa: F401
except ImportError:
    torch_npu = None

try:
    import ascend_kernel  # noqa: F401
except ImportError:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    lib_pattern = os.path.join(project_root, "python/ascend_kernel/ascend_kernel/lib/*.so")
    lib_files = glob.glob(lib_pattern)
    if lib_files:
        torch.ops.load_library(lib_files[0])
    else:
        ascend_kernel = None


def is_npu_available():
    try:
        return hasattr(torch, "npu") and torch.npu.is_available()
    except Exception:
        return False


@pytest.fixture(scope="module")
def device():
    if not is_npu_available():
        pytest.skip("NPU not available")
    return torch.device("npu:0")


def make_weight(shape, mode, dtype, device):
    if mode == "scalar":
        return torch.tensor([0.25], dtype=dtype, device=device)
    return torch.linspace(-0.5, 0.5, shape[1], dtype=torch.float32, device=device).to(dtype)


def prelu_reference(x, weight):
    return torch.prelu(x, weight)


class TestPrelu:
    @pytest.mark.parametrize(
        "shape,mode",
        [
            ((128,), "scalar"),
            ((8192,), "scalar"),
            ((32, 512), "channel"),
            ((8, 16, 64), "channel"),
            ((4, 8, 32, 16), "channel"),
            ((3,), "scalar"),
            ((5, 7), "channel"),
        ],
    )
    @pytest.mark.parametrize("dtype", [torch.float16, torch.bfloat16, torch.float32])
    def test_prelu(self, device, shape, mode, dtype):
        x = torch.randn(shape, dtype=torch.float32, device=device).to(dtype)
        weight = make_weight(shape, mode, dtype, device)

        npu_result = torch.ops.npu.prelu(x, weight)
        cpu_reference = prelu_reference(x.float().cpu(), weight.float().cpu()).to(dtype)

        rtol, atol = (1e-5, 1e-5)
        if dtype == torch.float16:
            rtol, atol = (1e-3, 1e-3)
        elif dtype == torch.bfloat16:
            rtol, atol = (8e-3, 8e-3)
        assert torch.allclose(npu_result.cpu(), cpu_reference, rtol=rtol, atol=atol), (
            f"max diff = {(npu_result.cpu().float() - cpu_reference.float()).abs().max().item()}"
        )


def run_simple_test():
    if not is_npu_available():
        print("NPU not available, skipping test")
        return False

    device = torch.device("npu:0")
    for dtype in [torch.float16, torch.bfloat16, torch.float32]:
        x = torch.randn((2, 4, 8), dtype=torch.float32, device=device).to(dtype)
        weight = make_weight(x.shape, "channel", dtype, device)
        result = torch.ops.npu.prelu(x, weight)
        print(f"dtype={dtype}, output shape={tuple(result.shape)} OK")
    print("Test PASSED!")
    return True


if __name__ == "__main__":
    run_simple_test()
