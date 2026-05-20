"""
输出生成模块
生成 Markdown、CSV、Excel 格式的排行榜
"""

import csv
import logging
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)


def generate_markdown(models: List[Dict[str, Any]], stats: Dict[str, Any], 
                     output_file: str = None) -> str:
    lines = []
    
    lines.append("# Awesome LLM Model 排行榜")
    lines.append("")
    lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    
    lines.append("## 统计信息")
    lines.append("")
    lines.append(f"- ModelScope 模型数：{stats.get('modelscope_count', 'N/A')}")
    lines.append(f"- HuggingFace 模型数：{stats.get('huggingface_count', 'N/A')}")
    lines.append(f"- 去重后总数：{stats.get('total_after', len(models))}")
    lines.append(f"- 去除重复：{stats.get('duplicates_removed', 0)} 个")
    lines.append("")
    
    lines.append("## 热度评分算法")
    lines.append("")
    lines.append("综合热度分数 = 下载量×0.3 + 点赞数×0.7")
    lines.append("")
    
    lines.append("## 模型类型说明")
    lines.append("")
    lines.append("- **LLM**: 大语言模型 (Large Language Model)")
    lines.append("- **VL**: 视觉语言模型 (Vision Language)")
    lines.append("- **Embedding**: 文本嵌入模型")
    lines.append("- **Generation**: 图像/视频生成模型 (Diffusion-based)")
    lines.append("- **Audio**: 语音/音频模型")
    lines.append("- **Video**: 视频生成模型")
    lines.append("- **Other**: 其他类型模型")
    lines.append("")
    
    lines.append("## 排行榜")
    lines.append("")
    lines.append("| 序号 | 模型名称 | 组织/作者 | 参数量 | 模型类型 | 下载路径 | 昇腾量化 | 量化路径 |")
    lines.append("|------|----------|-----------|--------|----------|----------|----------|----------|")
    
    for model in models:
        rank = model.get("rank", "?")
        name = model.get("name", "")
        org = model.get("organization", "") or model.get("author", "")
        params = model.get("params", "")
        model_type = model.get("model_type", "Other")
        
        download_path = model.get("download_path", "")
        if model.get("platform") == "huggingface" and model.get("mirror_path"):
            download_path = f"[HuggingFace]({download_path}) / [Mirror]({model.get('mirror_path')})"
        else:
            download_path = f"[链接]({download_path})"
        
        has_ascend = model.get("has_ascend_quant", "否")
        quant_path = model.get("quant_path", "")
        if quant_path:
            quant_path = f"[量化权重]({quant_path})"
        
        lines.append(f"| {rank} | {name} | {org} | {params} | {model_type} | {download_path} | {has_ascend} | {quant_path} |")
    
    markdown = "\n".join(lines)
    
    if output_file:
        Path(output_file).write_text(markdown, encoding='utf-8')
        logger.info(f"Markdown saved to {output_file}")
    
    return markdown


def generate_csv(models: List[Dict[str, Any]], output_file: str):
    headers = ["序号", "模型名称", "组织/作者", "参数量", "模型类型", "下载路径", "昇腾量化", "量化路径", 
               "下载量", "点赞数", "热度分数", "平台"]
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for model in models:
            writer.writerow([
                model.get("rank", ""),
                model.get("name", ""),
                model.get("organization", "") or model.get("author", ""),
                model.get("params", ""),
                model.get("model_type", ""),
                model.get("download_path", ""),
                model.get("has_ascend_quant", ""),
                model.get("quant_path", ""),
                model.get("downloads", ""),
                model.get("likes", "") or model.get("stars", ""),
                model.get("popularity_score", ""),
                model.get("platform", "")
            ])
    
    logger.info(f"CSV saved to {output_file}")


def generate_excel(models: List[Dict[str, Any]], output_file: str):
    try:
        import pandas as pd
    except ImportError:
        logger.error("pandas not installed. Run: pip install pandas openpyxl")
        return
    
    data = []
    for model in models:
        data.append({
            "序号": model.get("rank", ""),
            "模型名称": model.get("name", ""),
            "组织/作者": model.get("organization", "") or model.get("author", ""),
            "参数量": model.get("params", ""),
            "模型类型": model.get("model_type", ""),
            "下载路径": model.get("download_path", ""),
            "昇腾量化": model.get("has_ascend_quant", ""),
            "量化路径": model.get("quant_path", ""),
            "下载量": model.get("downloads", ""),
            "点赞数": model.get("likes", "") or model.get("stars", ""),
            "热度分数": model.get("popularity_score", ""),
            "平台": model.get("platform", "")
        })
    
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, engine='openpyxl')
    logger.info(f"Excel saved to {output_file}")


def save_outputs(models: List[Dict[str, Any]], stats: Dict[str, Any], 
                output_dir: str, formats: List[str] = None):
    if formats is None:
        formats = ["markdown"]
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if "markdown" in formats:
        md_file = output_path / f"awesome_llm_models_{timestamp}.md"
        generate_markdown(models, stats, str(md_file))
    
    if "csv" in formats:
        csv_file = output_path / f"awesome_llm_models_{timestamp}.csv"
        generate_csv(models, str(csv_file))
    
    if "excel" in formats:
        xlsx_file = output_path / f"awesome_llm_models_{timestamp}.xlsx"
        generate_excel(models, str(xlsx_file))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    test_models = [
        {"rank": 1, "name": "Qwen2-72B", "organization": "Alibaba", "params": "72B", "model_type": "LLM",
         "download_path": "https://modelscope.cn/Qwen/Qwen2-72B", "downloads": 1000000,
         "likes": 5000, "popularity_score": 3500, "platform": "modelscope"},
        {"rank": 2, "name": "Llama-2-70B", "organization": "Meta", "params": "70B", "model_type": "LLM",
         "download_path": "https://huggingface.co/meta-llama/Llama-2-70B", "downloads": 800000,
         "likes": 4000, "popularity_score": 2800, "platform": "huggingface"},
    ]
    
    stats = {"total_after": 2, "duplicates_removed": 0, "modelscope_count": 1, "huggingface_count": 1}
    
    print(generate_markdown(test_models, stats))