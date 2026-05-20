---
name: adapter-check-principle
description: 梳理模型适配框架检查的逻辑和原则。当用户需要了解适配框架检测的规则、关键词定义、训练/推理框架分类时使用此skill。
---

# 适配框架检查逻辑与原则

## 一、支持检测的适配框架

### 推理框架

| 框架名称 | 匹配关键词 | 说明 |
|---------|-----------|------|
| vllm-ascend | vllm-ascend, vllm_ascend, vllm ascend | 昇腾NPU推理框架 |
| vllm | vllm | 通用vllm，检测到后统一转为vllm-ascend |
| sglang | sglang | 高性能推理框架 |
| mindie | mindie | 华为MindIE推理框架 |
| omni-infer | omni-infer, omni infer | Omni推理框架（不区分大小写） |

### 训练框架

| 框架名称 | 匹配关键词 | 说明 |
|---------|-----------|------|
| mindspeed-llm | mindspeed-llm, mindspeed_llm, mindspeed llm | 大语言模型训练 |
| mindspeed-mm | mindspeed-mm, mindspeed_mm, mindspeed mm | 多模态模型训练 |
| LLaMa Factory | llama factory, llama-factory, llamafactory | LLaMA微调框架 |
| verl | verl | 强化学习训练框架 |

## 二、训练/推理分类

根据适配框架名称自动判断用途类型：

```python
TRAINING_FRAMEWORKS = ["mindspeed-llm", "mindspeed-mm", "LLaMa Factory", "verl"]
INFERENCE_FRAMEWORKS = ["vllm-ascend", "sglang", "mindie", "omni-infer"]

def get_training_or_inference(framework):
    if framework in TRAINING_FRAMEWORKS:
        return "训练"
    if framework in INFERENCE_FRAMEWORKS:
        return "推理"
    return ""
```

## 三、检测数据来源（必须全部检查）

**重要：必须按以下顺序检查所有数据来源，不能跳过任何一个！**

1. **模型name字段** - 模型名称中可能包含框架信息
2. **模型full_name字段** - 完整仓库名中可能包含框架信息
3. **模型description字段** - JSON数据源中包含的模型描述
4. **README文档内容** - GitCode仓库的README.md文档内容 **（必须获取）**

**强制要求：每个模型都必须尝试获取README内容进行检查，不能因为时间长或其他原因跳过！**

检查流程：依次遍历上述数据来源，在每个来源中检索适配框架关键词，一旦匹配成功即停止搜索，记录匹配到的框架。

## 四、关键词匹配规则

- 使用正则表达式进行**单词边界匹配**
- 关键词不区分大小写
- 匹配顺序按优先级列表依次进行，优先匹配到的框架生效

```python
ADAPTER_KEYWORDS = [
    ("vllm-ascend", ["vllm-ascend", "vllm_ascend", "vllm ascend"]),
    ("mindspeed-llm", ["mindspeed-llm", "mindspeed_llm", "mindspeed llm"]),
    ("mindspeed-mm", ["mindspeed-mm", "mindspeed_mm", "mindspeed mm"]),
    ("sglang", ["sglang"]),
    ("mindie", ["mindie"]),
    ("omni-infer", ["omni-infer", "omni infer"]),
    ("LLaMa Factory", ["llama factory", "llama-factory", "llamafactory"]),
    ("verl", ["verl"]),
    ("vllm", ["vllm"]),
]

pattern_with_boundary = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
pattern_without_boundary = re.compile(re.escape(term), re.IGNORECASE)

if pattern_with_boundary.search(content_lower):
    match = pattern_with_boundary.search(content_lower)
else:
    match = pattern_without_boundary.search(content_lower)
```

## 五、vllm特殊处理

- 匹配到关键词"vllm"时，统一转换为"vllm-ascend"
- 原因：本项目中所有vllm都是指昇腾NPU版本的vllm

## 六、核心代码实现

以下是完整的适配框架检测核心代码：

