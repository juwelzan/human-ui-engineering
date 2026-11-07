# Cross-Platform Adaptation & Internationalization

> Architectural rules for multi-platform UX idioms, hardware safe areas, and localization (i18n/L10n).

---

## 1. Purpose

A multi-platform Flutter application that feels like a poorly ported alien application fails with users. True Flutter cross-platform engineering balances a unified brand identity with deep respect for platform-specific hardware, navigation idioms, and international linguistic differences across Android, iOS, macOS, Windows, Linux, and Flutter Web.

This guide defines the standards for multi-platform Flutter excellence.

---

## 2. Platform Idiom Matrix in Flutter

| UX Element | iOS Platform Idiom | Android Platform Idiom | Web & Desktop Idiom |
|---|---|---|---|
| **Primary Navigation** | `CupertinoTabBar` or translucent pill bar | `NavigationBar` or `NavigationRail` | Left persistent sidebar / drawer |
| **Back Navigation** | Interactive edge-swipe gesture (`CupertinoPageRoute`) | Predictive back gesture / hardware back | Browser back button (`go_router`) |
| **Action Confirmation** | `showCupertinoModalPopup` Action Sheet | `showModalBottomSheet` or `AlertDialog` | Centered `showDialog` |
| **Scroll Physics** | `BouncingScrollPhysics` | `ClampingScrollPhysics` | Desktop wheel physics with scrollbar |
| **Context Menus** | `CupertinoContextMenu` | Material Long-press context menu | Right-click mouse context menu |
| **Icons** | `CupertinoIcons` (SF Symbols aligned) | `Icons` (Material Symbols) | Platform-adaptive iconography |

---

## 3. Hardware Insets & Safe Areas

Modern mobile and desktop devices have physical display cutouts, camera notches, Dynamic Islands, and software home indicator bars. 

### Mandatory Safe Area Handling:
- **Never allow interactive elements or text to collide with physical cutouts or home indicators**.
- In Flutter, wrap top-level scaffold bodies in `SafeArea`:
  ```dart
  Scaffold(
    body: SafeArea(
      top: true,
      bottom: true,
      child: ContentBody(),
    ),
  );
  ```
- For edge-to-edge background media, extend artwork beneath safe areas using `extendBodyBehindAppBar: true`, but ensure text and interactive controls remain inside `SafeArea`.

---

## 4. Internationalization (i18n) & Localization (L10n)

### 1. No Hardcoded Strings
Never render hardcoded English strings inside Flutter widgets:
```dart
// ❌ Anti-Pattern: Hardcoded text strings
AppButton.primary(
  label: 'Submit Payment',
  onPressed: _submit,
);

// ✅ Standard: Flutter AppLocalizations (generated from ARB files)
AppButton.primary(
  label: AppLocalizations.of(context)!.submitPayment,
  onPressed: _submit,
);
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

