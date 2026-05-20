# Issue #4313: [Bug]: KeyError: 'visual.blocks.0.attn.qkv.weight' when Loading FP8 Quantized Qwen2.5-VL Model

## 基本信息

- **编号**: #4313
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4313
- **创建时间**: 2025-11-20T09:27:29Z
- **关闭时间**: 2025-12-30T07:06:32Z
- **更新时间**: 2025-12-30T07:06:32Z
- **提交者**: @spencerr221
- **评论数**: 5

## 标签

bug

## 问题描述

### Current environment
vllm-ascend version 0.11.0rc1
Ascend NPU 910B aarch64
Python version: 3.11.13
Model: allenai/olmOCR-2-7B-1025-FP8
### Summary
I am encountering a KeyError during model initialization when trying to load an FP8 quantized vision-language model, specifically allenai/olmOCR-2-7B-1025-FP8, which is based on the Qwen2.5-VL architecture.

The error originates from the vllm-ascend quantization configuration module (quant_config.py), indicating that the quantization description map is missing an entry for a weight in the model's vision transformer (visual.blocks.0.attn.qkv.weight). This suggests the quantization configuration is incomplete for the visual components of this model. 

### Steps to Reproduce
```python
# reproduce_bug.py
from vllm import LLM, SamplingParams

# The model that causes the error
MODEL_PATH = "allenai/olmOCR-2-7B-1025-FP8"

try:
    print(f"Loading model: {MODEL_PATH}")
    
    # Initialize the LLM object
    # The error occurs during this initialization step
    llm = LLM(
        model=MODEL_PATH,
        enforce_eager=False,
        max_model_len=8192,
        trust_remote_code=True, 
        tensor_parallel_size=1,
    )
    
    print("Model loaded successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
```

### 🐛 Describe the bug

```python
(EngineCore_DP0 pid=5654) /vllm-workspace/vllm/vllm/executor/uniproc_executor.py:60: ResourceWarning: unclosed <socket.socket fd=25, family=2, type=2, proto=0, laddr=('10.50.93.216', 60069), raddr=('8.8.8.8', 80)>
(EngineCore_DP0 pid=5654)   get_ip(), get_open_port())
(EngineCore_DP0 pid=5654) INFO 11-20 08:26:48 [parallel_state.py:1208] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_DP0 pid=5654) INFO 11-20 08:26:49 [model_runner_v1.py:2642] Starting to load model olmocr/...
(EngineCore_DP0 pid=5654) /usr/local/python3.11.13/lib/python3.11/contextlib.py:191: ResourceWarning: Unclosed context <zmq.Context() at 0xfffcdea6c290>
(EngineCore_DP0 pid=5654)   exc.__traceback__ = traceback
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 55, in _init_executor
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.collective_rpc("load_model")
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3122, in run_method
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     return func(*args, **kwargs)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 313, in load_model
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.model_runner.load_model()
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2645, in load_model
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     model = initialize_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     return model_class(vllm_config=vllm_config, prefix=prefix)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen2_5_vl.py", line 521, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     super().__init__(vllm_config=vllm_config, prefix=prefix)
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1013, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.visual = Qwen2_5_VisionTransformer(
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 636, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.blocks = nn.ModuleList([
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                                 ^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 637, in <listcomp>
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     Qwen2_5_VisionBlock(
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 439, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.attn = Qwen2_5_VisionAttention(
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                 ^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 290, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.qkv = QKVParallelLinear(
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                ^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 142, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     AscendColumnParallelLinear.__init__(self,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 342, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     AscendLinearBase.__init__(self,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 84, in __init__
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     self.quant_method = quant_config.get_quant_method(self,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 110, in get_quant_method
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     if self.is_layer_skipped_ascend(prefix,
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 161, in is_layer_skipped_ascend
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708]                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=5654) ERROR 11-20 08:26:50 [core.py:708] KeyError: 'visual.blocks.0.attn.qkv.weight'
```
