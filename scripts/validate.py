#!/usr/bin/env python3
"""
Human Flutter Engineering — Master Repository Validation Suite
Runs:
1. Documentation Validator (scripts/validate-docs)
2. Relative Link Validator (scripts/validate-links)
3. Structural & Component Validator (scripts/validate-structure)
4. Absolute Flutter-Only Policy Validator (scripts/validate-flutter-only)
"""

import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(REPO_ROOT, "scripts")

def run_check(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    print(f"\n>>> Running {script_name}...")
    res = subprocess.run([sys.executable, script_path])
    return res.returncode

def main():
    print("==================================================")
    print(" Human Flutter Engineering — Validation Suite     ")
    print("==================================================")

    exit_codes = []
    exit_codes.append(run_check("validate-docs"))
    exit_codes.append(run_check("validate-links"))
    exit_codes.append(run_check("validate-structure"))
    exit_codes.append(run_check("validate-flutter-only"))

    print("\n--------------------------------------------------")
    if any(code != 0 for code in exit_codes):
        print("❌ MASTER VALIDATION FAILED! Review errors above.")
        return 1
    else:
        print("✅ MASTER VALIDATION SUITE PASSED WITH 0 ERRORS!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
