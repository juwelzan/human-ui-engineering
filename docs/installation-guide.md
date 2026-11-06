# Human UI Installation & Setup Guide

> Step-by-step instructions for installing, configuring, and updating Human UI Engineering across your development environments.

---

## 1. Quick Installation Overview

Choose the installation method that fits your workflow:

```mermaid
flowchart TD
    Choice{How do you want to install?} -->|Single Project| Sub[Method 1: Git Submodule]
    Choice -->|All Projects Globally| Glob[Method 2: Global Skill Directory]
    Choice -->|Specific Agent Only| Adapt[Method 3: Copy Agent Adapters]
```

---

## 2. Method 1: Git Submodule (Recommended for Teams)

Embed Human UI Engineering directly inside your repository so that all developers and agents share the exact same version:

```bash
# Add as a submodule in your project root
git submodule add https://github.com/juwelzan/human-ui-engineering.git .human-ui

# Setup adapters (creates lightweight symlinks or copies)
mkdir -p .agent/skills .cursor/rules .claude/commands .github/prompts .windsurf/workflows

cp -r .human-ui/.agent/skills/human-ui .agent/skills/
cp .human-ui/.cursor/rules/human-ui.mdc .cursor/rules/
cp .human-ui/.claude/commands/human-ui.md .claude/commands/
cp .human-ui/.github/prompts/human-ui.prompt.md .github/prompts/
cp .human-ui/.windsurf/workflows/human-ui.md .windsurf/workflows/
```

To update to the latest version:
```bash
git submodule update --remote .human-ui
```

---

## 3. Method 2: Global Installation (Single Developer, All Projects)

Install Human UI Engineering in your user home directory so it activates across every project on your machine:

### For Google Antigravity & Gemini CLI
```bash
mkdir -p ~/.gemini/skills
git clone https://github.com/juwelzan/human-ui-engineering.git ~/.gemini/skills/human-ui-engineering
ln -s ~/.gemini/skills/human-ui-engineering/skills/human-ui ~/.gemini/skills/human-ui
```
*Antigravity and Gemini CLI will automatically discover `/human-ui` in all workspaces.*

### For Claude Code
```bash
mkdir -p ~/.claude/commands
cat << 'EOF' > ~/.claude/commands/human-ui.md
---
description: Execute a production-grade UI engineering task using Human UI Engineering.
argument-hint: "[task or instruction]"
---
Follow the instructions at: https://github.com/juwelzan/human-ui-engineering/blob/main/skills/human-ui/SKILL.md
EOF
```

---

## 4. Method 3: Agent-Specific Manual Setup

If you only use one specific IDE or tool, follow its dedicated configuration:

### Cursor Setup
1. Copy `.cursor/rules/human-ui.mdc` into your project's `.cursor/rules/` directory.
2. In Cursor Composer or Chat, type `/human-ui` or mention `@human-ui`.

### VS Code GitHub Copilot Setup
1. Copy `.github/prompts/human-ui.prompt.md` into your project's `.github/prompts/` folder.
2. In GitHub Copilot Chat, type `/human-ui [task]`.

### Windsurf Cascade Setup
1. Copy `.windsurf/workflows/human-ui.md` into `.windsurf/workflows/`.
2. Copy `.windsurf/rules/human-ui.md` into `.windsurf/rules/`.
3. In Cascade, select `/human-ui` from the slash menu.

---

## 5. How to Verify Your Installation

Open your agent's chat window and type:
```text
/human-ui review
```
If properly installed, the agent will acknowledge the Human UI Engineering framework and audit recent UI changes against the release checklist.

---

## 6. Related Documentation

- Main Skill: [../skills/human-ui/SKILL.md](../skills/human-ui/SKILL.md)
- Compatibility Matrix: [compatibility-matrix.md](compatibility-matrix.md)
- Chat Slash Command Guide: [slash-command-guide.md](slash-command-guide.md)
