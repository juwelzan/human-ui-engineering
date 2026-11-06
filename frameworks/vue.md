# Vue.js UI Engineering Guide

> Practical engineering guide for building production Vue 3 applications using the Composition API, `<script setup lang="ts">`, Pinia, and Nuxt.

---

## 1. Recommended Project Structure

Follow a **Feature-First modular structure** for modern Vue 3 / Nuxt applications:

```text
src/
├── components/                 # Global shared UI primitives
│   ├── ui/                     # AppButton.vue, AppInput.vue, AppCard.vue
│   └── feedback/               # Skeletons, ErrorBoundary
├── composables/                # Cross-cutting composables (useTheme, useBreakpoint)
├── core/
│   ├── theme/                  # Tokens, Tailwind config, CSS variables
│   └── api/                    # Axios / ofetch client
├── features/                   # Feature-first domain modules
│   ├── checkout/
│   │   ├── components/         # Local sub-widgets
│   │   ├── composables/        # useCheckout.ts
│   │   ├── CheckoutView.vue    # Screen view
│   │   └── types.ts            # Local interfaces
│   └── dashboard/
├── stores/                     # Pinia stores (global state)
│   ├── auth.ts
│   └── preferences.ts
├── router/                     # Vue Router configuration
└── App.vue
```

---

## 2. Component Design (`<script setup lang="ts">`)

- **Strict Type Declarations**: Always declare typed props and emits using macro syntax:
  ```vue
  <script setup lang="ts">
  interface Props {
    variant?: 'primary' | 'secondary' | 'ghost';
    isLoading?: boolean;
    disabled?: boolean;
  }

  const props = withDefaults(defineProps<Props>(), {
    variant: 'primary',
    isLoading: false,
    disabled: false,
  });

  const emit = defineEmits<{
    (e: 'click', event: MouseEvent): void;
  }>();
  </script>

  <template>
    <button
      :class="['btn', `btn-${props.variant}`]"
      :disabled="props.disabled || props.isLoading"
      @click="(e) => emit('click', e)"
    >
      <span v-if="props.isLoading" class="spinner" aria-hidden="true" />
      <slot />
    </button>
  </template>
  ```
- **Slots Over Monster Props**: Use named slots (`#header`, `#footer`, `#default`) for flexible component composition.

---

## 3. State Management (Pinia & Composables)

- **Local State**: Use `ref()` for primitive values; use `reactive()` or `ref()` for typed objects.
- **Derived State**: Always use `computed()` for derived values. Never manually synchronize computed state in watchers.
- **Global Store**: Use **Pinia** setup stores:
  ```typescript
  export const useAuthStore = defineStore('auth', () => {
    const user = ref<User | null>(null);
    const isAuthenticated = computed(() => user.value !== null);

    function setUser(newUser: User | null) {
      user.value = newUser;
    }

    return { user, isAuthenticated, setUser };
  });
  ```

---

## 4. Lifecycle & Resource Disposal

Always release timers, observers, and event listeners in `onUnmounted`:

```typescript
import { onMounted, onUnmounted } from 'vue';

onMounted(() => {
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
});
```

---

## 5. Performance Optimization

1. **`v-once` & `v-memo`**: Use `v-once` for static unchanging elements; use `v-memo` on large table rows to skip re-rendering unless dependent values change.
2. **List Virtualization**: For long lists (> 30 items), use `vue-virtual-scroller` or `@tanstack/vue-virtual`.
3. **Async Components**: Lazy-load heavy modals and routes using `defineAsyncComponent`:
   ```typescript
   const AnalyticsModal = defineAsyncComponent(() => import('./AnalyticsModal.vue'));
   ```

---

## 6. Accessibility & Testing

- **Testing**: Use **Vitest** paired with **Vue Test Utils**:
  ```typescript
  import { mount } from '@vue/test-utils';
  import AppButton from './AppButton.vue';

  test('emits click event when clicked', async () => {
    const wrapper = mount(AppButton, { slots: { default: 'Submit' } });
    await wrapper.find('button').trigger('click');
    expect(wrapper.emitted('click')).toHaveLength(1);
  });
  ```
- **Semantics**: Use native semantic HTML elements and link input labels using `:for="id"`.

---

## 7. Common Mistakes to Avoid

1. **Mutating Props Directly**: Never mutate a prop inside a child component; emit an event (`update:modelValue`) to notify the parent.
2. **Destructuring Reactivity**: Destructuring properties directly from a reactive object breaks reactivity (`const { count } = state; // Breaks!`). Use `toRefs(state)`.
3. **Overusing Deep Watchers**: Setting `deep: true` on huge complex state objects causes severe CPU overhead on every nested mutation.

---

## 8. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Framework Isolation: [README.md](README.md)
- Clean Code Standards: [../engineering/clean-code.md](../engineering/clean-code.md)
