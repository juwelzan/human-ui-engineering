# Text Field & Form Input Engineering

> Anatomy, states, mobile keyboard optimization, and accessibility for form inputs.

---

## 1. Purpose

Form inputs are the primary mechanisms for user data entry. Bad inputs—such as missing labels, broken error states, or poor mobile keyboards—lead to form abandonment and high user frustration. 

This guide defines the engineering requirements for robust input primitives.

---

## 2. Anatomy of a Production Text Field

Every production form input consists of five distinct structural zones:

```text
┌────────────────────────────────────────────────────────┐
│ Label Text *                     (Optional Indicator)  │  ◄── 1. Top Label
├────────────────────────────────────────────────────────┤
│ [Prefix Icon]  Input Value Text       [Suffix Action]  │  ◄── 2. Input Container
├────────────────────────────────────────────────────────┤
│ ⚠ Error message description or helpful hint (0/100)    │  ◄── 3. Helper / Error Text
└────────────────────────────────────────────────────────┘
```

1. **Top Label**:
   - Always visible above the input container.
   - **NEVER** use placeholder text as a substitute for an input label. Placeholders disappear as soon as the user types, destroying context.
   - Clearly designate optional fields with `(optional)` rather than littering every single field with red asterisks `*`.
2. **Input Container**:
   - Standard height: 40px–48px.
   - Accommodates optional prefix icon (e.g. search magnifying glass) and suffix action (e.g. password visibility toggle, clear button).
3. **Helper & Error Message**:
   - Positioned directly below the field.
   - Renders in neutral muted color for hints, or semantic red when validation fails.

---

## 3. Input States

A complete text field component must handle:

| State | Visual Treatment | Technical Attributes |
|---|---|---|
| **Default / Rest** | Neutral border (`border-default`), surface background | `aria-invalid="false"` |
| **Hover** | Darker border (`border-strong`) | Cursor changes to text/I-beam |
| **Focused** | High-contrast accent border + focus ring (`ring-2 ring-primary`) | Keyboard cursor active |
| **Disabled** | Muted background, 50% opacity, non-interactive | `disabled`, `aria-disabled="true"` |
| **Read-Only** | Subtle border, selectable text, no focus ring | `readonly` |
| **Error / Invalid**| Semantic red border (`border-error`), red focus ring, red error text | `aria-invalid="true"`, `aria-describedby="error-id"` |

---

## 4. Mobile Keyboard & Auto-Fill Optimization

For mobile web and native apps, configure the virtual keyboard properly to match expected data:

```html
<!-- Email -->
<input type="email" inputmode="email" autocomplete="email" autocapitalize="none" />

<!-- Phone Number -->
<input type="tel" inputmode="tel" autocomplete="tel" />

<!-- Monetary / Numeric Quantity -->
<input type="text" inputmode="decimal" pattern="[0-9]*" />

<!-- One-Time Password (OTP) -->
<input type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" />
```

> [!TIP]
> Setting correct `inputmode` and `autocomplete` attributes dramatically increases conversion rates and reduces typing fatigue on mobile devices.

---

## 5. Accessibility Requirements

1. **Programmatic Association**: Always associate the `<label>` with `<input>` using `htmlFor` / `id` (or framework semantic equivalent).
2. **Accessible Error Links**: Connect error messages to the input using `aria-describedby="field-error-id"` so screen readers speak the error upon field focus.
3. **Hit Area**: Clicking anywhere on the label or within the container padding must focus the text input.

---

## 6. Text Field Anti-Patterns

1. **The Vanishing Label**: Using placeholder text as the only label. Once filled, the user cannot verify what the field was for.
2. **Validation on First Keystroke**: Displaying aggressive red error banners before the user finishes typing their email. Validate on `blur` (focus exit) or debounce input validation.
3. **Obscured Password Toggles**: Not providing an eye icon to let users reveal password characters when entering complex passwords on mobile devices.

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Color System: [../design/color-system.md](../design/color-system.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)
- Buttons: [buttons.md](buttons.md)

