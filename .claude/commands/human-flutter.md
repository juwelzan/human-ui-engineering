---
description: Execute a production-grade Flutter engineering task using Human Flutter Engineering.
argument-hint: "[subcommand] [task or instruction]"
---

You are executing a task using the **Human Flutter Engineering** system.

The single authoritative source of truth is [AGENTS.md](../../AGENTS.md).

## Absolute Flutter-Only Rule
- Flutter and Dart are the only supported application development framework.
- Never switch to or recommend React, Next.js, Vue, Angular, React Native, or standalone Kotlin/Swift architectures.
- Native code is allowed ONLY when platform channels or OS APIs require it.

## Execution Steps
1. Parse the subcommand: `plan`, `build`, `design`, `color`, `component`, `responsive`, `animation`, `performance`, `platform`, `product`, `audit`, `debug`, `refactor`, `test`, `review`, `release`, `recover`, `status`.
2. Load the corresponding reference from [skills/human-flutter/references/](../../skills/human-flutter/references/).
3. Execute the 18-step workflow from [AGENTS.md](../../AGENTS.md).
4. Run `flutter test` and `dart analyze` before reporting completion.
