# Cross-Platform Adaptation & Internationalization

> Architectural rules for multi-platform UX idioms, hardware safe areas, and localization (i18n/L10n).

---

## 1. Purpose

A cross-platform app (Flutter, React Native, or responsive Web) that feels like a poorly ported alien application fails with users. True cross-platform engineering balances a unified brand identity with deep respect for platform-specific hardware, navigation idioms, and international linguistic differences.

This guide defines the standards for multi-platform excellence.

---

## 2. Platform Idiom Matrix

| UX Element | iOS Platform Idiom | Android Platform Idiom | Web / Desktop Idiom |
|---|---|---|---|
| **Primary Navigation** | Bottom tab bar (translucent blur) | Bottom navigation bar or navigation rail | Left persistent sidebar or top navigation bar |
| **Back Navigation** | Interactive edge-swipe gesture + top left Chevron | Predictive back gesture / hardware back | Browser back button + breadcrumbs |
| **Action Confirmation** | Bottom Action Sheet (`UIActionSheet`) | Modal Bottom Sheet or Alert Dialog | Centered Modal Dialog or Popover |
| **Scroll Physics** | Elastic rubber-band overshoot with high friction | Overscroll stretch effect with linear deceleration | Scrollbar with discrete wheel ticks |
| **Context Menus** | Long-press / Haptic touch preview card | Long-press bottom sheet | Right-click context menu |
| **Icons** | SF Symbols (thin, smooth rounded strokes) | Material Symbols (geometric, sharp/rounded) | Lucide, Feather, or Heroicons |

---

## 3. Hardware Insets & Safe Areas

Modern mobile and desktop devices have physical display cutouts, camera notches, Dynamic Islands, and software home indicator bars. 

### Mandatory Safe Area Handling:
- **Never allow interactive elements or text to collide with physical cutouts or home indicators**.
- **Web**:
  ```css
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
  ```
- **Flutter**: Wrap edge views in `SafeArea()`.
- **Android**: Use `Modifier.windowInsetsPadding(WindowInsets.safeDrawing)`.
- **iOS**: Respect `safeAreaInsets` or `.ignoresSafeArea()` only for edge-to-edge background artwork, never for interactive buttons.

---

## 4. Internationalization (i18n) & Localization (L10n)

### 1. No Hardcoded Strings
Never render hardcoded English strings inside UI components:
```tsx
// Anti-Pattern
<Button>Submit Payment</Button>

// Standard
<Button>{t('checkout.submit_payment')}</Button>
```

### 2. Layout Flexibility for Text Expansion
Translations vary drastically in length:
- German and French phrases are often **30% to 50% longer** than English equivalents.
- Asian languages (Chinese, Japanese) require higher line-heights to prevent complex glyph collisions.
- **Rule**: Never lock fixed widths on buttons or labels containing localized text. Allow containers to wrap or expand naturally.

### 3. Bidirectional Support (RTL: Arabic, Hebrew)
Always use **logical properties** rather than physical `left` and `right`:
- Use `margin-inline-start` instead of `margin-left`.
- Use `margin-inline-end` instead of `margin-right`.
- Use `text-align: start` instead of `text-align: left`.
- In Flutter and Native frameworks, use `EdgeInsetsDirectional.fromSTEB()` instead of hardcoded `left`/`right`.
- Icons indicating direction (e.g. back arrows `←`, forward arrows `→`) must automatically mirror in RTL layouts.

---

## 5. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Responsive Design: [../design/responsive-design.md](../design/responsive-design.md)
- Navigation: [../components/navigation.md](../components/navigation.md)
- Clean Code: [clean-code.md](clean-code.md)
