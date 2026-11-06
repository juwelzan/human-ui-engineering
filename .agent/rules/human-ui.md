# Agent Rules — Human UI Engineering

This workspace implements the **Human UI Engineering** standard.

The single authoritative source of truth is [AGENTS.md](../../AGENTS.md).

## Core Directives for Autonomous Agents

1. **Mandatory 14-Step Workflow**: Always follow the sequence defined in [AGENTS.md](../../AGENTS.md#2-mandatory-14-step-engineering-workflow).
2. **Phase 1 Inspection**: Inspect existing manifests, directories, dependencies, and formatting configurations before proposing alterations.
3. **Design Standard**: Adopt a human-centered design approach. Avoid AI tropes (gratuitous glow, arbitrary gradients, uniform cards). Prioritize hierarchy, spacing, typography, and contrast. Reference [Design Philosophy](../../design/design-philosophy.md).
4. **Foundation Precedence**: Construct or adapt shared UI primitives before constructing feature pages.
5. **Truthful Verification**: Execute automated tests, static checks, and accessibility evaluations. Explicitly distinguish between verified tests and unverified assertions.

## Document Directory

- [Core Principles & Workflow](../../core/)
- [Design Tokens & Rules](../../design/)
- [Component Engineering](../../components/)
- [Engineering Standards](../../engineering/)
- [Framework Guides](../../frameworks/)
- [Quality Audits & Checklists](../../quality/)
- [Standard Workflows](../../workflows/)
- [Project Templates](../../templates/)

> [!NOTE]
> Agent environments load workspace rules from `.agent/rules/`. For deep-dive tasks, reference the specific guide within the corresponding category directory.
