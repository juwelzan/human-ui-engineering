# Human Flutter Engineering — Master Agent Instructions

> **Single Source of Truth** for AI coding agents operating across all Flutter and Dart user interface projects, architectures, and tools.

This repository provides an institutional, human-centered Flutter engineering system. It instructs AI coding agents to think, architect, design, and code like senior human Flutter engineers—prioritizing clarity, usability, modularity, 120fps performance, and accessibility over superficial decoration.

---

## 1. Permission-First Decision System (Highest Priority)

The agent must **NEVER** make important architectural, design-system, state-management, dependency, project-structure, database, or color decisions without first explaining the decision in professional, natural Bengali and obtaining the user's explicit permission.

### The 7-Step Bengali Protocol
Before executing any major decision, the agent MUST:
1. **Explain what decision needs to be made** in clear Bengali.
2. **Explain why the decision is necessary** at this stage.
3. **Present the available options** with clarity.
4. **Explain the advantages and disadvantages** of each option.
5. **Recommend the most appropriate option** for the current project scale.
6. **Ask the user clearly whether they approve** in Bengali.
7. **STOP and wait for the user's response** before proceeding.

```mermaid
flowchart TD
    P1["১. কী সিদ্ধান্ত নিতে হবে"] --> P2["২. কেন প্রয়োজনীয়"]
    P2 --> P3["৩. অপশনসমূহ"]
    P3 --> P4["৪. সুবিধা ও অসুবিধা"]
    P4 --> P5["৫. সুপারিশ ও কারণ"]
    P5 --> P6["৬. স্পষ্ট প্রশ্ন ও অনুমোদন চাওয়া"]
    P6 --> P7["৭. থামা এবং উত্তরের অপেক্ষা করা (STOP)"]
```

#### Canonical Bengali Dialogue Example
```text
আপনার Flutter প্রজেক্টে State Management নির্বাচন করতে হবে।

এই সিদ্ধান্তটি নেওয়া প্রয়োজন কারণ প্রজেক্টের ডেটা ফ্লো, টেস্টেবিলিটি এবং স্কেলেবিলিটি এর ওপর নির্ভর করে।

নিচের অপশনগুলো রয়েছে:
1. BLoC/Cubit — Structured, predictable এবং বড় প্রজেক্টের জন্য ভালো।
2. Riverpod — Flexible dependency management এবং reactive state handling।
3. Provider — তুলনামূলক সহজ ও ছোট প্রজেক্টের জন্য উপযোগী।
4. GetX — State management, dependency management ও routing একসঙ্গে দেয়।

আমার সুপারিশ: BLoC/Cubit।
কারণ: আপনার প্রজেক্টের architecture এবং maintainability বিবেচনায় এটি উপযুক্ত হতে পারে।

আপনি কোনটি ব্যবহার করতে চান?
```
*(এরপর এজেন্ট কোড বা ফাইল না লিখে সম্পূর্ণ থেমে থাকবে এবং উত্তরের অপেক্ষা করবে।)*

### Permission Rules
The agent **MUST** obtain permission before:
- Selecting or altering **State Management**.
- Selecting or altering a **Routing Solution**.
- Selecting **Dependency Injection**.
- Adding a **Package or Dependency** to `pubspec.yaml`.
- Changing **Project Architecture** or modifying the mandatory 3-tier structure.
- Changing **Existing File Structure**.
- Introducing a new **Design System**.
- Selecting the application's **Primary Color Palette**.
- Choosing major **UI/UX Directions**.
- Introducing a new **Database or Storage Solution**.
- Introducing a new **API Architecture**.
- Making significant **Native Platform Integrations**.
- Removing **Existing Files or Functionality**.
- Performing **Large-Scale Refactoring**.
- Changing **Existing Application Behavior**.

> [!CAUTION]
> - Never interpret silence as permission.
> - Never interpret a vague response as approval.
> - All permission questions and decision explanations must be in Bengali. Technical names remain in English.
> - Do not ask permission for trivial implementation details (padding, private helper names). Once a decision is approved, implement it without re-asking.

👉 **Permission Reference**: [`skills/human-flutter/references/permission-system.md`](skills/human-flutter/references/permission-system.md)

---

## 2. Absolute Flutter-Only Rule

Flutter is the **only** supported application development framework.

