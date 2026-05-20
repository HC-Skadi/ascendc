# Issue #2949: [Bug]: pangu+torchair is broken

## 基本信息

- **编号**: #2949
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2949
- **创建时间**: 2025-09-16T03:05:10Z
- **关闭时间**: 2026-01-22T11:44:16Z
- **更新时间**: 2026-01-22T11:44:16Z
- **提交者**: @wangxiyuan
- **评论数**: 0

## 标签

bug

## 问题描述

error log:
```
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654] WorkerProc hit an exception.
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 264, in compile_or_warm_up_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self.model_runner.capture_model()
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2943, in capture_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._capture_model()
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 229, in _capture_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._compile_torchair_graph(torchair_graph_batch_sizes)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 190, in _compile_torchair_graph
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._dummy_run(num_tokens, is_torchair_compile=True)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2234, in _dummy_run
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 154, in _generate_dummy_run_hidden_states
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     assert isinstance(kv, tuple), "kv_cache must be a tuple"
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654] AssertionError: kv_cache must be a tuple
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 264, in compile_or_warm_up_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self.model_runner.capture_model()
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2943, in capture_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._capture_model()
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 229, in _capture_model
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._compile_torchair_graph(torchair_graph_batch_sizes)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 190, in _compile_torchair_graph
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     self._dummy_run(num_tokens, is_torchair_compile=True)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2234, in _dummy_run
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 154, in _generate_dummy_run_hidden_states
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]     assert isinstance(kv, tuple), "kv_cache must be a tuple"
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=54270) ERROR 09-16 02:55:14 [multiproc_executor.py:654] AssertionError: kv_cache must be a tuple
```
