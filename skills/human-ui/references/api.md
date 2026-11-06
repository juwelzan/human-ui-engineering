# API Development Progressive Reference

> **Quick-reference rules for REST, GraphQL, gRPC & WebSockets.**

- **Contract-First**: Define schemas using OpenAPI 3.1, Protobuf, or GraphQL before implementing handlers.
- **Keyset Pagination**: Always default to cursor-based pagination (`limit`, `cursor`) for collections exceeding 1,000 items.
- **Idempotency**: Mandate `Idempotency-Key` headers on mutating requests (POST / transactions).
- **Error Standard**: Return machine-parseable error structures conforming to RFC 7807 (`type`, `title`, `status`, `detail`, `traceId`).
- **Rate Limiting**: Enforce Token Bucket limits with `RateLimit-*` and `Retry-After` headers.

See full guide in [`../../../frameworks/api.md`](../../../frameworks/api.md).
