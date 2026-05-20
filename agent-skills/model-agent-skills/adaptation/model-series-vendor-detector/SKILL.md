---
name: model-series-vendor-detector
description: 根据模型名称识别其所属系列和开发供应商。当用户需要从模型名称判断模型属于什么系列（如GLM、Qwen3、DeepSeek、MiniCPM等）以及其开发商/供应商时使用此skill。
---

# Model Series and Vendor Detector

根据模型名称通过正则匹配识别模型所属系列（series）和供应商（vendor）。

## Series 识别规则

使用以下优先级顺序进行匹配：

| 系列 | 正则匹配规则 | 示例 |
|------|--------------|------|
| GLM | `^GLM[-_]\|^glm[-_]\|zai-org-GLM` | GLM4.5-AIR, zai-org-GLM-Image |
| QwQ | `^QwQ[-_]` | QwQ-32B |
| Qwen3.5 | `^Qwen3\.5` | Qwen3.5-32B |
| Qwen3 | `^Qwen3[-_]\|^qwen3[-_]` | qwen3-tts-12hz-0.6b-base |
| Qwen2.5 | `^Qwen2\.5\|^qwen2\.5` | qwen2.5_14b_instruct |
| Qwen2 | `^Qwen2[-_]\|^qwen2_` | qwen2_vl_72b_instruct |
| Qwen | `^Qwen[-_]\|^qwen[-_]\|^qwen_` | qwen-image-layered, qwen_7b_base |
| DeepSeek | `^DeepSeek\|^deepseek` | DeepSeek-V3 |
| openPangu | `^openPangu\|^Pangu` | openPangu2 |
| MiniMax | `^MiniMax` | MiniMax-M2 |
| MiniCPM | `^MiniCPM` | MiniCPM-V-4_5 |
| Hunyuan | `^hunyuan\|^hy-` | hy-mt1.5-1.8b, hunyuan-tts |
| Xiaomi | `^Xiaomi` | Xiaomi-MiMo-VL-Miloco-7B |
| Intern | `^Intern` | InternLM3 |
| Yi | `^Yi[-_]` | Yi-34B |
| Llama | `^Llama` | Llama3-70B |
| Gemma | `^Gemma` | Gemma2-27B |
| GPT | `^GPT[-_]` | GPT-4 |
| LLaVA | `^LLaVA` | LLaVA1.6-34B |
| Whisper | `^Whisper` | Whisper-large-v3 |
| Flux | `^Flux` | Flux1.1-Pro |
| Wan | `^Wan` | Wan2.1-14B |
| CosyVoice | `^CosyVoice\|^Fun-CosyVoice` | CosyVoice2-0.5B |
| PaddleOCR | `^PaddleOCR` | PaddleOCRv5 |
| SenseVoice | `^SenseVoice` | SenseVoice-Large |
| ERNIE | `^ERNIE` | ERNIE4.0-8K |
| YOLO | `^YOLO` | YOLO11 |
| BGE | `^bge-` | bge-m3 |
| StepFun | `^StepFun\|^GOT-OCR` | StepFun-VL-32B |
| PaddleOCR | `^PaddleOCR` | PaddleOCRv5 |
| 其他 | - | 返回 'Unknown' |

## Vendor 识别规则

| 供应商 | 匹配系列 | 中文名称 |
|--------|----------|----------|
| 智谱AI | GLM | 智谱AI |
| 阿里云 | Qwen, QwQ, CosyVoice, SenseVoice, Fun-ASR, Fun-CosyVoice | 阿里云 |
| 深度求索 | DeepSeek | 深度求索 |
| 华为 | openPangu | 华为 |
| MiniMax | MiniMax | MiniMax |
| 面壁智能 | MiniCPM | 面壁智能 |
| 小米 | Xiaomi | 小米 |
| 百度 | PaddleOCR, PP-OCR, ERNIE | 百度 |
| 腾讯 | Hunyuan | 腾讯 |
| 上海人工智能实验室 | Intern | 上海人工智能实验室 |
| 零一万物 | Yi | 零一万物 |
| Meta | Llama | Meta |
| Google | Gemma, translategemma | Google |
| OpenAI | GPT, Whisper | OpenAI |
| LLaVA团队 | LLaVA | LLaVA团队 |
| BlackForestLabs | Flux | BlackForestLabs |
| 字节跳动 | Wan, Index-TTS, dots.ocr, LatentSync | 字节跳动 |
| 复旦大学 | MOSS | 复旦大学 |
| 出门问问 | WeNet | 出门问问 |
| 阶跃星辰 | StepFun, GOT-OCR | 阶跃星辰 |
| 月之暗面 | Kimi | 月之暗面 |
| Ultralytics | YOLO | Ultralytics |
| BAAI | bge- | BAAI |
| 阿联酋MBZUAI | Ovis | 阿联酋MBZUAI |
| MIT | MapFormer | MIT |
| Magic Data | MinerU | Magic Data |

## 输出格式

返回 JSON 格式：
```json
{
  "series": "Qwen3.5",
  "vendor": "阿里云"
}
```

## 使用示例

输入: "qwen3-tts-12hz-0.6b-base"
输出: `{"series": "Qwen3", "vendor": "阿里云"}`

输入: "MiniCPM-V-4_5"
输出: `{"series": "MiniCPM", "vendor": "面壁智能"}`

输入: "GLM4.5-AIR"
输出: `{"series": "GLM", "vendor": "智谱AI"}`