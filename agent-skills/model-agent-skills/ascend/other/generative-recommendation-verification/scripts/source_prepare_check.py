#!/usr/bin/env python3
"""
阶段4：源码与数据准备验证脚本
验证 RecSDK 仓库、generative-recommenders 源码、ml-1m 数据集
"""

import os
import subprocess
import sys
from pathlib import Path

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

LOG_FILE = "stage_4_src.log"

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


def run_command(cmd, cwd=None):
    """执行命令并返回输出"""
    try:
        result = subprocess.run(
            cmd, 
            cwd=cwd,
            capture_output=True, 
            text=True, 
            timeout=120,
            shell=isinstance(cmd, str)
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Command timed out"
    except Exception as e:
        return False, "", str(e)


def check_recsdk_repo(logger, workdir):
    """检查 RecSDK 仓库"""
    logger.info("检查: RecSDK 仓库...")
    
    recsdk_path = Path(workdir) / "RecSDK"
    
    if not recsdk_path.exists():
        logger.error(f"✗ RecSDK 仓库不存在: {recsdk_path}")
        return False
        
    # 检查 .git 目录
    if not (recsdk_path / ".git").exists():
        logger.warn(f"⚠ RecSDK 不是 git 仓库")
        
    # 检查分支
    success, stdout, stderr = run_command(["git", "branch"], cwd=recsdk_path)
    if success:
        current = None
        for line in stdout.split("\n"):
            if "*" in line:
                current = line.replace("*", "").strip()
                break
        if current:
            logger.info(f"  当前分支: {current}")
            if "branch_v7.0.0-POC_torch" in current or "v7.0.0" in current:
                logger.success("✓ RecSDK 分支正确")
                return True
            else:
                logger.warn(f"⚠ 分支不是 branch_v7.0.0-POC_torch: {current}")
                return True  # 不阻塞
                
    # 检查 remote
    success, stdout, stderr = run_command(["git", "remote", "-v"], cwd=recsdk_path)
    if success and stdout:
        logger.info(f"  Remote: {stdout.split()[0] if stdout else 'N/A'}")
        
    logger.success("✓ RecSDK 仓库存在")
    return True


def check_generative_recommenders(logger, workdir):
    """检查 generative-recommenders 源码"""
    logger.info("检查: generative-recommenders 源码...")
    
    gr_path = Path(workdir) / "generative-recommenders"
    
    if not gr_path.exists():
        logger.error(f"✗ generative-recommenders 源码不存在: {gr_path}")
        return False
        
    # 检查 NPU_GR.patch 是否已应用
    patch_path = gr_path / "NPU_GR.patch"
    if patch_path.exists():
        logger.info("  ✓ NPU_GR.patch 文件存在")
    else:
        logger.warn("  ⚠ NPU_GR.patch 文件不存在")
        
    # 检查 train.py 是否存在
    train_py = gr_path / "train.py"
    if train_py.exists():
        logger.info(f"  ✓ train.py 存在")
        
        # 检查是否已注释掉 seed_all
        with open(train_py, 'r') as f:
            content = f.read()
            
        if "from msprobe.pytorch import seed_all" in content:
            # 检查是否被注释
            for line in content.split("\n"):
                if "from msprobe" in line and "seed_all" in line:
                    if line.strip().startswith("#"):
                        logger.success("  ✓ seed_all 引用已注释")
                    else:
                        logger.warn("  ⚠ seed_all 引用未注释（建议注释）")
                    break
    else:
        logger.error(f"  ✗ train.py 不存在")
        return False
        
    logger.success("✓ generative-recommenders 源码检查通过")
    return True


def check_dataset(logger, workdir):
    """检查 ml-1m 数据集"""
    logger.info("检查: ml-1m 数据集...")
    
    # 数据集可能在多个位置
    possible_paths = [
        Path(workdir) / "data" / "ml-1m",
        Path(workdir) / "ml-1m",
        Path(workdir) / "RecSDK" / "data" / "ml-1m",
        Path(".") / "ml-1m",
    ]
    
    dataset_found = False
    for data_path in possible_paths:
        if data_path.exists():
            # 检查必要文件
            required_files = ["train.csv", "test.csv", "item.csv"]
            all_exist = True
            
            for req_file in required_files:
                if not (data_path / req_file).exists():
                    all_exist = False
                    break
                    
            if all_exist:
                logger.info(f"  数据集位置: {data_path}")
                dataset_found = True
                break
            else:
                logger.warn(f"  ⚠ 数据集目录存在但文件不完整: {data_path}")
                
    if dataset_found:
        logger.success("✓ ml-1m 数据集检查通过")
        return True
    else:
        logger.error("✗ ml-1m 数据集未找到或文件不完整")
        logger.info("  期望文件: train.csv, test.csv, item.csv")
        logger.info("  搜索路径:")
        for p in possible_paths:
            logger.info(f"    - {p}")
        return False


def check_preprocess_script(logger, workdir):
    """检查预处理脚本执行状态"""
    logger.info("检查: preprocess_public_data.py...")
    
    # 查找预处理脚本
    script_paths = [
        Path(workdir) / "RecSDK" / "preprocess_public_data.py",
        Path(workdir) / "generative-recommenders" / "preprocess_public_data.py",
        Path(".") / "preprocess_public_data.py",
    ]
    
    script_found = False
    for script_path in script_paths:
        if script_path.exists():
            logger.info(f"  预处理脚本位置: {script_path}")
            script_found = True
            
            # 检查脚本是否可执行
            if os.access(script_path, os.X_OK):
                logger.info("  ✓ 脚本有执行权限")
            else:
                logger.warn("  ⚠ 脚本没有执行权限")
                
            break
            
    if not script_found:
        logger.warn("⚠ preprocess_public_data.py 未找到（可能已预处理或在其他位置）")
        return True  # 不阻塞
        
    return True


def check_workdir_structure(logger, workdir):
    """检查工作目录结构"""
    logger.info("检查: 工作目录结构...")
    
    expected_dirs = [
        "RecSDK",
        "generative-recommenders",
    ]
    
    for dirname in expected_dirs:
        dirpath = Path(workdir) / dirname
        if dirpath.exists():
            logger.info(f"  ✓ {dirname}/")
        else:
            logger.warn(f"  ⚠ {dirname}/ 不存在")
            
    return True


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="源码与数据准备验证")
    parser.add_argument("--workdir", default=".", help="工作目录路径")
    parser.add_argument("--log-file", default="stage_4_src.log", help="日志文件路径")
    args = parser.parse_args()
    
    logger = Log(args.log_file)
    
    logger.info("=== 源码与数据准备验证 ===")
    logger.info(f"工作目录: {os.path.abspath(args.workdir)}")
    logger.info(f"日志文件: {args.log_file}")
    
    results = []
    
    # 执行各项检查
    results.append(("工作目录结构", check_workdir_structure(logger, args.workdir)))
    results.append(("RecSDK仓库", check_recsdk_repo(logger, args.workdir)))
    results.append(("generative-recommenders", check_generative_recommenders(logger, args.workdir)))
    results.append(("预处理脚本", check_preprocess_script(logger, args.workdir)))
    results.append(("ml-1m数据集", check_dataset(logger, args.workdir)))
    
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
        logger.warn(f"⚠ 部分检查有问题 ({passed}/{total})")
        return 0 if passed >= total - 1 else 1


if __name__ == "__main__":
    sys.exit(main())
