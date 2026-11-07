# Autonomous Testing Strategy & Verification Protocol

> **Unit, Component, Integration, API, E2E, Regression & Honest Reporting Standards**

Automated testing is the only objective proof that software behaves correctly. AI coding agents must apply targeted, proportional test strategies for every modification and report honest test results without fabrication.

---

## 1. The Autonomous Testing Pyramid

```mermaid
flowchart TD
    E2E[End-to-End Tests: Critical User Journeys - Cypress/Playwright/Patrol] --> Int[Integration & API Tests: Endpoints, Database, Supertest/Postman]
    Int --> Comp[Component / Widget Tests: Rendering, Interaction, Accessibility]
    Comp --> Unit[Unit Tests: Pure Logic, Reducers, Services, Calculations]
```

| Test Layer | Focus & Target | Execution Speed | Framework Tooling |
|---|---|---|---|
| **Unit Tests** | Pure functions, domain calculations, utilities, business rules | Milliseconds | Vitest, Jest, `test` (Dart), PyTest, JUnit 5, Go test |
| **Component Tests** | UI rendering, user interaction, state transitions, accessibility | Seconds | React Testing Library, Flutter WidgetTester, Compose UI Test |
| **API / Integration** | HTTP controllers, database transactions, middleware, auth | Seconds | Supertest, Testcontainers, Ktor Test, Httptest (Go) |
| **End-to-End (E2E)** | Full user journeys across real browsers / devices | Minutes | Playwright, Cypress, Maestro, Patrol, Appium |
| **Regression Tests** | Exact reproduction of previously fixed defects | Milliseconds–Seconds | Integrated into standard unit/component suite |

---

## 2. Proportional Test Selection Rule

> [!IMPORTANT]
> **Do Not Run the Entire Test Suite for Simple Changes**:
> Scope test execution to the blast radius of your changes:
> - **Edited utility / repository**: Run the targeted unit test file (`flutter test test/core/utils/formatters_test.dart`).
> - **Edited UI widget**: Run the targeted widget test (`flutter test test/core/widgets/app_button_test.dart`).
> - **Edited state holder**: Run the Cubit/Notifier test (`flutter test test/features/auth/auth_cubit_test.dart`).
> - **Full release / pre-flight**: Run the complete suite (`flutter test`).

---

## 3. Post-Modification Verification Sequence

After every code edit, execute this 4-step verification gate:

```mermaid
flowchart LR
    F[1. Format] --> S[2. Static Analysis]
    S --> T[3. Targeted Tests]
    T --> B[4. Build Verification]
```

1. **Format**: Format Dart files cleanly (`dart format .`).
2. **Static Type Analysis**: Verify zero errors or warnings (`dart analyze`).
3. **Targeted Tests**: Run relevant unit or widget tests (`flutter test <path_to_test>`).
4. **Build Verification**: Run release build verification if dependencies or exports were altered (`flutter build appbundle` or `flutter build web`).

---

## 4. Honest Test Status Reporting Standard

When reporting test outcomes, AI agents MUST use these standardized statuses:

- **PASSED**: Command executed with exit code 0; all assertions confirmed green.
- **FAILED**: Command executed with non-zero exit code or assertion failure (quote exact error).
- **SKIPPED**: Test suite was intentionally bypassed (state explicit justification).
- **BLOCKED**: Test could not be run due to missing environment, simulator, or credentials.
- **NOT APPLICABLE**: Change does not impact executable logic (e.g., Markdown documentation).

```markdown
### Verification Summary
- Static Analysis (`dart analyze`): **PASSED** (0 errors, 0 warnings)
- Unit Tests (`flutter test test/features/cart/cart_cubit_test.dart`): **PASSED** (8 passed, 0 failed)
- Integration Tests: **BLOCKED** (No connected mobile simulator on port 5554)
- E2E Tests: **SKIPPED** (Proportional scope for minor cart logic patch)
```

