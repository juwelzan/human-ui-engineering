# Test Mode Reference (`/human-ui test`)

> **Autonomous Test Authoring, Execution & Proportional Verification**

When invoked with `/human-ui test [scope]`:

1. **Identify Test Targets**:
   - Locate untested critical paths, complex calculation algorithms, state transitions, or user flows.
2. **Select Testing Level**:
   - Pure logic & reducers -> **Unit Tests** (`.test.ts`, `_test.dart`).
   - Interactive widgets & accessibility -> **Component Tests** (`Testing Library`, `WidgetTester`).
   - HTTP routes & DB models -> **API / Integration Tests** (`supertest`).
   - End-to-end critical paths -> **E2E Tests** (`Playwright`, `Maestro`).
3. **Resilient Test Design**:
   - Test behavior, not implementation details.
   - Select UI elements using semantic roles and accessibility labels (`getByRole('button', { name: /submit/i })`).
   - Avoid brittle CSS class selectors or arbitrary test IDs where semantic roles exist.
4. **Execute & Report Honestly**:
   - Run the targeted test suite.
   - Report exact counts: PASSED, FAILED, SKIPPED, BLOCKED, NOT APPLICABLE.

