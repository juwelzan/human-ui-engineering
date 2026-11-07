# Core Engineering Architecture — `lib/core/`

> **Foundational Infrastructure & Enterprise Standards** for production Flutter applications within the Human Flutter Engineering system.

`lib/core/` provides the global foundation for the entire application. It contains zero feature-specific UI or domain logic. All features depend on `core/`, but `core/` never depends on any feature.

---

## 1. Directory Structure & Responsibilities

```text
lib/core/
├── constants/          # Application invariants, API endpoints, flavor configs
│   ├── app_constants.dart
│   └── api_endpoints.dart
├── errors/             # Global exceptions, failures, and functional Result pattern
│   ├── exceptions.dart
│   ├── failures.dart
│   └── result.dart
├── network/            # Dio HTTP client, SSL pinning, auth/retry interceptors
│   ├── api_client.dart
│   ├── auth_interceptor.dart
│   ├── retry_interceptor.dart
│   └── ssl_pinning.dart
├── storage/            # Secure key-value storage and local persistence abstractions
│   ├── secure_storage_service.dart
│   └── local_storage_service.dart
├── routing/            # Declarative GoRouter configuration, route paths, guards
│   ├── app_router.dart
│   ├── app_routes.dart
│   └── auth_guard.dart
├── theme/              # Central design tokens and Material 3 ThemeData
│   ├── app_colors.dart
│   ├── app_typography.dart
│   ├── app_spacing.dart
│   ├── app_radius.dart
│   ├── app_elevation.dart
│   └── app_theme.dart
└── utils/              # Pure utility functions, extensions, and validators
    ├── context_extensions.dart
    ├── date_formatters.dart
    └── string_validators.dart
```

---

## 2. Functional Error Handling & The Result Pattern

Never allow unhandled raw exceptions to leak into UI widgets. Core provides a type-safe functional `Result<T, Failure>` pattern leveraging Dart 3 sealed classes.

### Implementation: `lib/core/errors/failures.dart`
```dart
import 'package:flutter/foundation.dart';

@immutable
sealed class Failure {
  final String message;
  final int? statusCode;

  const Failure(this.message, {this.statusCode});
}

final class ServerFailure extends Failure {
  const ServerFailure([super.message = 'A server error occurred. Please try again.', super.statusCode]);
}

final class NetworkFailure extends Failure {
  const NetworkFailure([super.message = 'No internet connection detected.', super.statusCode]);
}

final class CacheFailure extends Failure {
  const CacheFailure([super.message = 'Failed to read from local storage.', super.statusCode]);
}

final class AuthFailure extends Failure {
  const AuthFailure([super.message = 'Session expired. Please log in again.', super.statusCode = 401]);
}

final class ValidationFailure extends Failure {
  final Map<String, String> fieldErrors;
  const ValidationFailure(super.message, {this.fieldErrors = const {}, super.statusCode = 422});
}
```

### Implementation: `lib/core/errors/result.dart`
```dart
import 'package:flutter/foundation.dart';
import 'failures.dart';

@immutable
sealed class Result<S, F extends Failure> {
  const Result();

  bool get isSuccess => this is Success<S, F>;
  bool get isFailure => this is FailureResult<S, F>;

  R fold<R>({
    required R Function(S data) onSuccess,
    required R Function(F failure) onFailure,
  }) {
    return switch (this) {
      Success(data: final data) => onSuccess(data),
      FailureResult(failure: final failure) => onFailure(failure),
    };
  }
}

final class Success<S, F extends Failure> extends Result<S, F> {
  final S data;
  const Success(this.data);
}

final class FailureResult<S, F extends Failure> extends Result<S, F> {
  final F failure;
  const FailureResult(this.failure);
}
```

---

## 3. Production Network Infrastructure with Dio

Core networking handles automatic header injection, bearer token refreshing, exponential retry backoff, and mapping raw Dio errors into `Failure` types.

### Implementation: `lib/core/network/api_client.dart`
```dart
import 'package:dio/dio.dart';
import '../constants/api_endpoints.dart';
import '../errors/exceptions.dart';
import '../errors/failures.dart';
import '../storage/secure_storage_service.dart';
import 'auth_interceptor.dart';
import 'retry_interceptor.dart';

class ApiClient {
  final Dio dio;
  final SecureStorageService secureStorage;

  ApiClient({
    required this.dio,
    required this.secureStorage,
  }) {
    dio.options = BaseOptions(
      baseUrl: ApiEndpoints.baseUrl,
      connectTimeout: const Duration(seconds: 15),
      receiveTimeout: const Duration(seconds: 15),
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    );

    dio.interceptors.addAll([
      AuthInterceptor(secureStorage: secureStorage, dio: dio),
      RetryInterceptor(dio: dio, maxRetries: 3),
      LogInterceptor(requestBody: false, responseBody: false),
    ]);
  }

  Future<Response<T>> get<T>(
    String path, {
    Map<String, dynamic>? queryParameters,
    CancelToken? cancelToken,
  }) async {
    try {
      return await dio.get<T>(
        path,
        queryParameters: queryParameters,
        cancelToken: cancelToken,
      );
    } on DioException catch (e) {
      throw _handleDioException(e);
    }
  }

  Future<Response<T>> post<T>(
    String path, {
    dynamic data,
    CancelToken? cancelToken,
  }) async {
    try {
      return await dio.post<T>(
        path,
        data: data,
        cancelToken: cancelToken,
      );
    } on DioException catch (e) {
      throw _handleDioException(e);
    }
  }

  Exception _handleDioException(DioException e) {
    return switch (e.type) {
      DioExceptionType.connectionTimeout ||
      DioExceptionType.sendTimeout ||
      DioExceptionType.receiveTimeout =>
        const NetworkException('Connection timed out. Please check your network.'),
      DioExceptionType.badResponse => switch (e.response?.statusCode) {
          401 => const UnauthorizedException('Authentication credentials invalid.'),
          404 => const NotFoundException('Requested resource not found.'),
          500 => const ServerException('Internal server error.'),
          _ => ServerException(e.response?.data?['message'] ?? 'Unexpected server response.'),
        },
      DioExceptionType.cancel => const RequestCancelledException('Request was cancelled.'),
      _ => const NetworkException('Network communication failed.'),
    };
  }
}
```

