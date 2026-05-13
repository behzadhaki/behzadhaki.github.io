#!/usr/bin/env python3
"""
Pre-build orchestrator — run before `bundle exec jekyll serve`.

Runs in order:
  1. check_asset_sizes.py   — flag files that are too large for GitHub
  2. generate_permalinks.py — inject missing permalinks into Landing.md files
  3. assets/cv_latex/render_cv.py — rebuild CV PDF and _pages/cv.md
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

SCRIPTS = [
    {
        "label": "Asset size check",
        "path":  REPO / "scripts" / "check_asset_sizes.py",
        "fatal": False,   # warnings are fine, don't abort the chain
    },
    {
        "label": "Permalink generator",
        "path":  REPO / "scripts" / "generate_permalinks.py",
        "fatal": False,   # non-fatal: posts/projects/ may not exist
    },
    {
        "label": "CV render",
        "path":  REPO / "assets" / "cv_latex" / "render_cv.py",
        "fatal": False,   # non-fatal: pdflatex may not be installed
    },
]

SEP = "─" * 60

def run_script(script: dict) -> bool:
    path  = script["path"]
    label = script["label"]

    print(f"\n{SEP}", flush=True)
    print(f"  {label}", flush=True)
    print(SEP, flush=True)

    if not path.exists():
        print(f"  SKIP — script not found: {path.relative_to(REPO)}", flush=True)
        return True

    sys.stdout.flush()
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=REPO,
        stderr=subprocess.DEVNULL,   # suppress env noise (e.g. distutils warnings)
    )

    if result.returncode != 0:
        status = "FAILED" if script["fatal"] else "WARNING (non-fatal)"
        print(f"\n  {status} — exit code {result.returncode}")
        return not script["fatal"]

    return True

def main():
    print(f"\n{'═' * 60}")
    print(f"  Pre-build checks")
    print(f"{'═' * 60}")

    all_ok = True
    for script in SCRIPTS:
        ok = run_script(script)
        if not ok:
            all_ok = False
            print(f"\n  Aborting — fix the error above before serving.")
            sys.exit(1)

    print(f"\n{SEP}")
    print(f"  All checks complete {'✓' if all_ok else '⚠'}")
    print(f"{SEP}\n")

if __name__ == "__main__":
    main()
