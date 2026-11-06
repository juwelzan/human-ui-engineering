# React Native / Expo Progressive Reference

> **Quick-reference rules for Mobile React Native, Fabric & FlashList.**

- **Architecture Standard**: Use Expo with the New Architecture (Fabric renderer & TurboModules enabled).
- **Core Primitives**: Never use raw HTML elements (`div`, `span`, `p`); use `View`, `Text`, `Pressable`.
- **List Performance**: Always use `@shopify/flash-list` instead of unoptimized `FlatList` or `ScrollView`.
- **Safe Areas**: Wrap screens in `SafeAreaProvider` and `useSafeAreaInsets` to respect device notches and home indicator bars.
- **Styling**: Use `StyleSheet.create()` or NativeWind for high-performance styling without runtime overhead.

See full guide in [`../../../frameworks/react-native.md`](../../../frameworks/react-native.md).

