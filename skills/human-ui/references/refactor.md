# Refactor Mode Reference (`/human-ui refactor`)

> **Safe, Behavior-Preserving Code Modernization & Extraction**

When invoked with `/human-ui refactor [scope]`:

1. **Safety First**:
   - Verify that test coverage exists for the target scope BEFORE touching code. If tests are absent, author baseline characterization tests first.
   - Run `git status` to ensure a clean working tree.
2. **Strict Invariant: Zero Functional Changes**:
   - Refactoring improves internal structure without altering external observable behavior.
   - Do NOT add new features or modify public API contracts during refactoring.
3. **Execution Steps**:
   - Eliminate code duplication (extract shared utilities or primitives).
   - Decompose giant files (> 300 lines) and giant components (> 150 lines).
   - Simplify complex nested conditional logic using guard clauses or pattern matching.
4. **Validation**:
   - Re-run all existing unit and widget tests after each extraction step.
   - Verify that all tests continue to pass with identical inputs and outputs.
