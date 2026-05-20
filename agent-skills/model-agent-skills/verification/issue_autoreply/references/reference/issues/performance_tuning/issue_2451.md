# Issue #2451: [Usage]: vllm 0.9.1 + turbo没有生效  vllm0.7.3 + turbo吞吐有性能提升

## 基本信息

- **编号**: #2451
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2451
- **创建时间**: 2025-08-20T02:03:19Z
- **关闭时间**: 2025-08-22T09:24:52Z
- **更新时间**: 2025-08-22T09:24:52Z
- **提交者**: @linjianshu
- **评论数**: 1

## 标签

无

## 问题描述

### Your current environment


官方文档上显示mindie-turbo对cann以及vllm的版本有着严格的要求 参阅https://www.hiascend.com/document/detail/zh/mindie/21RC1/AcceleratePlugin/turbodev/mindie-turbo-0005.html  我机器上出现的问题在于vllm0.9.1搭配mindiet-turbo2.1.rc1没有吞吐提升 但是使用vllm0.7.3 搭配mindie-turbo2.0.rc2有吞吐提升 且vllm拉起服务时会有日志打印“INFO 08-18 12:19:07 utils.py:33] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.”  但这些日志在vllm0.9.1 搭配mindie-turbo2.1.rc1中也没有体现

为更快的帮您定位问题，推荐您用以下模板反馈：

1、出现问题时，您做了哪些操作？

答复：
1.1启动容器
# Update DEVICE according to your device (/dev/davinci[0-7])
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.9.1rc2
docker run -itd \
--name vllm-ascend-0.9.1 \
--privileged=true --ipc=host --network host \
--device=/dev/davinci4 \
--device=/dev/davinci5 \
--device=/dev/davinci6 \
--device=/dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /data/:/data/  \
-p 8000:8000 \
-it $IMAGE bash
# Install curl
apt-get update -y && apt-get install -y curl
1.2安装turbo


# 安装turbo
root@host-ds-2:/workspace# cd /data/ljs/mindie-turbo/
root@host-ds-2:/data/ljs/mindie-turbo# ls
Ascend-mindie-turbo_2.1.RC1_py310_linux_aarch64         Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64
Ascend-mindie-turbo_2.1.RC1_py310_linux_aarch64.tar.gz  Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64.tar.gz
root@host-ds-2:/data/ljs/mindie-turbo# cd Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64
root@host-ds-2:/data/ljs/mindie-turbo/Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64# python --version 
Python 3.11.13
root@host-ds-2:/data/ljs/mindie-turbo/Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64# pip install mindie_turbo-2.1rc1-cp311-cp311-linux_aarch64.whl

root@host-ds-2:/workspace# pip list | grep mindie
mindie_turbo                             2.1rc1


1.3安装测试工具


# 清华源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# evalscope测试工具
pip install 'evalscope[app]'
pip install evalscope
pip install sse_starlette

# 数据集下载
from modelscope import MsDataset
train_dataset = MsDataset.load('AI-ModelScope/LongAlpaca-12k', 
                               subset_name='default', split='train').to_hf_dataset()

print(train_dataset)
"""Out[0]
Dataset({
    features: ['instruction', 'output', 'file', 'input'],
    num_rows: 12000
})
"""

1.4 拉起推理服务


export ASCEND_VISIBLE_DEVICES=4,5,6,7
export ASCEND_RT_VISIBLE_DEVICES=4,5,6,7


VLLM_USE_V1=1  vllm serve /data/ljs/Qwen2.5-32B-Instruct \
--block-size=128 \
--served-model-name qwen2.5-32B-instruct \
--enable-auto-tool-choice \
--tool-call-parser hermes \
--tensor-parallel-size 4 \
--port 8000 \
--cpu-offload-gb=0 \
--enforce-eager \
--gpu-memory-utilization=0.95 \
--max-model-len=32768 \
--max-num-batched-tokens=32768 \
--enable_prefix_caching

