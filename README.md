# Human Flutter Engineering

> **Complete Flutter-Only Human UI Engineering Operating System & AI Agent Intelligence**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework: Flutter Only](https://img.shields.io/badge/Framework-Flutter%20%26%20Dart%20Only-02569B.svg)](AGENTS.md)
[![A11y: WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-purple.svg)](design/accessibility.md)
[![Chat Slash Command: /human-flutter](https://img.shields.io/badge/Slash%20Command-%2Fhuman--flutter-orange.svg)](docs/slash-command-guide.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 1. What is Human Flutter Engineering?

**Human Flutter Engineering** is a dedicated, Flutter-only knowledge and instruction system that teaches AI coding agents to think, architect, design, and code like senior human Flutter engineers.

Rather than generating generic "AI aesthetics" (unwarranted purple/teal glows, repetitive card grids, arbitrary glassmorphism, and unmaintainable 800-line monolithic files), this repository instills rigorous engineering standards:
- **Absolute Flutter-Only Focus**: Strictly and exclusively dedicated to Flutter and Dart. Never suggests, generates, or mixes alternative frontend or cross-platform frameworks.
- **Human Utility Over AI Decoration**: Prioritizes content hierarchy, readability, and user task completion.
- **Foundation-First Architecture**: Establishes design tokens and shared component primitives (`AppButton`, `AppCard`, `AppTextField`) before assembling screens.
- **Platform Authenticity**: Respects native idioms across Android, iOS, macOS, Windows, Linux, and Flutter Web.
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

# 2. Plan mode: structured task planning & dependency mapping
/human-flutter plan Architect a 3-step checkout flow with In-App Purchases.

# 3. Build mode: end-to-end full-stack Flutter feature assembly
/human-flutter build Implement offline note syncing with Drift database and BLoC.

# 4. Design mode: UI/UX design, visual hierarchy & layout
/human-flutter design Establish a clean information architecture for our dashboard.

# 5. Color mode: coherent color palettes, ThemeData & ColorScheme
/human-flutter color Define a Material 3 ColorScheme with custom ThemeExtension for status colors.

# 6. Component mode: reusable widget primitives & CustomPainter
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

## 4. The 10 Core Flutter Engineering Modules

1. **[Human UI Design Engineering](skills/human-flutter/references/ui-design.md)**: Information architecture, Material 3, Cupertino, custom interfaces, and complete interaction states.
2. **[Human Color Intelligence](skills/human-flutter/references/color-system.md)**: 60-30-10 palette balance, `ColorScheme`, `ThemeExtension<AppCustomColors>`, and WCAG 2.1 AA contrast.
3. **[Human Flutter Component Engineering](skills/human-flutter/references/components.md)**: Reusable widget primitives (`AppButton`, `AppCard`, `AppTextField`), `CustomPainter`, and `RenderBox`.
4. **[Human Flutter Coding Intelligence](skills/human-flutter/references/dart-standards.md)**: Clean Dart 3 standards, records, pattern matching, sealed classes, sound null safety, and UDF.
5. **[Human Flutter File Structure Engineering](skills/human-flutter/references/file-structure.md)**: Feature-First architecture, clean layer separation, core isolation, and test mirroring.
6. **[Human Responsive Design Engineering](skills/human-flutter/references/responsive-design.md)**: Multi-platform layouts (Mobile, Tablet, Desktop, Web), `LayoutBuilder`, and zero overflow bugs.
7. **[Human Flutter Animation Engineering](skills/human-flutter/references/animation.md)**: Implicit/explicit animations, `Hero`, page transitions, and 120fps frame budgets.
8. **[Human Performance Engineering](skills/human-flutter/references/performance.md)**: `const` optimization, `ListView.builder`, image downsampling, isolates (`compute`), and DevTools profiling.
9. **[Human Flutter Platform Engineering](skills/human-flutter/references/platform-integration.md)**: `MethodChannel`, `EventChannel`, FFI, permissions, lifecycle, and desktop window management.
10. **[Human Flutter Product Engineering](skills/human-flutter/references/api-integration.md)**: API integration via Dio, offline databases (Drift, Isar), Firebase, notifications, and store release.

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
│   └── references/         # 26 modular Flutter engineering reference guides
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
