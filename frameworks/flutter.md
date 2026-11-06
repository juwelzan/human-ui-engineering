# Flutter UI Engineering Guide

> Practical engineering guide for building production Flutter applications with high fidelity, 120fps performance, and clean architecture.

---

## 1. Recommended Project Structure

Follow a **Feature-First Clean Architecture** layout:

```text
lib/
├── core/
│   ├── theme/                  # AppColors, AppTypography, AppSpacing, AppTheme
│   ├── widgets/                # Shared primitives: AppButton, AppTextField, AppCard
│   ├── network/                # Dio / Http client, interceptors
│   └── utils/                  # Formatters, validators, extensions
├── features/
│   ├── auth/
│   │   ├── data/               # Repositories, DTOs, data sources
│   │   ├── domain/             # Entities, use cases
│   │   └── presentation/       # Screens, BLoC/Cubit/Notifier, feature widgets
│   │       ├── controllers/
│   │       ├── screens/
│   │       └── widgets/
│   └── dashboard/
└── main.dart
```

---

## 2. UI Architecture & Component Organization

- **Separate Views from Logic**: Never place network calls or business state inside `build()` methods.
- **Component Primitives**: Create reusable widgets with clear constructors and `const` support:
  - `AppButton.primary(...)`, `AppButton.secondary(...)`
  - `AppTextField(...)` with integrated `InputDecoration`
  - `AppCard(...)` with standardized padding and border radius
- **Widget Granularity**: Extract complex widget trees into small, dedicated private `StatelessWidget` classes rather than giant helper functions (`_buildHeader()` returning `Widget` is an anti-pattern because Flutter cannot optimize rebuilds).

---

## 3. State Management Guidance

- **Choose One Consistent Solution**: Respect the project's existing solution:
  - **BLoC / Cubit**: Best for large enterprise apps requiring strict event-driven separation.
  - **Riverpod**: Modern, type-safe, compile-time verified dependency injection and state management.
  - **Provider**: Traditional, lightweight dependency injection.
- **Selective Rebuilds**:
  - Always scope rebuilds using `BlocBuilder(buildWhen: ...)`, `Consumer(builder: ...)`, or `context.select(...)`.
  - Avoid calling `setState()` at the root screen widget when only an isolated counter or toggle changes.

---

## 4. Responsive Design & Layout

- Use `LayoutBuilder` to read available parent constraints rather than relying blindly on `MediaQuery.of(context).size`.
- Use `SafeArea` to respect device notches, Dynamic Island, and navigation bars.
- Prevent layout overflows (`RenderFlex overflowed by X pixels`):
  - In columns: Wrap scrollable content in `Expanded` + `SingleChildScrollView` or `ListView`.
  - In rows: Wrap flexible text in `Flexible` or `Expanded`.

---

## 5. Performance Optimization

1. **`const` Constructors Everywhere**: Mark every immutable widget with `const`. The compiler canonicalizes them and Flutter skips re-evaluating them during widget tree rebuilds.
2. **ListView.builder**: Never use `ListView(children: [...])` for long or dynamic collections. Always use `ListView.builder` or `CustomScrollView` with `SliverList` for lazy rendering.
3. **RepaintBoundary**: Wrap complex, continuously animating widgets in a `RepaintBoundary` to prevent repainting the entire screen canvas on every frame.
4. **Avoid Opacity Widget for Animations**: Animating `Opacity` forces expensive off-screen buffer allocation. Use `AnimatedOpacity` or `FadeTransition` instead.

---

## 6. Accessibility (A11y)

- Wrap custom interactive widgets in `Semantics()`:
  ```dart
  Semantics(
    button: true,
    label: 'Add to wishlist',
    onTap: () => handleTap(),
    child: CustomIconWidget(),
  )
  ```
- Use `ExcludeSemantics` on purely decorative artwork.
- Verify minimum touch targets using `kMinInteractiveDimension` (48x48 logical pixels).

---

## 7. Testing

- **Unit Tests**: Test repositories, use cases, and Cubits/Notifiers using `bloc_test` or `test`.
- **Widget Tests**: Test rendering and user interaction using `testWidgets`:
  ```dart
  testWidgets('AppButton shows spinner when loading', (tester) async {
    await tester.pumpWidget(MaterialApp(home: AppButton(isLoading: true, label: 'Save')));
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });
  ```

---

## 8. Common Mistakes to Avoid

1. **The `_buildSomething()` Function Anti-Pattern**: Writing helper functions returning widgets instead of creating separate `StatelessWidget` classes. Helper functions do not have their own `BuildContext` or element lifecycle and cause excessive parent rebuilds.
2. **Missing Controller Disposal**: Forgetting to call `dispose()` on `TextEditingController`, `AnimationController`, or `ScrollController`.
3. **Hardcoding Screen Heights**: Using `MediaQuery.of(context).size.height * 0.4` which clips when the keyboard opens.

---

## 9. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Flutter MCP Skills: Use available Flutter tools for analysis and tests.
- Master Instructions: [../AGENTS.md](../AGENTS.md)
