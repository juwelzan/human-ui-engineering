# Docs Mode Reference (`/human-ui docs`)

> **Technical Documentation, API Contracts & System Context Maintenance**

When invoked with `/human-ui docs [scope]`:

1. **Identify Documentation Scope**:
   - Component / Service API documentation (docstrings, JSDoc, Dartdoc).
   - System documentation ([`../../../PROJECT_CONTEXT.md`](../../../PROJECT_CONTEXT.md), README.md).
   - Architecture Decision Records ([`../../../docs/adr/`](../../../docs/adr/README.md)).
   - OpenAPI schemas or protocol buffers.
2. **Effective Documentation Principles**:
   - Document *why* and *assumptions*, not just obvious *what*.
   - Include practical code examples and edge case notes.
   - Maintain documentation integrity: preserve existing comments and docstrings unless explicitly requested.
3. **Validate All Links**:
   - Ensure all internal relative markdown links resolve to valid files without 404s.

