#!/usr/bin/env python3
"""
阶段7：训练过程监控脚本
监控训练日志，确认loss下降、NPU利用率、错误检查
"""

import os
import sys
import re
import time
import subprocess
from pathlib import Path

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

LOG_FILE = "stage_7_monitor.log"

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


def parse_loss_values(log_content):
    """从日志中提取 loss 值"""
    losses = []
    pattern = re.compile(r'loss[:\s]+([0-9.]+)', re.IGNORECASE)
    for match in pattern.finditer(log_content):
        try:
            loss = float(match.group(1))
            losses.append(loss)
        except ValueError:
            continue
    return losses


def check_npu_utilization(logger, device=0):
    """检查 NPU 利用率"""
    try:
        result = subprocess.run(
            ['npu-smi', 'info', '-t', 'util', '-i', str(device)],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            output = result.stdout
            util_match = re.search(r'Utilization\s*:\s*(\d+)%', output)
            if util_match:
                util = int(util_match.group(1))
                if util > 0:
                    logger.info(f"  ✓ NPU 利用率: {util}%")
                    return True
                else:
                    logger.warn(f"  ⚠ NPU 利用率: {util}% (可能空闲)")
                    return False
    except Exception as e:
        logger.warn(f"  ⚠ 无法获取 NPU 利用率: {e}")
    return False


def check_error_logs(logger, log_content):
    """检查错误日志"""
    error_patterns = [
        (r'error[:\s]+(.+)', 'ERROR'),
        (r'exception[:\s]+(.+)', 'EXCEPTION'),
        (r'traceback.*', 'TRACEBACK'),
        (r'out of memory', 'OOM'),
        (r'cuda.*out.*memory', 'CUDA_OOM'),
        (r'npu.*error', 'NPU_ERROR'),
    ]
    
    found_errors = []
    for pattern, name in error_patterns:
        matches = re.findall(pattern, log_content, re.IGNORECASE)
        if matches:
            for match in matches[:3]:
                found_errors.append(f"{name}: {match[:100]}")
                
    if found_errors:
        logger.error("检测到错误:")
        for err in found_errors[:5]:
            logger.error(f"  {err}")
        return False
        
    return True


def monitor_training(logger, log_file, duration=300, check_interval=10):
    """监控训练过程"""
    logger.info(f"开始监控训练日志: {log_file}")
    logger.info(f"监控时长: {duration}秒")
    
    if not os.path.exists(log_file):
        logger.error(f"日志文件不存在: {log_file}")
        return False
        
    start_size = os.path.getsize(log_file)
    start_time = time.time()
    
    last_loss = None
    loss_decreasing = False
    loss_values = []
    
    while time.time() - start_time < duration:
        time.sleep(check_interval)
        
        current_size = os.path.getsize(log_file)
        
        if current_size > start_size:
            logger.info(f"  日志增长正常 (+{current_size - start_size} bytes)")
            start_size = current_size
            
            with open(log_file, 'r') as f:
                f.seek(max(0, current_size - 10000))
                recent_content = f.read()
                
            losses = parse_loss_values(recent_content)
            if losses:
                last_loss = losses[-1]
                loss_values.append(last_loss)
                
                if len(loss_values) >= 2:
                    if loss_values[-1] < loss_values[-2]:
                        loss_decreasing = True
                        
                logger.info(f"  最新 Loss: {last_loss:.4f} (历史: {len(loss_values)} 个)")
        else:
            logger.warn("  日志无更新...")
            
        # 检查 NPU 利用率
        check_npu_utilization(logger)
        
    # 最终分析
    logger.info("")
    logger.info("=== 监控结果 ===")
    
    if loss_values:
        logger.info(f"Loss 值数量: {len(loss_values)}")
        logger.info(f"最新 Loss: {loss_values[-1]:.4f}")
        logger.info(f"最低 Loss: {min(loss_values):.4f}")
        
        if loss_decreasing:
            logger.info("✓ Loss 正常下降")
        else:
            logger.warn("⚠ Loss 未呈现明显下降趋势")
            
    with open(log_file, 'r') as f:
        full_content = f.read()
        
    if check_error_logs(logger, full_content):
        logger.info("✓ 无错误日志")
        
    return len(loss_values) > 0 and not logger.errors


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="训练过程监控")
    parser.add_argument("--log-file", default="training.log", help="训练日志文件")
    parser.add_argument("--duration", type=int, default=300, help="监控时长(秒)")
    parser.add_argument("--interval", type=int, default=10, help="检查间隔(秒)")
    parser.add_argument("--device", type=int, default=0, help="NPU设备编号")
    parser.add_argument("--log-output", default="stage_7_monitor.log", help="监控日志输出")
    args = parser.parse_args()
    
    logger = Log(args.log_output)
    
    logger.info("=== 训练过程监控验证 ===")
    logger.info(f"监控日志: {args.log_file}")
    logger.info(f"输出日志: {args.log_output}")
    
    result = monitor_training(
        logger, 
        args.log_file, 
        duration=args.duration,
        check_interval=args.interval
    )
    
    if result:
        logger.info("")
        logger.info("✓ 训练过程监控验证通过")
        return 0
    else:
        logger.error("")
        logger.error("✗ 训练过程监控验证失败")
        return 1


if __name__ == "__main__":
    sys.exit(main())
