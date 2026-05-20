# Issue #4110: [Misc]: Performance regression between v0.11.0rc1 and v0.9.1

## 基本信息

- **编号**: #4110
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4110
- **创建时间**: 2025-11-11T01:04:23Z
- **关闭时间**: 2026-03-01T14:22:36Z
- **更新时间**: 2026-03-01T14:22:36Z
- **提交者**: @Yikun
- **评论数**: 5

## 标签

无

## 问题描述

<img width="1004" height="135" alt="Image" src="https://github.com/user-attachments/assets/754be920-7530-410b-9a0f-4ad4f91a7175" />

Reproduce:

```
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci2
# Update the vllm-ascend image
#export IMAGE=swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/vllm-ascend:v0.11.0rc1
export IMAGE=quay.nju.edu.cn/ascend/vllm-ascend:v0.11.0rc1
docker run --rm \
--name yikun-main \
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
-e VLLM_USE_MODELSCOPE=True \
-it $IMAGE bash

~/.cache/perf.sh
```

```bash
# cat ~/.cache/perf.sh
# bash fonts colors
cyan='\e[96m'
yellow='\e[33m'
red='\e[31m'
none='\e[0m'

_cyan() { echo -e "${cyan}$*${none}"; }
_yellow() { echo -e "${yellow}$*${none}"; }
_red() { echo -e "${red}$*${none}"; }

_info() { _cyan "Info: $*"; }
_warn() { _yellow "Warn: $*"; }
_err() { _red "Error: $*" && exit 1; }

CURL_TIMEOUT=1
CURL_COOLDOWN=10
CURL_MAX_TRIES=180

function install_system_packages() {
    if command -v apt-get >/dev/null; then
        sed -i 's|ports.ubuntu.com|mirrors.tuna.tsinghua.edu.cn|g' /etc/apt/sources.list
        apt-get update -y && apt install -y curl
    elif command -v yum >/dev/null; then
        yum update -y && yum install -y curl
    else
        echo "Unknown package manager. Please install gcc, g++, numactl-devel, git, curl, and jq manually."
    fi
}

function wait_url_ready() {
  local serve_name="$1"
  local url="$2"
  i=0
  while true; do
    _info "===> Waiting for ${serve_name} to be ready...${i}s"
    i=$((i + CURL_COOLDOWN))
    set +e
    curl --silent --max-time "$CURL_TIMEOUT" "${url}" >/dev/null
    result=$?
    set -e
    if [ "$result" -eq 0 ]; then
      break
    fi
    if [ "$i" -gt "$CURL_MAX_TRIES" ]; then
      _info "===> ${CURL_MAX_TRIES}s exceeded waiting for ${serve_name} to be ready"
      return 1
    fi
    sleep "$CURL_COOLDOWN"
  done
  _info "===> ${serve_name} is ready."
}

function wait_for_exit() {
  local VLLM_PID="$1"
  while kill -0 "$VLLM_PID"; do
    _info "===> Wait for ${VLLM_PID} to exit."
    sleep 1
  done
  _info "===> Wait for ${VLLM_PID} to exit."
}


function perf_test() {
  install_system_packages
  export MODEL=Qwen/Qwen3-8B
  export VLLM_USE_MODELSCOPE=true
  export VLLM_USE_V1=1

  python3 -m vllm.entrypoints.openai.api_server --model $MODEL \
  --tensor-parallel-size 1 --swap-space 16 --disable-log-stats \
  --disable-log-requests  --load-format dummy > /dev/null &

  wait_url_ready "python3 -m vllm" "localhost:8000/v1/models"

  pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
  pip install -r /vllm-workspace/vllm-ascend/benchmarks/requirements-bench.txt

  # Round 1
  vllm bench serve --model $MODEL \
    --dataset-name random --random-input-len 200 --num-prompts 200 --request-rate 1 \
    --save-result --result-dir ./
  # Round 2
  vllm bench serve --model $MODEL \
    --dataset-name random --random-input-len 200 --num-prompts 200 --request-rate 1 \
    --save-result --result-dir ./
  # Round 2
  vllm bench serve --model $MODEL \
    --dataset-name random --random-input-len 200 --num-prompts 200 --request-rate 1 \
    --save-result --result-dir ./

  VLLM_PID=$(pgrep -f "python3 -m vllm")
  _info "===> Try kill -2 ${VLLM_PID} to exit."
  kill -2 "$VLLM_PID"
  wait_for_exit "$VLLM_PID"
}

_info "====> Start quickstart_online_test"
perf_test
```
