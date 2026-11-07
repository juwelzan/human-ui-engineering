# Flutter Accessibility (A11y) Engineering

> Building accessible, WCAG 2.1 AA compliant Flutter applications with Semantics, screen reader testing, and keyboard navigation.

---

## 1. Principles of Flutter Accessibility

1. **Accessibility is Core, Not An Afterthought**: A premium application must be usable by everyone, including people using screen readers (TalkBack, VoiceOver), keyboard-only navigation, and high-contrast modes.
2. **Semantic Meaning**: Visual presentation does not equal semantic meaning. Flutter's engine generates an explicit Semantics Tree alongside the Render Tree. Custom UI must declare its purpose.
3. **Minimum Tap Targets**: All touch targets must measure at least **48x48dp** (`kMinInteractiveDimension`) to accommodate motor impairments.

---

## 2. The Semantics Widget

### Custom Button Semantics
```dart
Semantics(
  button: true,
  enabled: isEnabled,
  label: 'Add to cart',
  hint: 'Double tap to add current item to your shopping bag',
  onTap: isEnabled ? handleAddToCart : null,
  child: CustomCartButton(),
)
```

### Merging Semantics
Avoid screen readers reading icon, title, and timestamp as three separate jarring announcements:
```dart
MergeSemantics(
  child: Row(
    children: [
      const Icon(Icons.check_circle),
      const SizedBox(width: 8),
      Text('Order Delivered on Oct 24'),
    ],
  ),
)
```

### Excluding Decorative Elements
```dart
ExcludeSemantics(
  child: SvgPicture.asset('assets/illustrations/decorative_pattern.svg'),
)
```

---

## 3. Keyboard Focus & Tab Navigation

On Desktop and Web, ensure every interactive widget participates in the focus order:

```dart
Focus(
  onKeyEvent: (node, event) {
    if (event.logicalKey == LogicalKeyboardKey.enter) {
      handleSelect();
      return KeyEventResult.handled;
    }
    return KeyEventResult.ignored;
  },
  child: Builder(
    builder: (context) {
      final isFocused = Focus.of(context).hasFocus;
      return Container(
        decoration: BoxDecoration(
          border: isFocused ? Border.all(color: Colors.blue, width: 2) : null,
        ),
        child: MyCustomTile(),
      );
    },
  ),
)
```

---

## 4. Automated Accessibility Testing

Test semantics trees automatically using `SemanticsTester`:

```dart
testWidgets('Button meets semantic accessibility requirements', (tester) async {
  final semantics = SemanticsTester(tester);

  await tester.pumpWidget(
    MaterialApp(
      home: Scaffold(
        body: AppButton(label: 'Submit Order', onPressed: () {}),
      ),
    ),
  );

  expect(
    semantics,
    includesNodeWith(
      label: 'Submit Order',
      actions: [SemanticsAction.tap],
    ),
  );

  semantics.dispose();
});
```

---

## 5. Related References

- Accessibility Guide: [../../../design/accessibility.md](../../../design/accessibility.md)
- Accessibility Audit: [../../../quality/accessibility-audit.md](../../../quality/accessibility-audit.md)
- Components: [components.md](components.md)
