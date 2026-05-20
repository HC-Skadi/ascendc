# quantify-agent（昇腾模型生态·模型量化Agent）

**昇腾 NPU 上模型量化**：基于 **msmodelslim** 等链路的 W8A8 / W4A8 量化、**敏感度分析**，以及 vLLM 在昇腾侧的安装与运行说明。本仓以 **Markdown 文档 / SKILL** 为主，供 Agent 与工程师查阅。

## 在 MoFixGo 中的位置

**[MoFix](https://gitcode.com/MoFixGo/MoFix)** 注册工具将用户意图映射到下列能力（实现可为占位，以文档为准逐步落地）：

| MoFix 工具名 | 说明 |
|--------------|------|
| `quantify_run_msmodelslim` | msmodelslim 量化任务 |
| `quantify_sensitivity_analysis` | 敏感度分析 |

实现见：`MoFix/examples/tools/quantify_agent_tools.py`。

## 目录说明

| 文件 | 说明 |
|------|------|
| `SKILL.md` | 量化工具链总述 |
| `msmodelslim.md` | msmodelslim 使用要点 |
| `sensitivity-analysis.md` | 敏感度分析 |
| `vllm-install.md` / `vllm-run.md` | vLLM 安装与运行 |
| `ais_bench.md` | 评测相关（若有） |

## 远程仓库

```bash
git clone https://gitcode.com/MoFixGo/quantify-agent.git
```

组织主页：[MoFixGo](https://gitcode.com/MoFixGo)
