# Issue #340: [Bug]: AttributeError: module 'torch_npu' has no attribute '_npu_flash_attention'

## 基本信息

- **编号**: #340
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/340
- **创建时间**: 2025-03-16T03:36:21Z
- **关闭时间**: 2025-03-31T15:45:30Z
- **更新时间**: 2025-03-31T15:45:30Z
- **提交者**: @geekchen007
- **评论数**: 10

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```
torch                                    2.5.1
torch-npu                                2.5.1rc1
torchaudio                               2.5.1
torchvision                              0.20.1
```

---

```text
Your output of above commands here
```

</details>

```
[rank0]:   File "/home/xxx/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm/attention/layer.py", line 198, in forward
[rank0]:     return self.impl.forward(self, query, key, value,
[rank0]:   File "/home/xxx/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/attention.py", line 845, in forward
[rank0]:     torch_npu._npu_flash_attention(
[rank0]: AttributeError: module 'torch_npu' has no attribute '_npu_flash_attention'
[ERROR] 2025-03-16-11:32:36 (PID:80511, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```


### 🐛 Describe the bug

```
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
from qwen_vl_utils import process_vision_info

MODEL_PATH = "Qwen/Qwen2.5-VL-7B-Instruct"

llm = LLM(
    model=MODEL_PATH,
    max_model_len=16384,
    limit_mm_per_prompt={"image": 10},
)
```
