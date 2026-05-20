# Issue #4678: [Bug]: Qwen3-VL-32B跑一半会报500错误

## 基本信息

- **编号**: #4678
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4678
- **创建时间**: 2025-12-03T12:34:52Z
- **关闭时间**: 2025-12-30T01:51:24Z
- **更新时间**: 2025-12-30T01:51:24Z
- **提交者**: @ZhihuaH
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

目前的环境是910B，vllm-ascend是0.11.0最新版。

### 🐛 Describe the bug

使用vllm serve model-path --tensor-parallel-size 2进行模型部署。

前面60个例子可以正常推理，后面就会500错误。

(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] EngineCore encountered a fatal error.                                                          
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] Traceback (most recent call last):                                                             
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 701, in run_engine_core             
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     engine_core.run_busy_loop()                                                                
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 728, in run_busy_loop               
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     self._process_engine_step()                                                                
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 754, in _process_engine_step        
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     outputs, model_executed = self.step_fn()                                                   
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]                               ^^^^^^^^^^^^^^                                                   
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 284, in step                        
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     model_output = self.execute_model_with_error_logging(                                      
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                      
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 270, in execute_model_with_error_log
ging                                                                                                                                                         
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     raise err
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 261, in execute_model_with_error_log
ging
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     return model_fn(scheduler_output)
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 181, in execute_mode
l
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     (output, ) = self.collective_rpc(
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]                  ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_r
pc
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]     raise RuntimeError(
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits
 for this inner error, and the current working operator name is SelfAttentionOperation.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to g
et the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performa
nce degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] [ERROR] 2025-12-03-12:16:41 (PID:10652, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] [PID: 10652] 2025-12-03-12:16:41.842.173 Memory_Allocation_Failure(EL0004): Failed to allocate 
memory.

(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]         Possible Cause: Available memory is insufficient.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]         Solution: Close applications not in use.
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]         TraceBack (most recent call last):
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inne
r.cpp][LINE:162]
(EngineCore_DP0 pid=10516) ERROR 12-03 12:16:41 [core.py:710] ', please check the stack trace above for the root cause
(Worker_TP0 pid=10652) INFO 12-03 12:16:41 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_TP0 pid=10652) INFO 12-03 12:16:41 [multiproc_executor.py:599] WorkerProc shutting down.
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480] AsyncLLM output_handler failed.
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480] Traceback (most recent call last):
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 439, in output_handler
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480]     outputs = await engine_core.get_output_async()
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 846, in get_output_async
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480]     raise self._format_exception(outputs) from None
(APIServer pid=10248) ERROR 12-03 12:16:41 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (ab
ove) for the root cause.
(Worker_TP1 pid=10653) INFO 12-03 12:16:41 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_TP1 pid=10653) INFO 12-03 12:16:41 [multiproc_executor.py:599] WorkerProc shutting down.
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     172.17.0.1:36746 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=10248) INFO:     Shutting down
(APIServer pid=10248) INFO:     Waiting for application shutdown.
(APIServer pid=10248) INFO:     Application shutdown complete.
(APIServer pid=10248) INFO:     Finished server process [10248]
