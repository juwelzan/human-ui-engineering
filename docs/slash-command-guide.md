# Chat Slash Command Guide: `/human-flutter`

> **Comprehensive Command Manual for Invoking Human Flutter Engineering Across AI Coding Agents**

---

## 1. Overview

The `/human-flutter` slash command (or its alias `/human-ui`) provides direct access to the entire Human Flutter Engineering system from your agent's chat box.

```text
/human-flutter [subcommand?] [task_description]
```

When invoked, the skill:
1. Identifies the requested mode (`plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`).
2. Inspects your Flutter project (`pubspec.yaml`, dependencies, architecture).
3. Loads only the relevant modular Flutter reference documents from `skills/human-flutter/references/`.
4. Executes the task using professional Flutter/Dart engineering standards.
5. Verifies the result with `flutter test` and `dart analyze` and reports exact telemetry.

---

## 2. Complete Command Mode Catalog

| Mode | Invocation Syntax | Purpose & Action Taken |
|---|---|---|
| **General** | `/human-flutter [task]` | Full 18-step workflow: discovery, design tokens, shared widgets, layout, state binding, test. |
| **Plan** | `/human-flutter plan [task]` | Read-only task decomposition, dependency mapping, state modeling, and risk analysis. |
| **Build** | `/human-flutter build [task]` | End-to-end full-stack Flutter feature assembly (models, state holders, UI widgets, tests). |
| **Design** | `/human-flutter design [task]` | UI/UX visual hierarchy, 8pt spatial grid, typography scales, Material 3 / Cupertino styling. |
| **Color** | `/human-flutter color [task]` | Coherent 60-30-10 color palettes, `ColorScheme`, `ThemeExtension<AppCustomColors>`, WCAG AA. |
| **Component** | `/human-flutter component [task]` | Reusable widget primitives (`AppButton`, `AppCard`, `AppTextField`), `CustomPainter`, `RenderBox`. |
| **Responsive** | `/human-flutter responsive [task]`| Multi-screen layouts (Mobile, Tablet, Desktop, Web) with `LayoutBuilder` and zero overflows. |
| **Animation** | `/human-flutter animation [task]` | Meaningful, 60/120fps animations, `Hero`, `go_router` page transitions, and reduced motion. |
| **Performance** | `/human-flutter performance` | Frame budget (16.6ms/8.3ms), `const` optimization, `ListView.builder`, image downsampling. |
| **Platform** | `/human-flutter platform [task]` | `MethodChannel`, `EventChannel`, FFI, native permissions, lifecycle, and desktop window controls. |
| **Product** | `/human-flutter product [task]` | Auth, offline databases (Drift, Isar), Firebase, notifications, payments, and l10n. |
| **Audit** | `/human-flutter audit [scope]` | Comprehensive UI review, visual polish, layout overflow, accessibility, and rebuild audit. |
| **Debug** | `/human-flutter debug [issue]` | Scientific 10-step root-cause diagnosis (RenderFlex overflows, memory leaks, state crashes). |
| **Refactor** | `/human-flutter refactor [scope]` | Safe widget extraction, decomposing monolithic build methods (<200 lines), zero regressions. |
| **Test** | `/human-flutter test [scope]` | Multi-tier test authoring (Unit, Widget, Golden, Integration) with honest reporting. |
| **Review** | `/human-flutter review [scope]` | Pre-flight PR review against the 13 quality gates, analyzer cleanliness, and test pass rates. |
| **Release** | `/human-flutter release [scope]` | Android App Bundle (AAB), iOS IPA, code obfuscation, signing, and store readiness. |
| **Recovery** | `/human-flutter recover` | Inspects `AI_TASK_STATE.md` and git telemetry to resume interrupted workflows without restarting. |
| **Status** | `/human-flutter status` | Displays active task checkpoint, progress, milestone checklist, and known blockers. |

---

## 3. Concrete Command Examples

```text
# 1. Plan a multi-screen checkout flow without modifying code
/human-flutter plan Architect a 3-step payment wizard with In-App Purchase and BLoC.

# 2. Build full-stack feature with database models and UI
/human-flutter build Create offline task sync with Drift database, repository, and custom list tile.

# 3. Design accessible tokens and spacing
/human-flutter design Establish an 8pt spatial grid and semantic status colors for dark mode.

# 4. Create a reusable widget primitive
/human-flutter component Build a theme-aware AppButton with primary, secondary, and destructive variants.

# 5. Scientific Root-Cause Debugging
/human-flutter debug Resolve "A RenderFlex overflowed by 38 pixels on the bottom" when keyboard appears.

# 6. Animation Engineering
/human-flutter animation Add a smooth shared-element Hero transition between card and detail view.

# 7. Frame Drop & Memory Leak Optimization
/human-flutter performance Eliminate scroll jank in our 5,000-item customer list using ListView.builder.

# 8. Resume Interrupted Work
/human-flutter recover
```

---

## 4. Related Documentation

- Main Skill: [../skills/human-flutter/SKILL.md](../skills/human-flutter/SKILL.md)
- Compatibility Matrix: [compatibility-matrix.md](compatibility-matrix.md)
- Installation Guide: [installation-guide.md](installation-guide.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)
