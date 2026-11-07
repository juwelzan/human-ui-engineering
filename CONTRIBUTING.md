# Contributing to Human Flutter Engineering

Thank you for your interest in contributing to **Human Flutter Engineering**! This project provides a complete Flutter-only context and instruction system for AI coding agents and human engineers building production-grade user interfaces.

---

## 1. Principles of Contribution

When proposing modifications, additions, or enhancements, adhere strictly to these guidelines:

1. **Absolute Flutter-Only Focus**: This repository is strictly and exclusively dedicated to Flutter and Dart. Contributions proposing or integrating React, Next.js, Vue, Angular, React Native, or alternative non-Flutter frameworks are rejected by design. Native code (Kotlin/Swift) is permitted ONLY when platform channels or OS hardware APIs genuinely require it.
2. **Human Practicality Over Pure Theory**: Every rule, pattern, or recommendation must be tested against real-world Flutter production engineering. Avoid excessive abstraction or pedantic dogma.
3. **Single Source of Truth**: Keep [`AGENTS.md`](AGENTS.md) as the authoritative master workflow. Avoid duplicating full chapters in agent-specific entry files.
4. **Relative Markdown Links**: Use relative links for all internal references so that documentation works offline, inside IDE sidecars, and across git submodules.
5. **No AI Cliché Prescriptions**: Do not suggest or mandate generic "AI aesthetic" defaults (e.g. indiscriminate neon borders, arbitrary glassmorphism, decorative cards). Design rules must advocate for intentional, content-first visual hierarchy.

---

## 2. Repository Structure

```text
human-ui-engineering/
├── AGENTS.md               # Master instructions (Single Source of Truth)
├── CLAUDE.md               # Claude Code entry point
├── GEMINI.md               # Gemini / Antigravity entry point
├── skills/human-flutter/   # Canonical Agent Skill Engine (/human-flutter)
├── docs/                   # Guides, matrices, and manuals
├── .github/                # GitHub-specific instructions & prompts
├── .cursor/                # Cursor rule definitions & skills
├── .agents/                # Canonical Antigravity workspace skills & rules
├── .agent/                 # Fallback Antigravity rule definitions & skills
├── .claude/commands/       # Claude Code custom commands
├── .windsurf/              # Windsurf rules & workflows
├── core/                   # Agent behavior, discovery, architecture, workflow
├── design/                 # Design philosophy, tokens, typography, colors, a11y
├── components/             # Reusable UI component specifications
├── engineering/            # Clean Dart code, state, memory, performance, error handling
├── quality/                # Testing, UI reviews, performance audits, release checklists
├── workflows/              # Step-by-step action workflows
├── templates/              # Reusable project, design, architecture, QA templates
└── scripts/validate.py     # Automated repository integrity & link validator
```

---

## 3. How to Submit Changes

1. **Fork and Branch**: Create a descriptive feature branch from `main` (e.g., `git checkout -b docs/add-drift-sync-guide` or `fix/improve-contrast-rules`).
2. **Run Local Validation**:
   Before committing, run the master repository validator:
   ```bash
   python3 scripts/validate.py
   ```
   All links, file structures, and Flutter-only isolation checks must pass with 0 errors.
3. **Open a Pull Request**: Provide a clear description of the enhancement, verified tests, and updated documentation.
