# GitHub Copilot Instructions — Human UI Engineering

This repository uses the **Human UI Engineering** standard.

All AI-assisted development must conform to the master instructions in [AGENTS.md](../AGENTS.md).

## Copilot Prompt & Command: `/human-ui`

GitHub Copilot in VS Code supports reusable prompts via `.github/prompts/human-ui.prompt.md`.
- **Chat Invocation**: Type `/human-ui [subcommand] [task]` or reference `#prompt:human-ui`.
- **Subcommands**: `design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`.
- **Recovery Mode**: `/human-ui recover` restores context from `AI_TASK_STATE.md` and git telemetry.
- **Skill Engine**: [skills/human-ui/SKILL.md](../skills/human-ui/SKILL.md).

## Core Directives for GitHub Copilot

1. **Follow the Master Workflow**: Refer to the 14-step engineering process in [AGENTS.md](../AGENTS.md#2-mandatory-14-step-engineering-workflow).
2. **Respect Existing Codebases**: Inspect conventions, directory layouts, and state patterns prior to generating components.
3. **Avoid Generic AI Visuals**: Prioritize functional hierarchy, accessibility, and clean typography over decorative gradients, arbitrary glows, or redundant card containers.
4. **Shared Components**: Consult [components/](../components/) before creating ad-hoc widgets or elements.
5. **Quality Standard**: Verify code against [UI Review](../quality/ui-review.md) and [Testing Guide](../quality/testing.md).

## Quick Reference Links

- Main Skill Engine: [skills/human-ui/](../skills/human-ui/SKILL.md)
- Core Methodology: [core/](../core/)
- Design Tokens & Systems: [design/](../design/)
- Shared Component Specs: [components/](../components/)
- Engineering Standards: [engineering/](../engineering/)
- Framework-Specific Guides: [frameworks/](../frameworks/)
- Quality Audits: [quality/](../quality/)

> [!NOTE]
> Copilot auto-loads repository instructions located at `.github/copilot-instructions.md`.
