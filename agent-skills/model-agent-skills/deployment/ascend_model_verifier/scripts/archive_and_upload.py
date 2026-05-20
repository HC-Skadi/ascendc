#!/usr/bin/env python3
"""Agent5: Archiver"""

import os, sys, tarfile
from datetime import datetime
from pathlib import Path

def find_completed(skill_dir: str):
    results = Path(skill_dir) / "results"
    if not results.exists():
        return []
    return [d for d in results.iterdir() if d.is_dir() and (d / "documentation.complete").exists()]

def process_model(model_dir: Path):
    # Clean up markers
    for marker in ["download.complete", "validation.complete", "documentation.complete"]:
        (model_dir / marker).unlink(missing_ok=True)
    print(f"Processed: {model_dir.name}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(os.path.dirname(script_dir))
    completed = find_completed(skill_dir)
    for d in completed:
        process_model(d)
    print(f"Processed {len(completed)} models")
    return 0

if __name__ == "__main__":
    sys.exit(main())
