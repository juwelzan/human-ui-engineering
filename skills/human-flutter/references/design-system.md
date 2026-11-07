# Centralized Design System Engineering

> **Design Tokens & System Architecture Specification** for Flutter applications built with Human Flutter Engineering.

A production-grade Flutter design system is a cohesive, mathematically grounded visual language codified into type-safe Dart classes. It coordinates color palettes, typography hierarchies, spatial grids, corner radii, elevations, and interaction states across all screens.

---

## 1. Design Token Architecture (`lib/core/theme/`)

The design system lives centrally in `lib/core/theme/`, preventing magic numbers and inconsistent styling:

```text
lib/core/theme/
├── app_colors.dart       # ColorScheme, semantic tokens, ThemeExtensions
├── app_theme.dart        # Light and Dark ThemeData builders
├── app_typography.dart   # TextTheme, font weights, line heights
├── app_spacing.dart      # 4pt/8pt spatial grid constants
├── app_radius.dart       # Border radius constants
├── app_elevation.dart    # Surface elevations and custom box shadows
├── app_breakpoints.dart  # Responsive layout breakpoints
└── theme.dart            # Unified theme barrel export
```

---

## 2. Spatial Grid & Sizing Tokens (`app_spacing.dart`)

All margins, paddings, and layout gaps adhere strictly to the **8pt/4pt mathematical spatial grid**:

```dart
// lib/core/theme/app_spacing.dart
abstract final class AppSpacing {
  static const double xxxs = 2.0;
  static const double xxs  = 4.0;
  static const double xs   = 8.0;
  static const double sm   = 12.0;
  static const double md   = 16.0;   // Default base padding
  static const double lg   = 24.0;   // Section separation
  static const double xl   = 32.0;   // Component group separation
  static const double xxl  = 48.0;   // Major viewport spacing
  static const double xxxl = 64.0;
}
```

---

## 3. Corner Radius & Shape Tokens (`app_radius.dart`)

```dart
// lib/core/theme/app_radius.dart
import 'package:flutter/material.dart';

abstract final class AppRadius {
  static const double xs  = 4.0;    // Badges, small tags
  static const double sm  = 8.0;    // Input fields, small buttons
  static const double md  = 12.0;   // Standard cards, dialogs
  static const double lg  = 16.0;   // Prominent hero cards
  static const double xl  = 24.0;   // Bottom sheets, modals
  static const double full = 999.0; // Circular pills, floating badges

  // Pre-built BorderRadius instances for zero-allocation performance
  static const BorderRadius borderSm = BorderRadius.all(Radius.circular(sm));
  static const BorderRadius borderMd = BorderRadius.all(Radius.circular(md));
  static const BorderRadius borderLg = BorderRadius.all(Radius.circular(lg));
}
```

---

## 4. Typography Scale (`app_typography.dart`)

The typography system maps directly to Material 3 type roles with deliberate line heights and letter spacing:

| Style Role | Font Size | Line Height | Weight | Usage |
|---|---|---|---|---|
| `displayLarge` | 57sp | 64dp | Bold | Hero splash statements |
| `headlineLarge`| 32sp | 40dp | SemiBold | Top screen titles |
| `headlineMedium`| 28sp| 36dp | SemiBold | Major section headers |
| `titleLarge`   | 22sp | 28dp | Medium | Card and dialog titles |
| `titleMedium`  | 16sp | 24dp | Medium | List item headers |
| `bodyLarge`    | 16sp | 24dp | Regular | Primary readable body text |
| `bodyMedium`   | 14sp | 20dp | Regular | Secondary captions |
| `labelLarge`   | 14sp | 20dp | SemiBold | Interactive button labels |
| `labelSmall`   | 11sp | 16dp | Medium | Badges, timestamps |

---

## 5. Elevation & Box Shadows (`app_elevation.dart`)

Rather than harsh generic shadows, human-centered Flutter interfaces utilize layered, subtle ambient shadows:

```dart
// lib/core/theme/app_elevation.dart
import 'package:flutter/material.dart';

abstract final class AppElevation {
  static const List<BoxShadow> level1 = [
    BoxShadow(
      color: Color(0x0A000000),
      offset: Offset(0, 1),
      blurRadius: 3,
    ),
    BoxShadow(
      color: Color(0x0F000000),
      offset: Offset(0, 1),
      blurRadius: 2,
    ),
  ];

  static const List<BoxShadow> level2 = [
    BoxShadow(
      color: Color(0x0D000000),
      offset: Offset(0, 4),
      blurRadius: 6,
      spreadRadius: -1,
    ),
  ];

  static const List<BoxShadow> level3 = [
    BoxShadow(
      color: Color(0x14000000),
      offset: Offset(0, 10),
      blurRadius: 15,
      spreadRadius: -3,
    ),
  ];
}
```

---

## 6. Centralized ThemeData Integration (`app_theme.dart`)

The master theme combines ColorScheme, TextTheme, and component themes into unified Light and Dark configurations:

```dart
// lib/core/theme/app_theme.dart
import 'package:flutter/material.dart';
import 'app_colors.dart';
import 'app_typography.dart';
import 'app_radius.dart';

abstract final class AppTheme {
  static ThemeData light({required ColorScheme colorScheme}) {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      colorScheme: colorScheme,
      textTheme: AppTypography.textTheme(colorScheme.onSurface),
      scaffoldBackgroundColor: colorScheme.surface,
      cardTheme: CardTheme(
        elevation: 0,
        shape: const RoundedRectangleBorder(borderRadius: AppRadius.borderMd),
        color: colorScheme.surfaceContainer,
      ),
      appBarTheme: AppBarTheme(
        elevation: 0,
        backgroundColor: colorScheme.surface,
        foregroundColor: colorScheme.onSurface,
      ),
      extensions: [
        AppCustomColors.light(),
      ],
    );
  }

  static ThemeData dark({required ColorScheme colorScheme}) {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      colorScheme: colorScheme,
      textTheme: AppTypography.textTheme(colorScheme.onSurface),
      scaffoldBackgroundColor: colorScheme.surface,
      cardTheme: CardTheme(
        elevation: 0,
        shape: const RoundedRectangleBorder(borderRadius: AppRadius.borderMd),
        color: colorScheme.surfaceContainer,
      ),
      appBarTheme: AppBarTheme(
        elevation: 0,
        backgroundColor: colorScheme.surface,
        foregroundColor: colorScheme.onSurface,
      ),
      extensions: [
        AppCustomColors.dark(),
      ],
    );
  }
}
```