1.5执行测试


export model="qwen2.5-32B-instruct"
export base_url="http://127.0.0.1:8000"

evalscope perf --url "${base_url}/v1/chat/completions" --model ${model} --api openai --api-key 123456 --dataset longalpaca --min-prompt-length 4096 --max-prompt-length 20480 -n 200 --temperature 0.0 --read-timeout 120 --parallel 5





2、在哪个步骤出现了问题？

答复：1.6测试结果 安装turbo和不安装turbo没有区别

3、您希望得到什么结果？

答复：mindie-turbo2.1.rc1 搭配vllm0.9.1 应该在吞吐上教vllm0.9.1有性能提升，但是没有窥见。但是mindit-turbo2.0.rc2 搭配vllm0.7.3 较vllm0.7.3有吞吐性能提升。

4、您实际得到什么结果？

答复：mindie-turbo2.1.rc1 搭配vllm0.9.1 应该在吞吐上教vllm0.9.1有性能提升，但是没有窥见。但是mindit-turbo2.0.rc2 搭配vllm0.7.3 较vllm0.7.3有吞吐性能提升。

5、请附上您出现问题页面的整屏截图或者日志信息;

答复：


vllm0.9.1

Quickstart — vllm-ascend

root@043346cf5f35:/usr/local/Ascend# cd ascend-toolkit/
root@043346cf5f35:/usr/local/Ascend/ascend-toolkit# ls
8.2  8.2.RC1  latest  set_env.sh
root@043346cf5f35:/usr/local/Ascend/ascend-toolkit# cd latest/
root@043346cf5f35:/usr/local/Ascend/ascend-toolkit/latest# ll
total 24
drwxr-xr-x  6 root root 4096 Jul 26 07:46 ./
drwxr-xr-x  1 root root   21 Jul 26 07:46 ../
dr-xr-xr-x 14 root root  280 Jul 26 07:44 aarch64-linux/
lrwxrwxrwx  1 root root   18 Jul 26 07:41 acllib -> ../8.2.RC1/runtime/
lrwxrwxrwx  1 root root   13 Jul 26 07:44 arm64-linux -> aarch64-linux/
​
npu-smi 25.2.0                   Version: 25.2.0                                       
​
root@043346cf5f35:/usr/local/Ascend/ascend-toolkit/latest# pip show torch_npu
Name: torch-npu
Version: 2.5.1.post1
Summary: NPU bridge for PyTorch
​
root@043346cf5f35:/usr/local/Ascend/ascend-toolkit/latest# pip show torch 
Name: torch
Version: 2.5.1
​
root@043346cf5f35:/usr/local/Ascend# cd nnal/
root@043346cf5f35:/usr/local/Ascend/nnal# ls
asdsip  atb  nnal_uninstall.sh
root@043346cf5f35:/usr/local/Ascend/nnal# cd atb/
root@043346cf5f35:/usr/local/Ascend/nnal/atb# ls
8.2.RC1  latest  set_env.sh
root@043346cf5f35:/usr/local/Ascend/nnal/atb# ll -lat
total 4
drwxr-xr-x 4 root root   56 Jul 26 07:46 ../
drwxr-xr-x 3 root root   53 Jul 26 07:46 ./
drwxr-xr-x 5 root root   81 Jul 26 07:46 8.2.RC1/
lrwxrwxrwx 1 root root    7 Jul 26 07:46 latest -> 8.2.RC1/
-r-xr-xr-x 1 root root 3959 Jul 26 07:46 set_env.sh*
​
root@host-ds-2:/data/ljs# pip show vllm 
Name: vllm
Version: 0.9.1+empty



