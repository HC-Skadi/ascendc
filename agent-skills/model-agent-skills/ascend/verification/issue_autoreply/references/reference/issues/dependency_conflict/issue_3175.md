# Issue #3175: [CI]: AttributeError: module 'triton.language' has no attribute 'tensor'

## 基本信息

- **编号**: #3175
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3175
- **创建时间**: 2025-09-25T06:45:08Z
- **关闭时间**: 2025-09-27T05:21:25Z
- **更新时间**: 2025-09-27T05:21:25Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

```
ImportError while loading conftest '/__w/vllm-ascend/vllm-ascend/tests/e2e/conftest.py'.
tests/e2e/conftest.py:55: in <module>
    adapt_patch(True)
vllm_ascend/utils.py:254: in adapt_patch
    from vllm_ascend.patch import platform  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm_ascend/patch/platform/__init__.py:17: in <module>
    from vllm_ascend.patch.platform import patch_common  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm_ascend/patch/platform/patch_common/__init__.py:20: in <module>
    import vllm_ascend.patch.platform.patch_common.patch_multimodal_merge  # noqa
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vllm_ascend/patch/platform/patch_common/patch_multimodal_merge.py:21: in <module>
    from vllm.model_executor.models.utils import (_embedding_count_expression,
vllm-empty/vllm/model_executor/models/utils.py:17: in <module>
    from vllm.model_executor.model_loader.weight_utils import default_weight_loader
vllm-empty/vllm/model_executor/model_loader/__init__.py:12: in <module>
    from vllm.model_executor.model_loader.bitsandbytes_loader import (
vllm-empty/vllm/model_executor/model_loader/bitsandbytes_loader.py:25: in <module>
    from vllm.model_executor.layers.fused_moe import FusedMoE
vllm-empty/vllm/model_executor/layers/fused_moe/__init__.py:8: in <module>
    from vllm.model_executor.layers.fused_moe.layer import (
vllm-empty/vllm/model_executor/layers/fused_moe/layer.py:27: in <module>
    from vllm.model_executor.layers.fused_moe.fused_moe import (
vllm-empty/vllm/model_executor/layers/fused_moe/fused_moe.py:670: in <module>
    hidden_states_ptr: tl.tensor,
                       ^^^^^^^^^
E   AttributeError: module 'triton.language' has no attribute 'tensor'
```

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/17998863821/job/51203513826
