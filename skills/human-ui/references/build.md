# Build Mode Reference (`/human-ui build`)

> **End-to-End Full-Stack Feature Implementation & Assembly**

When invoked with `/human-ui build [task]`:

1. **Verify Plan & Constraints**: Confirm active tech stack and project invariants from [`../../../PROJECT_CONTEXT.md`](../../../PROJECT_CONTEXT.md).
2. **Foundation First**:
   - Create or update required domain models, TypeScript interfaces, or schema migrations.
   - Construct reusable shared component primitives in `components/` before creating screens.
3. **Assemble Feature**:
   - Implement business logic in isolated services/hooks.
   - Assemble views following unidirectional data flow (UDF).
   - Leverage established design tokens (8pt grid, semantic colors, typographic scales).
4. **Targeted Validation**:
   - Run type check and lint.
   - Run relevant unit and component tests.
5. **Quality Gate Verification**:
   - Check against the 13 quality gates in [`../../../quality/engineering-quality-gates.md`](../../../quality/engineering-quality-gates.md).
   - Report honest results with changed files and verification commands.
