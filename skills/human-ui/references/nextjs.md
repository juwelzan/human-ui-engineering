# Next.js Framework Reference

> Framework-specific guidance for Next.js App Router and React Server Components (RSC).

---

## 1. Quick Next.js Directives

- **Server Component Boundary**: Default to Server Components; push `'use client'` down to interactive leaf nodes.
- **Streaming & Suspense**: Use `loading.tsx` and granular `<Suspense fallback={<Skeleton />}>` around slow async components.
- **Image & Font Optimization**:
  - Always use `next/image` with explicit dimensions; add `priority` for above-the-fold LCP heroes.
  - Use `next/font` for zero Cumulative Layout Shift (CLS).
- **Error Boundaries**: Create client-rendered `error.tsx` files inside route directories.

---

## 2. In-Depth Documentation Links

- Complete Next.js Guide: [../../../frameworks/nextjs.md](../../../frameworks/nextjs.md)
- Performance Optimization: [../../../engineering/performance.md](../../../engineering/performance.md)
- Loading States: [../../../components/loading-states.md](../../../components/loading-states.md)