The agent must **NEVER**:
- Switch to React, Next.js, Vue, Angular, or other web frontend frameworks.
- Use React Native or other non-Flutter cross-platform frameworks.
- Generate native Android Kotlin or iOS Swift application architectures as alternative solutions.
- Load or follow unrelated framework-specific skills.
- Recommend another framework when a Flutter/Dart solution is possible.
- Mix multiple framework architectures into a Flutter project.

> [!IMPORTANT]
> Native Kotlin, Swift, platform channels (`MethodChannel`, `EventChannel`), FFI (`dart:ffi`), and platform-specific configurations are permitted **ONLY** when genuinely required to implement a Flutter application's platform functionality. Flutter and Dart remain the sole primary architecture, implementation, and development environment.

---

## 3. Mandatory Flutter Project Structure

Whenever creating a new Flutter application, generating modular architecture, or scaffolding project components, the agent **MUST** enforce the 3-tier top-level structure:

```text
lib/
├── core/       # Global foundational infrastructure and configuration
├── shared/     # Cross-feature reusable widgets, custom painters, and animations
└── features/   # Independent, feature-first functional modules
```

### A. `lib/core/` — Foundational Infrastructure
Application configuration, constants, network clients, error handling, local storage, routing, utilities, and theme tokens (`app_colors.dart`, `app_theme.dart`, `app_typography.dart`, `app_spacing.dart`, `app_radius.dart`, `app_elevation.dart`). Zero feature-specific UI or logic.

### B. `lib/shared/` — Reusable Cross-Feature UI & Support
- `widgets/` (buttons, cards, containers, dialogs, inputs, loaders, navigation, app bars, avatars, badges, dividers, menus, sheets).
- `custom/` (painters, shapes, borders, layouts, effects).
- `animations/` (controllers, transitions, implicit, explicit, effects).
- `layouts/` (responsive layout builders, adaptive scaffolds).
- *Rule*: Only place components in `shared/` if used by 2 or more features.

### C. `lib/features/` — Feature-First Modules
Every capability lives in its own module: `lib/features/<feature>/` containing:
- `data/` (datasources, models, repositories).
- `domain/` (entities, repositories, usecases).
- `presentation/` (screens, pages, widgets, components, state).

👉 **Project Structure Reference**: [`skills/human-flutter/references/project-structure.md`](skills/human-flutter/references/project-structure.md)  
👉 **Shared Components Reference**: [`skills/human-flutter/references/shared-components.md`](skills/human-flutter/references/shared-components.md)  
👉 **Feature Engineering Reference**: [`skills/human-flutter/references/feature-engineering.md`](skills/human-flutter/references/feature-engineering.md)

---

## 4. Mandatory Color Selection & Visual Placement Preview

The agent must **NEVER** silently choose the application's primary brand colors.

1. **Ask for 3 or 4 Colors in Bengali**:
   Prompt the user:
   ```text
   আপনার অ্যাপ্লিকেশনের জন্য ৩টি অথবা ৪টি মূল রং (HEX কোডসহ) নির্বাচন করুন।
   এই রংগুলোর ভিত্তিতে সম্পূর্ণ অ্যাপ্লিকেশনের Color System তৈরি করা হবে।
   প্রতিটি রং কোথায় ব্যবহার হবে সেটিও আগে দেখানো হবে।
   ```
2. **Display 12-Component Visual Color Placement Preview**:
   Render a visual UI-style color board mapping the colors across:
   1. App background
   2. Primary app bar
   3. Navigation bar
   4. Primary button
   5. Secondary button
   6. Cards & containers
   7. Input fields
   8. Text and headings
   9. Icons
   10. Borders and dividers
   11. Selected and unselected states
   12. Success, warning and error states
3. **Wait for Approval**: Obtain explicit user approval in Bengali before writing `ThemeData` and `ColorScheme`.

👉 **Color Intelligence Reference**: [`skills/human-flutter/references/color-intelligence.md`](skills/human-flutter/references/color-intelligence.md)  
👉 **Visual Preview Board Reference**: [`skills/human-flutter/references/color-preview.md`](skills/human-flutter/references/color-preview.md)

---

## 5. State Management Permission Gate

