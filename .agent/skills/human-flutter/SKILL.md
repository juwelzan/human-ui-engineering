---
name: human-flutter
description: Human Flutter Engineering context and execution system for building production-grade, human-centered Flutter & Dart applications across Mobile, Web, and Desktop. Activate when the user asks to plan, design, implement, build, audit, review, debug, test, secure, optimize, or release Flutter applications, or explicitly invokes the /human-flutter or /human-ui slash command.
metadata:
  icon: flutter
  version: 4.0.0
---

# Human Flutter Engineering (Antigravity Workspace Skill)

This is the lightweight Antigravity agent skill entry point. It delegates execution directly to the canonical skill engine:

👉 **Canonical Skill**: [skills/human-flutter/SKILL.md](../../skills/human-flutter/SKILL.md)

## Execution Instructions for Agent

1. Parse any subcommand passed to `/human-flutter` (or alias `/human-ui`):
   - `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
2. Follow the progressive disclosure protocol in [skills/human-flutter/SKILL.md](../../skills/human-flutter/SKILL.md).
3. Strictly enforce the **Absolute Flutter-Only Rule** and execute the 18-step workflow defined in [AGENTS.md](../../AGENTS.md).
