# Modern Web UI Engineering Guide

> Practical engineering guide for building fast, resilient web interfaces using modern semantic HTML5, modern CSS, Web Standards, and Core Web Vitals.

---

## 1. Modern Web Capabilities & Standards

The modern web platform provides powerful native features that previously required heavy JavaScript libraries:

- **Native `<dialog>` & Popover API**: Built-in modal dialogs with native backdrop scrims, focus trapping, and `Escape` key handlers without third-party JS.
- **CSS Container Queries (`@container`)**: Style components based on their parent container's width rather than viewport width.
- **CSS Nesting & Variables**: Native custom properties (`var(--token)`) and hierarchical nesting without Sass or preprocessors.
- **Subgrid (`grid-template-rows: subgrid`)**: Aligning cards, titles, and buttons across disparate grid cells with pixel perfection.
- **`color-mix()` & OKLCH**: Creating accessible tints, shades, and high-gamut color palettes directly in CSS.

---

## 2. Recommended Project Structure

For standards-based, lightweight, or multi-page web applications:

```text
src/
├── assets/                     # SVGs, optimized images, web fonts
├── styles/
│   ├── tokens.css              # CSS Custom Properties (colors, spacing, type scale)
│   ├── base.css                # CSS Reset & typography defaults
│   ├── components.css          # Modular component primitives
│   └── utilities.css           # Layout helpers
├── components/                 # Custom Elements / Web Components or template partials
│   ├── app-button.js
│   ├── app-modal.js
│   └── user-card.js
└── index.html
```

---

## 3. UI Architecture & Component Organization

- **Embrace Semantic HTML**:
  - Always use `<button type="button">`, never `<div onclick="...">`.
  - Structure documents with `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, and `<footer>`.
- **Web Components (Custom Elements)**:
  - For reusable framework-agnostic widgets, use standard Custom Elements:
    ```javascript
    class AppBadge extends HTMLElement {
      connectedCallback() {
        this.setAttribute('role', 'status');
      }
    }
    customElements.define('app-badge', AppBadge);
    ```

---

## 4. Modern CSS & Responsive Architecture

### Container Queries Over Media Queries
When building a reusable component (like a product card), its layout should adapt based on where it is placed (e.g. narrow sidebar vs wide main feed):

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 480px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}
```

---

## 5. Performance & Core Web Vitals (CWV)

Optimize for the three Google Core Web Vitals:

1. **Largest Contentful Paint (LCP < 2.5s)**:
   - Preload primary hero images: `<link rel="preload" as="image" href="/hero.webp" fetchpriority="high">`.
   - Never lazy-load the hero image.
2. **Interaction to Next Paint (INP < 200ms)**:
   - Keep long tasks off the main thread; use `requestIdleCallback` or Web Workers for non-critical work.
   - Yield to the main thread during heavy operations using `scheduler.yield()`.
3. **Cumulative Layout Shift (CLS < 0.1)**:
   - Always declare explicit `width` and `height` attributes on `<img>` and `<video>` tags.
   - Reserve space for dynamic banners and ads.

---

## 6. Accessibility (A11y)

- **Semantic Form Binding**: Always link `<label for="email">` with `<input id="email">`.
- **Keyboard Navigation**: Ensure all interactive controls can be operated via keyboard.
- **Focus Rings**: Style `:focus-visible` with a high-contrast ring:
  ```css
  :focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
  }
  ```

---

## 7. Common Mistakes to Avoid

1. **The Clickable `<div>` Trap**: Building interactive elements with `<div onClick>` which destroys keyboard navigation, screen reader accessibility, and native browser behavior.
2. **Blocking CSS**: Placing huge uncompressed CSS bundles in the `<head>` without critical CSS extraction.
3. **Sticky Hover on Touch**: Failing to wrap hover rules in `@media (hover: hover)`.

---

## 8. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- React Guide: [react.md](react.md)
- Next.js Guide: [nextjs.md](nextjs.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)

