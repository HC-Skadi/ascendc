#!/usr/bin/env python3
"""Agent3: vLLM Benchmark"""

import gc, json, os, sys, time
from datetime import datetime
from pathlib import Path

def find_pending(skill_dir: str):
    results = Path(skill_dir) / "results"
    if not results.exists():
        return None
    for d in results.iterdir():
        if d.is_dir() and (d / "download.complete").exists() and not (d / "validation.complete").exists():
            return {"name": d.name.replace("-", "/"), "folder_name": d.name, "result_dir": d}
    return None

def run_benchmark(model_info: dict, skill_dir: str):
    result = {"model": model_info["name"], "timestamp": datetime.utcnow().isoformat() + "Z", "vllm_version": "0.17.0"}
    try:
        from vllm import LLM, SamplingParams
        model_path = Path(skill_dir) / "downloaded_models" / model_info["folder_name"]
        llm = LLM(model=str(model_path), tensor_parallel_size=1, trust_remote_code=True, max_model_len=4096, quantization="ascend")
        outputs = llm.generate(["Hello", "AI is"], SamplingParams(max_tokens=128))
        result["success"] = True
        result["tokens"] = sum(len(o.outputs[0].token_ids) if o.outputs else 0 for o in outputs)
        del llm; gc.collect()
    except Exception as e:
        result["success"] = False
        result["error"] = str(e)
    with open(model_info["result_dir"] / "benchmark_result.json", "w") as f:
        json.dump(result, f, indent=2)
    (model_info["result_dir"] / "validation.complete").write_text(f"Done: {datetime.utcnow().isoformat()}Z")
    return result

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    model = find_pending(skill_dir)
    if model:
        result = run_benchmark(model, skill_dir)
        print(f"Result: {result.get('success', False)}")
        return 0
    return 0

if __name__ == "__main__":
    sys.exit(main())
