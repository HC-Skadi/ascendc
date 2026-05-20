# Issue #1962: [Bug]: llava-hf/llava-1.5-7b-hf and Shanghai_AI_Laboratory/internlm-7b failed to start in graph mode due to unsupported operator: _C.rotary_embedding.default

## 基本信息

- **编号**: #1962
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1962
- **创建时间**: 2025-07-23T07:40:47Z
- **关闭时间**: 2025-07-25T06:12:52Z
- **更新时间**: 2025-07-25T06:12:52Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

image: v0.9.2rc1
```
VLLM_USE_MODELSCOPE=True vllm serve  llava-hf/llava-1.5-7b-hf --trust_remote_code &
```


### 🐛 Describe the bug

bug:
```
INFO 07-23 07:21:47 [default_loader.py:272] Loading weights took 14.26 seconds
INFO 07-23 07:21:48 [model_runner_v1.py:1831] Loading model weights took 13.1367 GB
ERROR 07-23 07:21:49 [core.py:586] EngineCore failed to start.
ERROR 07-23 07:21:49 [core.py:586] Traceback (most recent call last):
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2013, in _dispatch_impl
ERROR 07-23 07:21:49 [core.py:586]     r = func(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 716, in __call__
ERROR 07-23 07:21:49 [core.py:586]     return self._op(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586] NotImplementedError: _C::rotary_embedding: attempted to run this operator with Meta tensors, but there was no fake impl or Meta kernel registered. You may have run into this message while using an operator with PT2 compilation APIs (torch.compile/torch.export); in order to use this operator with those APIs you'll need to add a fake impl. Please see the following for next steps:  https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] During handling of the above exception, another exception occurred:
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] Traceback (most recent call last):
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
ERROR 07-23 07:21:49 [core.py:586]     return node.target(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 07-23 07:21:49 [core.py:586]     return self._op(*args, **(kwargs or {}))
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return fn(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
ERROR 07-23 07:21:49 [core.py:586]     return self.dispatch(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
ERROR 07-23 07:21:49 [core.py:586]     return self._cached_dispatch_impl(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
ERROR 07-23 07:21:49 [core.py:586]     output = self._dispatch_impl(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
ERROR 07-23 07:21:49 [core.py:586]     return maybe_run_unsafe_fallback(not_implemented_error)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
ERROR 07-23 07:21:49 [core.py:586]     raise UnsupportedOperatorException(func)
ERROR 07-23 07:21:49 [core.py:586] torch._subclasses.fake_tensor.UnsupportedOperatorException: _C.rotary_embedding.default
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] The above exception was the direct cause of the following exception:
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] Traceback (most recent call last):
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2017, in get_fake_value
ERROR 07-23 07:21:49 [core.py:586]     ret_val = wrap_fake_exception(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1574, in wrap_fake_exception
ERROR 07-23 07:21:49 [core.py:586]     return fn()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2018, in <lambda>
ERROR 07-23 07:21:49 [core.py:586]     lambda: run_node(tx.output, node, args, kwargs, nnmodule)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2150, in run_node
ERROR 07-23 07:21:49 [core.py:586]     raise RuntimeError(make_error_message(e)).with_traceback(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
ERROR 07-23 07:21:49 [core.py:586]     return node.target(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 07-23 07:21:49 [core.py:586]     return self._op(*args, **(kwargs or {}))
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return fn(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
ERROR 07-23 07:21:49 [core.py:586]     return self.dispatch(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
ERROR 07-23 07:21:49 [core.py:586]     return self._cached_dispatch_impl(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
ERROR 07-23 07:21:49 [core.py:586]     output = self._dispatch_impl(func, types, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
ERROR 07-23 07:21:49 [core.py:586]     return maybe_run_unsafe_fallback(not_implemented_error)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
ERROR 07-23 07:21:49 [core.py:586]     raise UnsupportedOperatorException(func)
ERROR 07-23 07:21:49 [core.py:586] RuntimeError: Failed running call_function _C.rotary_embedding(*(FakeTensor(..., device='npu:0', size=(s1,), dtype=torch.int64), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), 128, FakeTensor(..., device='npu:0', size=(4096, 128), dtype=torch.float16), True), **{}):
ERROR 07-23 07:21:49 [core.py:586] _C.rotary_embedding.default
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] During handling of the above exception, another exception occurred:
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] Traceback (most recent call last):
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 07-23 07:21:49 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 404, in __init__
ERROR 07-23 07:21:49 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 82, in __init__
ERROR 07-23 07:21:49 [core.py:586]     self._initialize_kv_caches(vllm_config)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 142, in _initialize_kv_caches
ERROR 07-23 07:21:49 [core.py:586]     available_gpu_memory = self.model_executor.determine_available_memory()
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
ERROR 07-23 07:21:49 [core.py:586]     output = self.collective_rpc("determine_available_memory")
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 07-23 07:21:49 [core.py:586]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/utils/__init__.py", line 2736, in run_method
ERROR 07-23 07:21:49 [core.py:586]     return func(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 146, in determine_available_memory
ERROR 07-23 07:21:49 [core.py:586]     self.model_runner.profile_run()
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1700, in profile_run
ERROR 07-23 07:21:49 [core.py:586]     hidden_states = self._dummy_run(self.max_num_tokens)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-23 07:21:49 [core.py:586]     return func(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1684, in _dummy_run
ERROR 07-23 07:21:49 [core.py:586]     hidden_states = model(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 07-23 07:21:49 [core.py:586]     return self._call_impl(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 07-23 07:21:49 [core.py:586]     return forward_call(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llava.py", line 759, in forward
ERROR 07-23 07:21:49 [core.py:586]     hidden_states = self.language_model.model(input_ids,
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 239, in __call__
ERROR 07-23 07:21:49 [core.py:586]     output = self.compiled_callable(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
ERROR 07-23 07:21:49 [core.py:586]     return fn(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 1269, in __call__
ERROR 07-23 07:21:49 [core.py:586]     return self._torchdynamo_orig_callable(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 526, in __call__
ERROR 07-23 07:21:49 [core.py:586]     return _compile(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 924, in _compile
ERROR 07-23 07:21:49 [core.py:586]     guarded_code = compile_inner(code, one_graph, hooks, transform)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 666, in compile_inner
ERROR 07-23 07:21:49 [core.py:586]     return _compile_inner(code, one_graph, hooks, transform)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_utils_internal.py", line 87, in wrapper_function
ERROR 07-23 07:21:49 [core.py:586]     return function(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 699, in _compile_inner
ERROR 07-23 07:21:49 [core.py:586]     out_code = transform_code_object(code, transform)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/bytecode_transformation.py", line 1322, in transform_code_object
ERROR 07-23 07:21:49 [core.py:586]     transformations(instructions, code_options)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 219, in _fn
ERROR 07-23 07:21:49 [core.py:586]     return fn(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 634, in transform
ERROR 07-23 07:21:49 [core.py:586]     tracer.run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2796, in run
ERROR 07-23 07:21:49 [core.py:586]     super().run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 07-23 07:21:49 [core.py:586]     while self.step():
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 07-23 07:21:49 [core.py:586]     self.dispatch_table[inst.opcode](self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return inner_fn(self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 07-23 07:21:49 [core.py:586]     self.call_function(fn, args, {})
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 07-23 07:21:49 [core.py:586]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return super().call_function(tx, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 07-23 07:21:49 [core.py:586]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 07-23 07:21:49 [core.py:586]     return inline_call(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 07-23 07:21:49 [core.py:586]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 07-23 07:21:49 [core.py:586]     tracer.run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 07-23 07:21:49 [core.py:586]     while self.step():
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 07-23 07:21:49 [core.py:586]     self.dispatch_table[inst.opcode](self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return inner_fn(self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1692, in CALL_FUNCTION_KW
ERROR 07-23 07:21:49 [core.py:586]     self.call_function(fn, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 07-23 07:21:49 [core.py:586]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
ERROR 07-23 07:21:49 [core.py:586]     return getattr(self.realize(), name)(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return super().call_function(tx, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 07-23 07:21:49 [core.py:586]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 07-23 07:21:49 [core.py:586]     return inline_call(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 07-23 07:21:49 [core.py:586]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 07-23 07:21:49 [core.py:586]     tracer.run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 07-23 07:21:49 [core.py:586]     while self.step():
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 07-23 07:21:49 [core.py:586]     self.dispatch_table[inst.opcode](self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return inner_fn(self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 07-23 07:21:49 [core.py:586]     self.call_function(fn, args, {})
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 07-23 07:21:49 [core.py:586]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
ERROR 07-23 07:21:49 [core.py:586]     return getattr(self.realize(), name)(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return variables.UserFunctionVariable(fn, source=source).call_function(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return super().call_function(tx, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 07-23 07:21:49 [core.py:586]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 07-23 07:21:49 [core.py:586]     return inline_call(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 07-23 07:21:49 [core.py:586]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 07-23 07:21:49 [core.py:586]     tracer.run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 07-23 07:21:49 [core.py:586]     while self.step():
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 07-23 07:21:49 [core.py:586]     self.dispatch_table[inst.opcode](self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return inner_fn(self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1680, in CALL_FUNCTION_EX
ERROR 07-23 07:21:49 [core.py:586]     self.call_function(fn, argsvars.items, kwargsvars)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 07-23 07:21:49 [core.py:586]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 385, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return super().call_function(tx, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return super().call_function(tx, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
ERROR 07-23 07:21:49 [core.py:586]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
ERROR 07-23 07:21:49 [core.py:586]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
ERROR 07-23 07:21:49 [core.py:586]     return inline_call(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
ERROR 07-23 07:21:49 [core.py:586]     return cls.inline_call_(parent, func, args, kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
ERROR 07-23 07:21:49 [core.py:586]     tracer.run()
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
ERROR 07-23 07:21:49 [core.py:586]     while self.step():
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
ERROR 07-23 07:21:49 [core.py:586]     self.dispatch_table[inst.opcode](self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
ERROR 07-23 07:21:49 [core.py:586]     return inner_fn(self, inst)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
ERROR 07-23 07:21:49 [core.py:586]     self.call_function(fn, args, {})
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
ERROR 07-23 07:21:49 [core.py:586]     self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/torch.py", line 897, in call_function
ERROR 07-23 07:21:49 [core.py:586]     tensor_variable = wrap_fx_proxy(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2037, in wrap_fx_proxy
ERROR 07-23 07:21:49 [core.py:586]     return wrap_fx_proxy_cls(target_cls=TensorVariable, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2124, in wrap_fx_proxy_cls
ERROR 07-23 07:21:49 [core.py:586]     example_value = get_fake_value(proxy.node, tx, allow_non_graph_fake=True)
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2064, in get_fake_value
ERROR 07-23 07:21:49 [core.py:586]     unimplemented(
ERROR 07-23 07:21:49 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/exc.py", line 297, in unimplemented
ERROR 07-23 07:21:49 [core.py:586]     raise Unsupported(msg, case_name=case_name)
ERROR 07-23 07:21:49 [core.py:586] torch._dynamo.exc.Unsupported: unsupported operator: _C.rotary_embedding.default (see https://docs.google.com/document/d/1GgvOe7C8_NVOMLOCwDaYV1mXXyHMXY7ExoewHqooxrs/edit#heading=h.64r4npvq0w0 for how to fix)
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] from user code:
ERROR 07-23 07:21:49 [core.py:586]    File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 392, in forward
ERROR 07-23 07:21:49 [core.py:586]     hidden_states, residual = layer(positions, hidden_states, residual)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 305, in forward
ERROR 07-23 07:21:49 [core.py:586]     hidden_states = self.self_attn(positions=positions,
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 202, in forward
ERROR 07-23 07:21:49 [core.py:586]     q, k = self.rotary_emb(positions, q, k)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/custom_op.py", line 44, in forward
ERROR 07-23 07:21:49 [core.py:586]     return self._forward_method(*args, **kwargs)
ERROR 07-23 07:21:49 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 62, in rope_forward_oot
ERROR 07-23 07:21:49 [core.py:586]     query, key = torch.ops._C.rotary_embedding(
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586]
ERROR 07-23 07:21:49 [core.py:586] You can suppress this exception and fall back to eager by setting:
ERROR 07-23 07:21:49 [core.py:586]     import torch._dynamo
ERROR 07-23 07:21:49 [core.py:586]     torch._dynamo.config.suppress_errors = True
ERROR 07-23 07:21:49 [core.py:586]
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2013, in _dispatch_impl
    r = func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 716, in __call__
    return self._op(*args, **kwargs)
NotImplementedError: _C::rotary_embedding: attempted to run this operator with Meta tensors, but there was no fake impl or Meta kernel registered. You may have run into this message while using an operator with PT2 compilation APIs (torch.compile/torch.export); in order to use this operator with those APIs you'll need to add a fake impl. Please see the following for next steps:  https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
    return node.target(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
    return self.dispatch(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
    return self._cached_dispatch_impl(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
    output = self._dispatch_impl(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
    return maybe_run_unsafe_fallback(not_implemented_error)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
    raise UnsupportedOperatorException(func)
torch._subclasses.fake_tensor.UnsupportedOperatorException: _C.rotary_embedding.default

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2017, in get_fake_value
    ret_val = wrap_fake_exception(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 1574, in wrap_fake_exception
    return fn()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2018, in <lambda>
    lambda: run_node(tx.output, node, args, kwargs, nnmodule)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2150, in run_node
    raise RuntimeError(make_error_message(e)).with_traceback(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2132, in run_node
    return node.target(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_stats.py", line 21, in wrapper
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1238, in __torch_dispatch__
    return self.dispatch(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1692, in dispatch
    return self._cached_dispatch_impl(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1348, in _cached_dispatch_impl
    output = self._dispatch_impl(func, types, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 2015, in _dispatch_impl
    return maybe_run_unsafe_fallback(not_implemented_error)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fake_tensor.py", line 1997, in maybe_run_unsafe_fallback
    raise UnsupportedOperatorException(func)
RuntimeError: Failed running call_function _C.rotary_embedding(*(FakeTensor(..., device='npu:0', size=(s1,), dtype=torch.int64), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), FakeTensor(..., device='npu:0', size=(s0, 4096), dtype=torch.float16), 128, FakeTensor(..., device='npu:0', size=(4096, 128), dtype=torch.float16), True), **{}):
_C.rotary_embedding.default

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 590, in run_engine_core
    raise e
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 577, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 404, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 82, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 142, in _initialize_kv_caches
    available_gpu_memory = self.model_executor.determine_available_memory()
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
    output = self.collective_rpc("determine_available_memory")
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/utils/__init__.py", line 2736, in run_method
    return func(*args, **kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 146, in determine_available_memory
    self.model_runner.profile_run()
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1700, in profile_run
    hidden_states = self._dummy_run(self.max_num_tokens)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1684, in _dummy_run
    hidden_states = model(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llava.py", line 759, in forward
    hidden_states = self.language_model.model(input_ids,
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 239, in __call__
    output = self.compiled_callable(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 1269, in __call__
    return self._torchdynamo_orig_callable(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 526, in __call__
    return _compile(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 924, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 666, in compile_inner
    return _compile_inner(code, one_graph, hooks, transform)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_utils_internal.py", line 87, in wrapper_function
    return function(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 699, in _compile_inner
    out_code = transform_code_object(code, transform)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/bytecode_transformation.py", line 1322, in transform_code_object
    transformations(instructions, code_options)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 219, in _fn
    return fn(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 634, in transform
    tracer.run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2796, in run
    super().run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
    while self.step():
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
    return inner_fn(self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
    self.call_function(fn, args, {})
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
    self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
    return variables.UserFunctionVariable(fn, source=source).call_function(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
    return super().call_function(tx, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
    return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
    return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
    return inline_call(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
    return cls.inline_call_(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
    tracer.run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
    while self.step():
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
    return inner_fn(self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1692, in CALL_FUNCTION_KW
    self.call_function(fn, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
    self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
    return getattr(self.realize(), name)(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
    return variables.UserFunctionVariable(fn, source=source).call_function(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
    return super().call_function(tx, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
    return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
    return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
    return inline_call(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
    return cls.inline_call_(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
    tracer.run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
    while self.step():
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
    return inner_fn(self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
    self.call_function(fn, args, {})
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
    self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/lazy.py", line 156, in realize_and_forward
    return getattr(self.realize(), name)(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/nn_module.py", line 899, in call_function
    return variables.UserFunctionVariable(fn, source=source).call_function(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
    return super().call_function(tx, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
    return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
    return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
    return inline_call(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
    return cls.inline_call_(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
    tracer.run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
    while self.step():
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
    return inner_fn(self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1680, in CALL_FUNCTION_EX
    self.call_function(fn, argsvars.items, kwargsvars)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
    self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 385, in call_function
    return super().call_function(tx, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 324, in call_function
    return super().call_function(tx, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/functions.py", line 111, in call_function
    return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 836, in inline_user_function_return
    return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/compilation/decorators.py", line 235, in patched_inline_call
    return inline_call(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3011, in inline_call
    return cls.inline_call_(parent, func, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 3139, in inline_call_
    tracer.run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 983, in run
    while self.step():
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 895, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 582, in wrapper
    return inner_fn(self, inst)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 1602, in CALL_FUNCTION
    self.call_function(fn, args, {})
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 830, in call_function
    self.push(fn.call_function(self, args, kwargs))  # type: ignore[arg-type]
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/torch.py", line 897, in call_function
    tensor_variable = wrap_fx_proxy(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2037, in wrap_fx_proxy
    return wrap_fx_proxy_cls(target_cls=TensorVariable, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/variables/builder.py", line 2124, in wrap_fx_proxy_cls
    example_value = get_fake_value(proxy.node, tx, allow_non_graph_fake=True)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/utils.py", line 2064, in get_fake_value
    unimplemented(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/exc.py", line 297, in unimplemented
    raise Unsupported(msg, case_name=case_name)
torch._dynamo.exc.Unsupported: unsupported operator: _C.rotary_embedding.default (see https://docs.google.com/document/d/1GgvOe7C8_NVOMLOCwDaYV1mXXyHMXY7ExoewHqooxrs/edit#heading=h.64r4npvq0w0 for how to fix)

from user code:
   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 392, in forward
    hidden_states, residual = layer(positions, hidden_states, residual)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 305, in forward
    hidden_states = self.self_attn(positions=positions,
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/llama.py", line 202, in forward
    q, k = self.rotary_emb(positions, q, k)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/custom_op.py", line 44, in forward
    return self._forward_method(*args, **kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 62, in rope_forward_oot
    query, key = torch.ops._C.rotary_embedding(

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

^C
root@linux-arm64-npu-2-qn9f9-runner-xn2kw-workflow:/__w/vllm-benchmarks/vllm-benchmarks# Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/cli/main.py", line 65, in main
    args.dispatch_function(args)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/cli/serve.py", line 55, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/async_llm.py", line 162, in from_vllm_config
    return cls(
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/async_llm.py", line 124, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core_client.py", line 96, in make_async_mp_client
    return AsyncMPClient(*client_args)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core_client.py", line 666, in __init__
    super().__init__(
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core_client.py", line 403, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/utils.py", line 434, in launch_core_engines
    wait_for_engine_startup(
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/utils.py", line 484, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-07-23-07:21:58 (PID:9058, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
^
```
