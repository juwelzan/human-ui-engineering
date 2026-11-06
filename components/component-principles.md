# Advanced Component Engineering Principles

> Principles for defining component boundaries, composition over configuration, token integration, and variant architectures.

---

## 1. Purpose

Components are the fundamental abstraction of modern user interfaces. However, poorly designed components create leaky abstractions, prop drilling nightmares, and maintenance friction. A component overloaded with 30 boolean flags to satisfy 10 distinct features becomes unmaintainable.

This guide defines the engineering principles for building robust, reusable UI component systems.

---

## 2. Component Boundaries & Single Responsibility

A component should have **one primary reason to change**:

| Component Tier | Primary Responsibility | Anti-Pattern to Avoid |
|---|---|---|
| **Atom / Primitive** (`Button`, `Badge`, `Input`) | Pure visual rendering of an interactive primitive with states. | Embedding network calls or analytics dispatches inside a button. |
| **Molecule / Composite** (`FormField`, `SearchBar`) | Grouping related primitives with layout proximity. | Hardcoding page-specific business logic or navigation routes. |
| **Organism / Widget** (`UserTable`, `PricingGrid`) | Rendering a coherent feature UI block with internal structure. | Monolithic 800-line views that handle their own database queries. |
| **View / Screen** (`BillingScreen`, `ProfileView`) | Coordinating widgets, binding to state controllers, handling routing. | Re-declaring primitive styling or custom button HTML inline. |

---

## 3. Composition Over Configuration (Slots & Compound Patterns)

When a component begins accumulating configuration props, pivot to **Composition**:

```tsx
// Anti-Pattern: Prop explosion / Mega-component
<Modal
  isOpen={isOpen}
  title="Edit Profile"
  titleIcon="user"
  showCloseButton={true}
  onClose={handleClose}
  bodyText="Please update your info"
  hasAvatarUpload={true}
  primaryActionLabel="Save"
  onPrimaryAction={handleSave}
  isPrimaryLoading={isSaving}
  secondaryActionLabel="Cancel"
  onSecondaryAction={handleClose}
/>

// Best Practice: Compound Component Pattern
<Modal isOpen={isOpen} onDismiss={handleClose}>
  <ModalHeader>
    <ModalTitle icon={<UserIcon />}>Edit Profile</ModalTitle>
    <ModalCloseButton onClick={handleClose} />
  </ModalHeader>
  <ModalBody>
    <Text>Please update your info</Text>
    <AvatarUpload onUpload={handleUpload} />
  </ModalBody>
  <ModalFooter>
    <Button variant="ghost" onClick={handleClose}>Cancel</Button>
    <Button variant="primary" isLoading={isSaving} onClick={handleSave}>Save</Button>
  </ModalFooter>
</Modal>
```

### Why Composition Wins:
1. **Zero Prop Bloat**: Adding a new icon, tooltip, or secondary badge requires zero changes to the `Modal` API.
2. **Flexible Structure**: Consumers can reorder headers, footers, or add custom dividers without hacking internal props.
3. **Transparent Mental Model**: The code in the consumer file mirrors the visual DOM tree.

---

## 4. State Matrix for Every Interactive Primitive

Every interactive primitive component must implement and document this exact 7-state matrix:

```mermaid
stateDiagram-v2
    [*] --> Default
    Default --> Hover: Pointer over
    Default --> Focused: Tab key focus
    Default --> Pressed: Mouse down / Tap
    Default --> Disabled: disabled = true
    Default --> Loading: isLoading = true
    Default --> Error: hasError = true
    
    Hover --> Default
    Focused --> Default
    Pressed --> Default
```

1. **Default / Rest**: Base design token styling.
2. **Hover**: 5%–10% surface luminance shift; pointer cursor.
3. **Pressed / Active**: Subtle scale (`0.98`) or tactile tint.
4. **Focused**: High-contrast keyboard focus ring with offset (`ring-2 ring-primary ring-offset-2`).
5. **Disabled**: Attenuated opacity (40%–50%), `cursor: not-allowed`, suppressed pointer events.
6. **Loading**: Replaced icon/spinner; layout dimensions preserved (no width jitter).
7. **Error**: Semantic red boundary with accessible error description link.

---

## 5. Avoiding Leaky & Unnecessary Abstractions

> [!WARNING]
> Do not create a wrapper component if it adds zero value over the underlying native framework primitive.
> - An `AppRow` component that merely wraps `Row(children: children)` adds indirection and cognitive load.
> - An abstraction is only justified if it encapsulates design tokens, reusable states, responsive rules, or accessibility invariants.

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Buttons: [buttons.md](buttons.md)
- Forms Architecture: [forms.md](forms.md)
- Component Testing: [component-testing.md](component-testing.md)

