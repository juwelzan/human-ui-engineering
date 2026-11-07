# Mandatory Flutter Project Structure (`lib/core/`, `lib/shared/`, `lib/features/`)

> **Standard Project Architecture Specification** for all Flutter applications generated or maintained by the Human Flutter Engineering system.

Whenever creating a new Flutter application, generating modular architecture, or refactoring existing codebases, the agent **MUST** enforce the 3-tier top-level structure:

```text
lib/
├── core/       # Global foundational infrastructure and configuration
├── shared/     # Cross-feature reusable widgets, custom painters, and animations
└── features/   # Independent, feature-first functional modules
```

Do not replace this architecture with alternative structures without explicit user permission.

---

## 1. `lib/core/` — Foundational Infrastructure

The `core/` folder hosts application-wide, non-feature-specific foundational infrastructure. It has zero knowledge of feature business logic or domain entities.

### Directory Layout
```text
lib/core/
├── config/             # App flavors, environment variables (AppConfig, Env)
├── constants/          # Immutable app constants, API endpoints, asset paths
├── errors/             # Failure definitions (ServerFailure, CacheFailure)
├── exceptions/         # System exceptions (NetworkException, ParseException)
├── extensions/         # Useful Dart extensions (BuildContext, String, DateTime)
├── helpers/            # Reusable helper functions and formatters
├── initializers/       # Async initialization routines (Firebase, local storage)
├── network/            # HTTP clients, Dio interceptors, SSL pinning
├── routing/            # Router configuration (GoRouter, AppRoutes, Guards)
├── services/           # Global services (Connectivity, Analytics, Permissions)
├── storage/            # Local storage clients (SecureStorage, SharedPreferences)
├── theme/              # Design tokens and theme infrastructure
│   ├── app_colors.dart       # Color tokens and ColorScheme definitions
│   ├── app_theme.dart        # Light and Dark ThemeData constructors
│   ├── app_typography.dart   # TextTheme configurations
│   ├── app_spacing.dart      # Spacing tokens (4pt/8pt spatial grid)
│   ├── app_radius.dart       # Corner radius constants
│   └── app_elevation.dart    # Surface elevation and shadow tokens
├── utils/              # Pure algorithmic utilities and loggers
└── core.dart           # Barrel export file
```

### Core Responsibilities & Rules
- **No Feature Logic**: Never place feature-specific UI widgets or feature state inside `core/`.
- **Minimal Surface**: Create only the directories and files genuinely required by the application.
- **Dependency Flow**: `features/` may import `core/`, but `core/` must never import `features/` or `shared/`.

---

## 2. `lib/shared/` — Reusable UI & Supporting Components

The `shared/` folder contains reusable UI widgets, visual primitives, animations, and presentation models that are genuinely used across multiple features and screens.

