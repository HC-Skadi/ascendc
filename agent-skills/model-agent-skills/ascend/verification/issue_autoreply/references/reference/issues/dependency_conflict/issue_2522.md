# Issue #2522: [Bug]: test_lm_eval_correctness failed: ImportError: cannot import name 'CUDAGraphMode' from 'vllm.config'

## 基本信息

- **编号**: #2522
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2522
- **创建时间**: 2025-08-25T07:50:51Z
- **关闭时间**: 2025-08-27T01:56:54Z
- **更新时间**: 2025-08-27T01:56:54Z
- **提交者**: @Yikun
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17201088581/job/48791678978

### 🐛 Describe the bug

```
tests/e2e/models/test_lm_eval_correctness.py:123: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/utils.py:422: in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/evaluator.py:196: in simple_evaluate
    lm = lm_eval.api.registry.get_model(model).create_from_arg_obj(
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/api/model.py:173: in create_from_arg_obj
    return cls(**arg_dict, **additional_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/models/vllm_causallms.py:107: in __init__
    self.model = LLM(**self.model_args)
                 ^^^^^^^^^^^^^^^^^^^^^^
vllm-empty/vllm/entrypoints/llm.py:243: in __init__
    engine_args = EngineArgs(
<string>:124: in __init__
    ???
vllm-empty/vllm/engine/arg_utils.py:449: in __post_init__
    load_general_plugins()
vllm-empty/vllm/plugins/__init__.py:81: in load_general_plugins
    func()
vllm_ascend/__init__.py:27: in register_model
    register_model()
vllm_ascend/models/__init__.py:7: in register_model
    from .deepseek_dbo import CustomDeepseekDBOForCausalLM  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm_ascend/models/deepseek_dbo.py:67: in <module>
    from vllm_ascend.models.deepseek_v2 import (CustomDeepseekV2MLP,
vllm_ascend/models/deepseek_v2.py:73: in <module>
    from vllm_ascend.ops.fused_moe import AscendFusedMoE
vllm_ascend/ops/__init__.py:20: in <module>
    import vllm_ascend.ops.common_fused_moe  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm_ascend/ops/common_fused_moe.py:27: in <module>
    from vllm_ascend.ops.fused_moe import fused_experts_moge, unified_fused_experts
vllm_ascend/ops/fused_moe.py:43: in <module>
    from vllm_ascend.ascend_forward_context import FusedMoEState
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    import math
    from contextlib import contextmanager
    from enum import Enum
    from typing import Any, Optional
    
    import torch
>   from vllm.config import CUDAGraphMode, VllmConfig
E   ImportError: cannot import name 'CUDAGraphMode' from 'vllm.config' (/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/config.py)
```
