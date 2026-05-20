#!/usr/bin/env python3
"""
Agent1: HuggingFace Hot Model Crawler
"""

import json
import os
import sys
import time
from datetime import datetime
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup


class HuggingFaceCrawler:
    BASE_URL = "https://huggingface.co"
    API_URL = "https://huggingface.co/api/models"
    
    def __init__(self, max_models: int = 50):
        self.max_models = max_models
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})
    
    def get_trending_models(self) -> List[Dict[str, Any]]:
        models = []
        try:
            response = self.session.get(self.API_URL, params={"sort": "downloads", "direction": -1, "limit": self.max_models}, timeout=30)
            response.raise_for_status()
            for model in response.json():
                model_info = self._extract_model_info(model)
                if model_info:
                    models.append(model_info)
        except Exception as e:
            print(f"API error: {e}")
            models = self._fallback_scrape()
        return models
    
    def _extract_model_info(self, model_data: Dict) -> Dict[str, Any]:
        try:
            model_id = model_data.get("modelId", "")
            if "/datasets" in model_id or "/spaces" in model_id:
                return None
            return {"name": model_id, "source": "huggingface", "downloads": model_data.get("downloads", 0), "parameters": self._estimate_parameters(model_data)}
        except:
            return None
    
    def _estimate_parameters(self, model_data: Dict) -> str:
        model_id = model_data.get("modelId", "").lower()
        tags = [t.lower() for t in model_data.get("tags", [])]
        for indicator, param in {"7b": "7B", "8b": "8B", "14b": "14B", "32b": "32B", "3b": "3B", "1b": "1B", "2b": "2B"}.items():
            if indicator in model_id or indicator in tags:
                return param
        return "unknown"
    
    def _fallback_scrape(self) -> List[Dict[str, Any]]:
        return []
    
    def save_results(self, models: List[Dict[str, Any]], output_path: str):
        with open(output_path, "w") as f:
            json.dump({"source": "huggingface", "models": models, "generated_at": datetime.utcnow().isoformat() + "Z"}, f, indent=2)
        print(f"Saved {len(models)} models to {output_path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    output_path = os.path.join(skill_dir, "huggingface_models.json")
    
    crawler = HuggingFaceCrawler()
    models = crawler.get_trending_models()
    if models:
        crawler.save_results(models, output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
