# Architecture Decision Records (ADRs)

> **Historical Log of Architectural & Technology Decisions**

This directory stores Architecture Decision Records (ADRs) following the lightweight format described by Michael Nygard. ADRs capture the context, alternatives, rationale, and consequences of significant technical choices made across the codebase.

---

## Index of Architecture Decision Records

| ADR # | Title | Date | Status | Summary |
|---|---|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record Architecture Decisions | 2026-11-07 | **Accepted** | Establish ADR practice for capturing major structural decisions. |

---

## When to Write an ADR

Create an ADR whenever a decision:
- Introduces or replaces a core framework, state management library, or database engine.
- Establishes a fundamental presentation pattern (e.g., MVVM, BLoC, Clean Architecture).
- Alters authentication, authorization, or security boundaries.
- Establishes cross-cutting API standards (e.g., REST vs GraphQL vs gRPC).
- Changes project directory conventions or monorepo isolation boundaries.

To create a new ADR, copy [`template.md`](template.md) to `docs/adr/NNNN-title-in-kebab-case.md` and increment the sequential number.
