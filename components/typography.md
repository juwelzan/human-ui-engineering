# Typography Components & Text Primitives

> Component API design, polymorphic rendering, truncation, and semantic hierarchy for text primitives.

---

## 1. Purpose

Hardcoding arbitrary typography classes (e.g. `text-xl font-bold text-gray-800` or raw `Text(style: ...)` widgets) across hundreds of view files causes inconsistent styling and visual drift. 

This guide defines the engineering standard for reusable typography components.

---

## 2. Decoupling Visual Style from Screen Reader Semantics

A critical principle of accessible Flutter UI engineering is separating **visual style** from **assistive accessibility semantics**:
- A heading might require the **visual size** of a compact `titleMedium` due to tight card constraints, but need to announce itself as an explicit section header for TalkBack / VoiceOver screen readers.
- In Flutter, wrap text primitives with the `Semantics` widget or use semantic label flags:

```dart
// Flutter Example: Visual titleMedium styling with explicit assistive header semantics
Semantics(
  header: true,
  child: Text(
    'Account Settings',
    style: Theme.of(context).textTheme.titleMedium?.copyWith(
      fontWeight: FontWeight.w600,
    ),
  ),
);
```

---

## 3. Recommended Typography Primitives

Create a focused set of reusable typography primitives in `lib/shared/widgets/text/`:

| Component Primitive | Material 3 Style Role | Semantic Behavior | Typical Usage |
|---|---|---|---|
| `AppHeading` | `headlineLarge` / `headlineMedium` | `Semantics(header: true)` | Screen titles, hero metrics |
| `AppSubheading` | `titleLarge` / `titleMedium` | `Semantics(header: true)` | Card headers, section dividers |
| `AppBodyText` | `bodyLarge` / `bodyMedium` | Default text node | Paragraphs, descriptions |
| `AppLabel` | `labelLarge` / `labelSmall` | `Semantics(label: ...)` | Buttons, badges, timestamps |
| `AppCodeText` | Custom Monospace `TextStyle` | Font: Fira Code / JetBrains | API keys, transaction IDs |

---

## 4. Text Truncation & Line Clamping

Long strings (names, URLs, descriptions) must never break layouts or overflow their containers.

### Single-Line Truncation
- Use standard ellipsis truncation for titles and table cells:
```css
.truncate-single {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```
> [!IMPORTANT]
> If a parent flex container wraps the truncated text, ensure `min-width: 0` is set on the flex item; otherwise, the flex child will expand to its unconstrained content width and push other elements off-screen.

### Multi-Line Clamp
- For previews and descriptions, use multi-line clamp (e.g. 2 or 3 lines):
```css
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

### Full Text Preservation
Whenever text is truncated, ensure the full string is accessible via a native `Tooltip(message: fullText, child: Text(...))` or screen reader `Semantics(label: fullText)`.

---

## 5. Typography Anti-Patterns

1. **Semantic Flattening**: Rendering all page titles as plain unannotated text without semantic heading roles (`Semantics(header: true)`), destroying screen reader document outline navigation.
2. **Missing TextScaler Clamp**: Failing to handle OS-level font enlargement, causing `RenderFlex` overflow errors on mobile devices.
3. **Uncapped Line Lengths**: Allowing `Text` to stretch across 1400px of screen real estate. Always constrain reading width with a `ConstrainedBox(constraints: BoxConstraints(maxWidth: 700))`.

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Typography Design System: [../design/typography.md](../design/typography.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)

