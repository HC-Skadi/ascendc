#!/usr/bin/env python3
"""Agent3: NPU Status Checker"""

import subprocess, sys

def check_npu():
    try:
        result = subprocess.run(["npu-smi", "info"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("NPU Available ✅")
            print(result.stdout)
            return True
    except:
        pass
    print("NPU Not Available ❌")
    return False

if __name__ == "__main__":
    check_npu()
