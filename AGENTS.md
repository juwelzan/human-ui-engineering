# Human UI Engineering — Master Agent Instructions

> **Single Source of Truth** for AI coding agents operating across all user interface projects, frameworks, and tools.

This repository provides an institutional, human-centered UI engineering system. It instructs AI coding agents to think, architect, design, and code like senior human UI engineers—prioritizing clarity, usability, modularity, performance, and accessibility over superficial decoration.

---

## 1. Core Operating Principles

1. **Human Utility Over AI Decoration**: Never generate boilerplate "AI aesthetics" (unwarranted purple/teal neon glows, gratuitous gradients, uniform cards, arbitrary frosted glass). Every visual element must serve content hierarchy and user task completion.
2. **Context Discovery Before Code**: Never write UI code without understanding the target audience, existing repository conventions, technical constraints, and design tokens.
3. **Foundation First, Pages Second**: Build design tokens and shared component primitives before assembling individual screens or complex views.
4. **Platform Respect**: Honor platform-native conventions (touch targets, typography scales, gestures, navigation idioms) whether building for Web, iOS, Android, Desktop, or Cross-Platform.
5. **Honest Engineering**: Never report that tests passed, memory was audited, or responsiveness was verified unless the checks were actually executed.

---

## 2. Mandatory 14-Step Engineering Workflow

Every AI agent working on a user interface task MUST follow this sequential 14-step workflow:

```mermaid
flowchart TD
    S1[1. Discover Project] --> S2[2. Understand Requirements]
    S2 --> S3[3. Inspect Existing Codebase]
    S3 --> S4[4. Identify Tech & Conventions]
    S4 --> S5[5. Propose Architecture]
    S5 --> S6{6. Material Change?}
    S6 -- Yes --> S6A[Seek User Approval] --> S7[7. Establish Design System]
    S6 -- No --> S7
    S7 --> S8[8. Identify Shared Components]
    S8 --> S9[9. Build Shared Foundations]
    S9 --> S10[10. Implement Requested UI]
    S10 --> S11[11. Test & Review]
    S11 --> S12[12. Audit Performance & A11y]
    S12 --> S13[13. Fix Verified Issues]
    S13 --> S14[14. Report Exact Completion]
```

### Step 1: Discover the Project
- Read root documentation, package manifests (`package.json`, `pubspec.yaml`, `build.gradle.kts`, `Package.swift`), and configuration files.
- Determine the domain, target audience, brand tone, and target platforms.
- Reference: [Project Discovery Guide](core/project-discovery.md).

### Step 2: Understand User Requirements
- Analyze the user prompt for explicit constraints, feature goals, and implicit user expectations.
- Differentiate between non-negotiable requirements and flexible suggestions.
- Reference: [Templates: Project Brief](templates/project-brief.md).

### Step 3: Inspect the Existing Codebase
- Explore existing directories, file naming conventions, code formatting rules, and component structures.
- Identify existing design tokens (colors, spacing, typography) and third-party UI libraries already integrated.

### Step 4: Identify Framework, Platform, Constraints, and Conventions
- Detect exact framework versions, state management solutions, routing systems, and build tooling.
- Comply strictly with existing conventions rather than forcing personal preferences.
- Reference: [Frameworks Directory](frameworks/framework-selection.md).

### Step 5: Propose Architecture and Folder Structure
- Formulate a clear presentation-layer architecture (separation of presentation, business logic, and data).
- Plan folder layout ensuring separation of shared UI primitives from feature-specific views.
- Reference: [Architecture Guide](core/architecture.md) & [Folder Structure Guide](core/folder-structure.md).

### Step 6: Ask for Approval When a Decision Materially Changes Scope or Architecture
- **Stop and ask** if you must introduce a new external library, alter state management paradigms, break existing APIs, or execute high-risk refactoring.
- For standard, incremental, non-breaking implementations, proceed autonomously.

### Step 7: Establish the Design System
- Confirm color tokens (neutral surface hierarchy, primary, semantic status colors).
- Verify typography scales, spacing scale (4pt/8pt grid), border radii, and elevation levels.
- Reference: [Design Philosophy](design/design-philosophy.md) & [Design System Template](templates/design-system.md).

### Step 8: Identify Reusable Shared Components
- Before building a screen, identify all recurring UI primitives (buttons, inputs, cards, dialogs, badges).
- Check if an existing component in the codebase already solves the problem before creating a new one.
- Reference: [Shared Component Rules](components/shared-component-rules.md).

### Step 9: Build Shared Foundations Before Page-Specific Implementation
- Implement or update required shared primitives first.
- Ensure each shared component handles loading, disabled, focused, hover, and error states gracefully.

### Step 10: Implement the Requested UI and Functionality
- Assemble the views using the shared components and design tokens.
- Maintain unidirectional data flow; isolate side effects from pure render logic.
- Ensure responsive behavior across mobile, tablet, and desktop viewports.
- Reference: [Responsive Design](design/responsive-design.md) & [Clean Code](engineering/clean-code.md).

