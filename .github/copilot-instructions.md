# GitHub Copilot Instructions — Human Flutter Engineering

You are operating within the **Human Flutter Engineering** system.

The single authoritative source of truth is [`AGENTS.md`](../AGENTS.md).

## Absolute Flutter-Only Rule
- Flutter and Dart are the only supported application development framework.
- Never switch to or recommend React, Next.js, Vue, Angular, React Native, or standalone Kotlin/Swift architectures.
- Native code is allowed ONLY when platform channels or OS APIs require it.

## Execution Directives
1. **Mandatory 18-Step Workflow**: Follow the sequence in [`AGENTS.md`](../AGENTS.md).
2. **Context Discovery**: Read `pubspec.yaml`, dependencies, and active architecture before proposing code.
3. **`const` Constructors**: Use `const` on all immutable widget constructors.
4. **Decomposed Widgets**: Keep widget files under 200 lines; extract private `StatelessWidget` classes.
5. **Verified Quality**: Run `flutter test` and `dart analyze` to verify code.

## Key Directory Links
- [Canonical Skill](../skills/human-flutter/SKILL.md)
- [Design Specifications](../design/)
- [Component Primitives](../components/)
- [Engineering Standards](../engineering/)
- [Quality Gates](../quality/)
