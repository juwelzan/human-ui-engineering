# Flutter Animation Engineering & Micro-Interactions

> **60fps/120fps Animation Architecture** for fluid, meaningful, and performance-aware Flutter motion design.

Motion in Flutter must communicate spatial relationships, guide user focus, provide immediate interaction feedback, and delight users without causing frame drops or visual disorientation.

---

## 1. Principles of Meaningful Motion

1. **Purposeful Feedback**: Every animation must serve an explicit communicative function (e.g., tap scale confirmation, drawer elevation, step progress).
2. **Strict Frame Budget**: Maintain 60fps (≤16.6ms) or 120fps (≤8.3ms) per frame budget on UI and raster threads. Never cause jank by rebuilding parent widget trees during ticks.
3. **Respect Reduced Motion**: Always inspect `MediaQuery.disableAnimationsOf(context)` or `MediaQuery.accessibleNavigationOf(context)`. If enabled, skip the tween duration and render the final state immediately.

---

## 2. Animation Categories & When to Use

| Category | Typical Flutter Classes | Best For | Frame Cost |
|---|---|---|---|
| **Implicit** | `AnimatedContainer`, `AnimatedOpacity`, `AnimatedSwitcher`, `AnimatedCrossFade` | Simple state-driven property transitions | Low (built-in optimizations) |
| **Explicit** | `AnimationController`, `Tween`, `CurvedAnimation`, `AnimatedBuilder` | Loops, scrubbing, physics-driven, multi-stage choreographies | Minimal if children are cached |
| **Shared Element** | `Hero`, `CustomTransitionPage` (GoRouter) | Spatial continuity between list and detail screens | Medium (runs across route pop/push) |
| **Micro-Interactions**| `AnimatedScale`, `Transform.scale`, `InkWell` / `InkResponse` | Tap press down, heart toggle, bookmark save | Very low |

---

## 3. Implementation Patterns

### A. Seamless State Switcher (`AnimatedSwitcher`)
```dart
AnimatedSwitcher(
  duration: const Duration(milliseconds: 250),
  switchInCurve: Curves.easeOutCubic,
  switchOutCurve: Curves.easeInCubic,
  transitionBuilder: (child, animation) {
    return FadeTransition(
      opacity: animation,
      child: SlideTransition(
        position: Tween<Offset>(
          begin: const Offset(0.0, 0.08),
          end: Offset.zero,
        ).animate(animation),
        child: child,
      ),
    );
  },
  child: isLoading
      ? const ShimmerDashboard(key: ValueKey('shimmer'))
      : const ContentDashboard(key: ValueKey('content')),
)
```

### B. Micro-Interaction: Tap Press Down Scale
```dart
// lib/shared/animations/implicit/animated_press_scale.dart
import 'package:flutter/material.dart';

class AnimatedPressScale extends StatefulWidget {
  const AnimatedPressScale({
    super.key,
    required this.child,
    required this.onTap,
  });

  final Widget child;
  final VoidCallback onTap;

  @override
  State<AnimatedPressScale> createState() => _AnimatedPressScaleState();
}

class _AnimatedPressScaleState extends State<AnimatedPressScale> {
  bool _isPressed = false;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTapDown: (_) => setState(() => _isPressed = true),
      onTapUp: (_) => setState(() => _isPressed = false),
      onTapCancel: () => setState(() => _isPressed = false),
      onTap: widget.onTap,
      child: AnimatedScale(
        scale: _isPressed ? 0.96 : 1.0,
        duration: const Duration(milliseconds: 100),
        curve: Curves.easeOutCubic,
        child: widget.child,
      ),
    );
  }
}
```

---

## 4. Animation Performance Golden Rules

1. **RepaintBoundary**: Wrap animating subtrees in a `RepaintBoundary` to isolate canvas repainting and prevent invalidating the entire screen.
2. **Never Animate `Opacity` Widget**: Calling `Opacity(opacity: animation.value)` creates an expensive offscreen compositing layer on every tick. Always use `FadeTransition` or `AnimatedOpacity`.
3. **Cache Static Children**: Always pass static child widgets into the `child` parameter of `AnimatedBuilder` so Flutter does not re-instantiate identical widgets 60 times a second.
4. **Mandatory Disposal**: Always dispose `AnimationController` inside `State.dispose()` to prevent memory leaks and dangling frame tickers.

---

## 5. Related References

- [permission-system.md](permission-system.md)
- [shared-components.md](shared-components.md)
- [performance.md](performance.md)
- [animation.md](animation.md)
