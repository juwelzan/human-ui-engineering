# Agent Rules — Human Flutter Engineering

This workspace implements the **Human Flutter Engineering** system.

The single authoritative source of truth is [AGENTS.md](../../AGENTS.md).

## Absolute Flutter-Only Rule

This workspace is strictly and exclusively dedicated to Flutter and Dart engineering. The agent must **NEVER**:
- Switch to React, Next.js, Vue, Angular, or other web frontend frameworks.
- Use React Native or other non-Flutter cross-platform frameworks.
- Generate native Android Kotlin or iOS Swift application architectures as standalone alternatives.
- Recommend another framework when a Flutter/Dart solution is possible.
- Mix multiple framework architectures into a Flutter project.

Native Kotlin, Swift, platform channels (`MethodChannel`, `EventChannel`), FFI, and platform integrations are allowed ONLY when genuinely required to implement a Flutter application's platform functionality.

## Chat Slash Command: `/human-flutter` (or `/human-ui`)

When the user types `/human-flutter [subcommand] [task]` (or `/human-ui`):
- Recognize the command mode: `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
- Load the canonical skill engine in [skills/human-flutter/SKILL.md](../../skills/human-flutter/SKILL.md) and appropriate reference.
- If invoked with `/human-flutter recover`, execute the recovery sequence from [AI_TASK_STATE.md](../../AI_TASK_STATE.md).

## Core Directives for Autonomous Agents

1. **Mandatory 18-Step Workflow**: Always follow the sequence defined in [AGENTS.md](../../AGENTS.md).
2. **Project Inspection First**: Inspect `pubspec.yaml`, dependencies, and directory conventions before proposing code.
3. **Design Standard**: Human-centered design. Avoid AI tropes (neon glows, arbitrary gradients, uniform card fatigue). Prioritize hierarchy, spacing, typography, and contrast. Reference [Design Philosophy](../../design/design-philosophy.md).
4. **Foundation Precedence**: Construct or adapt shared UI primitives before constructing feature screens.
5. **Truthful Verification**: Execute `flutter test` and `dart analyze`. Report exact results honestly.

## Document Directory

- [Main Skill Engine](../../skills/human-flutter/SKILL.md)
- [Core Principles & Workflow](../../core/)
- [Design Tokens & Rules](../../design/)
- [Component Engineering](../../components/)
- [Engineering Standards](../../engineering/)
- [Quality Audits & Checklists](../../quality/)
- [Standard Workflows](../../workflows/)
- [Project Templates](../../templates/)

> [!NOTE]
> Agent environments load workspace rules from `.agents/rules/` or `.agent/rules/`. For chat invocation, use `/human-flutter [task]` or `/human-ui [task]`.
