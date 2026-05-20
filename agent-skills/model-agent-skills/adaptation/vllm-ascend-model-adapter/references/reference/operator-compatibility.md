# Operator Compatibility — vLLM-Ascend

## Overview

Understanding operator compatibility is critical for adapting models to Ascend NPUs. This guide classifies operators and provides decision logic for the operator compatibility gate.

## Operator Classification

### Type 1: Native PyTorch Operators

| Status | ✅ FULLY SUPPORTED |
|--------|-------------------|

Native PyTorch operators work without modification on Ascend NPUs because they use Torch NPU backend.

**Examples:**
- `torch.matmul` with NPU tensors
- `torch.nn.functional.linear`
- `torch.layer_norm`
- `torch.softmax`
- Basic tensor operations (view, transpose, permute, etc.)

**Verification:**
```python
import torch
x = torch.randn(128, 512, device='npu')
y = torch.randn(512, 256, device='npu')
result = torch.matmul(x, y)  # Works automatically
```

### Type 2: Triton Kernels

| Status | ⚠️ VERIFICATION REQUIRED |
|--------|-------------------------|

Triton kernels may or may not work on Ascend. Verification is mandatory.

**Common Triton Kernels in vLLM:**
- FlashAttention implementations
- Custom matrix multiplication kernels
- Specialized activation functions

**Verification Process:**
1. Run functional test with small inputs
2. Compare outputs against reference (CPU/CUDA)
3. Measure performance on Ascend
4. If accuracy degradation > 1% or functional failure: **BLOCK**

### Type 3: CUDA-Only Operators

| Status | ❌ NOT SUPPORTED |
|--------|-------------------|

Pure CUDA operators cannot run on Ascend NPUs without translation.

**Examples:**
- `torch.cuda.synchronize()` (should be removed)
- CUDA-specific memory operations
- Custom CUDA kernels without NPU equivalents

**Decision Tree:**
```
CUDA Operator Encountered
        │
        ├─ Has Torch fallback? ──YES──▶ Use Torch fallback, document
        │
        ├─ Has Triton equivalent? ──YES──▶ Use Triton, verify
        │
        └─ No fallback? ──NO──▶ EARLY EXIT
                                File GitHub issue
```

## Operator Compatibility Matrix

### Attention Operators

| Operator | CUDA | Triton | Torch NPU | Notes |
|----------|------|--------|-----------|-------|
| `torch.nn.functional.scaled_dot_product_attention` | N/A | ✅ | ✅ | Preferred |
| `flash_attn_varlen_func` | ✅ | ✅ | ✅ | Supported |
| `flash_attn_func` | ✅ | ✅ | ✅ | Supported |
| `torch.nn.functional.flash_attention` | N/A | N/A | ✅ | PyTorch 2.0+ |
| Custom QKV projection | N/A | N/A | ✅ | Standard linear |

### Linear Layer Operators

| Operator | CUDA | Triton | Torch NPU | Notes |
|----------|------|--------|-----------|-------|
| `torch.nn.functional.linear` | N/A | N/A | ✅ | Standard |
| `torch.matmul` | N/A | N/A | ✅ | Standard |
| GroupedMatmul (MoE) | N/A | ✅ | ✅ | Via npu_grouped_matmul |
| Quantized linear | N/A | N/A | ✅ | Via ascend quantization |

### Normalization Operators

| Operator | CUDA | Triton | Torch NPU | Notes |
|----------|------|--------|-----------|-------|
| `torch.nn.functional.layer_norm` | N/A | N/A | ✅ | Standard |
| `torch.nn.functional.rms_norm` | N/A | N/A | ✅ | Standard |
| `aplay_rmsnorm` | N/A | ✅ | N/A | Triton kernel |
| `aplay_fused_add_rmsnorm` | N/A | ✅ | N/A | Triton kernel |

### MoE-Specific Operators

| Operator | Status | Notes |
|----------|--------|-------|
| `npu_moe_init_routing` | ✅ | Basic routing |
| `npu_moe_init_routing_v2` | ✅ | Recommended, supports scale |
| `npu_grouped_matmul` | ✅ | Basic grouped matmul |
| `npu_grouped_matmul_swiglu_quant` | ✅ | Fusion operator |
| `aclnnMoeInitRoutingQuantV2` | ✅ | Production recommended |
| `Dispatch/Combine MC2` | ✅ | Hierarchical communication |

### Activation Functions

| Operator | CUDA | Triton | Torch NPU | Notes |
|----------|------|--------|-----------|-------|
| `torch.nn.functional.silu` | N/A | N/A | ✅ | Standard |
| `torch.nn.functional.gelu` | N/A | N/A | ✅ | Standard |
| `swiglu` (custom) | N/A | ✅ | ✅ | Via Triton or NPU |

