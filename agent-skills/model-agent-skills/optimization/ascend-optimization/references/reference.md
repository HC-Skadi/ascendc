# 通用昇腾优化参考

## 诊断优先级

先确认瓶颈再选手段，不要把环境变量当成默认答案。

| 现象 | 优先方向 | 典型动作 |
|------|----------|----------|
| NPU 忙、热点集中在少数算子 | 代码层 | `torch_npu` 亲和算子替换、layout 优化 |
| 时间线存在 Free Time、Dequeue 阻塞、host 等待 | 运行时层 | `TASK_QUEUE_ENABLE=2`、`PER_STREAM_QUEUE=1`、`CPU_AFFINITY_CONF=2` |
| 内存峰值高、碎片或 malloc/free 压力大 | OS/内存层 | `PYTORCH_NPU_ALLOC_CONF`、`LD_PRELOAD=...libtcmalloc.so`、必要时 `MULTI_STREAM_MEMORY_REUSE` |
| 不知道慢在哪 | 先做 profiling | 跳转 `ascend-profiling` skill |

## 常用代码层模式

| 模式 | 可评估 API | 何时考虑 | 关键约束 |
|------|------------|----------|----------|
| 手写 RMSNorm | `torch_npu.npu_rms_norm` | pre-norm / RMSNorm 路径热点 | 返回 tuple，取 `[0]` |
| residual + LayerNorm | `torch_npu.npu_add_layer_norm` | post-norm block 且 add+LN 在同一路径 | 需要 residual 和 LN 紧邻 |
| SwiGLU | `torch_npu.npu_swiglu` | 门控 FFN 热点 | `SiLU(first_half) * second_half`，注意 concat 顺序 |
| RoPE | `torch_npu.npu_rotary_mul` | 手写 rotary 逻辑热点 | `cos/sin` 需 `expand_as(x)` |
| 因果 attention | `torch_npu.npu_fusion_attention` | 手写 attention 热点 | `atten_mask` 为 bool，`True=mask out` |
| 全量 flash attention | `torch_npu.npu_prompt_flash_attention` | fp16/bf16 attention 场景 | 不适合作为 fp32 默认方案 |
| GeGLU | `torch_npu.npu_gelu_mul` | GeGLU MLP 热点 | 末维需满足 API 约束 |
| 两层 FFN | `torch_npu.npu_ffn` | bf16/fp16 MLP 热点 | 仅适用于受支持精度与布局 |

## Attention 与 layout 关键规则

- `npu_fusion_attention` 的 `atten_mask` 语义是 `True=屏蔽`、`False=参与`，与常见 float additive mask 不同。
- 因果 attention 通常仍需要显式 causal bool mask，不要仅依赖窗口参数推断语义。
- `input_layout` 必须与真实张量布局一致；常见推理代码中容易混淆 `BSND` 与 `BNSD`。
- `permute`、`transpose` 后优先补 `contiguous()`，再交给融合算子。

## 通用运行时优化

### 一级流水优化

| 项目 | 内容 |
|------|------|
| 何时使用 | host-bound 严重、Free Time 明显、NPU 等待 host |
| 如何开启 | `export TASK_QUEUE_ENABLE=2` |
| 风险 | 可能增加峰值显存 |
| 互斥/限制 | `ASCEND_LAUNCH_BLOCKING=1` 时不生效 |

### Stream 级 TaskQueue 并行下发

| 项目 | 内容 |
|------|------|
| 何时使用 | 多线程多流场景，且 `Dequeue` 阻塞明显 |
| 如何开启 | `export TASK_QUEUE_ENABLE=2` 后再 `export PER_STREAM_QUEUE=1` |
| 风险 | 线程更多，可能出现资源抢占；event 交互下一级流水可能额外耗时 |
| 互斥/限制 | 依赖 `TASK_QUEUE_ENABLE=1/2`；不支持细粒度绑核；不适用于快恢场景 |

### CPU 绑核

| 项目 | 内容 |
|------|------|
| 何时使用 | CPU 调度开销高、线程漂移明显、跨 NUMA 干扰严重 |
| 如何开启 | 默认先试 `export CPU_AFFINITY_CONF=2` |
| 风险 | NUMA 映射、容器 cpuset、虚拟化拓扑不匹配时可能适得其反 |
| 互斥/限制 | 自定义区间仅支持粗粒度模式；与 `PER_STREAM_QUEUE=1` 不应作为默认组合 |

