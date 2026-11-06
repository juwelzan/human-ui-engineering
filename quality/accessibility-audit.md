# Accessibility (A11y) Audit Checklist

> Exhaustive WCAG 2.1 AA compliance audit procedure for user interfaces across Web, Mobile, and Desktop.

---

## 1. Purpose

Accessibility is not an afterthought; it is a foundational quality requirement. This checklist provides a rigorous, step-by-step audit process to verify that an interface can be perceived, operated, and understood by all users, including those using screen readers, keyboard-only navigation, switch access, or high-contrast display modes.

---

## 2. Visual & Contrast Verification

- [ ] **Normal Text Contrast**: All body text, table cells, and form labels have a contrast ratio of at least **4.5:1** against their background.
- [ ] **Large Text Contrast**: Headings (≥ 18pt regular or ≥ 14pt bold) have a contrast ratio of at least **3.0:1**.
- [ ] **UI Component & Active Boundary Contrast**: Input borders, checkbox borders, and active tab highlights have at least **3.0:1** contrast against adjacent surfaces.
- [ ] **Color Independence**: No error state, status indicator, or chart datum relies solely on color to communicate meaning. Color is always paired with text or distinct icons.
- [ ] **Dark Mode Inversion**: Dark mode surfaces maintain legible contrast without saturated accents causing visual vibration.

---

## 3. Keyboard & Focus Navigation

- [ ] **Complete Operability**: Every interactive element (buttons, links, inputs, dropdowns, tabs, dialogs) can be reached and activated using `Tab`, `Shift+Tab`, `Enter`, and `Space`.
- [ ] **Visible Focus Rings**: Every focused element displays a prominent, high-contrast focus indicator (e.g. `ring-2 ring-primary ring-offset-2`). Default browser outlines are never removed without replacement.
- [ ] **Logical Tab Order**: Keyboard tab sequence follows visual layout order strictly (left-to-right, top-to-bottom).
- [ ] **Modal Focus Trapping**: When dialogs or bottom sheets open, focus is locked inside the overlay. Tabbing cycles strictly within the modal until dismissed.
- [ ] **Escape Key Dismissal**: Pressing the `Escape` key immediately closes open dialogs, dropdown menus, and popovers, returning focus to the trigger element.

---

## 4. Screen Reader Semantics & Assistive Tech

- [ ] **Semantic Markup**: Standard elements (`<button>`, `<nav>`, `<main>`, `<input>`) or platform widgets (`Semantics()`, `contentDescription`) are used rather than clickable non-semantic containers (`<div>`, `Container()`).
- [ ] **Icon-Only Accessible Labels**: Every icon-only button (e.g. `✕`, `🔍`, `☰`) has an explicit text label (`aria-label`, `Semantics(label:)`, `.accessibilityLabel`).
- [ ] **Form Label Association**: Form inputs are explicitly connected to their labels (`htmlFor`, `id`).
- [ ] **Error Announcement**: Form error messages are programmatically linked to their inputs via `aria-describedby` or equivalent platform semantics.
- [ ] **Live Regions**: Asynchronous UI updates (e.g. toast alerts, cart counter increments) announce to screen readers using `aria-live="polite"`.
- [ ] **Decorative Graphics**: Purely decorative artwork, background blobs, and ambient vectors are hidden from screen readers (`aria-hidden="true"`, `ExcludeSemantics`).

---

## 5. Touch Targets & Motor Accessibility

- [ ] **Minimum Hit Areas**:
  - iOS Touch Targets: Minimum **44 × 44 points**.
  - Android Touch Targets: Minimum **48 × 48 dp**.
  - Web Mobile Targets: Minimum **44 × 44 pixels**.
- [ ] **Hit Target Spacing**: Adjacent buttons have at least 8px spacing between their clickable bounds to prevent accidental mis-taps.
- [ ] **Dynamic Type & Font Scaling**: Layout expands gracefully without clipping when user system font size is set to **200%**.

---

## 6. Audit Verdict Classification

Record the accessibility audit outcome in the task report:
- **COMPLIANT**: All WCAG 2.1 AA checks verified with zero violations.
- **NON-COMPLIANT**: Specific violations identified (list file, line, and failure type).
- **BLOCKED**: Verification blocked by missing simulator or screen reader harness.

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Accessibility Design Standard: [../design/accessibility.md](../design/accessibility.md)
- UI Review Checklist: [ui-review.md](ui-review.md)
- Quality Report Template: [../templates/quality-report.md](../templates/quality-report.md)
