# Component Testing Standards

> Methodologies for testing UI components in isolation: state coverage, event assertions, accessibility checks, and resilient queries.

---

## 1. Purpose

Component testing validates that UI primitives and composite widgets render correctly, respond to user inputs, handle edge-case states, and preserve accessibility invariants. Testing implementation details (e.g. asserting internal CSS class names or private state variables) produces brittle tests that break on simple refactors.

This guide defines the engineering standard for component test suites.

---

## 2. The 5-Stage Component Test Battery

Every production shared component should pass these five test scenarios:

```mermaid
flowchart LR
    T1[1. Default Render] --> T2[2. Interactive Event]
    T2 --> T3[3. Disabled Guard]
    T3 --> T4[4. Loading Lock]
    T4 --> T5[5. Error & A11y]
```

### 1. Default Rendering
- Asserts that text labels, icons, and child elements render with correct hierarchy.
- Queries by **accessible role** (`getByRole('button', { name: /save/i })`, `find.bySemanticsLabel('Save')`).

### 2. Interactive Events
- Simulates user clicks or taps using user-event dispatchers.
- Asserts that the corresponding `onClick` or `onPressed` callback fired with expected arguments.

### 3. Disabled Guard
- Sets `disabled = true`.
- Verifies that clicking does **NOT** fire the callback.
- Verifies that `aria-disabled="true"` or platform disabled semantics are present.

### 4. Loading Lock
- Sets `isLoading = true`.
- Asserts that the progress spinner is displayed.
- Asserts that duplicate clicks are blocked.
- Asserts that the button does not collapse or jitter in width.

### 5. Error & Accessibility Conformance
- Sets `hasError = true` and `errorMessage = "Invalid email"`.
- Asserts that the error text is visible.
- Asserts that the input has `aria-invalid="true"` and `aria-describedby` matching the error ID.

---

## 3. Reference Test Implementations

### A. React Testing Library (React / Next.js)
```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button Primitive', () => {
  it('fires onClick callback on click', async () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Submit</Button>);
    
    await userEvent.click(screen.getByRole('button', { name: /submit/i }));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('prevents click events when disabled', async () => {
    const handleClick = vi.fn();
    render(<Button disabled onClick={handleClick}>Submit</Button>);
    
    await userEvent.click(screen.getByRole('button', { name: /submit/i }));
    expect(handleClick).not.toHaveBeenCalled();
    expect(screen.getByRole('button', { name: /submit/i })).toBeDisabled();
  });
});
```

### B. Flutter Widget Test (`testWidgets`)
```dart
testWidgets('AppButton displays spinner and blocks tap when loading', (tester) async {
  bool tapped = false;
  await tester.pumpWidget(
    MaterialApp(
      home: Scaffold(
        body: AppButton(
          label: 'Submit',
          isLoading: true,
          onPressed: () => tapped = true,
        ),
      ),
    ),
  );

  expect(find.byType(CircularProgressIndicator), findsOneWidget);
  await tester.tap(find.byType(AppButton));
  expect(tapped, isFalse);
});
```

---

## 4. Testing Anti-Patterns to Avoid

1. **Testing CSS Class Names**: Writing `expect(element.classList.contains('bg-blue-600')).toBe(true)`. Test whether the button is accessible and clickable, not its internal utility class.
2. **Missing Wrapper Providers**: Testing components that require ThemeContext or NavigationContext without wrapping them in a test harness, resulting in false test crashes.
3. **Flaky Timers**: Using real `setTimeout` in tests instead of fake timers (`vi.useFakeTimers()` / `tester.pump(duration)`).

---

## 5. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Testing Standards: [../quality/testing.md](../quality/testing.md)
- Component Principles: [component-principles.md](component-principles.md)
- Buttons: [buttons.md](buttons.md)
- Forms Architecture: [forms.md](forms.md)
