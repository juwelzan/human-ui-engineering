# Modern Dart 3 Coding Standards

> Strict standards for clean, type-safe, maintainable Dart code in production Flutter applications.

---

## 1. Principles

1. **Sound Null Safety**: Never use the null assertion operator (`!`) as an escape hatch. Use pattern matching, null-aware operators (`?.`, `??`), or early guard clauses.
2. **Dart 3 Features**: Leverage sealed classes, pattern matching, records, and switch expressions to eliminate boilerplate.
3. **Immutability First**: Mark state classes `@immutable` or use records. Mutating shared in-memory objects leads to silent desynchronization bugs.
4. **Effective Dart**: Follow standard naming conventions (camelCase for members, PascalCase for types, lowercase_with_underscores for files).

---

## 2. Sealed Classes for Type-Safe UI States

Model state hierarchies with `sealed class` to ensure exhaustive compile-time checking:

```dart
// Explicit UI state hierarchy
sealed class ProfileState {
  const ProfileState();
}

class ProfileInitial extends ProfileState {
  const ProfileInitial();
}

class ProfileLoading extends ProfileState {
  const ProfileLoading();
}

class ProfileSuccess extends ProfileState {
  final UserProfile profile;
  const ProfileSuccess(this.profile);
}

class ProfileFailure extends ProfileState {
  final String errorMessage;
  const ProfileFailure(this.errorMessage);
}

// Exhaustive pattern matching in Flutter widget build()
Widget build(BuildContext context, ProfileState state) {
  return switch (state) {
    ProfileInitial() => const SizedBox.shrink(),
    ProfileLoading() => const AppShimmerLoading(),
    ProfileSuccess(:final profile) => ProfileDetailsCard(profile: profile),
    ProfileFailure(:final errorMessage) => AppErrorBanner(message: errorMessage),
  }; // Compiler guarantees all cases are handled!
}
```

---

## 3. Records & Destructuring

Use Dart 3 records for lightweight multiple return values instead of single-use tuple classes:

```dart
// Returning pagination metadata and items
(List<Transaction> items, {int totalCount, bool hasNextPage}) fetchTransactions() {
  // ...
  return (items, totalCount: 140, hasNextPage: true);
}

// Consuming with destructuring
final (items, totalCount: count, hasNextPage: _) = fetchTransactions();
```

---

## 4. Async Best Practices & Error Handling

### The Result Pattern for Domain & Data Layers
Never let raw network exceptions leak into presentation widgets:

```dart
sealed class Result<T> {
  const Result();
}

class Success<T> extends Result<T> {
  final T data;
  const Success(this.data);
}

class Failure<T> extends Result<T> {
  final AppError error;
  const Failure(this.error);
}

// In Repository
Future<Result<UserProfile>> getUserProfile(String userId) async {
  try {
    final response = await dio.get('/users/$userId');
    final profile = UserProfile.fromJson(response.data);
    return Success(profile);
  } on DioException catch (e) {
    return Failure(AppError.fromDio(e));
  } catch (e, stack) {
    return Failure(AppError.unexpected(e, stack));
  }
}
```

---

## 5. Recommended `analysis_options.yaml`

Enforce high standards via static analysis:

```yaml
include: package:flutter_lints/flutter.yaml

analyzer:
  language:
    strict-casts: true
    strict-inference: true
    strict-raw-types: true
  errors:
    missing_required_param: error
    missing_return: error
    todo: ignore

linter:
  rules:
    - prefer_const_constructors
    - prefer_const_declarations
    - avoid_print
    - unawaited_futures
    - cancel_subscriptions
    - close_sinks
    - use_super_parameters
    - prefer_final_locals
    - sort_constructors_first
```

---

## 6. Related References

- Clean Code: [../../../engineering/clean-code.md](../../../engineering/clean-code.md)
- Code Standards: [../../../engineering/code-standards.md](../../../engineering/code-standards.md)
- Architecture: [flutter-architecture.md](flutter-architecture.md)
