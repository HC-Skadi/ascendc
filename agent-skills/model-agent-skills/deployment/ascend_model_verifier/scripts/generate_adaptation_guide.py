#!/usr/bin/env python3
"""Agent4: Adaptation Guide Generator"""

import json, os, sys
from datetime import datetime
from pathlib import Path

def find_validated(skill_dir: str):
    results = Path(skill_dir) / "results"
    if not results.exists():
        return []
    validated = []
    for d in results.iterdir():
        if d.is_dir() and (d / "validation.complete").exists() and not (d / "documentation.complete").exists():
            validated.append(d)
    return validated

def generate_guide(model_dir: Path, skill_dir: str):
    result_file = model_dir / "benchmark_result.json"
    if not result_file.exists():
        return False
    with open(result_file) as f:
        result = json.load(f)
    if not result.get("success"):
        return False
    guide = f"""# {result['model']} 昇腾NPU适配指南

## 模型信息
- 模型: {result['model']}
- 验证时间: {result.get('timestamp', '')}

## 验证结果
- 状态: ✅ 通过
- 生成Token数: {result.get('tokens', 0)}

## 使用方法
```python
from vllm import LLM, SamplingParams
llm = LLM(model="{result['model']}", trust_remote_code=True, quantization="ascend")
```
"""
    (model_dir / "ASCEND_ADAPTATION_GUIDE.md").write_text(guide)
    (model_dir / "documentation.complete").write_text(f"Done: {datetime.utcnow().isoformat()}Z")
    return True

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    for d in find_validated(skill_dir):
        if generate_guide(d, skill_dir):
            print(f"Generated: {d.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
