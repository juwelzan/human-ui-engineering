# Human Flutter Performance Engineering

> Comprehensive performance optimization guide for Flutter: 120fps rendering, rebuild minimization, memory leak prevention, and DevTools profiling.

---

## 1. Frame Budget: The 16.6ms & 8.3ms Rules

Flutter apps run on two critical threads:
1. **UI Thread (Dart VM)**: Executes widget builds, layout logic, and animation tickers. Budget: ≤ 16.6ms (60fps) or ≤ 8.3ms (120fps).
2. **Raster Thread (GPU engine)**: Renders rasterized instructions onto the screen.

When either thread exceeds its frame budget, the user experiences visual jank (dropped frames).

---

## 2. Rebuild Minimization & Const Constructors

1. **`const` Constructors Everywhere**: Mark every immutable widget `const`. Flutter reuses the canonical instance, skipping entire branches during rebuilds.
2. **Scoped Rebuilds**:
   - In BLoC: Always use `buildWhen`:
     ```dart
     BlocBuilder<CartBloc, CartState>(
       buildWhen: (prev, curr) => prev.totalCount != curr.totalCount,
       builder: (context, state) => Badge(label: Text('${state.totalCount}')),
     );
     ```
   - In Riverpod: Use `.select()`:
     ```dart
     final totalCount = ref.watch(cartProvider.select((s) => s.totalCount));
     ```
   - In Provider: Use `context.select<CartModel, int>((m) => m.totalCount)`.

---

## 3. List Virtualization & Image Optimization

### Virtualized Lists
Never render large or dynamic collections via `ListView(children: [...])` or `SingleChildScrollView(child: Column(...))`. Use `ListView.builder` or `CustomScrollView` with `SliverList`:

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ItemTile(item: items[index]),
);
```

### Image Caching & Downsampling
Loading raw 4000x3000 camera images into a 50x50 avatar causes massive heap allocation and OOM crashes. Always provide `cacheWidth` and `cacheHeight`:

```dart
Image.network(
  avatarUrl,
  cacheWidth: 150, // Resizes decoded bitmap in memory to match render target
  cacheHeight: 150,
)
```

---

## 4. Heavy Computation via Isolates

Any task taking longer than 8ms on the UI thread (parsing giant 10MB JSON responses, image hashing, cryptography) must run on a background isolate:

```dart
// Using compute() for lightweight isolate offloading
Future<List<UserDto>> parseUsersInBackground(String rawJson) async {
  return compute(_parseUsers, rawJson);
}

List<UserDto> _parseUsers(String jsonString) {
  final List decoded = jsonDecode(jsonString);
  return decoded.map((e) => UserDto.fromJson(e)).toList();
}
```

---

## 5. Memory Management & Lifecycle Disposal

Failing to dispose controllers and stream subscriptions is the #1 cause of Flutter memory leaks. Always dispose in `State.dispose()`:

```dart
@override
void dispose() {
  _textController.dispose();
  _scrollController.dispose();
  _animationController.dispose();
  _userSubscription.cancel();
  super.dispose();
}
```

---

## 6. Profiling with Flutter DevTools

When diagnosing jank or high memory consumption:
1. Run in profile mode: `flutter run --profile`.
2. Open Flutter DevTools:
   - **Performance Tab**: Inspect frame rendering times (UI vs Raster bars). Look for red bars (>16ms).
   - **CPU Profiler**: Identify slow Dart methods consuming CPU cycles.
   - **Memory Tab**: Take heap snapshots before and after screen navigation to verify controllers and listeners are freed.

---

## 7. Related References

- Performance Audit Guide: [../../../quality/performance-audit.md](../../../quality/performance-audit.md)
- Memory Management: [../../../engineering/memory-management.md](../../../engineering/memory-management.md)
- Animation: [animation.md](animation.md)
