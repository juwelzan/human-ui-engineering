# Project Context: Human UI Engineering

> **Universal AI Agent Context & Instruction System for Professional Software Engineering**

- **Project Name**: Human UI Engineering
- **Repository**: `juwelzan/human-ui-engineering`
- **Domain**: AI Agent Engineering Systems, Software Architecture & UI/UX Discipline
- **Target Audience**: AI coding agents (Google Antigravity, Claude Code, Cursor, Copilot, Windsurf, Gemini) & Human Software Engineers
- **Target Platforms**: Multi-platform (Web, Mobile, Desktop, Cloud Backend)
- **Primary Tech Stack**: Markdown knowledge architecture, Agent Skills Standard, Python validation suite

---

## 1. High-Level System Architecture

Human UI Engineering is a universal, framework-agnostic AI software engineering operating system. It decouples high-level software engineering fundamentals (in `core/`, `design/`, `engineering/`, `quality/`) from strictly isolated, framework-specific implementation guides (in `frameworks/`).

The single source of truth for all agent operations is [`AGENTS.md`](AGENTS.md). The canonical chat-box skill engine is [`skills/human-ui/SKILL.md`](skills/human-ui/SKILL.md), supported by lightweight adapters across all major agent environments.

---

## 2. Core Technical Invariants & Rules

- **Universal Core Decoupling**: Universal modules must never assume a single framework (e.g., never mandate React hooks or Flutter widgets inside `core/`).
- **Framework Isolation**: Each framework module in `frameworks/` is completely self-contained. A framework module never imposes rules on another.
- **Evidence-Based Engineering**: 5-tier evidence hierarchy; zero hallucination; honest reporting of test outcomes (PASSED, FAILED, SKIPPED, BLOCKED, NOT APPLICABLE).
- **Autonomous Recovery**: Session interruptions are resumed via [`AI_TASK_STATE.md`](AI_TASK_STATE.md) and [`core/recovery-protocol.md`](core/recovery-protocol.md) without restarting completed work.
- **Automated Validation**: All markdown files and internal relative links must validate cleanly via `python3 scripts/validate.py`.

---

## 3. Directory Map & Package Boundaries

```text
human-ui-engineering/
├── AGENTS.md               # Master instructions (Single Source of Truth)
├── PROJECT_CONTEXT.md      # Stable system identity and invariants
├── AI_TASK_STATE.md        # Active task checkpoint and recovery state
├── CHANGELOG.md            # Release milestones
├── core/                   # Universal engineering intelligence and orchestration
├── design/                 # Human-centered UI/UX design tokens and laws
├── components/             # Reusable shared component engineering primitives
├── engineering/            # Clean code, security, async safety, performance
├── frameworks/             # 13 isolated framework modules (Web, Mobile, Desktop, Backend, DB)
├── quality/                # Testing, a11y, regression prevention, quality gates
├── workflows/              # Step-by-step actionable execution cycles
├── templates/              # Fillable engineering templates (ADRs, task state, bug reports)
├── docs/                   # Guides, matrices, and docs/adr/ (Architecture Decision Records)
├── scripts/                # Automated validation suite (validate-docs, validate-links, etc.)
└── skills/human-ui/        # Canonical Agent Skills engine
```

---

## 4. Key Agent Slash Commands

- `/human-ui` — General feature implementation
- `/human-ui plan` — Structured task planning and risk analysis
- `/human-ui build` — End-to-end full stack development
- `/human-ui design` — UI/UX design system and token specification
- `/human-ui architect` — System architecture design and ADR authoring
- `/human-ui audit` — Code, performance, security, and accessibility review
- `/human-ui debug` — Scientific 10-step root-cause diagnosis and repair
- `/human-ui refactor` — Safe, behavior-preserving refactoring
- `/human-ui test` — Multi-tier test authoring and verification
- `/human-ui review` — PR review against pre-flight release checklist
- `/human-ui security` — Threat analysis, input sanitization, and auth review
- `/human-ui performance` — Profiling, frame budget, and memory leak analysis
- `/human-ui docs` — Documentation and API contract generation
- `/human-ui release` — Pre-flight release checks and migration plans
- `/human-ui recover` — Context restoration from `AI_TASK_STATE.md`
- `/human-ui status` — Report active task milestone and progress

---

## 5. Verification Commands

```bash
# Run full automated validation suite (docs, links, structure)
python3 scripts/validate.py
```
