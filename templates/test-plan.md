# Structured Test Plan Template

> **Standard fillable template for planning and executing verification suites.**

```markdown
# Test Plan: [Feature / Module Name]

- **Date**: YYYY-MM-DD
- **Target Component / Service**: [e.g., `src/features/billing/`]
- **Author**: [AI Pair Programmer / Human Engineer]
- **Target Environment**: [e.g., Local Node.js / Docker Postgres]

---

## 1. Scope & Objectives

[Brief description of features under test, risk areas, and non-goals.]

---

## 2. Test Matrix & Coverage Strategy

| Test Layer | Test Case Description | Target File / Command | Expected Outcome | Status |
|---|---|---|---|---|
| **Unit** | Calculate tax for zero-rate exemptions | `taxCalculator.test.ts` | Returns `$0.00` with exemption flag | [PASSED] |
| **Unit** | Reject expired credit card format | `cardValidator.test.ts` | Throws `InvalidExpiryError` | [PASSED] |
| **Component** | Form submit button remains disabled until valid | `BillingForm.test.tsx` | Button has `disabled` attribute | [PASSED] |
| **API** | POST /api/v1/checkout idempotency | `checkout.api.test.ts` | Second call with same key returns cached 201 | [PASSED] |
| **A11y** | Error messages announced by screen readers | `BillingForm.a11y.test.tsx` | Error container has `role="alert"` | [PASSED] |
| **Regression** | Ensure legacy webhook still receives ping | `webhook.test.ts` | Returns 200 OK | [PASSED] |

---

## 3. Execution Commands & Telemetry

```bash
# Unit & Component Tests
npm test src/features/billing/

# Type Check
npm run typecheck

# Lint & Formatting
npm run lint
```

---

## 4. Blocker & Limitation Log

- **Known Blockers**: [None | External API sandbox down]
- **Unverified Edge Cases**: [e.g., High-concurrency race conditions require load testing in staging]
```

