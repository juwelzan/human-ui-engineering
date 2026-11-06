#!/usr/bin/env python3
"""
Human UI Engineering — Master Repository Validation Script
Runs:
1. Documentation Validator (scripts/validate-docs)
2. Relative Link Validator (scripts/validate-links)
3. Structural & Isolation Validator (scripts/validate-structure)
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
    print(" Human UI Engineering — Master Validation Suite   ")
    print("==================================================")

    exit_codes = []
    exit_codes.append(run_check("validate-docs"))
    exit_codes.append(run_check("validate-links"))
    exit_codes.append(run_check("validate-structure"))

    print("\n--------------------------------------------------")
    if any(code != 0 for code in exit_codes):
        print("❌ MASTER VALIDATION FAILED! Review errors above.")
        return 1
    else:
        print("✅ MASTER VALIDATION SUITE PASSED WITH 0 ERRORS!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
