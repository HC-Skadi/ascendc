# Issue #5942: [Bug]: 在双机800I A2上，使用vllm-ascend v0.13.0rc1拉起 DSv3.2-w8a8模型，DP4 TP4 一直卡住拉不起来（DP2 TP8可以拉起来）

**类型**: Issue

## 问题背景
### Your current environment

服务器：Atlas800IA2 *2 （双机混部16卡）
模型：DSv3.2-w8a8
vllm-ascend：直接使用镜像vllm-ascend v0.13.0rc1（在镜像中安装了triton-ascend==3.2.0.dev2025110717）

### 🐛 Describe the bug

<details>
<summary>The output of `python collect_env.py`</summary>

在双机800I A2上   使用vllm-ascend v0.13.0rc1  拉起 DSv3.2-w8a8模型     配置参数--max-num-seqs 2 \
--max-model-len 40000 \
--max-num-batched-tokens 4096 \    
DP4 TP4 拉不起来  一直卡在下图（DP2 TP8可以拉起来）

<img width="1705" height="732" alt="Image" src="https://github.com/user-attachments/assets/7d75362e-9d43-4024-9f62-a92331a811af" />

和DP2TP8比对，正常接下应该是如下图打印的红框中的日志

<img width="1678" height="761" alt="Image" src="https://github.com/user-attachments/assets/640e5034-cb2e-4565-9249-fa3f58b7e2f5" />

对比DP2 TP8发现DP4TP4的后台进程一直没有下图红框中的进程
<img width="1683" height="894" alt="Image" src="https://github.com/user-attachments/assets/cef0f5e5-2b7d-42b4-9c0c-81d0fb941409" />

实际操作步骤
1、拉取vllm-ascend v0.13.0rc1镜像（并在镜像中安装了triton-ascend==3.2.0.dev2025110717）
2、配置双机NPU卡的网络环境
3、配置node

## 基本信息
- **编号**: #5942
- **作者**: sjm0522
- **创建时间**: 2026-01-16T02:30:52Z
- **关闭时间**: 2026-01-20T02:32:11Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5942)
