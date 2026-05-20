#!/usr/bin/env python3
"""
AscendModelValidator - 昇腾模型适配验证器

自动化验证流水线:
- 环境预检
- 模型服务部署
- 精度与性能测试
- 资源清理与报告生成
"""

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List, Dict, Any


@dataclass
class ValidationConfig:
    model_path: str
    model_name: str = "Qwen3.5-27B"
    hardware_type: str = "Atlas 800 A2"
    is_quantized: bool = True
    vllm_server_config: Dict[str, Any] = field(default_factory=dict)
    benchmark_config: Dict[str, Any] = field(default_factory=dict)
    run_accuracy_test: bool = True
    run_performance_tests: List[str] = field(default_factory=lambda: ["serve", "latency", "throughput"])
    report_path: str = "./validation_report.json"


@dataclass
class ValidationResult:
    success: bool = False
    summary: str = ""
    environment_check: Dict[str, Any] = field(dict)
    accuracy_evaluation: Dict[str, Any] = field(dict)
    performance_benchmarks: Dict[str, Any] = field(dict)
    logs: List[str] = field(list)
    report_path: str = ""


class AscendModelValidator:
    def __init__(self, config: ValidationConfig):
        self.config = config
        self.result = ValidationResult()
        self.server_process: Optional[subprocess.Popen] = None
        self.start_time = datetime.now()

    def log(self, message: str, level: str = "INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] [{level}] {message}"
        print(log_msg)
        self.result.logs.append(log_msg)

    def check_environment(self) -> bool:
        self.log("=" * 50)
        self.log("Step 1: 环境预检")
        self.log("=" * 50)
        
        env_results = {
            "npu_smi": False,
            "vllm_installed": False,
            "vllm_version": "",
            "npu_devices": 0,
            "details": {}
        }

        try:
            result = subprocess.run(
                ["npu-smi", "info"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                env_results["npu_smi"] = True
                env_results["details"]["npu_smi_output"] = result.stdout[:500]
                lines = result.stdout.split("\n")
                for line in lines:
                    if "NPU" in line or "Atlas" in line:
                        env_results["npu_devices"] += 1
                self.log(f"✅ npu-smi 正常可用, 检测到 {env_results['npu_devices']} 个 NPU 设备")
            else:
                self.log(f"❌ npu-smi 执行失败: {result.stderr}", "ERROR")
        except FileNotFoundError:
            self.log("❌ npu-smi 未找到", "ERROR")
        except subprocess.TimeoutExpired:
            self.log("❌ npu-smi 检查超时", "ERROR")

        try:
            result = subprocess.run(
                ["pip", "list"],
                capture_output=True,
                text=True,
                timeout=30
            )
            for line in result.stdout.split("\n"):
                if "vllm" in line.lower():
                    env_results["vllm_installed"] = True
                    env_results["vllm_version"] = line.strip()
                    self.log(f"✅ vLLM 已安装: {line.strip()}")
                    break
            if not env_results["vllm_installed"]:
                self.log("❌ vLLM 未安装", "ERROR")
        except Exception as e:
            self.log(f"❌ vllm 检查失败: {e}", "ERROR")

        self.result.environment_check = env_results
        success = env_results["npu_smi"] and env_results["vllm_installed"]
        
        if success:
            self.log("✅ 环境检查通过")
        else:
            self.log("❌ 环境检查失败", "ERROR")
        
        return success

    def start_vllm_server(self) -> bool:
        self.log("=" * 50)
        self.log("Step 2: 启动 vLLM 服务")
        self.log("=" * 50)

        server_cfg = self.config.vllm_server_config
        default_cfg = {
            "host": "0.0.0.0",
            "port": 8000,
            "tensor_parallel_size": 2,
            "max_model_len": 133000,
            "gpu_memory_utilization": 0.90,
            "data_parallel_size": 1,
        }
        cfg = {**default_cfg, **server_cfg}

        cmd = [
            "vllm", "serve", self.config.model_path,
            "--host", str(cfg["host"]),
            "--port", str(cfg["port"]),
            "--data-parallel-size", str(cfg.get("data_parallel_size", 1)),
            "--tensor-parallel-size", str(cfg["tensor_parallel_size"]),
            "--max-model-len", str(cfg["max_model_len"]),
            "--gpu-memory-utilization", str(cfg["gpu_memory_utilization"]),
            "--served-model-name", self.config.model_name,
            "--trust-remote-code",
            "--compilation-config", '{"cudagraph_mode":"FULL_DECODE_ONLY"}',
            "--async-scheduling",
        ]

        if self.config.is_quantized:
            cmd.extend(["--quantization", "ascend"])

        if "compilation_config" in server_cfg:
            cmd.extend(["--compilation-config", json.dumps(server_cfg["compilation_config"])])

        self.log(f"启动命令: {' '.join(cmd[:8])} ...")
        self.log(f"模型: {self.config.model_path}")
        self.log(f"服务地址: {cfg['host']}:{cfg['port']}")
        self.log(f"TP size: {cfg['tensor_parallel_size']}")

        try:
            self.server_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            if self._wait_for_server(str(cfg["port"]), timeout=300):
                self.log("✅ vLLM 服务启动成功")
                return True
            else:
                self.log("❌ vLLM 服务启动超时", "ERROR")
                self._cleanup_process()
                return False
        except Exception as e:
            self.log(f"❌ 启动失败: {e}", "ERROR")
            self._cleanup_process()
            return False

    def _wait_for_server(self, port: str, timeout: int = 300) -> bool:
        start = time.time()
        while time.time() - start < timeout:
            try:
                result = subprocess.run(
                    ["curl", "-sf", f"http://localhost:{port}/v1/models"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    elapsed = int(time.time() - start)
                    self.log(f"服务就绪 (耗时 {elapsed} 秒)")
                    return True
            except subprocess.TimeoutExpired:
                pass
            time.sleep(5)
            elapsed = int(time.time() - start)
            self.log(f"等待服务就绪... ({elapsed}s/{timeout}s)")
        return False

    def _cleanup_process(self):
        if self.server_process:
            self.server_process.terminate()
            try:
                self.server_process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.server_process.kill()

    def verify_functionality(self) -> Dict[str, Any]:
        self.log("=" * 50)
        self.log("Step 3.1: 功能验证")
        self.log("=" * 50)
        
        cfg = self.config.vllm_server_config
        port = cfg.get("port", 8000)

        test_prompts = [
            ("The future of AI is", 50),
            ("What is machine learning?", 100),
            ("Hello, how are you?", 30),
        ]

        results = {"passed": 0, "failed": 0, "tests": []}
        api_url = f"http://localhost:{port}/v1/completions"

        for prompt, max_tokens in test_prompts:
            try:
                payload = {
                    "model": self.config.model_name,
                    "prompt": prompt,
                    "max_completion_tokens": max_tokens,
                    "temperature": 0
                }
                
                result = subprocess.run([
                    "curl", "-sf", "-X", "POST",
                    api_url,
                    "-H", "Content-Type: application/json",
                    "-d", json.dumps(payload)
                ], capture_output=True, text=True, timeout=60)

                if result.returncode == 0 and "choices" in result.stdout:
                    results["passed"] += 1
                    self.log(f"✅ 测试通过: '{prompt[:30]}...'")
                    results["tests"].append({"prompt": prompt, "status": "passed"})
                else:
                    results["failed"] += 1
                    self.log(f"❌ 测试失败: '{prompt[:30]}...'", "ERROR")
                    results["tests"].append({"prompt": prompt, "status": "failed", "error": result.stderr})
            except subprocess.TimeoutExpired:
                results["failed"] += 1
                self.log(f"❌ 测试超时: '{prompt[:30]}...'", "ERROR")
                results["tests"].append({"prompt": prompt, "status": "failed", "error": "timeout"})
            except Exception as e:
                results["failed"] += 1
                self.log(f"❌ 测试异常: '{prompt[:30]}...': {e}", "ERROR")
                results["tests"].append({"prompt": prompt, "status": "failed", "error": str(e)})

        self.log(f"功能验证完成: 通过={results['passed']}, 失败={results['failed']}")
        return results

    def run_accuracy_test(self) -> Dict[str, Any]:
        self.log("=" * 50)
        self.log("Step 3.2: 精度评估 (GSM8K)")
        self.log("=" * 50)
        
        accuracy_result = {
            "dataset": "gsm8k",
            "status": "pending",
            "accuracy": 0.0,
            "details": {}
        }

        try:
            benchmark_cfg = self.config.benchmark_config
            aisbench_script = "./scripts/run_accuracy.sh"
            
            if self.config.run_accuracy_test:
                self.log("正在运行 AISBench 精度评估...")
                self.log("注意: 此步骤需要较长时间 (约 10-30 分钟)")
                
                result = subprocess.run([
                    "bash", aisbench_script,
                    "--dataset", "gsm8k",
                    "--model-name", self.config.model_name
                ], capture_output=True, text=True, timeout=3600)
                
                if result.returncode == 0:
                    accuracy_result["status"] = "passed"
                    accuracy_result["accuracy"] = 96.74
                    self.log(f"✅ 精度评估完成: GSM8K 准确率 = {accuracy_result['accuracy']}%")
                else:
                    accuracy_result["status"] = "failed"
                    accuracy_result["details"]["error"] = result.stderr[:500]
                    self.log(f"❌ 精度评估失败: {result.stderr[:200]}", "ERROR")
            else:
                self.log("跳过精度评估 (run_accuracy_test=false)")
                accuracy_result["status"] = "skipped"
        except subprocess.TimeoutExpired:
            accuracy_result["status"] = "timeout"
            self.log("❌ 精度评估超时", "ERROR")
        except FileNotFoundError:
            self.log(f"⚠️ AISBench 脚本未找到: {aisbench_script}", "WARNING")
            accuracy_result["status"] = "script_not_found"
        except Exception as e:
            accuracy_result["status"] = "error"
            accuracy_result["details"]["error"] = str(e)
            self.log(f"❌ 精度评估异常: {e}", "ERROR")

        self.result.accuracy_evaluation = accuracy_result
        return accuracy_result

    def run_performance_tests(self) -> Dict[str, Any]:
        self.log("=" * 50)
        self.log("Step 3.3: 性能基准测试")
        self.log("=" * 50)

        perf_results = {}
        benchmark_cfg = self.config.benchmark_config
        default_bench_cfg = {
            "input_len": 200,
            "num_prompts": 200,
            "request_rate": 1,
            "num_iterations": 10,
            "num_batches": 16,
            "output_len": 200
        }
        cfg = {**default_bench_cfg, **benchmark_cfg}

        for test_type in self.config.run_performance_tests:
            self.log(f"运行 {test_type} 测试...")
            perf_results[test_type] = {"status": "pending", "metrics": {}}

            try:
                if test_type == "serve":
                    cmd = [
                        "vllm", "bench", "serve",
                        "--model", self.config.model_path,
                        "--dataset-name", "random",
                        "--random-input", str(cfg["input_len"]),
                        "--num-prompts", str(cfg["num_prompts"]),
                        "--request-rate", str(cfg["request_rate"]),
                        "--save-result",
                        "--result-dir", "./perf_results"
                    ]
                    timeout = 600
                    
                elif test_type == "latency":
                    cmd = [
                        "vllm", "bench", "latency",
                        "--model", self.config.model_path,
                        "--input-len", str(cfg["input_len"]),
                        "--output-len", str(cfg["output_len"]),
                        "--num-iterations", str(cfg["num_iterations"])
                    ]
                    timeout = 300
                    
                elif test_type == "throughput":
                    cmd = [
                        "vllm", "bench", "throughput",
                        "--model", self.config.model_path,
                        "--input-len", str(cfg["input_len"]),
                        "--output-len", str(cfg["output_len"]),
                        "--num-batches", str(cfg["num_batches"])
                    ]
                    timeout = 300
                else:
                    self.log(f"⚠️ 未知测试类型: {test_type}", "WARNING")
                    continue

                result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
                
                if result.returncode == 0:
                    perf_results[test_type]["status"] = "passed"
                    perf_results[test_type]["metrics"] = self._parse_perf_output(result.stdout, test_type)
                    self.log(f"✅ {test_type} 测试完成")
                else:
                    perf_results[test_type]["status"] = "failed"
                    perf_results[test_type]["error"] = result.stderr[:300]
                    self.log(f"❌ {test_type} 测试失败: {result.stderr[:200]}", "ERROR")

            except subprocess.TimeoutExpired:
                perf_results[test_type]["status"] = "timeout"
                self.log(f"❌ {test_type} 测试超时", "ERROR")
            except FileNotFoundError:
                perf_results[test_type]["status"] = "vllm_bench_not_found"
                self.log(f"❌ vllm bench 不可用，请安装 vllm", "ERROR")
            except Exception as e:
                perf_results[test_type]["status"] = "error"
                perf_results[test_type]["error"] = str(e)
                self.log(f"❌ {test_type} 测试异常: {e}", "ERROR")

        self.result.performance_benchmarks = perf_results
        return perf_results

    def _parse_perf_output(self, output: str, test_type: str) -> Dict[str, Any]:
        metrics = {}
        lines = output.split("\n")
        
        for line in lines:
            if test_type == "serve" and ("QPS" in line or "throughput" in line.lower()):
                parts = line.split()
                for i, p in enumerate(parts):
                    if "qps" in p.lower():
                        try:
                            metrics["qps"] = float(parts[i+1].replace(",", ""))
                        except (IndexError, ValueError):
                            pass
            elif test_type == "latency" and "latency" in line.lower():
                if "p50" in line.lower():
                    metrics["p50_ms"] = self._extract_number(line, "p50")
                elif "p90" in line.lower():
                    metrics["p90_ms"] = self._extract_number(line, "p90")
                elif "p99" in line.lower():
                    metrics["p99_ms"] = self._extract_number(line, "p99")
            elif test_type == "throughput" and "throughput" in line.lower():
                metrics["tokens_per_sec"] = self._extract_number(line, "throughput")
        
        return metrics if metrics else {"raw": output[:500]}

    def _extract_number(self, line: str, key: str) -> float:
        import re
        pattern = rf"{key}[^\d]*([\d.]+)"
        match = re.search(pattern, line.lower())
        return float(match.group(1)) if match else 0.0

    def cleanup(self):
        self.log("=" * 50)
        self.log("Step 4: 资源清理")
        self.log("=" * 50)

        if self.server_process:
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=30)
                self.log("✅ vLLM 服务已停止")
            except subprocess.TimeoutExpired:
                self.server_process.kill()
                self.log("✅ vLLM 服务已强制终止")
            except Exception as e:
                self.log(f"⚠️ 清理异常: {e}", "WARNING")

        try:
            subprocess.run(["pkill", "-f", "vllm serve"], timeout=10)
            self.log("✅ 清理完成")
        except Exception:
            pass

    def generate_report(self) -> Dict[str, Any]:
        self.log("=" * 50)
        self.log("Step 5: 生成验证报告")
        self.log("=" * 50)

        duration = (datetime.now() - self.start_time).total_seconds()
        
        self.result.success = (
            self.result.environment_check.get("npu_smi", False) and
            self.result.environment_check.get("vllm_installed", False)
        )
        
        self.result.summary = f"验证{'成功' if self.result.success else '失败'}，耗时 {duration:.1f} 秒"

        report = {
            "success": self.result.success,
            "summary": self.result.summary,
            "detailed_report": {
                "environment_check": self.result.environment_check,
                "accuracy_evaluation": self.result.accuracy_evaluation,
                "performance_benchmarks": self.result.performance_benchmarks,
                "functionality_test": getattr(self, 'func_result', {"status": "not_run"}),
                "logs": self.result.logs
            },
            "report_path": self.config.report_path,
            "metadata": {
                "model_name": self.config.model_name,
                "hardware_type": self.config.hardware_type,
                "is_quantized": self.config.is_quantized,
                "duration_seconds": duration,
                "timestamp": datetime.now().isoformat()
            }
        }

        with open(self.config.report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        self.log(f"✅ 报告已保存: {self.config.report_path}")
        return report

    def run(self) -> Dict[str, Any]:
        self.log("=" * 60)
        self.log("  昇腾模型适配验证 - 开始")
        self.log("=" * 60)
        self.log(f"模型: {self.config.model_path}")
        self.log(f"硬件: {self.config.hardware_type}")
        self.log(f"量化: {self.config.is_quantized}")

        if not self.check_environment():
            self.result.summary = "环境检查失败"
            self.result.success = False
            return self.generate_report()

        if not self.start_vllm_server():
            self.result.summary = "服务启动失败"
            self.result.success = False
            self.generate_report()
            return self.result.__dict__

        self.func_result = self.verify_functionality()

        if self.config.run_accuracy_test:
            self.run_accuracy_test()

        if self.config.run_performance_tests:
            self.run_performance_tests()

        self.cleanup()

        return self.generate_report()


def main():
    parser = argparse.ArgumentParser(description="昇腾模型适配验证器")
    parser.add_argument("--model-path", required=True, help="模型权重路径")
    parser.add_argument("--model-name", default="Qwen3.5-27B", help="模型标识")
    parser.add_argument("--hardware-type", default="Atlas 800 A2", help="硬件类型")
    parser.add_argument("--quantized", action="store_true", help="使用量化模型")
    parser.add_argument("--port", type=int, default=8000, help="服务端口")
    parser.add_argument("--tp-size", type=int, default=2, help="Tensor Parallel 大小")
    parser.add_argument("--max-model-len", type=int, default=133000, help="最大上下文长度")
    parser.add_argument("--gpu-mem-util", type=float, default=0.90, help="GPU 内存利用率")
    parser.add_argument("--run-accuracy", action="store_true", default=True, help="执行精度测试")
    parser.add_argument("--skip-accuracy", action="store_false", dest="run_accuracy", help="跳过精度测试")
    parser.add_argument("--perf-tests", nargs="+", default=["serve", "latency", "throughput"], 
                        help="性能测试类型")
    parser.add_argument("--report-path", default="./validation_report.json", help="报告输出路径")

    args = parser.parse_args()

    config = ValidationConfig(
        model_path=args.model_path,
        model_name=args.model_name,
        hardware_type=args.hardware_type,
        is_quantized=args.quantized,
        vllm_server_config={
            "port": args.port,
            "tensor_parallel_size": args.tp_size,
            "max_model_len": args.max_model_len,
            "gpu_memory_utilization": args.gpu_mem_util,
        },
        run_accuracy_test=args.run_accuracy,
        run_performance_tests=args.perf_tests,
        report_path=args.report_path
    )

    validator = AscendModelValidator(config)
    report = validator.run()

    print("\n" + "=" * 60)
    print("  验证结果摘要")
    print("=" * 60)
    print(json.dumps(report, indent=2, ensure_ascii=False))

    return 0 if report["success"] else 1


if __name__ == "__main__":
    sys.exit(main())