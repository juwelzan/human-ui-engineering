# Project Context Template

> **Standard template for initializing `PROJECT_CONTEXT.md` at repository roots.**

```markdown
# Project Context

> **System Identity, Core Invariants & Architecture Specifications**

- **Project Name**: [e.g., Acme Cloud Console]
- **Domain**: [e.g., Enterprise Cloud Resource Management]
- **Target Audience**: [e.g., DevOps engineers, system administrators]
- **Target Platforms**: [e.g., Web (Desktop/Mobile), Native iOS, Native Android]
- **Primary Tech Stack**: [e.g., Next.js 14, TypeScript, Tailwind CSS, PostgreSQL, Prisma]

---

## 1. High-Level System Architecture

[Brief 1-2 paragraph description of system architecture: presentation patterns (MVVM/Feature-first), backend runtimes, API contracts, database engines.]

---

## 2. Core Technical Invariants & Rules

- **Language & Runtime**: [e.g., Dart 3.x, sound null safety, strict lints in analysis_options.yaml]
- **State Management**: [e.g., BLoC / Cubit for feature state, Riverpod for reactive dependency state]
- **Design Tokens**: [e.g., 8pt spatial grid, ThemeData & ColorScheme, WCAG AA contrast]
- **Testing Standard**: [e.g., package:test for unit tests, WidgetTester for UI, integration_test for E2E flows]
- **Security Boundaries**: [e.g., FlutterSecureStorage for auth tokens, SSL pinning via Dio]

---

## 3. Directory Map & Package Boundaries

```text
lib/
├── core/            # Global foundational infrastructure (network, storage, theme tokens)
├── shared/          # Reusable cross-feature UI widgets, custom painters, animations
└── features/        # Feature-first domain modules (data, domain, presentation)
```

---

## 4. Active Design Token Conventions

- **Spacing Scale**: 4px (xs), 8px (sm), 16px (md), 24px (lg), 32px (xl), 48px (2xl).
- **Color Tokens**:
  - Primary: `theme.colorScheme.primary`
  - Surface: `theme.colorScheme.surface`
  - Semantic: `context.customColors.success`, `context.customColors.warning`
- **Typography**: Inter (`TextTheme.bodyMedium`, `TextTheme.titleLarge`).

---

## 5. Build, Test & CI Commands

- **Run Debug**: `flutter run`
- **Static Analysis**: `dart analyze`
- **Format Check**: `dart format --output=none --set-exit-if-changed .`
- **Test Suite**: `flutter test`
- **Release Build**: `flutter build appbundle --release` (or `flutter build web --release`)
```

