# Task Mode Routing & Parameter Guide

> How the `/human-ui` slash command parses arguments and routes tasks to the appropriate engineering references.

---

## 1. Subcommand Parsing Heuristics

The `/human-ui` command parses the first token of the input string as a mode keyword. If the first token does not match an explicit mode, the command treats the entire input as a general task and automatically detects the framework from the codebase.

```text
/human-ui [subcommand?] [task_description]
```

---

## 2. Mode Matrix & Dispatch Rules

### 1. `/human-ui design [task]`
- **Intent**: Focuses on UI/UX aesthetics, visual hierarchy, layout composition, typography, and color harmony.
- **Rules**:
  - Load [design.md](design.md) (which routes to `design/design-philosophy.md` and `design/human-design-rules.md`).
  - Eliminate AI visual tropes (no dark neon glow, arbitrary gradients, or card fatigue).
  - Produce design tokens and shared primitives before building screens.

### 2. `/human-ui audit [scope]`
- **Intent**: Comprehensive evaluation of an existing screen, component, or entire project.
- **Rules**:
  - Load [audit.md](audit.md).
  - Execute both the **UI Review Checklist** (visual hierarchy, contrast, spacing, a11y) and **Performance Audit** (frames, memory, layout shifts).
  - Output an objective audit report using [quality-report.md](../../../templates/quality-report.md).

### 3. `/human-ui flutter [task]`
- **Intent**: Explicit Flutter development.
- **Rules**:
  - Load [flutter.md](flutter.md).
  - Enforce `const` constructors, `ListView.builder`, `Semantics`, and separation of presentation from BLoC/Riverpod logic.

### 4. `/human-ui react [task]`
- **Intent**: Explicit React or Next.js development.
- **Rules**:
  - Load [react.md](react.md) or [nextjs.md](nextjs.md).
  - Enforce compound component composition, custom hook extraction, virtualized lists, and clean `useEffect` cleanup.

### 5. `/human-ui responsive [task]`
- **Intent**: Mobile, tablet, and desktop layout adaptation.
- **Rules**:
  - Load [responsive.md](responsive.md).
  - Audit viewports: 375px (mobile), 768px (tablet), 1280px+ (desktop).
  - Enforce minimum touch targets (44x44pt) and `min-w-0` on flex children.

### 6. `/human-ui performance [task]`
- **Intent**: Profiling and fixing jank, slow renders, or high memory usage.
- **Rules**:
  - Load [performance.md](performance.md).
  - Follow the 5-step diagnostic loop: Measure -> Isolate -> Fix -> Re-measure -> Report.

### 7. `/human-ui debug [issue]`
- **Intent**: Isolating and repairing UI bugs, layout overflows, or broken state.
- **Rules**:
  - Load [debug.md](debug.md).
  - Check against the Top 10 recurring UI bugs in `quality/bug-prevention.md`.

### 8. `/human-ui recover`
- **Intent**: Resuming an interrupted workflow without losing progress.
- **Rules**:
  - Load [recovery.md](recovery.md).
  - Inspect `AI_TASK_STATE.md`, git diff, and resume from last verified checkpoint.

### 9. `/human-ui review [scope]`
- **Intent**: Code and architecture review prior to pull request or release.
- **Rules**:
  - Load [review.md](review.md).
  - Run the 8-point pre-flight release checklist in `quality/release-checklist.md`.

---

## 3. Related References

- Main Skill: [../SKILL.md](../SKILL.md)
- Master Instructions: [../../../AGENTS.md](../../../AGENTS.md)
