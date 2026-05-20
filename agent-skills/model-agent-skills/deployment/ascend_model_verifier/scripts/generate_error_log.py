#!/usr/bin/env python3
"""Agent4: Error Log Generator"""

import json, os, sys
from datetime import datetime
from pathlib import Path

def find_failed(skill_dir: str):
    results = Path(skill_dir) / "results"
    if not results.exists():
        return []
    failed = []
    for d in results.iterdir():
        if d.is_dir():
            result_file = d / "benchmark_result.json"
            if result_file.exists() and not (d / "documentation.complete").exists():
                with open(result_file) as f:
                    r = json.load(f)
                if not r.get("success"):
                    failed.append((d, r))
    return failed

def generate_error_log(model_dir: Path, result: dict):
    log = f"""# {result['model']} 错误日志

## 错误信息
{result.get('error', 'Unknown error')}

## 时间
{result.get('timestamp', '')}

## 建议
1. 检查模型是否支持昇腾NPU
2. 确认vLLM-Ascend已正确安装
3. 检查NPU驱动状态
"""
    (model_dir / "ERROR_LOG.md").write_text(log)
    (model_dir / "documentation.complete").write_text(f"Done: {datetime.utcnow().isoformat()}Z")
    return True

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    for d, r in find_failed(skill_dir):
        generate_error_log(d, r)
        print(f"Generated error log: {d.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
