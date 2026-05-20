# Issue #3342: [Bug]: Custom kernels fail to compile without raising any errors

## 基本信息

- **编号**: #3342
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3342
- **创建时间**: 2025-10-09T10:38:46Z
- **关闭时间**: 2025-10-30T07:53:16Z
- **更新时间**: 2025-10-30T07:53:16Z
- **提交者**: @yiz-liu
- **评论数**: 0

## 标签

bug; guide

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

None.

</details>


### 🐛 Describe the bug

# Description

This is a long-standing problem: in some scenarios compilation fails but the installation still succeeds. This causes several hard-to-explain issues:

1. Graph mode becomes unusable — without `weak_ref_tensor` we can't free the intermediate tensors created during graph capture.
```
AttributeError: '_OpNamespace' '_C_ascend' object has no attribute 'weak_ref_tensor'
```
3. LoRA is affected too, because its `bgmv` kernels are custom kernels.
4. Other potential problems.

# Validation

```python
import torch
import vllm
import vllm_ascend.vllm_ascend_C

torch.ops._C_ascend.weak_ref_tensor
```

If custom kernels weren't compiled, this will raise errors.

# Workaround
 Double check the installation process and make sure you follow the guide, validate your installation with the methods mentioned above.

# Reproduction

There are multiple ways to trigger this. For example, manually changing the `torch_npu` version in `requirements.txt` can cause it.

# Suggestion

@wangxiyuan , I suggest we take a look and make sure compilation failures produce visible errors. Could you assign someone to investigate and arrange a fix?

