---
name: human-ui
description: Execute a production UI engineering task using Human UI Engineering standards.
user-invocable: true
argument-hint: "[task or instruction]"
---

# Human UI Engineering (Cursor Skill Adapter)

This adapter enables Cursor Composer and Chat to invoke `/human-ui`.

👉 **Canonical Skill Engine**: [skills/human-ui/SKILL.md](../../../skills/human-ui/SKILL.md)

## Cursor Execution Directives

1. When the user types `/human-ui` or references `@human-ui`, parse the subcommand (`design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`).
2. Read the corresponding reference from [skills/human-ui/references/](../../../skills/human-ui/references/).
3. Execute within existing project conventions following [AGENTS.md](../../../AGENTS.md).

