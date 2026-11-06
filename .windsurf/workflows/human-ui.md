---
name: human-ui
description: Execute a production-grade software engineering task using Human UI Engineering standards.
argument-hint: "[mode?] [task or instruction]"
---

# Human UI Engineering (Windsurf Cascade Workflow)

This workflow is triggered when `/human-ui` is invoked in Windsurf Cascade.

👉 **Canonical Skill**: [skills/human-ui/SKILL.md](../../skills/human-ui/SKILL.md)

## Execution Protocol

1. **Parse Arguments**:
   - Inspect whether a subcommand was specified (`plan`, `build`, `design`, `architect`, `audit`, `debug`, `refactor`, `test`, `review`, `security`, `performance`, `docs`, `release`, `recover`, `status`).
   - If `recover`, immediately inspect `AI_TASK_STATE.md`, git diff, and run [skills/human-ui/references/recovery.md](../../skills/human-ui/references/recovery.md).
2. **Context Discovery**:
   - Identify active framework (`pubspec.yaml`, `package.json`, `build.gradle.kts`, `Package.swift`, `go.mod`, `Cargo.toml`).
   - Read ONLY the target framework reference from `skills/human-ui/references/`.
3. **Execute & Verify**:
   - Execute the requested task mode following [AGENTS.md](../../AGENTS.md).
   - Validate with automated tests or lint checks before completion.
