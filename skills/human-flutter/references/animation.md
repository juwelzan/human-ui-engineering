# Human Flutter Animation Engineering

> Fluid, meaningful, and performance-aware animations across implicit, explicit, and physics-driven Flutter patterns.

---

## 1. Principles of Motion

1. **Purposeful Motion**: Every animation must serve a clear function: confirming an action, directing focus, or establishing spatial continuity. Avoid gratuitous, distracting animations.
2. **Performance First**: Maintain a steady 60/120fps frame budget (≤16.6ms / ≤8.3ms per frame). Never trigger full screen rebuilds on every animation tick.
3. **Accessibility (Reduced Motion)**: Always respect `MediaQuery.disableAnimationsOf(context)`. If the user has disabled animations in their operating system, snap immediately to the final state.

---

## 2. Implicit vs Explicit Animations

### Implicit Animations (Fast, Declarative, Built-in)
Use when animating simple state transitions (size, opacity, alignment, color):
- `AnimatedContainer`: Smooth size, padding, or decoration morphing.
- `AnimatedOpacity`: Fade in / fade out elements.
- `AnimatedCrossFade`: Smooth transition between two widgets.
- `AnimatedSwitcher`: Transition smoothly between widgets with different keys:
  ```dart
  AnimatedSwitcher(
    duration: const Duration(milliseconds: 250),
    transitionBuilder: (child, animation) => FadeTransition(opacity: animation, child: child),
    child: isEditing 
        ? const EditProfileForm(key: ValueKey('edit')) 
        : const ViewProfileDetails(key: ValueKey('view')),
  )
  ```

### Explicit Animations (Precise Control, Loops, Coordinated Staggers)
Use when an animation requires repeating, reversing, scrubbing with gestures, or orchestrating multiple staggered choreographies:

```dart
class PulseCardState extends State<PulseCard> with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    )..repeat(reverse: true);

    _scaleAnimation = Tween<double>(begin: 0.98, end: 1.02).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _controller.dispose(); // ALWAYS dispose controllers to prevent memory leaks!
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (MediaQuery.disableAnimationsOf(context)) {
      return widget.child; // Respect reduced motion
    }

    // Use AnimatedBuilder or ScaleTransition with pre-built child to avoid rebuilds
    return ScaleTransition(
      scale: _scaleAnimation,
      child: widget.child,
    );
  }
}
```

---

## 3. Hero Transitions for Spatial Continuity

Create seamless shared-element transitions between list items and detail screens:

```dart
// In List View
Hero(
  tag: 'product-image-${product.id}',
  child: ClipRRect(
    borderRadius: BorderRadius.circular(12),
    child: Image.network(product.imageUrl),
  ),
)

// In Detail View
Hero(
  tag: 'product-image-${product.id}',
  child: Image.network(product.imageUrl, fit: BoxFit.cover),
)
```

---

## 4. Animation Performance Golden Rules

1. **RepaintBoundary**: Wrap animating sub-trees in a `RepaintBoundary` to prevent raster repainting of static background widgets.
2. **Avoid Opacity Widget for Continuous Animation**: Never animate `Opacity(opacity: animation.value, child: ...)`. It creates an expensive offscreen buffer on every frame. Use `FadeTransition` or `AnimatedOpacity`.
3. **Pre-build Children**: Pass static children into `AnimatedBuilder(child: prebuiltWidget, builder: (context, child) => ...)` so the child is constructed once rather than 60 times a second.

---

## 5. Related References

- Animation Design Guide: [../../../design/animation.md](../../../design/animation.md)
- Performance: [performance.md](performance.md)
- Components: [components.md](components.md)
