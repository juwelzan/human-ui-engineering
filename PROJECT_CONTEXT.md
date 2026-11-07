# Project Context: Human Flutter Engineering

> **Complete Permission-First, Flutter-Only Human UI Engineering Operating System & AI Agent Intelligence**

- **Project Name**: Human Flutter Engineering
- **Repository**: `juwelzan/human-ui-engineering`
- **Domain**: Flutter & Dart AI Engineering Systems, Mobile/Desktop/Web UI Architecture & UI/UX Discipline
- **Target Audience**: AI coding agents (Google Antigravity, Gemini, Claude Code, Cursor, Copilot, Windsurf) & Human Flutter Engineers
- **Target Platforms**: Multi-platform via Flutter (Android, iOS, macOS, Windows, Linux, Flutter Web)
- **Primary Tech Stack**: Flutter SDK, Dart 3, Agent Skills Standard, Python validation suite

---

## 1. High-Level System Architecture

Human Flutter Engineering is a dedicated, Flutter-only AI software engineering system. It focuses exclusively on professional Flutter and Dart development, providing deep engineering intelligence across UI design, color harmony, reusable widget primitives, Dart coding standards, file structure, responsive layout, animations, performance, platform channels, and product lifecycle.

The single source of truth for all agent operations is [`AGENTS.md`](AGENTS.md). The canonical chat-box skill engine is [`skills/human-flutter/SKILL.md`](skills/human-flutter/SKILL.md), supported by lightweight adapters across all major agent environments.

---

## 2. Core Technical Invariants & Rules

1. **Permission-First in Bengali (Highest Priority)**: The agent must NEVER make important architectural, state-management, routing, dependency, project-structure, database, or color decisions without explaining the decision in natural Bengali, presenting options, recommending an approach, and obtaining explicit user permission.
2. **Absolute Flutter-Only Rule**: Flutter and Dart are the only supported application development framework. Never switch to or recommend alternative frameworks. Native code is allowed ONLY when platform channels or OS APIs require it.
3. **Mandatory 3-Tier Project Structure**: All generated Flutter codebases must enforce `lib/core/` (foundations), `lib/shared/` (reusable UI), and `lib/features/` (feature-first domain modules).
4. **Mandatory 3–4 Color Selection & Visual Preview**: Users choose 3–4 HEX colors, followed by a mandatory 12-component visual color placement board preview before theme finalization.
5. **18-Step Human Design-to-Code Workflow**: All non-trivial UI engineering follows the 18-step lifecycle from requirements and project inspection through responsive layout, state binding, performance profiling, and testing.
6. **Evidence-Based Engineering**: 5-tier evidence hierarchy; zero hallucination; honest reporting of test outcomes (`flutter test`, `dart analyze`).
7. **Autonomous Recovery**: Session interruptions are resumed via [`AI_TASK_STATE.md`](AI_TASK_STATE.md) and [`core/recovery-protocol.md`](core/recovery-protocol.md) without restarting completed work.
8. **Automated Validation**: All documentation files, internal relative links, and Flutter-only structural isolation must validate cleanly via `python3 scripts/validate.py`.

---

## 3. Directory Map & Package Boundaries

```text
human-ui-engineering/
├── AGENTS.md               # Master instructions (Single Source of Truth)
├── PROJECT_CONTEXT.md      # Stable system identity and invariants
├── AI_TASK_STATE.md        # Active task checkpoint and recovery state
├── CHANGELOG.md            # Release milestones
├── core/                   # Flutter engineering intelligence and orchestration
├── design/                 # Human-centered UI/UX design tokens, colors & typography
├── components/             # Reusable shared widget engineering primitives
├── engineering/            # Clean Dart code, security, async safety, performance
├── quality/                # Testing pyramid, a11y, regression prevention, quality gates
├── workflows/              # Step-by-step actionable Flutter execution cycles
├── templates/              # Fillable engineering templates (ADRs, task state, bug reports)
├── docs/                   # Guides, matrices, and docs/adr/ (Architecture Decision Records)
├── scripts/                # Automated validation suite (validate-docs, validate-links, etc.)
└── skills/human-flutter/   # Canonical Agent Skills engine (28 reference modules)
```

---

## 4. Key Agent Slash Commands

- `/human-flutter` (or alias `/human-ui`) — General Flutter feature implementation
- `/human-flutter plan` — Structured task planning, Bengali permission gates, and risk analysis
- `/human-flutter build` — End-to-end full-stack Flutter feature development
- `/human-flutter design` — UI/UX design system and token specification
- `/human-flutter color` — 3-4 color prompt, visual placement preview, and ThemeData
- `/human-flutter component` — Reusable widget primitive engineering in `shared/`
- `/human-flutter responsive` — Multi-breakpoint layouts (Mobile, Tablet, Desktop, Web)
- `/human-flutter animation` — 60/120fps animations and micro-interactions
- `/human-flutter performance` — Frame budget, rebuild reduction, and DevTools
- `/human-flutter platform` — MethodChannel, EventChannel, FFI, and permissions
- `/human-flutter product` — Auth, offline storage, Firebase, and payments
- `/human-flutter audit` — Visual, accessibility, and performance review
- `/human-flutter debug` — Scientific 10-step root-cause diagnosis (RenderFlex, leaks)
- `/human-flutter refactor` — Safe widget extraction and state decoupling
- `/human-flutter test` — Multi-tier test authoring and verification
- `/human-flutter review` — Pre-flight pull request review against 13 quality gates
- `/human-flutter release` — Production AAB/IPA build and release preparation
- `/human-flutter recover` — Restore active context from `AI_TASK_STATE.md` and git telemetry
- `/human-flutter status` — Output active task progress, milestones, and blockers
