# Human Design Rules: Do's and Don'ts

> Strict design rules and practical heuristics for creating interfaces that feel crafted by expert human designers.

---

## 1. Visual Hierarchy & Layout

### DO
- **Use whitespace to create grouping**: Use Gestalt principles of proximity. Elements belonging together should have tight spacing (e.g. 4px–8px between a label and input), while distinct sections should have generous breathing room (24px–48px).
- **Establish clear vertical cadence**: Keep vertical spacing predictable down the page. Use multiples of 8px for section breaks.
- **Align elements strictly**: Choose a grid line and stick to it. Avoid arbitrary offsets or slight indentations that look like rendering errors.
- **Size items proportional to their importance**: Primary action buttons and critical figures should catch the eye before secondary metadata.

### DON'T
- **Do not wrap everything in a card**: A page consisting of 12 identical rounded boxes with light gray borders looks cluttered, monotonous, and amateur. Use whitespace, subtle dividers, or background alternation instead of repetitive cards.
- **Do not center-align body copy**: Long paragraphs (more than 2 lines) should always be left-aligned (or right-aligned in RTL languages). Center alignment makes the left margin ragged and strains the reader's eye.
- **Do not use full-width buttons on desktop**: A button stretched 1200px across a widescreen monitor is jarring and difficult to target. Constrain button widths or align them naturally with content columns.

---

## 2. Color & Contrast

### DO
- **Maintain a 60-30-10 color balance**:
  - ~60% Neutral backgrounds and surfaces (white, subtle grays, deep slates).
  - ~30% Content elements (text, icons, borders, structural elements).
  - ~10% Accent / Brand color (primary action buttons, active tabs, selected states).
- **Ensure WCAG AA compliance**: Text must meet a minimum contrast ratio of 4.5:1 against its background (3:1 for large text 18pt+ or bold 14pt+).
- **Reserve semantic colors for meaning**: Red is exclusively for destructive actions, errors, or critical alerts. Green is for positive confirmation. Yellow/Amber is for warnings. Never use semantic red as a casual brand decoration.

### DON'T
- **Do not use pure black on pure white**: High-contrast `#000000` text on `#FFFFFF` can cause visual fatigue (halation). Prefer deep grays/slates like `#111827` or `#0F172A`.
- **Do not rely on color alone to communicate state**: Always accompany color status indicators with an icon or clear text (e.g. green checkmark + "Active", red exclamation + "Failed") for colorblind accessibility.
- **Do not use low-contrast text**: Never render `#9CA3AF` (light gray) text on a white background for readable information.

---

## 3. Typography & Text

### DO
- **Keep font families disciplined**: Use 1 primary typeface for the entire application (e.g., Inter, Roboto, San Francisco, Plus Jakarta Sans). Never use more than 2 font families (e.g., 1 for display headings, 1 for UI body).
- **Set proportional line-heights**:
  - Headings: Tight line heights (`1.1` to `1.25`).
  - Body text: Comfortable line heights (`1.4` to `1.6`).
- **Cap line length for reading**: Restrict body text reading width to 50–75 characters per line (approx. 500px–700px) to prevent reader fatigue.

### DON'T
- **Do not use ALL-CAPS for long sentences**: Restrict uppercase text to tiny category badges, abbreviations, or overlines (max 2–3 words), and add letter-spacing (`tracking-wider`).
- **Do not invent random font sizes**: Stick strictly to an established typographic scale (12px, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 48px).

---

## 4. Interactive Feedback & State

### DO
- **Provide immediate visual feedback for all user actions**:
  - Hover: Subtle background shift or border highlight.
  - Active / Pressed: Scale down slightly (`scale(0.98)`) or darken.
  - Focus: Clear, high-contrast focus ring (essential for keyboard users).
  - Loading: Replace label with an inline spinner or disable the button with a clear progress state.
- **Make touch targets accessible**: Ensure all interactive elements have an effective tap target of at least 44x44 points (iOS) or 48x48 dp (Android).

### DON'T
- **Do not hide disabled reasons**: If a button is disabled, provide an explanatory tooltip, helper text, or keep it clickable to display validation errors.
- **Do not swallow clicks without indication**: Never allow an interactive button to be tapped without showing an immediate response (ripple, loading spinner, or disabled lock).

---

## 5. The "Never Do" List for AI Agents

1. **NEVER** add decorative neon drop shadows or glowing border animations to standard forms and dashboards.
2. **NEVER** apply multi-stop saturated gradients to regular text or buttons unless explicitly requested by the user's design token guide.
3. **NEVER** produce unscrollable layouts that break on small mobile screens (375px) or landscape orientations.
4. **NEVER** omit error, empty, or loading states from views.
5. **NEVER** use placeholder text as a substitute for explicit form input labels.

---

## 6. Related Documentation

- Design Philosophy: [design-philosophy.md](design-philosophy.md)
- Color System: [color-system.md](color-system.md)
- Typography: [typography.md](typography.md)
- Spacing: [spacing.md](spacing.md)
- Accessibility: [accessibility.md](accessibility.md)
