# Windsurf Rules — Human UI Engineering

This repository uses the **Human UI Engineering** framework for all user interface development.

The authoritative source of truth for guidelines, workflows, and standards is [AGENTS.md](../../AGENTS.md).

## Instructions for Windsurf Cascade

1. **Follow the Master Workflow**: Execute tasks according to the 14-step sequence in [AGENTS.md](../../AGENTS.md#2-mandatory-14-step-engineering-workflow).
2. **Context First**: Always inspect project manifests (`package.json`, `pubspec.yaml`, etc.) and directory layouts before modifying code.
3. **Avoid AI Stereotypes**: Eschew arbitrary cyan/purple gradients, generic card layouts, and non-functional blur effects. Ground styling in [Human Design Rules](../../design/human-design-rules.md).
4. **Shared Components**: Leverage and expand modular primitives in `components/` before creating monolithic screen code.
5. **Rigorous Quality**: Validate against [UI Review](../../quality/ui-review.md) and [Performance Audit](../../quality/performance-audit.md).

## Quick Reference Index

- Master Instructions: [AGENTS.md](../../AGENTS.md)
- Core Architecture: [core/](../../core/)
- Design Tokens: [design/](../../design/)
- Shared Components: [components/](../../components/)
- Engineering Rules: [engineering/](../../engineering/)
- Framework Guides: [frameworks/](../../frameworks/)
- Quality Checklists: [quality/](../../quality/)
- Workflows: [workflows/](../../workflows/)
- Templates: [templates/](../../templates/)

> [!NOTE]
> Windsurf loads rules from `.windsurf/rules/`. For targeted domain instructions, read the corresponding chapter directly.
