---
name: awesome-llm-model
description: 获取和管理LLM模型热度排行榜。当用户需要获取ModelScope或HuggingFace上的热门模型列表、查询模型的下载量/点赞数、生成模型排行榜、进行模型去重分析、或需要导出模型信息表格时使用此技能。适用于需要了解当前最热门LLM模型的场景，例如模型调研、模型选型、排行榜分析等。
---

# Awesome LLM Model 技能

用于收集、整理和管理来自 ModelScope 和 HuggingFace 的热门 LLM 模型排行榜。

## 核心功能

1. **数据收集**：从 ModelScope 和 HuggingFace 获取热门模型
2. **热度评分**：使用 `下载量×0.3 + 点赞数×0.7` 的权重算法计算综合热度
3. **模型分类**：自动识别模型类型（LLM、VL、Embedding、Generation、Audio、Video）
4. **去重处理**：跨平台去重，保留热度最高的版本
5. **输出生成**：生成 Markdown、CSV、Excel 格式

## 使用方式

### 基本命令

```bash
# 收集所有模型数据并生成排行榜
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --output-dir /path/to/output

# 仅收集 ModelScope 数据
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --platform modelscope --top 200

# 仅收集 HuggingFace 数据
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --platform huggingface --top 200

# 生成去重后的排行榜
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --deduplicate

# 指定输出格式
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --output-format markdown  # 默认
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --output-format csv
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --output-format excel

# 强制刷新缓存
python /root/.config/opencode/skills/awesome-llm-model/scripts/collect_models.py --force-refresh
```

### 通过 Skill 调用

当用户请求以下内容时触发此技能：
- "获取 ModelScope/HuggingFace 热门模型"
- "生成 LLM 模型排行榜"
- "列出最受欢迎的模型"
- "模型去重分析"
- "导出模型信息表格"
- "比较两个平台的模型"

## 数据字段

收集的模型信息包含以下字段：

| 字段 | 说明 |
|------|------|
| 序号 | 排名（从1开始） |
| 模型名称 | 模型的完整名称 |
| 组织/作者 | 发布模型的组织或个人 |
| 参数量 | 模型参数数量（如7B、13B等） |
| 模型类型 | LLM/VL/Embedding/Generation/Audio/Video/Other |
| 下载路径 | ModelScope 链接（优先），或 hf-mirror.com 链接 |
| 昇腾量化 | 是否有昇腾可用的 w8a8/w4a8 量化权重 |
| 量化路径 | 量化权重路径（可为空） |

## 模型类型分类

| 类型 | 说明 | 示例 |
|------|------|------|
| LLM | 大语言模型 | Llama, Qwen, ChatGLM, DeepSeek, Mistral |
| VL | 视觉语言模型 | InternVL, Qwen-VL, Llava, MiniGPT |
| Embedding | 文本嵌入模型 | bge, e5, all-MiniLM, GTE |
| Generation | 图像生成模型(Diffusion) | Stable Diffusion, FLUX, SDXL, Kolors |
| Audio | 语音/音频模型 | Whisper, Kokoro, XTTS, CosyVoice |
| Video | 视频生成模型 | CogVideo, Open-Sora, Sora |
| Other | 其他类型 | 不属于上述类别的模型 |

## 热度评分算法

```
综合热度分数 = 下载量×0.3 + 点赞数×0.7
```

- 下载量标准化：使用对数缩放避免极值影响
- 点赞数权重更高（0.7），反映用户质量认可
- 最终按综合分数降序排列

## 去重规则

1. **同名去重**：如果模型名称完全相同，保留热度分数更高的版本
2. **跨平台匹配**：尝试通过模型名称模糊匹配（如 `Qwen/Qwen2-7B` 与 `Qwen2-7B`）
3. **优先保留**：ModelScope 平台数据优先（因为国内访问更稳定）

## 昇腾量化权重

### 量化权重来源

昇腾量化权重可从以下来源获取：

