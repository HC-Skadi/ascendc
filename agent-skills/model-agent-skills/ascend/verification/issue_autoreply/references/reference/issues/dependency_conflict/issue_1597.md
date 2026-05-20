# Issue #1597: [Bug]: In scenarios involving DP partitioning or combined DP+TP partitioning, executing other MOE models from clients may lead to accuracy issues, manifested as responses keep repeating.

## 基本信息

- **编号**: #1597
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1597
- **创建时间**: 2025-07-02T15:08:55Z
- **关闭时间**: 2025-07-14T08:38:47Z
- **更新时间**: 2025-07-14T08:38:47Z
- **提交者**: @leograssroot
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
环境信息参考这个issue：https://github.com/vllm-project/vllm-ascend/issues/1558
```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

参考https://github.com/vllm-project/vllm-ascend/issues/1558
dp切分精度有问题，单独只切tp精度ok