---

## 4. Secure Storage Service

For persisting sensitive data (JWT access tokens, refresh tokens, encryption keys, biometrics status), `core/storage` wraps `flutter_secure_storage` with strong typing and error isolation.

### Implementation: `lib/core/storage/secure_storage_service.dart`
```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../errors/exceptions.dart';

abstract interface class ISecureStorageService {
  Future<void> write(String key, String value);
  Future<String?> read(String key);
  Future<void> delete(String key);
  Future<void> deleteAll();
}

class SecureStorageService implements ISecureStorageService {
  final FlutterSecureStorage _storage;

  const SecureStorageService({FlutterSecureStorage? storage})
      : _storage = storage ??
            const FlutterSecureStorage(
              aOptions: AndroidOptions(encryptedSharedPreferences: true),
              iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock),
            );

  @override
  Future<void> write(String key, String value) async {
    try {
      await _storage.write(key: key, value: value);
    } catch (e) {
      throw CacheException('Failed to securely persist token for key: $key');
    }
  }

  @override
  Future<String?> read(String key) async {
    try {
      return await _storage.read(key: key);
    } catch (e) {
      throw CacheException('Failed to read secure token for key: $key');
    }
  }

  @override
  Future<void> delete(String key) async {
    try {
      await _storage.delete(key: key);
    } catch (e) {
      throw CacheException('Failed to delete secure key: $key');
    }
  }

  @override
  Future<void> deleteAll() async {
    try {
      await _storage.deleteAll();
    } catch (e) {
      throw CacheException('Failed to wipe secure storage');
    }
  }
}
```

---

## 5. Central Design Tokens

Core establishes the Single Source of Truth for visual design tokens across spacing, radius, typography, and color.

### A. Spacing Scale: `lib/core/theme/app_spacing.dart`
```dart
class AppSpacing {
  AppSpacing._();

  static const double xxs = 2.0;
  static const double xs = 4.0;
  static const double sm = 8.0;
  static const double md = 16.0;
  static const double lg = 24.0;
  static const double xl = 32.0;
  static const double xxl = 48.0;
  static const double xxxl = 64.0;
}
```

### B. Corner Radii: `lib/core/theme/app_radius.dart`
```dart
import 'package:flutter/material.dart';

class AppRadius {
  AppRadius._();

  static const double smValue = 4.0;
  static const double mdValue = 8.0;
  static const double lgValue = 12.0;
  static const double xlValue = 16.0;
  static const double fullValue = 999.0;

  static const BorderRadius sm = BorderRadius.all(Radius.circular(smValue));
  static const BorderRadius md = BorderRadius.all(Radius.circular(mdValue));
  static const BorderRadius lg = BorderRadius.all(Radius.circular(lgValue));
  static const BorderRadius xl = BorderRadius.all(Radius.circular(xlValue));
  static const BorderRadius full = BorderRadius.all(Radius.circular(fullValue));
}
```

### C. BuildContext Ergonomics: `lib/core/utils/context_extensions.dart`
```dart
import 'package:flutter/material.dart';

extension ContextExtensions on BuildContext {
  ThemeData get theme => Theme.of(this);
  ColorScheme get colorScheme => Theme.of(this).colorScheme;
  TextTheme get textTheme => Theme.of(this).textTheme;
  MediaQueryData get mediaQuery => MediaQuery.of(this);
  Size get screenSize => MediaQuery.sizeOf(this);
  bool get isDarkMode => Theme.of(this).brightness == Brightness.dark;
}
```

---

## 6. Golden Invariants for `lib/core/`

1. **Zero Downward Dependencies**: Never import `package:my_app/features/...` inside `core/`.
2. **Platform Isolation**: Wrap third-party packages (`dio`, `flutter_secure_storage`) behind pure abstract interfaces so features remain testable with standard mocks.
3. **No Stateful UI**: Never put screen widgets or mutable navigation state in `core/`. Only pure theme tokens, router definitions, and network services live here.
