# Claude Code Instructions — Human UI Engineering

This project adheres to the **Human UI Engineering** standard.

The single source of truth for all UI engineering tasks, architectural patterns, design standards, and workflows is located in [AGENTS.md](AGENTS.md).

## Chat Slash Command: `/human-ui`

Claude Code recognizes custom slash commands in `.claude/commands/human-ui.md`.
- **Invocation**: `/human-ui [subcommand] [task]`
- **Subcommands**: `design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`.
- **Recovery Mode**: `/human-ui recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-ui/SKILL.md](skills/human-ui/SKILL.md).

## Quick Guidance for Claude Code

1. **Master Workflow**: Always follow the 14-step workflow defined in [AGENTS.md](AGENTS.md#2-mandatory-14-step-engineering-workflow).
2. **Context Discovery**: Read existing project configuration and code conventions before generating code.
3. **No Synthetic AI Patterns**: Avoid gratuitous neon glows, excessive gradients, arbitrary frosted glass, and repetitive card layouts. Refer to [Design Philosophy](design/design-philosophy.md).
4. **Foundation First**: Build design tokens and shared components before assembling complex views.
5. **Quality Verification**: Execute actual tests and audits before marking tasks complete. Consult [UI Review](quality/ui-review.md) and [Performance Audit](quality/performance-audit.md).

## Reference Index

- Main Skill Engine: [skills/human-ui/](skills/human-ui/SKILL.md)
- Core Workflow & Architecture: [core/](core/)
- Design Tokens & Systems: [design/](design/)
- Shared Component Specs: [components/](components/)
- Engineering & Performance: [engineering/](engineering/)
- Framework Guides: [frameworks/](frameworks/)
- Quality & Audits: [quality/](quality/)
- Execution Workflows: [workflows/](workflows/)
- Fillable Templates: [templates/](templates/)

> [!NOTE]
> Claude Code automatically registers slash commands from `.claude/commands/`.
