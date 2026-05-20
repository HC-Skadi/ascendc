# Issue #445: [Bug]: 910b部署qwen2.5-vl-72b输出有时候会出现全部为感叹号的情况

## 基本信息

- **编号**: #445
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/445
- **创建时间**: 2025-03-31T08:50:39Z
- **关闭时间**: 2025-04-27T13:10:42Z
- **更新时间**: 2025-04-27T13:10:43Z
- **提交者**: @Huang-zhenxuan
- **评论数**: 13

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

vllm serve /root/model/qwen_2_5_vl --max-model-len 32768 --port 11025 -tp 8 --seed 42  --gpu_memory_utilization 0.97   

输出出现如下图所示：

![Image](https://github.com/user-attachments/assets/af4643a7-b4cb-41c3-9808-b9013feffb6e)
