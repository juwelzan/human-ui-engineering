# Dialogs, Modals & Overlay Engineering

> Architectural rules, focus trapping, dismissal behaviors, and responsive adaptations for overlay components.

---

## 1. Purpose

Dialogs and overlays interrupt the user flow to request critical confirmation, present focused tasks, or reveal contextual tools. Flawed modals—such as trapped keyboards, uncloseable backdrops, or missing mobile adaptations—break usability completely. 

This guide defines the engineering requirements for modal and overlay primitives.

---

## 2. Overlay Types & Use Cases

| Primitive | Primary Use Case | Desktop Presentation | Mobile Presentation |
|---|---|---|---|
| **Modal Dialog** | Focused sub-tasks (e.g. invite team member, edit record) | Centered floating box (max-w: 480px–640px) | Full-screen modal or bottom sheet |
| **Alert Dialog** | High-consequence confirmation (e.g. delete project) | Centered compact box (max-w: 400px) | Centered alert or bottom action sheet |
| **Bottom Sheet** | Mobile-first actions, menus, filtering controls | N/A (converts to popover or modal) | Anchored to bottom, swipeable downward |
| **Side Drawer** | Deep detail inspection, multi-filter panels | Slides from right edge (width: 380px–480px) | Full-width slide-over |
| **Popover** | Transient contextual details anchored to an element | Small floating card attached to anchor | Anchored popover or bottom sheet |

---

## 3. Anatomy of a Production Modal

```text
┌────────────────────────────────────────────────────────┐
│ ModalHeader                                            │
│   ModalTitle                                [✕ Close]  │
│   ModalDescription                                     │
├────────────────────────────────────────────────────────┤
│ ModalBody (Scrollable if content exceeds viewport)     │
│   Form inputs, configuration settings, or text         │
├────────────────────────────────────────────────────────┤
│ ModalFooter                                            │
│   [Secondary Action / Cancel]       [Primary Action]   │
└────────────────────────────────────────────────────────┘
```

### Essential Structural Rules:
1. **Pinned Header & Footer**: The title and action buttons must remain visible even when the modal body contains extensive scrollable content. Never let the close button or save button scroll off-screen.
2. **Backdrop Scrim**: A semi-transparent overlay (`bg-black/50` or `rgba(0,0,0,0.5)`) dims background content. Clicking the backdrop should dismiss non-destructive modals.

---

## 4. Focus Management & Accessibility (Mandatory)

Modals have the highest potential for critical accessibility failures:

1. **Focus Trapping**: When a modal opens, keyboard focus (`Tab` / `Shift+Tab`) must be strictly constrained inside the dialog. Focus must never escape to the hidden background page.
2. **Initial Focus**: On open, focus must move automatically to the first interactive field (or to the close button/title if no input exists).
3. **Focus Restoration**: When the dialog closes, focus must immediately return to the button or element that originally triggered it.
4. **Escape Key Dismissal**: Pressing the `Escape` key must dismiss the dialog immediately.
5. **Scroll Locking**: When the dialog is active, lock scrolling on the root background document (`document.body.style.overflow = 'hidden'` on web, or native modal controllers).
6. **ARIA Roles**:
   - Standard modal: `role="dialog"` with `aria-modal="true"`, `aria-labelledby="dialog-title-id"`, and `aria-describedby="dialog-desc-id"`.
   - Critical confirmation: `role="alertdialog"`.

---

## 5. Destructive Confirmations

For destructive actions (e.g. "Delete Database"):
- Modal title must clearly state the action: *"Delete 'Production DB'?"*
- Explain consequences: *"This action cannot be undone. All data will be permanently wiped."*
- Confirm button must use the **Destructive** variant.
- Require typed confirmation (e.g. *"Type 'DELETE' to confirm"*) for extreme irreversible actions.

---

## 6. Dialog Anti-Patterns

1. **Nested Modals (Modal Inception)**: Opening a modal on top of an existing modal. If a sub-task is required, swap the content within the current modal or use a side drawer.
2. **Mobile Width Squeeze**: Hardcoding `width: 500px` so that the modal overflows or clips on 375px mobile screens. Use `w-full max-w-lg mx-4`.
3. **Silent Dismiss on Unsaved Work**: Closing a modal and losing 20 minutes of user form input when they accidentally click the backdrop. Provide an unsaved changes warning before dismissal.

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)
- Buttons: [buttons.md](buttons.md)

