# Issue #200: [Bug]: TypeError: AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given

## 基本信息

- **编号**: #200
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/200
- **创建时间**: 2025-02-28T03:28:35Z
- **关闭时间**: 2025-02-28T07:45:59Z
- **更新时间**: 2025-03-03T12:13:34Z
- **提交者**: @caolicaoli
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment
用的是镜像
docker pull quay.io/ascend/vllm-ascend:v0.7.1rc1

运行embeding模型时候都汇报这个错，qwen的mistral的，还有其他多种，全部报这个错

e5-mistral-7b-instruct
gte-Qwen2-1.5B-instruct
等等

```
TypeError: AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given


ARNING 02-28 03:24:01 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:01 __init__.py:174] Platform plugin ascend is activated
INFO 02-28 03:24:02 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=480) INFO 02-28 03:24:02 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-28 03:24:14 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:14 __init__.py:174] Platform plugin ascend is activated
INFO 02-28 03:24:15 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:15 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:15 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:15 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:15 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:15 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-28 03:24:15 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:15 __init__.py:174] Platform plugin ascend is activated
[rank0]:[W228 03:24:19.786171073 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank1]:[W228 03:24:19.792338061 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
INFO 02-28 03:24:19 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_76ce9c25'), local_subscribe_port=40075, remote_subscribe_port=None)
INFO 02-28 03:24:19 model_runner.py:1111] Starting to load model /data/part2/e5-mistral-7b-instruct...
(VllmWorkerProcess pid=480) INFO 02-28 03:24:19 model_runner.py:1111] Starting to load model /data/part2/e5-mistral-7b-instruct...
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:02<00:02,  2.56s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00,  1.89s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00,  1.99s/it]

(VllmWorkerProcess pid=480) INFO 02-28 03:24:23 model_runner.py:1116] Loading model weights took 6.6315 GB
INFO 02-28 03:24:24 model_runner.py:1116] Loading model weights took 6.6315 GB
INFO 02-28 03:24:24 api_server.py:754] Using supplied chat template:
INFO 02-28 03:24:24 api_server.py:754] None
INFO 02-28 03:24:24 launcher.py:19] Available routes are:
INFO 02-28 03:24:24 launcher.py:27] Route: /openapi.json, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /docs, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /redoc, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /health, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /ping, Methods: GET, POST
INFO 02-28 03:24:24 launcher.py:27] Route: /tokenize, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /detokenize, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/models, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /version, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /pooling, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /score, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/score, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v2/rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /invocations, Methods: POST
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9093 (Press CTRL+C to quit)
INFO 02-28 03:25:56 logger.py:37] Received request embd-cbf64ff4c5c64e66b2c4bb0db30e22d7-0: prompt: '你的文本内容', params: PoolingParams(additional_metadata=None), prompt_token_ids: [1, 28705, 29383, 28914, 29019, 29119, 29188, 29329, 2], lora_request: None, prompt_adapter_request: None.
INFO 02-28 03:25:56 engine.py:273] Added request embd-cbf64ff4c5c64e66b2c4bb0db30e22d7-0.
CRITICAL 02-28 03:25:56 launcher.py:99] MQLLMEngine is already dead, terminating server process
INFO:     180.168.189.253:18475 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error
ERROR 02-28 03:25:56 engine.py:137] TypeError('AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given')
ERROR 02-28 03:25:56 engine.py:137] Traceback (most recent call last):
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 135, in start
ERROR 02-28 03:25:56 engine.py:137]     self.run_engine_loop()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 198, in run_engine_loop
ERROR 02-28 03:25:56 engine.py:137]     request_outputs = self.engine_step()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 216, in engine_step
ERROR 02-28 03:25:56 engine.py:137]     raise e
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 207, in engine_step
ERROR 02-28 03:25:56 engine.py:137]     return self.engine.step()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1384, in step
ERROR 02-28 03:25:56 engine.py:137]     outputs = self.model_executor.execute_model(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 273, in execute_model
ERROR 02-28 03:25:56 engine.py:137]     driver_outputs = self._driver_execute_model(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 142, in _driver_execute_model
ERROR 02-28 03:25:56 engine.py:137]     return self.driver_worker.execute_model(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 387, in execute_model
ERROR 02-28 03:25:56 engine.py:137]     inputs = self.prepare_input(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 372, in prepare_input
ERROR 02-28 03:25:56 engine.py:137]     return self._get_driver_input_and_broadcast(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 334, in _get_driver_input_and_broadcast
ERROR 02-28 03:25:56 engine.py:137]     self.model_runner.prepare_model_input(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/pooling_model_runner.py", line 169, in prepare_model_input
ERROR 02-28 03:25:56 engine.py:137]     model_input = self._prepare_model_input_tensors(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1221, in _prepare_model_input_tensors
ERROR 02-28 03:25:56 engine.py:137]     return self.builder.build()  # type: ignore
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 926, in build
ERROR 02-28 03:25:56 engine.py:137]     attn_metadata = self.attn_metadata_builder.build(
ERROR 02-28 03:25:56 engine.py:137] TypeError: AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 317, in _bootstrap
    util._exit_function()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 334, in _exit_function
    _run_finalizers(0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 300, in _run_finalizers
    finalizer()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 54, in wrapper
    return func(cls, *args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 219, in finalize
    cls.global_mgr.finalize()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 84, in finalize
    self.mgr.shutdown()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 674, in _finalize_manager
    process.join(timeout=1.0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 149, in join
    res = self._popen.wait(timeout)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/popen_fork.py", line 40, in wait
    if not wait([self.sentinel], timeout):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 931, in wait
    ready = selector.select(timeout)
  File "/usr/local/python3.10/lib/python3.10/selectors.py", line 416, in select
    fd_event_list = self._selector.poll(timeout)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 372, in signal_handler
    raise KeyboardInterrupt("MQLLMEngine terminated")
KeyboardInterrupt: MQLLMEngine terminated
INFO 02-28 03:25:57 multiproc_worker_utils.py:139] Terminating local vLLM worker processes


### 🐛 Describe the bug

ARNING 02-28 03:24:01 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:01 __init__.py:174] Platform plugin ascend is activated
INFO 02-28 03:24:02 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=480) INFO 02-28 03:24:02 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:14 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:14 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-28 03:24:14 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:14 __init__.py:174] Platform plugin ascend is activated
INFO 02-28 03:24:15 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-28 03:24:15 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-28 03:24:15 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-28 03:24:15 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-28 03:24:15 __init__.py:42] plugin ascend loaded.
INFO 02-28 03:24:15 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-28 03:24:15 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-28 03:24:15 __init__.py:174] Platform plugin ascend is activated
[rank0]:[W228 03:24:19.786171073 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank1]:[W228 03:24:19.792338061 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
INFO 02-28 03:24:19 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_76ce9c25'), local_subscribe_port=40075, remote_subscribe_port=None)
INFO 02-28 03:24:19 model_runner.py:1111] Starting to load model /data/part2/e5-mistral-7b-instruct...
(VllmWorkerProcess pid=480) INFO 02-28 03:24:19 model_runner.py:1111] Starting to load model /data/part2/e5-mistral-7b-instruct...
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:02<00:02,  2.56s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00,  1.89s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:03<00:00,  1.99s/it]

(VllmWorkerProcess pid=480) INFO 02-28 03:24:23 model_runner.py:1116] Loading model weights took 6.6315 GB
INFO 02-28 03:24:24 model_runner.py:1116] Loading model weights took 6.6315 GB
INFO 02-28 03:24:24 api_server.py:754] Using supplied chat template:
INFO 02-28 03:24:24 api_server.py:754] None
INFO 02-28 03:24:24 launcher.py:19] Available routes are:
INFO 02-28 03:24:24 launcher.py:27] Route: /openapi.json, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /docs, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /redoc, Methods: GET, HEAD
INFO 02-28 03:24:24 launcher.py:27] Route: /health, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /ping, Methods: GET, POST
INFO 02-28 03:24:24 launcher.py:27] Route: /tokenize, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /detokenize, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/models, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /version, Methods: GET
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /pooling, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /score, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/score, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v1/rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /v2/rerank, Methods: POST
INFO 02-28 03:24:24 launcher.py:27] Route: /invocations, Methods: POST
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9093 (Press CTRL+C to quit)
INFO 02-28 03:25:56 logger.py:37] Received request embd-cbf64ff4c5c64e66b2c4bb0db30e22d7-0: prompt: '你的文本内容', params: PoolingParams(additional_metadata=None), prompt_token_ids: [1, 28705, 29383, 28914, 29019, 29119, 29188, 29329, 2], lora_request: None, prompt_adapter_request: None.
INFO 02-28 03:25:56 engine.py:273] Added request embd-cbf64ff4c5c64e66b2c4bb0db30e22d7-0.
CRITICAL 02-28 03:25:56 launcher.py:99] MQLLMEngine is already dead, terminating server process
INFO:     180.168.189.253:18475 - "POST /v1/embeddings HTTP/1.1" 500 Internal Server Error
ERROR 02-28 03:25:56 engine.py:137] TypeError('AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given')
ERROR 02-28 03:25:56 engine.py:137] Traceback (most recent call last):
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 135, in start
ERROR 02-28 03:25:56 engine.py:137]     self.run_engine_loop()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 198, in run_engine_loop
ERROR 02-28 03:25:56 engine.py:137]     request_outputs = self.engine_step()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 216, in engine_step
ERROR 02-28 03:25:56 engine.py:137]     raise e
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 207, in engine_step
ERROR 02-28 03:25:56 engine.py:137]     return self.engine.step()
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1384, in step
ERROR 02-28 03:25:56 engine.py:137]     outputs = self.model_executor.execute_model(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 273, in execute_model
ERROR 02-28 03:25:56 engine.py:137]     driver_outputs = self._driver_execute_model(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 142, in _driver_execute_model
ERROR 02-28 03:25:56 engine.py:137]     return self.driver_worker.execute_model(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 387, in execute_model
ERROR 02-28 03:25:56 engine.py:137]     inputs = self.prepare_input(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 372, in prepare_input
ERROR 02-28 03:25:56 engine.py:137]     return self._get_driver_input_and_broadcast(execute_model_req)
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 334, in _get_driver_input_and_broadcast
ERROR 02-28 03:25:56 engine.py:137]     self.model_runner.prepare_model_input(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/pooling_model_runner.py", line 169, in prepare_model_input
ERROR 02-28 03:25:56 engine.py:137]     model_input = self._prepare_model_input_tensors(
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1221, in _prepare_model_input_tensors
ERROR 02-28 03:25:56 engine.py:137]     return self.builder.build()  # type: ignore
ERROR 02-28 03:25:56 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 926, in build
ERROR 02-28 03:25:56 engine.py:137]     attn_metadata = self.attn_metadata_builder.build(
ERROR 02-28 03:25:56 engine.py:137] TypeError: AscendMetadataBuilder.build() takes 3 positional arguments but 5 were given
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 317, in _bootstrap
    util._exit_function()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 334, in _exit_function
    _run_finalizers(0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 300, in _run_finalizers
    finalizer()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 54, in wrapper
    return func(cls, *args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 219, in finalize
    cls.global_mgr.finalize()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 84, in finalize
    self.mgr.shutdown()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 674, in _finalize_manager
    process.join(timeout=1.0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 149, in join
    res = self._popen.wait(timeout)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/popen_fork.py", line 40, in wait
    if not wait([self.sentinel], timeout):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 931, in wait
    ready = selector.select(timeout)
  File "/usr/local/python3.10/lib/python3.10/selectors.py", line 416, in select
    fd_event_list = self._selector.poll(timeout)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 372, in signal_handler
    raise KeyboardInterrupt("MQLLMEngine terminated")
KeyboardInterrupt: MQLLMEngine terminated
INFO 02-28 03:25:57 multiproc_worker_utils.py:139] Terminating local vLLM worker processes
```
