# Issue #133: RuntimeError: Prefix cache and chunked prefill are currently not supported

## 基本信息

- **编号**: #133
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/133
- **创建时间**: 2025-02-21T08:40:31Z
- **关闭时间**: 2025-03-13T07:50:24Z
- **更新时间**: 2025-03-13T07:50:26Z
- **提交者**: @dawnranger
- **评论数**: 4

## 标签

feature request

## 问题描述

# package version
```
torch                             2.5.1+cpu
torch-npu                         2.5.1.dev20250218
transformers                      4.50.0.dev0
trl                               0.16.0.dev0
vllm                              0.7.1+empty
vllm_ascend                       0.7.1rc1
```
CANN: 8.0.0.beta1

# LOG
```
[INFO|trainer.py:2407] 2025-02-21 08:20:06,854 >> ***** Running training *****
[INFO|trainer.py:2408] 2025-02-21 08:20:06,855 >>   Num examples = 7,473
[INFO|trainer.py:2409] 2025-02-21 08:20:06,855 >>   Num Epochs = 3
[INFO|trainer.py:2410] 2025-02-21 08:20:06,855 >>   Instantaneous batch size per device = 1
[INFO|trainer.py:2413] 2025-02-21 08:20:06,855 >>   Total train batch size (w. parallel, distributed & accumulation) = 14
[INFO|trainer.py:2414] 2025-02-21 08:20:06,855 >>   Gradient Accumulation steps = 2
[INFO|trainer.py:2415] 2025-02-21 08:20:06,855 >>   Total optimization steps = 11,208
[INFO|trainer.py:2416] 2025-02-21 08:20:06,856 >>   Number of trainable parameters = 1,543,714,304
[INFO|integration_utils.py:817] 2025-02-21 08:20:06,857 >> Automatic Weights & Biases logging enabled, to disable set os.environ["WANDB_DISABLED"] = "true"

  0%|          | 0/11208 [00:00<?, ?it/s]Traceback (most recent call last):
  File "/root/open-r1/src/run_grpo.py", line 9, in <module>
    main()
  File "/root/open-r1/src/run_grpo.py", line 6, in main
    run_exp()
  File "/root/open-r1/src/open_r1/grpo.py", line 263, in run_exp
    main(script_args, training_args, model_args)
  File "/root/open-r1/src/open_r1/grpo.py", line 225, in main
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2243, in train
    return inner_training_loop(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2554, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 3698, in training_step
    inputs = self._prepare_inputs(inputs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/trl/trainer/grpo_trainer.py", line 573, in _prepare_inputs
    outputs = self.llm.generate(all_prompts_text, sampling_params=self.sampling_params, use_tqdm=False)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 1074, in inner
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 467, in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1388, in _run_engine
    step_outputs = self.llm_engine.step()
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1384, in step
    outputs = self.model_executor.execute_model(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 136, in execute_model
    output = self.collective_rpc("execute_model",
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
    output = self.model_runner.execute_model(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
    hidden_or_intermediate_states = model_executable(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 484, in forward
    hidden_states = self.model(input_ids, positions, kv_caches,
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 170, in __call__
    return self.forward(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 346, in forward
    hidden_states, residual = layer(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 245, in forward
    hidden_states = self.self_attn(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 177, in forward
    attn_output = self.attn(q, k, v, kv_cache, attn_metadata)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/attention/layer.py", line 182, in forward
    return unified_attention(query, key, value, self.layer_name)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/attention/layer.py", line 290, in unified_attention
    return self.impl.forward(self, query, key, value, kv_cache, attn_metadata)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm_ascend/attention.py", line 596, in forward
    raise RuntimeError(
RuntimeError: Prefix cache and chunked prefill are currently not supported.
[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 9, in <module>
[rank0]:     main()
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 6, in main
[rank0]:     run_exp()
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 263, in run_exp
[rank0]:     main(script_args, training_args, model_args)
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 225, in main
[rank0]:     train_result = trainer.train(resume_from_checkpoint=checkpoint)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2243, in train
[rank0]:     return inner_training_loop(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 2554, in _inner_training_loop
[rank0]:     tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/transformers/trainer.py", line 3698, in training_step
[rank0]:     inputs = self._prepare_inputs(inputs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/trl/trainer/grpo_trainer.py", line 573, in _prepare_inputs
[rank0]:     outputs = self.llm.generate(all_prompts_text, sampling_params=self.sampling_params, use_tqdm=False)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 1074, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 467, in generate
[rank0]:     outputs = self._run_engine(use_tqdm=use_tqdm)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1388, in _run_engine
[rank0]:     step_outputs = self.llm_engine.step()
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1384, in step
[rank0]:     outputs = self.model_executor.execute_model(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 136, in execute_model
[rank0]:     output = self.collective_rpc("execute_model",
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
[rank0]:     output = self.model_runner.execute_model(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 484, in forward
[rank0]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 170, in __call__
[rank0]:     return self.forward(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 346, in forward
[rank0]:     hidden_states, residual = layer(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 245, in forward
[rank0]:     hidden_states = self.self_attn(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 177, in forward
[rank0]:     attn_output = self.attn(q, k, v, kv_cache, attn_metadata)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/attention/layer.py", line 182, in forward
[rank0]:     return unified_attention(query, key, value, self.layer_name)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/attention/layer.py", line 290, in unified_attention
[rank0]:     return self.impl.forward(self, query, key, value, kv_cache, attn_metadata)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm_ascend/attention.py", line 596, in forward
[rank0]:     raise RuntimeError(
[rank0]: RuntimeError: Prefix cache and chunked prefill are currently not supported.
```
