# Issue #412: [Bug]: Ray launch offline inference stuck

## 基本信息

- **编号**: #412
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/412
- **创建时间**: 2025-03-27T10:37:05Z
- **关闭时间**: 2025-06-11T06:19:35Z
- **更新时间**: 2025-06-11T06:19:35Z
- **提交者**: @zxy-111122
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
cann8beta1 torch2.5.1 示例多卡跑qwenvl可以，使用ray的distributed backend报错

</details>


### 🐛 Describe the bug

vllm rlhf offline inference示例代码
https://docs.vllm.ai/en/latest/getting_started/examples/rlhf.html

```
import os

import ray
import torch
from ray.util.placement_group import placement_group
from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy
# from rlhf_utils import stateless_init_process_group
# from transformers import AutoModelForCausalLM

from vllm import LLM, SamplingParams
from vllm.utils import get_ip, get_open_port


class MyLLM(LLM):

    def __init__(self, *args, **kwargs):
        # a hack to make the script work.
        # stop ray from manipulating CUDA_VISIBLE_DEVICES
        # at the top-level
        devices=os.environ.get("ASCEND_RT_VISIBLE_DEVICES", None)
        print(f"!!!!!!!!!!!!!!!!devices: {devices}")
        # os.environ.pop("ASCEND_RT_VISIBLE_DEVICES", None)
        # os.environ["ASCEND_RT_VISIBLE_DEVICES"] = "3,4"
        # os.environ["VLLM_RAY_PER_WORKER_GPUS"] = "0"
        # os.environ["VLLM_RAY_BUNDLE_INDICES"] = "3,4"
        super().__init__(*args, **kwargs)
        print("!!!!!!!!!!!!MyLLM init success")


"""
Start the training process, here we use huggingface transformers 
as an example to hold a model on GPU 0.
"""

# train_model = AutoModelForCausalLM.from_pretrained("facebook/opt-125m")
# train_model.to("cuda:0")
"""
Start the inference process, here we use vLLM to hold a model on GPU 1 and 
GPU 2. For the details on how to use ray, please refer to the ray 
documentation https://docs.ray.io/en/latest/ .
"""
# os.environ["RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES"]="1"
os.environ["ASCEND_RT_VISIBLE_DEVICES"] = "3,4"
ray.init()

pg_inference = placement_group([{"NPU": 1, "CPU": 0}] * 2)
ray.get(pg_inference.ready())
scheduling_inference = PlacementGroupSchedulingStrategy(
    placement_group=pg_inference,
    placement_group_capture_child_tasks=True,
    placement_group_bundle_index=0,
)
"""
launch the vLLM inference engine.
here we use `enforce_eager` to reduce the start time.
"""
llm = ray.remote(
    num_cpus=0,
    num_gpus=0,
    scheduling_strategy=scheduling_inference,
    runtime_env={"env_vars": {"ASCEND_RT_VISIBLE_DEVICES":"3,4"}}
)(MyLLM).remote(
    model="/home/ma-user/work/dataset/checkpointsulan/Qwen2.5-VL-3B-Instruct",
    enforce_eager=True,
    tensor_parallel_size=2,
    distributed_executor_backend="ray"
)
print("!!!!!!!!!!!!!!!!!!!succeed to init llm engine")
# Generate texts from the prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

sampling_params = SamplingParams(temperature=0)

outputs = ray.get(llm.generate.remote(prompts, sampling_params))

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, "
          f"Generated text: {generated_text!r}")
```

如果不使用RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES，会报getdevice错误
如果使用RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES 并且设置ASCEND_RT_VISIBLE_DEVICES 会卡死
```
(NPURayWorkerWrapper pid=3190927)   warnings.warn(msg, RuntimeWarning)
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:04<00:04,  4.18s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:07<00:00,  3.83s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:07<00:00,  3.88s/it]
(MyLLM pid=3180736) 
(MyLLM pid=3180736) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(NPURayWorkerWrapper pid=3190927) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
(NPURayWorkerWrapper pid=3190927) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(NPURayWorkerWrapper pid=3190927) .
(NPURayWorkerWrapper pid=3190927) INFO 03-27 17:41:43 config.py:3054] cudagraph sizes specified by model runner [] is overridden by config []
(MyLLM pid=3180736) /home/ma-user/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_5_vl.py:622: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
(MyLLM pid=3180736)   hidden_states = hidden_states[window_index, :, :]
(MyLLM pid=3180736) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
```

```
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 101.0       49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3405 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 98.3        48                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          64233/ 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 101.6       48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          64231/ 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 94.6        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 96.9        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 96.8        48                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3394 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 102.6       48                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 96.6        48                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| 1       0                 | 3180736       | rayMyLLM.__in            | 60889                   |
+===========================+===============+====================================================+
| 2       0                 | 3190927       | rayNPURayWork            | 60887                   |
+===========================+===============+====================================================+
```
有显存，但利用率没有，卡在LLM启动这里，看堆栈应该是有通信问题，能否帮忙解决？
