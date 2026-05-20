# Issue #1156: [Bug]: ModuleNotFoundError: No module named 'vllm_ascend.compilation'

## 基本信息

- **编号**: #1156
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1156
- **创建时间**: 2025-06-10T10:16:34Z
- **关闭时间**: 2025-06-10T10:24:05Z
- **更新时间**: 2025-06-10T10:34:19Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

VLLM_USE_V1=1 VLLM_USE_MODELSCOPE=true python3 -m vllm.entrypoints.openai.api_server --model $MODEL

pip install vllm-ascend==v0.9.0rc1

### 🐛 Describe the bug


```
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 1446, in _call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/repro/after_dynamo.py", line 129, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/repro/after_dynamo.py", line 129, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/__init__.py", line 2279, in __call__
    return self.compiler_fn(model_, inputs_, **self.kwargs)
  File "/vllm-workspace/vllm/vllm/compilation/backends.py", line 498, in __call__
    PiecewiseCompileInterpreter(self.split_gm, submod_names_to_compile,
  File "/vllm-workspace/vllm/vllm/compilation/backends.py", line 273, in run
    return super().run(*fake_args)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/interpreter.py", line 146, in run
    self.env[node] = self.run_node(node)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/interpreter.py", line 203, in run_node
    return getattr(self, n.op)(n.target, args, kwargs)
  File "/vllm-workspace/vllm/vllm/compilation/backends.py", line 298, in call_module
    piecewise_backend = resolve_obj_by_qualname(
  File "/vllm-workspace/vllm/vllm/utils.py", line 2191, in resolve_obj_by_qualname
    module = importlib.import_module(module_name)
  File "/usr/local/python3.10.17/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'vllm_ascend.compilation'
```
