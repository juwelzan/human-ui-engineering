---
name: human-ui
description: Human UI Engineering context and execution system for building production-grade, human-centered user interfaces. Activate when the user asks to design, implement, audit, review, debug, or optimize UI components, screens, or full frontends across Flutter, React, Next.js, Android, iOS, or Web, or explicitly invokes the /human-ui slash command.
user-invocable: true
argument-hint: "[task or instruction]"
metadata:
  icon: palette
  version: 1.0.0
---

# Human UI Engineering (Antigravity Adapter)

This is the Antigravity local agent skill entry point. It routes directly to the canonical skill engine:

👉 **Canonical Skill**: [skills/human-ui/SKILL.md](../../../skills/human-ui/SKILL.md)

## Execution Instructions for Agent

1. Parse any subcommands passed to `/human-ui`:
   - `design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`.
2. Follow the 5-step progressive disclosure protocol in [skills/human-ui/SKILL.md](../../../skills/human-ui/SKILL.md).
3. Anchor all actions to the 14-step engineering workflow in [AGENTS.md](../../../AGENTS.md).