启动容器
# Update DEVICE according to your device (/dev/davinci[0-7])
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.9.1rc2
docker run -itd \
--name vllm-ascend-0.9.1 \
--privileged=true --ipc=host --network host \
--device=/dev/davinci4 \
--device=/dev/davinci5 \
--device=/dev/davinci6 \
--device=/dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /data/:/data/  \
-p 8000:8000 \
-it $IMAGE bash
# Install curl
apt-get update -y && apt-get install -y curl



安装测试工具
# 清华源
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
​
# evalscope测试工具
pip install 'evalscope[app]'
pip install evalscope
pip install sse_starlette
​
# 数据集下载
from modelscope import MsDataset
train_dataset = MsDataset.load('AI-ModelScope/LongAlpaca-12k', 
                               subset_name='default', split='train').to_hf_dataset()
​
print(train_dataset)
"""Out[0]
Dataset({
    features: ['instruction', 'output', 'file', 'input'],
    num_rows: 12000
})
"""



qwen2.5-32B

用vllm自己的测试基准脚本来测 测0.9.1 有无turbo的性能差异 测0.8.5有无turbo的性能差异

export ASCEND_VISIBLE_DEVICES=4,5,6,7
export ASCEND_RT_VISIBLE_DEVICES=4,5,6,7
​
VLLM_USE_V1=1  vllm serve                       /data/ljs/Qwen2.5-32B-Instruct \
                                --block-size=128 \
                                --served-model-name qwen2.5-32B-instruct \
                                --enable-auto-tool-choice \
                                --tool-call-parser hermes \
                                --tensor-parallel-size 4 \
                                --port 8000 \
                                --cpu-offload-gb=0 \
                                --enforce-eager \
                                --gpu-memory-utilization=0.95 \
                                --max-model-len=32768 \
                                --max-num-batched-tokens=32768 \
                                --enable_prefix_caching 



执行测试
export model="qwen2.5-32B-instruct"
export base_url="http://127.0.0.1:8000"
​
evalscope perf --url "${base_url}/v1/chat/completions" --model ${model} --api openai --api-key 123456 --dataset longalpaca --min-prompt-length 4096 --max-prompt-length 20480 -n 200 --temperature 0.0 --read-timeout 120 --parallel 5



测试结果
2025-08-18 06:52:23,830 - evalscope - INFO - 
Benchmarking summary:
+-----------------------------------+-----------+
| Key                               |     Value |
+===================================+===========+
| Time taken for tests (s)          | 1026.99   |
+-----------------------------------+-----------+
| Number of concurrency             |    5      |
+-----------------------------------+-----------+
| Total requests                    |  200      |
+-----------------------------------+-----------+
| Succeed requests                  |  200      |
+-----------------------------------+-----------+
| Failed requests                   |    0      |
+-----------------------------------+-----------+
| Output token throughput (tok/s)   |   51.7432 |
+-----------------------------------+-----------+
| Total token throughput (tok/s)    |  756.736  |
+-----------------------------------+-----------+
| Request throughput (req/s)        |    0.1947 |
+-----------------------------------+-----------+
| Average latency (s)               |   25.3931 |
+-----------------------------------+-----------+
| Average time to first token (s)   |    0.4416 |
+-----------------------------------+-----------+
| Average time per output token (s) |    0.0943 |
+-----------------------------------+-----------+
| Average inter-token latency (s)   |    0.0944 |
+-----------------------------------+-----------+
| Average input tokens per request  | 3620.11   |
+-----------------------------------+-----------+
| Average output tokens per request |  265.7    |
+-----------------------------------+-----------+
2025-08-18 06:52:23,872 - evalscope - INFO - 
Percentile results:
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
| Percentiles | TTFT (s) | ITL (s) | TPOT (s) | Latency (s) | Input tokens | Output tokens | Output (tok/s) | Total (tok/s) |
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
|     10%     |  0.1855  | 0.0557  |  0.0922  |   14.3302   |     1768     |      148      |    10.1984     |    75.3825    |
|     25%     |  0.2031  | 0.0794  |  0.0931  |   15.3221   |     2746     |      161      |    10.3351     |   103.2946    |
|     50%     |  0.3493  | 0.0919  |  0.0944  |   19.2704   |     3742     |      204      |    10.4706     |   164.6076    |
|     66%     |  0.5254  | 0.0987  |  0.0948  |   29.6015   |     4127     |      300      |    10.5737     |   223.5434    |
|     75%     |  0.5904  |  0.104  |  0.0954  |   36.3877   |     4642     |      381      |    10.6147     |   256.9806    |
|     80%     |  0.6311  | 0.1082  |  0.0957  |   38.0257   |     4814     |      400      |    10.6503     |   274.0833    |
|     90%     |  0.7466  | 0.1282  |  0.0966  |   43.8944   |     5061     |      462      |    10.7263     |   313.0648    |
|     95%     |  0.839   |  0.152  |  0.0974  |   48.6551   |     5425     |      515      |    10.7596     |   345.5734    |
|     98%     |  2.0507  | 0.1884  |  0.0983  |   54.6329   |     6029     |      583      |    10.7925     |   451.8238    |
|     99%     |  2.0517  |  0.236  |  0.0988  |   66.5145   |     6516     |      697      |     10.892     |    509.784    |
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
2025-08-18 06:52:23,872 - evalscope - INFO - Save the summary to: outputs/20250818_063357/qwen2.5-32B-instruct
root@host-ds-2:/data/ljs/longAlpaca-12k# 



