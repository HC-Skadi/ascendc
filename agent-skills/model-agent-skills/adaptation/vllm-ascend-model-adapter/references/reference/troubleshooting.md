# Troubleshooting — vLLM-Ascend

## Common Failures and Resolutions

### Startup Failures

#### HCCL Bind Error

**Symptom:**
```
RuntimeError: HCCL error in: ...
HCCL binding failed
```

**Root Cause:** Stale server holding port or HCCL not properly initialized.

**Resolution:**
```bash
# Kill stale processes on port 8000
lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs -r kill -9

# Or use pkill
pkill -f "vllm serve"
pkill -f "vllm.entrypoints"

# Free port before retry
netstat -tulpn | grep 8000
```

#### Out of Memory on Startup

**Symptom:**
```
OutOfMemoryError: CUDA out of memory
```

**Root Cause:** Model too large for configured memory, or memory fragmentation.

**Resolution:**
```bash
# Reduce memory fragmentation
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

# Reduce batch sizes
--max-num-seqs 8 \
--max-model-len 8192 \

# Increase memory utilization
--gpu-memory-utilization 0.85
```

#### ACLGraph Capture Error (507903)

**Symptom:**
```
RuntimeError: EZ9999: [PID:xxx] 507903...
ACL Graph capture error
```

**Root Cause:** Stream capture sequence invalidated due to incompatible operations.

**Resolution:**
```bash
# Enable AIV mode for hierarchical communication
export HCCL_OP_EXPANSION_MODE="AIV"

# Reduce max-model-len
--max-model-len 16384

# Or use eager mode temporarily
--enforce-eager
```

### Inference Failures

#### fp8 Quantization Not Supported

**Symptom:**
```
RuntimeError: fp8 quantization is currently not supported in npu
```

**Root Cause:** fp8 execution kernels absent on Ascend.

**Resolution:**
```bash
# Option 1: Use ascend quantization instead
--quantization ascend

# Option 2: Dequantize fp8 to bf16 at load
# Use weight + weight_scale_inv pairing
```

#### Shape Mismatch Under TP

**Symptom:**
```
RuntimeError: Shape mismatch: 128 vs 64 under tensor parallel
```

**Root Cause:** KV-head replication not properly handled.

**Resolution:**
```python
# Detect replicated KV heads
# Use local norm-shard path for distributed execution

# Check model config
config = AutoConfig.from_pretrained(model_path)
print(f"num_kv_heads: {config.num_kv_heads}")
print(f"num_attention_heads: {config.num_attention_heads}")
```

#### MLA Runtime Error

**Symptom:**
```
RuntimeError: AtbRingMLA runtime error after startup
```

**Root Cause:** MLA backend/RoPE implementation mismatch.

**Resolution:**
```bash
# Use eager mode as isolation fallback
--enforce-eager

# Check vllm-ascend MLA/RoPE implementation
# Verify MLA configuration matches model
```

#### AtbRingMLA with numHeads/kvHeads Ratio

**Symptom:**
```
RuntimeError: EZ9999: numHeads / numKvHeads = 8, MLA only support {32, 64, 128}
```

**Root Cause:** MLA requires specific KV head configurations.

**Resolution:**
```bash
# MLA only supports num_heads / num_kv_heads in {32, 64, 128}
# Use a model with compatible configuration, or
# Fall back to standard attention
--enforce-eager
```

### Model Loading Failures

#### Cannot Copy Out of Meta Tensor

**Symptom:**
```
RuntimeError: Cannot copy out of meta tensor
```

**Root Cause:** Meta tensor load path triggered unexpectedly.

**Resolution:**
```bash
# Isolate multimodal processing from model core
--limit-mm-per-prompt '{"image":0,"video":0,"audio":0}'

# Then investigate processor configuration
```

#### Skip Tensor Conversion Signature Mismatch

**Symptom:**
```
RuntimeError: skip_tensor_conversion signature mismatch
```

**Root Cause:** Processor API version mismatch between HF remote code and current transformers.

**Resolution:**
```python
# Text-only isolation to separate processor from model core
# Align processor implementation with expected API

# Check transformers version
import transformers
print(transformers.__version__)
```

### TorchDynamo Failures

