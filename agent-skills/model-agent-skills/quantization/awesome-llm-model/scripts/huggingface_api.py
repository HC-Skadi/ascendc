"""
HuggingFace API 封装模块
用于从 HuggingFace 平台获取模型数据
"""

import json
import os
import time
import logging
import re
from typing import Optional, List, Dict, Any
from pathlib import Path

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

logger = logging.getLogger(__name__)

try:
    from huggingface_hub import HfApi
    from huggingface_hub import constants
    HF_AVAILABLE = True
except ImportError:
    HF_AVAILABLE = False
    logger.warning("huggingface_hub not installed. Run: pip install huggingface_hub")
    constants = None


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


def classify_model_type(model_id: str, pipeline_tag: str = None) -> str:
    """根据模型名称和pipeline标签分类模型类型"""
    model_lower = model_id.lower()
    
    if pipeline_tag:
        tag_lower = pipeline_tag.lower()
        if 'text-generation' in tag_lower or 'causal-lm' in tag_lower:
            if any(p in model_lower for p in ['vl', 'vision', 'llava', 'qwen-vl', 'internvl']):
                return "VL"
            return "LLM"
        if 'image-to-text' in tag_lower or 'visual-question-answering' in tag_lower:
            return "VL"
        if 'text-to-image' in tag_lower or 'image-generation' in tag_lower:
            return "Generation"
        if 'automatic-speech-recognition' in tag_lower or 'text-to-speech' in tag_lower:
            return "Audio"
        if 'feature-extraction' in tag_lower or 'sentence-embedding' in tag_lower:
            return "Embedding"
    
    for model_type, patterns in MODEL_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, model_id, re.IGNORECASE):
                return model_type
    
    return "Other"


class HuggingFaceCollector:
    """HuggingFace 模型数据收集器"""
    
    DEFAULT_TOP = 200
    HF_MIRROR = "https://hf-mirror.com"
    
    def __init__(self, cache_dir: Optional[Path] = None):
        self.cache_dir = cache_dir or Path("/root/.claude/skills/awesome-llm-model/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.cache_dir / "huggingface_models.json"
        self._api = None
    
    @property
    def api(self) -> Optional[HfApi]:
        if not HF_AVAILABLE:
            return None
        if self._api is None:
            if constants is not None:
                from importlib import reload
                reload(constants)
            self._api = HfApi()
        return self._api
    
    def fetch_models(self, top: int = 200, force_refresh: bool = False) -> List[Dict[str, Any]]:
        if not force_refresh and self.cache_file.exists():
            cache_age = time.time() - self.cache_file.stat().st_mtime
            if cache_age < 6 * 3600:
                logger.info(f"Using cached HuggingFace data (age: {cache_age/3600:.1f}h)")
                return self._load_cache()
        
        if not HF_AVAILABLE:
            logger.error("HuggingFace SDK not available")
            return self._load_cache() if self.cache_file.exists() else []
        
        models = []
        retries = 3
        
        for attempt in range(retries):
            try:
                logger.info(f"Fetching top {top} models from HuggingFace...")
                api = HfApi()
                
                models_batch = api.list_models(
                    sort="likes7d",
                    direction=-1,
                    limit=top
                )
                
                for model in models_batch:
                    pipeline_tag = getattr(model, 'pipeline_tag', None)
                    model_type = classify_model_type(model.id, pipeline_tag)
                    
                    models.append({
                        "id": model.id,
                        "model_name": model.id,
                        "name": model.id.split("/")[-1] if "/" in model.id else model.id,
                        "organization": model.id.split("/")[0] if "/" in model.id else "",
                        "author": getattr(model, 'author', '') or "",
                        "downloads": getattr(model, 'downloads', 0) or 0,
                        "likes": getattr(model, 'likes', 0) or 0,
                        "download_path": f"https://huggingface.co/{model.id}",
                        "mirror_path": f"https://hf-mirror.com/{model.id}",
                        "params": self._extract_params(model.id),
                        "has_ascend_quant": "",
                        "quant_path": "",
                        "platform": "huggingface",
                        "model_type": model_type,
                        "raw_model": {
                            "id": model.id,
                            "downloads": getattr(model, 'downloads', 0),
                            "likes": getattr(model, 'likes', 0),
                            "pipeline_tag": pipeline_tag,
                            "created_at": str(getattr(model, 'created_at', '')) if hasattr(model, 'created_at') else '',
                        }
                    })
                
                logger.info(f"Fetched {len(models)} HuggingFace models")
                break
                
            except Exception as e:
                logger.warning(f"Attempt {attempt+1} failed: {e}")
                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    logger.error(f"Failed after {retries} attempts")
                    cached = self._load_cache()
                    if cached:
                        logger.info(f"Loaded {len(cached)} models from cache")
                        return cached[:top]
        
        self._save_cache(models)
        return models
    
    def _extract_params(self, model_id: str) -> str:
        patterns = [
            r'(\d+[.,]?\d*)[bB]',
            r'(\d+)[mM]',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, model_id)
            if match:
                value = match.group(1)
                if 'b' in pattern.lower():
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
            logger.info(f"Cached {len(models)} HuggingFace models")
        except Exception as e:
            logger.error(f"Failed to save cache: {e}")


def get_huggingface_models(top: int = 200, force_refresh: bool = False) -> List[Dict[str, Any]]:
    collector = HuggingFaceCollector()
    return collector.fetch_models(top=top, force_refresh=force_refresh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    collector = HuggingFaceCollector()
    models = collector.fetch_models(top=10)
    print(f"Fetched {len(models)} models")
    for m in models[:3]:
        print(f"  - {m['name']} ({m.get('model_type', 'Unknown')}): {m['downloads']} downloads, {m['likes']} likes")