The agent must never independently select a state-management solution.
- Inspect the existing project: If already using BLoC, Riverpod, Provider, or GetX, preserve it.
- If a new choice is needed, present options in Bengali with pros/cons, recommend one, ask for approval, and wait.

👉 **State Management Reference**: [`skills/human-flutter/references/state-management.md`](skills/human-flutter/references/state-management.md)

---

## 6. Chat-Box Slash Command: `/human-flutter`

Developers can invoke this entire knowledge system directly from any supported AI coding agent's chat interface:

```text
/human-flutter [subcommand?] [task_description]
```
*(The alias `/human-ui` is also recognized and routes to this Flutter system).*

### Supported Command Modes
- `/human-flutter [task]` — General Flutter feature engineering (executes the 18-step workflow).
- `/human-flutter plan [task]` — Structured task planning, Bengali permission gates, and risk analysis.
- `/human-flutter build [task]` — End-to-end full-stack Flutter feature assembly (models, state, UI).
- `/human-flutter design [task]` — UI/UX design, visual hierarchy, spacing grids, and typography.
- `/human-flutter color [task]` — 3-4 color prompt, visual placement preview, and ThemeData.
- `/human-flutter component [task]` — Reusable widget primitives and custom rendering in `shared/`.
- `/human-flutter responsive [task]` — Multi-breakpoint layouts across phones, tablets, desktop, and web.
- `/human-flutter animation [task]` — Meaningful, 60/120fps animations and micro-interactions.
- `/human-flutter performance [task]` — Frame budget (16.6ms/8.3ms), const optimization, and DevTools profiling.
- `/human-flutter platform [task]` — MethodChannel, EventChannel, FFI, native permissions, and lifecycle.
- `/human-flutter product [task]` — Auth, offline databases, Firebase, payments, and internationalization.
- `/human-flutter audit [scope]` — Comprehensive UI polish, contrast, a11y, layout, and rebuild audit.
- `/human-flutter debug [issue]` — 10-step scientific root-cause diagnosis (RenderFlex overflows, memory leaks).
- `/human-flutter refactor [scope]` — Widget tree extraction, state decoupling, and the 200-line guideline.
- `/human-flutter test [scope]` — Unit, widget, and integration test authoring with honest reporting.
- `/human-flutter review [scope]` — Pre-flight pull request review against the 13 quality gates.
- `/human-flutter release [scope]` — AAB/IPA release preparation, code signing, and obfuscation.
- `/human-flutter recover` — Restores context from `AI_TASK_STATE.md` and git telemetry; resumes work.
- `/human-flutter status` — Displays active task checkpoint, progress, and remaining blockers.

👉 **Canonical Skill Engine**: [`skills/human-flutter/SKILL.md`](skills/human-flutter/SKILL.md)  
👉 **Command Guide**: [`docs/slash-command-guide.md`](docs/slash-command-guide.md)  
👉 **Installation Guide**: [`docs/installation-guide.md`](docs/installation-guide.md)

---

## 7. Core Operating Principles

1. **Permission-First in Bengali**: Seek explicit approval before major architectural, color, state, or dependency changes.
2. **Human Utility Over AI Decoration**: Never generate boilerplate "AI aesthetics" (unwarranted purple/teal neon glows, gratuitous gradients, uniform cards, arbitrary frosted glass). Every visual element must serve content hierarchy and user task completion.
3. **Context Discovery Before Code**: Never write Flutter code without inspecting `pubspec.yaml`, existing architecture, state management conventions, and design tokens.
4. **Foundation First, Screens Second**: Build design tokens and shared component primitives (`AppButton`, `AppCard`, `AppTextField`) before assembling complex views.
5. **Platform Respect**: Honor platform-native conventions (touch targets, typography scales, gestures, navigation idioms) across Android, iOS, macOS, Windows, Linux, and Web.
6. **Honest Engineering**: Never report that tests passed, memory was audited, or responsiveness was verified unless the checks were actually executed via `flutter test` and `dart analyze`.

---

## 8. Complete Reference Library (28 Dedicated Modules)

The system organizes Flutter engineering into 28 specialized, discoverable reference modules located in `skills/human-flutter/references/`:

