# Async Operations & Lifecycle Safety

> Engineering rules for request cancellation, race condition prevention, debouncing, throttling, and optimistic UI updates.

---

## 1. Purpose

User interfaces are inherently asynchronous: network latency, user typing, animations, and hardware sensor streams all execute concurrently. Failing to manage asynchronous lifecycles leads to race conditions, out-of-order state updates, zombie memory leaks, and duplicate submissions.

This guide defines the universal standards for asynchronous UI engineering.

---

## 2. The 3 Classic Async UI Hazards

```mermaid
flowchart LR
    H1[1. Race Condition] --> S1[AbortController / Sequence IDs]
    H2[2. Zombie State Update] --> S2[Lifecycle Cancellation on Unmount]
    H3[3. API Request Flooding] --> S3[Debounce & Throttle]
```

### 1. Race Conditions (Out-of-Order Responses)
- **Scenario**: User types "React" (Request 1), then rapidly types "React 19" (Request 2). If Request 1 is delayed by network jitter and arrives *after* Request 2, the UI will display the outdated "React" results instead of "React 19".
- **Solution**: Cancel obsolete in-flight requests or track monotonically increasing request sequence IDs.

### 2. Zombie Updates on Unmounted Views
- **Scenario**: A user taps "Load Analytics", then immediately clicks "Back". 3 seconds later, the promise resolves and calls `setState`, throwing warnings or leaking memory.
- **Solution**: Bind async tasks to the view's lifecycle and cancel them upon destruction.

### 3. API Request Flooding
- **Scenario**: An input fires an HTTP request on every single keystroke, overwhelming the backend.
- **Solution**: Debounce user input by 250ms–350ms.

---

## 3. Request Cancellation Across Ecosystems

Always wire request cancellation to component teardown:

### A. Web / React / Next.js / Vue
```typescript
useEffect(() => {
  const controller = new AbortController();

  async function fetchResults() {
    try {
      const response = await fetch(`/api/search?q=${query}`, {
        signal: controller.signal,
      });
      const data = await response.json();
      setResults(data);
    } catch (err: unknown) {
      if ((err as Error).name !== 'AbortError') {
        setError('Failed to fetch search results');
      }
    }
  }

  fetchResults();

  // Cancel in-flight request if query changes or component unmounts
  return () => controller.abort();
}, [query]);
```

### B. Flutter / Dart
```dart
CancelToken? _cancelToken;

Future<void> search(String query) async {
  _cancelToken?.cancel('Cancelled by new search request');
  _cancelToken = CancelToken();

  try {
    final response = await dio.get('/api/search', 
      queryParameters: {'q': query}, 
      cancelToken: _cancelToken,
    );
    setState(() => _results = response.data);
  } catch (e) {
    if (!CancelToken.isCancel(e)) {
      setState(() => _hasError = true);
    }
  }
}

@override
void dispose() {
  _cancelToken?.cancel();
  super.dispose();
}
```

### C. Android (Kotlin Coroutines)
Use `viewModelScope`—all launched jobs automatically cancel when the ViewModel clears:
```kotlin
private var searchJob: Job? = null

fun onQueryChanged(newQuery: String) {
    searchJob?.cancel() // Cancel previous pending query
    searchJob = viewModelScope.launch {
        delay(300) // Debounce
        val results = repository.search(newQuery)
        _uiState.update { it.copy(results = results) }
    }
}
```

---

## 4. Debounce vs. Throttle

| Pattern | Behavior | Ideal UI Scenario |
|---|---|---|
| **Debounce** | Delays execution until a specified quiet period has elapsed with no new events. | Search autocomplete typing, window resize layout recalculations, auto-saving drafts. |
| **Throttle** | Enforces a maximum execution rate (at most once every N milliseconds). | Infinite scroll trigger checks, drag-and-drop pointer tracking, audio/video playback scrubbing. |

---

## 5. Optimistic UI Updates & Rollback

For low-risk, immediate actions (e.g. toggling a favorite star or upvoting):

1. **Optimistic Mutation**: Immediately update the local UI state and render the active appearance.
2. **Background Dispatch**: Send the asynchronous request with a cancellation token.
3. **Rollback on Error**: If the server rejects the request:
   - Revert the state snapshot back to its pre-mutation value.
   - Display a non-blocking toast alert explaining the failure with an explicit "Retry" action.

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Error Handling: [error-handling.md](error-handling.md)
- Performance Engineering: [performance.md](performance.md)
- Memory Management: [memory-management.md](memory-management.md)