补充规则：

- `CPU_AFFINITY_CONF=1` 是粗粒度绑核，适合做按卡划分或自定义绑核区间。
- `CPU_AFFINITY_CONF=2` 是细粒度绑核，适合隔离热点线程，默认优先推荐。
- 自定义线程会继承主线程亲和性；在线程拉起前后使用 `torch_npu.utils.set_thread_affinity` / `reset_thread_affinity` 管理。

## 通用 OS / 内存优化

### 高性能内存库替换

| 项目 | 内容 |
|------|------|
| 何时使用 | Python/host 侧 malloc/free 频繁、锁竞争或 allocator 成为瓶颈 |
| 如何开启 | `LD_PRELOAD=/path/to/libtcmalloc.so python infer.py` |
| 风险 | 系统级依赖，需确认动态库路径和兼容性 |
| 互斥/限制 | 不作为默认推理模板，只在 allocator-bound 迹象明确时使用 |

### NPU 内存分配配置

| 项目 | 内容 |
|------|------|
| 何时使用 | 大块分配失败、碎片化明显、显存利用波动大 |
| 如何开启 | `export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:512` |
| 风险 | 需要结合实际 workload 调参，不能假设 512 永远最优 |
| 互斥/限制 | 无硬性互斥，但应与当前显存曲线一起验证 |

### 多流内存复用

| 项目 | 内容 |
|------|------|
| 何时使用 | 真实多流场景下，跨流依赖导致内存回收延迟、峰值显存偏高 |
| 如何开启 | `export MULTI_STREAM_MEMORY_REUSE=1` |
| 风险 | 是场景化优化，不适合作为单流推理的默认建议 |
| 互斥/限制 | 仅在存在跨流内存复用需求时再讨论；值 `2` 在官方文档中标注为当前不推荐默认使用 |

## 通用命令模板

```bash
# baseline
python infer.py

# 一级流水
TASK_QUEUE_ENABLE=2 python infer.py

# 多线程多流
TASK_QUEUE_ENABLE=2 PER_STREAM_QUEUE=1 python infer.py

# 绑核
CPU_AFFINITY_CONF=2 python infer.py

# tcmalloc
LD_PRELOAD=/path/to/libtcmalloc.so python infer.py

# 显存碎片调优
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:512 python infer.py
```

## 验证 checklist

- 同输入、同随机种子、同 batch
- 同 dtype、同设备、同 warmup 策略
- 先看端到端耗时，再看热点算子是否下降
- 代码层替换后检查输出 shape、dtype、mask 语义、数值精度
- 环境变量优化后复查显存峰值、CPU 利用率、线程数与时间线变化
- 只在证据表明瓶颈匹配时保留该优化，否则回退

## 官方参考

- 性能调优流程（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/performance_tuning_0001.html
- Free Time / Host 问题定位（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/performance_tuning_0018.html
- 一级流水与瓶颈分析（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/performance_tuning_0019.html
- 流水优化 `TASK_QUEUE_ENABLE=2`（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/performance_tuning_0059.html
- Stream 级 TaskQueue 并行下发 `PER_STREAM_QUEUE`（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/Frameworkfeatures/docs/zh/framework_feature_guide_pytorch/stream_taskqueue_parallel_delivery.md
- 自动绑核 `CPU_AFFINITY_CONF`（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/Frameworkfeatures/docs/zh/framework_feature_guide_pytorch/automatic_core_binding.md
- `CPU_AFFINITY_CONF` 环境变量参考（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/comref/Envvariables/docs/zh/environment_variable_reference/CPU_AFFINITY_CONF.md
- 高性能内存库替换 `tcmalloc`（PyTorch 7.0.0）：https://www.hiascend.com/document/detail/zh/Pytorch/700/ptmoddevg/trainingmigrguide/performance_tuning_0068.html
- 多流内存复用（PyTorch 7.3.0）：https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/Frameworkfeatures/docs/zh/framework_feature_guide_pytorch/multistream_memory_reuse.md
