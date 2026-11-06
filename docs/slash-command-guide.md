# Chat Slash Command Guide: `/human-ui`

> Practical user manual for invoking Human UI Engineering directly from your AI coding agent's chat input.

---

## 1. Overview

The `/human-ui` slash command provides direct access to the entire Human UI Engineering system from your agent's chat box.

```text
/human-ui [subcommand?] [task_description]
```

When invoked, the skill:
1. Identifies the requested mode (`design`, `audit`, `flutter`, `react`, etc.).
2. Inspects your project to identify the framework, design tokens, and existing components.
3. Loads only the relevant modular reference documents.
4. Executes the task using human-centered engineering standards.
5. Verifies the result and reports the exact status.

---

## 2. Command Catalog & Concrete Examples

### 1. General Task Mode
Used for end-to-end screen or feature implementation.
```text
/human-ui Build a clean, accessible account profile screen with avatar upload.
```
- **What Happens**: Discovers project framework, checks for existing `Button` and `TextField` components in `components/`, constructs missing primitives, wires unidirectional data flow, handles all 4 states (Loading, Empty, Error, Success), and audits contrast.

### 2. Design Mode (`design`)
Used when visual hierarchy, spacing, or color system requires dedicated focus.
```text
/human-ui design Establish a 4pt/8pt grid and accessible color palette for our SaaS dashboard.
```
- **What Happens**: Loads [design.md](../skills/human-ui/references/design.md), audits surface elevations and text contrast, and outputs semantic tokens.

### 3. Audit Mode (`audit`)
Used to evaluate existing code for visual defects, layout overflow, contrast failures, and performance bottlenecks.
```text
/human-ui audit src/features/billing
```
- **What Happens**: Runs the [UI Review Checklist](../quality/ui-review.md) and [Performance Audit](../quality/performance-audit.md), outputting an objective [Quality Report](../templates/quality-report.md).

### 4. Flutter Mode (`flutter`)
Used for Flutter-specific development.
```text
/human-ui flutter Implement an adaptive sliver app bar with pull-to-refresh.
```
- **What Happens**: Loads [flutter.md](../skills/human-ui/references/flutter.md), enforces `const` constructors, separates presentation from BLoC/Riverpod, and adds TalkBack semantics.

### 5. React / Next.js Mode (`react`)
Used for React SPA or Next.js implementations.
```text
/human-ui react Create a virtualized transaction table with debounced search.
```
- **What Happens**: Loads [react.md](../skills/human-ui/references/react.md), uses `@tanstack/react-virtual`, isolates volatile typing state, and adds proper `useEffect` cleanup.

### 6. Responsive Mode (`responsive`)
Used to fix mobile clipping, table overflow, or breakpoint layout shifts.
```text
/human-ui responsive Refactor our checkout summary to collapse gracefully on 375px mobile screens.
```
- **What Happens**: Loads [responsive.md](../skills/human-ui/references/responsive.md), adds `min-w-0` to flex containers, reflows multi-column grids, and verifies 44x44pt touch targets.

### 7. Performance Mode (`performance`)
Used to eliminate jank, frame drops, or high memory consumption.
```text
/human-ui performance Fix dropped frames and memory leaks during infinite feed scrolling.
```
- **What Happens**: Follows the 5-stage diagnostic loop in [performance-fix.md](../workflows/performance-fix.md): Measure -> Isolate -> Fix -> Re-measure -> Report.

### 8. Debug Mode (`debug`)
Used to resolve tricky UI glitches.
```text
/human-ui debug The virtual keyboard covers the password field on mobile devices.
```
- **What Happens**: References [debug.md](../skills/human-ui/references/debug.md) and applies defensive viewport/insets wrapping.

### 9. Recovery Mode (`recover`)
Used to resume interrupted or broken workflows without restarting.
```text
/human-ui recover
```
- **What Happens**: Loads [recovery.md](../skills/human-ui/references/recovery.md), inspects `AI_TASK_STATE.md`, runs `git status` and `git diff`, identifies the last verified checkpoint, diagnoses the interruption, and resumes work safely.

### 10. Review Mode (`review`)
Used for pre-flight PR checks.
```text
/human-ui review Review recent checkout changes before opening a PR.
```
- **What Happens**: Audits code against the [8-Point Release Checklist](../quality/release-checklist.md).

---

## 3. Related Documentation

- Main Skill: [../skills/human-ui/SKILL.md](../skills/human-ui/SKILL.md)
- Compatibility Matrix: [compatibility-matrix.md](compatibility-matrix.md)
- Installation Guide: [installation-guide.md](installation-guide.md)

