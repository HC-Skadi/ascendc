"""
ModelScope API 封装模块
用于从 ModelScope 平台获取模型数据
"""

import json
import time
import logging
import re
from typing import Optional, List, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)

try:
    from modelscope import HubApi
    from modelscope import Model
    MODELSCOLE_AVAILABLE = True
except ImportError:
    MODELSCOLE_AVAILABLE = False
    logger.warning("modelscope SDK not installed. Run: pip install modelscope")


MODEL_TYPE_PATTERNS = {
    "LLM": [
        r'Llama', r'Qwen', r'Baichuan', r'ChatGLM', r'GLM', r'DeepSeek', r'Mistral',
        r'Gemma', r'Mixtral', r'Yi', r'B Compact', r'InternLM', r'Falcon', r'Mamba',
        r'StableLM', r'Dbrx', r'Granite', r'Minitron', r'StableLM', r'Phi', r'Grok',
        r'WizardLM', r'Zephyr', r'OLMo', r'Pythia', r'RedPajama', r'ReJewel', r'Bert',
        r'RoBERTa', r'XLNet', r'ALBERT', r'DeBERTa', r'T5', r'FLAN', r'BART',
    ],
    "VL": [
        r'VL', r'Vision', r'InternVL', r'Qwen-VL', r'Llava', r'MiniGPT', r' Otter',
        r'Vary', r'DeepSeek-VL', r'ChatDM', r'VisionTower', r'Llama-3\.1-8B',
    ],
    "Embedding": [
        r'Embedding', r'embed', r'sentence-bert', r'all-MiniLM', r'e5', r'bge-',
        r'reranker', r'GTE', r'MiniLM', r'BAAI', r'GritLM', r'NV-Embed',
    ],
    "Generation": [
        r'Stable Diffusion', r'SD-XL', r'SD-', r'Diffusion', r'Flux', r'FLUX',
        r'Midjourney', r'DALL-E', r'SDXL', r' Playground', r'Kolors',
        r'Wan', r'Imagen', r'Vega', r'HunYuanDiT',
    ],
    "Audio": [
        r'Whisper', r'Bark', r'Speech', r'Audio', r'XTTS', r'CosyVoice',
        r'Qwen2-Audio', r'Falcon-M', r'Kokoro',
    ],
    "Video": [
        r'Video', r'CogVideo', r'Open-Sora', r'Sora', r'Latte', r'Magician',
    ],
}


def classify_model_type(path: str, model_type: str = None, tasks: List = None) -> str:
    """根据模型路径、类型和任务分类模型类型"""
    text = f"{path} {model_type or ''}"
    
    if tasks and len(tasks) > 0:
        for task in tasks:
            task_name = task.get('Name', '') or ''
            if 'text-generation' in task_name.lower() or 'causal-lm' in task_name.lower():
                return "LLM"
            if 'image-text-to-text' in task_name.lower() or 'visual-question-answering' in task_name.lower():
                return "VL"
            if 'text-to-image' in task_name.lower() or 'image-generation' in task_name.lower():
                return "Generation"
            if 'automatic-speech-recognition' in task_name.lower() or 'text-to-speech' in task_name.lower():
                return "Audio"
    
    for model_type_str, patterns in MODEL_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return model_type_str
    
    return "Other"


class ModelScopeCollector:
    """ModelScope 模型数据收集器"""
    
    BASE_URL = "https://modelscope.cn"
    DEFAULT_TOP = 200
    
    def __init__(self, cache_dir: Optional[Path] = None):
        self.cache_dir = cache_dir or Path("/root/.claude/skills/awesome-llm-model/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.cache_dir / "modelscope_models.json"
        self._api = None
    
    @property
    def api(self) -> Optional[HubApi]:
        if not MODELSCOLE_AVAILABLE:
            return None
        if self._api is None:
            self._api = HubApi()
        return self._api
    
    def fetch_models(self, top: int = 200, force_refresh: bool = False) -> List[Dict[str, Any]]:
        if not force_refresh and self.cache_file.exists():
            cache_age = time.time() - self.cache_file.stat().st_mtime
            if cache_age < 6 * 3600:
                logger.info(f"Using cached ModelScope data (age: {cache_age/3600:.1f}h)")
                return self._load_cache()
        
        if not MODELSCOLE_AVAILABLE:
            logger.error("ModelScope SDK not available")
            return self._load_cache() if self.cache_file.exists() else []
        
        models = []
        page_size = 100
        retries = 3
        
        for offset in range(0, top, page_size):
            current_page_size = min(page_size, top - offset)
            for attempt in range(retries):
                try:
                    models_page = self._fetch_page(offset, current_page_size)
                    models.extend(models_page)
                    logger.info(f"Fetched {len(models)} ModelScope models")
                    break
                except Exception as e:
                    logger.warning(f"Attempt {attempt+1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(2 ** attempt)
                    else:
                        logger.error(f"Failed to fetch ModelScope models after {retries} attempts")
        
        processed_models = self._process_models(models)
        self._save_cache(processed_models)
        
        return processed_models
    
    def _fetch_page(self, offset: int, limit: int) -> List[Dict[str, Any]]:
        page_number = (offset // limit) + 1
        page_size = limit
        result = self.api.list_models('', page_number=page_number, page_size=page_size)
        models = result.get("Models", [])
        return models
    
    def _process_models(self, models: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        
        for model in models:
            try:
                model_name = model.get("Name", "")
                path = model.get("Path", "")
                downloads = model.get("Downloads", 0) or 0
                stars = model.get("Stars", 0) or 0
                model_type_str = model.get("ModelType", "")
                tasks = model.get("Tasks", [])
                
                params = self._extract_params(path, model.get("Description", ""))
                model_type = classify_model_type(path, model_type_str, tasks)
                
                download_path = f"https://modelscope.cn/{path}"
                
                processed.append({
                    "name": model_name,
                    "path": path,
                    "model_name": path,
                    "organization": model.get("Org", ""),
                    "author": model.get("Owner", ""),
                    "downloads": downloads,
                    "stars": stars,
                    "likes": stars,
                    "download_path": download_path,
                    "params": params,
                    "has_ascend_quant": "",
                    "quant_path": "",
                    "platform": "modelscope",
                    "model_type": model_type,
                    "raw_data": model
                })
            except Exception as e:
                logger.debug(f"Error processing model: {e}")
                continue
        
        return processed
    
    def _extract_params(self, path: str, description: str) -> str:
        patterns = [
            r'(\d+[.,]?\d*)B',
            r'(\d+)[mM]',
        ]
        
        text = f"{path} {description}"
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                value = match.group(1)
                if 'B' in pattern:
                    return f"{value}B"
                else:
                    return f"{value}M"
        
        return ""
    
    def _load_cache(self) -> List[Dict[str, Any]]:
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load cache: {e}")
            return []
    
    def _save_cache(self, models: List[Dict[str, Any]]):
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(models, f, ensure_ascii=False, indent=2)
            logger.info(f"Cached {len(models)} ModelScope models")
        except Exception as e:
            logger.error(f"Failed to save cache: {e}")


def get_modelscope_models(top: int = 200, force_refresh: bool = False) -> List[Dict[str, Any]]:
    collector = ModelScopeCollector()
    return collector.fetch_models(top=top, force_refresh=force_refresh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    collector = ModelScopeCollector()
    models = collector.fetch_models(top=10)
    print(f"Fetched {len(models)} models")
    for m in models[:3]:
        print(f"  - {m['name']} ({m.get('model_type', 'Unknown')}): {m['downloads']} downloads, {m['stars']} stars")