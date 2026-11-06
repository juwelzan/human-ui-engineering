# Backend Development Progressive Reference

> **Quick-reference rules for Node.js, Python, Go, Java & Rust servers.**

- **Architecture Boundary**: Strictly separate Controller (transport) -> Service (domain rules) -> Repository (data persistence).
- **Startup Config**: Validate all environment variables during boot with schemas (Zod, Pydantic); fail fast on missing keys.
- **Worker Queues**: Offload heavy jobs (emails, image processing, analytics) to asynchronous queues with idempotency keys.
- **Graceful Shutdown**: Intercept `SIGTERM` / `SIGINT`, stop accepting new traffic, and complete in-flight requests cleanly within a timeout window.

See full guide in [`../../../frameworks/backend.md`](../../../frameworks/backend.md).
