# Memory Management & Resource Disposal

> Engineering practices for eliminating memory leaks, managing component lifecycles, and releasing resources.

---

## 1. Purpose

Memory leaks in UI applications cause progressive performance degradation, frame drops, battery exhaustion, and eventual out-of-memory (OOM) application crashes. In long-running Single Page Applications (SPAs) or mobile apps, failing to dispose of listeners and controllers is disastrous. 

This guide defines the engineering standard for resource disposal.

---

## 2. The 5 Major Culprits of UI Memory Leaks

```mermaid
flowchart LR
    A[1. Lingering Event Listeners] --- B[2. Uncancelled Timers]
    B --- C[3. Unsubscribed Streams / Observables]
    C --- D[4. Undisposed Controllers]
    D --- E[5. Retain Cycles in Closures]
```

### 1. Lingering Event Listeners
Attaching listeners to global targets (`window`, `document`, hardware sensors) without removing them when the component unmounts. The component remains trapped in memory forever.

### 2. Uncancelled Timers & Intervals
Setting `setInterval` or `Timer.periodic` and failing to call `clearInterval` or `timer.cancel()`. The timer continues firing in the background and holding a reference to the detached view.

### 3. Unsubscribed Streams & Observables
Subscribing to reactive streams (Dart Streams, RxJS Observables, WebSocket connections) without cancelling the subscription when the view disappears.

### 4. Undisposed Native Controllers
In mobile frameworks (Flutter, Android, iOS), controllers (e.g. `AnimationController`, `TextEditingController`, `ScrollController`, `MediaPlayer`) allocate underlying OS or GPU memory and must be explicitly destroyed.

### 5. Retain Cycles & Closures
Closures capturing `self` or large outer view state strongly, preventing the garbage collector or ARC from releasing the instance.

---

## 3. Flutter Lifecycle & Memory Cleanup Patterns

### 1. StatefulWidget Lifecycle Disposal
Always override `dispose()` in `StatefulWidget`:
```dart
class _CustomWidgetState extends State<CustomWidget> with SingleTickerProviderStateMixin {
  late final TextEditingController _controller;
  late final AnimationController _animController;
  late final ScrollController _scrollController;
  StreamSubscription<UserEvent>? _sub;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController();
    _animController = AnimationController(vsync: this, duration: const Duration(milliseconds: 300));
    _scrollController = ScrollController();
    _sub = eventBus.stream.listen(_handleEvent);
  }

  @override
  void dispose() {
    // MANDATORY: Dispose controllers and cancel subscriptions
    _controller.dispose();
    _animController.dispose();
    _scrollController.dispose();
    _sub?.cancel();
    super.dispose();
  }
}
```

### 2. Riverpod Provider Disposal
Use `ref.onDispose` to release native resources or close subscriptions:
```dart
final locationStreamProvider = StreamProvider.autoDispose<LocationData>((ref) {
  final service = LocationService();
  ref.onDispose(() => service.stopTracking());
  return service.locationStream;
});
```

### 3. BLoC & Cubit Sink Closure
Always close streams and sinks in `Bloc.close()`:
```dart
@override
Future<void> close() {
  _authSubscription.cancel();
  return super.close();
}
```

### 4. Image Cache Eviction
High-resolution images can quickly overwhelm mobile heap memory. Downsample decoded bitmaps using `cacheWidth` and `cacheHeight`, or clear the image cache if necessary:
```dart
PaintingBinding.instance.imageCache.clear();
```

---

## 4. Unbounded Cache Safeguards

- Never store unbounded lists of images, search queries, or API payloads in a plain global `Map` or `List`.
- Always use a **Least Recently Used (LRU)** cache with an explicit maximum entry limit or size threshold.

---

## 5. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Clean Code: [clean-code.md](clean-code.md)
- Performance: [performance.md](performance.md)
- Performance Audit Checklist: [../quality/performance-audit.md](../quality/performance-audit.md)

