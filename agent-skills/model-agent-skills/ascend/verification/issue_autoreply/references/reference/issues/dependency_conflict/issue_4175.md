# Issue #4175: [Bug]: 部署Qwen3-Next-80B-A3B-Instruct成功，但是发送带有参数response_format的请求时服务会崩溃

## 基本信息

- **编号**: #4175
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4175
- **创建时间**: 2025-11-13T10:02:45Z
- **关闭时间**: 2026-01-26T08:58:29Z
- **更新时间**: 2026-01-26T08:58:29Z
- **提交者**: @zxh0315
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
800I A2 64G npu型号：910B4-1
</details>


### 🐛 Describe the bug

发送的请求及响应：curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "qwen3",
  "messages": [
    {"role": "user", "content": "Who are you?"}
  ],
  "temperature": 0.6,
  "top_p": 0.95,
  "top_k": 20,
  "max_tokens": 32,
  "response_format": {
    "type": "text"
  }
}'
{"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"Internal Server Error","param":null,"code":500}}

服务的命令：
vllm serve /model/weights/Qwen3-Next-80B-A3B-Instruct/ --tensor-parallel-size 4 --max-model-len 4096 --gpu-memory-utilization 0.7 --enforce-eager --served-model-name qwen3

服务器日志：
```
(APIServer pid=7225) INFO:     Started server process [7225]
(APIServer pid=7225) INFO:     Waiting for application startup.
(APIServer pid=7225) INFO:     Application startup complete.
(APIServer pid=7225) INFO 11-13 09:22:26 [chat_utils.py:560] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710] Traceback (most recent call last):
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 701, in run_engine_core
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 728, in run_busy_loop
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     self._process_engine_step()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 754, in _process_engine_step
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 283, in step
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     scheduler_output = self.scheduler.schedule()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]                        ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/core/sched/scheduler.py", line 359, in schedule
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     if structured_output_req and structured_output_req.grammar:
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/structured_output/request.py", line 45, in grammar
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     completed = self._check_grammar_completion()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/structured_output/request.py", line 33, in _check_grammar_completion
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     self._grammar = self._grammar.result(timeout=0.0001)
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     return self.__get_result()
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     raise self._exception
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/thread.py", line 58, in run
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     result = self.fn(*self.args, **self.kwargs)
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/structured_output/__init__.py", line 128, in _async_create_grammar
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     key = request.structured_output_request.structured_output_key  # type: ignore[union-attr]
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/usr/local/python3.11.13/lib/python3.11/functools.py", line 1001, in __get__
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     val = self.func(instance)
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]           ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/structured_output/request.py", line 58, in structured_output_key
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     return get_structured_output_key(self.sampling_params)
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/structured_output/request.py", line 86, in get_structured_output_key
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710]     raise ValueError("No valid structured output parameter found")
(EngineCore_DP0 pid=7497) ERROR 11-13 09:22:27 [core.py:710] ValueError: No valid structured output parameter found
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480] AsyncLLM output_handler failed.
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480] Traceback (most recent call last):
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 439, in output_handler
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480]     outputs = await engine_core.get_output_async()
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 846, in get_output_async
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480]     raise self._format_exception(outputs) from None
(APIServer pid=7225) ERROR 11-13 09:22:27 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(APIServer pid=7225) INFO:     127.0.0.1:51906 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(Worker_TP0 pid=7633) INFO 11-13 09:22:27 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_TP0 pid=7633) INFO 11-13 09:22:27 [multiproc_executor.py:599] WorkerProc shutting down.
(Worker_TP1 pid=7634) INFO 11-13 09:22:27 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_TP2 pid=7635) INFO 11-13 09:22:27 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_TP1 pid=7634) INFO 11-13 09:22:27 [multiproc_executor.py:599] WorkerProc shutting down.
(Worker_TP2 pid=7635) INFO 11-13 09:22:27 [multiproc_executor.py:599] WorkerProc shutting down.
(Worker_TP3 pid=7636) INFO 11-13 09:22:27 [multiproc_executor.py:558] Parent process exited, terminating worker
(APIServer pid=7225) INFO:     Shutting down
(APIServer pid=7225) INFO:     Waiting for application shutdown.
(APIServer pid=7225) INFO:     Application shutdown complete.
(APIServer pid=7225) INFO:     Finished server process [7225]
root@localhost:/workspace# /usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
