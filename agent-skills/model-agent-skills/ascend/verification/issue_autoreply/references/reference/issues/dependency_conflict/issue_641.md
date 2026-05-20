# Issue #641: [Bug]:310p3显卡中部署语言模型报错

## 基本信息

- **编号**: #641
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/641
- **创建时间**: 2025-04-24T05:55:36Z
- **关闭时间**: 2025-04-25T02:51:13Z
- **更新时间**: 2025-04-25T02:51:13Z
- **提交者**: @wonders7796
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<html>
<body>
<!--StartFragment--><div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code" style="margin: 10px 0px; padding: 0px; color: rgb(51, 51, 51); border: 1px solid rgb(223, 225, 229); overflow: auto; border-radius: 3px; background-color: rgb(255, 255, 255); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="codeContent panelContent pdl" style="margin: 0px; padding: 0px; background: rgb(255, 255, 255); color: rgb(51, 51, 51); text-align: left; font-size: 14px; line-height: 20px; overflow: hidden; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px;"><div style="margin: 0px; padding: 0px;"><div id="highlighter_762790" class="syntaxhighlighter sh-confluence nogutter  java" style="margin: 0px; padding: 0px; width: 830.36px; position: relative; overflow: auto; font-size: 1em; background-color: rgb(255, 255, 255) !important;">
docker pull  --platform=arm64  quay.io/ascend/vllm-ascend@sha256:ee3668ece39acead1ee600079c98ff4394769feb2bc625e8cb24b00ad0f734f3
--

##  启动容器
docker run -itd --privileged --name=wingpt-01 \
  --shm-size 1g \
  --device=/dev/davinci0 \
  --device=/dev/davinci1 \
  --device=/dev/davinci_manager \
  --device=/dev/hisi_hdc \
  --device /dev/devmm_svm \
  -v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
  -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
  -v /etc/ascend_install.info:/etc/ascend_install.info \
  -v /usr/local/sbin/npu-smi:/usr/local/sbin/npu-smi \
  -v /usr/local/sbin:/usr/local/sbin \
  -v /data01/winning/wingpt/data:/data \
  -v /data01/vllm/:/vllm \
   -p 2025:8000 \
   7e8e9b031822 \
   bash

#启动服务
export ASCEND_RT_VISIBLE_DEVICES=0,1
export ASCEND_PROCESS_LOG_PATH=/workspace/vllm_log/
 
VLLM_TORCH_PROFILER_DIR=./vllm_profile
LOG_FILE="multinode_$(date +%Y%m%d_%H%M).log"
 
python -m vllm.entrypoints.openai.api_server \
 --model="/data/WiNGPT2-32B-1012-CPO" \
 --trust-remote-code \
 --enforce-eager \
 --max-model-len 8192 \
 --tensor-parallel-size 4 \
 --disable-log-requests \
 --served-model-name WiNGPT \
 --disable-log-stats \
 --disable-frontend-multiprocessing \
 --host 0.0.0.0 \
 --port 8000





</div></div></div></div><br class="Apple-interchange-newline"><!--EndFragment-->
</body>
</html>

### 🐛 Describe the bug

部分报错日志
(VllmWorkerProcess pid=343) ERROR 04-24 03:40:27 multiproc_worker_utils.py:240] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(VllmWorkerProcess pid=343) ERROR 04-24 03:40:27 multiproc_worker_utils.py:240] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(VllmWorkerProcess pid=343) ERROR 04-24 03:40:27 multiproc_worker_utils.py:240] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(VllmWorkerProcess pid=343) ERROR 04-24 03:40:27 multiproc_worker_utils.py:240] [ERROR] 2025-04-24-03:40:27 (PID:343, Device:1, RankID:-1) ERR00100 PTA call acl api failed
[rank0]:[W424 03:40:28.559765110 compiler_depend.ts:432] Warning: EI0003: [PID: 143] 2025-04-24-03:40:28.975.025 In [CheckDataType], value [bfloat16] for parameter [dataType] is invalid. Reason: The collective communication operator has an invalid argument. Reason[bfloat16]
