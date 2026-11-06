# Modern Web Standards Reference

> Framework-specific guidance for semantic HTML5, modern CSS, Container Queries, and Web Components.

---

## 1. Quick Web Directives

- **Semantic HTML First**: Always use `<button>`, `<nav>`, `<main>`, `<dialog>`, and `<input>`, never interactive `<div>` tags.
- **Native Overlays**: Leverage the native `<dialog>` and Popover API for focus trapping and backdrop dismissal without heavy JS bundles.
- **Container Queries**: Use CSS Container Queries (`@container`) for modular components that adapt to their parent container rather than viewport width.
- **Core Web Vitals (CWV)**:
  - LCP (< 2.5s): Preload hero images, avoid lazy-loading above-the-fold content.
  - INP (< 200ms): Offload heavy JS tasks via Web Workers.
  - CLS (< 0.1): Explicit `width` and `height` attributes on all images.

---

## 2. In-Depth Documentation Links

- Complete Modern Web Guide: [../../../frameworks/web.md](../../../frameworks/web.md)
- Responsive Design: [../../../design/responsive-design.md](../../../design/responsive-design.md)

