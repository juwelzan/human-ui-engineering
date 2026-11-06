---
description: Execute a production-grade UI engineering task using the Human UI Engineering system.
argument-hint: "[task or instruction]"
---

# Human UI Engineering Slash Command

You have been invoked via the `/human-ui` command with the following arguments:

`$ARGUMENTS`

## Execution Instructions

1. **Load Canonical Skill**: Read and execute the instructions in [skills/human-ui/SKILL.md](../../skills/human-ui/SKILL.md).
2. **Handle Mode**:
   - If `$ARGUMENTS` starts with `recover`, execute [skills/human-ui/references/recovery.md](../../skills/human-ui/references/recovery.md).
   - If `$ARGUMENTS` starts with a specific mode (`design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `review`), load the corresponding reference in `skills/human-ui/references/`.
   - Otherwise, detect the project framework and execute the general task using the 14-step workflow in [AGENTS.md](../../AGENTS.md).
3. **Preserve Code Integrity**: Never delete unrelated existing code; validate all changes with automated tests or linters.

