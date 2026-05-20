# Issue #2941: [Bug]: Lora doesn't work with 0.10.2rc1

## 基本信息

- **编号**: #2941
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2941
- **创建时间**: 2025-09-15T13:49:24Z
- **关闭时间**: 2025-09-28T02:31:32Z
- **更新时间**: 2025-09-28T02:31:45Z
- **提交者**: @wangxiyuan
- **评论数**: 1

## 标签

bug

## 问题描述

error log:
```
platform linux -- Python 3.11.13, pytest-8.4.2, pluggy-1.6.0 -- /usr/local/python3.11.13/bin/python3.11
cachedir: .pytest_cache
rootdir: /__w/vllm-ascend/vllm-ascend
configfile: pyproject.toml
plugins: cov-7.0.0, asyncio-1.2.0, mock-3.15.0, anyio-4.10.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 1 item

2025-09-15 13:34:20,619 - modelscope - INFO - Creating symbolic link [/root/.cache/modelscope/hub/models/vllm-ascend/ilama-3.2-1B].
2025-09-15 13:34:20,620 - modelscope - WARNING - Failed to create symbolic link /root/.cache/modelscope/hub/models/vllm-ascend/ilama-3.2-1B for /root/.cache/modelscope/hub/models/vllm-ascend/ilama-3___2-1B.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
`torch_dtype` is deprecated! Use `dtype` instead!
tests/e2e/multicard/test_ilama_lora_tp2.py::test_ilama_lora_tp2[mp] Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/ilama-text2sql-spider
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/ilama-3.2-1B
(Worker_TP0 pid=9572) `torch_dtype` is deprecated! Use `dtype` instead!
(Worker_TP1 pid=9573) `torch_dtype` is deprecated! Use `dtype` instead!
(Worker_TP0 pid=9572) 
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
(Worker_TP0 pid=9572) 
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:04<00:00,  4.50s/it]
(Worker_TP0 pid=9572) 
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:04<00:00,  4.50s/it]
(Worker_TP0 pid=9572) 
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] WorkerProc hit an exception.
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 606, in initialize_from_config
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.model_runner.initialize_kv_cache(kv_cache_config)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2396, in initialize_kv_cache
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in initialize_kv_cache_tensors
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     assert layer_names == set(kv_cache_raw_tensors.keys(
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] AssertionError: Some layers are not correctly initialized
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 606, in initialize_from_config
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.model_runner.initialize_kv_cache(kv_cache_config)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2[396](https://github.com/vllm-project/vllm-ascend/actions/runs/17734232095/job/50392452861?pr=2917#step:10:398), in initialize_kv_cache
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in initialize_kv_cache_tensors
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     assert layer_names == set(kv_cache_raw_tensors.keys(
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] AssertionError: Some layers are not correctly initialized
(Worker_TP0 pid=9572) ERROR 09-15 13:35:29 [multiproc_executor.py:654] 
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654] WorkerProc hit an exception.
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 606, in initialize_from_config
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.model_runner.initialize_kv_cache(kv_cache_config)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2396, in initialize_kv_cache
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in initialize_kv_cache_tensors
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     assert layer_names == set(kv_cache_raw_tensors.keys(
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654] AssertionError: Some layers are not correctly initialized
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654] Traceback (most recent call last):
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     output = func(*args, **kwargs)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 606, in initialize_from_config
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     self.model_runner.initialize_kv_cache(kv_cache_config)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2396, in initialize_kv_cache
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in initialize_kv_cache_tensors
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]     assert layer_names == set(kv_cache_raw_tensors.keys(
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=9573) ERROR 09-15 13:35:29 [multiproc_executor.py:654] AssertionError: Some layers are not correctly initialized
```

