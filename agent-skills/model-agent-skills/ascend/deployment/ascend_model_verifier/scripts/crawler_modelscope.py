#!/usr/bin/env python3
"""Agent1: ModelScope Crawler"""

import json, os, sys, time
from datetime import datetime
from typing import List, Dict, Any
import requests

class ModelScopeCrawler:
    BASE_URL = "https://modelscope.cn"
    
    def __init__(self, max_models: int = 50):
        self.max_models = max_models
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})
    
    def get_trending_models(self) -> List[Dict[str, Any]]:
        models = []
        try:
            response = self.session.get(f"{self.BASE_URL}/api/v1/models", params={"PageSize": self.max_models}, timeout=30)
            if response.status_code == 200:
                data = response.json()
                if "Data" in data and "Models" in data["Data"]:
                    for m in data["Data"]["Models"][:self.max_models]:
                        name = m.get("Name", "")
                        org = m.get("Org", "")
                        models.append({"name": f"{org}/{name}" if org else name, "source": "modelscope", "downloads": m.get("Downloads", 0), "parameters": "unknown"})
        except Exception as e:
            print(f"Error: {e}")
        return models
    
    def save_results(self, models, output_path):
        with open(output_path, "w") as f:
            json.dump({"source": "modelscope", "models": models, "generated_at": datetime.utcnow().isoformat() + "Z"}, f, indent=2)
        print(f"Saved {len(models)} models")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    crawler = ModelScopeCrawler()
    models = crawler.get_trending_models()
    crawler.save_results(models, os.path.join(skill_dir, "modelscope_models.json"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
