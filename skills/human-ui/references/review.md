# UI Code Review & Pre-Flight Reference

> Reference for evaluating code and architecture prior to release or pull request merge.

---

## 1. Code Review Directives

When reviewing UI code under `/human-ui review [scope]`:

- [ ] **Clean Code & Modularity**: Component files are under 200 lines; clear naming conventions (`isOpen`, `handleClick`).
- [ ] **No AI Visual Clichés**: Free of unwarranted dark neon glows, arbitrary gradients, and card overuse.
- [ ] **Accessibility (WCAG AA)**: Contrast ≥ 4.5:1, visible focus rings, explicit accessible labels on icon-only buttons.
- [ ] **Memory & Resource Disposal**: Event listeners, timers, controllers, and streams properly cleaned up.
- [ ] **Type Safety & Testing**: Zero `any`/`dynamic` props; unit/widget tests present for critical paths.

---

## 2. In-Depth Documentation Links

- 8-Point Pre-Flight Release Checklist: [../../../quality/release-checklist.md](../../../quality/release-checklist.md)
- Clean Code Standards: [../../../engineering/clean-code.md](../../../engineering/clean-code.md)
- Architecture Patterns: [../../../engineering/architecture-patterns.md](../../../engineering/architecture-patterns.md)

