# Human Flutter File Structure Engineering

> Scalable, feature-first and layer-based project organization patterns for production Flutter applications.

---

## 1. Principles

1. **Context-Driven Architecture**: Scale your structure to the project. A 3-screen utility app needs a simple layer-based layout. An enterprise commerce app needs a Feature-First Clean layout.
2. **Feature Cohesion**: Group code that changes together in the same directory (`features/<feature_name>/`).
3. **Core Isolation**: Truly shared foundations (primitives, network clients, formatters) belong in `lib/core/`. Feature-specific widgets must stay within their feature directory.
4. **Mirroring Tests**: The `test/` directory must strictly mirror the `lib/` hierarchy for immediate discoverability.

---

## 2. Recommended Feature-First Architecture

Best for medium-to-large Flutter applications:

```text
lib/
├── app.dart                     # MaterialApp.router root configuration
├── main.dart                    # Application entrypoint & initialization
│
├── core/                        # Shared foundations across all features
│   ├── constants/               # API endpoints, storage keys, asset paths
│   ├── errors/                  # AppError classes, failure mappings
│   ├── network/                 # Dio client, interceptors, retry policies
│   ├── router/                  # AppRouter, routes, redirection guards
│   ├── theme/                   # AppColors, AppTypography, AppTheme, ThemeExtensions
│   ├── utils/                   # Extensions, formatters, date helpers
│   └── widgets/                 # Universal UI primitives: AppButton, AppTextField, AppCard
│
├── features/                    # Independent business domains
│   ├── auth/
│   │   ├── data/                # Data sources, DTOs, repository implementations
│   │   │   ├── datasources/     # Remote & local auth data sources
│   │   │   ├── models/          # UserDto (JSON serialization)
│   │   │   └── repositories/    # AuthRepositoryImpl
│   │   ├── domain/              # Entities and repository interfaces (Pure Dart)
│   │   │   ├── entities/        # User entity
│   │   │   └── repositories/    # AuthRepository interface
│   │   └── presentation/        # UI layer
│   │       ├── controllers/     # AuthCubit, AuthNotifier, or AuthBloc
│   │       ├── screens/         # LoginScreen, RegisterScreen
│   │       └── widgets/         # AuthHeader, SocialLoginButtons (feature-private)
│   │
│   ├── cart/
│   └── products/
│
└── l10n/                        # Localization files (app_en.arb, app_es.arb)
```

---

## 3. Lightweight Layer-Based Structure

Best for small utilities, proof-of-concepts, and internal tools (< 5 screens):

```text
lib/
├── main.dart
├── models/                      # Lightweight models / DTOs
├── services/                    # ApiService, StorageService
├── state/                       # Providers, Notifiers, or Cubits
├── screens/                     # HomeScreen, SettingsScreen
├── widgets/                     # Shared widgets
└── theme/                       # AppTheme and colors
```

> [!TIP]
> Do not force Clean Architecture (`domain/`, `usecases/`, `datasources/`) when a direct `Repository` or `Notifier` communicates cleanly with a client. Upgrade to Feature-First as complexity warrants.

---

## 4. Test Directory Organization

Every file in `lib/` should have a corresponding test file in `test/`:

```text
test/
├── core/
│   ├── network/dio_client_test.dart
│   └── theme/color_scheme_test.dart
├── features/
│   ├── auth/
│   │   ├── data/auth_repository_impl_test.dart
│   │   ├── presentation/controllers/auth_cubit_test.dart
│   │   └── presentation/screens/login_screen_test.dart
│   └── products/
└── helpers/                     # Test fixtures, mock repositories, pumps
```

---

## 5. Related References

- Architecture Patterns: [flutter-architecture.md](flutter-architecture.md)
- Folder Structure Guide: [../../../core/folder-structure.md](../../../core/folder-structure.md)
- Testing: [testing.md](testing.md)
