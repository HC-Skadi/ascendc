# Issue #5680: [Bug]: Ubuntu A2 DeepSeek-V3.2 SingleNode Start Error in docker container

**类型**: Issue

## 问题背景
### Your current environment

According to the [document](https://docs.vllm.ai/projects/ascend/en/latest/installation.html#set-up-using-docker), the operation is carried out by using the docker method. The command is executed in the following way: in the Docker container that is started in this manner, the model startup code also runs within the container.
```bash
docker run --rm \
    --name vllm-ascend \
    --shm-size=1g \
    --net=host \
    --device /dev/davinci0 \
    --device /dev/davinci1 \
    --device /dev/davinci2 \
    --device /dev/davinci3 \
    --device /dev/davinci4 \
    --device /dev/davinci5 \
    --device /dev/davinci6 \
    --device /dev/davinci7 \
    --device /dev/davinci8 \
    --device /dev/davinci9 \
    --device /dev/davinci10 \
    --device /dev/davinci11 \
    --device /dev/davinci12 \
    --device /dev/davinci13 \
    --device /dev/davinci14 \
    --device /dev/davinci15 \
    --device /dev/davinci_manager \
    --device /dev/devmm_svm \
    --device /dev

## 基本信息
- **编号**: #5680
- **作者**: moluzhui
- **创建时间**: 2026-01-07T03:42:57Z
- **关闭时间**: 2026-01-07T03:44:29Z
- **标签**: bug

## 涉及版本
- vLLM: 0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5680)
