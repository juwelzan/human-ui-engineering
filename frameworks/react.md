# React UI Engineering Guide

> Practical engineering guide for building production React applications with functional components, hooks, clean state, and high rendering performance.

---

## 1. Recommended Project Structure

For modern React Single Page Applications (using Vite, Rsbuild, etc.):

```text
src/
├── components/                 # Global shared UI primitives
│   ├── ui/                     # Button, Input, Modal, Badge, Card
│   └── feedback/               # Skeletons, ErrorBoundary
├── core/
│   ├── theme/                  # Design tokens, CSS variables, Tailwind config
│   └── lib/                    # API clients, utils, formatters
├── features/                   # Feature-First domain modules
│   ├── checkout/
│   │   ├── components/         # Sub-widgets local to checkout
│   │   ├── hooks/              # useCheckout, usePaymentMethods
│   │   ├── services/           # API fetchers
│   │   ├── CheckoutView.tsx    # Screen assembly
│   │   └── types.ts            # Local interfaces
│   └── dashboard/
├── routes/                     # React Router / TanStack Router definitions
└── main.tsx
```

---

## 2. UI Architecture & Component Organization

- **Presentational vs Container Components**: Keep views declarative. Extract business logic, network orchestration, and complex state into custom hooks (`useCheckoutFlow()`), keeping TSX components focused on rendering.
- **Compound Components**: Use composition and compound patterns (`Dialog`, `DialogHeader`, `DialogContent`, `DialogFooter`) to avoid giant 30-prop components.
- **Component Size**: Enforce the 200-line limit per file; break large forms or dashboards into cohesive sub-widgets.

---

## 3. State Management Guidance

- **Separate Server State from Client State**:
  - Use **TanStack Query (React Query)** or **SWR** for remote server data (caching, deduping, background sync).
  - Use **Zustand** or **Redux Toolkit** for true global client state (session, theme, modal queues).
  - Use **`useState`** or **`useReducer`** for component-local ephemeral state.
- **Avoid Storing Derived State**: If a value can be computed during render (`filteredList = items.filter(...)`), compute it directly (wrapped in `useMemo` if expensive) rather than storing it in a synchronized `useState`.

---

## 4. Responsive Design

- Use CSS utility classes (Tailwind CSS) or CSS Modules with standard breakpoints (`sm:`, `md:`, `lg:`, `xl:`).
- Always guard text overflow inside flex containers with `min-w-0` and `truncate`.
- For layout-dependent rendering, prefer CSS media queries or Container Queries (`@container`) over JavaScript window resize listeners.

---

## 5. Performance Optimization

1. **Strategic Memoization**:
   - Do NOT wrap every trivial 3-line component in `React.memo`.
   - DO use `React.memo` on components that render frequently with heavy subtrees (e.g. data table rows, complex charts).
   - Use `useCallback` when passing callbacks to memoized child components to prevent breaking referential equality.
2. **List Virtualization**:
   - For lists or tables with more than 30–50 items, use `@tanstack/react-virtual` or `react-window`.
3. **Code Splitting**:
   - Lazy-load heavy routes and infrequent modals using `React.lazy` and `Suspense`:
     ```tsx
     const AnalyticsModal = React.lazy(() => import('./AnalyticsModal'));
     ```

---

## 6. Accessibility (A11y)

- Use semantic HTML tags: `<main>`, `<nav>`, `<header>`, `<footer>`, `<button>`, `<input>`.
- Use accessible libraries (Radix UI, Headless UI, React Aria) for complex primitives like dialogs, popovers, and comboboxes.
- Connect form inputs to error messages via `aria-describedby` and `aria-invalid`.
- Never remove focus rings without supplying a high-contrast replacement.

---

## 7. Testing

- Use **Vitest** or **Jest** paired with **React Testing Library**:
  ```tsx
  test('renders error state on API failure', async () => {
    render(<UserList />);
    const errorAlert = await screen.findByRole('alert');
    expect(errorAlert).toHaveTextContent(/failed to load users/i);
  });
  ```
- Query by role, text, and label rather than CSS classes or test IDs.

---

## 8. Common Mistakes to Avoid

1. **Missing Cleanup in `useEffect`**: Failing to remove event listeners, abort network requests (`AbortController`), or clear timers on unmount.
2. **Object Dependencies in `useEffect`**: Passing newly created object or array literals into `useEffect` dependency arrays, causing infinite re-render loops.
3. **Prop Drilling**: Passing props through 5 levels of components that do not need them instead of using context or component composition.

---

## 9. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Next.js Guide: [nextjs.md](nextjs.md)
- Web Guide: [web.md](web.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)

