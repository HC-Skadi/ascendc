# Issue #3357: [Bug]: 0.11.0rc0 qwen3-235B OOM

## 基本信息

- **编号**: #3357
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3357
- **创建时间**: 2025-10-10T03:46:46Z
- **关闭时间**: 2025-12-15T13:23:24Z
- **更新时间**: 2025-12-15T13:23:25Z
- **提交者**: @glowwormX
- **评论数**: 5

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

vllm                              0.11.0rc3+empty
vllm-ascend                       0.11.0rc0
torch                             2.7.1+cpu
torch_npu                         2.7.1.dev20250919
'CANN:8.2.RC1'

### 🐛 Describe the bug

```
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_FLASHCOMM=1
export VLLM_ASCEND_ENABLE_TOPK_OPTIMIZE=1
# export VLLM_ASCEND_ENABLE_MATMUL_ALLREDUCE=1
export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
export CPU_AFFINITY_CONF=1

model_name=Qwen3-235B-A22B-Thinking-2507
nohup vllm serve Qwen3/$model_name  \
--host 0.0.0.0 \
--port 8004 \
--tensor-parallel-size 16 \
--seed 1024 \
--served-model-name  $model_name \
--max-num-seqs 16 \
--max-model-len 98304 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.95 \
--disable-log-requests \
2>&1 | tee service.log &
```
执行一个90k的prompt，报OOM：
```
[1;36m(APIServer pid=728)[0;0m INFO 10-10 11:30:57 [loggers.py:127] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 15; 60.97 GiB total capacity; 55.29 GiB already allocated; 55.29 GiB current active; 4.64 GiB free; 55.46 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 15; 60.97 GiB total capacity; 55.29 GiB already allocated; 55.29 GiB current active; 4.64 GiB free; 55.46 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP15 pid=1177)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] 
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 9; 60.97 GiB total capacity; 55.28 GiB already allocated; 55.28 GiB current active; 4.65 GiB free; 55.44 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 9; 60.97 GiB total capacity; 55.28 GiB already allocated; 55.28 GiB current active; 4.65 GiB free; 55.44 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP9 pid=1171)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] 
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 5; 60.97 GiB total capacity; 55.28 GiB already allocated; 55.28 GiB current active; 4.65 GiB free; 55.44 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 5; 60.97 GiB total capacity; 55.28 GiB already allocated; 55.28 GiB current active; 4.65 GiB free; 55.44 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP5 pid=1167)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] 

...
 
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 0; 60.97 GiB total capacity; 54.10 GiB already allocated; 54.10 GiB current active; 4.64 GiB free; 54.27 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     output = self.model_runner.execute_model(scheduler_output,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1932, in execute_model
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     max_query_len) = (self._prepare_inputs(scheduler_output,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1381, in _prepare_inputs
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     self.attn_mask = self._make_attention_mask(seq_lens=seq_lens_cpu,
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/worker/model_runner_v1.py", line 898, in _make_attention_mask
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return self.attn_mask_builder.get_splitfuse_attn_mask(
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]   File "/cache/lib/python3.11/site-packages/vllm_ascend/attention/attention_mask.py", line 101, in get_splitfuse_attn_mask
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]     return attn_mask.contiguous().to(device, non_blocking=True)
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] RuntimeError: NPU out of memory. Tried to allocate 11.50 GiB (NPU 0; 60.97 GiB total capacity; 54.10 GiB already allocated; 54.10 GiB current active; 4.64 GiB free; 54.27 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
[1;36m(Worker_TP0 pid=1162)[0;0m ERROR 10-10 11:32:51 [multiproc_executor.py:671] 
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0rc3) with config: model='/opt/huawei/dataset/openLLM_guian_obs/Qwen3/Qwen3-235B-A22B-Thinking-2507', speculative_config=None, tokenizer='/opt/huawei/dataset/openLLM_guian_obs/Qwen3/Qwen3-235B-A22B-Thinking-2507', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=98304, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=Qwen3-235B-A22B-Thinking-2507, enable_prefix_caching=False, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified_ascend_attention_with_output","vllm.mla_forward","vllm.unified_ascend_attention_with_output","vllm.mla_forward"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":32,"local_cache_dir":null}, 
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=cmpl-173d0918ce964319b0d52f4d621dc548-0,prompt_token_ids_len=78567,mm_features=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None),block_ids=([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={cmpl-173d0918ce964319b0d52f4d621dc548-0: 78567}, total_num_scheduled_tokens=78567, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.1332465277777778, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0), spec_decoding_stats=None, kv_connector_stats=None, num_corrupted_reqs=0)
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710] EngineCore encountered a fatal error.
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710] Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 701, in run_engine_core
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     engine_core.run_busy_loop()
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 728, in run_busy_loop
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     self._process_engine_step()
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 754, in _process_engine_step
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     outputs, model_executed = self.step_fn()
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]                               ^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 284, in step
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     model_output = self.execute_model_with_error_logging(
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     raise err
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     return model_fn(scheduler_output)
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 181, in execute_model
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     (output, ) = self.collective_rpc(
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]                  ^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     result = get_response(w, dequeue_timeout,
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]   File "/cache/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710]     raise RuntimeError(
[1;36m(EngineCore_DP0 pid=1020)[0;0m ERROR 10-10 11:32:51 [core.py:710] RuntimeError: Worker failed with error 'NPU out of memory. Tried to allocate 11.50 GiB (NPU 0; 60.97 GiB total capacity; 54.10 GiB already allocated; 54.10 GiB current active; 4.64 GiB free; 54.27 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.', please check the stack trace above for the root cause
[1;36m(Worker_TP0 pid=1162)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP1 pid=1163)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP1 pid=1163)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP2 pid=1164)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP2 pid=1164)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP3 pid=1165)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480] AsyncLLM output_handler failed.
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480] Traceback (most recent call last):
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 439, in output_handler
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480]     outputs = await engine_core.get_output_async()
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480]   File "/cache/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 846, in get_output_async
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480]     raise self._format_exception(outputs) from None
[1;36m(APIServer pid=728)[0;0m ERROR 10-10 11:32:51 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
[1;36m(Worker_TP3 pid=1165)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP4 pid=1166)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP5 pid=1167)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(APIServer pid=728)[0;0m INFO:     6.51.239.79:40348 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error
[1;36m(Worker_TP5 pid=1167)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP6 pid=1168)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP6 pid=1168)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP7 pid=1169)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP8 pid=1170)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP9 pid=1171)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP10 pid=1172)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP9 pid=1171)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP11 pid=1173)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP12 pid=1174)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP13 pid=1175)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP14 pid=1176)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(Worker_TP8 pid=1170)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:599] WorkerProc shutting down.
[1;36m(Worker_TP15 pid=1177)[0;0m INFO 10-10 11:32:51 [multiproc_executor.py:558] Parent process exited, terminating worker
[1;36m(APIServer pid=728)[0;0m INFO:     Shutting down
[1;36m(APIServer pid=728)[0;0m INFO:     Waiting for application shutdown.
[1;36m(APIServer pid=728)[0;0m INFO:     Application shutdown complete.
[1;36m(APIServer pid=728)[0;0m INFO:     Finished server process [728]
/cache/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

换成0.9.1，不会报错，但是速度慢
