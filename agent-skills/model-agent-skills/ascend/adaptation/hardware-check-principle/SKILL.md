---
name: hardware-check-principle
description: 梳理模型硬件适配检查的逻辑和原则。当用户需要了解硬件适配检测的规则、关键词定义、昇腾硬件型号分类时使用此skill。
---

# 硬件适配检查逻辑与原则

## 一、支持检测的硬件型号

| 硬件名称 | 匹配关键词 | 说明 |
|---------|-----------|------|
| A2 | 910b, Atlas 800T A2, Atlas 800I A2,  A2 | 昇腾Atlas 800T A2 / 910B |
| A3 | 910c, Atlas 800T A3, Atlas 800I A3,  A3 | 昇腾Atlas 800T A3 / 910C |
| 310 | 310 | 昇腾310系列 |

## 二、检测数据来源（必须全部检查）

**重要：必须按以下顺序检查所有数据来源，不能跳过任何一个！**

1. **模型name字段** - 模型名称中可能包含硬件信息
2. **模型full_name字段** - 完整仓库名中可能包含硬件信息
3. **模型description字段** - JSON数据源中包含的模型描述
4. **README文档内容** - GitCode仓库的README.md文档内容 **（必须获取）**

**强制要求：每个模型都必须尝试获取README内容进行检查，不能因为时间长或其他原因跳过！**

检查流程：依次遍历上述数据来源，在每个来源中检索硬件关键词，一旦匹配成功即停止搜索，记录匹配到的硬件型号。

## 三、关键词匹配规则

- 使用正则表达式进行**单词边界匹配**
- 关键词不区分大小写
- 匹配顺序按优先级列表依次进行，优先匹配到的硬件生效

```python
HARDWARE_KEYWORDS = [
    ("A2", ["910b", "Atlas 800T A2", "Atlas 800I A2", " A2"]),
    ("A3", ["910c", "Atlas 800T A3", "Atlas 800I A3", " A3"]),
    ("310", ["310"]),
]

pattern_with_boundary = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
pattern_without_boundary = re.compile(re.escape(term), re.IGNORECASE)

if pattern_with_boundary.search(content_lower):
    match = pattern_with_boundary.search(content_lower)
else:
    match = pattern_without_boundary.search(content_lower)
```

## 四、核心代码实现

以下是完整的硬件适配检测核心代码：

```python
#!/usr/bin/env python3
import json
import re
import os
import time
from urllib.parse import urlparse

HARDWARE_KEYWORDS = [
    ("A2", ["910b", "Atlas 800T A2", "Atlas 800I A2", " A2"]),
    ("A3", ["910c", "Atlas 800T A3", "Atlas 800I A3", " A3"]),
    ("310", ["310"]),
]

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

def detect_adapter_hardware(content):
    """检测适配硬件"""
    if not content:
        return None
    
    content_lower = content.lower()
    
    for hardware, keywords in HARDWARE_KEYWORDS:
        for keyword in keywords:
            keyword_escaped = re.escape(keyword)
            pattern_with_boundary = re.compile(r'\b' + keyword_escaped + r'\b', re.IGNORECASE)
            pattern_without_boundary = re.compile(keyword_escaped, re.IGNORECASE)
            
            if pattern_with_boundary.search(content_lower):
                return hardware
            
            if pattern_without_boundary.search(content_lower):
                return hardware
    
    return None

def check_adapter_hardware(model):
    """检查模型的适配硬件
    
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
    
    adapter_hardware = None
    
    for source in search_sources:
        if source:
            hw = detect_adapter_hardware(source)
            if hw:
                adapter_hardware = hw
                return adapter_hardware
    
    readme_content = fetch_readme_content(url)
    if readme_content:
        adapter_hardware = detect_adapter_hardware(readme_content)
    
    return adapter_hardware
```

## 五、常见使用场景

### 场景1: 批量检查JSON中的模型硬件适配

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
6. 添加adapter_hardware字段

**禁止跳过README检查！** 无论时间多长，都必须获取README内容进行检测。

### 场景2: 与适配框架检测配合使用

硬件检测通常与框架检测配合使用，同时输出：
- `adapter_framework`: 适配框架
- `adapter_hardware`: 适配硬件
- `training_or_inference`: 训练/推理分类

## 六、输出格式

检测结果添加以下字段：

| 字段名 | 说明 |
|-------|------|
| adapter_hardware | 检测到的硬件型号（A2/A3/310），如未匹配则为空 |

## 七、README获取注意事项

1. **URL转换**: 将 `https://gitcode.com/{owner}/{repo}` 转换为 `https://raw.gitcode.com/{owner}/{repo}/raw/main/README.md`

2. **超时设置**: curl命令超时建议30秒

3. **请求间隔**: 每次请求间隔建议0.3秒，避免请求过快

4. **内容验证**: README内容长度需大于100字符才认为获取成功

5. **检查点保存**: 处理一定数量后保存进度，避免中断丢失数据

```python
def process_models_batch(models, checkpoint_interval=50):
    """批量处理模型，每50个保存一次检查点"""
    for idx, model in enumerate(models):
        # 检查适配硬件
        adapter_hardware = check_adapter_hardware(model)
        model["adapter_hardware"] = adapter_hardware or ""
        
        # 定期保存检查点
        if (idx + 1) % checkpoint_interval == 0:
            save_checkpoint(data, checkpoint_file)
        
        time.sleep(0.3)
```

## 八、完整处理流程示例

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
        adapter_hardware = check_adapter_hardware(model)
        model["adapter_hardware"] = adapter_hardware or ""
        
        print(f"[{idx+1}/{len(gitcode_models)}] {model.get('name')} -> hardware: {adapter_hardware}")
        
        time.sleep(0.3)
        
        if (idx + 1) % 50 == 0:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Checkpoint saved at {idx+1}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Done!")
```

**注意：处理模型时需要耐心等待，不要中断！**