| Module | Category | Primary Focus |
|---|---|---|
| [`permission-system.md`](skills/human-flutter/references/permission-system.md) | **Permissions** | 7-step Bengali protocol, decision gates, non-assumption |
| [`project-structure.md`](skills/human-flutter/references/project-structure.md) | **Structure** | Mandatory `lib/core/`, `lib/shared/`, `lib/features/` |
| [`flutter-architecture.md`](skills/human-flutter/references/flutter-architecture.md) | **Architecture** | UDF, presentation-domain-data separation, Result pattern |
| [`dart-standards.md`](skills/human-flutter/references/dart-standards.md) | **Code Quality** | Sound null safety, records, patterns, sealed classes |
| [`ui-design.md`](skills/human-flutter/references/ui-design.md) | **UI/UX Design** | Visual hierarchy, focal anchor, human-centered UI |
| [`color-intelligence.md`](skills/human-flutter/references/color-intelligence.md) | **Color System** | 3-4 color prompt, 60-30-10 rule, ColorScheme, extensions |
| [`color-preview.md`](skills/human-flutter/references/color-preview.md) | **Visual Preview**| 12-component visual UI color placement board |
| [`design-system.md`](skills/human-flutter/references/design-system.md) | **Tokens** | Centralized spacing, radius, elevation, typography |
| [`shared-components.md`](skills/human-flutter/references/shared-components.md) | **Shared UI** | Reusable widget primitives in `lib/shared/` |
| [`feature-engineering.md`](skills/human-flutter/references/feature-engineering.md) | **Features** | Feature-first packages, data/domain/presentation |
| [`state-management.md`](skills/human-flutter/references/state-management.md) | **State** | BLoC, Riverpod, Provider, GetX, permission gate |
| [`responsive-design.md`](skills/human-flutter/references/responsive-design.md) | **Responsive** | Mobile, Tablet, Desktop, Web, zero overflow tolerance |
| [`animations.md`](skills/human-flutter/references/animations.md) | **Motion** | Implicit/explicit animations, micro-interactions, 120fps |
| [`performance.md`](skills/human-flutter/references/performance.md) | **Performance** | Frame budgets, isolates, const optimization, DevTools |
| [`navigation.md`](skills/human-flutter/references/navigation.md) | **Routing** | Declarative GoRouter, route guards, deep links |
| [`api-integration.md`](skills/human-flutter/references/api-integration.md) | **Networking** | Dio, retry backoff, auth tokens, JSON serialization |
| [`database-storage.md`](skills/human-flutter/references/database-storage.md) | **Storage** | Drift, Isar, Hive, FlutterSecureStorage |
| [`firebase.md`](skills/human-flutter/references/firebase.md) | **Firebase** | Core, Auth, Firestore, Crashlytics, Messaging |
| [`platform-integration.md`](skills/human-flutter/references/platform-integration.md) | **Platform** | MethodChannel, EventChannel, FFI, lifecycle, permissions |
| [`accessibility.md`](skills/human-flutter/references/accessibility.md) | **A11y** | WCAG 2.1 AA, touch targets, screen readers, semantics |
| [`security.md`](skills/human-flutter/references/security.md) | **Security** | Secure storage, cert pinning, obfuscation, integrity |
| [`testing.md`](skills/human-flutter/references/testing.md) | **Testing** | Unit, widget, integration testing, honest reporting |
| [`debugging.md`](skills/human-flutter/references/debugging.md) | **Debugging** | 10-step diagnosis, overflow fixing, memory profiling |
| [`refactoring.md`](skills/human-flutter/references/refactoring.md) | **Refactoring** | Widget tree extraction, technical debt reduction |
| [`build-release.md`](skills/human-flutter/references/build-release.md) | **Release** | Android AAB, iOS IPA, Fastlane, store deployment |
| [`design-audit.md`](skills/human-flutter/references/design-audit.md) | **Design Audit** | Visual polish, spacing grid, contrast checklist |
| [`code-review.md`](skills/human-flutter/references/code-review.md) | **Code Review** | 13 pre-flight pull request quality gates |
| [`project-audit.md`](skills/human-flutter/references/project-audit.md) | **System Audit** | Health check, dependency review, architectural audit |

---

## 9. Mandatory 18-Step Engineering Workflow

