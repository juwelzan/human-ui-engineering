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

### 2. Event Handlers & Callbacks
Distinguish clearly between **callback props** and **handler implementations**:
- **Props (Declarative)**: Prefix with `on` (`onClick`, `onSelectionChange`, `onDismiss`).
- **Internal Handlers (Imperative)**: Prefix with `handle` (`handleClick`, `handleSelectionChange`, `handleDismiss`).

### 3. Component & File Names
- Use **PascalCase** for component definitions and filenames (`UserProfileCard.tsx`, `app_text_field.dart`, `ProfileHeader.kt`).
- Use domain-descriptive nouns, never generic names (`DashboardAnalyticsSummary` instead of `ContentBox2`).

---

## 4. Control Flow & JSX / Template Cleanliness

### Eliminate Nested Ternaries
Nested ternary operators inside templates are unreadable and error-prone:

```tsx
// Anti-Pattern: Nested Ternary Nightmare
return (
  <div>
    {isLoading ? (
      <Spinner />
    ) : hasError ? (
      <ErrorMessage />
    ) : data.length === 0 ? (
      <EmptyState />
    ) : (
      <DataList items={data} />
    )}
  </div>
);

// Clean Alternative: Early returns or declarative state branching
if (isLoading) return <Spinner />;
if (hasError) return <ErrorMessage />;
if (data.length === 0) return <EmptyState />;

return <DataList items={data} />;
```

---

## 5. Explicit Typing & Prop Contracts

- Always declare explicit types/interfaces for component props. Never use `any` (TypeScript) or `dynamic` (Dart) for UI data bindings.
- Differentiate between strictly required parameters and optional overrides.
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
