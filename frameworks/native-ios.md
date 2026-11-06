# Native iOS UI Engineering Guide (SwiftUI)

> Practical engineering guide for building modern iOS applications using Swift, SwiftUI, Observation, SF Symbols, and Apple Human Interface Guidelines (HIG).

---

## 1. Recommended Project Structure

Follow a modern modular SwiftUI architecture:

```text
App/
├── Core/
│   ├── DesignSystem/           # Colors (Assets.xcassets), Typography, Spacing
│   │   ├── Components/         # AppButton.swift, AppTextField.swift, AppCard.swift
│   │   └── ViewModifiers/      # Custom modifiers (e.g. CardModifier)
│   ├── Network/                # URLSession / async/await client
│   └── Storage/                # SwiftData / CoreData models
├── Features/                   # Feature modules
│   ├── Feed/
│   │   ├── Views/              # FeedView.swift, FeedItemRow.swift
│   │   ├── ViewModels/         # FeedViewModel.swift (@Observable)
│   │   └── Models/             # FeedItem.swift
│   └── Profile/
├── Navigation/                 # AppNavigationStack.swift, TabDestination.swift
└── AppEntry.swift              # @main App struct
```

---

## 2. UI Architecture & State Management

- **The `@Observable` Macro (iOS 17+)**: Use Swift's native `@Observable` for view models. SwiftUI automatically tracks property access and invalidates views only when observed properties actually mutate.
- **Unidirectional Flow**:
  - View model manages async network calls and exposes clean state.
  - View renders declarative UI based on state.
  - Actions flow to the view model via `async` methods.
- **State Property Wrappers**:
  - `@State`: For view-private ephemeral state (e.g. text input string, sheet presentation boolean).
  - `@Binding`: For two-way data binding with a child component.
  - `@Environment`: For system values (color scheme, dismiss action, safe area insets).

---

## 3. Responsive Layout & Apple HIG

- Use `NavigationStack` with `.navigationTitle("...")` and `.navigationBarTitleDisplayMode(.inline / .large)` following native Apple conventions.
- Use `TabView` for primary bottom navigation on iPhone, converting to a `NavigationSplitView` with sidebar on iPad and macOS.
- Always use Dynamic Type (`font(.headline)`, `.font(.subheadline)`) so text scales with the user's system font size preference.
- Respect Safe Area Insets naturally; only apply `.ignoresSafeArea()` to background image assets or gradients, never to interactive buttons or critical text.

---

## 4. Performance & View Invalidation Optimization

1. **LazyVStack / LazyHStack**: Always wrap scrollable lists inside `ScrollView` with `LazyVStack` or use `List`. Never use eager `VStack` for lists with more than 15 items.
2. **Stable Identifiers (`Identifiable`)**: Ensure all model collections conform to `Identifiable` using unique, immutable `id: UUID` or database keys.
3. **Small Granular Views**: Break complex views into small private sub-views. When a sub-view is in its own struct, SwiftUI can skip its body evaluation during parent updates.
4. **Avoid Heavy Computations in `body`**: The `var body: some View` getter executes frequently during animation and state changes. Move filtering and date formatting into computed properties on the model or ViewModel.

---

## 5. Accessibility (VoiceOver & HIG)

- Use `.accessibilityLabel("...")` and `.accessibilityHint("...")` for icon-only buttons:
  ```swift
  Button(action: toggleFavorite) {
      Image(systemName: isFavorite ? "heart.fill" : "heart")
  }
  .accessibilityLabel(isFavorite ? "Remove from favorites" : "Add to favorites")
  ```
- Enforce the **44x44 point** minimum hit target using `.frame(minWidth: 44, minHeight: 44)`.
- Use `.accessibilityElement(children: .combine)` to group related rows into a single clear VoiceOver element.

---

## 6. Testing

- Test view models and business logic with `XCTest` or Swift Testing (`@Test` in Swift 6).
- Use `ViewInspector` for unit testing SwiftUI views if required.

---

## 7. Common Mistakes to Avoid

1. **Over-Using `@StateObject` in Modern iOS**: In iOS 17+, prefer `@Observable` class view models over legacy `@StateObject` / `@Published` Combine setups.
2. **Hardcoding Frame Dimensions**: Setting fixed `frame(width: 350, height: 50)` which breaks on iPhone SE (320pt) or iPad.
3. **Forgetting Haptic Feedback**: Native iOS apps feel dead without subtle haptic touches (`UIImpactFeedbackGenerator` or `.sensoryFeedback(.impact, trigger: ...)`).

---

## 8. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Native Android Guide: [native-android.md](native-android.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)

