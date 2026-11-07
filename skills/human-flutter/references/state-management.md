# Flutter State Management Engineering

> Architectural rules, selection heuristics, and rebuild scoping across BLoC, Riverpod, and Provider.

---

## 1. The Four Tiers of State

| State Tier | Scope | Typical Examples | Recommended Solution |
|---|---|---|---|
| **1. Ephemeral UI State** | Single widget | Password visibility toggle, animation progress, tab index | `setState`, `ValueNotifier`, `AnimationController` |
| **2. Feature State** | Single screen or flow | Checkout form validation, filter selections, active pagination | `Cubit`, `StateNotifier`, `AutoDisposeNotifier` |
| **3. App Global State** | Entire application | Authenticated user session, theme mode, shopping cart | `Bloc`, `Riverpod`, `ChangeNotifier` |
| **4. Server / Async State** | Cached remote data | Feed articles, user profile, notifications list | `AsyncValue` (Riverpod), `BlocBuilder` (BLoC) |

---

## 2. Solution Heuristics: BLoC vs Riverpod vs Provider

- **Respect Existing Codebases**: Never introduce Riverpod into a mature BLoC codebase or vice versa. Stick to the project's established pattern.
- **BLoC / Cubit**: Recommended when apps require strict event-driven auditing, explicit state transitions, and robust separation between business logic and UI.
- **Riverpod**: Recommended when apps benefit from compile-time safe dependency injection, auto-disposal of unused providers (`.autoDispose`), and seamless family parameterization.
- **Provider**: Traditional, lightweight dependency injection for simple applications.

---

## 3. Scoped Rebuilds & Anti-Patterns

### Anti-Pattern: Root-Level Rebuilds
```dart
// BAD: Calling setState() on the Scaffold State whenever a single checkbox toggles
onChanged: (val) => setState(() => isAgreed = val),
```

### Best Practice: Isolating Rebuilds with ValueListenableBuilder
```dart
// GOOD: Only this small checkbox tile rebuilds; Scaffold remains static
final ValueNotifier<bool> isAgreed = ValueNotifier(false);

ValueListenableBuilder<bool>(
  valueListenable: isAgreed,
  builder: (context, value, child) {
    return CheckboxListTile(
      value: value,
      onChanged: (v) => isAgreed.value = v ?? false,
      title: child, // Prebuilt child avoids rebuilds
    );
  },
  child: const Text('Agree to terms'),
)
```

---

## 4. State Cleanup & Disposal

Every state container holding stream subscriptions, timers, or network cancel tokens must dispose them when leaving the widget tree:
- In BLoC: Close sinks and cancel subscriptions in `Bloc.close()`.
- In Riverpod: Use `ref.onDispose(() => timer.cancel())`.
- In StatefulWidget: Cancel in `dispose()`.

---

## 5. Related References

- Architecture Patterns: [../../../engineering/architecture-patterns.md](../../../engineering/architecture-patterns.md)
- Flutter Architecture: [flutter-architecture.md](flutter-architecture.md)
- Performance: [performance.md](performance.md)
