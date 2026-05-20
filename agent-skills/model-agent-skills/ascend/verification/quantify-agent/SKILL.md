______________________________________________________________________

## name: ascend description: Entry point for Ascend NPU inference toolchain. Use when running vLLM on Ascend/NPU, quantizing models with msmodelslim, or debugging NPU errors. argument-hint: "vllm issue / quantization / npu usage"

# Ascend Inference Toolchain

This skill manages Ascend NPU-related tasks, troubleshooting, and toolchain usage.

## Hardware Check

Run at the start of every session before any quantization or inference task:

```bash
npu-smi info
```

Verify:

- All expected NPUs appear and show **Health: OK**
- No NPU is occupied by another process (check "Process ID" column)
- If an NPU is stuck, identify the PID and confirm with the user before killing it

## Common Environment Setup

Set these before running either vLLM or msmodelslim:

```bash
# Required for vLLM multi-process NPU support
export VLLM_WORKER_MULTIPROC_METHOD=spawn

# Use ModelScope for downloads (recommended in China)
export VLLM_USE_MODELSCOPE=true

# Isolate specific NPUs (adjust indices to match available devices)
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
```

`ASCEND_RT_VISIBLE_DEVICES` controls which NPUs are visible to **both** vLLM and msmodelslim. Set this before any command that touches NPUs.

## Task Specifics

For detailed instructions on specific tools, refer to:

- **vLLM-Ascend**: See [vllm-install.md](vllm-install.md) for installation and [vllm-run.md](vllm-run.md) for running and troubleshooting.
- **msmodelslim**: See [msmodelslim.md](msmodelslim.md) for quantization protocols (includes end-to-end iterative workflow).
- **Sensitivity Analysis**: See [sensitivity-analysis.md](sensitivity-analysis.md) for diagnosing and fixing quantization accuracy drops via layer sensitivity analysis.
- **AISBench Evaluation**: See [ais_bench.md](ais_bench.md) for GSM8K accuracy and performance benchmarking against a running vLLM service.

## Core Tips

- **Source Debugging**: Use `pip show <package>` to find the editable source location for deep debugging.
