---
title: Regbase API Sync
purpose: Distinguish queue handoff, VF lane control, local event flags, pipe barriers, stronger full barriers, and cross-core coordination so sync choices stay on the right layer.
read_when:
  - The task needs a sync decision tree rather than a single generic sync answer.
  - You are debugging or designing handoff boundaries around regbase kernels.
not_for:
  - Top-level operator classification
  - Pure build failures
keywords:
  - sync
  - queue handoff
  - VF
  - overlap
next_reads:
  - ../patterns/regbase_sync_patterns.md
  - ../pitfalls/symptom_to_cause.md
  - regbase_api_whitelist.md
depth: foundation
topic_type: api
---

# Regbase API Sync

This card records synchronization decisions that commonly appear around regbase kernels. Use it to distinguish:

- UB-stage handoff
- VF-internal lane control
- local directional event sync
- pipe-local barriers
- stronger full barriers
- cross-core coordination

Do not collapse those into one “sync” concept.

## 1. Sync Types And Typical Primitives

Use this table first when the question is "what kind of synchronization is this?".

| Sync type | What it coordinates | Typical primitive(s) | Typical direction or shape | Use when | Do not treat it as |
|---|---|---|---|---|---|
| Queue handoff | readiness between `CopyIn`, `Compute`, and `CopyOut` around UB tiles | `EnQue`, `DeQue` | stage-to-stage handoff inside one kernel shell | a stage must wait until the current UB tile is ready | VF-internal event sync |
| VF lane control | active lanes and register load/store semantics inside `__VEC_SCOPE__` | `MaskReg`, `LoadDist`, `StoreDist` | lane masks and register distribution policies | you are shaping how the VF body loads, computes, or stores | barrier, flag, or queue sync |
| Local directional event sync | explicit producer-consumer ordering between local pipes when overlap is manual | `SetFlag`, `WaitFlag` | `HardEvent::MTE2_V`, `V_MTE2`, `S_V`, `V_S`, `S_MTE3`, `MTE3_MTE2` and similar directional pairs | vector work and movement work are overlapped manually and the reference implementation already uses event flags | a default requirement for light regbase kernels |
| Pipe-local barrier | flush or order work inside one pipe before continuing | `PipeBarrier<PIPE_V>`, `PipeBarrier<PIPE_M>`, `PipeBarrier<PIPE_ALL>` | one pipe or all local pipes | a single pipe needs an explicit barrier after a staged sequence | cross-core or queue handoff |
| Whole-kernel / all-core barrier | stronger block-wide or all-used-core synchronization | `SyncAll()` or `SyncAll(gmWorkspace, ubWorkspace, usedCores)` | full local barrier or workspace-backed all-core sync | the design truly needs a stronger synchronization point than local flags | ordinary VF sequencing |
| Cross-core coordination | dependencies between different cores or sub-blocks | `CrossCoreSetFlag`, `CrossCoreWaitFlag` | flag-based inter-core producer/consumer | one core must wait for another core’s progress | a patch for local UB ordering |

The directional `HardEvent::*` names are part of the sync type, not incidental decoration. They tell you which producer/consumer relationship is being synchronized.

## 2. Default Reading

For most regbase operators:

- the outer kernel shell may still use queue-based stage handoff
- the VF body usually does not need explicit event synchronization
- advanced `SetFlag` / `WaitFlag` patterns are a special case, not the default
- `PipeBarrier` and `SyncAll` are heavier than ordinary stage ordering, so add them only after the lighter models are ruled out

## 3. Queue-Based Stage Handoff

When the kernel uses queue-backed UB staging:

- `EnQue` marks a UB tile ready for the next stage
- `DeQue` makes the next stage wait until that tile is ready

That is valid local stage ordering in the kernel shell. It is not a sign that the task has automatically left the regbase path.

Use this model when the question is:

- has `CopyIn` finished preparing the current UB tile?
- can `Compute` consume it yet?
- can `CopyOut` now write the finished UB tile?

## 4. VF Lane Control Is Not Event Sync

Inside `__VEC_SCOPE__`:

- `MaskReg` controls active lanes
- `LoadDist` controls how UB data is loaded into register objects
- `StoreDist` controls how register results are written back to UB

These are part of the VF execution model. They do not replace:

- queue lifecycle
- event flags
- cross-core coordination

## 5. Explicit Event Flags

Use explicit flags only when the design truly overlaps movement and compute manually.

Typical families:

- `SetFlag`
- `WaitFlag`

Typical directional pairs seen in SDK code include:

- `HardEvent::MTE2_V` / `HardEvent::V_MTE2`
- `HardEvent::S_V` / `HardEvent::V_S`
- `HardEvent::S_MTE3`
- `HardEvent::MTE3_MTE2`

Typical use:

- ping-pong overlap between vector work and MTE work
- proving that a bug is caused by missing stage ordering
- advanced kernels with multiple concurrent UB slices

Do not add explicit flags to a simple regbase kernel unless a real reference operator proves the need.

## 6. Pipe Barriers And Stronger Barriers

Use `PipeBarrier<PIPE_*>` when a specific pipe or the whole local pipe set must be ordered before continuing.

Typical shapes:

- `PipeBarrier<PIPE_V>`: order vector-pipe work
- `PipeBarrier<PIPE_M>`: order matrix or M-pipe work
- `PipeBarrier<PIPE_ALL>`: local full-pipe barrier

`PipeBarrier` is still local to the current core and local pipeline context. It is not a substitute for cross-core or workspace-backed synchronization.

Use `SyncAll` only when the design truly needs a stronger full barrier:

- `SyncAll()`: stronger whole-kernel barrier style entry
- `SyncAll(gmWorkspace, ubWorkspace, usedCores)`: workspace-backed barrier form

Treat `SyncAll` as a heavy tool. Do not add it to solve a problem that is really just a missing queue handoff or a missing local directional flag.

## 7. Cross-Core Coordination

Use cross-core flags only for real inter-core dependencies:

- `CrossCoreSetFlag`
- `CrossCoreWaitFlag`

These are not substitutes for local UB stage ordering. They are also a device- and design-sensitive choice, so verify actual platform support before depending on them.

## 8. Practical Decision Path

1. Ask whether the problem is UB-stage readiness, VF lane semantics, explicit overlap, local pipe ordering, stronger full barriers, or cross-core dependency.
2. For UB-stage readiness, start with queue lifecycle or stable stage ordering.
3. For VF bodies, keep `MaskReg` and `LoadDist` / `StoreDist` in the “register semantics” bucket, not the “sync primitive” bucket.
4. If the design overlaps pipes manually, choose the directional `HardEvent::*` pair first, then use `SetFlag` / `WaitFlag`.
5. Add `PipeBarrier<PIPE_*>` only when one local pipe really needs an explicit barrier.
6. Use `SyncAll` only when a stronger barrier is genuinely required.
7. Use cross-core flags only when the design truly crosses core boundaries.

## Related Documents

- [[../regbase_development_guide]]
- [[../patterns/regbase_sync_patterns]]
- [[../patterns/regbase_kernel_dataflow_patterns]]
- [[pipeline_and_buffer]]
- [[precision_and_runtime]]
