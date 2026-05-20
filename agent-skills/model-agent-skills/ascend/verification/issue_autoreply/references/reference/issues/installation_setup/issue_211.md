# Issue #211: [Bug]: module 'torch_npu' has no attribute '_npu_flash_attention'

## 基本信息

- **编号**: #211
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/211
- **创建时间**: 2025-03-01T09:26:00Z
- **关闭时间**: 2025-03-04T06:44:09Z
- **更新时间**: 2025-03-04T06:44:10Z
- **提交者**: @pjgao
- **评论数**: 4

## 标签

documentation

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250218
```

</details>


### 🐛 Describe the bug

执行下面脚本报错：
```bash
vllm serve ./Qwen2-VL-7B-Instruct --trust-remote-code
```
日志：
```bash
 File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 243, in forward
    hidden_states = self.self_attn(
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 177, in forward
    attn_output = self.attn(q, k, v)
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/attention/layer.py", line 220, in forward
    return self.impl.forward(self, query, key, value,
  File "/home/data//rl/vllm-ascend/vllm_ascend/attention.py", line 597, in forward
    torch_npu._npu_flash_attention(
AttributeError: module 'torch_npu' has no attribute '_npu_flash_attention'

```
问题原因：
https://github.com/vllm-project/vllm-ascend/pull/187   这个PR合入后torch_npu的版本依赖从 2.5.1.dev20250218更新到了2.5.1.dev20250226 ，但readme以及安装文档中未同步修改，导致按照readme以及https://vllm-ascend.readthedocs.io/en/latest/installation.html  这个文档说明安装 2.5.1.dev20250218 版本报错
