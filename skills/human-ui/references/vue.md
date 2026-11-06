# Vue.js / Nuxt 3 Progressive Reference

> **Quick-reference rules for Vue 3 Composition API & Pinia.**

- **Component Standard**: Use `<script setup lang="ts">`.
- **Reactivity Rules**:
  - Use `ref()` for primitive state values.
  - Use `reactive()` for complex state objects.
  - Access `ref` values with `.value` in script blocks; unpacks automatically in templates.
- **State Management**: Use **Pinia** with setup syntax (`defineStore('id', () => { ... })`).
- **Performance**: Use `v-memo` on large table rows to skip re-renders when data does not change.
- **SSR / Nuxt**: Use `useAsyncData()` or `useFetch()` to avoid client-side fetch waterfalls.

See full guide in [`../../../frameworks/vue.md`](../../../frameworks/vue.md).

