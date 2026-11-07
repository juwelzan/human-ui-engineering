# Changelog

All notable changes to the **Human UI Engineering** repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [4.2.0] - 2026-11-07

### Milestone: Complete Foreign Code Cleansing, Decision Memory & Core Engineering Infrastructure

#### Added & Enhanced
- **Decision Memory System (`DECISION_MEMORY.md`)**:
  - Implemented persistent decision memory register with 5 explicit tiers: Approved Decisions, Rejected Decisions, Pending Decisions, Project-Specific Choices, and Global User Preferences.
  - Added dedicated reference: [`skills/human-flutter/references/decision-memory.md`](skills/human-flutter/references/decision-memory.md).
  - Added project template: [`templates/decision-memory.md`](templates/decision-memory.md).
  - Eliminates redundant questioning: once an architectural or color choice is approved in Bengali, the agent autonomously executes it without re-asking.
- **Core Engineering Architecture (`lib/core/`)**:
  - Added dedicated reference: [`skills/human-flutter/references/core-engineering.md`](skills/human-flutter/references/core-engineering.md) covering foundational infrastructure with zero feature UI dependencies.
  - Provided production-ready Dart 3 implementations:
    - Dio HTTP client with SSL pinning, auth token refreshing, and exponential retry backoff.
    - Functional error handling with `Result<T, Failure>` pattern using Dart 3 sealed classes.
    - Secure storage service wrapping `flutter_secure_storage` with hardware-backed encryption.
    - Centralized spacing, radius, and `BuildContext` theme extensions.
- **Complete Foreign Code Cleansing (100% Absolute Flutter-Only)**:
  - Systematically purged all remaining non-Flutter code snippets, types, and package managers across 33 files in `core/`, `components/`, `engineering/`, `quality/`, `workflows/`, and `templates/`.
  - Replaced legacy TSX/JSX, `AbortController`, React hooks, and npm references with Flutter equivalents (`Dio CancelToken`, `StreamSubscription`, `State.dispose()`, `WidgetTester`, `pubspec.yaml`).
- **Automated Anti-Regression Validation Hardening**:
  - Enhanced `scripts/validate-flutter-only` with automated document scanning to reject foreign framework code blocks (```tsx, ```jsx) and `package.json` references.
  - Updated `scripts/validate-docs` and `scripts/validate-structure` to verify 150 documentation files and 36 reference guides.
  - Master validation suite passes with 0 errors and 100% link integrity (773/773).

---

## [4.1.0] - 2026-11-07

### Master Upgrade: Permission-First Bengali Decision System & Mandatory 3-Tier Architecture

#### Added & Mandated
- **Permission-First Bengali Decision System (Highest Priority)**:
  - Enforced mandatory 7-step Bengali decision protocol before executing any major architectural, state management, routing, dependency, project structure, database, or color decisions.
  - Added dedicated reference: [`skills/human-flutter/references/permission-system.md`](skills/human-flutter/references/permission-system.md).
  - Codified strict non-assumption rules: silence or vague replies are never treated as consent.
- **Mandatory 3-Tier Flutter Project Architecture**:
  - Enforced `lib/core/` (foundational infrastructure, config, network, storage, theme tokens with zero feature UI), `lib/shared/` (cross-feature reusable widgets, custom painters, animations, and responsive layouts), and `lib/features/` (feature-first domain packages).
  - Added dedicated reference: [`skills/human-flutter/references/project-structure.md`](skills/human-flutter/references/project-structure.md).
  - Added shared components reference: [`skills/human-flutter/references/shared-components.md`](skills/human-flutter/references/shared-components.md).
  - Added feature engineering reference: [`skills/human-flutter/references/feature-engineering.md`](skills/human-flutter/references/feature-engineering.md).
- **Mandatory 3–4 Color Selection & Visual Color Placement Preview Board**:
  - Users explicitly choose 3 or 4 primary colors (HEX) via Bengali prompt.
  - Added mandatory 12-component visual UI color board preview (App background, App bar, Navigation bar, Primary/Secondary buttons, Cards, Inputs, Typography, Icons, Borders, Selection states, Status semantics) before theme finalization.
  - Added dedicated references: [`skills/human-flutter/references/color-intelligence.md`](skills/human-flutter/references/color-intelligence.md) and [`skills/human-flutter/references/color-preview.md`](skills/human-flutter/references/color-preview.md).
- **Centralized Design System Specification**:
  - Added dedicated reference: [`skills/human-flutter/references/design-system.md`](skills/human-flutter/references/design-system.md) integrating spacing, radius, elevation, typography, and ThemeData.
- **Micro-Interactions & Animation Architecture**:
  - Added dedicated reference: [`skills/human-flutter/references/animations.md`](skills/human-flutter/references/animations.md).
- **Architecture Decision Record (ADR 0003)**:
  - Recorded [`docs/adr/0003-permission-first-decision-system-and-mandatory-structure.md`](docs/adr/0003-permission-first-decision-system-and-mandatory-structure.md).
- **Updated Master Instructions**:
  - Updated `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `skills/human-flutter/SKILL.md`, `.agents/skills/human-flutter/SKILL.md`, `core/folder-structure.md`, `core/human-interaction.md`, `design/color-system.md`, and `workflows/new-project.md`.
- **Validation Suite Expansion**:
  - Expanded `scripts/validate-docs` (147 architecture files) and `scripts/validate-structure` (34 reference modules). All suites pass with 0 errors.

---

## [4.0.0] - 2026-11-07

### Major Transformation: Complete Flutter-Only Human UI Engineering System

#### Changed & Transformed
- **Absolute Flutter-Only Focus**: Transformed repository from a multi-framework software engineering system into an exclusive, specialized **Flutter & Dart Human UI Engineering System**. Removed all generic web (React, Next.js, Vue, Angular), non-Flutter mobile (React Native), and unrelated backend frameworks.
- **Canonical Skill Architecture**:
  - Restructured canonical skill to `skills/human-flutter/` (`SKILL.md`) with dedicated, in-depth Flutter engineering reference modules.
- **10 Core Flutter Engineering Intelligence Modules**:
  - Human UI Design Engineering, Human Color Intelligence, Component Engineering, Dart Coding Standards, File Structure Engineering, Responsive Layouts, Animations, Performance, Platform Integration, and Product Engineering.
- **Mandatory 18-Step Human Design-to-Code Workflow**:
  - Implemented the full 18-step sequential engineering lifecycle.
- **Automated Validation Suite**:
  - Added `scripts/validate-flutter-only` enforcing zero non-Flutter framework leakage.
  - Updated `scripts/validate-docs`, `scripts/validate-links`, and `scripts/validate-structure`.

---

## [3.0.0] - 2026-11-07

### Ultimate Upgrade: Universal AI Software Engineering Operating System
