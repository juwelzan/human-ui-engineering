# Native Android Framework Reference (Jetpack Compose)

> Framework-specific guidance for Android development using Jetpack Compose, Material 3, and Kotlin.

---

## 1. Quick Android Directives

- **Unidirectional Data Flow (UDF)**: Expose a single immutable `StateFlow<UiState>` from ViewModels; hoist state from composables.
- **Sealed State Hierarchy**: Model Loading, Success, Error, and Empty states explicitly with sealed interfaces.
- **Lazy Collections**: Use `LazyColumn` / `LazyRow` with unique, stable `key = { it.id }`.
- **Recomposition Optimization**: Ensure data models are `@Immutable` or `@Stable`. Use `derivedStateOf` for high-frequency state.
- **Accessibility & Touch Targets**: Enforce 48dp minimum targets (`Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)`) and clear `contentDescription`.

---

## 2. In-Depth Documentation Links

- Complete Native Android Guide: [../../../frameworks/native-android.md](../../../frameworks/native-android.md)
- Cross-Platform Idioms: [../../../engineering/cross-platform.md](../../../engineering/cross-platform.md)
