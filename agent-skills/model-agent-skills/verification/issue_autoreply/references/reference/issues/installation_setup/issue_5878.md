# Issue #5878: move _process_image_input to modelrunner process for Qwen3-VL

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
  |TTFT | TPOT | TPS |
|-- | -- | -- | -- | --
|base | 5.50s | 94.73 | 0.4868 |
|test | 4.65s | 94.36| 0.3036 |

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
export HCCL_BUFFSIZE=512
export VLLM_USE_V1=1
export VLLM_TORCH_PROFILER_WITH_STACK=1
export VLLM_TORCH_PROFILER_DIR=/home/l00882526/profiling
export VLLM_ASCEND_ENABLE_FUSED_MC2=1
export use_cache=true
LOGFILE=/workspace/log/qwen3.log

vllm serve /data/model/Qwen3-VL-235B-A22B-Instruct-W8A8/
--host 0.0.0.0
--port 8090
--data-parallel-size 4
--tensor-parallel-size 4
--seed 1024
--served-model-name qwen_235
--enable-expert-parallel
--max-model-len 20480
--max-num-batched-tokens 8192
--trust-remote-code
--quantization ascend
--no-enable-prefix-caching
--gpu-memory-utilization 0.7
--additional-config '{"enable_cpu_binding":true}'
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,16,

## 基本信息
- **编号**: #5878
- **作者**: leonlou33333
- **创建时间**: 2026-01-14T03:09:52Z
- **关闭时间**: 2026-01-14T03:31:04Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5878)
