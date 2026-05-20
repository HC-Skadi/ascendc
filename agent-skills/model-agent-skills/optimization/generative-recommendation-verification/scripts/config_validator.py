#!/usr/bin/env python3
"""
阶段5：配置参数验证脚本
验证 gin 配置文件参数是否符合要求
"""

import os
import re
import sys
from pathlib import Path

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

LOG_FILE = "stage_5_cfg.log"

class Log:
    def __init__(self, log_file):
        self.log_file = log_file
        self.errors = []
        self.warnings = []
        
    def _write(self, level, color, message):
        line = f"{color}[{level}]{NC} {message}"
        print(line)
        with open(self.log_file, 'a') as f:
            f.write(f"[{level}] {message}\n")
            
    def info(self, msg):
        self._write("INFO", GREEN, msg)
        
    def warn(self, msg):
        self._write("WARN", YELLOW, msg)
        self.warnings.append(msg)
        
    def error(self, msg):
        self._write("ERROR", RED, msg)
        self.errors.append(msg)


class GinConfigValidator:
    """gin 配置文件验证器"""
    
    def __init__(self, logger):
        self.logger = logger
        self.errors = []
        
    def validate_dqk(self, value):
        """验证 hstu_encoder.dqk 是否为16的整数倍"""
        try:
            v = int(value)
            if v % 16 == 0:
                return True, f"dqk={v} (✓ 16的整数倍)"
            else:
                return False, f"dqk={v} (✗ 需要是16的整数倍)"
        except ValueError:
            return False, f"dqk={value} (✗ 无效数值)"
            
    def validate_dv(self, value):
        """验证 hstu_encoder.dv 是否为16的整数倍"""
        try:
            v = int(value)
            if v % 16 == 0:
                return True, f"dv={v} (✓ 16的整数倍)"
            else:
                return False, f"dv={v} (✗ 需要是16的整数倍)"
        except ValueError:
            return False, f"dv={value} (✗ 无效数值)"
            
    def validate_max_sequence_length(self, value):
        """验证 train_fn.max_sequence_length"""
        try:
            v = int(value)
            if v == 3389:
                return True, f"max_sequence_length={v} (✓ 正确)"
            elif v > 0:
                return True, f"max_sequence_length={v} (⚠ 建议设置为3389)"
            else:
                return False, f"max_sequence_length={v} (✗ 需要大于0)"
        except ValueError:
            return False, f"max_sequence_length={value} (✗ 无效数值)"
            
    def validate_local_batch_size(self, value):
        """验证 train_fn.local_batch_size"""
        try:
            v = int(value)
            if v == 32:
                return True, f"local_batch_size={v} (✓ 建议值)"
            elif v > 0:
                return True, f"local_batch_size={v} (✓ 有效值)"
            else:
                return False, f"local_batch_size={v} (✗ 需要大于0)"
        except ValueError:
            return False, f"local_batch_size={value} (✗ 无效数值)"
            
    def validate_config(self, config_path):
        """验证整个配置文件"""
        self.logger.info(f"验证配置文件: {config_path}")
        
        if not os.path.exists(config_path):
            self.logger.error(f"✗ 配置文件不存在: {config_path}")
            return False
            
        with open(config_path, 'r') as f:
            content = f.read()
            
        # 定义验证规则
        validations = [
            (r'hstu_encoder\.dqk\s*=\s*(\d+)', self.validate_dqk, "dqk"),
            (r'hstu_encoder\.dv\s*=\s*(\d+)', self.validate_dv, "dv"),
            (r'train_fn\.max_sequence_length\s*=\s*(\d+)', self.validate_max_sequence_length, "max_sequence_length"),
            (r'train_fn\.local_batch_size\s*=\s*(\d+)', self.validate_local_batch_size, "local_batch_size"),
        ]
        
        all_passed = True
        found_params = set()
        
        for pattern, validator, name in validations:
            match = re.search(pattern, content)
            if match:
                found_params.add(name)
                value = match.group(1)
                passed, msg = validator(value)
                if passed:
                    self.logger.info(f"  ✓ {msg}")
                else:
                    self.logger.error(f"  ✗ {msg}")
                    all_passed = False
            else:
                self.logger.warn(f"  ⚠ 缺少参数: {name}")
                
        return all_passed and len(found_params) >= 2  # 至少验证了主要参数


def check_environment_variables(logger):
    """检查环境变量设置"""
    logger.info("检查: 必需环境变量...")
    
    required_vars = {
        "USE_NPU_HSTU": "1",  # 使用融合算子
        "ENABLE_RAB": "0",     # 禁用RAB
    }
    
    optional_vars = {
        "PYTORCH_NPU_ALLOC_CONF": "expandable_segments:True",
        "ASCEND_RT_VISIBLE_DEVICES": "0",
    }
    
    all_ok = True
    
    for var, expected in required_vars.items():
        value = os.environ.get(var)
        if value == expected:
            logger.info(f"  ✓ {var}={value}")
        elif value:
            logger.warn(f"  ⚠ {var}={value} (建议设置为 {expected})")
        else:
            logger.error(f"  ✗ {var} 未设置 (需要设置为 {expected})")
            all_ok = False
            
    for var, recommended in optional_vars.items():
        value = os.environ.get(var)
        if value:
            logger.info(f"  ✓ {var}={value}")
        else:
            logger.warn(f"  ⚠ {var} 未设置 (建议设置为 {recommended})")
            
    return all_ok


def check_config_file_syntax(logger, config_path):
    """检查配置文件语法"""
    logger.info("检查: 配置文件语法...")
    
    if not os.path.exists(config_path):
        logger.error(f"✗ 配置文件不存在: {config_path}")
        return False
        
    try:
        with open(config_path, 'r') as f:
            content = f.read()
            
        # 基本语法检查
        open_braces = content.count('{')
        close_braces = content.count('}')
        
        if open_braces != close_braces:
            logger.error(f"  ✗ 大括号不匹配: {{ {open_braces}, }} {close_braces}")
            return False
            
        # 检查无效字符
        invalid_chars = ['\x00', '\x01', '\x02']
        has_invalid = any(c in content for c in invalid_chars)
        if has_invalid:
            logger.error("  ✗ 配置文件包含无效字符")
            return False
            
        logger.success("  ✓ 配置文件语法正确")
        return True
        
    except Exception as e:
        logger.error(f"  ✗ 无法读取配置文件: {e}")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="配置参数验证")
    parser.add_argument("--config", default="configs/ml-1m/hstu-mt-3400.gin", help="配置文件路径")
    parser.add_argument("--log-file", default="stage_5_cfg.log", help="日志文件路径")
    args = parser.parse_args()
    
    logger = Log(args.log_file)
    
    logger.info("=== 配置参数验证 ===")
    logger.info(f"配置文件: {os.path.abspath(args.config)}")
    logger.info(f"日志文件: {args.log_file}")
    
    results = []
    
    # 1. 检查配置文件语法
    results.append(("配置文件语法", check_config_file_syntax(logger, args.config)))
    
    # 2. 验证 gin 参数
    validator = GinConfigValidator(logger)
    results.append(("gin参数验证", validator.validate_config(args.config)))
    
    # 3. 检查环境变量
    results.append(("环境变量", check_environment_variables(logger)))
    
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
