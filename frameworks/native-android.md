# Native Android UI Engineering Guide (Jetpack Compose)

> Practical engineering guide for building modern Android applications using Kotlin, Jetpack Compose, Material 3, and Coroutines.

---

## 1. Recommended Project Structure

Follow the official Android **Now in Android** modular or layered architecture:

```text
app/src/main/java/com/example/app/
├── core/
│   ├── designsystem/           # Material 3 theme (Theme.kt, Color.kt, Type.kt, Shape.kt)
│   │   ├── component/          # AppButton.kt, AppTextField.kt, AppCard.kt
│   │   └── icon/               # AppIcons.kt
│   ├── network/                # Retrofit / Ktor client, interceptors
│   └── data/                   # Repositories & Room database
├── feature/                    # Feature modules
│   ├── feed/
│   │   ├── FeedScreen.kt       # Composable screen entry
│   │   ├── FeedViewModel.kt    # State holder
│   │   ├── FeedUiState.kt      # Sealed interface state representation
│   │   └── components/         # Local feed composables
│   └── profile/
├── navigation/                 # Jetpack Compose Navigation graph
└── MainActivity.kt
```

---

## 2. UI Architecture & State Hoisting

- **MVI / UDF Pattern**: The ViewModel exposes a single, immutable `StateFlow<FeedUiState>` representing the entire screen state. The Composable consumes state and emits events back to the ViewModel.
- **State Hoisting**: A Composable should not hold internal mutable state if a parent needs to control it. Pass state down, pass event lambdas up:
  ```kotlin
  @Composable
  fun SearchBar(
      query: String,
      onQueryChange: (String) -> Unit,
      modifier: Modifier = Modifier
  ) { ... }
  ```
- **Sealed UI States**: Model distinct UI states explicitly:
  ```kotlin
  sealed interface FeedUiState {
      data object Loading : FeedUiState
      data class Success(val items: List<FeedItem>) : FeedUiState
      data class Error(val message: String) : FeedUiState
      data object Empty : FeedUiState
  }
  ```

---

## 3. Responsive Design & Window Size Classes

- Android runs on phones, foldables, tablets, and ChromeOS desktops.
- Use `WindowWidthSizeClass` (Compact, Medium, Expanded) to adapt layouts:
  - **Compact (< 600dp)**: Single column, bottom navigation bar (`NavigationBar`).
  - **Medium (600dp – 840dp)**: 2 columns, navigation rail (`NavigationRail`).
  - **Expanded (> 840dp)**: Multi-pane master-detail list, permanent navigation drawer.
- Support display cutouts and system bars using `WindowInsets.safeDrawing`.

---

## 4. Performance & Recomposition Optimization

1. **LazyColumn / LazyRow**: Never use `Column` with a `forEach` loop for large lists. Always use `LazyColumn` with stable, unique `items(items, key = { it.id })`.
2. **Stability & Immutability**:
   - Compose skips recomposition only if Composable parameters are **Stable**.
   - Annotate external models or data classes with `@Immutable` or `@Stable`.
   - Avoid passing unstable collections (like raw `List<T>`) if the compiler marks them unstable; consider `ImmutableList` from Kotlinx Collections Immutable.
3. **Derived State**: Use `derivedStateOf` when observing high-frequency changes (e.g. scroll offsets) to prevent recomposing on every pixel scroll:
   ```kotlin
   val showScrollToTop by remember {
       derivedStateOf { listState.firstVisibleItemIndex > 5 }
   }
   ```

---

## 5. Accessibility (TalkBack)

- Add clear semantic descriptions using `Modifier.semantics { contentDescription = "..." }`.
- Ensure icon-only `IconButton` composables have a non-null `contentDescription`.
- Combine child elements for TalkBack using `Modifier.semantics(mergeDescendants = true)`.
- Enforce the 48dp minimum touch target using `Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)`.

---

## 6. Testing

- Use **Compose UI Testing** (`createComposeRule()`):
  ```kotlin
  @Test
  fun appButton_showsProgress_whenLoading() {
      composeTestRule.setContent {
          AppButton(isLoading = true, label = "Submit", onClick = {})
      }
      composeTestRule.onNodeWithTag("LoadingSpinner").assertIsDisplayed()
  }
  ```
- Use Robolectric for fast local JVM UI tests without an Android emulator.

---

## 7. Common Mistakes to Avoid

1. **Instantiating Objects Directly in Composable Bodies**: Allocating expensive objects (formatters, lists) without wrapping them in `remember { ... }`, causing them to re-allocate on every recomposition.
2. **Missing Key in LazyColumn**: Omitting the `key` parameter in `items()`, which forces Compose to re-instantiate every item when one item is added or reordered.
3. **Hardcoding Density Pixels (dp) on Text**: Always use `sp` for font sizing (`fontSize = 16.sp`) so text scales with user accessibility settings.

---

## 8. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Native iOS Guide: [native-ios.md](native-ios.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)

