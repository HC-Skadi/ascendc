# Issue #2889: [Bug]: 使用main-openeuler镜像，运行Qwen3-Next-80B-A3B-Instruct模型失败报错

## 基本信息

- **编号**: #2889
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2889
- **创建时间**: 2025-09-12T09:23:09Z
- **关闭时间**: 2025-09-12T09:50:24Z
- **更新时间**: 2025-09-12T09:52:19Z
- **提交者**: @MaoJianwei
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

参考官网，如下启动vllm serve
https://modelscope.cn/models/Qwen/Qwen3-Next-80B-A3B-Instruct/summary
```
export VLLM_USE_V1=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export enforce_eager=True

export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
vllm serve /llm_data2/Qwen3-Next-80B-A3B-Instruct/ --served-model-name Qwen3-Next-80B-A3B-Instruct \
     --port 8000 --tensor-parallel-size 8 --gpu-memory-utilization 0.9 \
     --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}'

```

如果不使用MTP（不加--speculative-config参数），也会报错，错误信息相同。



根据版本号中的commit ID（12a8414），这个vLLM仓的main分支是支持运行Qwen3-Next模型的，只是vllm-ascend当前有问题。
```
 vLLM API server version 0.1.dev1+g12a8414d8
```

### 🐛 Describe the bug

```
(APIServer pid=883) INFO 09-12 09:11:42 [api_server.py:1896] vLLM API server version 0.1.dev1+g12a8414d8                                                                                                                                                        [77/1102]
(APIServer pid=883) INFO 09-12 09:11:42 [utils.py:328] non-default args: {'model_tag': '/llm_data2/Qwen3-Next-80B-A3B-Instruct/', 'model': '/llm_data2/Qwen3-Next-80B-A3B-Instruct/', 'served_model_name': ['Qwen3-Next-80B-A3B-Instruct'], 'tensor_parallel_size': 8, 's
peculative_config': {'method': 'qwen3_next_mtp', 'num_speculative_tokens': 2}}
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] Error in inspecting model architecture 'Qwen3NextForCausalLM'
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] Traceback (most recent call last):
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 867, in _run_in_subprocess
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     returned.check_returncode()
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/subprocess.py", line 502, in check_returncode
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     raise CalledProcessError(self.returncode, self.args, self.stdout,
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] subprocess.CalledProcessError: Command '['/usr/local/python3.11.13/bin/python3', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1.
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] The above exception was the direct cause of the following exception:
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] Traceback (most recent call last):
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 447, in _try_inspect_model_cls
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     return model.inspect_model_cls()
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 418, in inspect_model_cls
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     return _run_in_subprocess(
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 870, in _run_in_subprocess
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     raise RuntimeError(f"Error raised in subprocess:\n"
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] RuntimeError: Error raised in subprocess:
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] <frozen runpy>:128: RuntimeWarning: 'vllm.model_executor.models.registry' found in sys.modules after import of package 'vllm.model_executor.models', but prior to execution of 'vllm.model_executor.models.reg
istry'; this may result in unpredictable behaviour
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] Traceback (most recent call last):
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 891, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     _run()
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 884, in _run
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     result = fn()
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]              ^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 419, in <lambda>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     lambda: _ModelInfo.from_model_cls(self.load_model_cls()))
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]                                       ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/registry.py", line 422, in load_model_cls
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     mod = importlib.import_module(self.module_name)
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/usr/local/python3.11.13/lib/python3.11/importlib/__init__.py", line 126, in import_module
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     return _bootstrap._gcd_import(name[level:], package, level)
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap_external>", line 940, in exec_module
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 23, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     from vllm.model_executor.layers.fla.ops import (
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fla/ops/__init__.py", line 9, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     from .chunk import chunk_gated_delta_rule
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fla/ops/chunk.py", line 16, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     from .chunk_delta_h import chunk_gated_delta_rule_fwd_h
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fla/ops/chunk_delta_h.py", line 17, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     from .op import exp
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fla/ops/op.py", line 26, in <module>
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]     exp = tl.exp
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]           ^^^^^^
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449] AttributeError: module 'triton.language' has no attribute 'exp'
(APIServer pid=883) ERROR 09-12 09:11:55 [registry.py:449]
(APIServer pid=883) Traceback (most recent call last):

```

```

```
