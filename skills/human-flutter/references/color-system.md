# Human Color Intelligence in Flutter

> Engineering guide for defining, architecting, and applying semantic, accessible color systems using Flutter's `ColorScheme`, `ThemeData`, and custom `ThemeExtension`.

---

## 1. Core Principles

Color in a Flutter app communicates status, hierarchy, and interactive affordance. Random hex codes (`Color(0xFF3B82F6)`) scattered across widget trees create visual chaos, broken dark themes, and severe accessibility contrast failures.

Always establish a coherent, semantic color palette before building screens.

---

## 2. Color Hierarchy: The 60-30-10 Rule

A production Flutter UI balances color across three tiers:
- **60% Neutral Surfaces**: Canvas, cards, sheets, lists (`surface`, `surfaceContainer`, `surfaceContainerLowest`).
- **30% Structural & Content Neutrals**: Text (`onSurface`, `onSurfaceVariant`), dividers, outlines (`outline`, `outlineVariant`).
- **10% Intentional Accent**: Primary actions (`primary`), active toggles, badges, and semantic alerts.

---

## 3. Flutter Material 3 ColorScheme Architecture

Flutter's `ColorScheme` provides 30+ standardized semantic roles:

```dart
// Theme definition in theme/app_colors.dart
class AppColorScheme {
  static const light = ColorScheme(
    brightness: Brightness.light,
    primary: Color(0xFF0F52BA),         // Sapphire blue primary action
    onPrimary: Color(0xFFFFFFFF),
    primaryContainer: Color(0xFFDCE3F9),
    onPrimaryContainer: Color(0xFF001B44),
    
    secondary: Color(0xFF4B607C),       // Slate secondary accents
    onSecondary: Color(0xFFFFFFFF),
    secondaryContainer: Color(0xFFD2E4FF),
    onSecondaryContainer: Color(0xFF041C35),

    tertiary: Color(0xFF6B5778),        // Accent metadata / tags
    onTertiary: Color(0xFFFFFFFF),

    error: Color(0xFFBA1A1A),           // Semantic error
    onError: Color(0xFFFFFFFF),
    errorContainer: Color(0xFFFFDAD6),
    onErrorContainer: Color(0xFF410002),

    surface: Color(0xFFF8F9FF),         // Base background canvas
    onSurface: Color(0xFF191C20),       // High contrast body text
    onSurfaceVariant: Color(0xFF44474E),// Secondary metadata text
    outline: Color(0xFF74777F),         // Active borders
    outlineVariant: Color(0xFFC4C6D0),  // Dividers & card outlines
  );

  static const dark = ColorScheme(
    brightness: Brightness.dark,
    primary: Color(0xFFAEC6FF),
    onPrimary: Color(0xFF002E6C),
    primaryContainer: Color(0xFF004499),
    onPrimaryContainer: Color(0xFFDCE3F9),

    secondary: Color(0xFFB3C8E8),
    onSecondary: Color(0xFF1B324C),
    secondaryContainer: Color(0xFF334963),
    onSecondaryContainer: Color(0xFFD2E4FF),

    tertiary: Color(0xFFD7BEE4),
    onTertiary: Color(0xFF3B2947),

    error: Color(0xFFFFB4AB),
    onError: Color(0xFF690005),
    errorContainer: Color(0xFF93000A),
    onErrorContainer: Color(0xFFFFDAD6),

    surface: Color(0xFF111318),
    onSurface: Color(0xFFE2E2E9),
    onSurfaceVariant: Color(0xFFC4C6D0),
    outline: Color(0xFF8E9099),
    outlineVariant: Color(0xFF44474F),
  );
}
```

---

## 4. Semantic Status Colors via ThemeExtension

Flutter's built-in `ColorScheme` lacks explicit `success`, `warning`, and `info` roles. Never hardcode green or amber hex values in widgets. Extend `ThemeExtension<AppCustomColors>`:

```dart
import 'package:flutter/material.dart';

@immutable
class AppCustomColors extends ThemeExtension<AppCustomColors> {
  final Color success;
  final Color onSuccess;
  final Color successContainer;
  final Color warning;
  final Color onWarning;
  final Color warningContainer;
  final Color info;
  final Color onInfo;

  const AppCustomColors({
    required this.success,
    required this.onSuccess,
    required this.successContainer,
    required this.warning,
    required this.onWarning,
    required this.warningContainer,
    required this.info,
    required this.onInfo,
  });

  static const light = AppCustomColors(
    success: Color(0xFF1E8E3E),
    onSuccess: Colors.white,
    successContainer: Color(0xFFE6F4EA),
    warning: Color(0xFFE37400),
    onWarning: Colors.white,
    warningContainer: Color(0xFFFEF7E0),
    info: Color(0xFF1A73E8),
    onInfo: Colors.white,
  );

  static const dark = AppCustomColors(
    success: Color(0xFF81C995),
    onSuccess: Color(0xFF0D3814),
    successContainer: Color(0xFF135223),
    warning: Color(0xFFFDD663),
    onWarning: Color(0xFF422800),
    warningContainer: Color(0xFF5B3900),
    info: Color(0xFF8AB4F8),
    onInfo: Color(0xFF042B63),
  );

  @override
  AppCustomColors copyWith({
    Color? success,
    Color? onSuccess,
    Color? successContainer,
    Color? warning,
    Color? onWarning,
    Color? warningContainer,
    Color? info,
    Color? onInfo,
  }) {
    return AppCustomColors(
      success: success ?? this.success,
      onSuccess: onSuccess ?? this.onSuccess,
      successContainer: successContainer ?? this.successContainer,
      warning: warning ?? this.warning,
      onWarning: onWarning ?? this.onWarning,
      warningContainer: warningContainer ?? this.warningContainer,
      info: info ?? this.info,
      onInfo: onInfo ?? this.onInfo,
    );
  }

  @override
  AppCustomColors lerp(ThemeExtension<AppCustomColors>? other, double t) {
    if (other is! AppCustomColors) return this;
    return AppCustomColors(
      success: Color.lerp(success, other.success, t)!,
      onSuccess: Color.lerp(onSuccess, other.onSuccess, t)!,
      successContainer: Color.lerp(successContainer, other.successContainer, t)!,
      warning: Color.lerp(warning, other.warning, t)!,
      onWarning: Color.lerp(onWarning, other.onWarning, t)!,
      warningContainer: Color.lerp(warningContainer, other.warningContainer, t)!,
      info: Color.lerp(info, other.info, t)!,
      onInfo: Color.lerp(onInfo, other.onInfo, t)!,
    );
  }
}

// Convenient BuildContext extension
extension CustomThemeContext on BuildContext {
  AppCustomColors get customColors => Theme.of(this).extension<AppCustomColors>() ?? AppCustomColors.light;
}
```

---

## 5. WCAG 2.1 Contrast Standards

1. **Body Text**: Must achieve at least **4.5:1** contrast against its background (`onSurface` on `surface`).
2. **Large Text & Headings (≥18pt or 14pt bold)**: Must achieve at least **3.0:1** contrast.
3. **Interactive Icons & Form Outlines**: Must achieve at least **3.0:1** contrast (`outline` on `surface`).
4. **Disabled States**: Reduced opacity must never render labels completely invisible (minimum 38% opacity).

---

## 6. Dynamic Color Support

When building modern Android apps, use the `dynamic_color` package to harmonize custom brand colors with Android 12+ wallpaper tones:

```dart
DynamicColorBuilder(
  builder: (ColorScheme? lightDynamic, ColorScheme? darkDynamic) {
    ColorScheme lightScheme = lightDynamic?.harmonized() ?? AppColorScheme.light;
    ColorScheme darkScheme = darkDynamic?.harmonized() ?? AppColorScheme.dark;
    return MaterialApp(
      theme: ThemeData(colorScheme: lightScheme, extensions: const [AppCustomColors.light]),
      darkTheme: ThemeData(colorScheme: darkScheme, extensions: const [AppCustomColors.dark]),
      // ...
    );
  },
)
```

---

## 7. Related References

- Design System Document: [../../../design/color-system.md](../../../design/color-system.md)
- Accessibility Audit: [accessibility.md](accessibility.md)
- Component Engineering: [components.md](components.md)
