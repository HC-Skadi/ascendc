#!/usr/bin/env python3
"""Agent2: Model Downloader"""

import json, os, sys
from datetime import datetime
from pathlib import Path

def get_next_model(skill_dir: str):
    list_path = Path(skill_dir) / "hot_models_list.json"
    if not list_path.exists():
        return None
    with open(list_path) as f:
        data = json.load(f)
    for m in data.get("models", []):
        folder = m["name"].replace("/", "-")
        result_dir = Path(skill_dir) / "results" / folder
        if result_dir.exists() and (result_dir / "documentation.complete").exists():
            continue
        params = m.get("parameters", "unknown")
        if params != "unknown" and "B" in params:
            try:
                if float(params.replace("B", "")) > 300:
                    continue
            except:
                pass
        m["folder_name"] = folder
        return m
    return None

def download_model(model: dict, skill_dir: str) -> bool:
    from modelscope import snapshot_download
    folder = model["folder_name"]
    download_dir = Path(skill_dir) / "downloaded_models" / folder
    download_dir.mkdir(parents=True, exist_ok=True)
    try:
        snapshot_download(model_id=model["name"], cache_dir=str(download_dir.parent))
        result_dir = Path(skill_dir) / "results" / folder
        result_dir.mkdir(parents=True, exist_ok=True)
        (result_dir / "download.complete").write_text(f"Downloaded: {datetime.utcnow().isoformat()}Z\nModel: {model['name']}")
        return True
    except Exception as e:
        print(f"Download error: {e}")
        return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    model = get_next_model(skill_dir)
    if model and download_model(model, skill_dir):
        print("Download complete!")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
