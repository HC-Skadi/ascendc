# Issue #718: [Bug]:  vllm_version = vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__'

## 基本信息

- **编号**: #718
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/718
- **创建时间**: 2025-04-29T02:54:30Z
- **关闭时间**: 2025-05-14T06:32:25Z
- **更新时间**: 2025-05-14T06:32:25Z
- **提交者**: @FrankMinions
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>  File "/workspace/vllm-ascend/vllm_ascend/__init__.py", line 28, in register_model
    if vllm_version_is("0.8.4"):
  File "/workspace/vllm-ascend/vllm_ascend/utils.py", line 94, in vllm_version_is
    vllm_version = vllm.__version__
AttributeError: module 'vllm' has no attribute '__version__'</summary>

```text
vllm-ascend多处报错，提示vllm部分包找不到，或无此方法
```

</details>


### 🐛 Describe the bug

 File "/workspace/vllm-ascend/vllm_ascend/__init__.py", line 28, in register_model
    if vllm_version_is("0.8.4"):
  File "/workspace/vllm-ascend/vllm_ascend/utils.py", line 94, in vllm_version_is
    vllm_version = vllm.__version__
AttributeError: module 'vllm' has no attribute '__version__'</summary>
