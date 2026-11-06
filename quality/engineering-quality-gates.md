# Engineering Quality Gates

> **13-Point Pre-Delivery Verification Standard for Substantial Software Tasks**

Before delivering any substantial feature, architectural refactor, or release candidate, AI coding agents must verify each of the following 13 quality gates. Never claim a gate passed if it was not explicitly evaluated.

---

## The 13 Quality Gates Checklist

```markdown
### 13-Point Pre-Delivery Quality Checklist

- [ ] 1. **Requirement Satisfaction**: Does the implementation satisfy all explicit user acceptance criteria and implicit edge cases?
- [ ] 2. **Correct Framework Usage**: Does code strictly adhere to target framework idioms without cross-framework contamination?
- [ ] 3. **Architectural Consistency**: Does code respect the established 3-tier boundary (Controller -> Service -> Repository / Store -> Logic -> View)?
- [ ] 4. **Code Quality**: Zero dead code, no giant functions (> 50 lines), no excessive parameters (> 4), clean naming.
- [ ] 5. **UI Consistency**: Does UI align with existing design tokens (typography scale, 8pt spatial grid, semantic colors)?
- [ ] 6. **Responsive Behavior**: Tested on 375px mobile, 768px tablet, and 1280px desktop viewports without horizontal scrollbars.
- [ ] 7. **Accessibility (WCAG 2.1 AA)**: Minimum 4.5:1 text contrast, visible keyboard focus rings, semantic roles, screen-reader labels.
- [ ] 8. **Security & Input Sanitization**: Parameterized queries, context-aware output encoding, zero hardcoded credentials, safe URL validation.
- [ ] 9. **Performance Implications**: Virtualization for large lists, zero unconstrained rebuilds, proper asset sizing, lightweight bundle impact.
- [ ] 10. **Test Coverage**: Relevant unit, component, or integration tests implemented and executing with green status.
- [ ] 11. **Regression Risk Assessment**: Verified that public APIs remain backward-compatible and adjacent features operate without regression.
- [ ] 12. **Documentation Updates**: Updated relevant ADRs, API schemas, `PROJECT_CONTEXT.md`, or README notes.
- [ ] 13. **Git Diff Cleanliness**: Staged diff contains only intentional changes; zero temporary debug logs or unwanted whitespace churn.
```

---

## Gate Evaluation Protocol

When completing a task, output the status of all evaluated gates:

```markdown
### Pre-Delivery Quality Gate Summary
| Gate | Status | Notes |
|---|---|---|
| 1. Requirements | **PASSED** | All 4 checkout acceptance criteria satisfied. |
| 2. Framework Idioms | **PASSED** | React custom hook with clean unmount cleanup. |
| 3. Architecture | **PASSED** | Isolated state in `useBillingForm.ts`. |
| 4. Code Quality | **PASSED** | Max file length 142 lines, strict TypeScript. |
| 5. UI Tokens | **PASSED** | Used `var(--spacing-md)` and semantic status tokens. |
| 6. Responsiveness | **PASSED** | Form stacks cleanly on 375px mobile. |
| 7. Accessibility | **PASSED** | Verified with screen reader labels & 4.8:1 contrast. |
| 8. Security | **PASSED** | Card input uses masked fields; no PII logged. |
| 9. Performance | **PASSED** | Debounced address lookup by 300ms. |
| 10. Test Coverage | **PASSED** | 6 unit tests passing. |
| 11. Regression Risk | **PASSED** | No public exports altered. |
| 12. Documentation | **PASSED** | Updated component prop docs. |
| 13. Git Diff | **PASSED** | Clean 3-file diff reviewed. |
```

