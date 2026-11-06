# Git & Change Management Standards

> **Safe Change Boundaries, Git Discipline & Rollback Protection for AI Agents**

AI coding agents must treat version control as a safeguard, not a scratchpad. Modifying code without respecting git state leads to catastrophic data loss and unrecoverable regressions.

---

## 1. Pre-Change Git Telemetry & Safety Check

Before creating or editing a single file, execute:

```bash
git status --porcelain
```

### Safety Assessment Checklist
- [ ] **Are there uncommitted user changes?** If uncommitted modifications exist in files relevant to your task, inspect the diff (`git diff <file>`). **NEVER overwrite or discard user edits without explicit consent.**
- [ ] **Establish Safe Change Boundaries**: Determine the exact list of files requiring edits. Do not touch unrelated files or trigger mass linters across the entire repository.
- [ ] **Identify the Current Branch & Commit**: Ensure you are operating on the expected branch (`git branch --show-current`) and record the commit hash as your safe fallback point.

---

## 2. Implementation & Diff Review Discipline

1. **Atomic & Coherent Modifications**: Group related changes logically. Do not mix a database migration, an auth refactor, and a CSS tweak into a single messy commit.
2. **Preserve Public API Contracts**: Never rename exported functions, change method signatures, or remove parameters unless explicitly instructed. If an interface must evolve, maintain backward compatibility via optional parameters or deprecation wrappers.
3. **Inspect the Git Diff**: Before finalizing any task, review the staged diff:
   ```bash
   git diff --staged
   ```
   Verify that:
   - No sensitive files (`.env`, credentials, private keys, logs) are staged.
   - No unwanted whitespace-only churn or reformatting touched unrelated files.
   - No temporary debug logs (`console.log`, `print()`, `debugger;`) remain in production paths.

---

## 3. Strict Prohibitions & Destructive Commands

> [!CAUTION]
> **Prohibited Autonomous Actions**:
> - **NEVER** run destructive commands (`git reset --hard`, `git clean -fd`, `git checkout -- .`, `rm -rf`) without explicit, unambiguous user confirmation.
> - **NEVER** execute forced pushes (`git push --force` or `git push -f`) to remote repositories.
> - **NEVER** publish npm/pip/cargo packages or trigger production cloud deployments autonomously.

---

## 4. Rollback Guidance for Risky Operations

When undertaking complex architectural refactoring or schema migrations, provide clear rollback instructions in the task state or chat:

```markdown
> [!NOTE]
> **Rollback Safe Point**: Checkpoint `810ced9`
> If the current migration introduces regressions, safely revert via:
> ```bash
> git restore --staged .
> git checkout <modified_file>
> ```
```