## Operator Gate Decision Logic

### Step 3 — Operator Compatibility Gate

```python
def classify_operator(op_source_code):
    """
    Returns: TORCH | TRITON | CUDA | UNKNOWN
    """
    if "cuda" in op_source_code.lower() and "torch" not in op_source_code:
        return "CUDA"
    elif "@triton" in op_source_code or "triton" in op_source_code:
        return "TRITON"
    elif "torch" in op_source_code:
        return "TORCH"
    else:
        return "UNKNOWN"

def compatibility_action(op_type, has_fallback=False):
    if op_type == "TORCH":
        return "SUPPORTED", "Note performance uncertainty"
    elif op_type == "TRITON":
        return "VERIFY", "Verify correctness and accuracy on Ascend"
    elif op_type == "CUDA":
        if has_fallback:
            return "USE_FALLBACK", "Document fallback path"
        else:
            return "BLOCKED", "Early exit - file GitHub issue"
    else:
        return "UNKNOWN", "Manual investigation required"
```

## CUDA-to-NPU Migration Guide

### Common CUDA Patterns and NPU Equivalents

| CUDA Pattern | NPU Equivalent | Notes |
|------------|----------------|-------|
| `torch.cuda.synchronize()` | Remove or use `torch.npu.synchronize()` | Remove if not needed |
| `torch.cuda.empty_cache()` | `torch.npu.empty_cache()` | Same API |
| `torch.cuda.current_device()` | `torch.npu.current_device()` | Same API |
| `tensor.cuda()` | `tensor.npu()` | Same API |
| `tensor.to("cuda")` | `tensor.to("npu")` | Same API |
| CUDA streams | NPU streams via `torch.npu.Stream` | Different creation |

### Code Scanning Example

```bash
# Find CUDA-specific code in model files
grep -rn "cuda" vllm/model_executor/models/*.py | grep -v "# cuda"

# Check for problematic patterns
grep -rn "\.cuda\(\)" vllm/model_executor/models/
grep -rn "torch\.cuda\." vllm/model_executor/models/
```

## Early Exit Criteria

### Immediate Exit Required When:

1. **Pure CUDA kernel without fallback**
   - No Torch equivalent exists
   - No Triton equivalent exists
   - No NPU-specific implementation exists

2. **Triton kernel verification fails**
   - Functional incorrectness
   - Accuracy degradation > 1%
   - Performance unacceptable

### GitHub Issue Template for Early Exit

```markdown
## Operator Blocking Report

### Blocking Operator
- **File**: `<path/to/operator>`
- **Type**: CUDA-only / Triton verification failed
- **Issue**: `<specific failure>`

### Why No Fallback Exists
`<explanation>`

### Recommended Path Forward
1. Option A: Implement custom Ascend op
2. Option B: Replace with existing NPU-compatible alternative
3. Option C: Wait for upstream Triton/framework support

### Impact
- Blocked models: `<list>`
- Severity: Critical
```

## Verification Test Template

```python
import torch
import numpy as np

def verify_operator_on_npu(op_func, inputs, rtol=1e-3, atol=1e-5):
    """
    Verify operator produces correct results on NPU.
    
    Args:
        op_func: Function to test
        inputs: Tuple of input tensors
        rtol: Relative tolerance
        atol: Absolute tolerance
    
    Returns:
        (passed: bool, max_diff: float, details: str)
    """
    # Run on NPU
    torch.npu.set_device(0)
    npu_inputs = [x.npu() if isinstance(x, torch.Tensor) else x for x in inputs]
    npu_result = op_func(*npu_inputs)
    
    # Run on CPU for reference
    cpu_inputs = [x.cpu() if isinstance(x, torch.Tensor) else x for x in inputs]
    cpu_result = op_func(*cpu_inputs)
    
    # Compare
    if isinstance(npu_result, torch.Tensor):
        npu_result = npu_result.cpu()
    
    try:
        np.testing.assert_allclose(
            npu_result.numpy(), 
            cpu_result.numpy() if isinstance(cpu_result, torch.Tensor) else cpu_result,
            rtol=rtol, 
            atol=atol
        )
        return True, 0.0, "Results match within tolerance"
    except AssertionError as e:
        max_diff = np.abs(
            npu_result.numpy() - 
            (cpu_result.numpy() if isinstance(cpu_result, torch.Tensor) else cpu_result)
        ).max()
        return False, max_diff, str(e)
```

## Integration with Skill Workflow

The operator compatibility gate (Step 3) must complete before:
- Writing any adaptation code (Step 6)
- Running validation (Step 7)

This prevents investing time in models that cannot run on Ascend due to operator limitations.
