# Typography & Text Hierarchy

> Rules for establishing clear reading hierarchy, vertical rhythm, and comfortable typography.

---

## 1. Purpose

Typography accounts for more than 80% of any user interface. Weak typographic hierarchy confuses users, induces fatigue, and obscures critical information. 

This guide defines an intentional, legible typographic scale and layout rules.

---

## 2. Standard Typographic Scale

Use an 8-level scale with paired line-heights and semantic weights:

| Token | Size (px / pt) | Line Height | Recommended Weight | Usage |
|---|---|---|---|---|
| `font-display` | 40px – 48px | 1.15 | 700 (Bold) | Marketing hero, major landing headlines |
| `font-h1` | 30px – 32px | 1.2 | 700 (Bold) | Primary page titles (one per page) |
| `font-h2` | 24px | 1.25 | 600 (Semibold) | Major section headers, modal titles |
| `font-h3` | 20px | 1.3 | 600 (Semibold) | Subsection headers, card titles |
| `font-subhead` | 18px | 1.4 | 500 (Medium) | Lead paragraphs, callouts |
| `font-body` | 16px | 1.5 | 400 (Regular) | Primary readable body text, form inputs |
| `font-body-sm` | 14px | 1.5 | 400 (Reg) / 500 (Med) | Secondary metadata, table cells, buttons |
| `font-caption` | 12px | 1.4 | 500 (Medium) | Badges, timestamps, helper text |

---

## 3. Font Family Selection

- **Default to System Font Stacks**: System fonts load instantaneously with zero layout shift (CLS) and feel native to the device:
  - **Web**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
  - **iOS / macOS**: San Francisco (`SF Pro`)
  - **Android**: Roboto / Google Sans
- **Custom Web Fonts**: If brand identity requires a custom typeface (e.g. Inter, Plus Jakarta Sans, Geist, Poppins), use it consistently across the entire app. 
- **Maximum 2 Typefaces**: Never combine more than two font families (e.g., 1 for display headings, 1 for UI body).

---

## 4. Readability Heuristics

1. **Line Length (Measure)**: Restrict long-form text blocks to 50–75 characters per line (approx. 500px–680px). Unbounded full-width text lines on widescreen monitors force eye strain.
2. **Proportional Line-Height**:
   - As font size grows larger (headings), line-height should become tighter (`1.1` to `1.25`).
   - As font size decreases (body), line-height must expand (`1.4` to `1.6`) to prevent ascenders and descenders from colliding.
3. **Letter Spacing (Tracking)**:
   - Headings: Tighten slightly (`letter-spacing: -0.01em` to `-0.02em`) to improve cohesion.
   - Small uppercase overlines/tags: Loosen significantly (`letter-spacing: 0.05em` to `0.1em`) for legibility.
4. **Alignment**: Left-align all paragraphs and descriptive text. Reserve center-alignment strictly for brief, 1–2 line titles or isolated empty-state callouts.

---

## 5. Responsive Typography

Do not render 48px hero headers on 375px mobile screens. Scale typography across breakpoints:

- **Desktop (≥ 1024px)**: Full scale (H1: 32px, Display: 48px).
- **Mobile (< 768px)**: Step down headings by 1 tier (H1 becomes 26px–28px, Display becomes 36px; body text stays locked at 15px–16px for readability).

---

## 6. Related Documentation

- Design Philosophy: [design-philosophy.md](design-philosophy.md)
- Color System: [color-system.md](color-system.md)
- Spacing System: [spacing.md](spacing.md)
- Typography Component: [../components/typography.md](../components/typography.md)
