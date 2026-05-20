# vLLM Ascend 常见问题

> 本文档解答关于 vLLM Ascend 的常见问题
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 基础问题

### Q1: vLLM Ascend 是什么?

vLLM Ascend 是 vLLM 项目的华为昇腾 NPU 硬件插件,专门针对华为昇腾系列 AI 处理器进行优化。它允许用户在昇腾 NPU 上高效地部署和运行大语言模型推理。

### Q2: vLLM Ascend 支持哪些版本?

| 组件 | 支持版本 |
|------|---------|
| vLLM | 0.11.0+ |
| vLLM-Ascend | 0.11.0+ |
| CANN | 8.0+ |

### Q3: 支持哪些硬件?

- **华为昇腾 910B**: 全功能支持
- **华为昇腾 310B**: 基础推理支持

## 安装问题

### Q4: pip install vllm-ascend 失败?

**可能原因**:
1. 网络问题导致下载失败
2. Python 版本不兼容
3. 缺少系统依赖

**解决方案**:
```bash
# 检查Python版本
python --version  # 需要 3.8+

# 安装系统依赖
apt-get update
apt-get install -y python3-pip git build-essential

# 重新安装
pip install --upgrade pip
pip install vllm==0.17.0
pip install vllm-ascend==0.17.0
```

### Q5: 导入 vllm 失败?

**可能原因**:
1. vLLM 未正确安装
2. CANN 未安装
3. 环境变量未设置

**解决方案**:
```bash
# 设置CANN环境
source /usr/local/Ascend/ascend-toolkit/set_env.sh

# 验证安装
python -c "import vllm; print(vllm.__version__)"
```

### Q6: NPU 驱动未找到?

**可能原因**:
1. 昇腾驱动未安装
2. 驱动版本不匹配

**解决方案**:
```bash
# 检查驱动
npu-smi info

# 如果未安装,下载安装
# 访问: https://www.hiascend.com/
```

## 使用问题

### Q7: 模型加载失败?

**可能原因**:
1. 模型路径不正确
2. 模型格式不兼容
3. 磁盘空间不足

**解决方案**:
```bash
# 确认模型存在
ls -la /path/to/model

# 使用ModelScope下载
export VLLM_USE_MODELSCOPE=true
vllm serve modelscope.cn/xxx/xxx

# 检查磁盘空间
df -h
```

### Q8: 内存不足 (OOM)?

**可能原因**:
1. 模型太大
2. 批处理太大
3. 序列长度太长

**解决方案**:
```bash
# 减少最大序列长度
--max-model-len 2048

# 降低内存利用率
--gpu-memory-utilization 0.8

# 使用量化模型
--quantization ascend
--model vllm-ascend/Qwen3-8B-w4a8
```

### Q9: 推理速度慢?

**可能原因**:
1. 未启用量化
2. 批处理配置不当
3. 未使用最优参数

**优化建议**:
```bash
# 启用量化
--quantization ascend

# 启用CUDA Graph
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'

# 启用异步调度
--async-scheduling
```

### Q10: 量化模型如何使用?

**步骤**:
1. 量化模型 (参见量化指南)
2. 启动服务时指定量化参数:

```bash
vllm serve /path/to/quantized/model \
    --quantization ascend \
    --trust-remote-code
```

## 部署问题

### Q11: 如何进行多卡部署?

```bash
# 设置多卡
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3

# 启动服务
vllm serve model/name \
    --tensor-parallel-size 4 \
    --max-model-len 4096
```

### Q12: 如何进行多节点部署?

多节点部署需要配置:
1. 网络环境变量
2. KV传输配置
3. 数据并行参数

详细配置请参考 [模型部署文档](./models.md)。

### Q13: 支持哪些量化方法?

- W4A8 (4-bit权重, 8-bit激活)
- W8A8 (8-bit权重, 8-bit激活)
- W4A4 (4-bit权重, 4-bit激活)

### Q14: 如何选择张量并行度?

| 模型大小 | 推荐TP | 说明 |
|---------|-------|------|
| 7B | 1 | 单卡即可 |
| 14B | 2 | 2卡部署 |
| 34B | 4 | 4卡部署 |
| 70B+ | 8 | 8卡部署 |

### Q15: 前缀缓存如何启用?

```bash
vllm serve model/name \
    --enable-prefix-caching
```

## 性能问题

### Q16: 如何提高吞吐量?

1. **启用连续批处理**: 默认启用
2. **使用量化**: --quantization ascend
3. **调整批处理参数**:
```bash
--max-num-batched-tokens 4096
--max-num-seqs 64
```

### Q17: 如何降低延迟?

1. **减少序列长度**: --max-model-len 2048
2. **使用量化模型**: W4A8 更快
3. **启用前缀缓存**: 重复prompt时有效

### Q18: 显存占用太高?

1. **减小 max-model-len**
2. **使用量化模型**
3. **降低 gpu-memory-utilization**
4. **启用 PYTORCH_NPU_ALLOC_CONF**:

```bash
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
```

## 故障排除

### Q19: npu-smi 命令未找到?

```bash
# 安装驱动后,检查路径
which npu-smi

# 或者添加路径
export PATH=$PATH:/usr/local/Ascend/ascend-toolkit/latest/bin
```

### Q20: HCCL 通信错误?

**检查项**:
1. 网络连通性
2. 防火墙配置
3. 环境变量设置

**解决**:
```bash
export HCCL_IF_IP=192.168.1.1
export GLOO_SOCKET_IFNAME=eth0
export TP_SOCKET_IFNAME=eth0
```

### Q21: 模型精度问题?

1. **使用更大group_size**:
```bash
--group_size 256
```

2. **使用W8A8**:
```bash
--quantization ascend
# 使用W8A8量化模型
```

3. **检查模型来源**: 使用官方量化模型

### Q22: 如何清理缓存?

```python
import gc
del llm
gc.collect()
torch.npu.empty_cache()
```

## 最佳实践

### Q23: 生产环境建议配置?

```bash
vllm serve model/name \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 4 \
    --quantization ascend \
    --trust-remote-code \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.9 \
    --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
    --async-scheduling
```

### Q24: 如何监控性能?

```bash
# NPU监控
npu-smi monitor

# 查看vLLM指标
curl http://localhost:8000/metrics
```

### Q25: 如何更新 vLLM?

```bash
# 停止服务
pkill vllm

# 更新
pip install --upgrade vllm
pip install --upgrade vllm-ascend

# 重启服务
vllm serve ...
```

## 相关资源

- [官方文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [GitHub](https://github.com/vllm-project/vllm-ascend)
- [ModelScope](https://modelscope.cn/models)

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
