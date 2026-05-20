"""
Awesome LLM Model 数据收集主脚本
整合 ModelScope 和 HuggingFace 数据，生成热门模型排行榜
"""

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from modelscope_api import ModelScopeCollector
from huggingface_api import HuggingFaceCollector
from processor import process_and_rank_models, merge_platform_data
from output import generate_markdown, generate_csv, generate_excel, save_outputs

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

DEFAULT_TOP = 200
OUTPUT_DIR = Path("/root/.claude/skills/awesome-llm-model/output")


def collect_all_models(top: int = DEFAULT_TOP, force_refresh: bool = False, 
                      platform: str = None) -> tuple:
    """
    收集所有平台模型数据
    
    Returns:
        (modelscope_models, huggingface_models, collected_stats)
    """
    stats = {"modelscope_count": 0, "huggingface_count": 0}
    
    modelscope_models = []
    huggingface_models = []
    
    if platform is None or platform == "modelscope":
        try:
            logger.info("Collecting ModelScope models...")
            ms_collector = ModelScopeCollector()
            modelscope_models = ms_collector.fetch_models(top=top, force_refresh=force_refresh)
            stats["modelscope_count"] = len(modelscope_models)
            logger.info(f"Collected {len(modelscope_models)} ModelScope models")
        except Exception as e:
            logger.error(f"Failed to collect ModelScope models: {e}")
    
    if platform is None or platform == "huggingface":
        try:
            logger.info("Collecting HuggingFace models...")
            hf_collector = HuggingFaceCollector()
            huggingface_models = hf_collector.fetch_models(top=top, force_refresh=force_refresh)
            stats["huggingface_count"] = len(huggingface_models)
            logger.info(f"Collected {len(huggingface_models)} HuggingFace models")
        except Exception as e:
            logger.error(f"Failed to collect HuggingFace models: {e}")
    
    return modelscope_models, huggingface_models, stats


def main():
    parser = argparse.ArgumentParser(description="Awesome LLM Model 数据收集工具")
    parser.add_argument("--platform", choices=["modelscope", "huggingface"], 
                       help="指定平台（默认收集所有）")
    parser.add_argument("--top", type=int, default=DEFAULT_TOP,
                       help=f"获取数量（默认{DEFAULT_TOP}）")
    parser.add_argument("--force-refresh", action="store_true",
                       help="强制刷新缓存")
    parser.add_argument("--output-format", choices=["markdown", "csv", "excel"], 
                       default="markdown", nargs="+",
                       help="输出格式（默认markdown）")
    parser.add_argument("--output-dir", type=str, default=str(OUTPUT_DIR),
                       help=f"输出目录（默认{OUTPUT_DIR}）")
    parser.add_argument("--deduplicate", action="store_true", default=True,
                       help="执行去重（默认True）")
    parser.add_argument("--no-deduplicate", dest="deduplicate", action="store_false",
                       help="不执行去重")
    parser.add_argument("--cache-ttl", type=int, default=6*3600,
                       help="缓存有效期（秒，默认6小时）")
    
    args = parser.parse_args()
    
    logger.info(f"Starting collection: top={args.top}, platform={args.platform or 'all'}")
    
    modelscope_models, huggingface_models, collect_stats = collect_all_models(
        top=args.top,
        force_refresh=args.force_refresh
    )
    
    if not modelscope_models and not huggingface_models:
        logger.error("No models collected. Check API access and credentials.")
        sys.exit(1)
    
    all_models = modelscope_models + huggingface_models
    
    if args.deduplicate:
        logger.info("Deduplicating models...")
        processed_models, dedup_stats = process_and_rank_models(all_models, top=args.top)
    else:
        for i, m in enumerate(all_models, 1):
            m["rank"] = i
        processed_models = all_models[:args.top]
        dedup_stats = {
            "total_before": len(all_models),
            "total_after": len(processed_models),
            "duplicates_removed": 0
        }
    
    final_stats = {
        **collect_stats,
        **dedup_stats
    }
    
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    formats = args.output_format if isinstance(args.output_format, list) else [args.output_format]
    
    for fmt in formats:
        if fmt == "markdown":
            output_file = output_path / "awesome_llm_models.md"
            markdown = generate_markdown(processed_models, final_stats, str(output_file))
            print(f"\n{'='*60}")
            print(f"Markdown output saved to: {output_file}")
            print(f"{'='*60}\n")
            print(markdown[:2000] + "..." if len(markdown) > 2000 else markdown)
            
        elif fmt == "csv":
            output_file = output_path / "awesome_llm_models.csv"
            generate_csv(processed_models, str(output_file))
            print(f"\nCSV output saved to: {output_file}")
            
        elif fmt == "excel":
            output_file = output_path / "awesome_llm_models.xlsx"
            generate_excel(processed_models, str(output_file))
            print(f"\nExcel output saved to: {output_file}")
    
    print(f"\n{'='*60}")
    print("Collection Summary")
    print(f"{'='*60}")
    print(f"ModelScope models: {final_stats.get('modelscope_count', 0)}")
    print(f"HuggingFace models: {final_stats.get('huggingface_count', 0)}")
    print(f"Total before dedup: {final_stats.get('total_before', len(all_models))}")
    print(f"Duplicates removed: {final_stats.get('duplicates_removed', 0)}")
    print(f"Final count: {final_stats.get('total_after', len(processed_models))}")


if __name__ == "__main__":
    main()
