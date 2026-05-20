# Issue #449: [Bug]: 在910b部署vllm-ascend的时候，当启用v1引擎、设置使用的npu卡为非0~n的连续卡时，会报错显示AssertionError: Invalid device id

## 基本信息

- **编号**: #449
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/449
- **创建时间**: 2025-03-31T12:16:39Z
- **关闭时间**: 2025-05-14T03:11:44Z
- **更新时间**: 2025-05-14T03:11:46Z
- **提交者**: @xsbl233
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

昇腾910B4
python3.11
ubuntu22.04
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,5

### 🐛 Describe the bug

<details>
<summary>sample执行程序和输出结果</summary>

```python
if __name__ == '__main__':
    from vllm import LLM, SamplingParams

    prompts = ['San Francisco is a'*2]*10

    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=5, temperature=0.0)
    # Create an LLM.
    llm = LLM(model="/home/data/models/meta-llama/LLaMA3-8B", tensor_parallel_size=1)

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```



```bash
Traceback (most recent call last):
  File "/home/fb/run/sample.py", line 9, in <module>
    llm = LLM(model="/home/data/models/meta-llama/LLaMA3-8B", tensor_parallel_size=1)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/vllm/utils.py", line 1022, in inner
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 242, in __init__
    self.llm_engine = self.engine_class.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/vllm/v1/engine/llm_engine.py", line 90, in from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/vllm/engine/arg_utils.py", line 1100, in create_engine_config
    self._override_v1_engine_args(usage_context)
  File "/usr/local/lib/python3.11/site-packages/vllm/engine/arg_utils.py", line 1367, in _override_v1_engine_args
    device_name = current_platform.get_device_name().lower()
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/fb/vllm-ascend/vllm_ascend/platform.py", line 94, in get_device_name
    return torch.npu.get_device_name(physical_device_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 70, in get_device_name
    raise AssertionError("Invalid device id" + pta_error(ErrCode.VALUE))
AssertionError: Invalid device id

```

</details>

检查后似乎是vllm-ascend中有获取到的npu数量是设置可用的数量，传入的device_id是对应的物理id，如设置卡为0,1,2,7，则device_count() = 4，会在判定id为7的卡的时候认为7>4而返回错误
