---
name: human-flutter
description: Human Flutter Engineering context and execution system for building production-grade, human-centered Flutter & Dart applications across Mobile, Web, and Desktop. Activate when the user asks to plan, design, implement, build, audit, review, debug, test, secure, optimize, or release Flutter applications, or explicitly invokes the /human-flutter or /human-ui slash command.
metadata:
  icon: flutter
  version: 4.1.0
---

# Human Flutter Engineering (Antigravity Workspace Skill)

> Lightweight Antigravity agent skill entry point. Delegates execution directly to the canonical skill engine.

👉 **Canonical Skill**: [skills/human-flutter/SKILL.md](../../../skills/human-flutter/SKILL.md)  
👉 **Submodule Fallback**: `.human-ui/skills/human-flutter/SKILL.md`

---

## Core Execution Invariants

1. **Permission-First in Bengali (Highest Priority)**: Never make important architectural, state-management, routing, dependency, project-structure, database, or color decisions without explaining in Bengali, presenting options, recommending, and waiting for explicit user approval.
2. **Mandatory Project Structure**: All generated Flutter projects must enforce `lib/core/`, `lib/shared/`, and `lib/features/`.
3. **Mandatory 3–4 Color Selection**: Always request 3–4 HEX colors and display the 12-component visual color placement board preview before theme finalization.
4. **Absolute Flutter-Only**: Never switch to or recommend non-Flutter frameworks.

---

## Execution Instructions for Agent

1. Parse any subcommand passed to `/human-flutter` (or alias `/human-ui`):
   - `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
2. Follow the progressive disclosure protocol in [skills/human-flutter/SKILL.md](../../../skills/human-flutter/SKILL.md).
3. If installed as a Git submodule at `.human-ui/`, resolve references from `.human-ui/skills/human-flutter/`.
4. Follow the master instructions in [AGENTS.md](../../../AGENTS.md).
