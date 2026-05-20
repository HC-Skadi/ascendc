# Issue #2885: [Bug]: test_custom_deepseek_v2_mlp failed under 8.3.RC1.alpha002

## 基本信息

- **编号**: #2885
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2885
- **创建时间**: 2025-09-12T06:38:02Z
- **关闭时间**: 2025-09-12T12:51:14Z
- **更新时间**: 2025-09-12T12:51:14Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17662776298/job/50199547607?pr=2880


### 🐛 Describe the bug

```
self = <torch.utils._device.DeviceContext object at 0x7f090d7d1f50>
func = <built-in method matmul of type object at 0x7f09c0786c20>, types = ()
args = (tensor([[[ 1.1147,  0.2011, -1.5971,  ..., -0.2831,  0.1326, -0.6125],
         [-1.1164, -0.8247, -0.9337,  ..., -0....  0.0000e+00],
        [ 0.0000e+00,  0.0000e+00,  0.0000e+00,  ...,  0.0000e+00,
          0.0000e+00,  0.0000e+00]]))
kwargs = {}

    def __torch_function__(self, func, types, args=(), kwargs=None):
        kwargs = kwargs or {}
        if func in _device_constructors() and kwargs.get('device') is None:
            kwargs['device'] = self.device
>       return func(*args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^
E       RuntimeError: mat1 and mat2 shapes cannot be multiplied (8x128 and 512x128)
```
