# Architecture Decision Records (ADRs)

> **Historical Log of Architectural & Technology Decisions**

This directory stores Architecture Decision Records (ADRs) following the lightweight format described by Michael Nygard. ADRs capture the context, alternatives, rationale, and consequences of significant technical choices made across the codebase.

---

## Index of Architecture Decision Records

| ADR # | Title | Date | Status | Summary |
|---|---|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record Architecture Decisions | 2026-11-07 | **Accepted** | Establish ADR practice for capturing major structural decisions. |
| [0002](0002-flutter-only-engineering-system.md) | Transform into Complete Flutter-Only Engineering System | 2026-11-07 | **Accepted** | Focus repository exclusively on Flutter & Dart engineering. |
| [0003](0003-permission-first-decision-system-and-mandatory-structure.md) | Permission-First Bengali Decision System & Mandatory 3-Tier Architecture | 2026-11-07 | **Accepted** | Mandate 7-step Bengali permission gates, `lib/core/`, `lib/shared/`, `lib/features/`, and color previews. |

---

## When to Write an ADR

Create an ADR whenever a decision:
- Introduces or replaces a core state management library, database engine, or routing pattern.
- Establishes a fundamental presentation pattern (e.g., Feature-First BLoC, Clean Architecture).
- Alters authentication, authorization, or security boundaries.
- Establishes cross-cutting API standards (e.g., REST vs GraphQL vs WebSockets).
- Changes project directory conventions or build configurations.

To create a new ADR, copy [`template.md`](template.md) to `docs/adr/NNNN-title-in-kebab-case.md` and increment the sequential number.
