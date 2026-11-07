# Template: UI Bug Report & Root Cause Analysis

> Fillable template for documenting, isolating, reproducing, and resolving UI bugs.

---

## 1. Defect Overview

- **Bug Title**: [Concise summary, e.g. "Input field obscured by virtual keyboard on mobile"]
- **Affected Area**: [Screen / Component name, e.g. `lib/features/auth/presentation/screens/login_screen.dart`]
- **Severity**: [Critical / High / Medium / Low]
- **Target Platform**: [iOS / Android / Web / Desktop]
- **Viewport Dimensions**: [e.g. 375px width (iPhone SE portrait)]

---

## 2. Steps to Reproduce

1. Navigate to `[Screen / URL]`.
2. Tap on `[Input field / Button]`.
3. Observe behavior: `[Describe incorrect behavior]`.
4. Expected behavior: `[Describe correct human behavior]`.

---

## 3. Evidence & Diagnostics

- **Error Message / Console Log**:
  ```text
  [Paste console error, stack trace, or RenderFlex overflow message here]
  ```
- **Observed Behavior**: [e.g. "Submit button pushed 40px off-screen; yellow-black stripes appear"]

---

## 4. Root Cause Analysis (RCA)

- **Failure Category**: [Layout Overflow / Null Crash / Race Condition / Sticky Hover / Z-Index / Memory Leak]
- **Technical Explanation**: [Explain exactly why the bug occurred, e.g. "Flex child lacked `min-w-0`, preventing text ellipsis truncation"]

---

## 5. Applied Surgical Fix & Verification

- **Files Modified**: `[List of files]`
- **Surgical Diff Summary**: [Describe the minimal edit made]
- **Automated Regression Test**: `[Test file name and test case title]`
- **Verification Status**:
  - [ ] Mobile (375px) Verified
  - [ ] Tablet (768px) Verified
  - [ ] Desktop (1280px) Verified
  - [ ] Automated Test Passing

