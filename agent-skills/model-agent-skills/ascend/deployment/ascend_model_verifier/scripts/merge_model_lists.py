#!/usr/bin/env python3
"""Agent1: Merge Lists"""

import json, os, sys
from datetime import datetime
from typing import List, Set

def merge_lists(hf_path: str, ms_path: str, output_path: str):
    seen: Set[str] = set()
    merged = []
    
    for path in [hf_path, ms_path]:
        if not os.path.exists(path):
            continue
        with open(path) as f:
            data = json.load(f)
        for m in data.get("models", []):
            name = m.get("name", "").lower()
            if name and name not in seen:
                seen.add(name)
                merged.append(m)
    
    merged.sort(key=lambda x: x.get("downloads", 0), reverse=True)
    
    with open(output_path, "w") as f:
        json.dump({"models": merged[:100], "total_count": len(merged[:100]), "generated_at": datetime.utcnow().isoformat() + "Z"}, f, indent=2)
    print(f"Merged to {len(merged[:100])} models")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    merge_lists(os.path.join(skill_dir, "huggingface_models.json"), os.path.join(skill_dir, "modelscope_models.json"), os.path.join(skill_dir, "hot_models_list.json"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
