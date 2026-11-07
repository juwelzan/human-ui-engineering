# Shared Components Engineering (`lib/shared/`)

> **Comprehensive Engineering Guide** for constructing reusable, theme-aware Flutter widget primitives, custom painters, and layouts in `lib/shared/`.

The `lib/shared/` directory is the single source of truth for cross-feature UI primitives. It enforces high modularity, predictable constructor APIs, complete interaction states, and strict avoidance of code duplication.

---

## 1. Directory Structure & Taxonomy

```text
lib/shared/
├── widgets/            # Reusable UI primitives
│   ├── buttons/        # AppButton, AppIconButton, AppSegmentedButton
│   ├── cards/          # AppCard, AppMetricCard, AppTonalCard
│   ├── containers/     # ResponsiveContainer, GlassCard
│   ├── dialogs/        # AppAlertDialog, AppActionSheet
│   ├── inputs/         # AppTextField, AppSearchField, AppDropdown
│   ├── indicators/     # AppStatusBadge, AppProgressBar
│   ├── loaders/        # AppShimmer, AppSkeletonList, AppSpinner
│   ├── navigation/     # AppBottomBar, AppNavigationRail
│   ├── app_bars/       # AppHeaderBar, AppSliverAppBar
│   ├── avatars/        # AppUserAvatar, AppStatusAvatar
│   ├── badges/         # AppCountBadge, AppNotificationDot
│   ├── dividers/       # AppDivider, AppLabeledDivider
│   ├── menus/          # AppDropdownMenu, AppContextMenu
│   └── sheets/         # AppModalBottomSheet, AppFilterSheet
│
├── custom/             # Custom rendering & graphics
│   ├── painters/       # CustomPainter implementations (charts, canvas)
│   ├── shapes/         # CustomShapeBorder, ClipPath definitions
│   ├── borders/        # DashedBorder, GradientBorder
│   └── effects/        # ShadowDecorations, GlassMorphism
│
├── animations/         # Reusable animations & micro-interactions
│   ├── transitions/    # SharedAxisTransition, FadeSlideTransition
│   ├── implicit/       # AnimatedPressScale, AnimatedVisibility
│   └── explicit/       # ShimmerAnimation, PulseAnimation
│
└── layouts/            # Adaptive layout scaffolds
    ├── responsive/     # ResponsiveLayoutBuilder, AdaptiveGrid
    └── adaptive/       # AdaptivePlatformScaffold
```

---

## 2. Shared Component Design Rubric

Every widget placed in `lib/shared/` MUST comply with these 7 rules:

1. **Multi-Feature Usage**: Belongs in `shared/` ONLY if utilized by 2 or more distinct features. Feature-private widgets must stay in `features/<feature>/presentation/widgets/`.
2. **Named Variant Constructors**: Expose semantic constructors instead of complex boolean flags:
   ```dart
   // ✅ Clean, expressive API
   AppButton.primary({required VoidCallback onPressed, required String label});
   AppButton.secondary({required VoidCallback onPressed, required String label});
   AppButton.destructive({required VoidCallback onPressed, required String label});
   ```
3. **Theme Awareness**: Never hardcode colors, text sizes, or corner radii. Derive all visual properties from `Theme.of(context)`:
   ```dart
   final colorScheme = Theme.of(context).colorScheme;
   final textTheme = Theme.of(context).textTheme;
   ```
4. **All Interactive States Handled**: Default, Hover, Pressed, Focused, Disabled, and Loading.
5. **No Monolithic Parameter Lists**: Keep constructor parameters concise (≤ 6 core parameters). Avoid parameter bloat.
6. **Built-in Accessibility**: Ensure minimum 48x48dp touch targets (`kMinInteractiveDimension`), accessible contrast, and explicit `Semantics` wrappers.
7. **Const Constructors**: Expose `const` constructors wherever possible to optimize Flutter's widget rebuild pipeline.

---

## 3. Production Component Example: `AppButton`

