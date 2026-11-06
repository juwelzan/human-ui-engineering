# Changelog

All notable changes to the **Human UI Engineering** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-11-06

### Major Architectural Upgrade: Universal, Parallel, Self-Maintaining AI Engineering System

#### Added
- **Universal Core Architecture**:
  - `core/anti-hallucination.md`: Non-negotiable evidence-based engineering rules preventing AI agents from inventing non-existent packages, APIs, configuration flags, or test results.
  - `core/recovery-protocol.md`: 6-step autonomous recovery sequence for agents encountering failures without abandoning tasks or wiping progress.
  - `core/checkpoint-management.md`: Standardized state tracking via `AI_TASK_STATE.md` enabling agents to resume multi-turn work.
  - `core/change-control.md`: Safe refactoring standards, blast-radius assessment, and backward-compatible component API evolution.
  - `core/engineering-workflow.md`: Universal 6-stage engineering lifecycle applying across all programming languages and frameworks.
- **Parallel Framework Modules**:
  - `frameworks/README.md`: Master framework isolation rules preventing implementation cross-contamination.
  - `frameworks/vue.md`: Modern Vue 3 with Composition API, `<script setup lang="ts">`, Pinia, and Nuxt.
  - `frameworks/angular.md`: Modern Angular 17+ with Standalone Components, Signals, and `@if`/`@for` control flow.
  - `frameworks/react-native.md`: Cross-platform mobile engineering with Expo, Fabric, and TurboModules.
  - `frameworks/desktop.md`: Desktop engineering across Electron, Tauri, and Flutter Desktop.
  - Updated `frameworks/framework-selection.md` with complete 10-framework decision tree and matrix.
- **Advanced UI & Engineering Systems**:
  - `design/human-interface-design.md`: Information architecture, Miller's Law chunking, Hick's Law, Fitts's Law, visual rhythm.
  - `engineering/security.md`: XSS prevention, Content Security Policy, token hygiene, safe IPC bridges.
  - `engineering/async-operations.md`: Request cancellation via `AbortController`, race condition guards, debouncing vs. throttling.
  - `components/component-principles.md`: Component boundaries, composition over prop explosion, 7-state interactive matrix.
  - `components/forms.md`: Comprehensive form control engineering, validation timing, and multi-step wizards.
  - `components/component-testing.md`: 5-stage component test suite across React, Flutter, and Compose.
- **Quality & Workflows Expansion**:
  - `quality/accessibility-audit.md`: Formal WCAG 2.1 AA audit checklist across visual, keyboard, screen reader, and motor criteria.
  - `quality/regression-prevention.md`: 4-dimension regression prevention protocol.
  - `workflows/project-discovery.md`: Evidence-based codebase mapping and monorepo isolation.
  - `workflows/new-feature.md`: Multi-screen feature execution workflow.
  - `workflows/debugging.md`: Scientific 6-stage defect isolation and repair loop.
  - `workflows/recovery.md`: Step-by-step task recovery procedure.
  - `workflows/refactoring.md`: Gated refactoring workflow.
  - `workflows/performance-optimization.md`: Profiling and quantitative metric reporting.
- **Templates & Tooling**:
  - `templates/task-state.md`: Fillable template for `AI_TASK_STATE.md`.
  - `templates/bug-report.md`: Defect documentation and root cause analysis template.
  - `scripts/validate-docs`: Automated documentation existence and content validator.
  - `scripts/validate-links`: Automated relative markdown link checker.
  - `scripts/validate-structure`: Automated framework isolation and agent entry point validator.
  - Updated `scripts/validate.py` to run full 83+ file and link verification.

---

## [1.1.0] - 2026-11-06

### Chat-Box Slash Command Skill Integration (`/human-ui`)

#### Added
- `skills/human-ui/SKILL.md`: Main Agent Skill engine supporting 10 task modes (`design`, `audit`, `flutter`, `react`, `responsive`, `performance`, `debug`, `recover`, `review`).
- `skills/human-ui/references/`: 14 progressive disclosure references preventing context window saturation.
- Lightweight agent adapters for Google Antigravity, Claude Code, VS Code GitHub Copilot, Cursor, and Windsurf.
- `docs/compatibility-matrix.md`: Verified compatibility matrix across 8 major AI coding environments.
- `docs/slash-command-guide.md`: Comprehensive chat command manual.
- `docs/installation-guide.md`: Installation instructions for submodules, global skills, and manual configurations.
- `.github/workflows/validate.yml`: Continuous Integration workflow on GitHub Actions.

---

## [1.0.0] - 2026-11-06

### Initial Release

#### Added
- Universal Human UI Engineering context repository.
- Master 14-Step Engineering Workflow in `AGENTS.md`.
- Foundational guidelines in `core/`, `design/`, `components/`, `engineering/`, `frameworks/`, `quality/`, `workflows/`, `templates/`.
- Lightweight entry points: `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/human-ui.mdc`, `.agent/rules/human-ui.md`, `.windsurf/rules/human-ui.md`.

