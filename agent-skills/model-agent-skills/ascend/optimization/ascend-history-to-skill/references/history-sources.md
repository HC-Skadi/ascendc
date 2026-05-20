# History Sources

## Candidate Paths

下面这些路径是常见候选，不保证所有版本都存在。
如果默认搜索无结果，先用 `find` 确认真实路径，再通过 `--root` 追加。

### Codex

- `~/.codex/history.jsonl`
- `~/.codex/sessions/`
- `~/.codex/*.sqlite`
- `~/.codex/log/`

### Claude Code

常见候选：

- `~/.claude/`
- `~/.config/claude/`
- `~/.config/Claude/`

### OpenCode

常见候选：

- `~/.opencode/`
- `~/.config/opencode/`
- `~/.config/OpenCode/`

### Cursor

常见候选：

- `~/.cursor/`
- `~/.config/cursor/`
- `~/.config/Cursor/`

## Evidence Ranking

优先级从高到低：

1. 有成功退出、生成产物、或明确 benchmark 数字的记录
2. 有代码路径、命令、环境名、报错与修复闭环的记录
3. 只有计划和讨论、没有执行证据的记录

## Extraction Checklist

从历史里尽量提取这些字段：

- 模型名及其别名
- 仓库路径
- conda 环境名
- CANN / torch / torch_npu 版本
- 权重名与下载位置
- 入口脚本和关键命令
- 代码修改点
- 性能参数和 benchmark 口径
- 最终验证命令与产物路径
- 已知问题和修复方法
