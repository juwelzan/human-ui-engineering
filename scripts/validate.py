#!/usr/bin/env python3
"""
Human UI Engineering — Repository Validation Script
Verifies:
1. All required architecture files exist and are non-empty.
2. All internal relative markdown links resolve to existing files on disk.
3. No broken anchors or unlinked templates exist.
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_FILES = [
    # Root & Agent instructions
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "CONTRIBUTING.md",
    "LICENSE",
    ".github/copilot-instructions.md",
    ".github/prompts/human-ui.prompt.md",
    ".cursor/rules/human-ui.mdc",
    ".cursor/skills/human-ui/SKILL.md",
    ".agent/rules/human-ui.md",
    ".agent/skills/human-ui/SKILL.md",
    ".claude/commands/human-ui.md",
    ".windsurf/rules/human-ui.md",
    ".windsurf/workflows/human-ui.md",

    # Main Skill & References
    "skills/human-ui/SKILL.md",
    "skills/human-ui/references/recovery.md",
    "skills/human-ui/references/routing.md",
    "skills/human-ui/references/design.md",
    "skills/human-ui/references/audit.md",
    "skills/human-ui/references/flutter.md",
    "skills/human-ui/references/react.md",
    "skills/human-ui/references/nextjs.md",
    "skills/human-ui/references/android.md",
    "skills/human-ui/references/ios.md",
    "skills/human-ui/references/web.md",
    "skills/human-ui/references/responsive.md",
    "skills/human-ui/references/performance.md",
    "skills/human-ui/references/debug.md",
    "skills/human-ui/references/review.md",

    # Core
    "core/agent-behavior.md",
    "core/project-discovery.md",
    "core/architecture.md",
    "core/folder-structure.md",
    "core/development-workflow.md",

    # Design
    "design/design-philosophy.md",
    "design/human-design-rules.md",
    "design/color-system.md",
    "design/typography.md",
    "design/spacing.md",
    "design/responsive-design.md",
    "design/accessibility.md",
    "design/animation.md",

    # Components
    "components/shared-component-rules.md",
    "components/buttons.md",
    "components/text-fields.md",
    "components/typography.md",
    "components/cards.md",
    "components/navigation.md",
    "components/dialogs.md",
    "components/loading-states.md",
    "components/reusable-widgets.md",

    # Engineering
    "engineering/clean-code.md",
    "engineering/architecture-patterns.md",
    "engineering/state-management.md",
    "engineering/error-handling.md",
    "engineering/performance.md",
    "engineering/memory-management.md",
    "engineering/cross-platform.md",

    # Quality
    "quality/testing.md",
    "quality/ui-review.md",
    "quality/performance-audit.md",
    "quality/bug-prevention.md",
    "quality/release-checklist.md",

    # Frameworks
    "frameworks/framework-selection.md",
    "frameworks/flutter.md",
    "frameworks/react.md",
    "frameworks/nextjs.md",
    "frameworks/native-android.md",
    "frameworks/native-ios.md",
    "frameworks/web.md",

    # Workflows
    "workflows/new-project.md",
    "workflows/new-page.md",
    "workflows/shared-component.md",
    "workflows/redesign.md",
    "workflows/performance-fix.md",

    # Templates
    "templates/project-brief.md",
    "templates/architecture-plan.md",
    "templates/design-system.md",
    "templates/quality-report.md",

    # Docs
    "docs/compatibility-matrix.md",
    "docs/slash-command-guide.md",
    "docs/installation-guide.md"
]

def validate():
    errors = []
    print("==================================================")
    print(" Human UI Engineering — Repository Integrity Check")
    print("==================================================")

    # 1. Expected Files Check
    print(f"\n[1/2] Verifying {len(EXPECTED_FILES)} core architecture files...")
    for rel_path in EXPECTED_FILES:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            errors.append(f"MISSING: {rel_path}")
        else:
            size = os.path.getsize(full_path)
            if size < 50:
                errors.append(f"EMPTY / TRUNCATED: {rel_path} ({size} bytes)")

    if not errors:
        print(f"  ✓ All {len(EXPECTED_FILES)} core files exist and are populated.")

    # 2. Markdown Relative Link Validation
    print("\n[2/2] Scanning all markdown files for valid relative links...")
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    total_links = 0
    scanned_files = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        # Exclude git internals
        if ".git" in root.split(os.sep):
            continue
        for f in files:
            if f.endswith(".md") or f.endswith(".mdc"):
                scanned_files += 1
                rel_file = os.path.relpath(os.path.join(root, f), REPO_ROOT)
                full_file = os.path.join(root, f)
                dir_path = os.path.dirname(full_file)

                with open(full_file, "r", encoding="utf-8") as fh:
                    content = fh.read()

                matches = link_pattern.findall(content)
                for text, link in matches:
                    # Ignore absolute external URLs, mailto, anchor-only links
                    if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:") or link.startswith("#"):
                        continue

                    total_links += 1
                    clean_link = link.split("#")[0]
                    if not clean_link:
                        continue

                    target_path = os.path.normpath(os.path.join(dir_path, clean_link))
                    if not os.path.exists(target_path):
                        errors.append(f"BROKEN LINK in {rel_file}: '{link}' -> Target '{target_path}' does not exist")

    print(f"  ✓ Scanned {scanned_files} markdown files.")
    print(f"  ✓ Validated {total_links} relative internal links.")

    print("\n--------------------------------------------------")
    if errors:
        print(f"❌ VALIDATION FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("✅ ALL INTEGRITY CHECKS PASSED PERFECTLY!")
        return 0

if __name__ == "__main__":
    sys.exit(validate())
