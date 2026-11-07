# Workflow: Creating a Shared Component

> Step-by-step execution guide for identifying, abstracting, implementing, and documenting reusable UI components.

---

## 1. Purpose

Shared components must be resilient, flexible, and backward-compatible. Creating hasty abstractions without testing all interactive states produces leaky components that break across views. 

This workflow defines the lifecycle for building a shared component.

---

## 2. Step-by-Step Component Lifecycle

```mermaid
flowchart TD
    S1[1. Rubric Qualification] --> S2[2. API Contract Design]
    S2 --> S3[3. Implement 5 Core States]
    S3 --> S4[4. Accessibility & Semantics]
    S4 --> S5[5. Co-Located Tests & Stories]
    S5 --> S6[6. Documentation & Migration]
```

### Step 1: Rubric Qualification
Answer the 6 qualification questions from [Shared Component Rules](../components/shared-component-rules.md):
- Is it used in ≥ 2 places?
- Does it have a single clear responsibility?
- Can existing components solve this?
- Is the API understandable?
- Does it need variants?
- Will abstraction ease maintenance?

### Step 2: API Contract Design
1. Define explicit types for all widget parameters.
2. Provide sensible defaults for optional parameters.
3. Expose named constructors for variants (e.g. `AppButton.primary()`, `AppButton.secondary()`).
4. Keep constructors `const` wherever possible.

### Step 3: Implement the 5 Core States
Ensure the component explicitly supports:
1. **Default / Rest**: Standard styling with design tokens.
2. **Hover / Active**: Visual and tactile feedback.
3. **Focused**: High-contrast keyboard focus highlight.
4. **Disabled**: Reduced opacity, `onPressed: null`.
5. **Loading**: Inline progress indicator without layout jitter or dimension shifts.

### Step 4: Accessibility & Semantics
1. Assign semantic roles using Flutter's `Semantics` widget.
2. Ensure touch target padding satisfies minimum dimensions (48x48dp, `kMinInteractiveDimension`).
3. Verify contrast ratio (minimum 4.5:1).

### Step 5: Co-Located Widget Tests & Previews
1. Write widget tests in `test/shared/widgets/<category>/<widget_name>_test.dart`.
2. Test default rendering, tap handlers, disabled lock, and loading states using `WidgetTester`.
3. Verify interactive widget previews where applicable.

### Step 6: Documentation & Caller Migration
1. Document the component's variants and usage example in a markdown docstring or story.
2. Refactor existing duplicate code to consume the new shared component.
3. Verify that existing views did not regress.

---

## 3. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [../components/shared-component-rules.md](../components/shared-component-rules.md)
- Testing: [../quality/testing.md](../quality/testing.md)
- UI Review Checklist: [../quality/ui-review.md](../quality/ui-review.md)

