# Flutter Framework Reference

> Framework-specific guidance for Flutter development within the `/human-ui` skill.

---

## 1. Quick Flutter Directives

- **Clean Architecture**: Isolate `presentation/` from `domain/` and `data/`.
- **`const` Constructors**: Mark all immutable widgets with `const` to skip rebuild cycles.
- **Granular Widgets**: Extract small `StatelessWidget` classes instead of `_buildWidget()` helper functions.
- **List Virtualization**: Always use `ListView.builder` or `CustomScrollView` for dynamic collections.
- **Lifecycle Cleanup**: Explicitly call `dispose()` on `TextEditingController`, `AnimationController`, and cancel `StreamSubscription`s.
- **Accessibility**: Wrap custom interactive elements in `Semantics(button: true, label: '...')`.

---

## 2. In-Depth Documentation Links

- Complete Flutter Guide: [../../../frameworks/flutter.md](../../../frameworks/flutter.md)
- Shared Component Rules: [../../../components/shared-component-rules.md](../../../components/shared-component-rules.md)
- Buttons Specification: [../../../components/buttons.md](../../../components/buttons.md)

