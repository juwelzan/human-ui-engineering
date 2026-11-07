# 0002: Transform into a Complete Flutter-Only Engineering System

- **Status**: **Accepted**
- **Date**: 2026-11-07
- **Deciders**: AI Engineering System Architecture Team

---

## 1. Context & Problem Statement

Previously, `human-ui-engineering` attempted to serve as a universal, multi-framework software engineering system spanning 13 disparate web, mobile, desktop, and backend frameworks (React, Next.js, Vue, Angular, React Native, Native Android, Native iOS, Web, Desktop, Node.js, Go, etc.).

This broad scope created significant drawbacks:
- Unnecessary complexity and cognitive bloat across multi-framework guides.
- Inability to provide the deepest, high-fidelity Flutter & Dart engineering intelligence (such as Material 3 `ColorScheme`, custom `ThemeExtension`, `CustomPainter`, `RenderBox`, sound null safety in Dart 3, `go_router`, Drift, BLoC, and Riverpod).
- AI coding agents occasionally suggested or mixed incompatible frontend frameworks into Flutter projects.

## 2. Decision Drivers

- **Specialization & Deep Quality**: Focus exclusively on Flutter and Dart to provide deep, senior-level Flutter intelligence.
- **Strict Architecture Integrity**: Enforce an Absolute Flutter-Only Rule that eliminates framework switching or contamination.
- **Antigravity Optimization**: Provide first-class Antigravity workspace skill discovery via `.agents/skills/human-flutter/SKILL.md`.

## 3. Considered Options

1. **Keep Multi-Framework System**: Maintain 13 isolated frameworks. Rejected due to superficial coverage and risk of framework mixing.
2. **Transform into a Complete Flutter-Only Human UI Engineering System**: Eliminate unrelated frameworks, remove `frameworks/`, build a comprehensive 26-module Flutter skill architecture (`skills/human-flutter/`), and ground the entire repository in Flutter and Dart. **(Chosen)**

## 4. Decision Outcome

Adopt Option 2: Transform `human-ui-engineering` into an exclusive, complete Flutter & Dart engineering system.

### Positive Consequences
- Deep, specialized guidance for Flutter UI design, color intelligence, component primitives, Dart 3 standards, responsive design, animations, 120fps performance, platform channels, and store deployment.
- Zero risk of AI agents recommending non-Flutter alternatives.
- Simplified repository structure without extraneous framework modules.
- Complete automated validation enforcing Flutter-only isolation (`scripts/validate-flutter-only`).

### Negative Consequences
- Non-Flutter projects can no longer use this repository as a universal reference.
