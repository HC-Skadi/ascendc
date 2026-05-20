# Issue #2034: [Bug]: ValueError: While loading model xxx, expected target modules in ['embed_tokens'] but received

## 基本信息

- **编号**: #2034
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2034
- **创建时间**: 2025-07-26T06:23:03Z
- **关闭时间**: 2025-09-18T00:39:25Z
- **更新时间**: 2025-09-18T00:39:42Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment
Keyerror: ValueError: While loading /root/.cache/modelscope/hub/models/vllm-ascend/ilama-text2sql-spider, expected target modules in ['embed_tokens'] but received
Workaround

transformers 4.54.0

cmd:

`VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_VERSION=0.10.0 VLLM_USE_MODELSCOPE=true pytest -sv tests/e2e/singlecard/test_ilama_lora.py::test_ilama_lora`

https://github.com/vllm-project/vllm-ascend/actions/runs/16535834694/job/46770133393

### 🐛 Describe the bug

<details>
<summary>The output of `python collect_env.py`</summary>

ERROR 07-26 06:20:12 [core.py:634] EngineCore encountered a fatal error.
ERROR 07-26 06:20:12 [core.py:634] Traceback (most recent call last):
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 625, in run_engine_core
ERROR 07-26 06:20:12 [core.py:634]     engine_core.run_busy_loop()
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 652, in run_busy_loop
ERROR 07-26 06:20:12 [core.py:634]     self._process_engine_step()
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 677, in _process_engine_step
ERROR 07-26 06:20:12 [core.py:634]     outputs, model_executed = self.step_fn()
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 267, in step
ERROR 07-26 06:20:12 [core.py:634]     model_output = self.execute_model_with_error_logging(
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 253, in execute_model_with_error_logging
ERROR 07-26 06:20:12 [core.py:634]     raise err
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 244, in execute_model_with_error_logging
ERROR 07-26 06:20:12 [core.py:634]     return model_fn(scheduler_output)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 87, in execute_model
ERROR 07-26 06:20:12 [core.py:634]     output = self.collective_rpc("execute_model",
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
ERROR 07-26 06:20:12 [core.py:634]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2985, in run_method
ERROR 07-26 06:20:12 [core.py:634]     return func(*args, **kwargs)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 194, in execute_model
ERROR 07-26 06:20:12 [core.py:634]     output = self.model_runner.execute_model(scheduler_output,
ERROR 07-26 06:20:12 [core.py:634]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-26 06:20:12 [core.py:634]     return func(*args, **kwargs)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1442, in execute_model
ERROR 07-26 06:20:12 [core.py:634]     num_scheduled_tokens_np) = (self._process_reqs(
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 949, in _process_reqs
ERROR 07-26 06:20:12 [core.py:634]     self.set_active_loras(self.input_batch, num_scheduled_tokens)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/worker/lora_model_runner_mixin.py", line 84, in set_active_loras
ERROR 07-26 06:20:12 [core.py:634]     return self._set_active_loras(prompt_lora_mapping, token_lora_mapping,
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/worker/lora_model_runner_mixin.py", line 73, in _set_active_loras
ERROR 07-26 06:20:12 [core.py:634]     self.lora_manager.set_active_adapters(lora_requests, lora_mapping)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 167, in set_active_adapters
ERROR 07-26 06:20:12 [core.py:634]     set_active_adapters_worker(requests, mapping, self._apply_adapters,
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/adapter_commons/utils.py", line 55, in set_active_adapters_worker
ERROR 07-26 06:20:12 [core.py:634]     apply_adapters_func(requests)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 227, in _apply_adapters
ERROR 07-26 06:20:12 [core.py:634]     self.add_adapter(lora)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 240, in add_adapter
ERROR 07-26 06:20:12 [core.py:634]     lora = self._load_adapter(lora_request)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 141, in _load_adapter
ERROR 07-26 06:20:12 [core.py:634]     raise e
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/worker_manager.py", line 116, in _load_adapter
ERROR 07-26 06:20:12 [core.py:634]     lora = self._lora_model_cls.from_local_checkpoint(
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/models.py", line 255, in from_local_checkpoint
ERROR 07-26 06:20:12 [core.py:634]     check_unexpected_modules(f)
ERROR 07-26 06:20:12 [core.py:634]   File "/vllm-workspace/vllm/vllm/lora/models.py", line 225, in check_unexpected_modules
ERROR 07-26 06:20:12 [core.py:634]     raise ValueError(
ERROR 07-26 06:20:12 [core.py:634] ValueError: While loading /root/.cache/modelscope/hub/models/vllm-ascend/ilama-text2sql-spider, expected target modules in ['embed_tokens'] but received ['model.layers.0.mlp.down_proj', 'model.layers.0.mlp.down_proj', 'model.layers.0.mlp.gate_proj', 'model.layers.0.mlp.gate_proj', 'model.layers.0.mlp.up_proj', 'model.layers.0.mlp.up_proj', 'model.layers.0.self_attn.k_proj', 'model.layers.0.self_attn.k_proj', 'model.layers.0.self_attn.o_proj', 'model.layers.0.self_attn.o_proj', 'model.layers.0.self_attn.q_proj', 'model.layers.0.self_attn.q_proj', 'model.layers.0.self_attn.v_proj', 'model.layers.0.self_attn.v_proj', 'model.layers.1.mlp.down_proj', 'model.layers.1.mlp.down_proj', 'model.layers.1.mlp.gate_proj', 'model.layers.1.mlp.gate_proj', 'model.layers.1.mlp.up_proj', 'model.layers.1.mlp.up_proj', 'model.layers.1.self_attn.k_proj', 'model.layers.1.self_attn.k_proj', 'model.layers.1.self_attn.o_proj', 'model.layers.1.self_attn.o_proj', 'model.layers.1.self_attn.q_proj', 'model.layers.1.self_attn.q_proj', 'model.layers.1.self_attn.v_proj', 'model.layers.1.self_attn.v_proj', 'model.layers.10.mlp.down_proj', 'model.layers.10.mlp.down_proj', 'model.layers.10.mlp.gate_proj', 'model.layers.10.mlp.gate_proj', 'model.layers.10.mlp.up_proj', 'model.layers.10.mlp.up_proj', 'model.layers.10.self_attn.k_proj', 'model.layers.10.self_attn.k_proj', 'model.layers.10.self_attn.o_proj', 'model.layers.10.self_attn.o_proj', 'model.layers.10.self_attn.q_proj', 'model.layers.10.self_attn.q_proj', 'model.layers.10.self_attn.v_proj', 'model.layers.10.self_attn.v_proj', 'model.layers.11.mlp.down_proj', 'model.layers.11.mlp.down_proj', 'model.layers.11.mlp.gate_proj', 'model.layers.11.mlp.gate_proj', 'model.layers.11.mlp.up_proj', 'model.layers.11.mlp.up_proj', 'model.layers.11.self_attn.k_proj', 'model.layers.11.self_attn.k_proj', 'model.layers.11.self_attn.o_proj', 'model.layers.11.self_attn.o_proj', 'model.layers.11.self_attn.q_proj', 'model.layers.11.self_attn.q_proj', 'model.layers.11.self_attn.v_proj', 'model.layers.11.self_attn.v_proj', 'model.layers.12.mlp.down_proj', 'model.layers.12.mlp.down_proj', 'model.layers.12.mlp.gate_proj', 'model.layers.12.mlp.gate_proj', 'model.layers.12.mlp.up_proj', 'model.layers.12.mlp.up_proj', 'model.layers.12.self_attn.k_proj', 'model.layers.12.self_attn.k_proj', 'model.layers.12.self_attn.o_proj', 'model.layers.12.self_attn.o_proj', 'model.layers.12.self_attn.q_proj', 'model.layers.12.self_attn.q_proj', 'model.layers.12.self_attn.v_proj', 'model.layers.12.self_attn.v_proj', 'model.layers.13.mlp.down_proj', 'model.layers.13.mlp.down_proj', 'model.layers.13.mlp.gate_proj', 'model.layers.13.mlp.gate_proj', 'model.layers.13.mlp.up_proj', 'model.layers.13.mlp.up_proj', 'model.layers.13.self_attn.k_proj', 'model.layers.13.self_attn.k_proj', 'model.layers.13.self_attn.o_proj', 'model.layers.13.self_attn.o_proj', 'model.layers.13.self_attn.q_proj', 'model.layers.13.self_attn.q_proj', 'model.layers.13.self_attn.v_proj', 'model.layers.13.self_attn.v_proj', 'model.layers.14.mlp.down_proj', 'model.layers.14.mlp.down_proj', 'model.layers.14.mlp.gate_proj', 'model.layers.14.mlp.gate_proj', 'model.layers.14.mlp.up_proj', 'model.layers.14.mlp.up_proj', 'model.layers.14.self_attn.k_proj', 'model.layers.14.self_attn.k_proj', 'model.layers.14.self_attn.o_proj', 'model.layers.14.self_attn.o_proj', 'model.layers.14.self_attn.q_proj', 'model.layers.14.self_attn.q_proj', 'model.layers.14.self_attn.v_proj', 'model.layers.14.self_attn.v_proj', 'model.layers.15.mlp.down_proj', 'model.layers.15.mlp.down_proj', 'model.layers.15.mlp.gate_proj', 'model.layers.15.mlp.gate_proj', 'model.layers.15.mlp.up_proj', 'model.layers.15.mlp.up_proj', 'model.layers.15.self_attn.k_proj', 'model.layers.15.self_attn.k_proj', 'model.layers.15.self_attn.o_proj', 'model.layers.15.self_attn.o_proj', 'model.layers.15.self_attn.q_proj', 'model.layers.15.self_attn.q_proj', 'model.layers.15.self_attn.v_proj', 'model.layers.15.self_attn.v_proj', 'model.layers.2.mlp.down_proj', 'model.layers.2.mlp.down_proj', 'model.layers.2.mlp.gate_proj', 'model.layers.2.mlp.gate_proj', 'model.layers.2.mlp.up_proj', 'model.layers.2.mlp.up_proj', 'model.layers.2.self_attn.k_proj', 'model.layers.2.self_attn.k_proj', 'model.layers.2.self_attn.o_proj', 'model.layers.2.self_attn.o_proj', 'model.layers.2.self_attn.q_proj', 'model.layers.2.self_attn.q_proj', 'model.layers.2.self_attn.v_proj', 'model.layers.2.self_attn.v_proj', 'model.layers.3.mlp.down_proj', 'model.layers.3.mlp.down_proj', 'model.layers.3.mlp.gate_proj', 'model.layers.3.mlp.gate_proj', 'model.layers.3.mlp.up_proj', 'model.layers.3.mlp.up_proj', 'model.layers.3.self_attn.k_proj', 'model.layers.3.self_attn.k_proj', 'model.layers.3.self_attn.o_proj', 'model.layers.3.self_attn.o_proj', 'model.layers.3.self_attn.q_proj', 'model.layers.3.self_attn.q_proj', 'model.layers.3.self_attn.v_proj', 'model.layers.3.self_attn.v_proj', 'model.layers.4.mlp.down_proj', 'model.layers.4.mlp.down_proj', 'model.layers.4.mlp.gate_proj', 'model.layers.4.mlp.gate_proj', 'model.layers.4.mlp.up_proj', 'model.layers.4.mlp.up_proj', 'model.layers.4.self_attn.k_proj', 'model.layers.4.self_attn.k_proj', 'model.layers.4.self_attn.o_proj', 'model.layers.4.self_attn.o_proj', 'model.layers.4.self_attn.q_proj', 'model.layers.4.self_attn.q_proj', 'model.layers.4.self_attn.v_proj', 'model.layers.4.self_attn.v_proj', 'model.layers.5.mlp.down_proj', 'model.layers.5.mlp.down_proj', 'model.layers.5.mlp.gate_proj', 'model.layers.5.mlp.gate_proj', 'model.layers.5.mlp.up_proj', 'model.layers.5.mlp.up_proj', 'model.layers.5.self_attn.k_proj', 'model.layers.5.self_attn.k_proj', 'model.layers.5.self_attn.o_proj', 'model.layers.5.self_attn.o_proj', 'model.layers.5.self_attn.q_proj', 'model.layers.5.self_attn.q_proj', 'model.layers.5.self_attn.v_proj', 'model.layers.5.self_attn.v_proj', 'model.layers.6.mlp.down_proj', 'model.layers.6.mlp.down_proj', 'model.layers.6.mlp.gate_proj', 'model.layers.6.mlp.gate_proj', 'model.layers.6.mlp.up_proj', 'model.layers.6.mlp.up_proj', 'model.layers.6.self_attn.k_proj', 'model.layers.6.self_attn.k_proj', 'model.layers.6.self_attn.o_proj', 'model.layers.6.self_attn.o_proj', 'model.layers.6.self_attn.q_proj', 'model.layers.6.self_attn.q_proj', 'model.layers.6.self_attn.v_proj', 'model.layers.6.self_attn.v_proj', 'model.layers.7.mlp.down_proj', 'model.layers.7.mlp.down_proj', 'model.layers.7.mlp.gate_proj', 'model.layers.7.mlp.gate_proj', 'model.layers.7.mlp.up_proj', 'model.layers.7.mlp.up_proj', 'model.layers.7.self_attn.k_proj', 'model.layers.7.self_attn.k_proj', 'model.layers.7.self_attn.o_proj', 'model.layers.7.self_attn.o_proj', 'model.layers.7.self_attn.q_proj', 'model.layers.7.self_attn.q_proj', 'model.layers.7.self_attn.v_proj', 'model.layers.7.self_attn.v_proj', 'model.layers.8.mlp.down_proj', 'model.layers.8.mlp.down_proj', 'model.layers.8.mlp.gate_proj', 'model.layers.8.mlp.gate_proj', 'model.layers.8.mlp.up_proj', 'model.layers.8.mlp.up_proj', 'model.layers.8.self_attn.k_proj', 'model.layers.8.self_attn.k_proj', 'model.layers.8.self_attn.o_proj', 'model.layers.8.self_attn.o_proj', 'model.layers.8.self_attn.q_proj', 'model.layers.8.self_attn.q_proj', 'model.layers.8.self_attn.v_proj', 'model.layers.8.self_attn.v_proj', 'model.layers.9.mlp.down_proj', 'model.layers.9.mlp.down_proj', 'model.layers.9.mlp.gate_proj', 'model.layers.9.mlp.gate_proj', 'model.layers.9.mlp.up_proj', 'model.layers.9.mlp.up_proj', 'model.layers.9.self_attn.k_proj', 'model.layers.9.self_attn.k_proj', 'model.layers.9.self_attn.o_proj', 'model.layers.9.self_attn.o_proj', 'model.layers.9.self_attn.q_proj', 'model.layers.9.self_attn.q_proj', 'model.layers.9.self_attn.v_proj', 'model.layers.9.self_attn.v_proj']. Please verify that the loaded LoRA module is correct


</details>
