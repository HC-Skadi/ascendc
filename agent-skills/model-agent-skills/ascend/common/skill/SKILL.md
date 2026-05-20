---
name: ops-easyasc-dsl
description: Use this skill when working in the ops-easyasc-dsl repository to drive the easyasc DSL to AscendC workflow under agent/. Restore archived runtime, docs, and examples with agent/scripts/init.sh before tasks that need easyasc/, doc/, doc_cn/, or agent/example/, then route through agent/ROUTER.md for progressive disclosure.
---

# ops-easyasc-dsl

## First Step

If `easyasc/`, `doc/`, `doc_cn/`, or `agent/example/` are missing from the repository, run:

```bash
bash agent/scripts/init.sh
```

Use that before:

- importing `easyasc.a5` or `easyasc.a2`
- reading `doc/` or `doc_cn/`
- running examples under `agent/example/`
- using workflow helpers that inspect example kernels

## Workflow Location

The callable easyasc DSL to AscendC workflow lives under `agent/`.

After initialization, use:

- `agent/ROUTER.md` for the first routing pass
- `agent/playbooks/` for short workflow guidance
- `agent/references/` for focused constraints, patterns, and repo maps
- `agent/index/` for machine-readable example lookup
- `agent/scripts/` for workflow utilities and repository maintenance

## Progressive Disclosure

Prefer this read order:

1. `agent/ROUTER.md`
2. one playbook under `agent/playbooks/`
3. one focused file under `agent/references/`
4. one concrete source file under `agent/example/kernels/` or `agent/example/demo/`

Do not load the whole repository summary when a smaller route answers the task.

## Key Working Areas

- Skill entrypoint: `skill/`
- Workflow router and references: `agent/`
- Kernel examples: `agent/example/kernels/`
- Manual demos: `agent/example/demo/`
- Repository scripts: `agent/scripts/`
- Script reference summary: `agent/scripts/tools_summary.md`
- Archived runtime/docs payload: `agent/assets/ops-easyasc-dsl-runtime.tar.gz`
- Archived example payload: `agent/assets/ops-easyasc-dsl-example.tar.gz`

## Local Environment Hints

- preferred local Python environment: any environment that already has the dependencies you need; `torch210npu` is only an example
- CANN install root: use your local toolkit path via `ASCEND_HOME_PATH`; do not assume a fixed machine-specific directory
- common validation command: `python agent/example/kernels/a5/matmul_float_mmad.py`

That kernel should validate both `OpExec(..., simulator=True)` and `OpExec(..., simulator=False)`.
