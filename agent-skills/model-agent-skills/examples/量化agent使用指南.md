# 昇腾量化 Agent 使用指南

## 目录

- [概述](#概述)
- [功能特性](#功能特性)
- [系统要求](#系统要求)
- [与 MoFix 的对接](#与-mofix-的对接)
- [快速开始](#快速开始)
- [详细使用指南](#详细使用指南)
- [端到端迭代流程（量化闭环）](#端到端迭代流程量化闭环)
- [工具与文档索引](#工具与文档索引)
- [环境变量与运行规范](#环境变量与运行规范)
- [常见问题](#常见问题)
- [参考文档](#参考文档)
- [版本信息](#版本信息)

---

## 概述

**量化 Agent** 面向华为昇腾 NPU 上的大模型压缩与推理落地，覆盖 **msmodelslim 量化**、**敏感度分析**、**vLLM-Ascend 安装与运行**，以及基于 **AISBench** 的精度/性能评测。其方法论与操作要点与开源技能集 [gvim · g-claude/skills/ascend](https://github.com/starmountain1997/gvim/tree/main/g-claude/skills/ascend) 一致；本指南在 MoFix 场景下做结构化说明，便于工程师与对话 Agent 按同一套规范执行。

### 适用场景

- 在 Atlas 800 A2/A3 等昇腾设备上对 LLM 做 **W8A8 / W4A8** 等量化并落盘权重
- 量化后精度相对 FP16 基线下降，需要通过 **敏感度分析** 定位层并调整 YAML
- 量化模型用 **vLLM-Ascend** 拉起服务，并用 **GSM8K** 等任务做快速精度回归
- 需要 **可复现日志**：长命令通过脚本执行并将 stdout/stderr 落盘

---

## 功能特性

| 功能 | 说明 |
|------|------|
| **硬件预检** | 通过 `npu-smi info` 确认 NPU 健康与占用，避免与已有 vLLM/训练进程冲突 |
| **msmodelslim 量化** | 支持 `lab_practice` 一键匹配或自定义 YAML；支持 `analyze` 敏感度扫描 |
| **压缩档位策略** | 从 w4a4 → bf16 的分级回退思路，需在用户确认后再降级精度档位 |
| **vLLM-Ascend** | 源码/可编辑安装与版本对齐；量化模型需 `--quantization ascend` |
| **AISBench 评测** | GSM8K 精度与性能配置模板；接受阈值建议相对 FP16 **≤ 1 个百分点** 跌幅 |
| **运行规范** | 关键任务建议 shell 脚本 + 时间戳日志（见下文模板），便于排障 |

---

## 系统要求

### 硬件要求

| 组件 | 要求 |
|------|------|
| NPU | 与目标模型规模匹配的昇腾卡（如 Atlas 800 A2/A3） |
| 内存 / 存储 | 满足全量权重 + 校准样本 + 导出目录；建议预留充足临时空间 |

### 软件要求

| 软件 | 说明 |
|------|------|
| Python | 量化与 AISBench 侧建议 **3.10–3.11**（以各工具官方要求为准） |
| CANN / 驱动 | 与机型、msmodelslim、torch_npu 版本矩阵一致 |
| msmodelslim / torch_npu | `pip show msmodelslim torch_npu transformers` 可定位安装与可编辑源码路径 |
| vLLM + vllm-ascend | 需 **版本对齐**（见 [vLLM-Ascend 安装要点](#第一步vllm-ascend-安装要点)） |

---

## 与 MoFix 的对接

在 **[MoFix](https://gitcode.com/MoFixGo/MoFix)** 中，量化相关意图可映射到注册工具（实现以 `MoFix/examples/tools/quantify_agent_tools.py` 为准）：

| MoFix 工具名 | 说明 |
|--------------|------|
| `quantify_run_msmodelslim` | 触发或编排 msmodelslim 量化任务 |
| `quantify_sensitivity_analysis` | 触发敏感度分析（`msmodelslim analyze`） |

详细技能与长文说明仍建议查阅仓内 **[quantify-agent](https://gitcode.com/MoFixGo/quantify-agent)** 目录下的 `SKILL.md`、`msmodelslim.md`、`sensitivity-analysis.md`、`vllm-install.md`、`vllm-run.md`、`ais_bench.md`。

---

## 快速开始

### 1. 硬件检查（任意量化 / 推理会话前）

```bash
npu-smi info
```

确认：

- 预期卡均 **Health: OK**
- 无意外进程长期占用（结合「Process ID」等列判断）；释放前需与用户确认

### 2. 通用环境变量（vLLM 与 msmodelslim 共用可见设备）

```bash
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export VLLM_USE_MODELSCOPE=true
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
```

`ASCEND_RT_VISIBLE_DEVICES` 对 **vLLM 与 msmodelslim 同时生效**，请在任一触碰 NPU 的命令前设置。

### 3. 一键量化示例（存在 lab_practice 配置时）

```bash
msmodelslim quant \
  --model_path ${MODEL_PATH} \
  --save_path ${SAVE_PATH} \
  --device npu \
  --model_type <ModelName> \
  --quant_type w8a8 \
  --trust_remote_code True
```

自定义架构（Qwen3、DeepSeek、GLM 等）务必 **`--trust_remote_code True`**。若已有专用 YAML，改用 `--config_path /path/to/config.yaml`（与 `--quant_type` 二选一）。

---

## 详细使用指南

### 第一步：vLLM-Ascend 安装要点

1. 清理冲突安装：`pip uninstall -y vllm vllm-ascend`
2. 克隆 `vllm` 与 `vllm-ascend`，按 **vllm-ascend 工作流中声明的 vLLM commit** 检出 vllm，避免 ABI/API 不一致
3. 安装核心：`cd vllm && VLLM_TARGET_DEVICE=empty pip install -v -e .`
4. 安装插件：`cd vllm-ascend && pip install -v -e .`
5. 验证：`pip list | grep vllm`

### 第二步：量化前校验

```bash
pip show msmodelslim torch_npu transformers
npu-smi info
```

- `transformers` 若不识别目标模型，应先升级至最新；仍不支持则**停止**并告知用户无法量化。

### 第三步：执行量化（msmodelslim）

**策略 A（优先）**：在 `msmodelslim/lab_practice` 中查找与「模型 + 目标 dtype」匹配的 YAML，使用 `--quant_type` 自动匹配或 `--config_path` 显式指定。

**策略 B**：无现成配置时，按 `msmodelslim.md` 中 **参数选择**（如 `act.scope` 与 `symmetric` 约束）编写自定义 YAML。

**策略 C（深度调试）**：参考 msmodelslim 源码 `example/` 下的 Python API，仅建议研发排障使用。

### 第四步：用 vLLM 拉起量化模型

量化权重服务化时须加 **`--quantization ascend`**；BF16/FP16 全精度模型**不要**加该标志，否则可能输出异常或 NaN。

典型环境：

```bash
export VLLM_USE_MODELSCOPE=true
export VLLM_WORKER_MULTIPROC_METHOD=spawn
```

自定义结构需 `--trust-remote-code`。若图模式异常，可先用 `--enforce-eager` 区分算子问题与构图问题。

### 第五步：AISBench 精度回归（GSM8K）

1. 在 benchmark 仓库根目录按文档执行 `pip install -e` 等安装步骤  
2. 向用户确认 **服务端口** 与 **`/v1/models` 返回的 served model 名称**  
3. 编写评测配置（如 `gsm8k_eval.py`），使用 `VLLMCustomAPIChatStream`，`batch_size` 与并发相关  
4. 执行：`ais_bench gsm8k_eval.py --mode all -w ./eval_output`  
5. **验收**：相对 FP16 基线，GSM8K 精度跌幅建议 **≤ 1 个百分点**；超出则进入敏感度分析与 YAML 调整，而非静默降档。

### 第六步：精度不达标时的敏感度分析

仅在评测未通过后执行（勿预先空跑）：

```bash
msmodelslim analyze \
  --model_type <ModelName> \
  --model_path ${MODEL_PATH} \
  --device npu \
  --metrics kurtosis \
  --topk 15 \
  --trust_remote_code True
```

将输出中的敏感层加入配置的 **`exclude`** 或更高精度 **group**（见 quantify-agent 中 `sensitivity-analysis.md`）。**在同一目标 dtype 下重试量化**，未经用户同意不要擅自换成更低压缩档位。

---

## 端到端迭代流程（量化闭环）

下列闭环与 [gvim ascend · SKILL 任务分支](https://github.com/starmountain1997/gvim/tree/main/g-claude/skills/ascend) 及仓内 `msmodelslim.md` 一致：

```
用户指定目标 dtype（如 w4a8 / w8a8）
         │
         ▼
[1] msmodelslim 量化（lab_practice 或自定义 YAML）
         │
         ▼
[2] vLLM 部署量化模型（--quantization ascend）
         │
         ▼
[3] AISBench（如 GSM8K）精度评测
         │
    ┌────┴────┐
  通过      未通过
    │         │
   结束   [4] 敏感度分析 → 调整 disable_names / exclude / 混合精度
            │
            └── 回到 [1]，保持用户原定 dtype，直至通过或用户同意降档
```

### 压缩档位（高 → 低）参考

| 档位 | dtype | 说明 |
|------|--------|------|
| 1 | w4a4 | 多为自定义 YAML；仅当显存极度紧张 |
| 2 | w4a8 | MoE 等常用激进档位 |
| 3 | w8a8 / w8a8s | Dense 模型常用 |
| 4 | w8a16 | 更保守 |
| 5 | w16a16s / bf16 | 接近无损，最后手段 |

---

## 工具与文档索引

| 文档 | 内容 |
|------|------|
| [SKILL.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/SKILL.md) | 昇腾工具链总入口、硬件检查、任务分流 |
| [msmodelslim.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/msmodelslim.md) | 量化协议、YAML、analyze |
| [sensitivity-analysis.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/sensitivity-analysis.md) | 指标选择、输出解读、exclude/group 策略 |
| [vllm-install.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/vllm-install.md) | vLLM + Ascend 插件安装 |
| [vllm-run.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/vllm-run.md) | 运行、排障、eager 模式 |
| [aisbench-accuracy.md](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/aisbench-accuracy.md) | AISBench 精度评测（与仓内 `ais_bench.md` 对应补充） |

MoFix 同主题离线副本见 **`quantify-agent/`** 目录下同名 Markdown。

---

## 环境变量与运行规范

### 推荐：脚本执行 + 时间戳日志

与 [gvim ascend SKILL](https://github.com/starmountain1997/gvim/blob/main/g-claude/skills/ascend/SKILL.md) 一致，**长命令**建议写入 shell 脚本，并将 **stdout/stderr** 一并写入带时间戳的日志，便于回溯：

```bash
cat > run.sh << 'EOF'
#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="${SCRIPT_DIR}/run_$(date +%Y%m%d_%H%M%S).log"

export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3

"$@" 2>&1 | tee "$LOG_FILE"
EOF
chmod +x run.sh
./run.sh your_command_here
```

要点：

- 使用 `2>&1 | tee` 保留终端实时输出与日志文件  
- 日志文件名带时间戳，避免覆盖  
- **前台执行**（避免后台丢日志）；正式环境按运维规范再决定是否 nohup/systemd  

### 调试建议

- 可编辑安装时，用 **`pip show <包名>`** 定位源码目录后再改代码、打分支（如 `debug/quant-issue`）

---

## 常见问题

### Q1: 量化后 vLLM 输出乱码或 NaN？

**可能原因：** BF16 模型误加 `--quantization ascend`，或量化权重与配置不一致。

**处理：** 全精度模型去掉 `quantization`；量化模型确认 ascend 量化格式与 `--quantization ascend` 匹配，并尝试 `--enforce-eager` 对比。

### Q2: GSM8K 跌幅超过 1 个百分点？

**可能原因：** 校准数据与任务分布不匹配、敏感层未保护、档位过激进。

**处理：** 先跑 `msmodelslim analyze`，将 topk 层加入 `exclude` 或混合精度 group，**保持原目标 dtype** 重跑量化；仍失败再与用户确认是否降压缩档位。

### Q3: `npu-smi` 显示卡被占用？

**处理：** 确认 PID 归属，**征得用户同意**后再结束进程；避免误杀共享节点上他人任务。

### Q4: vLLM 与 vllm-ascend 版本不一致报错？

**处理：** 严格按 vllm-ascend CI/文档中指定的 vLLM commit 安装；两仓尽量 **editable** 安装以便对齐与热修。

### Q5: Windows 本机如何对照本指南？

**说明：** 文中命令以 Linux 昇腾训练/推理机为主。Windows 可用于阅读与生成脚本；**实际量化与 NPU 任务**请在昇腾环境或文档指定的容器内执行。

---

## 参考文档

- [gvim · g-claude/skills/ascend](https://github.com/starmountain1997/gvim/tree/main/g-claude/skills/ascend)（技能源仓库）
- [MoFixGo · quantify-agent](https://gitcode.com/MoFixGo/quantify-agent)
- [vLLM Ascend 文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [OpenCompass](https://github.com/open-compass/opencompass)（AISBench 相关上游）

---

## 版本信息

- **文档版本**: 1.0.0  
- **更新日期**: 2026-03-30  
- **对齐参考**: `ascend-model-verification使用指南.md` 结构；技术要点来自 gvim ascend skills 与 MoFix `quantify-agent` 文档
