# Issue #56: running of v0.7.1 problem

## 基本信息

- **编号**: #56
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/56
- **创建时间**: 2025-02-13T08:13:26Z
- **关闭时间**: 2025-02-21T03:39:55Z
- **更新时间**: 2025-02-21T03:39:57Z
- **提交者**: @hz0ne
- **评论数**: 11

## 标签

documentation

## 问题描述

base env: 
torch                             2.5.1+cpu
torch-npu                         2.5.1rc1
torch-optimizer                   0.3.0
torchaudio                        2.5.1+cpu
torchmetrics                      0.10.0
torchscale                        0.2.0
torchtext                         0.18.0+cpu
torchvision                       0.20.1+cpu

CANN                               8.0

install version branch:
vllm                      0.7.1
vllm-ascend        0.7.1-release 

when I running the vllm server, encounter `AttributeError: module 'torch_npu' has no attribute 'npu_rope'`

```
  File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 23, in forward
    return self._forward_method(*args, **kwargs)
  File "/home/admin/runtime_package/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 41, in rope_forward_oot
    torch_npu.npu_rope(
AttributeError: module 'torch_npu' has no attribute 'npu_rope'
Traceback (most recent call last):
  File "/opt/conda/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/opt/conda/lib/python3.10/site-packages/vllm/scripts.py", line 202, in main
    args.dispatch_function(args)
  File "/opt/conda/lib/python3.10/site-packages/vllm/scripts.py", line 42, in serve
    uvloop.run(run_server(args))
  File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
```



