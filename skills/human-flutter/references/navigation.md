# Flutter Navigation & Declarative Routing

> Declarative routing, deep linking, nested navigation, and URL management with `go_router`.

---

## 1. Principles of Flutter Navigation

1. **Declarative Over Imperative**: Use declarative routing (`go_router`) instead of raw imperative `Navigator.push()` calls. Declarative routing ensures consistent deep linking, web browser history, and parameter serialization.
2. **Stateful Bottom Navigation**: Preserve state and scroll position across bottom navigation tabs using `StatefulShellRoute.indexedStack`.
3. **Guarded Redirection**: Centralize authentication checks and onboarding gates in route redirects rather than sprinkling checks inside screens.

---

## 2. Recommended GoRouter Setup

```dart
// core/router/app_router.dart
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

final GlobalKey<NavigatorState> _rootNavigatorKey = GlobalKey<NavigatorState>();

final GoRouter appRouter = GoRouter(
  navigatorKey: _rootNavigatorKey,
  initialLocation: '/home',
  debugLogDiagnostics: true,
  redirect: (context, state) {
    final bool isLoggedIn = checkAuthSession();
    final bool isLoggingIn = state.matchedLocation == '/login';

    if (!isLoggedIn && !isLoggingIn) return '/login';
    if (isLoggedIn && isLoggingIn) return '/home';
    return null; // No redirect needed
  },
  routes: [
    GoRoute(
      path: '/login',
      builder: (context, state) => const LoginScreen(),
    ),
    // Bottom Navigation Shell
    StatefulShellRoute.indexedStack(
      builder: (context, state, navigationShell) {
        return ScaffoldWithNavBar(navigationShell: navigationShell);
      },
      branches: [
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/home',
              builder: (context, state) => const HomeScreen(),
              routes: [
                GoRoute(
                  path: 'details/:id',
                  builder: (context, state) {
                    final id = state.pathParameters['id']!;
                    return ProductDetailScreen(productId: id);
                  },
                ),
              ],
            ),
          ],
        ),
        StatefulShellBranch(
          routes: [
            GoRoute(
              path: '/settings',
              builder: (context, state) => const SettingsScreen(),
            ),
          ],
        ),
      ],
    ),
  ],
);
```

---

## 3. Web URL Strategy & Deep Linking

For Flutter Web, remove the `#` fragment from URLs:

```dart
// In main.dart
import 'package:flutter_web_plugins/url_strategy.dart';

void main() {
  usePathUrlStrategy();
  runApp(const MyApp());
}
```

### Deep Linking Configuration
- **Android**: Configure intent filters in `android/app/src/main/AndroidManifest.xml` (`autoVerify="true"` for App Links).
- **iOS**: Configure Associated Domains (`applinks:example.com`) in Xcode and host `apple-app-site-association`.

---

## 4. Custom Page Transitions

```dart
GoRoute(
  path: '/modal',
  pageBuilder: (context, state) => CustomTransitionPage(
    key: state.pageKey,
    child: const ModalScreen(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      return SlideTransition(
        position: Tween<Offset>(
          begin: const Offset(0, 1),
          end: Offset.zero,
        ).animate(CurvedAnimation(parent: animation, curve: Curves.easeOutCubic)),
        child: child,
      );
    },
  ),
);
```

---

## 5. Related References

- Architecture: [flutter-architecture.md](flutter-architecture.md)
- Responsive Design: [responsive-design.md](responsive-design.md)
- Platform Integration: [platform-integration.md](platform-integration.md)
