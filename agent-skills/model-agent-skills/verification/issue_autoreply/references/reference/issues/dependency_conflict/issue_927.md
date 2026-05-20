# Issue #927: [Bug]: vllm-ascend/benchmarks/vllm_benchmarks/benchmark_serving.py': [Errno 2] No such file or directory

## 基本信息

- **编号**: #927
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/927
- **创建时间**: 2025-05-22T06:50:20Z
- **关闭时间**: 2026-01-04T03:39:11Z
- **更新时间**: 2026-01-04T03:39:11Z
- **提交者**: @Schweizliu
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment


<summary>800I A2 8卡，启动qwen2.5-vl-72b的vllm服务后进行客户端吞吐测试</summary>

```
pip install -r benchmarks/requirements-bench.txt
```



### 🐛 Describe the bug

出现问题的代码
```
bash benchmarks/scripts/run-performance-benchmarks.sh
```

```
Running test case serving_qwen2_5_7B_tp1 with qps inf
Client command: python3 vllm_benchmarks/benchmark_serving.py         --save-result         --result-dir results         --result-filename serving_qwen2_5_7B_tp1_qps_inf.json         --request-rate inf         --model Qwen/Qwen2.5-7B-Instruct --backend vllm --dataset-name sharegpt --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json --num-prompts 200
python3: can't open file '/home/xhs/tools/vllm-ascend/benchmarks/vllm_benchmarks/benchmark_serving.py': [Errno 2] No such file or directory
```
仓库里没有benchmark_serving.py

