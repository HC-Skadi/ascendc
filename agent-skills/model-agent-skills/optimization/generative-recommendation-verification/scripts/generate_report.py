#!/usr/bin/env python3
"""
生成式推荐模型验证报告生成脚本
汇总所有验证阶段的结果，生成完整报告
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

class ReportGenerator:
    STAGES = [
        ("1", "环境基础验证", "environment_check.sh"),
        ("2", "依赖安装验证", "dependency_verify.py"),
        ("3", "算子编译验证", "operator_compile_test.sh"),
        ("4", "源码与数据准备验证", "source_prepare_check.py"),
        ("5", "配置参数验证", "config_validator.py"),
        ("6", "训练启动验证", "training_launcher.sh"),
        ("7", "训练过程监控验证", "training_monitor.py"),
        ("8", "性能对比验证", "performance_comparison.py"),
    ]
    
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def find_log_file(self, stage_name):
        """查找阶段日志文件"""
        possible_names = [
            f"stage_{stage_name[0]}_{stage_name[2].split('.')[0]}.log",
            f"stage_{stage_name[0]}_*.log",
            f"{stage_name[2].split('.')[0]}.log",
        ]
        
        for pattern in possible_names:
            if "*" in pattern:
                import glob
                matches = glob.glob(str(self.output_dir / pattern))
                if matches:
                    return matches[0]
            else:
                path = self.output_dir / pattern
                if path.exists():
                    return str(path)
        return None
        
    def parse_log_result(self, log_file):
        """解析日志文件判断结果"""
        if not log_file or not os.path.exists(log_file):
            return "未运行", "日志文件不存在"
            
        with open(log_file, 'r') as f:
            content = f.read()
            
        if "所有检查通过" in content or "验证通过" in content or "✓" in content:
            if "失败" not in content.lower() and "error" not in content.lower():
                return "通过", None
                
        if "ERROR" in content or "✗" in content:
            errors = []
            for line in content.split('\n'):
                if 'ERROR' in line or '✗' in line:
                    errors.append(line.strip())
            return "失败", errors[:3]
            
        return "未知", None
        
    def get_device_info(self):
        """获取设备信息"""
        import subprocess
        info = {}
        
        try:
            result = subprocess.run(
                ['npu-smi', 'info'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                info['npu_smi'] = result.stdout[:500]
        except:
            info['npu_smi'] = "无法获取"
            
        try:
            result = subprocess.run(
                ['gcc', '--version'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                info['gcc'] = result.stdout.split('\n')[0]
        except:
            info['gcc'] = "未安装"
            
        return info
        
    def generate_json_report(self, stage_results):
        """生成 JSON 格式报告"""
        report = {
            "report_version": "1.0",
            "generated_at": datetime.now().isoformat(),
            "device_info": self.get_device_info(),
            "stages": [],
            "summary": {
                "total": len(self.STAGES),
                "passed": sum(1 for _, status, _ in stage_results if status == "通过"),
                "failed": sum(1 for _, status, _ in stage_results if status == "失败"),
                "not_run": sum(1 for _, status, _ in stage_results if status == "未运行"),
            }
        }
        
        for i, (stage_num, stage_name, script) in enumerate(self.STAGES):
            status, errors = stage_results[i]
            log_file = self.find_log_file((stage_num, stage_name, script))
            
            stage_data = {
                "stage": stage_num,
                "name": stage_name,
                "script": script,
                "status": status,
                "log_file": log_file,
            }
            
            if errors:
                stage_data["errors"] = errors
                
            report["stages"].append(stage_data)
            
        return report
        
    def generate_markdown_report(self, stage_results, device_info):
        """生成 Markdown 格式报告"""
        md = []
        md.append("# 生成式推荐模型验证报告")
        md.append("")
        md.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md.append("")
        
        # 设备信息
        md.append("## 设备信息")
        md.append("")
        md.append("```")
        md.append(f"NPU信息:")
        md.append(device_info.get('npu_smi', '无法获取')[:200])
        md.append(f"GCC版本: {device_info.get('gcc', '未知')}")
        md.append("```")
        md.append("")
        
        # 验证结果汇总
        passed = sum(1 for _, status, _ in stage_results if status == "通过")
        failed = sum(1 for _, status, _ in stage_results if status == "失败")
        not_run = sum(1 for _, status, _ in stage_results if status == "未运行")
        
        md.append("## 验证结果汇总")
        md.append("")
        md.append(f"| 状态 | 数量 |")
        md.append(f"|------|------|")
        md.append(f"| ✓ 通过 | {passed} |")
        md.append(f"| ✗ 失败 | {failed} |")
        md.append(f"| - 未运行 | {not_run} |")
        md.append("")
        
        # 各阶段详情
        md.append("## 各阶段验证详情")
        md.append("")
        md.append("| 阶段 | 验证项 | 脚本 | 状态 |")
        md.append("|------|--------|------|------|")
        
        for stage_num, stage_name, script in self.STAGES:
            status, _ = stage_results[self.STAGES.index((stage_num, stage_name, script))]
            status_icon = "✓" if status == "通过" else ("✗" if status == "失败" else "-")
            md.append(f"| {stage_num} | {stage_name} | `{script}` | {status_icon} |")
            
        md.append("")
        
        # 错误详情
        failed_stages = [(s, n, e) for s, n, e in stage_results if n[1] == "失败"]
        if failed_stages:
            md.append("## 错误详情")
            md.append("")
            for stage_num, stage_name, errors in failed_stages:
                md.append(f"### 阶段{stage_num}: {stage_name}")
                md.append("")
                if errors:
                    for err in errors:
                        md.append(f"```")
                        md.append(f"ERROR: {err}")
                        md.append(f"```")
                else:
                    md.append("无详细错误信息")
                md.append("")
        
        # 建议
        md.append("## 建议和下一步操作")
        md.append("")
        
        if failed == 0:
            md.append("✓ 所有验证阶段通过，模型可以正常运行。")
        else:
            md.append(f"⚠ 有 {failed} 个阶段验证失败，请先解决上述错误后重新验证。")
            md.append("")
            md.append("建议操作:")
            md.append("1. 查看错误详情了解具体问题")
            md.append("2. 检查相关配置和依赖")
            md.append("3. 修复后使用 `--resume-from` 从失败阶段重新验证")
            
        md.append("")
        md.append("---")
        md.append("*报告由 generative-recommendation-verification skill 自动生成*")
        
        return '\n'.join(md)
        
    def generate_report(self):
        """生成完整报告"""
        print("=== 生成验证报告 ===")
        
        stage_results = []
        for stage_num, stage_name, script in self.STAGES:
            log_file = self.find_log_file((stage_num, stage_name, script))
            status, errors = self.parse_log_result(log_file)
            stage_results.append((stage_num, stage_name, errors))
            print(f"  阶段{stage_num}: {stage_name} - {status}")
            
        device_info = self.get_device_info()
        
        # 生成 JSON 报告
        json_report = self.generate_json_report(stage_results)
        json_file = self.output_dir / "report.json"
        with open(json_file, 'w') as f:
            json.dump(json_report, f, indent=2, ensure_ascii=False)
        print(f"✓ JSON报告已保存: {json_file}")
        
        # 生成 Markdown 报告
        md_report = self.generate_markdown_report(stage_results, device_info)
        md_file = self.output_dir / "report.md"
        with open(md_file, 'w') as f:
            f.write(md_report)
        print(f"✓ Markdown报告已保存: {md_file}")
        
        return json_report["summary"]


def main():
    parser = argparse.ArgumentParser(description="生成验证报告")
    parser.add_argument("--output", default="./verification_report", help="报告输出目录")
    parser.add_argument("--all-stages", action="store_true", help="运行所有阶段")
    parser.add_argument("--stage", type=int, help="指定阶段(1-8)")
    parser.add_argument("--resume-from", type=int, help="从指定阶段恢复")
    parser.add_argument("--ascend-path", default="/usr/local/Ascend", help="昇腾路径")
    parser.add_argument("--config", default="configs/ml-1m/hstu-mt-3400.gin", help="配置文件")
    args = parser.parse_args()
    
    generator = ReportGenerator(args.output)
    summary = generator.generate_report()
    
    print("")
    print("=== 报告生成完成 ===")
    print(f"通过: {summary['passed']}/{summary['total']}")
    
    return 0 if summary['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
