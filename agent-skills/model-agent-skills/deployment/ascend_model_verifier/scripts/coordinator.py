#!/usr/bin/env python3
"""Pipeline Coordinator"""

import os, subprocess, sys
from datetime import datetime
from pathlib import Path

def log(msg):
    print(f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def run_script(script_name: str, skill_dir: str):
    script_path = Path(skill_dir) / "scripts" / script_name
    result = subprocess.run([sys.executable, str(script_path)], cwd=skill_dir, capture_output=True, text=True)
    return result.returncode

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    
    mode = "once"
    if "--continuous" in sys.argv:
        mode = "continuous"
    
    if mode == "once":
        log("=== Step 1: Fetch Models ===")
        run_script("crawler_huggingface.py", skill_dir)
        run_script("crawler_modelscope.py", skill_dir)
        run_script("merge_model_lists.py", skill_dir)
        
        log("=== Step 2: Download ===")
        run_script("download_model.py", skill_dir)
        
        log("=== Step 3: Validate ===")
        run_script("run_vllm_benchmark.py", skill_dir)
        
        log("=== Step 4: Generate Docs ===")
        run_script("generate_adaptation_guide.py", skill_dir)
        run_script("generate_error_log.py", skill_dir)
        
        log("=== Step 5: Archive ===")
        run_script("archive_and_upload.py", skill_dir)
        
        log("Pipeline complete!")
    else:
        log("Continuous mode - use Ctrl+C to stop")
        while True:
            main()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
