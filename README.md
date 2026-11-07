# Human Flutter Engineering

> **Permission-First, Human-Centered Flutter & Dart Engineering Operating System & AI Agent Intelligence**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework: Flutter Only](https://img.shields.io/badge/Framework-Flutter%20%26%20Dart%20Only-02569B.svg)](AGENTS.md)
[![Protocol: Permission--First](https://img.shields.io/badge/Protocol-Permission--First%20(Bengali)-059669.svg)](skills/human-flutter/references/permission-system.md)
[![Architecture: Core--Shared--Features](https://img.shields.io/badge/Architecture-Core%2FShared%2FFeatures-blueviolet.svg)](skills/human-flutter/references/project-structure.md)
[![A11y: WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-purple.svg)](design/accessibility.md)
[![Chat Slash Command: /human-flutter](https://img.shields.io/badge/Slash%20Command-%2Fhuman--flutter-orange.svg)](docs/slash-command-guide.md)

---

## 1. What is Human Flutter Engineering?

**Human Flutter Engineering** is a dedicated, Flutter-only knowledge and instruction system that teaches AI coding agents to think, architect, design, and code like senior human Flutter engineers.

Rather than generating generic "AI aesthetics" (unwarranted purple/teal glows, repetitive card grids, arbitrary glassmorphism, and unmaintainable monolithic files), this repository instills rigorous engineering standards:

- **Permission-First in Bengali (Highest Priority)**: Agents never make major architectural, state management, dependency, color, or structural decisions without explaining the options, pros/cons, and recommendations in natural Bengali and waiting for explicit user permission.
- **Absolute Flutter-Only Focus**: Strictly and exclusively dedicated to Flutter and Dart. Never suggests or generates alternative frontend frameworks.
- **Mandatory 3-Tier Architecture**: All generated projects strictly follow `lib/core/` (foundations), `lib/shared/` (reusable UI), and `lib/features/` (feature-first modules).
- **Mandatory 3–4 Color Selection & Visual Preview**: Users choose 3 or 4 primary colors, followed by a mandatory 12-component visual UI color board preview before theme finalization.
- **Human Utility Over AI Decoration**: Prioritizes content hierarchy, readability, and user task completion.
- **Deterministic Quality**: Enforces strict verification of 120fps performance, accessibility, memory disposal, and responsiveness.

The single source of truth for all agent operations is [`AGENTS.md`](AGENTS.md).

---

## 2. Direct Chat Slash Command: `/human-flutter`

Developers can invoke Human Flutter Engineering directly from their AI agent's chat input:

```text
/human-flutter [subcommand?] [task_description]
```
*(The alias `/human-ui` is also supported).*

### Example Invocations
```text
# 1. General Flutter feature engineering (executes the 18-step workflow)
/human-flutter Create a modern, accessible customer profile screen.

# 2. Plan mode: structured task planning & Bengali permission gates
/human-flutter plan Architect a 3-step checkout flow with In-App Purchases.

# 3. Build mode: end-to-end full-stack Flutter feature assembly in lib/features/
/human-flutter build Implement offline note syncing with Drift database and BLoC.

# 4. Design mode: UI/UX design, visual hierarchy & layout
/human-flutter design Establish a clean information architecture for our dashboard.

# 5. Color mode: 3-4 color prompt, visual placement preview & ThemeData
/human-flutter color Define a Material 3 ColorScheme with custom ThemeExtension for status colors.

# 6. Component mode: reusable widget primitives in lib/shared/
/human-flutter component Build a theme-aware AppButton with primary, secondary, and destructive variants.

# 7. Responsive mode: multi-breakpoint layouts across mobile, tablet, desktop, web
/human-flutter responsive Adapt our data table to stack cleanly on mobile viewports.

# 8. Animation mode: meaningful, 60/120fps animations & micro-interactions
/human-flutter animation Add a smooth shared-element Hero transition between card and detail view.

# 9. Performance mode: frame budget, const optimization & DevTools profiling
/human-flutter performance Eliminate jank and memory leaks during infinite list scrolling.

# 10. Platform mode: MethodChannel, EventChannel, FFI & native permissions
/human-flutter platform Implement native biometric authentication via local_auth.

# 11. Product mode: Auth, offline storage, Firebase & internationalization
/human-flutter product Configure Firebase Crashlytics with uncaught FlutterError handlers.

# 12. Audit mode: visual polish, contrast, a11y & layout audit
/human-flutter audit lib/features/checkout

# 13. Debug mode: scientific 10-step root-cause diagnosis
/human-flutter debug Resolve "A RenderFlex overflowed by 38 pixels on the bottom".

# 14. Refactor mode: safe widget extraction & state decoupling
/human-flutter refactor Decompose giant 600-line OrderDashboard into focused private StatelessWidget classes.

# 15. Test mode: unit, widget, and integration test authoring
/human-flutter test Add widget tests for BillingSummary asserting loading, empty, and success states.

# 16. Review mode: pre-flight PR review against the 13 quality gates
/human-flutter review Audit our recent PR changes before merging.

# 17. Release mode: AAB/IPA release preparation, signing & obfuscation
/human-flutter release Prepare Android App Bundle with code obfuscation and debug symbols.

# 18. Recovery Mode: resume interrupted work without restarting
/human-flutter recover

# 19. Status Mode: inspect active task state and blockers
/human-flutter status
```

👉 Read the full [Chat Slash Command Guide](docs/slash-command-guide.md) and [Compatibility Matrix](docs/compatibility-matrix.md).

---

## 3. Supported AI Coding Agents

This repository provides standardized, lightweight entry points for all major AI coding environments:

| Agent / Tool | Entry File | Chat Invocation Syntax | Autocomplete | Auto-Activation | Notes |
|---|---|---|---|---|---|
| **Google Antigravity** | [`.agents/skills/human-flutter/`](.agents/skills/human-flutter/SKILL.md) | `/human-flutter [task]` | **YES** | **YES** | Native workspace skill integration |
| **Claude Code** | [`.claude/commands/human-flutter.md`](.claude/commands/human-flutter.md) | `/human-flutter [task]` | **YES** | **YES** | CLI slash command |
| **Gemini CLI / IDE** | [`GEMINI.md`](GEMINI.md) | `/human-flutter [task]` | **YES** | **YES** | Agent Skills standard |
| **Cursor** | [`.cursor/rules/human-flutter.mdc`](.cursor/rules/human-flutter.mdc) | `/human-flutter [task]` or `@human-flutter` | **YES** | **YES** | Rules & symbol picker |
| **VS Code Copilot** | [`.github/prompts/human-flutter.prompt.md`](.github/prompts/human-flutter.prompt.md) | `/human-flutter [task]` | **YES** | **YES** | Reusable prompt file |
| **Windsurf** | [`.windsurf/workflows/human-flutter.md`](.windsurf/workflows/human-flutter.md) | `/human-flutter [task]` | **YES** | **YES** | Cascade workflow |

👉 Read the complete [Compatibility Matrix](docs/compatibility-matrix.md) and [Installation Guide](docs/installation-guide.md).

---

## 4. Complete Reference Library (28 Modules)

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

## 5. Repository Architecture

```text
human-ui-engineering/
├── README.md               # Overview, slash commands, and setup guide
├── AGENTS.md               # Master instructions (Single Source of Truth)
├── PROJECT_CONTEXT.md      # Stable system identity and invariants
├── AI_TASK_STATE.md        # Active task checkpoint & recovery tracker
├── CHANGELOG.md            # Version release milestones & roadmap
├── CLAUDE.md               # Claude Code entry point
├── GEMINI.md               # Gemini agent entry point
├── CONTRIBUTING.md         # Contribution standards (Flutter-only policy)
├── LICENSE                 # MIT License
│
├── skills/human-flutter/   # Canonical Agent Skill Engine
│   ├── SKILL.md            # Main skill with YAML frontmatter
│   └── references/         # 28 modular Flutter engineering reference guides
│
├── docs/                   # User guides & matrices
│   ├── compatibility-matrix.md # Verified agent support matrix
│   ├── slash-command-guide.md  # Detailed /human-flutter command manual
│   ├── installation-guide.md   # Step-by-step installation instructions
│   └── adr/                # Architecture Decision Records (ADRs)
│
├── .github/                # GitHub-specific instructions
│   ├── copilot-instructions.md
│   ├── prompts/human-flutter.prompt.md
│   └── workflows/validate.yml  # GitHub Actions CI validator
│
├── .cursor/                # Cursor IDE configuration
│   ├── rules/human-flutter.mdc
│   └── skills/human-flutter/
│
├── .agents/                # Google Antigravity & Agent OS (Canonical)
│   ├── rules/human-flutter.md
│   └── skills/human-flutter/
│
├── .agent/                 # Agent configuration (Fallback)
│   ├── rules/human-flutter.md
│   └── skills/human-flutter/
│
├── .claude/commands/       # Claude Code slash commands
│   └── human-flutter.md
│
├── .windsurf/              # Windsurf Cascade configuration
│   ├── rules/human-flutter.md
│   └── workflows/human-flutter.md
│
├── core/                   # Flutter engineering intelligence & orchestration
├── design/                 # Human-centered UI design system, colors & typography
├── components/             # Reusable shared widget component engineering
├── engineering/            # Production Flutter engineering standards & clean code
├── quality/                # Quality assurance, testing pyramid & pre-flight gates
├── workflows/              # Step-by-step Flutter execution workflows
├── templates/              # Fillable engineering templates (ADRs, task state, bug reports)
└── scripts/                # Automated validation suite (docs, links, structure, flutter-only)
```

---

## 6. Verification Commands

```bash
# Run full automated validation suite (docs, links, structure, flutter-only)
python3 scripts/validate.py
```
