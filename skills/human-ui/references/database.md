# Database Engineering Progressive Reference

> **Quick-reference rules for PostgreSQL, MySQL, SQLite, MongoDB & Redis.**

- **Parameterized Queries**: Never concatenate raw strings into SQL queries. Always use parameterized queries or trusted ORMs.
- **Zero-Downtime Migrations**: Use the Expand and Contract pattern across deploy cycles. Never drop columns before updating running apps.
- **Concurrent Indexing**: In PostgreSQL, always create indexes on production tables with `CREATE INDEX CONCURRENTLY`.
- **Eliminate N+1 Queries**: Batch child entity queries using JOINs, `WHERE id IN (...)`, or `DataLoader`.
- **Connection Pooling**: Size connection pools to $(2 \times \text{cores}) + \text{spindles}$; use connection proxies (PgBouncer) in serverless runtimes.

See full guide in [`../../../frameworks/database.md`](../../../frameworks/database.md).

