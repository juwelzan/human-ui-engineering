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

- **Language & Runtime**: [e.g., TypeScript 5.4, strict mode enabled, no explicit `any`]
- **State Management**: [e.g., TanStack Query for server state, Zustand for client modal state]
- **Design Tokens**: [e.g., 8pt spatial grid, Tailwind semantic color tokens, WCAG AA contrast]
- **Testing Standard**: [e.g., Vitest for unit tests, Playwright for E2E user flows]
- **Security Boundaries**: [e.g., HttpOnly secure cookies for auth, zero secrets in client bundles]

---

## 3. Directory Map & Package Boundaries

```text
src/
├── app/             # Next.js App Router pages and layouts
├── components/      # Shared presentation primitives (Button, Card, Modal)
├── features/        # Domain features (auth, billing, metrics)
├── lib/             # Shared utilities, database client, API clients
└── types/           # Global TypeScript definitions
```

---

## 4. Active Design Token Conventions

- **Spacing Scale**: 4px (xs), 8px (sm), 16px (md), 24px (lg), 32px (xl), 48px (2xl).
- **Color Tokens**:
  - Primary: `var(--color-primary-600)`
  - Surface: `var(--color-surface)`
  - Semantic: `var(--color-success)`, `var(--color-warning)`, `var(--color-danger)`
- **Typography**: Inter (Body), JetBrains Mono (Code/Telemetry).

---

## 5. Build, Test & CI Commands

- **Local Dev Server**: `npm run dev`
- **Type Check**: `npm run typecheck`
- **Lint**: `npm run lint`
- **Test Suite**: `npm test`
- **Build**: `npm run build`
```

