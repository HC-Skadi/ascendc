# Issue #4874: [Bug]: 使用v0.11.0rc2-310p-openeuler 执行qwen 2.5 报错

## 基本信息

- **编号**: #4874
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4874
- **创建时间**: 2025-12-10T07:04:32Z
- **关闭时间**: 2025-12-15T02:54:12Z
- **更新时间**: 2025-12-15T02:54:12Z
- **提交者**: @xucqX
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

cmd = [
        "python", "-m", "vllm.entrypoints.openai.api_server",
        "--model", after_model_path,
        "--tensor-parallel-size", 2,
        "--gpu-memory-utilization", 0.7,
        "--max-model-len", "1536",
        "--trust-remote-code",
        "--dtype",  'float16',
        "--host", '127.0.0.1',
        "--port", 7070,
        "--served-model-name", "xxx"
    ]
    logger.info(cmd)
    subprocess.Popen(cmd)

### 🐛 Describe the bug

使用v0.11.0rc2-310p-openeuler 执行qwen 2.5 报错


```报错信息
(Worker_TP1 pid=1226) INFO 12-10 06:37:53 [default_loader.py:267] Loading weights took 11.60 seconds
(Worker_TP0 pid=1225) INFO 12-10 06:37:53 [default_loader.py:267] Loading weights took 11.61 seconds
(Worker_TP0 pid=1225) INFO 12-10 06:37:54 [model_runner_v1.py:2667] Loading model weights took 7.5124 GB
(Worker_TP1 pid=1226) INFO 12-10 06:37:54 [model_runner_v1.py:2667] Loading model weights took 7.5124 GB
(Worker_TP1 pid=1226) WARNING 12-10 06:38:03 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(Worker_TP0 pid=1225) WARNING 12-10 06:38:03 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] WorkerProc hit an exception.
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] Traceback (most recent call last):
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     output = func(*args, **kwargs)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 227, in determine_available_memory
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     self.model_runner.profile_run()
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in profile_run
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     hidden_states = self._dummy_run(self.max_num_tokens,
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     return func(*args, **kwargs)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2493, in _dummy_run
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2314, in _generate_dummy_run_hidden_states
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 597, in forward
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     model_output = self.model(input_ids, positions, intermediate_tensors,
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 310, in __call__
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     output = self.compiled_callable(*args, **kwargs)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 659, in _fn
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     raise e.with_traceback(None) from None
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] torch._dynamo.exc.Unsupported: Observed exception
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   Explanation: Dynamo found no exception handler at the top-level compiled function when encountering an exception. Exception will propagate outside the compiled region.
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   Hint: Dynamo has detected that tracing the code will result in an error when running in eager. Please double check that your code doesn't contain a similar error when actually running eager/uncompiled.
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   Hint: It may be possible to write Dynamo tracing rules for this code. Please report an issue to PyTorch if you encounter this graph break often and it is causing performance issues.
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] 
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]   Developer debug context: 
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] 
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] 
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] from user code:
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]    File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 405, in forward
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671]     hidden_states, residual = layer(positions, hidden_states, residual)
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] 
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"
(Worker_TP1 pid=1226) ERROR 12-10 06:38:04 [multiproc_executor.py:671] 
```