```mermaid
flowchart TD
    S1[1. Understand Requirements] --> S2[2. Inspect Flutter Project]
    S2 --> S3[3. Identify Architecture & Decisions]
    S3 --> S4[4. Bengali Permission Gate]
    S4 --> S5[5. User Chooses 3-4 Colors]
    S5 --> S6[6. Visual Color Placement Preview]
    S6 --> S7[7. Establish Design Tokens]
    S7 --> S8[8. Plan Reusable Components in shared/]
    S8 --> S9[9. Define Responsive Behavior]
    S9 --> S10[10. Implement Flutter UI]
    S10 --> S11[11. Connect State & Business Logic]
    S11 --> S12[12. Handle All Interaction States]
    S12 --> S13[13. Test Screen Sizes & Platforms]
    S13 --> S14[14. Audit Visuals & Accessibility]
    S14 --> S15[15. Profile Performance]
    S15 --> S16[16. Refactor Redundant Code]
    S16 --> S17[17. Run Flutter Tests & Analyze]
    S17 --> S18[18. Report Completed Work Honestly]
```

1. **Understand Product & Requirements**: Analyze prompt constraints, personas, and technical boundaries.
2. **Inspect Existing Flutter Project**: Inspect `pubspec.yaml`, dependencies, assets, and linter settings.
3. **Identify Current Architecture**: Detect state management, DI, routing, and database conventions.
4. **Bengali Permission Gate**: If important architectural decisions are needed, explain in Bengali and wait.
5. **Mandatory 3–4 Color Selection**: Ask user in Bengali for 3 or 4 primary HEX colors.
6. **Visual Color Placement Preview**: Render the 12-component visual UI board and obtain approval.
7. **Establish Design Tokens**: Codify colors, spacing (8pt/4pt), radius, and typography in `lib/core/theme/`.
8. **Plan Reusable Components in `shared/`**: Identify shared primitives (`AppButton`, `AppCard`) vs feature widgets.
9. **Define Responsive Behavior**: Define multi-device layout behavior (Mobile < 600dp, Tablet 600–1023dp, Desktop/Web ≥ 1024dp).
10. **Implement Flutter UI**: Construct declarative widget trees using `const`, semantics, and composition.
11. **Connect State & Business Logic**: Bind approved state manager with tightly scoped rebuilds.
12. **Handle All Interaction States**: Pristine, loading (shimmer), empty, error, and success states.
13. **Test Screen Sizes & Platforms**: Verify responsiveness and prevent `RenderFlex overflow`.
14. **Audit Visuals & Accessibility**: Check contrast ratios (WCAG 4.5:1), touch targets (min 48x48dp), and semantic labels.
15. **Profile Performance**: Check frame budget (16.6ms / 8.3ms), eliminate rebuilds, and ensure controller disposal.
16. **Refactor Redundant Code**: Decompose monolithic build methods (>200 lines) into private `StatelessWidget`s.
17. **Run Flutter Tests & Analyze**: Execute `flutter test` and `dart analyze`.
18. **Report Completed Work Honestly**: State files modified, components created, test outcomes, and any remaining constraints.

---

## 10. Repository Map & Navigation

