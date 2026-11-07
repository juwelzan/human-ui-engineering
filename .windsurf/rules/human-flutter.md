# Windsurf Cascade Rules — Human Flutter Engineering

This workspace implements the **Human Flutter Engineering** system.

The single authoritative source of truth is [AGENTS.md](../../AGENTS.md).

## Absolute Flutter-Only Rule
- Flutter and Dart are the only supported application development framework.
- Never switch to or recommend React, Next.js, Vue, Angular, React Native, or standalone Kotlin/Swift architectures.
- Native code is allowed ONLY when platform channels or OS APIs require it.

## Chat Command: `/human-flutter` (or `/human-ui`)
- Canonical Skill: [skills/human-flutter/SKILL.md](../../skills/human-flutter/SKILL.md)
- Follow the 18-step workflow in [AGENTS.md](../../AGENTS.md).
- Use `const` constructors, scoped rebuilds, and verify with `flutter test` and `dart analyze`.

## Directory Index
- [Canonical Skill](../../skills/human-flutter/SKILL.md)
- [Design Specifications](../../design/)
- [Component Primitives](../../components/)
- [Engineering Standards](../../engineering/)
- [Quality Gates](../../quality/)
