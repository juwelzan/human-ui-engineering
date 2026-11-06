# Release Mode Reference (`/human-ui release`)

> **Pre-Flight Release Checks, Semantic Versioning & Deployment Verification**

When invoked with `/human-ui release [version?]`:

1. **Working Tree Verification**:
   - Ensure working tree is clean (`git status`).
   - Verify active branch is `main` or designated release branch.
2. **Execute Full Pre-Flight Gate**:
   - Run type check (`tsc --noEmit`, `mypy`).
   - Run linter (`npm run lint`, `dart analyze`).
   - Run full automated test suite.
   - Run production build command (`npm run build`, `flutter build`).
3. **Changelog & Semantic Versioning**:
   - Update [`../../../CHANGELOG.md`](../../../CHANGELOG.md) with new release version, date, breaking changes, and improvements.
   - Verify semantic version bump (Major/Minor/Patch).
4. **Migration & Deployment Safety**:
   - Check if database migrations follow the expand-and-contract zero-downtime pattern.
   - Outline rollback instructions in the release summary.

