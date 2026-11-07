# Human Flutter Component Engineering

> Specifications, patterns, and best practices for authoring reusable, theme-aware, and performant Flutter widget primitives.

---

## 1. Principles of Flutter Component Design

1. **Composition Over Inheritance**: Build rich widgets by combining core Flutter primitives (`Padding`, `Row`, `Column`, `InkWell`) rather than deep class hierarchies.
2. **Explicit Constructor APIs**: Avoid boolean soup. Use named constructors for variants (`AppButton.primary`, `AppButton.secondary`, `AppButton.destructive`).
3. **`const` Support**: Every widget primitive with immutable configuration must provide a `const` constructor.
4. **Theme-Aware**: Components must derive colors, radii, and typography from `Theme.of(context)` rather than hardcoding style properties.
5. **Interactive State Completeness**: Handle normal, hover, pressed, focused, disabled, and loading states seamlessly.

---

## 2. Core Reusable Primitives Catalog

### 1. AppButton (Interactive Action Trigger)
```dart
enum AppButtonVariant { primary, secondary, ghost, destructive }

class AppButton extends StatelessWidget {
  final String label;
  final VoidCallback? onPressed;
  final bool isLoading;
  final Widget? leadingIcon;
  final AppButtonVariant variant;

  const AppButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.isLoading = false,
    this.leadingIcon,
    this.variant = AppButtonVariant.primary,
  });

  const AppButton.secondary({
    super.key,
    required this.label,
    required this.onPressed,
    this.isLoading = false,
    this.leadingIcon,
  }) : variant = AppButtonVariant.secondary;

  const AppButton.destructive({
    super.key,
    required this.label,
    required this.onPressed,
    this.isLoading = false,
    this.leadingIcon,
  }) : variant = AppButtonVariant.destructive;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isEnabled = onPressed != null && !isLoading;

    Color bg;
    Color fg;
    BorderSide border = BorderSide.none;

    switch (variant) {
      case AppButtonVariant.primary:
        bg = theme.colorScheme.primary;
        fg = theme.colorScheme.onPrimary;
        break;
      case AppButtonVariant.secondary:
        bg = theme.colorScheme.surface;
        fg = theme.colorScheme.onSurface;
        border = BorderSide(color: theme.colorScheme.outlineVariant);
        break;
      case AppButtonVariant.ghost:
        bg = Colors.transparent;
        fg = theme.colorScheme.primary;
        break;
      case AppButtonVariant.destructive:
        bg = theme.colorScheme.error;
        fg = theme.colorScheme.onError;
        break;
    }

    return Semantics(
      button: true,
      enabled: isEnabled,
      label: label,
      child: SizedBox(
        height: 48, // 48dp minimum touch target
        child: FilledButton(
          style: FilledButton.styleFrom(
            backgroundColor: bg,
            foregroundColor: fg,
            disabledBackgroundColor: bg.withOpacity(0.38),
            disabledForegroundColor: fg.withOpacity(0.38),
            side: border,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
            padding: const EdgeInsets.symmetric(horizontal: 20),
          ),
          onPressed: isEnabled ? onPressed : null,
          child: isLoading
              ? SizedBox(
                  width: 20,
                  height: 20,
                  child: CircularProgressIndicator(strokeWidth: 2, color: fg),
                )
              : Row(
                  mainAxisSize: MainAxisSize.min,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    if (leadingIcon != null) ...[
                      leadingIcon!,
                      const SizedBox(width: 8),
                    ],
                    Text(label, style: theme.textTheme.labelLarge?.copyWith(color: fg)),
                  ],
                ),
        ),
      ),
    );
  }
}
```

### 2. AppCard (Content Container)
```dart
class AppCard extends StatelessWidget {
  final Widget child;
  final EdgeInsetsGeometry padding;
  final VoidCallback? onTap;

  const AppCard({
    super.key,
    required this.child,
    this.padding = const EdgeInsets.all(16),
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Material(
      color: theme.colorScheme.surface,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: BorderSide(color: theme.colorScheme.outlineVariant.withOpacity(0.6)),
      ),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: onTap,
        child: Padding(padding: padding, child: child),
      ),
    );
  }
}
```

### 3. AppTextField (Form Input Primitive)
```dart
class AppTextField extends StatelessWidget {
  final String label;
  final String? hint;
  final TextEditingController? controller;
  final String? errorText;
  final bool obscureText;
  final TextInputType keyboardType;
  final Widget? prefixIcon;
  final Widget? suffixIcon;
  final ValueChanged<String>? onChanged;

  const AppTextField({
    super.key,
    required this.label,
    this.hint,
    this.controller,
    this.errorText,
    this.obscureText = false,
    this.keyboardType = TextInputType.text,
    this.prefixIcon,
    this.suffixIcon,
    this.onChanged,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: theme.textTheme.labelMedium?.copyWith(
            fontWeight: FontWeight.w600,
            color: theme.colorScheme.onSurfaceVariant,
          ),
        ),
        const SizedBox(height: 6),
        TextField(
          controller: controller,
          obscureText: obscureText,
          keyboardType: keyboardType,
          onChanged: onChanged,
          decoration: InputDecoration(
            hintText: hint,
            errorText: errorText,
            prefixIcon: prefixIcon,
            suffixIcon: suffixIcon,
            filled: true,
            fillColor: theme.colorScheme.surfaceContainerLowest,
            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(color: theme.colorScheme.outlineVariant),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(color: theme.colorScheme.outlineVariant),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(10),
              borderSide: BorderSide(color: theme.colorScheme.primary, width: 2),
            ),
          ),
        ),
      ],
    );
  }
}
```

---

## 3. Custom Rendering: CustomPaint & RenderBox

When standard layout widgets cannot achieve the required visual performance (e.g. interactive charts, signature pads, particle animations):

### CustomPainter Rules:
1. Always implement `shouldRepaint` accurately; never return `true` blindly.
2. Cache complex `Paint` objects and `Path`s outside `paint()` if possible.
3. Wrap animating `CustomPaint` in a `RepaintBoundary`.

```dart
class SparklinePainter extends CustomPainter {
  final List<double> dataPoints;
  final Color lineColor;

  SparklinePainter({required this.dataPoints, required this.lineColor});

  @override
  void paint(Canvas canvas, Size size) {
    if (dataPoints.length < 2) return;
    final paint = Paint()
      ..color = lineColor
      ..strokeWidth = 2.0
      ..style = PaintingStyle.stroke;

    final path = Path();
    final stepX = size.width / (dataPoints.length - 1);
    final maxVal = dataPoints.reduce((a, b) => a > b ? a : b);
    final minVal = dataPoints.reduce((a, b) => a < b ? a : b);
    final range = (maxVal - minVal) == 0 ? 1.0 : (maxVal - minVal);

    for (int i = 0; i < dataPoints.length; i++) {
      final x = i * stepX;
      final y = size.height - ((dataPoints[i] - minVal) / range * size.height);
      if (i == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(path, paint);
  }

  @override
  bool shouldRepaint(covariant SparklinePainter oldDelegate) {
    return oldDelegate.dataPoints != dataPoints || oldDelegate.lineColor != lineColor;
  }
}
```

---

## 4. Related References

- Buttons: [../../../components/buttons.md](../../../components/buttons.md)
- Cards: [../../../components/cards.md](../../../components/cards.md)
- Forms & Text Fields: [../../../components/forms.md](../../../components/forms.md)
- Loading States: [../../../components/loading-states.md](../../../components/loading-states.md)
- Performance: [performance.md](performance.md)
