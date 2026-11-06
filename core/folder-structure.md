# UI Folder Structure Conventions

> Standardized, scalable directory organization patterns for multi-platform UI codebases.

---

## 1. Purpose

Chaotic folder layouts lead to lost components, duplicated code, broken mental models, and circular dependencies. 

This guide defines standard folder structures that balance modular scalability with pragmatic simplicity.

---

## 2. Organization Philosophy: Feature-First vs. Layer-First

For small projects (< 5 screens), a **Layer-First** approach is acceptable:
```text
src/
├── components/
├── screens/
├── services/
└── utils/
```

For production applications (scalable, multi-developer), **Feature-First** is the mandatory standard:
```text
src/
├── core/                  # Cross-cutting utilities, base clients, design tokens
│   ├── theme/             # Colors, typography, spacing tokens
│   └── components/        # Universal shared UI primitives (buttons, inputs)
├── features/              # Self-contained business domains
│   ├── auth/              # Components, state, services isolated to auth
│   ├── dashboard/
│   └── settings/
└── app/                   # App entrypoint, routing, root providers
```

---

## 3. Co-Location Principle

Keep related assets, tests, and types close to where they are consumed. Rather than scattering files across separate root folders:

```text
// Highly Recommended: Co-located
features/profile/
├── components/
│   ├── ProfileAvatar.tsx
│   └── ProfileAvatar.test.tsx
├── hooks/
│   └── useProfileData.ts
├── ProfileScreen.tsx
├── ProfileScreen.test.tsx
└── types.ts
```

```text
// Discouraged: Dispersed across repo
src/views/ProfileScreen.tsx
src/tests/ProfileScreen.test.tsx
src/hooks/useProfileData.ts
src/types/profile.ts
```

---

## 4. Framework Reference Implementations

### A. React / Next.js (App Router)
```text
src/
├── app/                        # Next.js App Router routes & layouts
│   ├── layout.tsx
│   ├── page.tsx
│   └── dashboard/
│       └── page.tsx
├── components/                 # Global UI primitives (design system)
│   ├── ui/                     # Primitives (Button, Input, Modal, Badge)
│   └── feedback/               # Skeletons, ErrorBoundaries
├── features/                   # Domain features
│   └── analytics/
│       ├── components/
│       ├── hooks/
│       └── services/
├── lib/                        # Third-party wrappers (queryClient, supabase)
└── styles/                     # Tailwind or global CSS tokens
```

### B. Flutter
```text
lib/
├── core/
│   ├── theme/                  # AppColors, AppTypography, AppSpacing
│   ├── widgets/                # AppButton, AppTextField, AppCard
│   └── utils/
├── features/
│   └── authentication/
│       ├── data/               # Repositories, DTOs, data sources
│       ├── domain/             # Entities, use cases
│       └── presentation/       # Screens, controllers/cubits, feature widgets
│           ├── controllers/
│           ├── screens/
│           └── widgets/
└── main.dart
```

### C. Android (Jetpack Compose)
```text
app/src/main/java/com/example/app/
├── core/
│   ├── designsystem/           # Theme.kt, Color.kt, Type.kt, Component primitives
│   └── network/
├── features/
│   ├── feed/
│   │   ├── FeedScreen.kt
│   │   ├── FeedViewModel.kt
│   │   └── components/
│   └── settings/
└── MainActivity.kt
```

### D. iOS (SwiftUI)
```text
App/
├── Core/
│   ├── DesignSystem/           # Colors, Fonts, Spacing, Buttons, Cards
│   └── Networking/
├── Features/
│   ├── Checkout/
│   │   ├── Views/              # CheckoutView.swift, PaymentMethodRow.swift
│   │   ├── ViewModels/         # CheckoutViewModel.swift
│   │   └── Models/
├── Navigation/
└── AppEntry.swift
```

---

## 5. Directory Anti-Patterns

1. **The Junk Drawer (`utils/` or `helpers/` with 50 files)**: Dumping random unrelated helper functions in a single folder. Group by concern (e.g. `formatting/`, `validation/`, `date/`).
2. **Infinite Nesting**: Nesting folders 7-8 levels deep (`features/auth/presentation/views/components/buttons/primary/...`). Aim for a maximum depth of 3-4 levels within a feature.
3. **Duplicate Shared Folders**: Having both `components/`, `widgets/`, `elements/`, and `common/` at the root level. Pick one unified name (typically `components/` or `core/designsystem/`).

---

## 6. Related Documentation

- Master Instructions: [AGENTS.md](../AGENTS.md)
- Project Discovery: [project-discovery.md](project-discovery.md)
- UI Architecture: [architecture.md](architecture.md)
- Development Workflow: [development-workflow.md](development-workflow.md)

