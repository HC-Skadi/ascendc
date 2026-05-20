# Issue #3338: [Usage]: vllm-ascend不支持torch.arrange算子

## 基本信息

- **编号**: #3338
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3338
- **创建时间**: 2025-10-09T08:29:52Z
- **关闭时间**: 2025-10-13T08:44:16Z
- **更新时间**: 2025-10-14T06:25:54Z
- **提交者**: @cyber-taico
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
v0.11.0rc0和v0.11.0rc0-a3都不支持torch.arrange算子，可能导致很多模型拉起失败


```text

```

</details>


### 🐛 Describe the bug

<img width="1441" height="405" alt="Image" src="https://github.com/user-attachments/assets/7c168169-e2f1-4ae5-a52b-694a8f5a87cb" />

执行脚本报错，RuntimeError: arange_out_op_api:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:36 NPU function error: call aclnnArange failed, error code is 561103

```python
#!/usr/bin/env python3
"""
test_arange.py
快速验证 torch.arange 在不同参数下的行为
"""
import torch
import torch_npu


def test_basic():
    print("=== 1. 基本功能 ===")
    x = torch.arange(0, 5)          # 默认步长 1，int64
    y = torch.arange(0, 5, 0.5)     # 浮点步长
    print("x =", x, x.dtype)
    print("y =", y, y.dtype)

def test_dtype():
    print("\n=== 2. 指定 dtype ===")
    z = torch.arange(10, dtype=torch.float32)
    print("z =", z, z.dtype)



if __name__ == "__main__":
    with torch.device("npu:0"):
        test_basic()
        test_dtype()
        print("\n=== 所有测试跑完 ===")

```
