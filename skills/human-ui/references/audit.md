# UI & Performance Audit Reference

> Concise reference for conducting UI visual reviews, contrast audits, and performance profiling.

---

## 1. Audit Execution Protocol

When invoked with `/human-ui audit [scope]`:

1. **Visual Hierarchy & Spacing**:
   - Verify alignment against 4pt/8pt spatial grid.
   - Verify no card fatigue or unnecessary containers.
2. **Color & Contrast**:
   - Check all text contrast ratios (≥ 4.5:1 normal, ≥ 3.0:1 large).
   - Ensure errors and status badges are accompanied by icons and text, not color alone.
3. **Responsiveness**:
   - Test 375px (mobile), 768px (tablet), and 1280px (desktop).
   - Check touch targets (≥ 44x44pt on touch surfaces).
4. **Four UI States**:
   - Audit Loading, Empty, Error, and Populated states.
5. **Performance & Memory**:
   - Audit list virtualization, image dimension reservation (CLS), and resource disposal.

---

## 2. In-Depth Documentation Links

- Exhaustive UI Review Checklist: [../../../quality/ui-review.md](../../../quality/ui-review.md)
- Performance & Memory Audit: [../../../quality/performance-audit.md](../../../quality/performance-audit.md)
- Standard Quality Report Template: [../../../templates/quality-report.md](../../../templates/quality-report.md)

