# Angular 17+ Progressive Reference

> **Quick-reference rules for Standalone Components, Signals & modern control flow.**

- **Component Standard**: Always use `standalone: true` components; avoid legacy NgModules.
- **Change Detection**: Set `changeDetection: ChangeDetectionStrategy.OnPush` on every component.
- **Reactivity & State**:
  - Use **Signals** (`signal()`, `computed()`) for component state.
  - Read signal values by invoking them as functions: `count()`.
  - Use `effect()` strictly for side effects (logging, analytics), never for syncing state.
- **Built-in Control Flow**: Use modern `@if`, `@else`, `@for (item of items; track item.id)`, and `@switch`.
- **Forms**: Use Reactive Forms with typed form controls (`FormControl<string>`).

See full guide in [`../../../frameworks/angular.md`](../../../frameworks/angular.md).
