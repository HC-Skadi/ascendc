# Issue #3096: [Bug]:  AssertionError: Some layers are not correctly initialized(gpt-oss模型）

## 基本信息

- **编号**: #3096
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3096
- **创建时间**: 2025-09-22T08:50:25Z
- **关闭时间**: 2025-09-24T03:32:36Z
- **更新时间**: 2025-09-24T03:32:36Z
- **提交者**: @yuanyuanwwu
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

# GPT-OSS模型推理时，部分层初始化失败

(EngineCore_DP0 pid=2684565) ERROR 09-22 09:44:21 [core.py:718] AssertionError: Some layers are not correctly initialized
(EngineCore_DP0 pid=2684565) Process EngineCore_DP0:
(EngineCore_DP0 pid=2684565) Traceback (most recent call last):
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=2684565)     self.run()
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=2684565)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 722, in run_engine_core
(EngineCore_DP0 pid=2684565)     raise e
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=2684565)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=2684565)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 91, in __init__
(EngineCore_DP0 pid=2684565)     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 215, in _initialize_kv_caches
(EngineCore_DP0 pid=2684565)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 72, in initialize_from_config
(EngineCore_DP0 pid=2684565)     self.collective_rpc("initialize_from_config",
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=2684565)     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=2684565)     return func(*args, **kwargs)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 606, in initialize_from_config
(EngineCore_DP0 pid=2684565)     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 293, in initialize_from_config
(EngineCore_DP0 pid=2684565)     self.model_runner.initialize_kv_cache(kv_cache_config)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2396, in initialize_kv_cache
(EngineCore_DP0 pid=2684565)     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
(EngineCore_DP0 pid=2684565)   File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2530, in initialize_kv_cache_tensors
(EngineCore_DP0 pid=2684565)     assert layer_names == set(kv_cache_raw_tensors.keys(
(EngineCore_DP0 pid=2684565) AssertionError: Some layers are not correctly initialized
Traceback (most recent call last):
  File "/home/w00898017/verl/verl/vllm_wyy/example.py", line 14, in <module>
    llm = LLM(model="/home/j30074199/models/gpt-oss-20b-bf16",trust_remote_code=True,max_num_batched_tokens=64,max_model_len=32768,enforce_eager=True,tensor_parallel_size=1,gpu_memory_utilization=0.9,skip_tokenizer_init=False,tokenizer_mode="auto")
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 282, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 493, in from_engine_args
    return engine_cls.from_vllm_config(
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 134, in from_vllm_config
    return cls(vllm_config=vllm_config,
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 111, in __init__
    self.engine_core = EngineCoreClient.make_client(
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 80, in make_client
    return SyncMPClient(vllm_config, executor_class, log_stats)
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 602, in __init__
    super().__init__(
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 448, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 729, in launch_core_engines
    wait_for_engine_startup(
  File "/home/anaconda3/envs/verl_wyy_vllm0/lib/python3.10/site-packages/vllm/v1/engine/utils.py", line 782, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-09-22-09:44:22 (PID:2682507, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

