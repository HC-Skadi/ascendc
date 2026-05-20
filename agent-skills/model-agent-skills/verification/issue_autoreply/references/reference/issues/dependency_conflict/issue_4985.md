# Issue #4985: [Bug]: server crashes when running FULL_DECODE_ONLY mode with Qwen3-235B && DeepSeek V3.1

## 基本信息

- **编号**: #4985
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4985
- **创建时间**: 2025-12-13T10:23:46Z
- **关闭时间**: 2026-02-09T07:34:27Z
- **更新时间**: 2026-02-09T07:34:27Z
- **提交者**: @Angazenn
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
vLLM: 0.12.0+empty

vLLM-Ascend: main(commit 4721e4f53ff416e082b52791676aa80fa21c9e29) 
</details>

### 🐛 Describe the bug

When we run Qwen3-235B or DeepSeek V3.1 with `FULL_DECODE_ONLY` mode and multi-dp on latest main, the server carshes if we send multiple requests. Example scripts:
```
vllm serve /path/to/Qwen3-235B-A22B-W8A8/ \
        --served-model-name "qwen" \
        --host 0.0.0.0 \
        --port 8000 \
        --async-scheduling \
        --tensor-parallel-size 4 \
        --data-parallel-size 4 \
        --max-num-seqs 64 \
        --max-model-len 6000 \
        --max-num-batched-tokens 8192 \
        --gpu-memory-utilization 0.9 \
        --enable-expert-parallel \
        --quantization "ascend" \
        --trust-remote-code \
        --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
```
Error info:
```
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 369, in execute_model
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 293, in execute_model
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     output = self.model_runner.execute_model(scheduler_output,
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2463, in execute_model
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1910, in _prepare_inputs
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822]     self.query_start_loc[num_reqs + 1:num_reqs_padded +
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822] RuntimeError: The expanded size of the tensor (11) must match the existing size (879) at non-singleton dimension 0.  Target sizes: [11].  Tensor sizes: [879]
(Worker_DP1_TP2_EP6 pid=2768) ERROR 12-12 08:14:50 [multiproc_executor.py:822] 
```
