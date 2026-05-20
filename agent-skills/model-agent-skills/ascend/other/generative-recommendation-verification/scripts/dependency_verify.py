#!/usr/bin/env python3
"""
阶段2：依赖安装验证脚本
验证 torch_npu、mindxsdk、Python 版本等依赖
"""

import subprocess
import sys
import re
import os
from pathlib import Path

# 颜色定义
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

LOG_FILE = "stage_2_dep.log"

class Log:
    def __init__(self, log_file):
        self.log_file = log_file
        self.errors = []
        
    def _write(self, level, color, message):
        line = f"{color}[{level}]{NC} {message}"
        print(line)
        with open(self.log_file, 'a') as f:
            f.write(f"[{level}] {message}\n")
            
    def info(self, msg):
        self._write("INFO", GREEN, msg)
        
    def warn(self, msg):
        self._write("WARN", YELLOW, msg)
        
    def error(self, msg):
        self._write("ERROR", RED, msg)
        self.errors.append(msg)
        
    def success(self, msg):
        self._write("OK", GREEN, msg)


def run_command(cmd, shell=False):
    """执行命令并返回输出"""
    try:
        if shell:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
        else:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)


def check_python_version(logger):
    """检查 Python 版本"""
    logger.info("检查: Python 版本...")
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 11:
        logger.success(f"✓ Python 版本符合要求: {version_str} (需要 ≥3.11)")
        return True
    else:
        logger.error(f"✗ Python 版本过低: {version_str} (需要 ≥3.11)")
        return False


def check_torch(logger):
    """检查 PyTorch 版本"""
    logger.info("检查: PyTorch 版本...")
    success, stdout, stderr = run_command([sys.executable, "-c", "import torch; print(torch.__version__)"])
    
    if success:
        version = stdout.strip()
        logger.success(f"✓ PyTorch 已安装: {version}")
        
        # 检查 CUDA/NPU 可用性
        has_npu = False
        try:
            _, npu_out, _ = run_command([sys.executable, "-c", "import torch; print(torch.npu.is_available())"])
            has_npu = "True" in npu_out
        except:
            pass
            
        if has_npu:
            logger.info("  ✓ NPU 可用")
        else:
            logger.warn("  ⚠ NPU 不可用（可能未安装 torch_npu）")
        return True
    else:
        logger.error(f"✗ PyTorch 未安装: {stderr}")
        return False


def check_torch_npu(logger):
    """检查 torch_npu 版本"""
    logger.info("检查: torch_npu 版本...")
    success, stdout, stderr = run_command([sys.executable, "-m", "pip", "show", "torch_npu"])
    
    if success and "Version:" in stdout:
        match = re.search(r"Version:\s*(.+)", stdout)
        if match:
            version = match.group(1).strip()
            
            # 检查兼容版本
            compatible_versions = ["2.1.0.post9", "2.1.0.post3", "2.0.0"]
            is_compatible = any(v in version for v in compatible_versions)
            
            if is_compatible or "post" in version:
                logger.success(f"✓ torch_npu 版本符合要求: {version}")
                return True
            else:
                logger.warn(f"⚠ torch_npu 版本: {version} (建议使用 2.1.0.post9 或兼容版本)")
                return True  # 不阻塞，使用警告
    else:
        logger.error("✗ torch_npu 未安装或版本未知")
        return False


def check_mindxsdk(logger):
    """检查 mindxsdk-mxec-add-ons 安装"""
    logger.info("检查: mindxsdk-mxec-add-ons...")
    success, stdout, stderr = run_command([sys.executable, "-m", "pip", "list"])
    
    if success:
        packages = stdout.lower()
        if "mindxsdk" in packages or "mxec" in packages:
            logger.success("✓ mindxsdk-mxec-add-ons 已安装")
            return True
        else:
            logger.error("✗ mindxsdk-mxec-add-ons 未安装")
            return False
    else:
        logger.error("✗ 无法检查已安装包")
        return False


def check_numpy(logger):
    """检查 numpy 版本"""
    logger.info("检查: NumPy 版本...")
    success, stdout, stderr = run_command([sys.executable, "-c", "import numpy; print(numpy.__version__)"])
    
    if success:
        version = stdout.strip()
        logger.success(f"✓ NumPy 已安装: {version}")
        return True
    else:
        logger.error(f"✗ NumPy 未安装: {stderr}")
        return False


def check_other_dependencies(logger):
    """检查其他必要依赖"""
    logger.info("检查: 其他必要依赖...")
    
    dependencies = [
        ("yaml", "PyYAML"),
        ("gin", "gin"),
        ("torch.nn.functional", "torch.nn.functional"),
    ]
    
    all_ok = True
    for module_name, package_name in dependencies:
        success, stdout, stderr = run_command([sys.executable, "-c", f"import {module_name}; print('{module_name}')"])
        if success:
            logger.info(f"  ✓ {package_name}")
        else:
            logger.warn(f"  ⚠ {package_name} 未安装")
            all_ok = False
    
    return all_ok


def check_env_variables(logger):
    """检查环境变量"""
    logger.info("检查: 关键环境变量...")
    
    env_vars = [
        "ASCEND_VISIBLE_DEVICES",
        "PYTORCH_NPU_ALLOC_CONF",
        "USE_NPU_HSTU",
    ]
    
    all_ok = True
    for var in env_vars:
        value = os.environ.get(var)
        if value:
            logger.info(f"  ✓ {var}={value}")
        else:
            logger.warn(f"  ⚠ {var} 未设置")
            
    return all_ok


def main():
    logger = Log(LOG_FILE)
    
    logger.info("=== 依赖安装验证 ===")
    logger.info(f"Python: {sys.version}")
    logger.info(f"工作目录: {os.getcwd()}")
    
    results = []
    
    # 执行各项检查
    results.append(("Python版本", check_python_version(logger)))
    results.append(("PyTorch", check_torch(logger)))
    results.append(("torch_npu", check_torch_npu(logger)))
    results.append(("mindxsdk-mxec", check_mindxsdk(logger)))
    results.append(("NumPy", check_numpy(logger)))
    results.append(("其他依赖", check_other_dependencies(logger)))
    results.append(("环境变量", check_env_variables(logger)))
    
    # 总结
    logger.info("")
    logger.info("=== 验证总结 ===")
    
    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    
    for name, ok in results:
        status = "✓" if ok else "✗"
        logger.info(f"  {status} {name}")
    
    if passed == total:
        logger.info(f"✓ 所有检查通过！ ({passed}/{total})")
        return 0
    else:
        logger.error(f"✗ 部分检查失败 ({passed}/{total})")
        return 1


if __name__ == "__main__":
    sys.exit(main())
