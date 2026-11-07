# Project Decision Memory

> **System of Record** for architectural, state management, dependency, color, and design decisions approved via the Permission-First Bengali Protocol.

---

## 1. Project Identity & Metadata

- **Project Name**: [e.g. Acme Mobile App]
- **Initialized Date**: [YYYY-MM-DD]
- **Target Platforms**: [iOS / Android / Web / Desktop]
- **Flutter SDK Constraint**: [e.g. `>=3.24.0 <4.0.0`]
- **Primary Architecture**: Presentation-Domain-Data Clean Architecture (`lib/core/`, `lib/shared/`, `lib/features/`)

---

## 2. Active Architectural & Design Decisions

| ID | Date | Category | Decision | Status | Rationale / Approved By |
|---|---|---|---|---|---|
| DEC-001 | YYYY-MM-DD | State Management | [e.g. flutter_bloc + cubit] | APPROVED | [Structured event-driven state flow] |
| DEC-002 | YYYY-MM-DD | Routing | [e.g. go_router] | APPROVED | [Declarative routing with deep link support] |
| DEC-003 | YYYY-MM-DD | Color Palette | [e.g. 4-Color Corporate] | APPROVED | [Primary: #1E3A8A, Secondary: #0D9488, Neutral: #F8FAFC, Accent: #F59E0B] |
| DEC-004 | YYYY-MM-DD | Database / Storage | [e.g. Drift SQLite] | APPROVED | [Type-safe SQL queries with schema migrations] |
| DEC-005 | YYYY-MM-DD | Network Client | [e.g. Dio + SSL Pinning] | APPROVED | [Interceptors, retry backoff, certificate validation] |

---

## 3. Rejected & Prohibited Technologies / Patterns

| ID | Date | Category | Proposed Option | Status | Reason for Rejection |
|---|---|---|---|---|---|
| REJ-001 | YYYY-MM-DD | State Management | GetX | REJECTED | Avoid hidden global context dependencies and tight coupling |
| REJ-002 | YYYY-MM-DD | Storage | Raw SharedPreferences for Tokens | REJECTED | Insecure; tokens must be stored in FlutterSecureStorage |

---

## 4. Pending Architectural Inquiries

| ID | Date | Category | Question Presented | Options Under Consideration | Status |
|---|---|---|---|---|---|
| PEN-001 | YYYY-MM-DD | Analytics | Choice of telemetry provider | Firebase Analytics vs PostHog | PENDING |

---

## 5. Global Developer Preferences

- **Dart Style**: Sound null safety, exhaustive pattern matching with Dart 3 switch expressions.
- **Component Rules**: Max 200 lines per build method; extract complex subtrees into private `StatelessWidget`s.
- **Error Handling**: Functional `Result<T, Failure>` pattern, never throw uncaught exceptions in presentation layers.
- **Color Selection**: Always enforce the 3–4 color prompt and 12-component visual placement preview before theming.
