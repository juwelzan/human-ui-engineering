# Typography Components & Text Primitives

> Component API design, polymorphic rendering, truncation, and semantic hierarchy for text primitives.

---

## 1. Purpose

Hardcoding arbitrary typography classes (e.g. `text-xl font-bold text-gray-800` or raw `Text(style: ...)` widgets) across hundreds of view files causes inconsistent styling and visual drift. 

This guide defines the engineering standard for reusable typography components.

---

## 2. Decoupling Visual Style from Semantic HTML

A critical principle of accessible UI engineering is separating **visual size** from **semantic markup**:
- A heading might need the **semantic weight** of an `<h2>` for screen reader document structure, but require the **visual style** of a compact `h4` due to tight card space.
- Typography components should support an `as` prop (polymorphic rendering) or semantic tag parameter:

```tsx
// React Example: Styled as Heading 3, rendered semantically as H2
<Heading variant="h3" as="h2">
  Account Settings
</Heading>
```

```dart
// Flutter Example: Pre-composed text widgets with semantic roles
AppHeading.h3(
  'Account Settings',
  semanticTag: 'h2',
)
```

---

## 3. Recommended Typography Primitives

Create a focused set of typography components:

| Component | Intended Content | Default Element / Tag | Default Style |
|---|---|---|---|
| `<Heading>` | Page, section, and card titles | `<h1>` – `<h6>` | Bold / Semibold, tight line-height |
| `<Text>` | General body copy, descriptions | `<p>`, `<span>` | Regular / Medium, comfortable line-height |
| `<Label>` | Form labels, category badges | `<label>`, `<span>` | Medium / Semibold, compact height |
| `<Code>` | Monospace snippets, IDs, keys | `<code>`, `<pre>` | Monospace font, subtle background tint |

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
Whenever text is truncated, ensure the full string is accessible via a native tooltip (`title="..."` attribute, `<Tooltip>` component, or screen reader disclosure).

---

## 5. Typography Anti-Patterns

1. **Semantic Flattening**: Rendering all page titles as `<div>` or `<span>` without heading tags, destroying screen reader document outline navigation.
2. **Skipping Heading Levels**: Jumping directly from `<h1>` to `<h4>` without intermediate levels.
3. **Uncapped Line Lengths**: Allowing `<Text>` to stretch across 1400px of screen real estate. Always constrain reading width (`max-w-prose` / ~65ch).

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Typography Design System: [../design/typography.md](../design/typography.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)
