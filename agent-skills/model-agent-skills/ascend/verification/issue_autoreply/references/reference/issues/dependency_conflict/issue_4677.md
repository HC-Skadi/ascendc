# Issue #4677: [Bug]: qwen3-235B A3单机用ray作分布式调度抛异常

## 基本信息

- **编号**: #4677
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4677
- **创建时间**: 2025-12-03T12:24:41Z
- **关闭时间**: 2025-12-15T03:12:56Z
- **更新时间**: 2025-12-15T03:12:56Z
- **提交者**: @bingnanchina
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

服务端：
#export VLLM_LOGGING_LEVEL=DEBUG
export HCCL_IF_IP=141.61.81.44
export HCCL_IF_BASE_PORT=58888
export HCCL_CONNECT_TIMEOUT=3600
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_SOCKET_IFNAME=enp48s3u1u2
export VLOO_SCOKET_IFNAME=enp48s3u1u2
export TP_SOCKET_IFNAME=enp48s3u1u2
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

vllm serve /home/weight/Qwen3-235B-A22B-Instruct-2507/ \
--served-model-name qwen3-235B-instruct \
--distributed-executor-backend ray \
 --tensor-parallel-size 8 \
--pipeline-parallel-size 2 \
--no-enable-expert-parallel \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.75 \
--port 9090 \
--max-model-len 262144 \
--trust-remote-code \
--dtype float16

客户端：
#loop_array[0]="256 256 10"
#loop_array[0]="256 256 20"
#loop_array[0]="256 256 30"
#loop_array[0]="256 256 40"
#loop_array[0]="256 256 50"
loop_array[0]="512 512 10"
#loop_array[0]="512 512 20"
#loop_array[0]="512 512 30"
#loop_array[0]="512 512 40"
#loop_array[0]="512 512 50"
loop_array[1]="4096 2048 10"
#loop_array[1]="4096 2048 20"
#loop_array[2]="4096 2048 30"
#loop_array[3]="4096 2048 40"
#loop_array[4]="4096 2048 50"
loop_array[2]="8192 4096 40"
#loop_array[0]="8192 4096 40"
#loop_array[0]="8192 4096 40"
#loop_array[0]="8192 4096 40"
#loop_array[1]="8192 4096 50"
#loop_array[7]="8192 4096 30"
loop_array[3]="16384 8192 10"
#loop_array[4]="16384 8192 30"
#loop_array[5]="16384 8192 40"
#loop_array[6]="16384 8192 50"
#loop_array[9]="32768 16384 10"
#loop_array[9]="32768 16384 10"
#loop_array[9]="32768 16384 10"
#loop_array[9]="32768 16384 10"
#loop_array[9]="32768 16384 10"
loop_array[4]="2048 4096 10"
#loop_array[11]="2048 4096 20"
#loop_array[12]="2048 4096 30"
#loop_array[13]="2048 4096 40"
#loop_array[14]="2048 4096 50"
loop_array[5]="4096 8192 10"
#loop_array[16]="4096 8192 20"
#loop_array[17]="4096 8192 30"
loop_array[6]="8192 16384 10"
#loop_array[8]="8192 16384 30"
#loop_array[9]="8192 16384 40"
#loop_array[18]="8192 16384 50"
#loop_array[19]="16384 32768 5"
#loop_array[20]="65536 65536 5"
#loop_array[21]="131072 131072 5"


for var in "${loop_array[@]}"; do
    var_str=($var)
    var_str_temp="${var_str[2]}"
    prompts=$(($var_str_temp * 5))
    echo "=================== input: ${var_str[0]}      output ${var_str[1]}    concurrency: ${var_str[2]}      prompts: ${prompts} ==================="

    vllm bench serve \
    --backend vllm \
    --random-output-len="${var_str[1]}" \
    --random-input-len="${var_str[0]}" \
    --ready-check-timeout-sec 18000 \
    --model qwen3-235B-instruct \
    --tokenizer /home/weight/Qwen3-235B-A22B-Instruct-2507/ \
    --max_concurrency "${var_str[2]}" \
    --num_prompts $prompts \
    --host localhost \
    --port 9090 \
    --endpoint /v1/completions \
    --ready-check-timeout-sec 18000 \
    --ignore-eos || true
done




</details>


### 🐛 Describe the bug

[error_from_service.txt](https://github.com/user-attachments/files/23905683/error_from_service.txt)

[error_from_plog.log](https://github.com/user-attachments/files/23905690/error_from_plog.log)