| 来源 | 链接 | 说明 |
|------|------|------|
| vllm-ascend (ModelScope) | https://modelscope.cn/organization/vllm-ascend | 华为官方 vLLM-Ascend 量化模型 |
| Eco-Tech (Modelers) | https://modelers.cn/user/Eco-Tech | 社区提供的量化权重 |

### 量化格式说明

- **w8a8**: 8位权重 + 8位激活量化
- **w4a8**: 4位权重 + 8位激活量化
- **w8a16**: 8位权重 + 16位激活量化

## 输出格式

### Markdown 表格示例

```markdown
# Awesome LLM Model 排行榜

**生成时间**: 2026-04-11

## 统计信息
- ModelScope 模型数：200
- HuggingFace 模型数：200
- 去重后总数：XXX

## 模型类型说明
- **LLM**: 大语言模型 (Large Language Model)
- **VL**: 视觉语言模型 (Vision Language)
- **Embedding**: 文本嵌入模型
- **Generation**: 图像/视频生成模型 (Diffusion-based)
- **Audio**: 语音/音频模型
- **Video**: 视频生成模型
- **Other**: 其他类型模型

## 排行榜

| 序号 | 模型名称 | 组织/作者 | 参数量 | 模型类型 | 下载路径 | 昇腾量化 | 量化路径 |
|------|----------|-----------|--------|----------|----------|----------|----------|
| 1 | Qwen2-72B | Qwen | 72B | LLM | [链接](https://modelscope.cn/...) | 是 | /path/to/w8a8 |
...
```

### CSV/Excel 格式

CSV 文件包含相同的字段，支持 Excel 直接打开。

## 缓存机制

- 缓存位置：`/root/.config/opencode/skills/awesome-llm-model/cache/`
- 缓存有效期：6小时（可通过 `--force-refresh` 强制刷新）
- 缓存文件：
  - `modelscope_models.json` - ModelScope 数据
  - `huggingface_models.json` - HuggingFace 数据

## 错误处理

1. **API 请求失败**：自动重试3次，间隔2秒
2. **网络超时**：超时时间30秒
3. **部分数据失败**：继续处理可用数据，记录错误日志
4. **Rate Limiting**：遵守 API 速率限制，自动退避

## API 接口

### ModelScope API

使用 `modelscope` Python SDK：

```python
from modelscope import HubApi
api = HubApi()
# 获取模型列表
result = api.list_models('', page_number=1, page_size=100)
models = result.get("Models", [])
```

### HuggingFace API

使用 `huggingface_hub` Python SDK，自动使用 hf-mirror.com 镜像：

```python
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from huggingface_hub import HfApi
api = HfApi()
models = list(api.list_models(sort="likes7d", direction=-1, limit=200))
```

## 依赖

- Python 3.8+
- modelscope>=1.11.0
- huggingface_hub>=0.19.0
- pandas>=2.0.0
- openpyxl>=3.1.0 (用于 Excel 导出)

## 目录结构

```
awesome-llm-model/
├── SKILL.md
├── scripts/
│   ├── __init__.py
│   ├── collect_models.py      # 主入口脚本
│   ├── modelscope_api.py     # ModelScope API 封装
│   ├── huggingface_api.py    # HuggingFace API 封装
│   ├── processor.py          # 数据处理和去重
│   └── output.py             # 输出生成
├── cache/                    # 缓存目录
└── logs/                     # 日志目录
```

## 故障排除

### 常见问题

1. **API 认证失败**：确保已登录 ModelScope/HuggingFace
   ```bash
   modelscope login
   huggingface-cli login
   ```

2. **网络访问问题**：HuggingFace 自动使用 hf-mirror.com 镜像

3. **数据收集缓慢**：减少并发请求，增加缓存时间

### 日志位置

- 主日志：`/root/.config/opencode/skills/awesome-llm-model/logs/collect.log`
- 错误日志：`/root/.config/opencode/skills/awesome-llm-model/logs/error.log`