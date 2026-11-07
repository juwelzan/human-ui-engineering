# Accessibility (A11y) & Inclusive Design

> Mandatory engineering requirements for building accessible, WCAG 2.1 AA-compliant user interfaces.

---

## 1. Purpose

Accessibility is not a cosmetic checklist or an optional post-launch optimization; it is a fundamental engineering requirement. Over 15% of the global population lives with some form of permanent disability, and 100% of users experience temporary situational impairments (glare, one-handed operation, fatigue).

This guide mandates the accessibility standards that all generated UI must satisfy.

---

## 2. Visual Accessibility

### 1. Contrast Ratios (WCAG 2.1 AA)
- **Normal Text (< 18pt / 24px regular, < 14pt / 18.5px bold)**: Minimum **4.5:1** contrast ratio against its background.
- **Large Text (≥ 18pt or ≥ 14pt bold)**: Minimum **3.0:1** contrast ratio.
- **Active UI Components & Borders**: Minimum **3.0:1** for input boundaries, checkboxes, and toggle switches.

### 2. Color Independence
Never use color as the sole indicator of meaning, status, or validation:
- **Form errors**: Red border + inline exclamation icon + explicit error message text.
- **Active tabs**: Primary color + bold font weight + distinct underline indicator.
- **Status pills**: Green background + text label ("Completed" or "Active").

### 3. Font Scaling & Zoom Support
- Text containers must adapt to user-selected OS font scaling (iOS Dynamic Type, Android Font Scale, Browser 200% zoom) without clipping, overflowing, or truncating critical content.
- Avoid locking container heights (`height: 48px`) when children contain variable-size text; use `min-height` and allow vertical expansion.

---

## 3. Keyboard & Focus Management

Every interactive workflow must be fully operable via keyboard alone:

1. **Logical Tab Order**: Tab sequence must follow visual layout left-to-right, top-to-bottom.
2. **Visible Focus Indicators**: Ensure a high-contrast focus indicator is visible when navigating via keyboard or directional pad (e.g. `Focus(child: ...)` with border highlighting).
3. **Modal Focus Trapping**: When a dialog or sheet opens:
   - Initial focus must move to the dialog title or first interactive element.
   - Tab navigation must remain trapped inside the modal until dismissed.
   - Pressing `Escape` must close the dialog and return focus to the triggering element.
4. **Skip Links**: On web applications with extensive header navigation, provide a "Skip to Main Content" link as the first focusable element.

---

## 4. Assistive Technology & Screen Readers

| Platform | Screen Reader | Semantic API |
|---|---|---|
| **Web** | VoiceOver, NVDA, JAWS | Semantic HTML (`<button>`, `<main>`, `<nav>`, `<input>`) + WAI-ARIA |
| **Flutter** | TalkBack / VoiceOver | `Semantics()` widget, `excludeFromSemantics`, `button: true` |
| **Android** | TalkBack | `Modifier.semantics { contentDescription = "..." }`, `onClickLabel` |
| **iOS** | VoiceOver | `.accessibilityLabel("...")`, `.accessibilityHint("...")`, `.accessibilityAddTraits(.isButton)` |

### Screen Reader Best Practices:
- **Icon-Only Buttons**: Every button lacking visible text (e.g. `✕` close button or `🔍` search icon) MUST have an accessible label (`aria-label="Close dialog"`, `contentDescription = "Close dialog"`).
- **Decorative Images**: Images that do not convey essential information must be marked as decorative (`aria-hidden="true"`, empty `alt=""`, or `excludeFromSemantics: true`) to prevent screen reader noise.
- **Dynamic Updates**: Announce live changes (e.g. "Item added to cart") using live regions (`aria-live="polite"` or platform announcements).

---

## 5. Touch & Target Sizes

Interactive elements must provide ample surface area to accommodate coarse pointers and motor tremors:

- **iOS Touch Targets**: Minimum **44 × 44 points**.
- **Android Touch Targets**: Minimum **48 × 48 dp**.
- **Web Touch Targets**: Minimum **24 × 24 px** for dense desktop layouts, **44 × 44 px** for mobile viewports.
- If an icon is 16px wide, expand its clickable hit area with internal padding to satisfy the minimum target requirement.

---

## 6. Accessibility Verification Checklist

Before considering any UI task complete, verify:
- [ ] Are all text contrast ratios ≥ 4.5:1 (or ≥ 3:1 for large text)?
- [ ] Can all interactive elements be reached and activated via `Tab`, `Enter`, and `Space`?
- [ ] Are focus rings clearly visible when tabbing through the UI?
- [ ] Does pressing `Escape` close open modals, popovers, and menus?
- [ ] Do icon-only buttons carry descriptive accessibility labels?
- [ ] Does the UI scale gracefully when font size is increased to 150%–200%?
- [ ] Are all tap targets ≥ 44pt / 48dp on touch surfaces?

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Color System: [color-system.md](color-system.md)
- Buttons: [../components/buttons.md](../components/buttons.md)
- Text Fields: [../components/text-fields.md](../components/text-fields.md)
- Dialogs: [../components/dialogs.md](../components/dialogs.md)
- UI Review: [../quality/ui-review.md](../quality/ui-review.md)

