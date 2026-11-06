# UI Debugging & Bug Prevention Reference

> Reference for diagnosing layout overflows, null pointer exceptions, double-submits, and sticky mobile hovers.

---

## 1. Quick Debugging Heuristics

1. **Layout Overflow (Yellow & Black stripes / Horizontal scroll)**:
   - Add `min-w-0` to flex child elements.
   - Wrap unconstrained columns in a scrollable container (`SingleChildScrollView` / `overflow-y-auto`).
2. **"Cannot read properties of undefined"**:
   - Add optional chaining (`user?.profile?.avatar`) and fallbacks (`?? 'Guest'`).
3. **Double-Submit / Race Condition**:
   - Disable button immediately upon click (`disabled={isLoading}`).
4. **Sticky Mobile Hover**:
   - Wrap hover rules in `@media (hover: hover) and (pointer: fine)`.
5. **Keyboard Obscuring Input**:
   - Use keyboard-avoiding scroll containers and window insets.

---

## 2. In-Depth Documentation Links

- Top 10 Recurring UI Bugs & Defenses: [../../../quality/bug-prevention.md](../../../quality/bug-prevention.md)
- Error Handling & Resilience: [../../../engineering/error-handling.md](../../../engineering/error-handling.md)

