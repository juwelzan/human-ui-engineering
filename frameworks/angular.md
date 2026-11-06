# Angular UI Engineering Guide

> Practical engineering guide for building modern Angular applications using Standalone Components, Signals, modern control flow (`@if`, `@for`), and `OnPush` change detection.

---

## 1. Recommended Project Structure

Follow a modern modular Standalone Architecture (Angular 17+):

```text
src/app/
├── core/
│   ├── designsystem/           # Shared UI primitives: app-button, app-input
│   ├── interceptors/           # HTTP interceptors
│   └── services/               # Global services (AuthService, ThemeService)
├── features/                   # Feature-first domain modules
│   ├── billing/
│   │   ├── components/         # Local billing sub-components
│   │   ├── services/           # BillingService (SignalStore)
│   │   ├── billing.routes.ts   # Feature routes
│   │   └── billing.component.ts# Smart container view
│   └── dashboard/
├── app.config.ts               # Application providers & router configuration
├── app.routes.ts               # Root routing table with loadComponent
└── app.component.ts            # Root shell
```

---

## 2. Component Design (Standalone & Signals)

- **Standalone Components by Default**: Never generate legacy `@NgModule` declarations for new components.
- **Signals for State & Inputs**: Use Angular's modern signal-based inputs and outputs:
  ```typescript
  import { Component, input, output, ChangeDetectionStrategy } from '@angular/core';

  @Component({
    selector: 'app-button',
    standalone: true,
    template: `
      <button
        [class]="'btn btn-' + variant()"
        [disabled]="disabled() || isLoading()"
        (click)="clicked.emit($event)"
      >
        @if (isLoading()) {
          <span class="spinner" aria-hidden="true"></span>
        }
        <ng-content></ng-content>
      </button>
    `,
    changeDetection: ChangeDetectionStrategy.OnPush,
  })
  export class AppButtonComponent {
    variant = input<'primary' | 'secondary' | 'ghost'>('primary');
    isLoading = input<boolean>(false);
    disabled = input<boolean>(false);
    clicked = output<MouseEvent>();
  }
  ```

---

## 3. Modern Control Flow Syntax

Always use built-in control flow instead of legacy structural directives (`*ngIf`, `*ngFor`):

```html
<!-- Modern Angular Control Flow -->
@if (isLoading()) {
  <app-skeleton-loader />
} @else if (hasError()) {
  <app-error-banner [message]="errorMessage()" (retry)="fetchData()" />
} @else {
  @for (user of users(); track user.id) {
    <app-user-row [user]="user" />
  } @empty {
    <app-empty-state title="No users found" />
  }
}
```

> [!IMPORTANT]
> Always specify `track item.id` in `@for` blocks to prevent DOM recreation during collection updates.

---

## 4. State Management (Signals & RxJS)

- **Use Signals for Synchronous UI State**: `signal()`, `computed()`, and `effect()` provide glitch-free fine-grained reactivity.
- **Use RxJS for Asynchronous Event Streams**: Debounced search inputs, WebSocket feeds, and polling mechanisms.
- **Convert Between RxJS and Signals Seamlessly**: Use `toSignal(observable$)` and `toObservable(signal)`.

---

## 5. Performance & Change Detection

1. **`ChangeDetectionStrategy.OnPush`**: Apply `OnPush` to every component. In modern Angular with Signals, `OnPush` skips entire component subtrees when inputs and signals have not updated.
2. **Virtual Scrolling**: For datasets exceeding 50 items, use the Angular CDK Virtual Scroll (`cdk-virtual-scroll-viewport`).
3. **Route Lazy Loading**: Use `loadComponent` in routing tables:
   ```typescript
   export const routes: Routes = [
     {
       path: 'billing',
       loadComponent: () => import('./features/billing/billing.component')
         .then(m => m.BillingComponent),
     },
   ];
   ```

---

## 6. Testing

- Use **Angular TestBed** or modern **Vitest / Jest**:
  ```typescript
  import { ComponentFixture, TestBed } from '@angular/core/testing';
  import { AppButtonComponent } from './app-button.component';

  describe('AppButtonComponent', () => {
    let fixture: ComponentFixture<AppButtonComponent>;

    beforeEach(async () => {
      await TestBed.configureTestingModule({
        imports: [AppButtonComponent],
      }).compileComponents();

      fixture = TestBed.createComponent(AppButtonComponent);
      fixture.detectChanges();
    });

    it('renders button element', () => {
      const button = fixture.nativeElement.querySelector('button');
      expect(button).toBeTruthy();
    });
  });
  ```

---

## 7. Common Mistakes to Avoid

1. **Calling Functions in Template Bindings**: Writing `<span>{{ calculateTotal() }}</span>` causes the function to execute on every change detection cycle. Use a `computed()` signal instead.
2. **Missing `track` in `@for`**: Leaving out the tracking identity in `@for` ruins list performance.
3. **Memory Leaks in RxJS**: Forgetting to unsubscribe from manual `.subscribe()` calls. Use `takeUntilDestroyed()` or convert to signals via `toSignal()`.

---

## 8. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Framework Isolation: [README.md](README.md)
- Clean Code Standards: [../engineering/clean-code.md](../engineering/clean-code.md)
