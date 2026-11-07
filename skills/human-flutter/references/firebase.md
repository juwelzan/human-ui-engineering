# Flutter Firebase Integration Engineering

> Practical guide for integrating the Firebase suite in production Flutter applications.

---

## 1. Principles

1. **Platform-Safe Initialization**: Initialize Firebase using generated `DefaultFirebaseOptions.currentPlatform` via `flutterfire configure`.
2. **Type-Safe Firestore Converters**: Never work with raw `Map<String, dynamic>` in Firestore queries. Always use `.withConverter<T>()`.
3. **Crash Diagnostics**: Route all uncaught Flutter framework errors and asynchronous Dart zone errors into Firebase Crashlytics.

---

## 2. Initialization & Uncaught Error Handling

```dart
// main.dart
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'firebase_options.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // 1. Initialize Firebase
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  // 2. Catch Flutter framework errors (build/layout errors)
  FlutterError.onError = (errorDetails) {
    FirebaseCrashlytics.instance.recordFlutterFatalError(errorDetails);
  };

  // 3. Catch asynchronous Dart runtime errors
  PlatformDispatcher.instance.onError = (error, stack) {
    FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
    return true;
  };

  runApp(const MyApp());
}
```

---

## 3. Firestore Type-Safe Converters

```dart
import 'package:cloud_firestore/cloud_firestore.dart';

CollectionReference<UserProfile> getUsersCollection() {
  return FirebaseFirestore.instance.collection('users').withConverter<UserProfile>(
    fromFirestore: (snapshot, _) => UserProfile.fromJson(snapshot.data()!),
    toFirestore: (user, _) => user.toJson(),
  );
}

// Consuming with full type safety
Future<UserProfile?> fetchUserProfile(String userId) async {
  final doc = await getUsersCollection().doc(userId).get();
  return doc.data(); // Returns typed UserProfile? directly!
}
```

---

## 4. Push Notifications with FCM

```dart
import 'package:firebase_messaging/firebase_messaging.dart';

Future<void> setupFCM() async {
  final messaging = FirebaseMessaging.instance;

  // Request permissions (critical on iOS & Android 13+)
  final settings = await messaging.requestPermission(
    alert: true,
    badge: true,
    sound: true,
  );

  if (settings.authorizationStatus == AuthorizationStatus.authorized) {
    // Listen to foreground notifications
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      // Show in-app banner or toast
    });
  }
}
```

---

## 5. Related References

- Product Engineering: [api-integration.md](api-integration.md)
- Security: [security.md](security.md)
- Error Handling: [../../../engineering/error-handling.md](../../../engineering/error-handling.md)
