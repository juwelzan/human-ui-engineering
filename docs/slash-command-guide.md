# Chat Slash Command Guide: `/human-ui`

> **Comprehensive Command Manual for Invoking Human UI Engineering Across AI Coding Agents**

---

## 1. Overview

The `/human-ui` slash command provides direct access to the entire Human UI Engineering system from your agent's chat box.

```text
/human-ui [subcommand?] [task_description]
```

When invoked, the skill:
1. Identifies the requested mode (`plan`, `build`, `design`, `architect`, `debug`, etc.).
2. Inspects your project to identify the framework, design tokens, architecture, and dependencies.
3. Loads only the relevant modular reference documents.
4. Executes the task using professional software engineering standards.
5. Verifies the result against the 13 quality gates and reports exact telemetry.

---

## 2. Complete 16-Command Mode Catalog

| Mode | Invocation Syntax | Purpose & Action Taken |
|---|---|---|
| **General** | `/human-ui [task]` | Full 14-step workflow: discovery, design tokens, shared primitives, view assembly, verification. |
| **Plan** | `/human-ui plan [task]` | Read-only task decomposition, dependency resolution, risk analysis, and ordered milestones. |
| **Build** | `/human-ui build [task]` | End-to-end full-stack feature assembly, models/schemas, business logic, views, and testing. |
| **Design** | `/human-ui design [task]` | UI/UX visual hierarchy, 8pt spatial grid, typography scales, semantic status tokens, WCAG AA contrast. |
| **Architect** | `/human-ui architect [task]` | System architecture evaluation, boundary isolation, and Architecture Decision Record (ADR) drafting. |
| **Audit** | `/human-ui audit [scope]` | Comprehensive UI review, visual polish, layout overflow, accessibility, and performance audit. |
| **Debug** | `/human-ui debug [issue]` | Scientific 10-step root-cause diagnosis, execution path tracing, and smallest safe fix with tests. |
| **Refactor** | `/human-ui refactor [scope]` | Safe, behavior-preserving code extraction, decomposing giant files, zero functional regression. |
| **Test** | `/human-ui test [scope]` | Multi-tier test authoring (Unit, Component, Integration, API, E2E) with honest status reporting. |
| **Review** | `/human-ui review [scope]` | Code review against the 13 pre-flight quality gates, security vulnerabilities, and git cleanliness. |
| **Security** | `/human-ui security [scope]` | Threat modeling, injection/XSS audits, parameterized query verification, and auth token hygiene. |
| **Performance** | `/human-ui performance [scope]`| 16.6ms frame budget profiling, list virtualization, query optimization, and memory leak disposal. |
| **Docs** | `/human-ui docs [scope]` | API documentation, docstrings, OpenAPI contracts, and `PROJECT_CONTEXT.md` updates. |
| **Release** | `/human-ui release [ver?]` | Pre-flight release verification, semantic versioning, zero-downtime DB migrations, and changelog. |
| **Recovery** | `/human-ui recover` | Inspects `AI_TASK_STATE.md` and git telemetry to resume interrupted workflows without restarting. |
| **Status** | `/human-ui status` | Displays active task checkpoint, progress, milestone checklist, and known blockers. |

---

## 3. Concrete Command Examples

```text
# 1. Plan a multi-screen checkout flow without modifying code
/human-ui plan Architect a 3-step payment wizard with Stripe integration.

# 2. Build full-stack feature with database models and UI
/human-ui build Create tenant invite management with Prisma schema and React modal.

# 3. Design accessible tokens and spacing
/human-ui design Establish an 8pt spatial grid and semantic status colors for dark mode.

# 4. Draft an Architecture Decision Record (ADR)
/human-ui architect Evaluate PostgreSQL vs MongoDB for user activity telemetry.

# 5. Scientific Root-Cause Debugging
/human-ui debug The mobile keyboard is obscuring the form submit button in iOS Safari.

# 6. Security Vulnerability Audit
/human-ui security Audit our auth session handling and search for IDOR vulnerabilities.

# 7. Frame Drop & Memory Leak Optimization
/human-ui performance Eliminate scroll jank in our 5,000-item customer data table.

# 8. Resume Interrupted Work
/human-ui recover
```

---

## 4. Related Documentation

- Main Skill: [../skills/human-ui/SKILL.md](../skills/human-ui/SKILL.md)
- Compatibility Matrix: [compatibility-matrix.md](compatibility-matrix.md)
- Installation Guide: [installation-guide.md](installation-guide.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)
