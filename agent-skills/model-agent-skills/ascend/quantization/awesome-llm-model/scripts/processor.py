"""
数据处理和去重模块
"""

import math
import logging
from typing import List, Dict, Any, Tuple

logger = logging.getLogger(__name__)

DOWNLOAD_WEIGHT = 0.3
LIKE_WEIGHT = 0.7


def normalize_downloads(downloads: int) -> float:
    if downloads <= 0:
        return 0.0
    return math.log10(downloads + 1) * 10


def calculate_popularity_score(downloads: int, likes: int) -> float:
    normalized_downloads = normalize_downloads(downloads)
    score = normalized_downloads * DOWNLOAD_WEIGHT + likes * LIKE_WEIGHT
    return round(score, 2)


def normalize_model_name(name: str) -> str:
    import re
    name = name.lower().strip()
    name = re.sub(r'[\s_-]+', '', name)
    name = re.sub(r'[v](\d)', r'\1', name)
    return name


def extract_base_name(model_id: str) -> str:
    import re
    patterns = [
        r'^(.*?)[-/]v?[\d.]+$',
        r'^(.*?)[-/]?checkpoint.*$',
    ]
    for pattern in patterns:
        match = re.match(pattern, model_id, re.IGNORECASE)
        if match:
            return match.group(1)
    return model_id


def is_same_model(name1: str, name2: str) -> bool:
    norm1 = normalize_model_name(name1)
    norm2 = normalize_model_name(name2)
    
    if norm1 == norm2:
        return True
    
    base1 = normalize_model_name(extract_base_name(name1))
    base2 = normalize_model_name(extract_base_name(name2))
    
    if base1 and base2 and base1 == base2:
        return True
    
    return False


def deduplicate_models(models: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    seen = {}
    duplicates = []
    
    for model in models:
        model_name = model.get("model_name", model.get("name", ""))
        normalized = normalize_model_name(model_name)
        base_name = normalize_model_name(extract_base_name(model_name))
        
        key = base_name if base_name else normalized
        
        if key not in seen:
            seen[key] = model
        else:
            existing = seen[key]
            existing_score = calculate_popularity_score(
                existing.get("downloads", 0),
                existing.get("likes", 0) or existing.get("stars", 0)
            )
            new_score = calculate_popularity_score(
                model.get("downloads", 0),
                model.get("likes", 0) or model.get("stars", 0)
            )
            
            if new_score > existing_score:
                duplicates.append(existing)
                seen[key] = model
            else:
                duplicates.append(model)
    
    deduped = list(seen.values())
    
    stats = {
        "total_before": len(models),
        "total_after": len(deduped),
        "duplicates_removed": len(duplicates),
        "dedup_rate": f"{len(duplicates)/len(models)*100:.1f}%" if models else "0%"
    }
    
    logger.info(f"Deduplication: {stats['total_before']} -> {stats['total_after']} ({stats['duplicates_removed']} removed)")
    
    return deduped, stats


def process_and_rank_models(models: List[Dict[str, Any]], top: int = 200) -> List[Dict[str, Any]]:
    for model in models:
        downloads = model.get("downloads", 0)
        likes = model.get("likes", 0) or model.get("stars", 0)
        model["popularity_score"] = calculate_popularity_score(downloads, likes)
    
    deduped, stats = deduplicate_models(models)
    
    deduped.sort(key=lambda x: x.get("popularity_score", 0), reverse=True)
    
    for i, model in enumerate(deduped[:top], 1):
        model["rank"] = i
    
    return deduped[:top], stats


def merge_platform_data(modelscope_models: List[Dict[str, Any]], 
                       huggingface_models: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged = []
    
    for m in modelscope_models:
        m["source_platform"] = "modelscope"
        merged.append(m)
    
    for m in huggingface_models:
        m["source_platform"] = "huggingface"
        merged.append(m)
    
    return merged


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    test_models = [
        {"name": "Qwen/Qwen2-7B", "downloads": 1000000, "likes": 5000, "platform": "huggingface", "model_type": "LLM"},
        {"name": "Qwen2-7B", "downloads": 500000, "likes": 3000, "platform": "modelscope", "model_type": "LLM"},
        {"name": "Llama-2-7B", "downloads": 2000000, "likes": 8000, "platform": "huggingface", "model_type": "LLM"},
        {"name": "meta-llama/Llama-2-7B", "downloads": 1500000, "likes": 6000, "platform": "huggingface", "model_type": "LLM"},
    ]
    
    processed, stats = process_and_rank_models(test_models)
    
    print(f"\nStatistics: {stats}")
    print("\nRanked models:")
    for m in processed:
        print(f"  {m.get('rank', '?')}. {m.get('name')} ({m.get('model_type', 'Unknown')}) - Score: {m.get('popularity_score')}")