#### Dynamo + Interpolate + NPU Contiguous

**Symptom:**
```
torch._dynamo.exc.Unsupported: interpolate operation
```

**Root Cause:** TorchDynamo compiles interpolate against CUDA semantics.

**Resolution:**
```bash
# Disable TorchDynamo
export TORCHDYNAMO_DISABLE=1

# Or use eager mode
--enforce-eager
```

#### Graph Capture Failures

**Symptom:**
```
RuntimeError: Failed to capture NPU graph
```

**Resolution:**
```bash
# Step 1: Reproduce to confirm
vllm serve <model> 2>&1 | grep "capture"

# Step 2: Isolate with enforce-eager
--enforce-eager

# Step 3: Check specific operations causing failure
# Usually from non-tensor operations in graph
```

### Multimodal Failures

#### VL Model OOM

**Symptom:**
```
OutOfMemoryError: VL model inference exceeded memory
```

**Resolution:**
```bash
# Reduce image resolution handling
---mm-cache-max-unit 1

# Limit concurrent images
--max-num-seqs 4

# Reduce max-model-len
--max-model-len 8192
```

#### Processor Loading Failures

**Symptom:**
```
ValueError: Processor class does not support
```

**Resolution:**
```python
# Check processor configuration
from transformers import AutoProcessor
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

# Override if needed
processor = AutoProcessor.from_pretrained(
    model_path,
    trust_remote_code=True,
    use_fast=True
)
```

## Fallback Ladder

When encountering failures, follow this ordered approach:

```
1. Reproduce once to confirm deterministic failure
        ↓
2. Add --enforce-eager
   → Isolate graph-capture vs operator failures
        ↓
3. [VL] TORCHDYNAMO_DISABLE=1
   → Isolate dynamo/interpolate/contiguous failures
        ↓
4. [VL] --limit-mm-per-prompt '{"image":0,"video":0,"audio":0}'
   → Isolate multimodal processor failures from model core
        ↓
5. Apply targeted code fix
   → Loop back to validation Stage A
```

## Environment Variable Quick Reference

| Variable | Purpose | Recommended |
|----------|---------|-------------|
| `ASCEND_RT_VISIBLE_DEVICES` | NPU device selection | `0,1,2,3` |
| `TASK_QUEUE_ENABLE` | Task queue for ACLGraph | `1` |
| `HCCL_OP_EXPANSION_MODE` | Hierarchical communication | `"AIV"` |
| `PYTORCH_NPU_ALLOC_CONF` | Memory allocation | `expandable_segments:True` |
| `HCCL_BUFFSIZE` | HCCL buffer size | Dynamic calculation |
| `VLLM_USE_V1` | Use V1 engine | `1` |
| `LD_PRELOAD` | Jemalloc for performance | `/usr/lib/.../libjemalloc.so.2` |

## Diagnostic Commands

### Check NPU Status

```bash
npu-smi info
npu-smi info -l  # List all devices
```

### Check Running Processes

```bash
ps aux | grep vllm
ps aux | grep python
```

### Check Port Usage

```bash
lsof -i :8000
netstat -tulpn | grep 8000
```

### Check Memory Usage

```bash
# NPU memory
npu-smi info -q -m memory

# System memory
free -h
```

### Validate Import

```bash
python -c "import vllm; print(vllm.__file__)"
# Should point to /vllm-workspace/vllm/
```

## Error Code Reference

| Error Code | Description | Resolution |
|------------|-------------|------------|
| EZ9999 | General runtime error | Check logs for details |
| 507903 | ACL graph capture | Set HCCL_OP_EXPANSION_MODE=AIV |
| E00101 | HCCL initialization | Kill stale processes |
| E00102 | Memory allocation | Reduce batch size |
| E00103 | Operator not found | Check operator compatibility |

## Getting Help

### Before Filing Issue

1. Confirm vllm-ascend version: `pip show vllm-ascend`
2. Confirm CANN version: `ascend-cann-py -v`
3. Check NPU driver: `npu-smi info`
4. Reproduce with `--enforce-eager`
5. Collect error logs

### Filing GitHub Issue

Include:
- Model name and source
- vllm-ascend version
- CANN version
- NPU device info
- Complete error traceback
- Minimal reproduction code
