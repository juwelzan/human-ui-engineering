# React Framework Reference

> Framework-specific guidance for React SPA development within the `/human-ui` skill.

---

## 1. Quick React Directives

- **Component Size**: Enforce 200-line maximum per file; extract sub-widgets and custom hooks.
- **Composition Over Props**: Use compound components (`Dialog`, `DialogHeader`, `DialogContent`) instead of giant 25-prop components.
- **State Separation**:
  - Server state: TanStack Query (React Query) / SWR.
  - Global state: Zustand / Redux Toolkit.
  - Local state: `useState` / `useReducer`.
- **Render Optimization**: Use `React.memo` and `useCallback` strategically on heavy components; virtualize long lists with `@tanstack/react-virtual`.
- **Lifecycle Cleanup**: Always return a cleanup function from `useEffect` to abort fetch requests, clear intervals, and remove event listeners.

---

## 2. In-Depth Documentation Links

- Complete React Guide: [../../../frameworks/react.md](../../../frameworks/react.md)
- Clean Code Standards: [../../../engineering/clean-code.md](../../../engineering/clean-code.md)
- State Management: [../../../engineering/state-management.md](../../../engineering/state-management.md)

