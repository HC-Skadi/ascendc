# Issue #2929: [Doc]: qwen3-next 启动服务失败

## 基本信息

- **编号**: #2929
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2929
- **创建时间**: 2025-09-15T08:04:53Z
- **关闭时间**: 2025-09-15T10:11:46Z
- **更新时间**: 2025-09-15T10:11:46Z
- **提交者**: @danielchao001
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] Error in inspecting model architecture 'Qwen3NextForCausalLM'
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] Traceback (most recent call last):
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 867, in _run_in_subprocess
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     returned.check_returncode()
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/subprocess.py", line 502, in check_returncode
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     raise CalledProcessError(self.returncode, self.args, self.stdout,
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] subprocess.CalledProcessError: Command '['/usr/local/python3.11.13/bin/python3', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1.
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] The above exception was the direct cause of the following exception:
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] Traceback (most recent call last):
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 447, in _try_inspect_model_cls
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     return model.inspect_model_cls()
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 418, in inspect_model_cls
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     return _run_in_subprocess(
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 870, in _run_in_subprocess
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     raise RuntimeError(f"Error raised in subprocess:\n"
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] RuntimeError: Error raised in subprocess:
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] <frozen runpy>:128: RuntimeWarning: 'vllm.model_executor.models.registry' found in sys.modules after import of package 'vllm.model_executor.models', but prior to execution of 'vllm.model_executor.models.registry'; this may result in unpredictable behaviour
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] Traceback (most recent call last):
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 891, in <module>
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     _run()
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 884, in _run
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     result = fn()
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]              ^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 419, in <lambda>
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     lambda: _ModelInfo.from_model_cls(self.load_model_cls()))
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]                                       ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 422, in load_model_cls
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     mod = importlib.import_module(self.module_name)
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/importlib/__init__.py", line 126, in import_module
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     return _bootstrap._gcd_import(name[level:], package, level)
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]   File "/home/gch/vllm-ascend-main/vllm_ascend/models/qwen3_next.py", line 61, in <module>
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]     from .interfaces import (HasInnerState, IsHybrid, MixtureOfExperts,
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449] ModuleNotFoundError: No module named 'vllm_ascend.models.interfaces'
(APIServer pid=4121) ERROR 09-15 08:02:41 [registry.py:449]


### Suggest a potential alternative/fix

_No response_
