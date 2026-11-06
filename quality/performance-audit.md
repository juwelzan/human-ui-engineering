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
- [ ] **Const / Static Instantiation**:
  - In Flutter: Are all static sub-widgets declared with `const`?
  - In React: Are expensive callback functions wrapped in `useCallback` when passed to memoized children?
  - In Compose: Are state parameters stable and models marked `@Immutable`?
- [ ] **No Expensive Operations in Render Loops**: Are filtering, regex transformations, and sorting operations memoized or executed outside render passes?

---

## 3. List & Scroll Performance

- [ ] **Mandatory Virtualization**: Are lists exceeding 20 items virtualized (e.g. `ListView.builder`, `LazyColumn`, `@tanstack/react-virtual`, `LazyVStack`)?
- [ ] **Recycled Keys**: Does every dynamic list item have a stable, unique key/id (not array index) for efficient DOM / widget reconciliation?
- [ ] **Scroll-Time Paint Bottlenecks**: Are elements free of heavy run-time blur effects (`backdrop-filter`) and complex multi-layered drop shadows during active scrolling?

---

## 4. Memory & Resource Disposal

- [ ] **Event Listener Cleanup**: Are all `window`, `document`, or global bus listeners explicitly removed on component unmount?
- [ ] **Timer Cancellation**: Are all `setInterval`, `setTimeout`, and `Timer.periodic` instances cancelled in cleanup/dispose handlers?
- [ ] **Stream & Subscription Cancellation**: Are all reactive streams, observables, and WebSocket listeners closed upon component destruction?
- [ ] **Native Controller Disposal**: Are all text controllers, animation controllers, and scroll controllers explicitly disposed of in Flutter, Android, or iOS?
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
> Never claim "zero memory leaks" or "perfect 60fps" unless verified using profilers (e.g. Chrome DevTools Performance/Memory tab, Flutter DevTools, Android Studio Profiler, or Xcode Instruments).
> If profiling tools were not executed, report: *"Static code inspection completed for disposal and memoization; dynamic runtime profiling pending device run."*

---

## 7. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Performance Engineering: [../engineering/performance.md](../engineering/performance.md)
- Memory Management: [../engineering/memory-management.md](../engineering/memory-management.md)
- Quality Report Template: [../templates/quality-report.md](../templates/quality-report.md)

