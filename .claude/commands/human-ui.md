---
description: Execute a production-grade UI engineering or full-stack software task using the Human UI Engineering system.
argument-hint: "[mode?] [task or instruction]"
---

# Human UI Engineering Slash Command

You have been invoked via the `/human-ui` command with the following arguments:

`$ARGUMENTS`

## Execution Instructions

1. **Load Canonical Skill**: Read and execute the instructions in [skills/human-ui/SKILL.md](../../skills/human-ui/SKILL.md).
2. **Handle Mode**:
   - If `$ARGUMENTS` starts with `recover`, execute [skills/human-ui/references/recovery.md](../../skills/human-ui/references/recovery.md).
   - If `$ARGUMENTS` starts with `status`, execute [skills/human-ui/references/status.md](../../skills/human-ui/references/status.md).
   - If `$ARGUMENTS` starts with a mode (`plan`, `build`, `design`, `architect`, `audit`, `debug`, `refactor`, `test`, `review`, `security`, `performance`, `docs`, `release`), load the corresponding reference in `skills/human-ui/references/`.
   - Otherwise, detect the project framework and execute the general task using the engineering workflow in [AGENTS.md](../../AGENTS.md).
3. **Preserve Code Integrity**: Never delete unrelated existing code; validate all changes with automated tests or linters.
