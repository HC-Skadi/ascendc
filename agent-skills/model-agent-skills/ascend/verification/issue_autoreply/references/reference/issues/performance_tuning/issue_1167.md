# Issue #1167: [Guide]: Benchmark on v0.9.0rc2

## 基本信息

- **编号**: #1167
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1167
- **创建时间**: 2025-06-11T03:09:17Z
- **关闭时间**: 2025-06-11T14:14:11Z
- **更新时间**: 2025-08-01T09:15:51Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

guide

## 问题描述

Qwen/Qwen2.5-7B-Instruct:
![Image](https://github.com/user-attachments/assets/32f47f5e-47a2-4160-9338-c371de5f83dd)

Qwen/Qwen3-8B
<img width="889" alt="Image" src="https://github.com/user-attachments/assets/1a1337cb-0e88-4cee-9266-aec2507755b2" />

Link: https://docs.google.com/spreadsheets/d/1Z6KIp54n2NUhubMPImQrVtKnV5ZaUyu0FwP9NYtXdrA/

### Test Env
- Model: Qwen/Qwen2.5-7B-Instruct
- Altlas A2 313T 64GB
- vLLM v0.9.0rc2
- Image: m.daocloud.io/quay.io/ascend/vllm-ascend:v0.9.0rc2

```
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci4
# Update the vllm-ascend image
#export IMAGE=m.daocloud.io/quay.io/ascend/cann:8.1.rc1-910b-ubuntu22.04-py3.10
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.9.0rc2
docker run --rm \
--name yikun-test \
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

### Test step
```
# Start vLLM
export MODEL=Qwen/Qwen2.5-7B-Instruct
export VLLM_USE_MODELSCOPE=true
VLLM_USE_V1=1 VLLM_USE_MODELSCOPE=true python3 -m vllm.entrypoints.openai.api_server --model $MODEL \
         --tensor-parallel-size 1 --swap-space 16 --disable-log-stats \
         --disable-log-requests  --load-format dummy
```

```
# Benchmark
export MODEL=Qwen/Qwen2.5-7B-Instruct
export VLLM_USE_MODELSCOPE=true
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
pip install -r /vllm-workspace/vllm-ascend/benchmarks/requirements-bench.txt
python3 /vllm-workspace/vllm/benchmarks/benchmark_serving.py --model $MODEL --dataset-name random \
         --random-input-len 200 --num-prompts 200 --request-rate 1 \
         --save-result --result-dir ./
```

### Test results
```
============ Serving Benchmark Result ============
Successful requests:                     200
Benchmark duration (s):                  187.38
Total input tokens:                      40000
Total generated tokens:                  25600
Request throughput (req/s):              1.07
Output token throughput (tok/s):         136.62
Total Token throughput (tok/s):          350.09
---------------Time to First Token----------------
Mean TTFT (ms):                          49.75
Median TTFT (ms):                        48.97
P99 TTFT (ms):                           68.68
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          22.07
Median TPOT (ms):                        22.51
P99 TPOT (ms):                           25.85
---------------Inter-token Latency----------------
Mean ITL (ms):                           22.07
Median ITL (ms):                         24.31
P99 ITL (ms):                            32.47
==================================================
```