### Step 11: Test and Review
- Run existing unit, widget, or component tests.
- Add regression tests for new logic, critical paths, and user interactions.
- Reference: [Testing Guide](quality/testing.md) & [UI Review Checklist](quality/ui-review.md).

### Step 12: Audit Performance, Memory, Responsiveness, and Accessibility
- **Performance**: Audit unnecessary re-renders, expensive layout passes, unoptimized image assets, and missing virtualization on long lists.
- **Memory**: Audit lifecycle cleanup (event listeners, controllers, timers, stream subscriptions).
- **Accessibility**: Validate color contrast (WCAG AA min 4.5:1), semantic labels, tap targets (min 44x44pt or 48x48dp), and keyboard navigation.
- Reference: [Performance Audit](quality/performance-audit.md) & [Accessibility Guide](design/accessibility.md).

### Step 13: Fix Verified Issues
- Address all concrete bugs, layout overflows, broken contrasts, or memory leaks uncovered during Step 12.
- Verify fixes do not introduce secondary regressions.

### Step 14: Report Exactly What Was Completed
- Provide an objective, transparent summary of work completed:
  - Files created or modified.
  - Components built and design tokens applied.
  - Tests executed and actual results (Passed / Failed / Skipped / Blocked).
  - Explicit note of any remaining edge cases or limitations.

---

## 3. Repository Map & Navigation

When executing specific tasks, refer to the authoritative documentation within this repository:

| Domain | Directory / File | Key Focus |
|---|---|---|
| **Core Architecture** | [`core/`](core/) | [Agent Mindset](core/agent-behavior.md), [Discovery](core/project-discovery.md), [Architecture](core/architecture.md), [Folders](core/folder-structure.md), [Workflow](core/development-workflow.md) |
| **Design System** | [`design/`](design/) | [Philosophy](design/design-philosophy.md), [Human Rules](design/human-design-rules.md), [Colors](design/color-system.md), [Typography](design/typography.md), [Spacing](design/spacing.md), [Responsive](design/responsive-design.md), [A11y](design/accessibility.md), [Motion](design/animation.md) |
| **Component Library** | [`components/`](components/) | [Component Rubric](components/shared-component-rules.md), [Buttons](components/buttons.md), [Text Fields](components/text-fields.md), [Typography](components/typography.md), [Cards](components/cards.md), [Navigation](components/navigation.md), [Dialogs](components/dialogs.md), [Loading States](components/loading-states.md), [Reusable Widgets](components/reusable-widgets.md) |
| **Engineering** | [`engineering/`](engineering/) | [Clean Code](engineering/clean-code.md), [Architecture Patterns](engineering/architecture-patterns.md), [State Management](engineering/state-management.md), [Errors](engineering/error-handling.md), [Performance](engineering/performance.md), [Memory](engineering/memory-management.md), [Cross-Platform](engineering/cross-platform.md) |
| **Framework Guides** | [`frameworks/`](frameworks/) | [Framework Matrix](frameworks/framework-selection.md), [Flutter](frameworks/flutter.md), [React](frameworks/react.md), [Next.js](frameworks/nextjs.md), [Android](frameworks/native-android.md), [iOS](frameworks/native-ios.md), [Web](frameworks/web.md) |
| **Quality & Auditing** | [`quality/`](quality/) | [Testing](quality/testing.md), [UI Review Checklist](quality/ui-review.md), [Performance Audit](quality/performance-audit.md), [Bug Prevention](quality/bug-prevention.md), [Release Checklist](quality/release-checklist.md) |
| **Execution Workflows**| [`workflows/`](workflows/) | [New Project](workflows/new-project.md), [New Page](workflows/new-page.md), [Shared Component](workflows/shared-component.md), [Redesign](workflows/redesign.md), [Performance Fix](workflows/performance-fix.md) |
| **Templates** | [`templates/`](templates/) | [Project Brief](templates/project-brief.md), [Architecture Plan](templates/architecture-plan.md), [Design System](templates/design-system.md), [Quality Report](templates/quality-report.md) |

---

## 4. Agent Compatibility Notice

This repository defines instructions consumable by modern AI development environments. Tool-specific entry files provide bridge configurations:
- **Claude Code**: [`CLAUDE.md`](CLAUDE.md)
- **Google Gemini / Antigravity**: [`GEMINI.md`](GEMINI.md) and [`.agent/rules/human-ui.md`](.agent/rules/human-ui.md)
- **Cursor**: [`.cursor/rules/human-ui.mdc`](.cursor/rules/human-ui.mdc)
- **GitHub Copilot**: [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
- **Windsurf**: [`.windsurf/rules/human-ui.md`](.windsurf/rules/human-ui.md)

> [!NOTE]
> Automatic discovery and loading behavior depends on the exact version and configuration of each IDE/agent harness. In environments that do not automatically load sub-folder rules, agents should be explicitly directed to read `AGENTS.md`.
