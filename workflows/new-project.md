# Workflow: New Project Setup

> Step-by-step execution guide for establishing a new UI engineering project from scratch.

---

## 1. Purpose

Starting a new UI project without systematic foundations results in early architectural drift, ad-hoc styling, and technical debt. 

This workflow guides an AI agent or engineer through setting up a production-ready UI codebase.

---

## 2. Step-by-Step Workflow

```mermaid
flowchart TD
    S1[Step 1: Project Discovery & Specs] --> S2[Step 2: Framework Selection]
    S2 --> S3[Step 3: Scaffolding & Tooling]
    S3 --> S4[Step 4: Design Tokens Setup]
    S4 --> S5[Step 5: Shared Core Primitives]
    S5 --> S6[Step 6: App Shell & Routing]
    S6 --> S7[Step 7: Verification & QA Baseline]
```

### Step 1: Project Discovery & Requirements
1. Define the Flutter application domain, target audience, brand tone, and supported platforms (Android, iOS, Web, macOS, Windows, Linux).
2. Complete the standardized [Project Brief Template](../templates/project-brief.md).

### Step 2: Architecture & State Management Selection
1. Consult [Flutter Architecture](../skills/human-flutter/references/flutter-architecture.md) and [State Management](../skills/human-flutter/references/state-management.md).
2. Confirm state management approach (BLoC, Riverpod, Provider) and routing (`go_router`).

### Step 3: Scaffolding & Strict Tooling Setup
1. Initialize the Flutter project repository with standard feature-first directory conventions (refer to [Folder Structure](../core/folder-structure.md)).
2. Configure strict type-checking and lints in `analysis_options.yaml` (strict casts, inference, raw types).
3. Setup code formatters (`dart format .`).

### Step 4: Design Tokens & Base Theme Setup
1. Establish the design token system:
   - Neutrals, primary brand colors, semantic status colors (refer to [Color System](../design/color-system.md)).
   - Typographic scale, line-heights, and font families (refer to [Typography](../design/typography.md)).
   - Spatial 4pt/8pt grid (refer to [Spacing](../design/spacing.md)).
2. Complete the [Design System Template](../templates/design-system.md).

### Step 5: Shared Core Primitives
Construct the foundational reusable widget primitives before building any business screens:
- `AppButton` (Primary, Secondary, Ghost, Destructive) with loading states.
- `AppTextField` with accessible labels, error hints, and focus rings.
- `AppCard` container with outlined and elevated variants.
- `Typography` primitives and semantic badges.

### Step 6: Navigation Shell & Root Layout
1. Implement the responsive navigation shell (NavigationRail on desktop, NavigationBar on mobile).
2. Wire up the `go_router` system and root error boundaries.

### Step 7: Verification & QA Baseline
1. Verify clean release build (`flutter build appbundle` or `flutter build web`).
2. Run initial test suite (`flutter test`) and accessibility audit.
3. Generate the baseline [Quality Report](../templates/quality-report.md).

---

## 3. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Project Discovery: [../core/project-discovery.md](../core/project-discovery.md)
- Canonical Flutter Skill: [../skills/human-flutter/SKILL.md](../skills/human-flutter/SKILL.md)
- Project Brief Template: [../templates/project-brief.md](../templates/project-brief.md)
- Release Checklist: [../quality/release-checklist.md](../quality/release-checklist.md)