### Directory Layout
```text
lib/shared/
├── widgets/            # Reusable UI primitives
│   ├── buttons/        # AppButton, IconButton, GhostButton
│   ├── cards/          # AppCard, ElevatedCard, OutlineCard
│   ├── containers/     # ResponsiveContainer, GlassContainer
│   ├── dialogs/        # ConfirmDialog, InfoDialog, ActionSheet
│   ├── inputs/         # AppTextField, DropdownField, CheckboxField
│   ├── indicators/     # StatusBadge, StepIndicator, ProgressDots
│   ├── loaders/        # ShimmerBox, SkeletonLoader, CircularProgress
│   ├── navigation/     # AppNavigationBar, AdaptiveNavRail
│   ├── app_bars/       # CustomAppBar, CollapsibleAppBar
│   ├── avatars/        # UserAvatar, GroupAvatar
│   ├── badges/         # CountBadge, DotBadge
│   ├── dividers/       # SectionDivider, LabeledDivider
│   ├── menus/          # ContextMenu, DropdownMenu
│   ├── sheets/         # ModalBottomSheet, DragHandleSheet
│   └── widgets.dart    # Widgets barrel export
│
├── custom/             # Custom rendering and drawing
│   ├── painters/       # CustomPainter implementations
│   ├── shapes/         # CustomShapeBorder, ClipPaths
│   ├── borders/        # DashedBorder, GradientBorder
│   ├── layouts/        # FlowLayout, OverlapLayout
│   ├── effects/        # ShadowDecorations, GlassMorphism
│   └── custom.dart     # Custom barrel export
│
├── animations/         # Reusable animation components
│   ├── controllers/    # Shared animation controllers
│   ├── transitions/    # PageTransitions, SharedAxisTransition
│   ├── implicit/       # AnimatedPressScale, AnimatedVisibility
│   ├── explicit/       # PulseAnimation, ShimmerEffect
│   ├── effects/        # ParticleEffects, ConfettiEffect
│   └── animations.dart # Animations barrel export
│
├── layouts/            # Adaptive structural scaffolds
│   ├── responsive/     # ResponsiveLayoutBuilder, BreakpointScaffold
│   ├── adaptive/       # AdaptivePlatformWidget, WindowSizeLayout
│   └── layouts.dart    # Layouts barrel export
│
├── components/         # Composite shared UI blocks
├── models/             # Shared presentation models (DropdownItem, ActionItem)
├── enums/              # Shared visual enums (ButtonVariant, CardElevation)
└── shared.dart         # Universal shared barrel export
```

### Shared Folder Rules
1. **Genuine Reusability**: A component belongs in `shared/` ONLY when it is used by two or more independent features.
2. **Feature Isolation**: Never move feature-specific components into `shared/`. Keep them inside `features/<feature>/presentation/widgets/`.
3. **No Duplication**: Inspect `shared/` before creating a new widget primitive.
4. **Clean API**: Every shared component must have a focused API, sound null safety, theme awareness (`Theme.of(context)`), and unit/widget tests.

---

## 3. `lib/features/` — Feature-First Modules

All business logic, user journeys, screens, and feature-specific components live inside `features/`. Every feature is self-contained.

### Directory Layout
```text
lib/features/
├── <feature_name>/
│   ├── data/                   # Data Access Layer
│   │   ├── datasources/        # Remote API endpoints, local cache
│   │   ├── models/             # DTOs, JSON serialization (fromJson/toJson)
│   │   └── repositories/       # Repository implementations (implements domain)
│   │
│   ├── domain/                 # Core Business Logic Layer (Clean Architecture)
│   │   ├── entities/           # Pure Dart business models (@immutable)
│   │   ├── repositories/       # Abstract repository interfaces
│   │   └── usecases/           # Single-responsibility business use cases
│   │
│   ├── presentation/           # User Interface Layer
│   │   ├── screens/            # Full-screen views (or pages/)
│   │   ├── pages/              # Composite multi-tab pages
│   │   ├── widgets/            # Feature-private reusable widgets
│   │   ├── components/         # Micro-components scoped to this feature
│   │   └── state/              # State management (BLoC, Cubit, Notifier, Controller)
│   │
│   ├── <feature_name>.dart     # Public feature interface
│   └── README.md               # Feature documentation and scope
```

### Scalability Principles
- **Small Features**: Do not force all 3 layers (`data`, `domain`, `presentation`) onto trivial features. A simple utility feature may contain just `presentation/` and `state/`.
- **Complex Features**: Full Clean Architecture with `domain/` use cases is recommended for mission-critical, complex financial, auth, or transactional domains.
- **Independence**: Features should not import internal widgets from other features. If cross-feature interaction is required, route via domain contracts or shared models.

---

## 4. Test Directory Mirroring

The `test/` directory MUST mirror the structure of `lib/` exactly:

```text
test/
├── core/
│   ├── network/
│   └── theme/
├── shared/
│   ├── widgets/
│   └── custom/
└── features/
    └── <feature_name>/
        ├── data/
        ├── domain/
        └── presentation/
```
