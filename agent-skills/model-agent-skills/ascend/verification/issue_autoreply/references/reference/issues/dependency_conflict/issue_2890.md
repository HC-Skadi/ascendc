# Issue #2890: [Bug]: DeepSeek-w4a8dynamic failed

## 基本信息

- **编号**: #2890
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2890
- **创建时间**: 2025-09-12T09:24:51Z
- **关闭时间**: 2025-09-12T12:51:14Z
- **更新时间**: 2025-09-12T12:51:14Z
- **提交者**: @Pr0Wh1teGivee
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

vllm: d21a36f5f9569949dd6c313deed609d77e393850
vllm-ascend: fc2bcbe21c86f7684c80e42771b128da9fc17571
npu: a3
cann: 8.3.RC1 B020

This issue is introduced by: 
https://github.com/vllm-project/vllm-ascend/commit/7b2ecc1e9a64aeda78e2137aa06abdbf2890c000

### 🐛 Describe the bug

scirpt:
```python
from vllm import LLM, SamplingParams
import os

tp_size = 2
etp_size = 1
n_samples = 2

os.environ["VLLM_ASCEND_MLA_PA"] = "1"
llm = LLM(
    model="/data/zwc/weights/vllm-ascend/DeepSeek-V3-W4A8-Pruing/",
    trust_remote_code=True,
    tensor_parallel_size=4,
    dtype="auto",
    distributed_executor_backend="mp",
    max_model_len=8192,
    max_num_seqs=1,
    enforce_eager=True,
    enable_expert_parallel=True,
    gpu_memory_utilization=0.95,
    quantization="ascend",
    additional_config={
        "torchair_graph_config": {
            "enabled": False,
        },
        "ascend_scheduler_config": {
            "enabled": True,
        }
    }
)

sampling_params = SamplingParams(
        temperature=0.7,
        top_p=0.9,
        max_tokens=128,
        n=n_samples
    )

prompts = "Doug constructs a square window using $8$ equal-size panes of glass. The ratio of the height to width for each pane is $5 : 2$, and the borders around and between the panes are $2$ inches wide. In inches, what is the side length of the square window?\nPlease reason step by step, and put your final answer within \\boxed{}."


outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(f"Prompt: {output.prompt}")
    print(f"Generated text: {output.outputs[0].text}\n")


```
error:
```
(EngineCore_DP0 pid=701301) (Worker_TP0_EP0 pid=701308)   packed_weight = torch.from_numpy(
(EngineCore_DP0 pid=701301) (Worker_TP2_EP2 pid=701316) /data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/quantization/w4a8_dynamic.py:361: UserWarning: The given NumPy array is not writhis tensor will result in undefined behavior. You may want to copy the array to protect its data or make it writable before converting it to a tensor. This type of warning will be suppressed for thr_numpy.cpp:203.)
(EngineCore_DP0 pid=701301) (Worker_TP2_EP2 pid=701316)   packed_weight = torch.from_numpy(
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585] WorkerProc failed to start.
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585] Traceback (most recent call last):
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py",
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     worker = WorkerProc(*args, **kwargs)
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py",
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.worker.load_model()
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/worker/worker_v1.py",
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.model_runner.load_model()
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/worker/model_runner_v1
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/__init__
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/base_loa
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     process_weights_after_loading(model, model_config, target_device)
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/utils.py
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     module.process_weights_after_loading(model_config.dtype)
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/attention/layer.py", line 316, in pr
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.impl.process_weights_after_loading(act_dtype)
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/attention/mla_v1.py",
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     assert kv_b_proj_weight.shape == (
(EngineCore_DP0 pid=701301) (Worker_TP1_EP1 pid=701311) ERROR 09-12 17:00:45 [multiproc_executor.py:585] AssertionError: kv_b_proj_weight.shape=torch.Size([8192, 512]), self.kv_lora_rank=512, self.n
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585] WorkerProc failed to start.
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585] Traceback (most recent call last):
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py",
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     worker = WorkerProc(*args, **kwargs)
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py",
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.worker.load_model()
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/worker/worker_v1.py",
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.model_runner.load_model()
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/worker/model_runner_v1
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/__init__
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/base_loa
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     process_weights_after_loading(model, model_config, target_device)
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/model_executor/model_loader/utils.py
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     module.process_weights_after_loading(model_config.dtype)
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/attention/layer.py", line 316, in pr
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     self.impl.process_weights_after_loading(act_dtype)
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]   File "/data/zwc/vllm_refactor_main/original2/vllm-ascend/vllm_ascend/attention/mla_v1.py",
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585]     assert kv_b_proj_weight.shape == (
(EngineCore_DP0 pid=701301) (Worker_TP3_EP3 pid=701321) ERROR 09-12 17:00:45 [multiproc_executor.py:585] AssertionError: kv_b_proj_weight.shape=torch.Size([8192, 512]), self.kv_lora_rank=512, self.n
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718] EngineCore failed to start.
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718] Traceback (most recent call last):
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     self._init_executor()
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py", line 99, in _init_executor
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]   File "/data/zwc/vllm_refactor_main/original2/vllm/vllm/v1/executor/multiproc_executor.py", line 497, in wait_for_ready
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718]     raise e from None
(EngineCore_DP0 pid=701301) ERROR 09-12 17:00:46 [core.py:718] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP0 pid=701301) Process EngineCore_DP0:
```
