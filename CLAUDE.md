# Claude Code Instructions — Human Flutter Engineering

This project adheres to the **Human Flutter Engineering** system.

The single source of truth for all Flutter engineering tasks, architectural patterns, design standards, and workflows is located in [AGENTS.md](AGENTS.md).

---

## 1. Permission-First Decision System in Bengali (Highest Priority)

Claude Code must **NEVER** make important architectural, state-management, routing, dependency, project-structure, database, or color decisions without first explaining the decision in Bengali, presenting options, stating pros and cons, recommending an approach, and obtaining explicit user permission.

👉 **Permission Reference**: [skills/human-flutter/references/permission-system.md](skills/human-flutter/references/permission-system.md)

---

## 2. Absolute Flutter-Only Rule

Flutter and Dart are the only supported application development framework. Never switch to or recommend alternative frameworks.

---

## 3. Mandatory Flutter Project Structure

All generated Flutter projects must strictly enforce:
- `lib/core/` — Global foundational infrastructure (config, network, routing, storage, theme tokens). Zero feature UI.
- `lib/shared/` — Reusable widgets, custom painters, animations, and responsive layouts.
- `lib/features/` — Feature-first domain modules (`data/`, `domain/`, `presentation/`).

👉 **Project Structure**: [skills/human-flutter/references/project-structure.md](skills/human-flutter/references/project-structure.md)

---

## 4. Mandatory Color Selection & Visual Placement Preview

Before finalizing theme code:
1. Ask the user in Bengali to choose 3 or 4 HEX colors.
2. Present a visual UI color placement board across the 12 core components.
3. Obtain explicit user approval before writing `ThemeData` and `ColorScheme`.

👉 **Visual Preview**: [skills/human-flutter/references/color-preview.md](skills/human-flutter/references/color-preview.md)

---

## 5. Chat Slash Command: `/human-flutter` (or `/human-ui`)

Claude Code recognizes custom slash commands in `.claude/commands/human-flutter.md`.
- **Invocation**: `/human-flutter [subcommand] [task]`
- **Subcommands**: `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
- **Recovery Mode**: `/human-flutter recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-flutter/SKILL.md](skills/human-flutter/SKILL.md).

---

## 6. Reference Index

- Main Skill Engine: [skills/human-flutter/](skills/human-flutter/SKILL.md)
- Core Workflow & Architecture: [core/](core/)
- Design Tokens & Systems: [design/](design/)
- Shared Component Specs: [components/](components/)
- Engineering & Performance: [engineering/](engineering/)
- Quality & Audits: [quality/](quality/)
- Execution Workflows: [workflows/](workflows/)
- Fillable Templates: [templates/](templates/)

> [!NOTE]
> Claude Code automatically registers slash commands from `.claude/commands/`.
