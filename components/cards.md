# Card Component Engineering

> Anatomy, elevation, compound architecture, and heuristics to avoid card overuse.

---

## 1. Purpose

Cards are containment surfaces used to group related, heterogeneous information together. However, overusing cards—putting every statistic, paragraph, or form field into its own rounded border box—leads to visual noise and cluttered interfaces. 

This guide defines the engineering requirements for card primitives.

---

## 2. When to Use a Card (And When NOT To)

### USE a Card When:
- Grouping heterogeneous content that forms a single logical entity (e.g. a product item with image, title, price, and "Add to Cart" button).
- Presenting modular items in a masonry or responsive grid (e.g. blog post summaries, dashboard widgets).
- Isolating a self-contained interactive widget (e.g. a payment method summary card).

### DO NOT Use a Card When:
- Displaying homogeneous, tabular data (use a clean **Table** or **List** instead).
- Presenting a simple form or settings view (use whitespace and subtle horizontal dividers instead).
- Wrapping an isolated statistic or single line of text.

---

## 3. Anatomy of a Production Card

Structure cards using compound components:

```text
┌────────────────────────────────────────────────────────┐
│ CardHeader                                             │
│   Avatar   CardTitle                      [Badge/Menu] │
│            CardDescription                             │
├────────────────────────────────────────────────────────┤
│ CardContent / Body                                     │
│   Primary content, charts, forms, or text blocks       │
├────────────────────────────────────────────────────────┤
│ CardFooter                                             │
│   [Secondary Metadata]          [Primary Action Button]│
└────────────────────────────────────────────────────────┘
```

### Compound Pattern Implementation (React Example):
```tsx
<Card variant="outline">
  <CardHeader>
    <div>
      <CardTitle>Cloud Storage</CardTitle>
      <CardDescription>Enterprise plan usage</CardDescription>
    </div>
    <Badge variant="warning">82% Full</Badge>
  </CardHeader>
  <CardContent>
    <ProgressBar value={82} />
  </CardContent>
  <CardFooter>
    <Button variant="ghost" size="sm">View Logs</Button>
    <Button variant="primary" size="sm">Upgrade</Button>
  </CardFooter>
</Card>
```

---

## 4. Card Variants

| Variant | Visual Attributes | Recommended Context |
|---|---|---|
| **Outlined (Flat)** | 1px subtle border (`border-default`), zero shadow, clean surface | Preferred for modern data dashboards, dense SaaS views |
| **Elevated** | Subtle ambient drop shadow (`shadow-sm`), transparent or borderless | Used for floating panels, draggable cards, popovers |
| **Interactive** | Outlined with hover border highlight + scale or shadow lift | Clickable summaries that navigate to detail pages |

---

## 5. Interactive Cards & Nested Action Rules

When an entire card is clickable (navigates to a detail route):
1. **Never Nest Interactive Elements Directly Inside a Clickable Surface**: Placing a `<button>` inside an `<a>` tag is invalid HTML and confuses screen readers.
2. **The Stretched Link Pattern**: Wrap the title in an anchor tag and stretch its pseudo-element (`after:absolute after:inset-0`) over the entire card. If the card contains secondary actions (like a "Favorite" star button), elevate the secondary button above the stretched link with `relative z-10`.
3. **Keyboard Focus**: The interactive card must show a distinct focus ring when tabbed to.

---

## 6. Related Documentation

- Master Instructions: [../AGENTS.md](../AGENTS.md)
- Shared Component Rules: [shared-component-rules.md](shared-component-rules.md)
- Spacing System: [../design/spacing.md](../design/spacing.md)
- Buttons: [buttons.md](buttons.md)

