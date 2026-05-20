# Issue #4960: [Bug]: qwen3-vl-235B-bf16 FULL_DECODE_ONLY + VLLM_ASCEND_ENABLE_NZ=1 压测报错问题

## 基本信息

- **编号**: #4960
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4960
- **创建时间**: 2025-12-12T08:07:09Z
- **关闭时间**: 2025-12-30T10:59:19Z
- **更新时间**: 2025-12-30T10:59:19Z
- **提交者**: @Levi-JQ
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

报错信息如下：
<img width="1837" height="638" alt="Image" src="https://github.com/user-attachments/assets/e42feaaf-c43d-4703-822d-c31b9fed3f32" />
由于w8a8权重同配置下没有报错，所以怀疑和NZ格式有关
验证和NZ格式有关：
（1）v0.11.0-dev分支加了这个PR https://github.com/vllm-project/vllm-ascend/pull/4495 可以解决
（2）验证使用export VLLM_ASCEND_ENABLE_NZ=0 也可以解决

怀疑是FULL_DECODE_ONLY和VLLM_ASCEND_ENABLE_NZ=1有冲突，报错位置在PA算子处
