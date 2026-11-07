# Human Responsive & Adaptive Engineering in Flutter

> Multi-platform responsive design across Android, iOS, macOS, Windows, Linux, and Flutter Web.

---

## 1. Principles

1. **Adaptive, Not Just Scaled**: Responsive Flutter design is not merely enlarging widgets to fill a 32-inch 4K monitor. Desktop and tablet viewports demand multi-pane master-detail layouts, persistent sidebars, and keyboard shortcuts.
2. **Constraint-Driven Layout**: Use `LayoutBuilder` to inspect available parent constraints. Relying exclusively on `MediaQuery.sizeOf(context)` fails inside split-screen multitasking, floating windows, and modal dialogs.
3. **Zero Overflow Tolerance**: Layout bugs (`A RenderFlex overflowed by X pixels`) are severe defects that undermine user trust.

---

## 2. Standard Breakpoints in Flutter

```dart
class ResponsiveBreakpoints {
  static const double mobileMax = 599;
  static const double tabletMin = 600;
  static const double desktopMin = 1024;
  static const double wideDesktopMin = 1440;
}

enum ScreenType { mobile, tablet, desktop }

ScreenType getScreenType(BuildContext context) {
  final width = MediaQuery.sizeOf(context).width;
  if (width < ResponsiveBreakpoints.tabletMin) return ScreenType.mobile;
  if (width < ResponsiveBreakpoints.desktopMin) return ScreenType.tablet;
  return ScreenType.desktop;
}
```

---

## 3. Responsive Navigation Pattern

Switch dynamically between bottom navigation on mobile and navigation rail on tablet/desktop:

```dart
class AdaptiveScaffold extends StatelessWidget {
  final int selectedIndex;
  final ValueChanged<int> onDestinationSelected;
  final List<NavigationDestination> destinations;
  final Widget body;

  const AdaptiveScaffold({
    super.key,
    required this.selectedIndex,
    required this.onDestinationSelected,
    required this.destinations,
    required this.body,
  });

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        // Desktop & Tablet: Persistent NavigationRail
        if (constraints.maxWidth >= ResponsiveBreakpoints.tabletMin) {
          return Scaffold(
            body: Row(
              children: [
                NavigationRail(
                  selectedIndex: selectedIndex,
                  onDestinationSelected: onDestinationSelected,
                  labelType: NavigationRailLabelType.selected,
                  destinations: destinations
                      .map((d) => NavigationRailDestination(icon: d.icon, label: Text(d.label)))
                      .toList(),
                ),
                const VerticalDivider(thickness: 1, width: 1),
                Expanded(child: body),
              ],
            ),
          );
        }

        // Mobile: Traditional Bottom NavigationBar
        return Scaffold(
          body: body,
          bottomNavigationBar: NavigationBar(
            selectedIndex: selectedIndex,
            onDestinationSelected: onDestinationSelected,
            destinations: destinations,
          ),
        );
      },
    );
  }
}
```

---

## 4. Preventing Top Flutter Layout Overflows

### 1. The Column Inside Unconstrained Height Bug
- **Bug**: `ListView` inside `Column` without constraints -> `Vertical viewport was given unbounded height`.
- **Fix**: Wrap `ListView` in `Expanded` or use `shrinkWrap: true, physics: const NeverScrollableScrollPhysics()` inside a parent `SingleChildScrollView`.

### 2. The Keyboard Overlap Bug
- **Bug**: Mobile keyboard pops up and covers form submit button, causing yellow/black striped overflow.
- **Fix**: Wrap form body in `SafeArea` + `SingleChildScrollView(keyboardDismissBehavior: ScrollViewKeyboardDismissBehavior.onDrag)`.

### 3. The Row Text Truncation Bug
- **Bug**: Long text inside a `Row` alongside an icon causes `A RenderFlex overflowed by 42 pixels on the right`.
- **Fix**: Wrap the `Text` in `Expanded` or `Flexible` with `overflow: TextOverflow.ellipsis`.

---

## 5. Desktop Max-Width Container Pattern

Never allow a mobile card or text form to stretch across 1400px of desktop width. Center and constrain content:

```dart
class ContentContainer extends StatelessWidget {
  final Widget child;
  final double maxWidth;

  const ContentContainer({
    super.key,
    required this.child,
    this.maxWidth = 1100,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth),
        child: child,
      ),
    );
  }
}
```

---

## 6. Related References

- Responsive Design Guide: [../../../design/responsive-design.md](../../../design/responsive-design.md)
- Platform Integration: [platform-integration.md](platform-integration.md)
- Performance: [performance.md](performance.md)
