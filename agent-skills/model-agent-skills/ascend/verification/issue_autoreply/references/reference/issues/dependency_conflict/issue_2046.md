# Issue #2046: [doctest]: ValueError: 'aimv2' is already used by a Transformers config, pick another name

## 基本信息

- **编号**: #2046
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2046
- **创建时间**: 2025-07-27T00:24:43Z
- **关闭时间**: 2025-09-18T00:37:57Z
- **更新时间**: 2025-09-24T23:34:36Z
- **提交者**: @Yikun
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/16539763269/job/46779322335

### 🐛 Describe the bug
```
Traceback (most recent call last):
  File "/vllm-workspace/vllm-ascend/tests/e2e/../../examples/offline_inference_npu.py", line 26, in <module>
    from vllm import LLM, SamplingParams
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/__init__.py", line 12, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/engine/arg_utils.py", line 20, in <module>
    from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig,
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/config.py", line 38, in <module>
    from vllm.transformers_utils.config import (
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/transformers_utils/config.py", line 31, in <module>
    from vllm.transformers_utils.configs import (ChatGLMConfig, Cohere2Config,
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/transformers_utils/configs/__init__.py", line 26, in <module>
    from vllm.transformers_utils.configs.ovis import OvisConfig
  File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm/transformers_utils/configs/ovis.py", line 75, in <module>
    AutoConfig.register("aimv2", AIMv2Config)
  File "/tmp/vllm_venv/lib/python3.11/site-packages/transformers/models/auto/configuration_auto.py", line 1306, in register
    CONFIG_MAPPING.register(model_type, config, exist_ok=exist_ok)
  File "/tmp/vllm_venv/lib/python3.11/site-packages/transformers/models/auto/configuration_auto.py", line 993, in register
    raise ValueError(f"'{key}' is already used by a Transformers config, pick another name.")
ValueError: 'aimv2' is already used by a Transformers config, pick another name.
```
