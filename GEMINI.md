# Gemini Agent Instructions — Human Flutter Engineering

This repository implements the **Human Flutter Engineering** system for high-fidelity, human-grade Flutter & Dart UI engineering.

The authoritative single source of truth is [AGENTS.md](AGENTS.md).

## Absolute Flutter-Only Rule

Flutter and Dart are the only supported application development framework. Never switch to or recommend alternative frameworks.

## Chat Slash Command: `/human-flutter` (or `/human-ui`)

Gemini CLI and Antigravity discover skills in `.agents/skills/human-flutter/SKILL.md`, `.agent/skills/human-flutter/SKILL.md`, or canonical `skills/human-flutter/SKILL.md`.
- **Command Syntax**: `/human-flutter [subcommand] [task]` (or `/human-ui [subcommand] [task]`)
- **Subcommands**: `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
- **Recovery Mode**: `/human-flutter recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-flutter/SKILL.md](skills/human-flutter/SKILL.md).

## Operational Rules for Gemini

- **Mandatory 18-Step Workflow**: Follow the engineering process in [AGENTS.md](AGENTS.md).
- **Discovery**: Thoroughly inspect `pubspec.yaml`, project structure, design tokens, and state management conventions before proposing code.
- **Pragmatic Design**: Emulate senior human UI engineers. Reject cliché AI styling (e.g., purple/cyan glows, uniform cards, purposeless glassmorphism). Ground decisions in [Human Design Rules](design/human-design-rules.md).
- **Modularity & Reusability**: Ensure shared primitives in [components/](components/) are utilized and maintained with `const` support.
- **Verification**: Run `flutter test` and `dart analyze`, and verify contrast and accessibility before claiming completion.

## Documentation Index

- **Main Skill Engine**: [skills/human-flutter/](skills/human-flutter/SKILL.md)
- **Core Guidelines**: [core/](core/)
- **Design Specifications**: [design/](design/)
- **Component Patterns**: [components/](components/)
- **Engineering Standards**: [engineering/](engineering/)
- **Quality & Checklists**: [quality/](quality/)
- **Execution Workflows**: [workflows/](workflows/)
- **Templates**: [templates/](templates/)

> [!NOTE]
> Automatic rule loading varies depending on the Gemini harness (CLI, Antigravity, or API integration). Always verify that [AGENTS.md](AGENTS.md) is active in context.
