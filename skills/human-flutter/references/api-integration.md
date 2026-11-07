# Flutter API Integration & Networking

> Robust REST, GraphQL, WebSocket communication, Dio interceptors, and error handling in Flutter.

---

## 1. Principles

1. **Centralized HTTP Client**: Never use raw `http.get` scattered across widgets. Centralize requests through a configured `Dio` instance with interceptors, timeouts, and logging.
2. **Type-Safe Serialization**: Every API response must deserialize into a typed model or record before reaching presentation widgets.
3. **Graceful Error Mapping**: Convert low-level socket, timeout, and HTTP error codes (401, 404, 500) into typed domain errors (`AppError`).

---

## 2. Production Dio Client Architecture

```dart
// core/network/dio_client.dart
import 'package:dio/dio.dart';

class DioClient {
  final Dio dio;

  DioClient({required String baseUrl, required SecureTokenStorage tokenStorage})
      : dio = Dio(
          BaseOptions(
            baseUrl: baseUrl,
            connectTimeout: const Duration(seconds: 10),
            receiveTimeout: const Duration(seconds: 15),
            headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
          ),
        ) {
    dio.interceptors.addAll([
      // 1. Auth Interceptor: Injects Bearer Token
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await tokenStorage.getAccessToken();
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          return handler.next(options);
        },
        // 2. Token Refresh Interceptor on 401
        onError: (DioException error, handler) async {
          if (error.response?.statusCode == 401) {
            final refreshed = await tokenStorage.refreshSession();
            if (refreshed) {
              // Retry original request with new token
              final opts = Options(method: error.requestOptions.method, headers: error.requestOptions.headers);
              final cloneReq = await dio.request(error.requestOptions.path, options: opts, data: error.requestOptions.data);
              return handler.resolve(cloneReq);
            }
          }
          return handler.next(error);
        },
      ),
      // 3. Logger (in debug mode only)
      LogInterceptor(requestBody: true, responseBody: false),
    ]);
  }
}
```

---

## 3. Serialization & Model Design

Prefer lightweight, null-safe `fromJson` factory constructors:

```dart
class UserProfile {
  final String id;
  final String email;
  final String displayName;
  final DateTime createdAt;

  const UserProfile({
    required this.id,
    required this.email,
    required this.displayName,
    required this.createdAt,
  });

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      id: json['id'] as String,
      email: json['email'] as String,
      displayName: json['display_name'] as String? ?? 'Anonymous',
      createdAt: DateTime.parse(json['created_at'] as String),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'email': email,
    'display_name': displayName,
    'created_at': createdAt.toIso8601String(),
  };
}
```

---

## 4. File Upload with Progress Tracking

```dart
Future<void> uploadAvatar(File imageFile, void Function(int, int) onProgress) async {
  final formData = FormData.fromMap({
    'file': await MultipartFile.fromFile(imageFile.path, filename: 'avatar.jpg'),
  });

  await dio.post(
    '/users/avatar',
    data: formData,
    onSendProgress: onProgress,
  );
}
```

---

## 5. WebSockets for Real-Time Streaming

```dart
import 'package:web_socket_channel/web_socket_channel.dart';

class RealtimeFeedService {
  final WebSocketChannel _channel;

  RealtimeFeedService(Uri uri) : _channel = WebSocketChannel.connect(uri);

  Stream<dynamic> get stream => _channel.stream;

  void sendMessage(String message) => _channel.sink.add(message);

  void dispose() => _channel.sink.close();
}
```

---

## 6. Related References

- Security: [security.md](security.md)
- Database & Storage: [database-storage.md](database-storage.md)
- Flutter Architecture: [flutter-architecture.md](flutter-architecture.md)
