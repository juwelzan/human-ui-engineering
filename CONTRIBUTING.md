# Contributing to Human UI Engineering

Thank you for your interest in contributing to **Human UI Engineering**! This project provides a universal context and instruction system for AI coding agents and human engineers building production-grade user interfaces.

---

## 1. Principles of Contribution

When proposing modifications, additions, or enhancements, adhere to these guidelines:

1. **Framework Neutrality in Core**: Core standards, design principles, component guidelines, and quality checklists must remain framework-neutral. Framework-specific nuances belong exclusively in [`frameworks/`](frameworks/).
2. **Human Practicality Over Pure Theory**: Every rule, pattern, or recommendation must be tested against real-world production engineering realities. Avoid excessive abstraction or pedantic dogma.
3. **Single Source of Truth**: Keep [`AGENTS.md`](AGENTS.md) as the authoritative master workflow. Avoid duplicating full chapters in agent-specific entry files.
4. **Relative Markdown Links**: Use relative links for all internal references so that documentation works offline, inside IDE sidecars, and across git branches.
5. **No AI Cliché Prescriptions**: Do not suggest or mandate generic "AI aesthetic" defaults (e.g. indiscriminate neon borders, arbitrary glassmorphism, decorative cards). Design rules must advocate for intentional, content-first visual hierarchy.

---

## 2. Repository Structure

```text
human-ui-engineering/
├── AGENTS.md               # Master instructions (Single Source of Truth)
├── CLAUDE.md               # Claude Code entry point
├── GEMINI.md               # Gemini / Antigravity entry point
├── .github/                # GitHub-specific instructions (Copilot)
├── .cursor/rules/          # Cursor rule definitions
├── .agent/rules/           # Antigravity / Agent rule definitions
├── .windsurf/rules/        # Windsurf rule definitions
├── core/                   # Agent behavior, discovery, architecture, workflow
├── design/                 # Design philosophy, tokens, typography, colors, a11y
├── components/             # Reusable UI component specifications
├── engineering/            # Clean code, state, memory, performance, error handling
├── frameworks/             # Practical guides (Flutter, React, Next.js, Android, iOS, Web)
├── quality/                # Testing, UI reviews, performance audits, release checklists
├── workflows/              # Step-by-step action workflows
└── templates/              # Reusable project, design, architecture, QA templates
```

---

## 3. How to Submit Changes

1. **Fork and Branch**: Create a descriptive feature branch from `main` (e.g., `git checkout -b docs/add-svelte-guide` or `fix/improve-contrast-rules`).
2. **Validate Links & Consistency**:
   - Ensure all relative links resolve correctly.
   - Verify that new files are cross-referenced in `AGENTS.md`, `README.md`, and the relevant category indexes.
   - Check spelling, grammar, and markdown formatting.
3. **Commit Guidelines**:
   - Use conventional commit messages:
     - `feat: ...` for new guides, templates, or agent configurations.
     - `fix: ...` for correcting broken links, typos, or inaccurate technical advice.
     - `docs: ...` for documentation refinements.
4. **Open a Pull Request**: Provide a clear explanation of what was added or improved and why it benefits AI agents or human engineers.

---

## 4. Code of Conduct

Maintain an inclusive, welcoming, and professional environment. Treat all contributors and reviewers with respect and constructive feedback.

