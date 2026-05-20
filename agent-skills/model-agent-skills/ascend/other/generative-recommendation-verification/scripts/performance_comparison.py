#!/usr/bin/env python3
"""
阶段8：性能对比验证脚本
对比使用融合算子(USE_NPU_HSTU=1)与不使用融合算子(USE_NPU_HSTU=0)的性能差异
"""

import os
import sys
import re
import time
import subprocess
import json
import argparse
from pathlib import Path

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

LOG_FILE = "stage_8_perf.log"

class Log:
    def __init__(self, log_file):
        self.log_file = log_file
        
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


def run_training(config, use_npu_hstu, device=0, port=12345, duration=180):
    """运行一次训练并返回性能指标"""
    env = os.environ.copy()
    env["USE_NPU_HSTU"] = "1" if use_npu_hstu else "0"
    env["ENABLE_RAB"] = "0"
    env["ASCEND_RT_VISIBLE_DEVICES"] = str(device)
    env["PYTORCH_NPU_ALLOC_CONF"] = "expandable_segments:True"
    
    mode = "融合算子" if use_npu_hstu else "非融合算子"
    log_file = f"perf_{'hstu' if use_npu_hstu else 'baseline'}.log"
    
    cmd = [
        "python3", "main.py",
        "--gin_config_file", config,
        "--master_port", str(port)
    ]
    
    log = Log(log_file)
    log.info(f"=== 运行训练: {mode} ===")
    log.info(f"命令: {' '.join(cmd)}")
    log.info(f"USE_NPU_HSTU={env['USE_NPU_HSTU']}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            timeout=duration
        )
        
        elapsed = time.time() - start_time
        
        # 解析日志获取性能指标
        output = result.stdout + result.stderr
        
        # 提取 iterations 信息
        iter_matches = re.findall(r'iter[:\s]+(\d+)', output, re.IGNORECASE)
        iterations = int(iter_matches[-1]) if iter_matches else 0
        
        # 提取 loss 信息
        loss_matches = re.findall(r'loss[:\s]+([0-9.]+)', output, re.IGNORECASE)
        final_loss = float(loss_matches[-1]) if loss_matches else None
        
        # 计算速度
        speed = iterations / elapsed if elapsed > 0 else 0
        
        log.info(f"运行时长: {elapsed:.1f}秒")
        log.info(f"迭代次数: {iterations}")
        log.info(f"速度: {speed:.2f} iter/s")
        if final_loss:
            log.info(f"最终 Loss: {final_loss:.4f}")
            
        return {
            "mode": mode,
            "use_npu_hstu": use_npu_hstu,
            "elapsed": elapsed,
            "iterations": iterations,
            "speed": speed,
            "final_loss": final_loss,
            "log_file": log_file,
            "success": result.returncode == 0
        }
        
    except subprocess.TimeoutExpired:
        log.error("训练超时")
        return {
            "mode": mode,
            "use_npu_hstu": use_npu_hstu,
            "elapsed": duration,
            "iterations": 0,
            "speed": 0,
            "final_loss": None,
            "log_file": log_file,
            "success": False,
            "error": "timeout"
        }
    except Exception as e:
        log.error(f"训练失败: {e}")
        return {
            "mode": mode,
            "use_npu_hstu": use_npu_hstu,
            "elapsed": 0,
            "iterations": 0,
            "speed": 0,
            "final_loss": None,
            "log_file": log_file,
            "success": False,
            "error": str(e)
        }


def compare_performance(baseline_result, optimized_result, logger):
    """对比性能结果"""
    logger.info("")
    logger.info("=== 性能对比结果 ===")
    
    if not baseline_result["success"] or not optimized_result["success"]:
        logger.error("✗ 有一个或两个配置运行失败")
        return None
        
    baseline_speed = baseline_result["speed"]
    optimized_speed = optimized_result["speed"]
    
    if baseline_speed > 0:
        speedup = optimized_speed / baseline_speed
    else:
        speedup = 0
        
    logger.info("")
    logger.info("| 指标 | 非融合算子(基准) | 融合算子(优化) | 提升 |")
    logger.info("|------|-----------------|---------------|------|")
    logger.info(f"| 速度 (iter/s) | {baseline_speed:.2f} | {optimized_speed:.2f} | {speedup:.2f}x |")
    
    if baseline_result["final_loss"] and optimized_result["final_loss"]:
        logger.info(f"| 最终 Loss | {baseline_result['final_loss']:.4f} | {optimized_result['final_loss']:.4f} | - |")
    
    logger.info(f"| 运行时间 (s) | {baseline_result['elapsed']:.1f} | {optimized_result['elapsed']:.1f} | - |")
    
    # 性能提升判断
    expected_speedup_min = 5.3
    expected_speedup_max = 15.2
    
    logger.info("")
    if speedup >= expected_speedup_min:
        logger.info(f"✓ 性能提升符合预期: {speedup:.2f}x (期望: {expected_speedup_min}x-{expected_speedup_max}x)")
        return speedup
    elif speedup > 1:
        logger.warn(f"⚠ 性能有提升但低于预期: {speedup:.2f}x (期望: {expected_speedup_min}x-{expected_speedup_max}x)")
        return speedup
    else:
        logger.error(f"✗ 性能无提升或下降: {speedup:.2f}x")
        return speedup


def main():
    parser = argparse.ArgumentParser(description="性能对比验证")
    parser.add_argument("--config", default="configs/ml-1m/hstu-mt-3400.gin", help="配置文件")
    parser.add_argument("--device", type=int, default=0, help="设备编号")
    parser.add_argument("--port", type=int, default=12345, help="主端口")
    parser.add_argument("--duration", type=int, default=180, help="单次运行时间(秒)")
    parser.add_argument("--baseline", action="store_true", help="仅运行基准配置")
    parser.add_argument("--optimized", action="store_true", help="仅运行优化配置")
    parser.add_argument("--log-file", default="stage_8_perf.log", help="日志文件")
    args = parser.parse_args()
    
    logger = Log(args.log_file)
    
    logger.info("=== 性能对比验证 ===")
    logger.info(f"配置文件: {args.config}")
    logger.info(f"设备: NPU {args.device}")
    logger.info(f"单次运行时长: {args.duration}秒")
    
    results = {}
    
    # 运行基准配置 (USE_NPU_HSTU=0)
    if not args.optimized:
        logger.info("")
        results["baseline"] = run_training(
            args.config, 
            use_npu_hstu=False,
            device=args.device,
            port=args.port,
            duration=args.duration
        )
    
    # 运行优化配置 (USE_NPU_HSTU=1)
    if not args.baseline:
        port = args.port + 1 if not args.optimized else args.port
        logger.info("")
        results["optimized"] = run_training(
            args.config,
            use_npu_hstu=True,
            device=args.device,
            port=port,
            duration=args.duration
        )
    
    # 对比结果
    if "baseline" in results and "optimized" in results:
        speedup = compare_performance(results["baseline"], results["optimized"], logger)
        
        # 保存结果
        output_file = "performance_comparison_result.json"
        with open(output_file, 'w') as f:
            json.dump({
                "baseline": results["baseline"],
                "optimized": results["optimized"],
                "speedup": speedup
            }, f, indent=2)
        logger.info(f"结果已保存: {output_file}")
        
        if speedup and speedup >= 5.3:
            return 0
            
    return 1


if __name__ == "__main__":
    sys.exit(main())
