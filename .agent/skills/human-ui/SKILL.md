---
name: human-ui
description: Human UI Engineering context and execution system for building production-grade, human-centered user interfaces and full-stack software systems. Activate when the user asks to plan, design, implement, build, audit, review, debug, test, secure, optimize, or document software across Flutter, React, Next.js, Vue, Angular, React Native, Android, iOS, Web, Desktop, Backend, or Databases, or explicitly invokes the /human-ui slash command.
metadata:
  icon: terminal
  version: 3.0.0
---

# Human UI Engineering (Antigravity Adapter)

This is the Antigravity local agent skill entry point. It routes directly to the canonical skill engine:

👉 **Canonical Skill**: [skills/human-ui/SKILL.md](../../../skills/human-ui/SKILL.md)

## Execution Instructions for Agent

1. Parse any subcommands passed to `/human-ui`:
   - `plan`, `build`, `design`, `architect`, `audit`, `debug`, `refactor`, `test`, `review`, `security`, `performance`, `docs`, `release`, `recover`, `status`.
2. Follow the 5-step progressive disclosure protocol in [skills/human-ui/SKILL.md](../../../skills/human-ui/SKILL.md).
3. Anchor all actions to the master engineering instructions in [AGENTS.md](../../../AGENTS.md).
