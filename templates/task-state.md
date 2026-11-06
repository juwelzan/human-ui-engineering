# Template: AI Task State (`AI_TASK_STATE.md`)

> Standardized fillable template for tracking execution milestones, checkpoints, and recovery states during multi-turn tasks.

---

```markdown
# AI Task State

- **Task Title**: [Concise Task Description, e.g. "Implement Multi-Step Checkout Flow"]
- **Target Framework**: [e.g. Flutter 3.24 / BLoC, Next.js 15 App Router, Compose]
- **Current Phase**: [Phase 1 to 5 / Workflow Step]
- **Status**: [IN PROGRESS / VERIFIED / BLOCKED]

---

## 1. Completed Milestones
- [x] Step 1-4: Project Discovery, Manifest Audit & Token Inventory
- [x] Step 7-8: Shared Component Primitives created & verified
- [ ] Step 10: Screen layout scaffolding and state controller wiring
- [ ] Step 11: Unit and component test suites passing
- [ ] Step 12: Performance & accessibility audit passing

---

## 2. Active Checkpoint & Working Files
- **Active Step**: [e.g. Wiring CartSummary to CheckoutCubit]
- **Modified / Created Files**:
  - `lib/core/widgets/app_button.dart` (Verified & Passing)
  - `lib/features/checkout/presentation/views/checkout_view.dart` (In progress)
- **Last Verified Checkpoint**: [e.g. Commit SHA or "AppButton test suite passing"]

---

## 3. Failure Diagnosis & Blockers (If Any)
- **Failure Encountered**: [e.g. "None" or describe compiler error / failing assertion]
- **Root Cause Finding**: [e.g. Missing closing bracket or incompatible version]
- **Pivoted Strategy**: [e.g. Swapped library X for native implementation]

---

## 4. Next Safe Action
- **Immediate Next Step**: [e.g. "Implement empty cart state and run widget tests"]
```