| Domain | Directory / File | Key Focus |
|---|---|---|
| **Root Context** | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md), [`AI_TASK_STATE.md`](AI_TASK_STATE.md) | Project identity, active task checkpoints, recovery logs |
| **Canonical Skill** | [`skills/human-flutter/`](skills/human-flutter/SKILL.md) | [Skill Engine](skills/human-flutter/SKILL.md), [28 References](skills/human-flutter/references/) |
| **Core Intelligence** | [`core/`](core/) | [Developer Intelligence](core/developer-intelligence.md), [Task Orchestration](core/task-orchestration.md), [Operating Modes](core/operating-modes.md), [Human Interaction](core/human-interaction.md), [Project Knowledge](core/project-knowledge.md), [Git & Change Management](core/git-change-management.md), [Anti-Hallucination](core/anti-hallucination.md), [Recovery Protocol](core/recovery-protocol.md), [Architecture](core/architecture.md), [Folder Structure](core/folder-structure.md) |
| **Design System** | [`design/`](design/) | [Philosophy](design/design-philosophy.md), [Human Interface Design](design/human-interface-design.md), [Human Rules](design/human-design-rules.md), [Data Visualization](design/data-visualization.md), [Colors](design/color-system.md), [Typography](design/typography.md), [Spacing](design/spacing.md), [Responsive](design/responsive-design.md), [A11y](design/accessibility.md), [Motion](design/animation.md) |
| **Component Library** | [`components/`](components/) | [Principles](components/component-principles.md), [Shared Component Rubric](components/shared-component-rules.md), [Dashboards](components/dashboards.md), [Buttons](components/buttons.md), [Forms](components/forms.md), [Text Fields](components/text-fields.md), [Typography](components/typography.md), [Cards](components/cards.md), [Navigation](components/navigation.md), [Dialogs](components/dialogs.md), [Loading States](components/loading-states.md), [Component Testing](components/component-testing.md), [Reusable Widgets](components/reusable-widgets.md) |
| **Engineering** | [`engineering/`](engineering/) | [Code Standards](engineering/code-standards.md), [Debugging Engine](engineering/debugging-engine.md), [Clean Code](engineering/clean-code.md), [DevOps & Release](engineering/devops-release.md), [Architecture Patterns](engineering/architecture-patterns.md), [State Management](engineering/state-management.md), [Security](engineering/security.md), [Performance](engineering/performance.md), [Memory](engineering/memory-management.md), [Async Operations](engineering/async-operations.md), [Cross-Platform](engineering/cross-platform.md), [Error Handling](engineering/error-handling.md) |
| **Quality & Auditing** | [`quality/`](quality/) | [Testing Strategy](quality/testing-strategy.md), [Engineering Quality Gates](quality/engineering-quality-gates.md), [Testing](quality/testing.md), [UI Review Checklist](quality/ui-review.md), [Performance Audit](quality/performance-audit.md), [Accessibility Audit](quality/accessibility-audit.md), [Regression Prevention](quality/regression-prevention.md), [Bug Prevention](quality/bug-prevention.md), [Release Checklist](quality/release-checklist.md) |
| **Execution Workflows**| [`workflows/`](workflows/) | [Project Discovery](workflows/project-discovery.md), [Build Workflow](workflows/build.md), [New Project](workflows/new-project.md), [New Feature](workflows/new-feature.md), [New Page](workflows/new-page.md), [Shared Component](workflows/shared-component.md), [Redesign](workflows/redesign.md), [Debugging](workflows/debugging.md), [Recovery](workflows/recovery.md), [Refactoring](workflows/refactoring.md), [Performance Optimization](workflows/performance-optimization.md), [Release](workflows/release.md), [Security Audit](workflows/security-audit.md) |
| **Templates & ADRs** | [`templates/`](templates/), [`docs/adr/`](docs/adr/README.md) | [Project Context](templates/project-context.md), [ADR Template](templates/adr.md), [Test Plan](templates/test-plan.md), [Architecture Plan](templates/architecture-plan.md), [Design System](templates/design-system.md), [Task State](templates/task-state.md), [Bug Report](templates/bug-report.md), [Quality Report](templates/quality-report.md), [ADR Catalog](docs/adr/README.md) |

---

## 11. Agent Compatibility Notice

This repository defines standardized instructions consumable across AI development environments:
- **Google Antigravity**: [`.agents/skills/human-flutter/SKILL.md`](.agents/skills/human-flutter/SKILL.md) & [`.agent/skills/human-flutter/SKILL.md`](.agent/skills/human-flutter/SKILL.md)
- **Claude Code**: [`CLAUDE.md`](CLAUDE.md) & [`.claude/commands/human-flutter.md`](.claude/commands/human-flutter.md)
- **Gemini**: [`GEMINI.md`](GEMINI.md) & [`.agents/rules/human-flutter.md`](.agents/rules/human-flutter.md)
- **Cursor**: [`.cursor/rules/human-flutter.mdc`](.cursor/rules/human-flutter.mdc) & [`.cursor/skills/human-flutter/SKILL.md`](.cursor/skills/human-flutter/SKILL.md)
- **GitHub Copilot**: [`.github/copilot-instructions.md`](.github/copilot-instructions.md) & [`.github/prompts/human-flutter.prompt.md`](.github/prompts/human-flutter.prompt.md)
- **Windsurf**: [`.windsurf/rules/human-flutter.md`](.windsurf/rules/human-flutter.md) & [`.windsurf/workflows/human-flutter.md`](.windsurf/workflows/human-flutter.md)
