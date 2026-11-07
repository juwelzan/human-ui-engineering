# Clean Code Standards for UI Engineering

> Practical coding standards for readability, maintainability, naming discipline, and modularity in UI codebases.

---

## 1. Purpose

UI code evolves rapidly under changing product requirements. Without strict coding standards, components devolve into tangled, undocumented monstrosities where small visual tweaks trigger unexpected side effects. 

This guide defines the clean code standards enforced across all frameworks.

---

## 2. Component Size & Modularity

- **The 200-Line Guideline**: Strive to keep individual UI component files under 200 lines. If a file exceeds 250 lines, it is almost certainly doing too much:
  - Extract sub-widgets (e.g. `UserTableHeader`, `UserTableRow`, `UserActionsMenu`).
  - Extract complex business logic or validation into dedicated hooks, controllers, or helper modules.
- **Single Responsibility Principle (SRP)**: A component should render one distinct visual piece. Do not combine data fetching, complex data transformation, and 4 modal implementations in one file.

---

## 3. Naming Conventions

Consistent naming creates immediate cognitive clarity:

### 1. Boolean Variables & State Flags
Always prefix booleans with auxiliary verbs (`is`, `has`, `should`, `can`):
- **Good**: `isOpen`, `isLoading`, `hasError`, `canSubmit`, `shouldAutoFocus`
- **Bad**: `open`, `loading`, `error`, `submit`, `focus`

### 2. Event Callbacks & Handlers
Distinguish clearly between **callback parameters** and **handler methods**:
- **Callbacks (Declarative)**: Prefix with `on` (`onPressed`, `onSelectionChanged`, `onDismiss`).
- **Internal Handlers (Private)**: Prefix with `_handle` (`_handleTap`, `_handleSelectionChanged`, `_handleDismiss`).

### 3. Widget & File Names
- Use **PascalCase** for Flutter widget class definitions (`UserProfileCard`, `AppTextField`).
- Use **snake_case** for all Dart filenames (`user_profile_card.dart`, `app_text_field.dart`).
- Use domain-descriptive nouns, never generic names (`DashboardAnalyticsSummary` instead of `ContentBox2`).

---

## 4. Control Flow & Widget Tree Cleanliness

### Eliminate Nested Ternaries
Nested ternary operators inside Flutter widget trees are unreadable and error-prone:

```dart
// ❌ Anti-Pattern: Nested Ternaries inside build()
return Container(
  child: isLoading
      ? const AppSpinner()
      : hasError
          ? const AppErrorWidget()
          : data.isEmpty
              ? const AppEmptyState()
              : AppDataList(items: data),
);

// ✅ Clean Alternative: Dart 3 Exhaustive Pattern Matching
return switch (state) {
  DataLoading() => const AppSpinner(),
  DataError(:final message) => AppErrorWidget(message: message),
  DataSuccess(:final items) when items.isEmpty => const AppEmptyState(),
  DataSuccess(:final items) => AppDataList(items: items),
};
```

---

## 5. Explicit Typing & Widget Parameter Contracts

- Always declare explicit types for widget parameters. Never use `dynamic` or `Object` for UI data bindings.
- Differentiate between strictly required parameters (`required this.onPressed`) and optional overrides.
- Provide sensible default values for all optional configuration properties.

---

## 6. Preserving Existing Documentation & Code Integrity

- **Never delete unrelated comments or docstrings** when modifying files.
- Preserve the existing formatting, linting rules, and indentation conventions of the repository.
- Avoid introducing huge stylistic reformatting diffs in files where you only modified a few lines.

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- UI Architecture: [../core/architecture.md](../core/architecture.md)
- Architecture Patterns: [architecture-patterns.md](architecture-patterns.md)
- State Management: [state-management.md](state-management.md)

