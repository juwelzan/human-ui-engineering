# Reusable Widget & Micro-Component Catalog

> Specifications for essential micro-primitives: Badges, Avatars, Tooltips, List Tiles, Empty States, and Alert Banners.

---

## 1. Purpose

Micro-components are the ubiquitous details that tie a user interface together. When poorly standardized, teams end up with 10 different badge designs, inconsistent avatar sizes, and clunky tooltips. 

This guide defines the engineering standard for essential micro-primitives.

---

## 2. Status Badges & Chips

Used to display tags, counts, or entity statuses (e.g. "Active", "Trial", "Pending").

### Specifications:
- **Variants**: `neutral`, `success`, `warning`, `error`, `info`.
- **Anatomy**:
  - Optional 6px circular status dot (filled with status color).
  - Text label: 12px font size, semibold weight, uppercase or title case.
  - Optional right dismiss icon (`✕`) for filter chips.
- **Dimensions**: Height 20px–24px, horizontal padding 8px, border radius full (`rounded-full`) or 4px (`rounded`).
- **Color Rule**: In light mode, use subtle 10% opacity backgrounds with dark saturated text (e.g. green: `#DCFCE7` bg + `#15803D` text) to ensure WCAG AA contrast.

---

## 3. Avatars & Avatar Groups

Used to represent users, organizations, or bots.

### Specifications:
- **Sizes**:
  - `xs`: 24px (dense table rows)
  - `sm`: 32px (header navigation, comment threads)
  - `md`: 40px (default user lists, card headers)
  - `lg`: 56px–64px (profile overviews, account settings)
- **Fallback Hierarchy**:
  1. Primary: Image URL (rendered via `<img src="..." alt="User Name" />`).
  2. Fallback 1: Uppercase initials (e.g. "JD" for John Doe) centered on a neutral surface background.
  3. Fallback 2: Generic person silhouette vector icon if no name or image exists.
- **Broken Image Handling**: The component must listen for image load errors (`onError`) and seamlessly switch to the initials fallback without breaking layout.
- **Avatar Group / Stack**: Support overlapping avatars with a `-space-x-2` margin and a trailing `+N` badge indicating remaining users.

---

## 4. Tooltips

Used to provide brief contextual assistance on hover or keyboard focus.

### Specifications:
- **Trigger**: Activates on pointer hover or keyboard focus.
- **Delay**: 200ms–300ms hover delay before appearing (prevents visual clutter during casual mouse passes).
- **Positioning**: Automatically flips placement (top, bottom, left, right) if close to viewport boundaries (collision avoidance).
- **Style**: High-contrast dark background (`#1E293B`) with white text (`#F8FAFC`), 12px font, subtle shadow, 4px border radius.
- **Accessibility**: Must include `role="tooltip"` and be linked to the trigger via `aria-describedby`.

---

## 5. List Tiles & Row Items

Standardized horizontal rows used in settings lists, search results, and directories.

### Specifications:
- **Leading Slot**: Avatar, category icon, or checkbox.
- **Body Slot**: Title (bold/medium 14px–16px) + Subtitle/Description (muted 13px–14px).
- **Trailing Slot**: Metadata (timestamp, badge) + navigation disclosure indicator (`ChevronRight` icon).
- **Interactive**: Hover highlight, focus ring on keyboard tab, minimum height 48px–56px for touch targets.

---

## 6. Empty States

Displayed when a view has no data, search returns zero matches, or an inbox is clear.

### Specifications:
```text
┌────────────────────────────────────────────────────────┐
│                      [ Icon / Vector ]                 │
│                                                        │
│                    No projects found                   │  ◄── Title (H3 / Semibold)
│  Get started by creating your first project to begin.  │  ◄── Description (Muted)
│                                                        │
│                  [ + Create Project ]                  │  ◄── Primary Action CTA
└────────────────────────────────────────────────────────┘
```
- **Never leave the user stranded**: Always pair an empty state with a clear call-to-action button or reset search filter action.

---

## 7. Inline Alert Banners

Used for contextual notices within a page or form.

### Specifications:
- **Variants**: `info`, `warning`, `error`, `success`.
- **Anatomy**: Status icon (left) + Title / Message text + optional Dismiss button (`✕`).
- **Placement**: Placed directly above the relevant content section, never floating arbitrarily.

---

## 8. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Buttons: [buttons.md](buttons.md)
- Color System: [../design/color-system.md](../design/color-system.md)
- Accessibility: [../design/accessibility.md](../design/accessibility.md)

