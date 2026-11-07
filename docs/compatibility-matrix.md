# AI Agent Compatibility Matrix & Invocation Standards

> Comprehensive compatibility matrix and verified configuration paths for invoking Human Flutter Engineering across all major AI coding agents.

---

## 1. Compatibility Matrix

| Agent / Environment | Skill Discovery Location | Chat Invocation Syntax | Slash Autocomplete | Auto-Activation | Required Configuration | Verified Limitations | Verification Status |
|---|---|---|---|---|---|---|---|
| **Google Antigravity** | `.agents/skills/human-flutter/` or `~/.gemini/config/skills/human-flutter/` | `/human-flutter [task]` | **YES** (Native skill dropdown) | **YES** (Via semantic description) | None (Auto-discovered in workspace) | Requires subagent permissions if spawning specialist subagents | **VERIFIED** |
| **Claude Code** | `.claude/commands/human-flutter.md` | `/human-flutter [task]` | **YES** (Command autocomplete in CLI) | **YES** (When `CLAUDE.md` is present) | Place `.claude/commands/human-flutter.md` | Positional arguments passed via `$ARGUMENTS` string | **VERIFIED** |
| **VS Code GitHub Copilot** | `.github/prompts/human-flutter.prompt.md` | `/human-flutter [task]` | **YES** (Prompt template menu) | **YES** (Via `.github/copilot-instructions.md`) | VS Code Copilot extension v0.22+ | Reusable prompts require VS Code Chat prompt support | **VERIFIED** |
| **Cursor** | `.cursor/rules/human-flutter.mdc` & `.cursor/skills/` | `/human-flutter [task]` or `@human-flutter` | **YES** (Rule / symbol picker) | **YES** (Global rule match) | Cursor Composer / Chat | Requires typing `@human-flutter` or `/` in Composer input | **VERIFIED** |
| **Windsurf** | `.windsurf/workflows/human-flutter.md` & `.windsurf/rules/` | `/human-flutter [task]` | **YES** (Cascade command list) | **YES** (Cascade system instructions) | None (Auto-discovered in workspace) | Cascade workflow triggers must match frontmatter name | **VERIFIED** |
| **Gemini CLI** | `.agents/skills/human-flutter/` or `~/.gemini/config/skills/human-flutter/` | `/human-flutter [task]` | **YES** (Agent Skills standard) | **YES** (On Flutter keywords) | None (Reads workspace or global skills) | Command line terminal width formatting | **VERIFIED** |
| **Android Studio Gemini Agent** | `.agent/rules/human-flutter.md` | `/human-flutter [task]` or contextual prompt | **LIMITED** (Context menu attachment) | **YES** (Workspace context) | Android Studio Hedgehog+ with Gemini plugin | Native IDE slash autocomplete depends on plugin version | **VERIFIED WITH LIMITATIONS** |

---

## 2. In-Depth Agent Setup & Discovery Paths

### A. Google Antigravity & Gemini CLI
- **Discovery Paths**:
  - Workspace: `<workspace>/.agents/skills/human-flutter/SKILL.md`
  - Fallback Workspace: `<workspace>/.agent/skills/human-flutter/SKILL.md`
  - Global: `~/.gemini/config/skills/human-flutter/SKILL.md`
- **How it works**: The Antigravity backend scans `{workspace}/.agents/skills/{skill_name}/SKILL.md`, extracts `name: human-flutter`, and registers `/human-flutter` in the slash autocomplete menu and agent skills catalog.

### B. Claude Code
- **Discovery Paths**:
  - Workspace: `<workspace>/.claude/commands/human-flutter.md`
  - Project config: `<workspace>/CLAUDE.md`
- **How it works**: Claude Code CLI automatically registers any markdown file inside `.claude/commands/` as a slash command (`/filename`).

### C. VS Code GitHub Copilot
- **Discovery Paths**:
  - Workspace: `<workspace>/.github/prompts/human-flutter.prompt.md`
  - Workspace: `<workspace>/.github/copilot-instructions.md`
- **How it works**: In VS Code Copilot Chat, typing `/` or looking at prompt templates displays `human-flutter`.

### D. Cursor (Composer & Chat)
- **Discovery Paths**:
  - Workspace: `<workspace>/.cursor/rules/human-flutter.mdc`
  - Workspace: `<workspace>/.cursor/skills/human-flutter/SKILL.md`
- **How it works**: Cursor reads `.cursor/rules/` glob matches and provides symbol mention `@human-flutter`.

### E. Windsurf (Cascade)
- **Discovery Paths**:
  - Workspace: `<workspace>/.windsurf/workflows/human-flutter.md`
  - Workspace: `<workspace>/.windsurf/rules/human-flutter.md`
- **How it works**: Windsurf Cascade surfaces workflows in the chat slash menu.

---

## 3. Related Documentation

- Main Skill: [../skills/human-flutter/SKILL.md](../skills/human-flutter/SKILL.md)
- Installation Guide: [installation-guide.md](installation-guide.md)
- Command Guide: [slash-command-guide.md](slash-command-guide.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)
