# Issue #2887: [Bug]: DeepSeek-V2-Lite-Chat failed with CANN 8.3.rc1.alpha002

## 基本信息

- **编号**: #2887
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2887
- **创建时间**: 2025-09-12T08:09:56Z
- **关闭时间**: 2025-09-12T12:51:14Z
- **更新时间**: 2025-09-12T12:51:14Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17668018582/job/50213328364?pr=2880

### 🐛 Describe the bug

```
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585] Traceback (most recent call last):
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 559, in worker_main
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     worker = WorkerProc(*args, **kwargs)
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 427, in __init__
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     self.worker.load_model()
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 249, in load_model
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     self.model_runner.load_model()
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2195, in load_model
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     self.model = get_model(vllm_config=self.vllm_config)
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     return loader.load_model(vllm_config=vllm_config,
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 51, in load_model
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     process_weights_after_loading(model, model_config, target_device)
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/utils.py", line 123, in process_weights_after_loading
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     module.process_weights_after_loading(model_config.dtype)
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/attention/layer.py", line 316, in process_weights_after_loading
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     self.impl.process_weights_after_loading(act_dtype)
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/attention/mla_v1.py", line 547, in process_weights_after_loading
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]     assert kv_b_proj_weight.shape == (
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=7523) ERROR 09-12 07:57:46 [multiproc_executor.py:585] AssertionError: kv_b_proj_weight.shape=torch.Size([2048, 512]), self.kv_lora_rank=512, self.num_heads=8, self.qk_nope_head_dim=128, self.v_head_dim=128
```
