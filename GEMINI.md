# Gemini Agent Instructions — Human UI Engineering

This repository implements the **Human UI Engineering** framework for high-fidelity, human-grade user interface engineering.

The authoritative single source of truth is [AGENTS.md](AGENTS.md).

## Chat Slash Command: `/human-ui`

Gemini CLI and Antigravity discover skills in `skills/human-ui/SKILL.md` or `.agent/skills/human-ui/SKILL.md`.
- **Command Syntax**: `/human-ui [subcommand] [task]`
- **Subcommands**: `design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`.
- **Recovery Mode**: `/human-ui recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-ui/SKILL.md](skills/human-ui/SKILL.md).

## Operational Rules for Gemini

- **Mandatory Workflow**: Follow the 14-step engineering process in [AGENTS.md](AGENTS.md#2-mandatory-14-step-engineering-workflow).
- **Discovery**: Thoroughly inspect manifests, project structure, design tokens, and state management conventions before proposing code.
- **Pragmatic Design**: Emulate senior human UI engineers. Reject cliché AI styling (e.g., purple/cyan glows, uniform cards, purposeless glassmorphism). Ground decisions in [Human Design Rules](design/human-design-rules.md).
- **Modularity & Reusability**: Ensure shared primitives in [components/](components/) are utilized and maintained without creating leaky abstractions.
- **Verification**: Run tests, static analysis, and verify contrast and accessibility before claiming completion.

## Documentation Index

- **Main Skill Engine**: [skills/human-ui/](skills/human-ui/SKILL.md)
- **Core Guidelines**: [core/](core/)
- **Design Specifications**: [design/](design/)
- **Component Patterns**: [components/](components/)
- **Engineering Standards**: [engineering/](engineering/)
- **Framework Guides**: [frameworks/](frameworks/)
- **Quality & Checklists**: [quality/](quality/)
- **Execution Workflows**: [workflows/](workflows/)
- **Templates**: [templates/](templates/)

> [!NOTE]
> Automatic rule loading varies depending on the Gemini harness (CLI, Antigravity, or API integration). Always verify that [AGENTS.md](AGENTS.md) is active in context.
