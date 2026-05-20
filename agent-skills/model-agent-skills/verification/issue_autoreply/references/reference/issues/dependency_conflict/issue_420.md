# Issue #420: [Bug]: AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'

## 基本信息

- **编号**: #420
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/420
- **创建时间**: 2025-03-28T06:29:03Z
- **关闭时间**: 2025-05-14T03:07:38Z
- **更新时间**: 2025-05-14T03:07:39Z
- **提交者**: @rfy48
- **评论数**: 6

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

When I ran the script below，it returned the error:
 AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'

![Image](https://github.com/user-attachments/assets/34b6603b-1782-4c4d-90a8-5592e7a44ffa)

version:

![Image](https://github.com/user-attachments/assets/1302e9dd-21d4-493a-a963-eada92800733)
