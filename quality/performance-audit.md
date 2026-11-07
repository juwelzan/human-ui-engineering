# UI Performance & Memory Audit Checklist

> Systematic verification checklist for frame budgets, render cycles, memory leaks, and asset weights.

---

## 1. Purpose

UI applications can look visually polished while silently suffering from severe performance defects: memory leaks, dropped animation frames, unbounded list allocations, and un-optimized assets. 

This checklist defines the mandatory performance and memory audit before releasing code.

---

## 2. Render & Rebuild Optimization

- [ ] **Volatile State Containment**: Is fast-changing state (e.g. typing input, slider dragging) contained within isolated sub-components rather than re-rendering entire screen trees?
- [ ] **Selective Subscriptions**: Do components subscribe only to the specific slices of state they require, rather than observing global root objects?
- [ ] **Const / Static Instantiation**: Are all static sub-widgets declared with `const` constructors to prevent unnecessary rebuild churn?
- [ ] **RepaintBoundary Isolation**: Are animating subtrees isolated with `RepaintBoundary` to prevent invalidating adjacent static render objects?
- [ ] **No Expensive Operations in Build Loops**: Are heavy computations (JSON decoding, complex regex filtering) offloaded to background isolates via `compute()`?

---

## 3. List & Scroll Performance

- [ ] **Mandatory Virtualization**: Are lists and grids exceeding 20 items virtualized using `ListView.builder`, `GridView.builder`, or `CustomScrollView` with `SliverList`?
- [ ] **Recycled Keys**: Does every dynamic list item have a stable, unique `Key` (e.g. `ValueKey(item.id)`) for efficient Element tree reconciliation?
- [ ] **Scroll-Time Paint Bottlenecks**: Are elements free of heavy run-time blur effects and complex multi-layered drop shadows during active scrolling?

---

## 4. Memory & Resource Disposal

- [ ] **Event Listener Cleanup**: Are all `AppLifecycleListener` or global stream listeners explicitly removed in `State.dispose()`?
- [ ] **Timer Cancellation**: Are all `Timer` and `Timer.periodic` instances cancelled in `dispose()`?
- [ ] **Stream & Subscription Cancellation**: Are all `StreamSubscription` instances closed upon widget destruction?
- [ ] **Native Controller Disposal**: Are all `TextEditingController`, `AnimationController`, `ScrollController`, and `FocusNode` instances explicitly disposed of in `State.dispose()`?
- [ ] **Bounded Caches**: Are image and network caches bounded by an LRU eviction policy?

---

## 5. Media & Asset Discipline

- [ ] **Format Optimization**: Are photographic images formatted as WebP or AVIF rather than uncompressed PNG/JPEG?
- [ ] **Dimension Reservation**: Do all images specify `width` and `height` (or aspect-ratio containers) to avoid Cumulative Layout Shift (CLS)?
- [ ] **Lazy Loading**: Are off-screen below-the-fold images loaded lazily?
- [ ] **Icon Vectors**: Are UI icons provided as optimized SVGs or vector drawables rather than pixelated raster bitmaps?

---

## 6. Audit Reporting Honesty

> [!CAUTION]
> Never claim "zero memory leaks" or "perfect 120fps" unless verified using Flutter DevTools (Performance View, Memory snapshot diffs, or CPU Profiler).
> If profiling tools were not executed, report: *"Static code inspection completed for disposal and memoization; dynamic runtime profiling pending device run."*

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Performance Engineering: [../engineering/performance.md](../engineering/performance.md)
- Memory Management: [../engineering/memory-management.md](../engineering/memory-management.md)
- Quality Report Template: [../templates/quality-report.md](../templates/quality-report.md)

