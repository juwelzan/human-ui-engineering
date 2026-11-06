---
name: human-ui
description: Execute a production-grade software engineering task using Human UI Engineering standards.
argument-hint: "[mode?] [task or instruction]"
---

You are executing a task using the **Human UI Engineering** framework.

Task request:
${input}

## Mandatory Execution Instructions

1. **Canonical Skill**: Consult [skills/human-ui/SKILL.md](../../skills/human-ui/SKILL.md) for the active command mode and progressive reference loading.
2. **Framework Detection**: Inspect project manifests (`package.json`, `pubspec.yaml`, `build.gradle.kts`, `Package.swift`, `go.mod`, `Cargo.toml`) to adapt to existing frameworks and conventions.
3. **Master Workflow**: Adhere to the master engineering workflow defined in [AGENTS.md](../../AGENTS.md).
4. **No AI Tropes**: Avoid arbitrary neon glows, gradients, and card fatigue. Ground styling in [Human Design Rules](../../design/human-design-rules.md).
5. **Recovery & Status Protocol**: If the prompt requests recovery or status, consult [skills/human-ui/references/recovery.md](../../skills/human-ui/references/recovery.md) or [skills/human-ui/references/status.md](../../skills/human-ui/references/status.md).
