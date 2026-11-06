# Responsive & Multi-Platform Design

> Patterns and constraints for adapting interfaces smoothly across phones, tablets, desktops, and landscape orientations.

---

## 1. Purpose

A user interface that only works at 1440x900px or breaks on mobile screens is defective. Responsive design is not merely shrinking font sizes; it is reorganizing content to suit the device form factor, input mode, and viewing context.

---

## 2. Standard Breakpoints

Use a 5-tier responsive breakpoint scale:

| Breakpoint | Range | Typical Target Devices | Layout Behavior |
|---|---|---|---|
| **xs** (Mobile) | `< 640px` | Phones (iPhone 13–16, Pixel, Galaxy) | Single column, bottom navigation, full-width actions |
| **sm** (Phablet / Foldable) | `640px – 767px` | Large phones, folded foldables | 1–2 columns, compact headers |
| **md** (Tablet) | `768px – 1023px` | iPad portrait, Android tablets | 2 columns, collapsible sidebar, modal dialogs |
| **lg** (Desktop) | `1024px – 1279px` | Laptops, iPad landscape | 3 columns or fixed sidebar + main content area |
| **xl** (Widescreen) | `≥ 1280px` | Desktop monitors, ultra-wides | Max-width centered container (1200px–1440px) |

---

## 3. Core Adaptation Patterns

### 1. Reflow & Column Stacking
Multi-column grids (e.g. 3-column feature cards or 2-column checkout forms) must stack vertically into a single coherent column on mobile screens without horizontal scroll.

### 2. Navigation Transformation
- **Desktop (≥ 1024px)**: Persistent left sidebar or top horizontal navigation bar with dropdown menus.
- **Mobile (< 768px)**: Bottom navigation bar (3 to 5 core destinations) or top app bar with an off-canvas drawer.

### 3. Modals to Bottom Sheets
- On desktop, use centered modal dialogs with backdrop overlays.
- On mobile, convert modals into bottom sheets anchored to the thumb zone, swipeable downward to dismiss.

### 4. Data Tables to Card Lists
Wide data tables with 6+ columns overflow mobile viewports. On small screens:
- Either wrap the table in an explicit horizontally-scrollable container with a visual scroll cue.
- Or transform each row into a compact summary card displaying primary fields, with expandable rows for secondary details.

---

## 4. Input Modalities: Pointer vs. Touch

| Dimension | Mouse & Trackpad (Desktop) | Touchscreen (Mobile / Tablet) |
|---|---|---|
| **Target Size** | 24px – 32px clickable areas | Minimum **44x44pt** (iOS) / **48x48dp** (Android) |
| **Hover States** | Rich hover feedback, tooltips | No persistent hover; tooltips must open on tap/long-press |
| **Scrollbars** | Thin, scroll-on-demand or persistent | Invisible until scrolling; momentum flick physics |
| **Controls** | Context menus (right click), hover dropdowns | Action sheets, bottom drawers, long-press actions |

> [!IMPORTANT]
> Always guard hover-only styles using `@media (hover: hover) and (pointer: fine)` in CSS, or framework equivalents, to avoid sticky hover states on mobile touch devices.

---

## 5. Preventing Common Responsive Bugs

1. **Flex Child Overflow**: In CSS Flexbox, children default to `min-width: auto`, which prevents text truncation (`text-overflow: ellipsis`) from working. Always add `min-w-0` (`min-width: 0`) to flex children containing truncating text.
2. **Fixed Pixel Widths**: Never hardcode `width: 600px` on containers intended for mobile screens. Use `max-width: 600px; width: 100%`.
3. **Viewport Unit Traps (`100vh`)**: On mobile browsers, `100vh` includes the retractable browser address bar, causing button clipping at the bottom. Use `100dvh` (dynamic viewport height) or framework safe-area insets.

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Spacing System: [spacing.md](spacing.md)
- Navigation Component: [../components/navigation.md](../components/navigation.md)
- Dialogs & Sheets: [../components/dialogs.md](../components/dialogs.md)
