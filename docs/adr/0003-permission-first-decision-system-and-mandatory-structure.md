# 3. Permission-First Bengali Decision System & Mandatory 3-Tier Architecture

Date: 2026-11-07

## Status

Accepted

## Context

AI coding assistants frequently execute sweeping architectural, dependency, state management, or styling changes autonomously based on silent assumptions. In real-world enterprise Flutter development, this leads to architectural drift, incompatible package churn, unwanted color theme alterations, and loss of developer control.

Furthermore, applications generated without a consistent folder structure develop circular dependencies and disorganized codebases where business logic, widgets, and domain models are mixed haphazardly.

## Decision

We establish two non-negotiable architectural mandates for the Human Flutter Engineering system:

1. **Permission-First Decision System in Bengali (Highest Priority)**:
   - Before executing any important decision (State Management, Routing, DI, Packages, Architecture, File Structure, Design System, Brand Colors, UI/UX direction, Database, API client, Native integrations, Refactoring), the agent MUST explain the decision in professional Bengali following a strict 7-step sequence:
     1. Explain the decision.
     2. Explain why it is necessary.
     3. Present options.
     4. Detail pros & cons.
     5. Recommend the best option.
     6. Ask for approval clearly.
     7. STOP and wait for explicit confirmation.
   - Silence or vague replies are never treated as consent.

2. **Mandatory 3-Tier Flutter Project Structure**:
   - All Flutter applications generated or maintained MUST enforce:
     - `lib/core/` — Global foundational infrastructure (config, network, routing, storage, theme tokens). Zero feature logic.
     - `lib/shared/` — Reusable cross-feature UI (`widgets/`, `custom/`, `animations/`, `layouts/`).
     - `lib/features/` — Feature-first domain modules (`data/`, `domain/`, `presentation/`).

3. **Mandatory 3–4 Color Selection & 12-Component Visual Placement Preview**:
   - The user must explicitly choose 3 or 4 primary colors (HEX).
   - Before theme finalization, the agent must present a 12-component visual UI color board preview demonstrating color distribution across App background, App bar, Navigation bar, Buttons, Cards, Inputs, Typography, Icons, Borders, Selection states, and Status states.

## Consequences

- **Positive**: Complete developer transparency and control; eliminates unwanted code rewrites and unsolicited dependencies; guarantees enterprise-grade, clean modular structure.
- **Negative**: Adds interactive decision gates before starting new project generation; requires agents to adhere strictly to multi-step stop-and-wait communication protocols.
