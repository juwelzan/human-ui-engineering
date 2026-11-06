# Status Mode Reference (`/human-ui status`)

> **Active Task State, Checkpoint Inspection & Blocker Telemetry**

When invoked with `/human-ui status`:

1. **Inspect Active State**:
   - Read [`../../../AI_TASK_STATE.md`](../../../AI_TASK_STATE.md) at the repository root.
   - Inspect git status via `git status --porcelain`.
   - Inspect recent git commits via `git log -3 --oneline`.
2. **Present Concise Status Report**:
   - Current task name and target outcome.
   - Active phase and milestone checklist (completed vs remaining).
   - Last verified commit / checkpoint hash.
   - Known blockers or pending user inputs.
   - Next recommended safe action.