vllm0.9.1 + mindie turbo(舍弃 无法生效)

安装MindIE Turbo（物理机）-MindIE2.1.RC1-昇腾社区

启动容器
[root@host-ds-2 ~]# export IMAGE=quay.io/ascend/vllm-ascend:v0.9.1rc2
[root@host-ds-2 ~]# docker run -itd --name vllm-ascend-0.9.1-with-turbo --privileged=true --ipc=host --network host --device=/dev/davinci4 --device=/dev/davinci5 --device=/dev/davinci6 --device=/dev/davinci7 --device /dev/davinci_manager --device /dev/devmm_svm --device /dev/hisi_hdc -v /usr/local/dcmi:/usr/local/dcmi -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info -v /etc/ascend_install.info:/etc/ascend_install.info -v /root/.cache:/root/.cache -v /data/:/data/  -p 8000:8000 -it $IMAGE bash



安装turbo

# 安装turbo
root@host-ds-2:/workspace# cd /data/ljs/mindie-turbo/
root@host-ds-2:/data/ljs/mindie-turbo# ls
Ascend-mindie-turbo_2.1.RC1_py310_linux_aarch64         Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64
Ascend-mindie-turbo_2.1.RC1_py310_linux_aarch64.tar.gz  Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64.tar.gz
root@host-ds-2:/data/ljs/mindie-turbo# cd Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64
root@host-ds-2:/data/ljs/mindie-turbo/Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64# python --version 
Python 3.11.13
root@host-ds-2:/data/ljs/mindie-turbo/Ascend-mindie-turbo_2.1.RC1_py311_linux_aarch64# pip install mindie_turbo-2.1rc1-cp311-cp311-linux_aarch64.whl
​
root@host-ds-2:/workspace# pip list | grep mindie
mindie_turbo                             2.1rc1



qwen2.5-32B
export ASCEND_VISIBLE_DEVICES=4,5,6,7
export ASCEND_RT_VISIBLE_DEVICES=4,5,6,7
​
VLLM_USE_V1=1  vllm serve                       /data/ljs/Qwen2.5-32B-Instruct \
                                --block-size=128 \
                                --served-model-name qwen2.5-32B-instruct \
                                --enable-auto-tool-choice \
                                --tool-call-parser hermes \
                                --tensor-parallel-size 4 \
                                --port 8000 \
                                --cpu-offload-gb=0 \
                                --enforce-eager \
                                --gpu-memory-utilization=0.95 \
                                --max-model-len=32768 \
                                --max-num-batched-tokens=32768 \
                                --enable_prefix_caching 



