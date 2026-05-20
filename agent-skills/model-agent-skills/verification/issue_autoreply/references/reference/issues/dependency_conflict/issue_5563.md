# Issue #5563: [Bug]: no module named 'flash_attn.ops'

## 基本信息

- **编号**: #5563
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5563
- **创建时间**: 2026-01-03T04:08:35Z
- **关闭时间**: 2026-01-29T03:28:25Z
- **更新时间**: 2026-01-29T03:28:25Z
- **提交者**: @wuruichill
- **评论数**: 1

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

 我的环境为，vllm 0.13.0 + vllm-ascend 0.13.0rc1 + torch_npu 2.8.0

<img width="1530" height="424" alt="Image" src="https://github.com/user-attachments/assets/8952b0d1-1b98-4d94-ab2f-5f1c3b5e685d" />

我的推理demo为：
`import os
import torch
import torch_npu
from vllm import LLM, SamplingParams
from transformers import Qwen3OmniMoeProcessor
from qwen_omni_utils import process_mm_info

if __name__ == '__main__':
    os.environ['VLLM_USE_V1'] = '1'

    MODEL_PATH = "/mnt/bn/mmlab-audio-codec-hl/wurui/qwen3-omni/Qwen3-Omni-30B-A3B-Instruct"

    print(f"Initializing vLLM engine on NPU with model: {MODEL_PATH}...")
    llm = LLM(
            model=MODEL_PATH,
            trust_remote_code=True,
            gpu_memory_utilization=0.95,
            tensor_parallel_size=torch.npu.device_count(),
    )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        max_tokens=512, 
    )

    processor = Qwen3OmniMoeProcessor.from_pretrained(MODEL_PATH)

    print("\nPreparing multi-modal inputs...")
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cars.jpg"},
                {"type": "audio", "audio": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Omni/demo/cough.wav"},
                {"type": "text", "text": "What can you see and hear? Answer in one short sentence."}
            ],
        },
    ]
    
    USE_AUDIO_IN_VIDEO_FLAG = True

    prompt_text = processor.apply_chat_template(
        conversation, 
        add_generation_prompt=True, 
        tokenize=False
    )
    print("Prompt generated.")
    print("Downloading and processing raw image/audio data...")
    audios_raw, images_raw, videos_raw = process_mm_info(conversation, use_audio_in_video=USE_AUDIO_IN_VIDEO_FLAG)

    vllm_inputs = {
        'prompt': prompt_text,
        'multi_modal_data': {},
        "mm_processor_kwargs": {
            "use_audio_in_video": USE_AUDIO_IN_VIDEO_FLAG,
        },
    }

    if images_raw:
        vllm_inputs['multi_modal_data']['image'] = images_raw
    if audios_raw:
        vllm_inputs['multi_modal_data']['audio'] = audios_raw
    print("\nGenerating response on NPU...")
    outputs = llm.generate([vllm_inputs], sampling_params=sampling_params)
    generated_text = outputs[0].outputs[0].text

    print("\n" + "="*50)
    print("Generated Text Output:")
    print("="*50)
    print_text = generated_text.strip()
    print(print_text)
    print("="*50)`

然后就报错：

<img width="1280" height="695" alt="Image" src="https://github.com/user-attachments/assets/e88a7d9d-1867-42d5-a72d-d42bd33bb159" />

我的解决方案为：

<img width="1280" height="852" alt="Image" src="https://github.com/user-attachments/assets/796154f6-1fc7-41f1-b73f-7c8429270614" />

<img width="1280" height="846" alt="Image" src="https://github.com/user-attachments/assets/11e09440-a776-4fd0-8fcd-f06d58040922" />

所以我在想，这里是不是需要做一些适配，因为我实测下来，这部分代码注释，对NPU推理完全无影响，所以只是依赖导入有问题？ 
