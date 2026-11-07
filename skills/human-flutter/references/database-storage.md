# Flutter Local Database & Offline-First Storage

> Local persistence, relational and document caching, secure storage, and offline-first synchronization in Flutter.

---

## 1. Storage Selection Matrix

| Storage Solution | Paradigm | Best For | Encryption Support | Reactive Streams |
|---|---|---|---|---|
| **Drift** | Type-Safe Relational (SQLite) | Complex relational data, relational queries, enterprise apps | Yes (via SQLCipher) | Native `Stream` queries |
| **Isar** | NoSQL Object Store | High-performance document queries, offline search, large datasets | Yes | Native watchers |
| **Hive** | Lightweight Key-Value / Box | Fast cache boxes, simple offline documents | Yes (AES-256) | Box event streams |
| **SharedPreferences** | Key-Value | UI preferences, theme mode, onboarding flags | No | ValueNotifier / Streams |
| **FlutterSecureStorage** | Hardware Keystore / Keychain | Auth tokens, refresh tokens, encryption keys, biometrics | Hardware Backed | Manual listeners |

---

## 2. Offline-First Sync Pattern (NetworkBoundResource)

Always display cached local database data immediately, fetch remote updates in the background, update local storage, and stream fresh records to the UI:

```dart
// Stream-based repository pattern
Stream<List<Task>> watchTasks() async* {
  // 1. Emit cached local records immediately
  yield* localDb.watchAllTasks();

  // 2. Fetch fresh data from remote API
  try {
    final remoteTasks = await apiClient.getTasks();
    // 3. Upsert into local database; reactive stream updates UI automatically
    await localDb.upsertTasks(remoteTasks);
  } catch (e) {
    // UI continues showing cached tasks; optionally log or emit network warning
  }
}
```

---

## 3. Secure Token Storage

Never store JWTs or credentials in unencrypted `SharedPreferences`:

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureTokenStorage {
  static const _storage = FlutterSecureStorage(
    aOptions: AndroidOptions(encryptedSharedPreferences: true),
    iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock),
  );

  static const _keyAccessToken = 'access_token';

  Future<void> saveAccessToken(String token) async {
    await _storage.write(key: _keyAccessToken, value: token);
  }

  Future<String?> getAccessToken() async {
    return _storage.read(key: _keyAccessToken);
  }

  Future<void> clearSession() async {
    await _storage.deleteAll();
  }
}
```

---

## 4. Drift Migrations Best Practices

When evolving schemas in production:
1. Always test migrations with `drift_dev make-migrations`.
2. Wrap column additions in `MigrationStrategy`:
   ```dart
   @override
   MigrationStrategy get migration => MigrationStrategy(
     onCreate: (Migrator m) async => m.createAll(),
     onUpgrade: (Migrator m, int from, int to) async {
       if (from < 2) {
         await m.addColumn(tasks, tasks.priority);
       }
     },
   );
   ```

---

## 5. Related References

- API Integration: [api-integration.md](api-integration.md)
- Security: [security.md](security.md)
- Architecture: [flutter-architecture.md](flutter-architecture.md)
