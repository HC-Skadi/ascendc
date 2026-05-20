---
name: ascendc-regbase-best-practice
description: Use when a task has already been routed into the Ascend C regbase branch, or when the request explicitly mentions regbase 设计、regbase 开发、regbase 融合算子开发, and the work needs regbase-specific API guidance, implementation patterns, pitfalls, development experience, or fusion-operator development support for ascend950.
---

# Ascend C Regbase Development

This skill is the shared knowledge pack for tasks that have already entered the `regbase` branch in the team workflow. It does not decide branch routing by itself. Its job is to provide a reliable regbase-oriented reading path across API constraints, implementation patterns, pitfalls, engineering experience, and lightweight reference-implementation selection.

The `reference-ops` subtree is intentionally lightweight. A name match or a basic-type match in the operator table is only a screening lead for choosing a reference implementation to inspect. It is not evidence that the source implementation can be copied, fused, or reused without a fresh regbase-specific design judgment.

## When To Use

Use this skill when:

- the task is already confirmed as `ascend950 / regbase` work
- the user explicitly asks for regbase design, development, review, or debugging guidance
- the agent needs regbase-specific API constraints instead of generic default operator-development assumptions
- the task needs regbase implementation patterns, pitfalls, or development experience before coding or repair
- the task needs to choose at least one existing regbase operator implementation to inspect before coding
Do not use this skill as a generic replacement for the default operator-development path. If the task has not been routed into the regbase branch, follow the team workflow first and only load this skill when the regbase branch is actually in scope.

## Reading Order

1. Read `references/index.md` first for global entry points.
2. Read `references/knowledge/regbase_development_guide.md` when the task needs a practical end-to-end regbase development path instead of only isolated cards.
3. Read `references/knowledge/index.md` when you need to choose between API, patterns, pitfalls, or development experience.
4. Inside `api/`, `patterns/`, `pitfalls/`, or `dev-experience/`, read that directory's `index.md` before opening leaf documents.
5. For one subproblem, use the directory index fields `purpose`, `read_when`, and `keywords` to select the relevant leaf documents, and expand at most 5 of them before you either close the question or split it into smaller subproblems.
6. Read `references/reference-ops/open_source_operator_table.md` only when you need to choose at least one existing regbase implementation to inspect before coding.

## Asset Map

- `references/index.md`: top-level retrieval map for agentic navigation.
- `references/knowledge/regbase_development_guide.md`: practical main guide for developing a regbase operator end to end.
- `references/knowledge/api/`: regbase API reference, whitelist, synchronization notes, and API-adjacent best practices.
- `references/knowledge/patterns/`: regbase operator structure, tiling patterns, reduction patterns, broadcast patterns, kernel dataflow patterns, buffer partitioning, and sync patterns.
- `references/knowledge/pitfalls/`: common traps, symptom-to-cause lookup, API misuse cases, precision failure modes, and regbase-vs-membase confusion points.
- `references/knowledge/dev-experience/`: distilled engineering experience, route selection heuristics, build habits, case notes, performance practices, and high-signal implementation notes.
- `references/reference-ops/open_source_operator_table.md`: lightweight open-source operator table with operator name, basic type, and code path for reference-implementation selection.

## Guardrails

- Treat this skill as a regbase-specific supplement, not as the owner of team-level workflow routing.
- Prefer the indexed reading path. Do not load the entire subtree when one index can route you to the right branch.
- Inside `api/`, `patterns/`, `pitfalls/`, and `dev-experience/`, always use the directory `index.md` as the routing table before reading leaf notes.
- For one subproblem, stop at 5 leaf notes and either close the question or split it into narrower subproblems.
- Before coding a new regbase operator, inspect at least one existing regbase operator implementation located through `open_source_operator_table.md`.
- Do not treat a candidate from `open_source_operator_table.md` as proof of direct reusability. The table exists to help you choose real regbase code to inspect, not to make automatic reuse decisions.
- Keep platform reasoning explicit. If a note comes from compatibility experience rather than the primary `ascend950 / regbase` path, say so.
