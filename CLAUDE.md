# Claude Code Instructions — Human Flutter Engineering

This project adheres to the **Human Flutter Engineering** system.

The single source of truth for all Flutter engineering tasks, architectural patterns, design standards, and workflows is located in [AGENTS.md](AGENTS.md).

## Chat Slash Command: `/human-flutter` (or `/human-ui`)

Claude Code recognizes custom slash commands in `.claude/commands/human-flutter.md`.
- **Invocation**: `/human-flutter [subcommand] [task]`
- **Subcommands**: `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
- **Recovery Mode**: `/human-flutter recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-flutter/SKILL.md](skills/human-flutter/SKILL.md).

## Quick Guidance for Claude Code

1. **Absolute Flutter-Only Rule**: Flutter and Dart are the only supported application development framework. Never switch to or recommend alternative frameworks.
2. **Master 18-Step Workflow**: Always follow the workflow defined in [AGENTS.md](AGENTS.md).
3. **Context Discovery**: Read `pubspec.yaml`, dependencies, and code conventions before generating code.
4. **No Synthetic AI Patterns**: Avoid gratuitous neon glows, excessive gradients, arbitrary frosted glass, and repetitive card layouts. Refer to [Design Philosophy](design/design-philosophy.md).
5. **Foundation First**: Build design tokens and shared components before assembling complex views.
6. **Quality Verification**: Execute `flutter test` and `dart analyze` before marking tasks complete.

## Reference Index

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
