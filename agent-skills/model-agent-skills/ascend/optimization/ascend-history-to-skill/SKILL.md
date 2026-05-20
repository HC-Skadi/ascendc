---
name: ascend-history-to-skill
description: 从本机 Codex、Claude Code、OpenCode、Cursor 的历史记录中检索指定昇腾模型的适配、迁移、推理优化和性能验证记录，并基于已验证步骤生成或更新模型专属 skill。适用于用户要求“从历史里找某个 Ascend 模型的适配/优化记录”“把过去做过的昇腾迁移整理成 skill”“复用 Codex/Claude/Cursor/OpenCode 聊天记录形成可复现技能”时触发。
---

# Ascend History To Skill

## Overview

这个 skill 用于把历史对话、执行记录、会话日志中的昇腾经验沉淀成可复用 skill。
优先提取已经跑通过的环境、代码修改、验证命令、性能结果和排错结论，避免把未验证的讨论直接写进 skill。

## Workflow

### 1. 明确目标模型和范围

先确认以下信息；若用户没给全，做最小必要推断：

- 目标模型名，如 `esm2`、`DiffSBDD`、`Boltz2`
- 目标阶段：`适配`、`优化`，或两者都要
- 历史来源：`codex`、`claude-code`、`opencode`、`cursor`，默认全搜
- 输出位置：默认写到 `~/.codex/skills/<model-skill-name>/`

若模型名存在常见变体，同时搜索：

- 原始名，如 `esm2_t33_650M_UR50D`
- 仓库名，如 `esm-main`
- 连字符、下划线、大小写变体

### 2. 搜索历史记录

优先运行脚本：

```bash
python scripts/search_history.py --model esm2 --stage adapt,optimize --output markdown
```

按需补充关键词：

```bash
python scripts/search_history.py   --model esm2   --stage adapt,optimize   --keyword torch_npu   --keyword TASK_QUEUE_ENABLE   --keyword esm2_t33_650M_UR50D
```

若默认路径没命中，读取 [references/history-sources.md](references/history-sources.md)，再显式追加 `--root`。

如果命中里混入当前任务或其他噪声，可追加 `--exclude-term <keyword>` 做二次过滤。

### 3. 只保留高价值证据

优先保留这些记录：

- 明确的环境创建与依赖安装命令
- 已落地的代码修改点、脚本路径、关键参数
- 真实跑通的验证命令和输出产物
- 有数字的性能对比、精度对比、benchmark 结论
- 真实报错及对应修复

降权或丢弃这些记录：

- 只有用户提问、没有执行结果的片段
- 纯 brainstorming、没有落地命令的讨论
- 与目标模型无关、只共享“昇腾”关键词的记录
- 被后续记录推翻的旧方案

### 4. 整理成 skill 素材

从命中的历史中提炼以下结构化信息：

- 模型/仓库定位：仓库路径、入口脚本、权重名
- 环境要求：Python、torch、torch_npu、CANN、conda 环境名
- 适配步骤：入口注入、CUDA API 替换、第三方库处理、分布式约束
- 优化步骤：热点路径修改、运行时环境变量、benchmark 口径
- 验证步骤：README 命令、最小推理、精度/性能验收标准
- 常见问题：真实遇到的错误和修复动作

如果历史里同一模型已有旧 skill，优先更新它，而不是再造一个近似副本。

### 5. 生成模型 skill

新 skill 应尽量复用历史中已经证明可行的命令和路径，避免重新发明流程。
生成时遵循这些规则：

- 默认输出目录：`~/.codex/skills/<model-skill-name>/`
- `SKILL.md` 要写清触发场景，不要只写模型名
- 只写已验证通过的步骤；未验证内容必须明确标注
- 若同一模型同时有“适配”和“优化”记录，按“先能跑、再跑快”的顺序组织
- 若历史里有本地脚本、命令模板、验证模板，优先放进 `scripts/` 或 `references/`

### 6. 生成后验证

至少做两类验证：

1. 结构验证：

```bash
python /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/<model-skill-name>
```

2. 内容验证：

- 检查 skill 中引用的路径、环境名、脚本名在本机是否真实存在
- 检查验证命令是否来自历史中的成功记录，而不是未执行草案
- 若有性能数字，确认 baseline 和优化版口径一致

## Notes

- 历史路径和存储格式会随工具版本变化。默认脚本只提供常见位置，必要时自行扩展 `--root`。
- SQLite 命中需要二次人工确认上下文，避免把 unrelated row 当作结论。
- 如果不同工具历史互相矛盾，以最近、已验证、带产物的记录为准。
- 当用户要“直接生成 skill”时，不要停在搜索结果；应继续整理并落盘。
