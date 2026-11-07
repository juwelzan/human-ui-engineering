# Human Typography Engineering in Flutter

> Typographic scale, TextTheme architecture, custom font loading, and accessibility scaling in Flutter.

---

## 1. Principles

Typography establishes reading flow, structural hierarchy, and brand identity. In Flutter, unstructured `TextStyle` declarations scattered across screens create disjointed sizing, broken line-heights, and severe layout overflow when users adjust OS-level text scaling.

---

## 2. Flutter Material 3 TextTheme Hierarchy

Configure a central `TextTheme` with mathematically grounded scale and line-heights:

```dart
// theme/app_typography.dart
import 'package:flutter/material.dart';

class AppTypography {
  static const String fontFamily = 'Inter';

  static const TextTheme textTheme = TextTheme(
    // Display: Hero banners & splash numbers
    displayLarge: TextStyle(fontSize: 48, fontWeight: FontWeight.w700, height: 1.15, letterSpacing: -1.0),
    displayMedium: TextStyle(fontSize: 36, fontWeight: FontWeight.w700, height: 1.2, letterSpacing: -0.5),

    // Headlines: Screen titles & major section headers
    headlineLarge: TextStyle(fontSize: 28, fontWeight: FontWeight.w600, height: 1.25, letterSpacing: -0.25),
    headlineMedium: TextStyle(fontSize: 24, fontWeight: FontWeight.w600, height: 1.3),
    headlineSmall: TextStyle(fontSize: 20, fontWeight: FontWeight.w600, height: 1.35),

    // Titles: Card titles, modal headers, list section headers
    titleLarge: TextStyle(fontSize: 18, fontWeight: FontWeight.w600, height: 1.4),
    titleMedium: TextStyle(fontSize: 16, fontWeight: FontWeight.w500, height: 1.45),
    titleSmall: TextStyle(fontSize: 14, fontWeight: FontWeight.w500, height: 1.45),

    // Body: Paragraphs, descriptions, user inputs
    bodyLarge: TextStyle(fontSize: 16, fontWeight: FontWeight.w400, height: 1.5),
    bodyMedium: TextStyle(fontSize: 14, fontWeight: FontWeight.w400, height: 1.5),
    bodySmall: TextStyle(fontSize: 12, fontWeight: FontWeight.w400, height: 1.45),

    // Labels: Buttons, badges, metadata, captions
    labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.w600, height: 1.25, letterSpacing: 0.1),
    labelMedium: TextStyle(fontSize: 12, fontWeight: FontWeight.w500, height: 1.3, letterSpacing: 0.25),
    labelSmall: TextStyle(fontSize: 11, fontWeight: FontWeight.w500, height: 1.3, letterSpacing: 0.5),
  );
}
```

---

## 3. Dynamic Type & TextScaler Safety

Users frequently increase system font size for readability. Unconstrained widgets will trigger `RenderFlex overflowed by X pixels`. 

Always enforce responsive text safety:
1. **Never use fixed heights on text containers**: Avoid `Container(height: 40, child: Text(...))`. Use `Padding` or let intrinsic dimensions size the widget.
2. **Use TextScaler.clamp**: Restrict extreme scaling to prevent layout destruction while preserving accessibility:
   ```dart
   // In MaterialApp.builder
   MaterialApp(
     builder: (context, child) {
       final mediaQuery = MediaQuery.of(context);
       return MediaQuery(
         data: mediaQuery.copyWith(
           textScaler: mediaQuery.textScaler.clamp(
             minScaleFactor: 0.85,
             maxScaleFactor: 1.35,
           ),
         ),
         child: child!,
       );
     },
   );
   ```
3. **Handle Long Strings with TextOverflow**: Always provide `overflow: TextOverflow.ellipsis` and `maxLines` on constrained titles:
   ```dart
   Text(
     product.title,
     style: Theme.of(context).textTheme.titleMedium,
     maxLines: 1,
     overflow: TextOverflow.ellipsis,
   )
   ```

---

## 4. Custom Font Loading Best Practices

Prefer bundling fonts locally in `pubspec.yaml` to avoid network latency and layout shifting:

```yaml
flutter:
  fonts:
    - family: Inter
      fonts:
        - asset: assets/fonts/Inter-Regular.ttf
          weight: 400
        - asset: assets/fonts/Inter-Medium.ttf
          weight: 500
        - asset: assets/fonts/Inter-SemiBold.ttf
          weight: 600
        - asset: assets/fonts/Inter-Bold.ttf
          weight: 700
```

---

## 5. Related References

- Typography Guide: [../../../design/typography.md](../../../design/typography.md)
- Color System: [color-system.md](color-system.md)
- Responsive Design: [responsive-design.md](responsive-design.md)
