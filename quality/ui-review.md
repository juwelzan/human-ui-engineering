# UI Review & Visual Polish Checklist

> The exhaustive quality checklist that every AI agent and human engineer must audit before marking a UI task complete.

---

## 1. Purpose

Visual defects, misalignments, unhandled edge cases, and missing interactive states erode user trust. 

This checklist serves as the formal gate for UI completion. Audit every item before submitting code.

---

## 2. Visual Hierarchy & Layout Composition

- [ ] **Primary Action Clarity**: Is there a single, prominent primary action per viewport, with secondary actions clearly de-emphasized?
- [ ] **Grouping by Proximity**: Are related fields and labels grouped closely together (4px–8px) with generous breathing room between sections (24px–32px)?
- [ ] **Card Fatigue Elimination**: Is the screen free of unnecessary card wrappers? Has whitespace or subtle line division been used where appropriate?
- [ ] **Visual Noise**: Are there any arbitrary glowing borders, purposeless gradients, or decorative glassmorphism that should be removed?

---

## 3. Alignment & Spacing Cadence

- [ ] **Grid Adherence**: Are all margins, paddings, and gaps adhering strictly to the 4pt / 8pt spatial scale?
- [ ] **Horizontal Alignment**: Do input fields, buttons, and text share clean vertical grid lines?
- [ ] **Balanced Padding**: Do cards and modals have symmetrical internal padding?
- [ ] **Scroll Padding**: Does the bottom of scrollable views have enough padding (32px+) to prevent content from hiding beneath navigation bars or floating buttons?

---

## 4. Typography & Readability

- [ ] **Type Scale Discipline**: Are font sizes constrained to the approved 8-tier scale without arbitrary one-off pixel values?
- [ ] **Line-Height Proportion**: Are headings tight (1.15–1.25) and body text comfortable (1.4–1.6)?
- [ ] **Reading Measure**: Are text paragraphs capped at 50–75 characters per line (`max-w-prose`)?
- [ ] **Text Alignment**: Are all body paragraphs and descriptions left-aligned (or right-aligned in RTL)?

---

## 5. Color & Contrast

- [ ] **Contrast Compliance**: Do all body and label texts meet or exceed the **4.5:1** WCAG AA contrast ratio?
- [ ] **Color Independence**: Are errors and status alerts reinforced with icons and text rather than color alone?
- [ ] **Semantic Color Discipline**: Is red reserved exclusively for errors and destructive actions, green for success, and amber for warnings?
- [ ] **Dark Mode Harmony**: In dark mode, are surfaces elevated via lighter background luminance rather than invisible drop shadows?

---

## 6. Layout Stability & Responsiveness

- [ ] **No Horizontal Scroll**: Does the layout fit within the viewport without horizontal overflow on standard mobile widths (375px / 390px)?
- [ ] **Breakpoint Adaptations**: Do multi-column grids collapse gracefully into single-column layouts on mobile?
- [ ] **Text Truncation Guard**: Do flex items with truncating text include `min-w-0` to avoid blowing out container widths?
- [ ] **Image Dimensions**: Do images have explicit aspect ratios or dimensions to prevent Cumulative Layout Shift (CLS)?

---

## 7. The 4 Essential UI States

- [ ] **Loading State**: Is there a skeleton loader or spinner that matches the layout shape during async fetching?
- [ ] **Empty State**: When no data exists, does the view show a clear icon, explanation, and action button?
- [ ] **Error State**: If the network or query fails, is there an informative error message and a retry button?
- [ ] **Populated State**: Does the happy path render cleanly with varying data volumes?

---

## 8. Interactive Feedback & Touch Targets

- [ ] **Hit Area Sizing**: Are all buttons, icons, and tap targets at least **44x44pt** (iOS) or **48x48dp** (Android)?
- [ ] **All 5 Interactive States**: Do inputs and buttons handle Rest, Hover, Pressed, Focused, and Disabled states?
- [ ] **Keyboard Focus Rings**: Are high-contrast focus indicators clearly visible when navigating with the `Tab` key?
- [ ] **Modal Trapping & Escape**: Does `Escape` close active dialogs, and is keyboard focus trapped within open modals?

---

## 9. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Testing Standards: [testing.md](testing.md)
- Performance Audit: [performance-audit.md](performance-audit.md)
- Bug Prevention: [bug-prevention.md](bug-prevention.md)
- Release Checklist: [release-checklist.md](release-checklist.md)

