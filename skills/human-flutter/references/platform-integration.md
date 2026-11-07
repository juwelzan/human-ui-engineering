# Human Flutter Platform Engineering

> Seamless native platform integration across Android, iOS, macOS, Windows, Linux, and Web using platform channels, FFI, and lifecycle hooks.

---

## 1. Principles of Platform Integration

1. **Flutter-First Rule**: Always prefer an existing Flutter/Dart package or solution. Write native code (Kotlin/Swift) ONLY when platform hardware, OS APIs, or OEM restrictions make it impossible in pure Dart.
2. **Type Safety Across Boundaries**: Prefer code generation with `pigeon` over manual untyped string-based `MethodChannel` payloads whenever building custom native bridges.
3. **Platform-Adaptive Feel**: Respect OS conventions (haptic feedback, keyboard shortcuts on desktop, swipe back on iOS, window drag handles on macOS).

---

## 2. Platform Detection

```dart
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

bool get isMobile => !kIsWeb && (defaultTargetPlatform == TargetPlatform.iOS || defaultTargetPlatform == TargetPlatform.android);
bool get isDesktop => !kIsWeb && (defaultTargetPlatform == TargetPlatform.macOS || defaultTargetPlatform == TargetPlatform.windows || defaultTargetPlatform == TargetPlatform.linux);
```

---

## 3. Platform Channels: MethodChannel & EventChannel

### MethodChannel (One-Off Native Invocations)
```dart
import 'package:flutter/services.dart';

class NativeBatteryService {
  static const MethodChannel _channel = MethodChannel('com.example.app/battery');

  static Future<int> getBatteryLevel() async {
    try {
      final int level = await _channel.invokeMethod('getBatteryLevel');
      return level;
    } on PlatformException catch (e) {
      throw AppError.platform(e.message ?? 'Failed to get battery');
    }
  }
}
```

### EventChannel (Continuous Native Hardware Streams)
```dart
class AccelerometerService {
  static const EventChannel _eventChannel = EventChannel('com.example.app/sensors');

  Stream<List<double>> get sensorStream {
    return _eventChannel.receiveBroadcastStream().map((event) {
      return (event as List).cast<double>();
    });
  }
}
```

---

## 4. App Lifecycle Management: AppLifecycleListener

Flutter 3.13+ provides `AppLifecycleListener` for clean, declarative lifecycle monitoring:

```dart
class AppShellState extends State<AppShell> {
  late final AppLifecycleListener _lifecycleListener;

  @override
  void initState() {
    super.initState();
    _lifecycleListener = AppLifecycleListener(
      onResume: () => print('App resumed: sync background updates'),
      onPause: () => print('App paused: persist draft state'),
      onHide: () => print('App hidden: lock secure credentials'),
    );
  }

  @override
  void dispose() {
    _lifecycleListener.dispose();
    super.dispose();
  }
}
```

---

## 5. Desktop Window Management

For macOS, Windows, and Linux desktop targets:
- Use `window_manager` to configure min/max window dimensions, frameless window headers, and titlebar drag regions:
  ```dart
  WindowOptions windowOptions = const WindowOptions(
    size: Size(1280, 800),
    minimumSize: Size(800, 600),
    center: true,
    titleBarStyle: TitleBarStyle.hidden, // Frameless design
  );
  ```

---

## 6. Related References

- Cross-Platform Engineering: [../../../engineering/cross-platform.md](../../../engineering/cross-platform.md)
- Responsive Design: [responsive-design.md](responsive-design.md)
- Security: [security.md](security.md)
