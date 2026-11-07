# Safe Flutter Refactoring Standards

> Behavior-preserving refactoring protocols for decomposing monolithic widget trees and decoupling business logic.

---

## 1. Principles of Flutter Refactoring

1. **Preserve External Contracts**: Never change existing widget parameters, public methods, or route URLs unless explicitly instructed.
2. **Behavior-Preserving Increments**: Refactor in small, verifiable steps. Run `flutter test` after each extraction.
3. **The 200-Line Guideline**: Any widget file exceeding 200–250 lines is a prime candidate for decomposition into focused, reusable sub-widgets.
4. **Zero Accidental Deletions**: Never remove working business logic, comments, analytics triggers, or error handlers during a refactor.

---

## 2. Decomposing Monolithic Screens

### Step 1: Identify Cohesive Sub-Trees
Scan the monolithic `build()` method for distinct visual blocks (e.g. Header, Metrics Carousel, Recent Transactions, Action Bar).

### Step 2: Extract to Private `StatelessWidget` Classes
Instead of extracting private helper methods (`_buildHeader()`), extract proper private classes:

```dart
// Before: Giant 400-line OrderScreen with 5 helper methods

// After: Clean 120-line coordinator
class OrderScreen extends StatelessWidget {
  final String orderId;
  const OrderScreen({super.key, required this.orderId});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Order Details')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            _OrderStatusBanner(orderId: orderId),
            const SizedBox(height: 16),
            _OrderItemsList(orderId: orderId),
            const SizedBox(height: 24),
            _OrderShippingSummary(orderId: orderId),
          ],
        ),
      ),
    );
  }
}
```

---

## 3. Extracting Business Logic from Views

When a `StatefulWidget` contains HTTP calls, timer intervals, or complex validations:
1. Extract business logic into a dedicated `Cubit`, `StateNotifier`, or `ChangeNotifier`.
2. Keep the widget purely declarative: it reads state and triggers controller methods.
3. Verify with existing widget tests.

---

## 4. Verification Checkpoint

Before considering a refactoring task complete:
```bash
# 1. Verify zero static analysis regressions
dart analyze

# 2. Verify all existing tests pass
flutter test
```

---

## 5. Related References

- Clean Code: [../../../engineering/clean-code.md](../../../engineering/clean-code.md)
- Flutter Architecture: [flutter-architecture.md](flutter-architecture.md)
- Testing: [testing.md](testing.md)
