# Issue #864: [Guide]: How to quickly run a perf benchmark to determine if performance has improved

## 基本信息

- **编号**: #864
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/864
- **创建时间**: 2025-05-15T01:28:19Z
- **关闭时间**: 2025-06-15T07:50:35Z
- **更新时间**: 2025-06-15T07:50:35Z
- **提交者**: @Potabk
- **评论数**: 0

## 标签

guide

## 问题描述

### Your current environment

None

### How would you like to use vllm on ascend

Assume you are using vllm-acend v0.7.3, and you want to know if the tuning strategy make sense, the following step may as a reference:
- Run with docker
```bash
export DEVICE=/dev/davinci0
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.7.3
docker run --rm \
--name vllm-ascend \
--device $DEVICE \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-it $IMAGE bash
```

- Launch vllm server
```bash
# note set `load-format=dummy`, for a lightweight test, we don't need real download weights
export HF_ENDPOINT="https://hf-mirror.com"
python3  -m vllm.entrypoints.openai.api_server  --model Qwen/Qwen2.5-7B-Instruct --tensor-parallel-size 1 --swap-space 16 --disable-log-stats  --disable-log-requests  --load-format dummy
```
- Install necessary dependencies
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas datasets
```

- Run benchmark for online serving
 need wait for vllm serving  ready
```bash
cd /vllm-workspace/vllm/benchmarks
python benchmark_serving.py --model Qwen/Qwen2.5-7B-Instruct --dataset-name random --random-input-len 200 --num-prompts 200 --request-rate 1 --save-result --result-dir ./
```

