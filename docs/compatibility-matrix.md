# AI Agent Compatibility Matrix & Invocation Standards

> Comprehensive compatibility matrix and verified configuration paths for invoking Human UI Engineering across all major AI coding agents.

---

## 1. Compatibility Matrix

| Agent / Environment | Skill Discovery Location | Chat Invocation Syntax | Slash Autocomplete | Auto-Activation | Required Configuration | Verified Limitations | Verification Status |
|---|---|---|---|---|---|---|---|
| **Google Antigravity** | `.agent/skills/human-ui/` or `skills/human-ui/` | `/human-ui [task]` | **YES** (Native skill dropdown) | **YES** (Via semantic description) | None (Auto-discovered in workspace) | Requires subagent permissions if spawning specialist subagents | **VERIFIED** |
| **Claude Code** | `.claude/commands/human-ui.md` | `/human-ui [task]` | **YES** (Command autocomplete in CLI) | **YES** (When `CLAUDE.md` is present) | Place `.claude/commands/human-ui.md` | Positional arguments passed via `$ARGUMENTS` string | **VERIFIED** |
| **VS Code GitHub Copilot** | `.github/prompts/human-ui.prompt.md` | `/human-ui [task]` or `#prompt:human-ui` | **YES** (Prompt template menu) | **YES** (Via `.github/copilot-instructions.md`) | VS Code Copilot extension v0.22+ | Reusable prompts require VS Code Chat prompt support | **VERIFIED** |
| **Cursor** | `.cursor/rules/human-ui.mdc` & `.cursor/skills/` | `/human-ui [task]` or `@human-ui` | **YES** (Rule / symbol picker) | **YES** (Global rule match) | Cursor Composer / Chat | Requires typing `@human-ui` or `/` in Composer input | **VERIFIED** |
| **Windsurf** | `.windsurf/workflows/human-ui.md` & `.windsurf/rules/` | `/human-ui [task]` | **YES** (Cascade command list) | **YES** (Cascade system instructions) | None (Auto-discovered in workspace) | Cascade workflow triggers must match frontmatter name | **VERIFIED** |
| **Gemini CLI** | `skills/human-ui/SKILL.md` or `~/.gemini/skills/` | `/human-ui [task]` | **YES** (Agent Skills standard) | **YES** (On UI keywords) | None (Reads workspace `skills/`) | Command line terminal width formatting | **VERIFIED** |
| **Android Studio Gemini Agent** | `.agent/rules/human-ui.md` | `/human-ui [task]` or contextual prompt | **LIMITED** (Context menu attachment) | **YES** (Workspace context) | Android Studio Hedgehog+ with Gemini plugin | Native IDE slash autocomplete depends on plugin version | **VERIFIED WITH LIMITATIONS** |
| **Codex / OpenAI Assistant** | Workspace instructions / system prompt | `/human-ui [task]` | **UNVERIFIED** (No native slash autocomplete) | **YES** (System prompt instruction) | Manual system prompt injection | Generic OpenAI chat lacks custom `/` autocomplete | **UNVERIFIED (MANUAL INJECTION)** |

---

## 2. In-Depth Agent Setup & Discovery Paths

### A. Google Antigravity & Gemini CLI
- **Discovery Paths**:
  - Workspace: `<workspace>/.agent/skills/human-ui/SKILL.md` or `<workspace>/skills/human-ui/SKILL.md`
  - Global: `~/.gemini/skills/human-ui/SKILL.md`
- **How it works**: The agent runtime inspects `name: human-ui` in YAML frontmatter and registers `/human-ui` in the slash autocomplete menu.

### B. Claude Code
- **Discovery Paths**:
  - Workspace: `<workspace>/.claude/commands/human-ui.md`
  - Project config: `<workspace>/CLAUDE.md`
- **How it works**: Claude Code CLI automatically registers any markdown file inside `.claude/commands/` as a slash command (`/filename`).

### C. VS Code GitHub Copilot
- **Discovery Paths**:
  - Workspace: `<workspace>/.github/prompts/human-ui.prompt.md`
  - Workspace: `<workspace>/.github/copilot-instructions.md`
- **How it works**: In VS Code Copilot Chat, typing `/` or looking at prompt templates displays `human-ui`.

### D. Cursor (Composer & Chat)
- **Discovery Paths**:
  - Workspace: `<workspace>/.cursor/rules/human-ui.mdc`
  - Workspace: `<workspace>/.cursor/skills/human-ui/SKILL.md`
- **How it works**: Cursor reads `.cursor/rules/` glob matches and provides symbol mention `@human-ui`.

### E. Windsurf (Cascade)
- **Discovery Paths**:
  - Workspace: `<workspace>/.windsurf/workflows/human-ui.md`
  - Workspace: `<workspace>/.windsurf/rules/human-ui.md`
- **How it works**: Windsurf Cascade surfaces workflows in the chat slash menu.

---

## 3. Verified Limitations & Workarounds

1. **Codex / Standard OpenAI Web Chat**:
   - Standard ChatGPT / Codex interfaces do not support arbitrary custom `/` commands from local repositories without custom GPT actions.
   - **Workaround**: Paste the initial instruction: `"Apply Human UI Engineering rules from skills/human-ui/SKILL.md to the following task: [task]"`
2. **Android Studio Gemini Plugin**:
   - Some older versions of the Gemini in Android Studio plugin only support built-in slash commands (`/generate`, `/explain`).
   - **Workaround**: Include `.agent/rules/human-ui.md` in the project; the agent automatically activates context-driven rules.

---

## 4. Related Documentation

- Main Skill: [../skills/human-ui/SKILL.md](../skills/human-ui/SKILL.md)
- Chat Slash Command Guide: [slash-command-guide.md](slash-command-guide.md)
- Installation Guide: [installation-guide.md](installation-guide.md)
- Master Instructions: [../AGENTS.md](../AGENTS.md)
