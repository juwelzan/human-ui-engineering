# Flutter Security & Privacy Engineering

> Mobile and multi-platform security best practices: secure storage, certificate pinning, code obfuscation, and biometric authentication.

---

## 1. Principles of Flutter Security

1. **Defense in Depth**: Client-side code runs in an untrusted environment. Never rely on the mobile app to enforce authorization or access control; always validate on the server.
2. **Zero Plaintext Secrets**: Never commit API keys, private keys, or passwords into Git. Use compile-time environment variables (`--dart-define` or `--dart-define-from-file`).
3. **Hardware-Backed Storage**: All auth tokens, encryption keys, and refresh secrets must be stored in the OS Keystore (Android) or Keychain (iOS).

---

## 2. Compile-Time Secrets via `--dart-define`

Avoid hardcoding API endpoints and secrets:

```dart
class AppConfig {
  static const String apiBaseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'https://api.example.com',
  );

  static const String sentryDsn = String.fromEnvironment('SENTRY_DSN');
}
```

Run with:
```bash
flutter run --dart-define=API_BASE_URL=https://staging.example.com
```

---

## 3. SSL / TLS Certificate Pinning

Prevent Man-in-the-Middle (MitM) attacks by pinning server public keys or certificates in `Dio`:

```dart
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:dio/io.dart';

void setupCertificatePinning(Dio dio, String expectedFingerprint) {
  dio.httpClientAdapter = IOHttpClientAdapter(
    createHttpClient: () {
      final client = HttpClient(context: SecurityContext(withTrustedRoots: false));
      client.badCertificateCallback = (X509Certificate cert, String host, int port) {
        // Compare SHA-256 fingerprint against expected hash
        return cert.sha256.toString() == expectedFingerprint;
      };
      return client;
    },
  );
}
```

---

## 4. Biometric Authentication

```dart
import 'package:local_auth/local_auth.dart';

class BiometricAuthService {
  final LocalAuthentication _auth = LocalAuthentication();

  Future<bool> authenticate() async {
    final canCheck = await _auth.canCheckBiometrics;
    if (!canCheck) return false;

    return _auth.authenticate(
      localizedReason: 'Please authenticate to view your sensitive financial records',
      options: const AuthenticationOptions(
        biometricOnly: true,
        stickyAuth: true,
      ),
    );
  }
}
```

---

## 5. Production Release Hardening

When building release binaries:
1. **Enable Code Obfuscation**:
   ```bash
   flutter build appbundle --obfuscate --split-debug-info=symbols/android
   flutter build ipa --obfuscate --split-debug-info=symbols/ios
   ```
2. **Background Screen Protection**: Blank or blur the screen when transitioning to background to prevent sensitive data from appearing in the OS app switcher (`AppLifecycleListener`).

---

## 6. Related References

- Security Standards: [../../../engineering/security.md](../../../engineering/security.md)
- Database & Storage: [database-storage.md](database-storage.md)
- Build & Release: [build-release.md](build-release.md)
