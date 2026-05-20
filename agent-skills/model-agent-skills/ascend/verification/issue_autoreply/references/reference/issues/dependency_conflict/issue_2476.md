# Issue #2476: [Bug]: Deepseek mtp torchair graph mode

## 基本信息

- **编号**: #2476
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2476
- **创建时间**: 2025-08-21T11:10:27Z
- **关闭时间**: 2025-08-29T08:17:03Z
- **更新时间**: 2025-08-29T08:17:03Z
- **提交者**: @sunchendd
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

分支信息：v0.10.0rc1

### 🐛 Describe the bug

deepseek mtp叠加torchair graph mode性能比只开torchair graph mode还差。还不清楚什么原因导致
temperature  parallel 	不开mtp（tok/s）	开启mtp（tok/s）
0.6                  12             17.13	                  15.83


启动脚本：
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export HCCL_BUFFSIZE=1024
export ASCEND_LAUNCH_BLOCKING=0
export VLLM_USE_MODELSCOPE="True"
export VLLM_WORKER_MULTIPROC_METHOD="spawn"
python -m vllm.entrypoints.openai.api_server \
--model="/data/DeepSeek-R1-W8A8" \
--trust-remote-code \
--max_model_len 15000 \
--max_num_batched_tokens 15000 \
--served-model-name DeepSeek-R1-W8A8 \
--tensor-parallel-size 16 \
--no-enable-prefix-caching \
--gpu_memory_utilization 0.95 \
--port 8000 \
--quantization ascend \
--disable-log-stats \
--disable-log-requests \
--additional_config='{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true,"graph_batch_sizes_init":true}}' \
--speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":1}'

测试脚本：benchmark或evalscope
