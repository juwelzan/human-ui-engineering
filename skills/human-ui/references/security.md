# Security Mode Reference (`/human-ui security`)

> **Vulnerability Auditing, Threat Modeling, Input Sanitization & Auth Hardening**

When invoked with `/human-ui security [scope]`:

1. **Vulnerability Audit Checklist**:
   - Check for hardcoded secrets, API keys, or private tokens.
   - Inspect input perimeters for SQL injection, Command injection, or XSS vectors.
   - Verify that all database queries use parameterized interfaces.
   - Audit authentication sessions: verify `HttpOnly`, `Secure`, `SameSite=Strict` cookies.
   - Audit authorization boundaries: check for IDOR (Broken Object Level Authorization).
2. **Dependency Supply Chain Check**:
   - Run dependency audit (`npm audit`, `dart pub audit`, `cargo audit`, `pip-audit`).
3. **Remediation Protocol**:
   - Apply the smallest safe patch for verified vulnerabilities.
   - Add security regression tests confirming that malicious input payloads are safely rejected or escaped.

See [`../../../engineering/security.md`](../../../engineering/security.md) for full security rules.
