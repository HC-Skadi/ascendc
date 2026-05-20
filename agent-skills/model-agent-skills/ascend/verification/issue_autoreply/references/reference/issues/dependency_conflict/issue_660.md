# Issue #660: [Bug]: [Spec Decode] MLP and ngram spec deocde mode run failed

## 基本信息

- **编号**: #660
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/660
- **创建时间**: 2025-04-25T17:51:34Z
- **关闭时间**: 2025-04-30T08:05:32Z
- **更新时间**: 2025-04-30T08:05:32Z
- **提交者**: @mengwei805
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm main and vllm-ascend main


add notes:
vllm c53e0730cb9cffa27c9a11c5489eb771b6865f6b and vllm-ascend 3879d9cad95c14e3cce8fc053540e369a39cd341 failed

vllm 6317a5174a4f3cbd57c44d15023042cecc576f9e and vllm-ascend 5c6d05a59e996ab0ce6b91e7d4e267d7be1157f8 success
```

</details>


### 🐛 Describe the bug

mlp mode and ngram mode run failed 