```dart
// lib/shared/widgets/buttons/app_button.dart
import 'package:flutter/material.dart';

enum AppButtonVariant { primary, secondary, outline, destructive }

class AppButton extends StatelessWidget {
  const AppButton.primary({
    super.key,
    required this.onPressed,
    required this.label,
    this.icon,
    this.isLoading = false,
    this.isFullWidth = false,
  }) : variant = AppButtonVariant.primary;

  const AppButton.secondary({
    super.key,
    required this.onPressed,
    required this.label,
    this.icon,
    this.isLoading = false,
    this.isFullWidth = false,
  }) : variant = AppButtonVariant.secondary;

  const AppButton.destructive({
    super.key,
    required this.onPressed,
    required this.label,
    this.icon,
    this.isLoading = false,
    this.isFullWidth = false,
  }) : variant = AppButtonVariant.destructive;

  final VoidCallback? onPressed;
  final String label;
  final Widget? icon;
  final bool isLoading;
  final bool isFullWidth;
  final AppButtonVariant variant;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final colorScheme = theme.colorScheme;

    final (Color bg, Color fg, BorderSide? border) = switch (variant) {
      AppButtonVariant.primary => (
        colorScheme.primary,
        colorScheme.onPrimary,
        null,
      ),
      AppButtonVariant.secondary => (
        colorScheme.secondaryContainer,
        colorScheme.onSecondaryContainer,
        null,
      ),
      AppButtonVariant.outline => (
        Colors.transparent,
        colorScheme.primary,
        BorderSide(color: colorScheme.outline),
      ),
      AppButtonVariant.destructive => (
        colorScheme.error,
        colorScheme.onError,
        null,
      ),
    };

    final buttonStyle = ElevatedButton.styleFrom(
      backgroundColor: bg,
      foregroundColor: fg,
      elevation: 0,
      side: border,
      minimumSize: Size(isFullWidth ? double.infinity : 64, 48),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
    );

    return ConstrainedBox(
      constraints: BoxConstraints(
        minHeight: 48,
        minWidth: isFullWidth ? double.infinity : 64,
      ),
      child: ElevatedButton(
        style: buttonStyle,
        onPressed: isLoading ? null : onPressed,
        child: isLoading
            ? SizedBox(
                width: 20,
                height: 20,
                child: CircularProgressIndicator(
                  strokeWidth: 2,
                  color: fg,
                ),
              )
            : Row(
                mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  if (icon != null) ...[icon!, const SizedBox(width: 8)],
                  Text(
                    label,
                    style: theme.textTheme.labelLarge?.copyWith(
                      color: fg,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
      ),
    );
  }
}
```

---

## 4. Custom Graphics & Rendering (`lib/shared/custom/`)

When custom visual elements cannot be achieved with standard composited widgets, implement high-performance `CustomPainter` instances:

```dart
// lib/shared/custom/painters/circle_progress_painter.dart
import 'dart:math' as math;
import 'package:flutter/material.dart';

class CircleProgressPainter extends CustomPainter {
  const CircleProgressPainter({
    required this.progress,
    required this.trackColor,
    required this.progressColor,
    this.strokeWidth = 6.0,
  });

  final double progress;
  final Color trackColor;
  final Color progressColor;
  final double strokeWidth;

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = (size.width - strokeWidth) / 2;

    final trackPaint = Paint()
      ..color = trackColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = strokeWidth;

    final progressPaint = Paint()
      ..color = progressColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = strokeWidth
      ..strokeCap = StrokeCap.round;

    canvas.drawCircle(center, radius, trackPaint);
    final sweepAngle = 2 * math.pi * progress;
    canvas.drawArc(
      Rect.fromCircle(center: center, radius: radius),
      -math.pi / 2,
      sweepAngle,
      false,
      progressPaint,
    );
  }

  @override
  bool shouldRepaint(covariant CircleProgressPainter oldDelegate) {
    return oldDelegate.progress != progress ||
        oldDelegate.progressColor != progressColor ||
        oldDelegate.trackColor != trackColor;
  }
}
```

---

## 5. Inspection Before Creation Rule

Before authoring any new widget primitive:
1. Search `lib/shared/widgets/` to verify if an equivalent or adaptable component already exists.
2. If an existing widget covers 80% of the functionality, extend its constructor or expose a new variant rather than cloning a near-identical widget.
3. Keep barrel files (`widgets.dart`, `custom.dart`, `shared.dart`) updated so consumers import via a clean unified namespace: `import 'package:app/shared/shared.dart';`.
