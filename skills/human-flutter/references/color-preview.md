# Color Placement Preview — 12-Component Visual UI Board

> **Mandatory Visual Theme Verification Gate** before finalizing or implementing `ThemeData` and `ColorScheme` in any Flutter project.

The agent must **NEVER** finalize theme code based solely on a raw list of HEX values. A structured, visual UI-style color placement preview demonstrating exactly where each color lives across the 12 core UI components MUST be presented to the user for explicit approval.

---

## 1. The 12 Mandatory UI Placement Elements

The preview board must demonstrate color assignment across these 12 canonical application touchpoints:

| # | UI Element | Default Role | Visual Intent |
|---|---|---|---|
| **1** | **App Background** | Surface / Canvas | Foundational canvas (`surface`, `surfaceContainerLowest`) |
| **2** | **Primary App Bar** | Top Chrome | Distinct elevation, clear title contrast, subtle divider |
| **3** | **Navigation Bar** | Bottom/Rail Nav | Active item accent highlight, inactive neutral muting |
| **4** | **Primary Button** | Main Action CTA | `primary` background with high-contrast `onPrimary` text |
| **5** | **Secondary Button** | Supporting Action | Outlined/tonal container with subtle border & text |
| **6** | **Cards & Containers** | Content Modules | Elevated/filled surface (`surfaceContainer`) with soft shadows |
| **7** | **Input Fields** | Form Controls | Neutral fill, focused primary border, error alert border |
| **8** | **Text & Headings** | Typography | High-contrast `onSurface` for titles, `onSurfaceVariant` for body |
| **9** | **Icons** | Visual Indicators | Matched to text luminance, accent color for interactive icons |
| **10**| **Borders & Dividers**| Structural Separation | Subtle, low-contrast `outline` / `outlineVariant` (1px) |
| **11**| **Selection States** | Chips, Tabs, Radios | Selected accent tint vs unselected neutral resting state |
| **12**| **Status Semantics** | Alerts & Badges | Success (green), Warning (amber), Error (red), Info (cyan) |

---

## 2. Visual UI Color Board Preview Template

When presenting the preview to the user in chat, the agent renders a markdown visual board following this exact layout:

````markdown
### 🎨 Visual UI Color Placement Preview Board

#### Selected Palette Swatches
- **Primary**: `[#2563EB]` (Royal Blue) — Primary interactive actions, active navigation, focus rings
- **Secondary**: `[#4F46E5]` (Indigo) — Supporting buttons, filter tags, badges
- **Tertiary**: `[#0D9488]` (Teal Accent) — Success indicators, metrics, special callouts
- **Neutral Surface**: `[#F8FAFC]` (Light Slate) / `[#0F172A]` (Dark Slate) — App backgrounds & card canvas

---

#### 📱 Component-by-Component Color Distribution

```text
┌────────────────────────────────────────────────────────┐
│ [1. App Bar] #F8FAFC (Surface) | Title: #0F172A       │
├────────────────────────────────────────────────────────┤
│ [8. Headings] Welcome Back (#0F172A)                   │
│ [8. Body Text] Review your metrics (#475569)           │
│                                                        │
│ ┌────────────────────────────────────────────────────┐ │
│ │ [6. Card Container] #FFFFFF (Surface Container)     │ │
│ │ [10. Border] 1px solid #E2E8F0                      │ │
│ │ [9. Icon] #2563EB (Primary) 📊 Analytics Report    │ │
│ │                                                    │ │
│ │ [11. Selection State]                               │ │
│ │ (•) Active Tab [#2563EB]   ( ) Inactive Tab [#94A3B8]│ │
│ │                                                    │ │
│ │ [7. Input Field]                                    │ │
│ │ ┌────────────────────────────────────────────────┐ │ │
│ │ │ Email Address... (Border: #CBD5E1 | Focus: #2563EB│ │
│ │ └────────────────────────────────────────────────┘ │ │
│ │                                                    │ │
│ │ [4. Primary Button]          [5. Secondary Button]  │ │
│ │ ┌───────────────────┐        ┌───────────────────┐  │ │
│ │ │ #2563EB (Primary) │        │ #F1F5F9 (Outline) │  │ │
│ │ │ Text: #FFFFFF     │        │ Text: #1E293B     │  │ │
│ │ └───────────────────┘        └───────────────────┘  │ │
│ └────────────────────────────────────────────────────┘ │
│                                                        │
│ [12. Status States]                                    │
│ [✓ Success: #10B981] [⚠ Warning: #F59E0B] [✕ Error: #EF4444]
│                                                        │
├────────────────────────────────────────────────────────┤
│ [3. Navigation Bar] #FFFFFF                            │
│ ⌂ Home [#2563EB Active]   🔍 Search [#64748B Inactive]  │
└────────────────────────────────────────────────────────┘
```

---

#### 🌓 Light vs. Dark Mode Mapping

| Component | Light Mode Token | Dark Mode Token | Contrast Ratio |
|---|---|---|---|
| Background (1) | `#F8FAFC` | `#0F172A` | AA Compliant |
| App Bar (2) | `#FFFFFF` | `#1E293B` | AA Compliant |
| Navigation Bar (3) | `#FFFFFF` | `#1E293B` | AA Compliant |
| Primary Button (4) | `#2563EB` (on: `#FFFFFF`) | `#3B82F6` (on: `#0F172A`) | 5.8:1 (AAA) |
| Secondary Button (5)| `#F1F5F9` (on: `#1E293B`)| `#334155` (on: `#F8FAFC`) | 6.2:1 (AAA) |
| Cards (6) | `#FFFFFF` | `#1E293B` | AA Compliant |
| Inputs Fill/Stroke (7)| `#FFFFFF` / `#E2E8F0` | `#1E293B` / `#475569` | AA Compliant |
| Primary Text (8) | `#0F172A` | `#F8FAFC` | 13.5:1 (AAA) |
| Icons (9) | `#2563EB` / `#64748B` | `#60A5FA` / `#94A3B8` | 4.8:1 (AA) |
| Borders (10) | `#E2E8F0` | `#334155` | 3.2:1 (AA Graphic)|
| Selected State (11)| `#2563EB` | `#60A5FA` | High Distinction |
| Status Success (12)| `#10B981` | `#34D399` | 4.6:1 (AA) |
| Status Warning (12)| `#F59E0B` | `#FBBF24` | 4.5:1 (AA) |
| Status Error (12) | `#EF4444` | `#F87171` | 4.9:1 (AA) |
````

---

## 3. Verification Protocol Before Proceeding

Once the visual board is displayed:
1. Explain in Bengali how the selected 3–4 colors harmonize.
2. Ask the user clearly in Bengali if they approve this distribution or want specific token adjustments.
3. **STOP** and wait for approval.
4. Only upon explicit approval, proceed to code `lib/core/theme/app_colors.dart` and `lib/core/theme/app_theme.dart`.
