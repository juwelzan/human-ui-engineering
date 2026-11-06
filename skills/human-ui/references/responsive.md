# Responsive Layout Reference

> Reference for multi-breakpoint layouts, drawer transformations, and touch targets within the `/human-ui` skill.

---

## 1. Responsive Guidelines

- **5-Tier Breakpoints**:
  - `xs (< 640px)`: Single column, bottom navigation, full-width actions.
  - `sm (640px – 767px)`: 1–2 columns, compact headers.
  - `md (768px – 1023px)`: 2 columns, collapsible sidebar, modal dialogs.
  - `lg (1024px – 1279px)`: 3 columns, persistent sidebar.
  - `xl (≥ 1280px)`: Max-width centered container (`1200px – 1440px`).
- **Touch Targets**: Minimum **44x44pt** (iOS) / **48x48dp** (Android) on all touch surfaces.
- **Preventing Overflow**: Add `min-w-0` to flex child containers with truncating text to prevent horizontal overflow.
- **Dynamic Viewports**: Use `100dvh` on mobile web rather than `100vh` to avoid mobile address bar overlap.

---

## 2. In-Depth Documentation Links

- Complete Responsive Design Guide: [../../../design/responsive-design.md](../../../design/responsive-design.md)
- Navigation Architecture: [../../../components/navigation.md](../../../components/navigation.md)
