# vLLM-ascend Issue 分类汇总报告

## 项目背景

vLLM-ascend 是一个社区维护的硬件插件，用于在昇腾Ascend NPU上无缝运行vLLM。该项目支持 Transformer-like、MoE、Embedding、Multi-modal 等模型类型，遵循硬件可插拔原则。

**仓库地址**: https://github.com/vllm-project/vllm-ascend

---

## 分类标准说明

本报告对 vLLM-ascend 项目中所有已关闭的 910 个 Issue 进行了分类整理，按照问题的性质将 Issue 分为以下六个类别：

| 类别 | 说明 | 关键词 |
|------|------|--------|
| installation_setup | 安装部署相关问题 | install, setup, build, compile, pip, docker, dependency, environment |
| model_compatibility | 模型兼容性相关问题 | model, transformer, moe, embedding, multimodal, compatibility |
| performance_tuning | 性能优化相关问题 | performance, speed, throughput, latency, optimization, memory |
| api_usage | API使用相关问题 | api, openai, rest, client, server, request, completion |
| hardware_adapter | 硬件适配相关问题 | npu, ascend, cann, hardware, device, rank, world_size |
| dependency_conflict | 依赖冲突相关问题 | conflict, version, error, bug, crash, fail, exception |

---

## 分类统计

| 类别 | Issue 数量 | 占比 |
|------|-----------|------|
| dependency_conflict | 513 | 56.4% |
| installation_setup | 150 | 16.5% |
| model_compatibility | 126 | 13.8% |
| performance_tuning | 57 | 6.3% |
| api_usage | 48 | 5.3% |
| hardware_adapter | 16 | 1.8% |
| **总计** | **910** | **100%** |

---

## 各类别详情

### 1. dependency_conflict (513 个 Issue)
- Bug 报告: 代码运行时的错误、崩溃、异常
- 版本问题: vLLM 版本与 vLLM-ascend 版本的兼容性问题
- 环境配置: 缺少依赖、依赖冲突等

### 2. installation_setup (150 个 Issue)
- 安装问题: pip install 失败、源码编译问题
- 环境配置: Docker 环境、conda 环境设置
- 依赖问题: 缺少必要的系统依赖或 Python 包

### 3. model_compatibility (126 个 Issue)
- 模型支持: 特定模型是否支持在 Ascend NPU 上运行
- 功能缺失: 某些模型特性在 NPU 后端不可用
- 算子支持: 特定算子在 NPU 上不支持

### 4. performance_tuning (57 个 Issue)
- 性能问题: 推理速度慢、吞吐量低
- 内存问题: VRAM 占用过高、内存溢出
- 批处理问题: batch size 设置问题

### 5. api_usage (48 个 Issue)
- OpenAI API: OpenAI 兼容 API 使用问题
- 接口调用: SDK 使用、API 参数配置
- 服务部署: API Server 部署和配置

### 6. hardware_adapter (16 个 Issue)
- 设备发现: NPU 设备识别问题
- 分布式配置: 多设备并行配置
- 设备映射: CUDA device 与 NPU device 映射

---

*报告生成时间: 2026-03-03*
*数据来源: https://github.com/vllm-project/vllm-ascend*