执行测试
export model="qwen2.5-32B-instruct"
export base_url="http://127.0.0.1:8000"
​
evalscope perf --url "${base_url}/v1/chat/completions" --model ${model} --api openai --api-key 123456 --dataset longalpaca --min-prompt-length 4096 --max-prompt-length 20480 -n 200 --temperature 0.0 --read-timeout 120 --parallel 5



测试结果
2025-08-18 08:05:42,735 - evalscope - INFO - 
Benchmarking summary:
+-----------------------------------+-----------+
| Key                               |     Value |
+===================================+===========+
| Time taken for tests (s)          | 1052.21   |
+-----------------------------------+-----------+
| Number of concurrency             |    5      |
+-----------------------------------+-----------+
| Total requests                    |  200      |
+-----------------------------------+-----------+
| Succeed requests                  |  200      |
+-----------------------------------+-----------+
| Failed requests                   |    0      |
+-----------------------------------+-----------+
| Output token throughput (tok/s)   |   50.9187 |
+-----------------------------------+-----------+
| Total token throughput (tok/s)    |  739.018  |
+-----------------------------------+-----------+
| Request throughput (req/s)        |    0.1901 |
+-----------------------------------+-----------+
| Average latency (s)               |   25.9346 |
+-----------------------------------+-----------+
| Average time to first token (s)   |    0.4415 |
+-----------------------------------+-----------+
| Average time per output token (s) |    0.0955 |
+-----------------------------------+-----------+
| Average inter-token latency (s)   |    0.0955 |
+-----------------------------------+-----------+
| Average input tokens per request  | 3620.11   |
+-----------------------------------+-----------+
| Average output tokens per request |  267.885  |
+-----------------------------------+-----------+
2025-08-18 08:05:42,781 - evalscope - INFO - 
Percentile results:
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
| Percentiles | TTFT (s) | ITL (s) | TPOT (s) | Latency (s) | Input tokens | Output tokens | Output (tok/s) | Total (tok/s) |
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
|     10%     |  0.1821  |  0.052  |  0.0929  |   14.3025   |     1768     |      147      |     9.9813     |    74.6982    |
|     25%     |  0.2018  | 0.0792  |  0.0941  |   15.5977   |     2746     |      161      |    10.2142     |   101.1301    |
|     50%     |  0.3464  | 0.0921  |  0.0954  |   19.7713   |     3742     |      205      |    10.3493     |   161.1626    |
|     66%     |  0.5374  | 0.1001  |  0.0962  |   30.3129   |     4127     |      315      |    10.4315     |   224.6408    |
|     75%     |  0.5988  | 0.1077  |  0.0966  |   36.2264   |     4642     |      378      |     10.472     |    254.485    |
|     80%     |  0.6615  |  0.112  |  0.0971  |   39.2267   |     4814     |      411      |    10.5001     |   271.0018    |
|     90%     |  0.7583  | 0.1323  |  0.0988  |   45.9381   |     5061     |      473      |    10.6159     |   305.9915    |
|     95%     |  0.8337  | 0.1578  |   0.1    |   49.5679   |     5425     |      507      |    10.6865     |    343.694    |
|     98%     |  2.0287  | 0.1959  |  0.1008  |   53.8904   |     6029     |      545      |    10.8297     |   411.4835    |
|     99%     |  2.0298  | 0.2401  |  0.1025  |   63.3459   |     6516     |      664      |    10.9474     |   541.1831    |
+-------------+----------+---------+----------+-------------+--------------+---------------+----------------+---------------+
2025-08-18 08:05:42,781 - evalscope - INFO - Save the summary to: outputs/20250818_074649/qwen2.5-32B-instruct
root@host-ds-2:/workspace# 



结论

对比vllm 0.9.1 without torbo吞吐提升很少 是不是模型不支持的原因？

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

