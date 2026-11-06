# Professional Coding Standards

> **Readability, Maintainability, Type Safety & Anti-Pattern Defenses**

Writing code like a senior human software engineer requires discipline. This guide defines non-negotiable coding standards and defense mechanisms against recurring software anti-patterns.

---

## 1. Core Engineering Principles

1. **Readability Over Cleverness**: Code is read 10 times more often than it is written. Avoid clever one-liners or esoteric language tricks when an explicit, well-named function is more understandable.
2. **Single Responsibility Principle (SRP)**: Each class, module, and component must have exactly one reason to change. Separate presentation rendering, state management, and data access.
3. **Strict Type Safety**: Never bypass type systems with `any`, `Object`, `dynamic`, or forced type casts (`as unknown as T`) to silence compiler warnings. Model data accurately using discriminated unions, sealed classes, or algebraic data types.
4. **Boundary Validation**: Validate inputs at the system perimeter (API controllers, form inputs, route parameters) and treat internal domain functions as trusted, typed contracts.
5. **Preserve Working Code**: **Never refactor working code merely to satisfy personal stylistic preferences.** Respect established patterns in the codebase.

---

## 2. Prevention of the 11 Lethal Code Anti-Patterns

```text
+----+----------------------------+-----------------------------------+-------------------------------------+
| #  | Anti-Pattern               | Dangerous Symptom                 | Professional Defense               |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 1  | Giant Files                | Single file exceeds 300-400 lines | Extract helper components, domain   |
|    |                            | with mixed concerns.              | hooks, or repository submodules.    |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 2  | Giant Components           | 1 component renders header, table,| Decompose into focused presentational|
|    |                            | modal, and handles 15 state vars. | primitives (Card, Row, Actions).   |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 3  | Excessive Parameters       | Functions taking > 4 positional   | Group related parameters into a     |
|    | (Parameter Creep)          | arguments (`fn(a, b, c, d, e)`).  | typed options object or config struct.|
+----+----------------------------+-----------------------------------+-------------------------------------+
| 4  | Duplicate Implementations  | Copy-pasting formatting or date   | Extract shared utility into         |
|    | (DRY Violations)           | parsing logic across 5 screens.   | `lib/utils/` or design tokens.      |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 5  | Premature Abstractions     | Creating complex generics or base | Follow the Rule of Three: duplicate |
|    |                            | classes before 3 distinct usages. | twice, abstract on the 3rd instance.|
+----+----------------------------+-----------------------------------+-------------------------------------+
| 6  | Unnecessary Dependencies   | Installing large npm/pub packages | Prefer standard library or minimal  |
|    |                            | for simple 10-line utilities.     | self-contained utility functions.   |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 7  | Dead Code                  | Commented-out blocks, unreachable | Remove dead code cleanly; rely on   |
|    |                            | branches, unused interfaces.      | Git history for preservation.       |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 8  | Unused Imports             | Lingering unused imports bloating | Run automated linter (`eslint --fix`|
|    |                            | bundles and triggering warnings.  | or `dart fix --apply`).             |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 9  | Unnecessary State          | Duplicating calculated values in  | Compute derived values on the fly   |
|    | (Derived State Desync)     | state (`fullName` from names).    | or leverage memoized selectors.     |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 10 | Hidden Side Effects        | Getters or render functions that  | Keep queries pure; trigger side     |
|    |                            | mutate state or dispatch network. | effects exclusively in event sinks. |
+----+----------------------------+-----------------------------------+-------------------------------------+
| 11 | Uncontrolled Global State  | Dumping ephemeral UI toggles into | Restrict global state to true app   |
|    |                            | root Redux or global singletons.  | globals (auth user, theme, locale). |
+----+----------------------------+-----------------------------------+-------------------------------------+
```

---

## 3. Naming Conventions & Semantics

- **Booleans**: Prefix with auxiliary verbs: `isActive`, `hasPermission`, `isLoading`, `canSubmit`, `shouldRefresh`.
- **Functions**: Use verb-noun pairings describing the action: `fetchUserProfile()`, `validateBillingForm()`, `calculateTax()`.
- **Event Handlers**:
  - Declaration / Callback prop: `onUserSelect`, `onSubmit`, `onDismiss`.
  - Implementation function: `handleUserSelect`, `handleSubmit`, `handleDismiss`.
- **Constants & Enums**: Use uppercase screaming snake case for immutable configuration values (`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`).

---

## 4. Error Handling & Defense in Depth

1. **Fail Fast**: Check preconditions and throw or return early before performing expensive work:
   ```typescript
   if (!userId) {
     throw new InvalidArgumentError('userId is required');
   }
   ```
2. **Never Swallow Errors**:
   ```typescript
   // UNACCEPTABLE:
   try { doSomething(); } catch (e) {}

   // PROFESSIONAL:
   try {
     doSomething();
   } catch (error) {
     logger.error('Failed to execute critical sync', { error, context: { userId } });
     throw new ServiceUnavailableException('Sync service unreachable', { cause: error });
   }
   ```
