# UI Performance Reference

> Reference for frame budgets, virtualization, layout thrashing, and memory disposal within the `/human-ui` skill.

---

## 1. Performance Guidelines

- **Frame Budget Target**: < 16.6ms (60fps) or < 8.3ms (120fps).
- **Mandatory List Virtualization**: Virtualize any scrollable list with > 20 items (`ListView.builder`, `LazyColumn`, `@tanstack/react-virtual`).
- **Composite Animation Properties**: Animate GPU-composited properties only (`transform`, `opacity`); avoid animating `height`, `width`, or `margin`.
- **Resource Disposal**:
  - Remove all event listeners on unmount.
  - Cancel all timers (`clearInterval`, `timer.cancel()`).
  - Close all reactive streams and subscriptions.
  - Call `.dispose()` on all native controllers.

---

## 2. In-Depth Documentation Links

- Complete Performance Guide: [../../../engineering/performance.md](../../../engineering/performance.md)
- Memory Management & Disposal: [../../../engineering/memory-management.md](../../../engineering/memory-management.md)
- Performance Audit Checklist: [../../../quality/performance-audit.md](../../../quality/performance-audit.md)
