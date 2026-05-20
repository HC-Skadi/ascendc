# Issue #1615: [Bug]: Deepseekr1w8a8+torchair, T4P4 run failed

## 基本信息

- **编号**: #1615
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1615
- **创建时间**: 2025-07-03T11:06:00Z
- **关闭时间**: 2025-07-07T11:30:45Z
- **更新时间**: 2025-07-07T11:30:45Z
- **提交者**: @tt545571022
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
single machine 910B2C*16p
docker image:  vllm-ascend 0.9.1rc1
</details>


### 🐛 Describe the bug

I want to run deepseekr1-w8a8 on single machine 910B2C*16p，when I enable torchair，and set TP=4，PP=4，then run failed with as follow dynamo error：
```
     raise Unsupported(msg, case_name=case_name)
 torch._dynamo.exc.Unsupported: call_function DelayGraphBreakVariable() [TensorVariable()] {}
 
 from user code:
    File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 753, in forward
     hidden_states = self.model(input_ids, positions, kv_caches,
   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 700, in forward
     hidden_states, residual = layer(
   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 590, in forward
     dispose_tensor(previous_hidden_states)
   File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 330, in dispose_tensor
     x.set_(torch.empty((0, ), device=x.device, dtype=x.dtype))
```
the py script is as follows：
```python
import os

from vllm import LLM, SamplingParams

os.environ["VLLM_USE_V1"] = "1"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

if __name__ == "__main__":
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=1024, temperature=0.0)
    # Create an LLM.
    llm = LLM(
        # model="/data/weight/deepseek_weights_7b",
        model="/home/tjl/DeepSeek-R1-W8A8",
              tensor_parallel_size=4,
              pipeline_parallel_size=4,
            #   enforce_eager=True,
              trust_remote_code=True,
              max_model_len=1024,
              quantization="ascend",
              additional_config={
              "torchair_graph_config": {"enabled": True, "enable_multistream_mla": True, "enable_multistream_moe": True},
              "ascend_scheduler_config": {"enabled": True, "enable_chunked_prefill": False,},
              }
              )

    # Generate texts from the prompts.
    for i in range(55):
        print(f"Iteration {i + 1}")
        outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

```
