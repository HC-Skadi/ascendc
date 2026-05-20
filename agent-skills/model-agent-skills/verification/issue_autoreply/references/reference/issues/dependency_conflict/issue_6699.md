# Issue #6699: [Bug]: Qwen3-Omni-30B-A3B-Thinking 运行音频转写任务，文本随机或者为空

## 基本信息

- **编号**: #6699
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6699
- **创建时间**: 2026-02-11T10:45:06Z
- **关闭时间**: 2026-02-28T07:01:55Z
- **更新时间**: 2026-02-28T07:01:55Z
- **提交者**: @hahadashi
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

镜像包是0.13.0;
4卡32G显存NPU; 

### 🐛 Describe the bug

输出的 Prompt: '<|im_start|>user\n<|audio_start|><|audio_pad|><|audio_end|>请将这段中文语音转换为纯文本。<|im_end|>\n<|im_start|>assistant\n', Generated text: "<think>\n<think>\n用户\nGot you have provided a011.99.000\nSo, I've been I'm in the user is a\n" 
输入的音频是16k采样的音频，内容为中文
messages = [
        {
            "role": "user",
            "content": [ 
                {"type": "audio", "audio": "/home/ma-user/work/ISR-U110635s420fa8c000h-utt.wav"},
                {"type": "text", "text": "请将这段中文语音转换为纯文本。"}
            ]
        }
    ]
打印了生成的text: '<|im_start|>user\n<|audio_start|><|audio_pad|><|audio_end|>请将这段中文语音转换为纯文本。<|im_end|>\n<|im_start|>assistant\n'

