# Issue #540: [Bug]: RuntimeError: Failed to infer device type

## 基本信息

- **编号**: #540
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/540
- **创建时间**: 2025-04-16T06:00:45Z
- **关闭时间**: 2025-04-20T12:08:29Z
- **更新时间**: 2025-04-20T12:08:29Z
- **提交者**: @RyanOvO
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

环境信息：
CANN：8.0.RC2.2

Name: vllm
Version: 0.7.3+empty

Name: vllm_ascend
Version: 0.7.3rc2

Name: torch-npu
Version: 2.5.1.dev20250308

脚本：
```
# 修改 ascend-toolkit 路径
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh

vllm serve /home/hwtest/DeepSeek-R1-Distill-Qwen-32B/mg2hf/ --max-model-len 4096 --port 8000 -tp 4
```




### 🐛 Describe the bug

```text
RuntimeError: Failed to infer device type
[ERROR] 2025-04-16-13:55:33 (PID:2867459, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 04-16 13:55:44 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-16 13:55:44 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-16 13:55:44 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-16 13:55:44 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
ERROR 04-16 13:55:44 __init__.py:46] Failed to load plugin ascend
ERROR 04-16 13:55:44 __init__.py:46] Traceback (most recent call last):
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/plugins/__init__.py", line 42, in load_plugins_by_group
ERROR 04-16 13:55:44 __init__.py:46]     func = plugin.load()
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/importlib/metadata/__init__.py", line 171, in load
ERROR 04-16 13:55:44 __init__.py:46]     module = import_module(match.group('module'))
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/importlib/__init__.py", line 126, in import_module
ERROR 04-16 13:55:44 __init__.py:46]     return _bootstrap._gcd_import(name[level:], package, level)
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ERROR 04-16 13:55:44 __init__.py:46] ModuleNotFoundError: No module named 'vllm_ascend'
INFO 04-16 13:55:44 __init__.py:211] No platform detected, vLLM is running on UnspecifiedPlatform
INFO 04-16 13:55:44 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-16 13:55:44 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-16 13:55:44 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-16 13:55:44 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
ERROR 04-16 13:55:44 __init__.py:46] Failed to load plugin ascend_enhanced_model
ERROR 04-16 13:55:44 __init__.py:46] Traceback (most recent call last):
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/plugins/__init__.py", line 42, in load_plugins_by_group
ERROR 04-16 13:55:44 __init__.py:46]     func = plugin.load()
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/importlib/metadata/__init__.py", line 171, in load
ERROR 04-16 13:55:44 __init__.py:46]     module = import_module(match.group('module'))
ERROR 04-16 13:55:44 __init__.py:46]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/importlib/__init__.py", line 126, in import_module
ERROR 04-16 13:55:44 __init__.py:46]     return _bootstrap._gcd_import(name[level:], package, level)
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 04-16 13:55:44 __init__.py:46]   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ERROR 04-16 13:55:44 __init__.py:46] ModuleNotFoundError: No module named 'vllm_ascend'
ERROR 04-16 13:55:44 engine.py:400] Failed to infer device type
ERROR 04-16 13:55:44 engine.py:400] Traceback (most recent call last):
ERROR 04-16 13:55:44 engine.py:400]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 04-16 13:55:44 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 04-16 13:55:44 engine.py:400]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args
ERROR 04-16 13:55:44 engine.py:400]     engine_config = engine_args.create_engine_config(usage_context)
ERROR 04-16 13:55:44 engine.py:400]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1126, in create_engine_config
ERROR 04-16 13:55:44 engine.py:400]     device_config = DeviceConfig(device=self.device)
ERROR 04-16 13:55:44 engine.py:400]   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/config.py", line 1660, in __init__
ERROR 04-16 13:55:44 engine.py:400]     raise RuntimeError("Failed to infer device type")
ERROR 04-16 13:55:44 engine.py:400] RuntimeError: Failed to infer device type
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 119, in from_engine_args
    engine_config = engine_args.create_engine_config(usage_context)
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1126, in create_engine_config
    device_config = DeviceConfig(device=self.device)
  File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/config.py", line 1660, in __init__
    raise RuntimeError("Failed to infer device type")
RuntimeError: Failed to infer device type
```


