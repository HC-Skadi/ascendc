# Issue #2726: [Bug]:

## 基本信息

- **编号**: #2726
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2726
- **创建时间**: 2025-09-03T08:45:52Z
- **关闭时间**: 2025-12-22T03:09:31Z
- **更新时间**: 2025-12-22T03:09:31Z
- **提交者**: @yangqinghao-cmss
- **评论数**: 0

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

这是不是已经图编译成功了，kv cache 都出来了：
<img width="1420" height="561" alt="Image" src="https://github.com/user-attachments/assets/09160991-4dd1-4f13-9e15-749528933596" />
可是怎么突然 torch 的 add norm 怎么就报错了：

<img width="1430" height="658" alt="Image" src="https://github.com/user-attachments/assets/03ca30ba-4cc0-4e8b-84de-32eb284ba203" />

 
