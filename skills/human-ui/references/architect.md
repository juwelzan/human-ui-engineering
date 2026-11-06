# Architect Mode Reference (`/human-ui architect`)

> **System Architecture Evaluation & Architecture Decision Record (ADR) Authoring**

When invoked with `/human-ui architect [task]`:

1. **Analyze Existing System**:
   - Inspect package boundaries, directory structures, and state management paradigms.
   - Review existing ADRs in [`../../../docs/adr/`](../../../docs/adr/README.md).
2. **Evaluate Architecture Trade-Offs**:
   - Assess scalability, maintainability, team skill boundaries, bundle overhead, and runtime latency.
   - Evaluate Layered vs Clean vs Feature-first vs MVVM/MVI architectures.
3. **Draft Architecture Decision Record (ADR)**:
   - Copy [`../../../templates/adr.md`](../../../templates/adr.md) to `docs/adr/NNNN-title.md`.
   - Fill in: Context, Decision Drivers, Considered Alternatives (pros/cons), Decision Outcome, Consequences, and Migration Implications.
4. **Present Architectural Proposal**:
   - Summarize the structural recommendation in chat.
   - Outline migration steps and blast radius before modifying any application code.

