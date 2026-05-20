# Ascend C Regbase Knowledge Index

This is the global retrieval entry for `ascendc-regbase-best-practice`, organized so agents can enter by stage, knowledge type, platform context, or common question.

`reference-ops` is a conditional asset. Do not treat it as a default entry point unless the task already needs at least one existing regbase implementation to inspect.

## Routing Rules

- Start with one primary branch: `knowledge/regbase_development_guide`, `knowledge/index`, or `reference-ops/open_source_operator_table`.
- If you enter `api/`, `patterns/`, `pitfalls/`, or `dev-experience/`, read that directory's `index.md` before any leaf note.
- For one subproblem, expand at most 5 leaf notes from a directory. If that is still not enough, split the subproblem or switch branches.

## By Task Stage

- Branch entry and scoping: [[knowledge/regbase_development_guide]], [[knowledge/index]], [[knowledge/dev-experience/index]]
- Design and walkthrough: [[knowledge/index]], [[knowledge/patterns/index]]
- Implementation: [[knowledge/api/index]], [[knowledge/patterns/index]]
- Review: [[knowledge/pitfalls/index]], [[knowledge/dev-experience/index]]
- Repair and debugging: [[knowledge/pitfalls/index]], [[knowledge/dev-experience/index]]
- Reference-implementation selection: [[reference-ops/open_source_operator_table]]

## By Knowledge Type

- Practical development mainline: [[knowledge/regbase_development_guide]]
- Core knowledge hub: [[knowledge/index]]
- API constraints and signatures: [[knowledge/api/index]]
- Regbase implementation patterns: [[knowledge/patterns/index]]
- Pitfalls and precision risks: [[knowledge/pitfalls/index]]
- Workflow and execution experience: [[knowledge/dev-experience/index]]
- Reference-implementation selection: [[reference-ops/open_source_operator_table]]

## By Platform Context

- `ascend950 / regbase` primary path: [[knowledge/api/index]], [[knowledge/patterns/index]], [[knowledge/dev-experience/index]]
- `ascend910b / membase` compatibility context: [[knowledge/index]], [[knowledge/pitfalls/index]]
- Existing-code reference context: [[reference-ops/open_source_operator_table]]

## Common Questions

- How do I actually develop a regbase operator end to end? [[knowledge/regbase_development_guide]]
- Which APIs are safe to start from in regbase? [[knowledge/api/index]]
- How should I structure a regbase kernel or VF / Reg-MicroAPI chain? [[knowledge/patterns/index]]
- Where do precision and numeric stability issues usually come from? [[knowledge/pitfalls/index]]
- Which existing regbase operators are worth checking as real reference implementations? [[reference-ops/open_source_operator_table]]
- What operational experience should I use before coding or repairing? [[knowledge/dev-experience/index]]

## Related Documents

- [[knowledge/regbase_development_guide]]
- [[knowledge/index]]
- [[reference-ops/open_source_operator_table]]
