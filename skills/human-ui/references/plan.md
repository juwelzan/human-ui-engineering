# Plan Mode Reference (`/human-ui plan`)

> **Structured Task Decomposition, Dependency Mapping & Risk Assessment**

When invoked with `/human-ui plan [task]`:

1. **Strictly Read-Only**: **DO NOT write, modify, or delete any source files.**
2. **Project Discovery**: Inspect package manifests, active architecture, design tokens, and git status.
3. **Task Decomposition**: Break the request into numbered, ordered subtasks with clear blast radii:
   - Types and schemas first.
   - Shared component primitives second.
   - Domain logic and state management third.
   - View assembly fourth.
   - Tests and validation fifth.
4. **Risk & Dependency Identification**:
   - List external libraries required (if any).
   - Identify potential breaking changes to public APIs or schemas.
   - Flag performance or security hotspots.
5. **Output**: Present the structured implementation plan in chat and request confirmation before transitioning to Developer Mode.

See detailed orchestration rules in [`../../../core/task-orchestration.md`](../../../core/task-orchestration.md).