```python
#!/usr/bin/env python3
import json
import re
import os
import time
from urllib.parse import urlparse

ADAPTER_KEYWORDS = [
    ("vllm-ascend", ["vllm-ascend", "vllm_ascend", "vllm ascend"]),
    ("mindspeed-llm", ["mindspeed-llm", "mindspeed_llm", "mindspeed llm"]),
    ("mindspeed-mm", ["mindspeed-mm", "mindspeed_mm", "mindspeed mm"]),
    ("sglang", ["sglang"]),
    ("mindie", ["mindie"]),
    ("omni-infer", ["omni-infer", "omni infer"]),
    ("LLaMa Factory", ["llama factory", "llama-factory", "llamafactory"]),
    ("verl", ["verl"]),
    ("vllm", ["vllm"]),
]

TRAINING_FRAMEWORKS = ["mindspeed-llm", "mindspeed-mm", "LLaMa Factory", "verl"]
INFERENCE_FRAMEWORKS = ["vllm-ascend", "sglang", "mindie", "omni-infer"]

def get_raw_readme_url(url):
    """从gitcode仓库URL获取raw README URL"""
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    if len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return f"https://raw.gitcode.com/{owner}/{repo}/raw/main/README.md"
    return None

def fetch_readme_content(url):
    """使用curl获取README内容"""
    raw_url = get_raw_readme_url(url)
    if not raw_url:
        return None
    
    import subprocess
    try:
        result = subprocess.run(
            ['curl', '-sL', raw_url],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0 and result.stdout:
            content = result.stdout
            if len(content) > 100:
                return content
    except:
        pass
    return None

def detect_adapter_framework(content):
    """检测适配框架"""
    if not content:
        return None, None
    
    content_lower = content.lower()
    
    for framework, keywords in ADAPTER_KEYWORDS:
        for keyword in keywords:
            pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
            if pattern.search(content_lower):
                if framework == "vllm":
                    framework = "vllm-ascend"
                training_or_inference = "训练" if framework in TRAINING_FRAMEWORKS else "推理"
                return framework, training_or_inference
    
    return None, None

def check_adapter_framework(model):
    """检查模型的适配框架
    
    必须检查所有数据来源：
    1. name字段
    2. full_name字段  
    3. description字段
    4. README文档（必须获取）
    """
    name = model.get("name", "")
    full_name = model.get("full_name", "")
    description = model.get("description", "") or ""
    url = model.get("url", "")
    
    search_sources = [name, full_name, description]
    
    adapter_framework = None
    training_or_inference = None
    
    for source in search_sources:
        if source:
            fw, toi = detect_adapter_framework(source)
            if fw:
                adapter_framework = fw
                training_or_inference = toi
                return adapter_framework, training_or_inference
    
    readme_content = fetch_readme_content(url)
    if readme_content:
        adapter_framework, training_or_inference = detect_adapter_framework(readme_content)
    
    return adapter_framework, training_or_inference
```

## 七、常见使用场景

### 场景1: 批量检查JSON中的模型适配框架

输入文件格式要求：
```json
{
  "models": [
    {
      "name": "模型名称",
      "full_name": "完整仓库名",
      "url": "https://gitcode.com/xxx/xxx",
      "description": "模型描述..."
    }
  ]
}
```

**关键处理逻辑（必须执行）：**
1. 遍历每个source为"gitcode"的模型
2. 检查name字段
3. 检查full_name字段
4. 检查description字段
5. **必须获取README.md内容并检查**
6. 添加adapter_framework字段
7. 添加training_or_inference字段

**禁止跳过README检查！** 无论时间多长，都必须获取README内容进行检测。

### 场景2: 从Excel读取待检查模型

Excel文件格式：
| 模型系列 | 模型名 | 仓库名 | 适配框架 | 训练/推理 | 链接 |
|---------|-------|--------|---------|---------|-----|

检查逻辑：
- 只检查"适配框架"列为空的模型
- **必须爬取README内容进行检测**

### 场景3: 验证已标记的模型

针对已标记适配框架的模型，重新验证README内容确保标记准确性。

## 八、输出格式

检测结果添加以下字段：

| 字段名 | 说明 |
|-------|------|
| adapter_framework | 检测到的适配框架名称，如未匹配则为空 |
| training_or_inference | "训练" 或 "推理"，如未匹配则为空 |

## 九、README获取注意事项

1. **URL转换**: 将 `https://gitcode.com/{owner}/{repo}` 转换为 `https://raw.gitcode.com/{owner}/{repo}/raw/main/README.md`

2. **超时设置**: curl命令超时建议30秒

3. **请求间隔**: 每次请求间隔建议0.3秒，避免请求过快

4. **内容验证**: README内容长度需大于100字符才认为获取成功

5. **检查点保存**: 处理一定数量后保存进度，避免中断丢失数据

```python
def process_models_batch(models, checkpoint_interval=50):
    """批量处理模型，每50个保存一次检查点"""
    for idx, model in enumerate(models):
        # 检查适配框架
        adapter_framework, training_or_inference = check_adapter_framework(model)
        model["adapter_framework"] = adapter_framework or ""
        model["training_or_inference"] = training_or_inference or ""
        
        # 定期保存检查点
        if (idx + 1) % checkpoint_interval == 0:
            save_checkpoint(data, checkpoint_file)
        
        time.sleep(0.3)
```

## 十、完整处理流程示例

```python
def main():
    input_file = "ascend_model.json"
    output_file = "ascend_model_with_adapter.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    models = data.get("models", [])
    gitcode_models = [m for m in models if m.get("source") == "gitcode"]
    
    print(f"Gitcode models: {len(gitcode_models)}")
    
    for idx, model in enumerate(gitcode_models):
        adapter_framework, training_or_inference = check_adapter_framework(model)
        model["adapter_framework"] = adapter_framework or ""
        model["training_or_inference"] = training_or_inference or ""
        
        print(f"[{idx+1}/{len(gitcode_models)}] {model.get('name')} -> {adapter_framework}")
        
        time.sleep(0.3)
        
        if (idx + 1) % 50 == 0:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Checkpoint saved at {idx+1}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Done!")
```

**注意：处理426个模型大约需要2-3分钟，请耐心等待，不要中断！**