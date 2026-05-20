# Issue #6526: [Bug]: vllm-ascend v0.14.0rc1-310p 部署Qwen3-coder-30B报错

**类型**: Issue

## 问题背景
### Your current environment

我使用的镜像是vllm-ascend v0.14.0rc1-310p的arm64版本，启动docker的指令是：
docker run -it -d --net=host --shm-size=200g --name vllm-qwen-coder -w /home \
            --device /dev/davinci4\
           --device /dev/davinci5\
           --device /dev/davinci6\
           --device /dev/davinci7\
           --device /dev/davinci_manager\
           --device /dev/hisi_hdc\
           --device /dev/devmm_svm\
           -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro\
           -v /usr/local/dcmi:/usr/local/dcmi:ro\
           -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi:ro\
           -v /usr/local/sbin/:/usr/local/sbin:ro\
           -v /datadir/Qwen3-Coder-30B-A3B-Instruct:/root/work/Qwen3-Coder-30B-A3B-Instruct:rw \
           a14bc3fdeb2d bash
执行vllm serve报错信息如下，前面的都是正常执行，但出现了一个WARNING 02-03 07:19:44 [camem.py:66] Failed to import vllm_ascend_C:/vllm-workspace/vllm-ascend/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so: undefined symbol: _ZN9pp_matmu

## 基本信息
- **编号**: #6526
- **作者**: lin807095501
- **创建时间**: 2026-02-04T03:31:14Z
- **关闭时间**: 2026-02-04T03:33:57Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6526)
