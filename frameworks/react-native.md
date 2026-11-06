# React Native UI Engineering Guide

> Practical engineering guide for building cross-platform mobile applications using React Native, Expo, the New Architecture (Fabric), and NativeWind.

---

## 1. Recommended Project Structure (Expo / Bare RN)

Follow a modern modular Feature-First layout:

```text
src/
├── components/                 # Global UI primitives
│   ├── ui/                     # AppButton.tsx, AppInput.tsx, AppCard.tsx
│   └── feedback/               # Skeletons, ErrorBoundary
├── core/
│   ├── theme/                  # Color tokens, typography, spacing
│   └── api/                    # Network clients
├── features/                   # Feature domain modules
│   ├── feed/
│   │   ├── components/         # FeedItemRow.tsx
│   │   ├── hooks/              # useFeedData.ts
│   │   └── FeedScreen.tsx      # Main screen
│   └── profile/
├── navigation/                 # Expo Router (app/) or React Navigation stacks
└── App.tsx
```

---

## 2. Component Design & Native Primitives

- **Use Native Primitives Exclusively**: React Native does not use DOM elements. Never render `<div>`, `<span>`, `<button>`, or `<a>`:
  - Containers: `<View>`
  - Text: `<Text>` (all raw strings MUST be wrapped in a `<Text>` element; un-wrapped text throws runtime fatal exceptions)
  - Interactive: `<Pressable>` (avoid legacy `TouchableOpacity` where possible)
- **Accessible Pressable Component**:
  ```tsx
  import { Pressable, Text, ActivityIndicator, StyleSheet } from 'react-native';

  interface AppButtonProps {
    label: string;
    onPress: () => void;
    isLoading?: boolean;
    disabled?: boolean;
  }

  export function AppButton({ label, onPress, isLoading, disabled }: AppButtonProps) {
    return (
      <Pressable
        accessibilityRole="button"
        accessibilityState={{ disabled: disabled || isLoading, busy: isLoading }}
        accessibilityLabel={label}
        disabled={disabled || isLoading}
        onPress={onPress}
        hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
        style={({ pressed }) => [
          styles.button,
          pressed && styles.pressed,
          (disabled || isLoading) && styles.disabled,
        ]}
      >
        {isLoading ? (
          <ActivityIndicator color="#FFFFFF" />
        ) : (
          <Text style={styles.text}>{label}</Text>
        )}
      </Pressable>
    );
  }
  ```

---

## 3. Responsive Layout & Safe Areas

1. **Safe Area Insets**: Always wrap screens in `SafeAreaView` from `react-native-safe-area-context` to prevent collision with notches and home bars.
2. **Dynamic Viewport Dimensions**: Use `useWindowDimensions()` rather than static `Dimensions.get()` to adapt when foldables unfold or screens rotate.
3. **Hit Slop**: When icon buttons are small (< 44pt), expand their touch area with `hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}`.

---

## 4. Performance Optimization

1. **FlashList (Shopify)**: Replace standard `FlatList` with `@shopify/flash-list`. FlashList recycles views across iOS and Android, eliminating memory spikes and maintaining steady 60fps scrolling.
2. **New Architecture (Fabric & TurboModules)**: Enable the New Architecture in modern RN versions (v0.74+) to execute synchronous native calls without serialized bridge bottlenecks.
3. **Reanimated & Gesture Handler**: Use `react-native-reanimated` for smooth 60/120fps animations running directly on the native UI thread.

---

## 5. Testing

- Use **React Native Testing Library (RNTL)**:
  ```tsx
  import { render, screen, fireEvent } from '@testing-library/react-native';
  import { AppButton } from './AppButton';

  test('calls onPress when tapped', () => {
    const handlePress = jest.fn();
    render(<AppButton label="Checkout" onPress={handlePress} />);

    fireEvent.press(screen.getByRole('button', { name: /checkout/i }));
    expect(handlePress).toHaveBeenCalledTimes(1);
  });
  ```

---

## 6. Common Mistakes to Avoid

1. **Rendering Raw Text Outside `<Text>`**: Placing raw text inside `<View>Hello</View>` causes an immediate red-screen crash on native devices.
2. **Hardcoding Fixed Pixel Widths**: Using `width: 380` which clips on iPhone SE (320pt) or fails to expand on tablets.
3. **Heavy Synchronous Operations on JS Thread**: Running heavy array filtering or JSON parsing synchronously, which blocks touch events and UI animations.

---

## 7. Related Documentation

- Framework Selection: [framework-selection.md](framework-selection.md)
- Framework Isolation: [README.md](README.md)
- React Guide: [react.md](react.md)
- Cross-Platform Standards: [../engineering/cross-platform.md](../engineering/cross-platform.md)

