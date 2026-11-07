# Flutter Build & Store Release Engineering

> Release preparation, signing, obfuscation, CI/CD, and Play Store & App Store deployment guidelines for Flutter.

---

## 1. Principles of Release Engineering

1. **Deterministic Versioning**: Follow Semantic Versioning in `pubspec.yaml` (`version: X.Y.Z+buildNumber`). The build number must increment with every uploaded artifact.
2. **Obfuscation by Default**: Always release production binaries with `--obfuscate` and save debug symbols for crash symbolication.
3. **Automated Verification**: Never submit to app stores without automated tests, linting, and smoke testing across target devices.

---

## 2. Android Build & Release Preparation

### 1. Keystore & Signing Config
Never commit signing credentials (`keystore.jks`, `key.properties`) into source control. Store `key.properties` locally:

```properties
storePassword=SECURE_STORE_PASSWORD
keyPassword=SECURE_KEY_PASSWORD
keyAlias=upload_key
storeFile=/path/to/upload-keystore.jks
```

Configure `android/app/build.gradle`:
```groovy
signingConfigs {
    release {
        storeFile file(keystoreProperties['storeFile'])
        storePassword keystoreProperties['storePassword']
        keyAlias keystoreProperties['keyAlias']
        keyPassword keystoreProperties['keyPassword']
    }
}
buildTypes {
    release {
        signingConfig signingConfigs.release
        minifyEnabled true
        shrinkResources true
    }
}
```

### 2. Generate Android App Bundle (AAB)
```bash
flutter build appbundle --release --obfuscate --split-debug-info=build/app/outputs/symbols
```

---

## 3. iOS Build & Release Preparation

### 1. Signing & Xcode Capabilities
- Open `ios/Runner.xcworkspace` in Xcode.
- Verify **Team**, **Bundle Identifier**, and **Capabilities** (Push Notifications, Associated Domains, In-App Purchase).
- Ensure `PrivacyInfo.xcprivacy` (Apple Privacy Manifest) is included.

### 2. Generate iOS Archive / IPA
```bash
flutter build ipa --release --obfuscate --split-debug-info=build/ios/outputs/symbols
```

---

## 4. Flutter Web Build

```bash
flutter build web --release --pwa-strategy=offline-first
```

---

## 5. Pre-Release Checklist

- [ ] All unit, widget, and integration tests pass (`flutter test`).
- [ ] Static analysis clean with zero warnings (`flutter analyze`).
- [ ] Version and build number bumped in `pubspec.yaml`.
- [ ] App launcher icons generated via `flutter_launcher_icons`.
- [ ] Splash screens configured via `flutter_native_splash`.
- [ ] Privacy policies, terms of service, and app store screenshots prepared.
- [ ] Symbol files archived for Crashlytics/Sentry de-obfuscation.

---

## 6. Related References

- Security: [security.md](security.md)
- Release Checklist: [../../../quality/release-checklist.md](../../../quality/release-checklist.md)
- DevOps: [../../../engineering/devops-release.md](../../../engineering/devops-release.md)
