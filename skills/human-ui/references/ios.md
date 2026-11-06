# Native iOS Framework Reference (SwiftUI)

> Framework-specific guidance for iOS development using Swift, SwiftUI, and Apple HIG.

---

## 1. Quick iOS Directives

- **Observation Macro (`@Observable`)**: In iOS 17+, use Swift native `@Observable` view models rather than legacy `@StateObject`.
- **Granular Views**: Break complex views into small private sub-views to enable fine-grained SwiftUI body invalidation.
- **Dynamic Type**: Always use system typography tokens (`.font(.headline)`, `.font(.subheadline)`) so text scales with user accessibility settings.
- **Apple HIG Navigation**: Use `NavigationStack` with standard display modes; respect safe areas naturally.
- **Accessibility & Hit Targets**: Enforce **44x44 point** minimum hit areas (`.frame(minWidth: 44, minHeight: 44)`) and explicit `.accessibilityLabel`.

---

## 2. In-Depth Documentation Links

- Complete Native iOS Guide: [../../../frameworks/native-ios.md](../../../frameworks/native-ios.md)
- Cross-Platform Idioms: [../../../engineering/cross-platform.md](../../../engineering/cross-platform.md)
