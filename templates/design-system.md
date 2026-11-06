# Template: Design System & Tokens Specification

> Fillable template for establishing and documenting color palettes, typography scales, spacing grids, and elevation tokens.

---

## 1. Color Palette Tokens

### Neutrals & Surfaces
| Token Name | Light Mode Hex | Dark Mode Hex | Usage |
|---|---|---|---|
| `bg-canvas` | `#F8FAFC` | `#0B0F19` | Root app background |
| `surface-card` | `#FFFFFF` | `#1E293B` | Cards, modals, sheets |
| `surface-subtle` | `#F1F5F9` | `#151E2E` | Table hover, input backgrounds |
| `border-default` | `#E2E8F0` | `#334155` | Dividers, card borders |
| `border-strong` | `#CBD5E1` | `#475569` | Active input borders |

### Typography & Content
| Token Name | Light Mode Hex | Dark Mode Hex | Usage |
|---|---|---|---|
| `text-primary` | `#0F172A` | `#F8FAFC` | Headings, primary labels (Min 7:1) |
| `text-secondary` | `#475569` | `#94A3B8` | Body text, descriptions (Min 4.5:1) |
| `text-muted` | `#64748B` | `#64748B` | Timestamps, helper hints |

### Brand & Semantic Status
| Token Name | Light Mode Hex | Dark Mode Hex | Usage |
|---|---|---|---|
| `brand-primary` | `[#Hex]` | `[#Hex]` | Primary CTA button background |
| `status-success` | `#16A34A` | `#4ADE80` | Valid states, completed alerts |
| `status-warning` | `#D97706` | `#FBBF24` | Pending tasks, warnings |
| `status-error` | `#DC2626` | `#F87171` | Validation errors, destructive |

---

## 2. Typography Hierarchy

- **Primary Font Family**: `[e.g. Inter, system-ui, Roboto, SF Pro]`
- **Display Font Family**: `[Optional, max 1 secondary typeface]`

| Token | Size | Line Height | Weight | Usage |
|---|---|---|---|---|
| `font-display` | 40px–48px | 1.15 | 700 | Hero headlines |
| `font-h1` | 30px–32px | 1.2 | 700 | Primary page titles |
| `font-h2` | 24px | 1.25 | 600 | Section headers |
| `font-h3` | 20px | 1.3 | 600 | Card titles |
| `font-body` | 16px | 1.5 | 400 | Primary body text |
| `font-body-sm` | 14px | 1.5 | 400 / 500 | Secondary metadata, inputs |
| `font-caption` | 12px | 1.4 | 500 | Badges, micro-labels |

---

## 3. Spacing Scale (4pt / 8pt Grid)

| Token | Pixels | Usage |
|---|---|---|
| `space-1` | 4px | Micro: Icon-to-text gap, badge padding |
| `space-2` | 8px | Tight: Label to input gap |
| `space-3` | 12px | Compact: Small button padding |
| `space-4` | 16px | Base: Standard card padding, list gap |
| `space-6` | 24px | Generous: Section padding, form gaps |
| `space-8` | 32px | Sectional: Major module spacing |
| `space-12`| 48px | Structural: Page headers |

---

## 4. Elevation, Radii & Motion

- **Border Radii**:
  - `radius-sm`: 4px (inputs, badges)
  - `radius-md`: 8px (buttons, small cards)
  - `radius-lg`: 12px–16px (dialogs, large containers)
  - `radius-full`: 9999px (pills, avatars)
- **Motion Durations**:
  - `motion-fast`: 150ms–200ms (hover, tap)
  - `motion-moderate`: 250ms–350ms (sheet slide, modal fade)
  - `motion-easing`: `cubic-bezier(0, 0, 0.2, 1)` (Decelerate ease-out)

